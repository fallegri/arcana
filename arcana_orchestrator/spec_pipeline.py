"""
Spec Pipeline — Integrador Spec → BDD → TDD → Plan.

Conecta la cadena completa:
1. Spec Document (confirmado) → extrae entidades, reglas, roles
2. BDD Generator → genera escenarios Gherkin
3. TDD Generator → genera tests pytest derivados de BDD
4. Orchestrator Planner → genera plan de implementación

Este módulo es el "pegamento" que hace que la fusión sea automática.
Cuando el usuario confirma la Spec, todo lo demás se genera en cascada.
"""

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

sys.path.insert(0, str(Path(__file__).parent.parent))

from arcana_orchestrator.spec_to_bdd import SpecToBDD, GeneratedFeature
from arcana_orchestrator.bdd_to_tdd import BDDToTDD
from arcana_orchestrator.planner import Planner
from arcana_orchestrator.spec_engine import SpecSession


@dataclass
class PipelineResult:
    """Resultado del pipeline Spec→BDD→TDD→Plan."""

    # BDD
    features_generated: List[GeneratedFeature] = field(default_factory=list)
    total_scenarios: int = 0

    # TDD
    total_tests: int = 0
    test_files: List[str] = field(default_factory=list)

    # Plan
    plan_steps: int = 0
    plan_id: str = ""

    # General
    output_path: str = ""
    success: bool = False


class SpecPipeline:
    """
    Pipeline completo: Spec → BDD → TDD → Plan.

    Después de que el usuario confirma la Spec via spec_confirm(),
    este pipeline genera automáticamente todo lo necesario para
    que el Orchestrator pueda guiar la implementación.
    """

    def __init__(self):
        self._bdd_gen = SpecToBDD()
        self._tdd_gen = BDDToTDD()
        self._planner = Planner()

    def execute(self, session: SpecSession, output_path: Path) -> PipelineResult:
        """
        Ejecuta el pipeline completo desde una sesión de Spec confirmada.

        Args:
            session: Sesión de Spec con entidades, reglas, roles
            output_path: Dónde generar los archivos

        Returns:
            PipelineResult con métricas de lo generado
        """
        output_path.mkdir(parents=True, exist_ok=True)
        result = PipelineResult(output_path=str(output_path))

        # ═══ PASO 1: Spec → BDD ═══
        features = self._bdd_gen.generate(
            entities=session.entities,
            rules=session.rules,
            roles=session.roles,
            project_name=session.project_name,
            output_path=output_path,
        )
        result.features_generated = features
        result.total_scenarios = sum(f.scenarios_count for f in features)

        # ═══ PASO 2: BDD → TDD ═══
        total_tests = self._tdd_gen.generate(
            entities=session.entities,
            rules=session.rules,
            roles=session.roles,
            project_name=session.project_name,
            output_path=output_path,
        )
        result.total_tests = total_tests
        result.test_files = [
            str(f.relative_to(output_path))
            for f in (output_path / "tests").rglob("test_*.py")
        ]

        # ═══ PASO 3: Generar Plan ═══
        # Construir requirements text desde la sesión
        requirements_text = self._session_to_requirements(session)
        plan = self._planner.create_plan(
            session.project_name,
            requirements_text,
            output_path,
        )
        result.plan_steps = plan.total_steps
        result.plan_id = plan.id

        # Guardar plan
        import json
        plan_path = output_path / "arcana_plan.json"
        plan_path.write_text(
            json.dumps(plan.to_dict(), indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

        result.success = True
        return result

    def _session_to_requirements(self, session: SpecSession) -> str:
        """Convierte la sesión de Spec en texto de requerimientos para el Planner."""
        lines = []

        # Historias de usuario derivadas de entidades
        for entity in session.entities:
            if entity["name"] == "User":
                lines.append("Como usuario quiero registrarme e iniciar sesión de forma segura")
                continue
            name_lower = entity["name"].lower()
            lines.append(f"Como usuario quiero gestionar {name_lower}s (crear, ver, editar, eliminar)")

        # Reglas de negocio
        for rule in session.rules:
            lines.append(rule)

        # Roles/permisos
        if session.roles:
            for role in session.roles:
                lines.append(f"El rol {role['name']} tiene acceso: {role['description']}")

        # Contexto regulatorio
        if session.regulatory_context:
            lines.append(f"Dominio regulado: {', '.join(session.regulatory_context)}")

        return "\n".join(lines)


def run_pipeline_from_spec(session: SpecSession, output_path: Path) -> Dict:
    """
    Función helper para ejecutar el pipeline desde el MCP.

    Returns:
        Dict con métricas para retornar al usuario via MCP
    """
    pipeline = SpecPipeline()
    result = pipeline.execute(session, output_path)

    return {
        "success": result.success,
        "output_path": result.output_path,
        "bdd": {
            "features": len(result.features_generated),
            "scenarios": result.total_scenarios,
            "files": [f.filename for f in result.features_generated],
        },
        "tdd": {
            "tests": result.total_tests,
            "files": result.test_files,
        },
        "plan": {
            "id": result.plan_id,
            "steps": result.plan_steps,
        },
        "message": (
            f"✅ Pipeline Spec→BDD→TDD→Plan completado.\n"
            f"   {result.total_scenarios} escenarios BDD generados\n"
            f"   {result.total_tests} tests TDD generados\n"
            f"   Plan de {result.plan_steps} pasos listo\n"
            f"   Siguiente: orchestrator_start o orchestrator_step"
        ),
    }
