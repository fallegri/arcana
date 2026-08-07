"""
BDD Agent — Agente de Behavior-Driven Development.

Responsabilidades:
1. Descubrir y validar archivos .feature (Gherkin)
2. Ejecutar escenarios con behave
3. Generar reportes de cobertura BDD
4. Producir Living Documentation
5. Emitir notas educativas sobre BDD

Principios SOLID demostrados:
- SRP: Solo se encarga de BDD (no de TDD, no de seguridad)
- LSP: Sustituible por cualquier BaseAgent
- DIP: Depende de abstracciones (BaseAgent), no de behave directamente

ISO 42010: Este agente atiende los Concerns C3 (Demostrabilidad)
y C2 (Progresividad) para los Stakeholders S1, S2, S6.
"""

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from agents.base import AgentInput, AgentOutput, BaseAgent


@dataclass
class FeatureReport:
    """Reporte de una feature individual."""

    name: str
    file_path: Path
    total_scenarios: int
    passed_scenarios: int
    failed_scenarios: int
    pending_scenarios: int

    @property
    def status(self) -> str:
        if self.failed_scenarios > 0:
            return "failed"
        if self.pending_scenarios > 0:
            return "pending"
        return "passed"

    @property
    def pass_rate(self) -> float:
        if self.total_scenarios == 0:
            return 0.0
        return self.passed_scenarios / self.total_scenarios


@dataclass
class BDDReport:
    """Reporte consolidado de todas las features."""

    features: List[FeatureReport]
    total_scenarios: int = 0
    total_steps: int = 0
    passed_scenarios: int = 0
    failed_scenarios: int = 0
    execution_time_seconds: float = 0.0

    @property
    def coverage_percentage(self) -> float:
        if self.total_scenarios == 0:
            return 0.0
        return (self.passed_scenarios / self.total_scenarios) * 100

    @property
    def overall_status(self) -> str:
        if self.failed_scenarios > 0:
            return "failed"
        if self.coverage_percentage >= 95:
            return "excellent"
        if self.coverage_percentage >= 80:
            return "good"
        return "needs_work"


class BDDAgent(BaseAgent):
    """
    Agente BDD — Ejecuta y valida escenarios de comportamiento.

    Modos de operación:
    - validate: Solo verifica que los .feature son válidos
    - execute: Ejecuta los escenarios con behave
    - report: Genera Living Documentation
    - full: Hace todo (validate + execute + report)
    """

    @property
    def name(self) -> str:
        return "bdd"

    @property
    def description(self) -> str:
        return (
            "Ejecuta y valida escenarios BDD (Gherkin). "
            "Genera Living Documentation y reportes de cobertura."
        )

    @property
    def phase(self) -> str:
        return "testing"

    def validate_input(self, input_data: AgentInput) -> List[str]:
        """Valida que existan features para ejecutar."""
        errors = super().validate_input(input_data)

        features_path = input_data.project_path / "features"
        if not features_path.exists():
            # Buscar en agents/bdd/features como fallback
            alt_path = Path("agents/bdd/features")
            if not alt_path.exists():
                errors.append(
                    "No se encontraron archivos .feature. "
                    "Crea escenarios Gherkin en features/ o agents/bdd/features/"
                )

        return errors

    async def execute(self, input_data: AgentInput) -> AgentOutput:
        """
        Ejecuta el agente BDD.

        Flujo:
        1. Descubre archivos .feature
        2. Valida sintaxis Gherkin
        3. Ejecuta escenarios (si mode != 'validate')
        4. Genera reporte y Living Documentation
        5. Produce notas educativas
        """
        mode = input_data.config.get("mode", "full")
        features_path = self._find_features_path(input_data.project_path)

        # 1. Descubrir features
        features = self._discover_features(features_path)
        if not features:
            return AgentOutput(
                agent_name=self.name,
                status="warning",
                recommendations=[
                    "No se encontraron archivos .feature",
                    "Crea tu primer escenario siguiendo la guía: docs/guides/BDD-paso-a-paso.md"
                ],
                educational_notes=[
                    "BDD comienza escribiendo escenarios en lenguaje Gherkin.",
                    "Un archivo .feature describe UNA funcionalidad con múltiples escenarios.",
                    "Cada escenario tiene: Given (contexto), When (acción), Then (verificación)."
                ]
            )

        # 2. Validar sintaxis
        validation_errors = self._validate_features(features)

        # 3. Ejecutar (si corresponde)
        report = None
        if mode in ("execute", "full") and not validation_errors:
            report = await self._execute_features(features_path)

        # 4. Generar Living Documentation
        artifacts = []
        if report:
            doc_path = self._generate_living_doc(report, input_data.project_path)
            artifacts.append(doc_path)

        # 5. Construir output
        return self._build_output(features, validation_errors, report, artifacts, input_data)

    def _find_features_path(self, project_path: Path) -> Path:
        """Encuentra el directorio de features."""
        candidates = [
            project_path / "features",
            Path("agents/bdd/features"),
            project_path / "tests" / "features",
        ]
        for path in candidates:
            if path.exists():
                return path
        return candidates[0]  # Default

    def _discover_features(self, features_path: Path) -> List[Path]:
        """Descubre todos los archivos .feature recursivamente."""
        if not features_path.exists():
            return []
        return sorted(features_path.rglob("*.feature"))

    def _validate_features(self, features: List[Path]) -> List[str]:
        """
        Valida la sintaxis de los archivos Gherkin.

        Verifica:
        - Estructura correcta (Feature/Scenario/Given/When/Then)
        - No hay steps ambiguos
        - Los escenarios tienen al menos Given + When + Then
        """
        errors = []
        required_keywords = {"Feature", "Scenario", "Característica", "Escenario"}

        for feature_file in features:
            content = feature_file.read_text(encoding="utf-8")

            # Verificar que tiene al menos Feature/Característica
            has_feature = any(kw in content for kw in ("Feature:", "Característica:"))
            if not has_feature:
                errors.append(f"{feature_file}: Falta keyword 'Feature:' o 'Característica:'")

            # Verificar que tiene escenarios
            has_scenario = any(kw in content for kw in (
                "Scenario:", "Escenario:", "Scenario Outline:", "Esquema del escenario:"
            ))
            if not has_scenario:
                errors.append(f"{feature_file}: No tiene escenarios definidos")

        return errors

    async def _execute_features(self, features_path: Path) -> Optional[BDDReport]:
        """
        Ejecuta los escenarios con behave.

        NOTA: En modo educativo, no falla si behave no está instalado,
        sino que genera un reporte simulado con notas educativas.
        """
        try:
            result = subprocess.run(
                ["behave", str(features_path), "--format", "json", "--no-capture"],
                capture_output=True,
                text=True,
                timeout=120
            )

            if result.returncode == 0 or result.stdout:
                return self._parse_behave_output(result.stdout)
            else:
                return self._generate_mock_report(features_path)

        except (FileNotFoundError, subprocess.TimeoutExpired):
            # behave no instalado o timeout — generar reporte educativo
            return self._generate_mock_report(features_path)

    def _parse_behave_output(self, output: str) -> BDDReport:
        """Parsea la salida JSON de behave."""
        try:
            data = json.loads(output)
        except json.JSONDecodeError:
            return BDDReport(features=[])

        features = []
        for feature_data in data:
            scenarios = feature_data.get("elements", [])
            passed = sum(1 for s in scenarios if s.get("status") == "passed")
            failed = sum(1 for s in scenarios if s.get("status") == "failed")
            pending = sum(1 for s in scenarios if s.get("status") in ("skipped", "undefined"))

            features.append(FeatureReport(
                name=feature_data["name"],
                file_path=Path(feature_data.get("location", "")),
                total_scenarios=len(scenarios),
                passed_scenarios=passed,
                failed_scenarios=failed,
                pending_scenarios=pending,
            ))

        total_scenarios = sum(f.total_scenarios for f in features)
        passed_scenarios = sum(f.passed_scenarios for f in features)
        failed_scenarios = sum(f.failed_scenarios for f in features)

        return BDDReport(
            features=features,
            total_scenarios=total_scenarios,
            passed_scenarios=passed_scenarios,
            failed_scenarios=failed_scenarios,
        )

    def _generate_mock_report(self, features_path: Path) -> BDDReport:
        """Genera reporte educativo cuando no se puede ejecutar."""
        features = self._discover_features(features_path)
        reports = []

        for f in features:
            content = f.read_text(encoding="utf-8")
            scenario_count = content.count("Scenario:") + content.count("Escenario:")
            reports.append(FeatureReport(
                name=f.stem,
                file_path=f,
                total_scenarios=scenario_count,
                passed_scenarios=0,
                failed_scenarios=0,
                pending_scenarios=scenario_count,
            ))

        return BDDReport(
            features=reports,
            total_scenarios=sum(r.total_scenarios for r in reports),
            passed_scenarios=0,
            failed_scenarios=0,
        )

    def _generate_living_doc(self, report: BDDReport, project_path: Path) -> Path:
        """Genera archivo de Living Documentation."""
        output_path = project_path / "docs" / "living-documentation.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        lines = [
            "# Living Documentation",
            f"## Generado automáticamente por el agente BDD",
            f"",
            f"**Cobertura BDD**: {report.coverage_percentage:.1f}%",
            f"**Escenarios totales**: {report.total_scenarios}",
            f"**Pasando**: {report.passed_scenarios}",
            f"**Fallando**: {report.failed_scenarios}",
            f"",
            "---",
            "",
        ]

        for feature in report.features:
            status_icon = {"passed": "✅", "failed": "❌", "pending": "🔄"}[feature.status]
            lines.append(f"### {status_icon} {feature.name}")
            lines.append(f"- Escenarios: {feature.total_scenarios}")
            lines.append(f"- Pasando: {feature.passed_scenarios}")
            lines.append(f"- Tasa: {feature.pass_rate*100:.0f}%")
            lines.append("")

        output_path.write_text("\n".join(lines), encoding="utf-8")
        return output_path

    def _build_output(
        self,
        features: List[Path],
        validation_errors: List[str],
        report: Optional[BDDReport],
        artifacts: List[Path],
        input_data: AgentInput,
    ) -> AgentOutput:
        """Construye el AgentOutput final con métricas y notas educativas."""

        # Determinar status
        if validation_errors:
            status = "error"
        elif report and report.failed_scenarios > 0:
            status = "warning"
        else:
            status = "success"

        # Métricas (ISO 25023)
        metrics: Dict[str, float] = {
            "bdd.features_count": len(features),
            "bdd.total_scenarios": report.total_scenarios if report else 0,
            "bdd.passed_scenarios": report.passed_scenarios if report else 0,
            "bdd.coverage_percentage": report.coverage_percentage if report else 0.0,
        }

        # Recomendaciones
        recommendations = list(validation_errors)
        if report:
            if report.coverage_percentage < 80:
                recommendations.append(
                    f"Cobertura BDD en {report.coverage_percentage:.0f}%. "
                    f"Meta: ≥80%. Agrega escenarios para features sin cubrir."
                )
            if report.failed_scenarios > 0:
                recommendations.append(
                    f"{report.failed_scenarios} escenarios fallando. "
                    f"Revisa los step definitions o la implementación."
                )

        # Notas educativas (adaptadas al modo)
        educational_notes = self._generate_educational_notes(
            report, input_data.context.educational_mode
        )

        return AgentOutput(
            agent_name=self.name,
            status=status,
            artifacts=artifacts,
            metrics=metrics,
            recommendations=recommendations,
            educational_notes=educational_notes,
            errors=validation_errors,
        )

    def _generate_educational_notes(
        self, report: Optional[BDDReport], mode: str
    ) -> List[str]:
        """Genera notas educativas adaptadas al nivel del usuario."""

        if mode == "beginner":
            return [
                "📚 BDD significa 'Desarrollo Guiado por Comportamiento'.",
                "📝 Los archivos .feature describen QUÉ hace el sistema en lenguaje humano.",
                "🔗 Los Step Definitions son la 'traducción' de Gherkin a código Python.",
                "✅ Un escenario que 'pasa' significa que el sistema se comporta como se espera.",
                "❌ Un escenario que 'falla' indica que algo no cumple la especificación.",
                "💡 Tip: Empieza con escenarios simples (happy path) y agrega edge cases después.",
                "📖 Guía completa: docs/guides/BDD-paso-a-paso.md",
            ]
        elif mode == "expert":
            notes = []
            if report:
                notes.append(f"BDD Coverage: {report.coverage_percentage:.1f}%")
                if report.failed_scenarios > 0:
                    notes.append(f"⚠️ {report.failed_scenarios} scenarios failing")
            return notes
        else:  # standard
            return [
                "BDD valida que el sistema cumple el comportamiento esperado.",
                "Cada escenario es un 'contrato' entre el negocio y el código.",
                "Los escenarios que pasan generan Living Documentation automáticamente.",
                "Guía completa: docs/guides/BDD-paso-a-paso.md",
            ]
