"""
Spec Engine — Motor de Especificación Interactiva.

Simula el proceso mental de un Ingeniero de Software Senior:
1. Escucha la descripción del usuario
2. Identifica lo que entiende y lo que NO
3. Pregunta hasta que todo quede claro
4. Genera un Spec Document aprobado
5. Solo ENTONCES permite generar código

Inspirado en cómo trabaja un buen arquitecto:
"Primero entender, luego diseñar, finalmente construir."
"""

import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from arcana_builder.requirements_engineer import RequirementsEngineer
from arcana_builder.context_analyzer import ContextAnalyzer


@dataclass
class SpecSession:
    """Sesión de especificación en progreso."""

    id: str
    project_name: str
    created_at: str

    # Acumulado de todo lo que el usuario dijo
    raw_inputs: List[str] = field(default_factory=list)

    # Estado del entendimiento
    understood: Dict[str, str] = field(default_factory=dict)
    entities: List[Dict] = field(default_factory=list)
    rules: List[str] = field(default_factory=list)
    roles: List[Dict] = field(default_factory=list)
    out_of_scope: List[str] = field(default_factory=list)

    # Preguntas pendientes
    pending_questions: List[Dict] = field(default_factory=list)
    answered_questions: List[Dict] = field(default_factory=list)

    # Contexto adicional
    regulatory_context: List[str] = field(default_factory=list)
    ux_required: bool = False
    skills_activated: List[str] = field(default_factory=list)

    # Estado
    completeness: float = 0.0
    ready: bool = False
    confirmed: bool = False
    rounds: int = 0

    def all_text(self) -> str:
        """Todo el texto acumulado del usuario."""
        return "\n".join(self.raw_inputs)


class SpecEngine:
    """
    Motor de Especificación Interactiva.

    Proceso:
    1. spec_start(descripción) → análisis + preguntas
    2. spec_answer(respuestas) → actualización + más preguntas (loop)
    3. spec_confirm() → genera Spec Document final
    """

    def __init__(self):
        self._req_engineer = RequirementsEngineer()
        self._ctx_analyzer = ContextAnalyzer()
        self._sessions: Dict[str, SpecSession] = {}

    def spec_start(self, project_name: str, description: str) -> Dict:
        """
        Inicia una sesión de especificación.

        Analiza la descripción inicial y genera las primeras preguntas.
        """
        session_id = f"SPEC-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        session = SpecSession(
            id=session_id,
            project_name=project_name,
            created_at=datetime.now().isoformat(),
        )
        session.raw_inputs.append(description)
        session.rounds = 1

        # Analizar con Requirements Engineer
        req_analysis = self._req_engineer.analyze(description, project_name)
        session.understood = req_analysis.understood
        session.entities = req_analysis.proposed_entities
        session.rules = req_analysis.detected_rules
        session.completeness = req_analysis.completeness

        # Analizar contexto (regulatorio + UX)
        ctx_analysis = self._ctx_analyzer.analyze(
            description, session.entities, session.rules
        )
        if ctx_analysis.needs_regulatory_context:
            for reg in ctx_analysis.regulatory_requirements:
                session.regulatory_context.append(reg.domain)
        session.ux_required = ctx_analysis.needs_ux_process

        # Detectar skills
        try:
            from skills.skill_matcher import SkillMatcher
            matcher = SkillMatcher()
            active_skills = matcher.match(description)
            session.skills_activated = [s.config.name for s in active_skills]
        except Exception:
            pass

        # Generar preguntas (primera ronda)
        questions = self._generate_questions(session, req_analysis, ctx_analysis)
        session.pending_questions = questions

        # Guardar sesión
        self._sessions[session_id] = session

        return self._format_start_response(session)

    def spec_answer(self, session_id: str, answers: str) -> Dict:
        """
        Procesa las respuestas del usuario y genera nuevas preguntas si necesita.
        """
        session = self._sessions.get(session_id)
        if not session:
            return {"error": f"Sesión {session_id} no encontrada."}

        session.raw_inputs.append(answers)
        session.rounds += 1

        # Refinar análisis con las respuestas
        req_analysis = self._req_engineer.analyze(session.all_text(), session.project_name)
        refined = self._req_engineer.refine(req_analysis, answers)

        # Actualizar sesión
        session.understood = refined.understood
        session.entities = refined.proposed_entities
        session.rules = refined.detected_rules
        session.completeness = refined.completeness

        # Extraer roles si los mencionó
        self._extract_roles(answers, session)

        # Detectar si hay nuevas ambigüedades
        ctx_analysis = self._ctx_analyzer.analyze(
            session.all_text(), session.entities, session.rules
        )

        # Mover preguntas respondidas
        session.answered_questions.extend(session.pending_questions)

        # Generar nuevas preguntas (si faltan)
        new_questions = self._generate_followup_questions(session, ctx_analysis)
        session.pending_questions = new_questions

        # Calcular si está listo (completitud >= 85% es suficiente)
        session.ready = session.completeness >= 85

        return self._format_answer_response(session)

    def spec_confirm(self, session_id: str, output_path: str = "./output") -> Dict:
        """
        Genera el Spec Document final Y ejecuta el pipeline BDD→TDD→Plan.

        Flujo automático:
        1. Genera Spec Document (Markdown)
        2. Ejecuta Spec→BDD (genera .feature)
        3. Ejecuta BDD→TDD (genera tests)
        4. Genera Plan de desarrollo (10 pasos)

        Solo se ejecuta si la spec fue aprobada (ready=true).
        """
        session = self._sessions.get(session_id)
        if not session:
            return {"error": f"Sesión {session_id} no encontrada."}

        session.confirmed = True
        spec_document = self._generate_spec_document(session)

        # Ejecutar pipeline automático: Spec → BDD → TDD → Plan
        from arcana_orchestrator.spec_pipeline import run_pipeline_from_spec
        from pathlib import Path

        project_output = Path(output_path) / session.project_name
        pipeline_result = run_pipeline_from_spec(session, project_output)

        # Guardar Spec Document
        docs_dir = project_output / "docs"
        docs_dir.mkdir(parents=True, exist_ok=True)
        (docs_dir / "spec.md").write_text(spec_document, encoding="utf-8")

        return {
            "session_id": session_id,
            "status": "confirmed",
            "spec_document": spec_document,
            "pipeline": pipeline_result,
            "message": (
                "✅ Especificación confirmada.\n"
                f"📋 BDD: {pipeline_result['bdd']['scenarios']} escenarios generados\n"
                f"🧪 TDD: {pipeline_result['tdd']['tests']} tests generados\n"
                f"📐 Plan: {pipeline_result['plan']['steps']} pasos\n"
                f"\nSiguiente: llama a orchestrator_start para comenzar la implementación."
            ),
        }

    # ═══════════════════════════════════════════════════════════════
    # GENERACIÓN DE PREGUNTAS
    # ═══════════════════════════════════════════════════════════════

    def _generate_questions(self, session, req_analysis, ctx_analysis) -> List[Dict]:
        """Genera preguntas iniciales (primera ronda)."""
        questions = []

        # Preguntas del Requirements Engineer
        for q in req_analysis.questions[:5]:
            questions.append(q)

        # Preguntas de contexto regulatorio
        if ctx_analysis.needs_regulatory_context:
            for reg in ctx_analysis.regulatory_requirements:
                for rq in reg.questions[:3]:
                    questions.append({
                        "category": f"regulatory_{reg.domain}",
                        "question": rq,
                        "priority": "high",
                    })

        # Preguntas UX
        if ctx_analysis.needs_ux_process and ctx_analysis.ux_process:
            for uq in ctx_analysis.ux_process.questions[:2]:
                questions.append({
                    "category": "ux",
                    "question": uq["question"],
                    "hint": uq.get("hint", ""),
                    "priority": "medium",
                })

        # Preguntas base que SIEMPRE hacemos si no se respondieron
        base_questions = [
            {"category": "scope", "question": "¿Qué está FUERA de alcance? (qué NO incluye esta versión)", "priority": "medium"},
        ]

        if "Actores" not in session.understood:
            base_questions.insert(0, {
                "category": "actors",
                "question": "¿Quiénes usan el sistema? ¿Qué roles tienen? ¿Qué puede hacer cada uno?",
                "priority": "high",
            })

        for bq in base_questions:
            if not any(q["question"] == bq["question"] for q in questions):
                questions.append(bq)

        return questions[:8]  # Máximo 8 preguntas por ronda

    def _generate_followup_questions(self, session, ctx_analysis) -> List[Dict]:
        """Genera preguntas de seguimiento (rondas 2+)."""
        questions = []

        # Si no tiene roles claros aún
        if not session.roles:
            questions.append({
                "category": "actors",
                "question": "No me quedaron claros los ROLES. ¿Quiénes usan esto y qué permisos tiene cada uno?",
                "priority": "high",
            })

        # Si tiene muchas entidades sin relaciones explícitas
        if len(session.entities) > 2:
            all_text = session.all_text().lower()
            if not any(w in all_text for w in ["pertenece", "tiene", "relación", "asociado"]):
                entity_names = [e["name"] for e in session.entities if e["name"] != "User"]
                if entity_names:
                    questions.append({
                        "category": "entities",
                        "question": f"¿Cómo se relacionan {', '.join(entity_names)}? (ej: un X pertenece a un Y, un Y tiene muchos X)",
                        "priority": "high",
                    })

        # Coherencia
        if ctx_analysis.coherence_issues:
            for issue in ctx_analysis.coherence_issues[:2]:
                questions.append({
                    "category": "coherence",
                    "question": f"Detecté una posible ambigüedad: {issue.description}. {issue.suggestion}",
                    "priority": "high",
                })

        # Si completitud < 85 y ya va ronda 2+, preguntar más específico
        if session.completeness < 85 and session.rounds >= 2:
            if not session.rules:
                questions.append({
                    "category": "rules",
                    "question": "Dame al menos 3 REGLAS de negocio (ej: 'no se puede X', 'siempre debe Y', 'máximo Z')",
                    "priority": "high",
                })

        return questions[:5]  # Máximo 5 por ronda de seguimiento

    # ═══════════════════════════════════════════════════════════════
    # HELPERS
    # ═══════════════════════════════════════════════════════════════

    def _extract_roles(self, text: str, session: SpecSession):
        """Extrae roles del texto."""
        text_lower = text.lower()
        role_keywords = {
            "admin": "Administrador — acceso total",
            "usuario": "Usuario regular — operaciones básicas",
            "gerente": "Gerente — reportes y aprobaciones",
            "vendedor": "Vendedor — operaciones de venta",
            "comprador": "Comprador — operaciones de compra",
            "auditor": "Auditor — solo lectura + logs",
            "empleado": "Empleado — acceso a sus propios datos",
            "jefe": "Jefe — aprobaciones de su departamento",
            "rrhh": "RRHH — gestión de personal",
            "cliente": "Cliente — acceso externo limitado",
        }

        for keyword, desc in role_keywords.items():
            if keyword in text_lower:
                if not any(r.get("name") == keyword for r in session.roles):
                    session.roles.append({"name": keyword, "description": desc})

    def _format_start_response(self, session: SpecSession) -> Dict:
        """Formatea respuesta para spec_start."""
        output = {
            "session_id": session.id,
            "round": session.rounds,
            "completeness": session.completeness,
            "ready": session.ready,
            "understood": session.understood,
            "entities_detected": [
                {"name": e["name"], "fields": e.get("fields", [])}
                for e in session.entities
            ],
            "rules_detected": session.rules,
            "skills_activated": session.skills_activated,
            "regulatory_context": session.regulatory_context,
            "ux_required": session.ux_required,
            "questions": session.pending_questions,
            "message": self._get_status_message(session),
        }
        return output

    def _format_answer_response(self, session: SpecSession) -> Dict:
        """Formatea respuesta para spec_answer."""
        output = {
            "session_id": session.id,
            "round": session.rounds,
            "completeness": session.completeness,
            "ready": session.ready,
            "entities": [
                {"name": e["name"], "fields": e.get("fields", [])}
                for e in session.entities
            ],
            "rules": session.rules,
            "roles": session.roles,
            "questions": session.pending_questions if not session.ready else [],
            "message": self._get_status_message(session),
        }

        if session.ready:
            output["next_step"] = "Llamá orchestrator_spec_confirm para generar el documento de especificación."
        return output

    def _get_status_message(self, session: SpecSession) -> str:
        """Genera mensaje de estado según completitud."""
        if session.completeness >= 85:
            return f"✅ Completitud: {session.completeness:.0f}%. Listo para confirmar. Pero si tenés más detalle, sumalo."
        elif session.completeness >= 60:
            return f"⚠️ Completitud: {session.completeness:.0f}%. Casi listo, pero necesito aclarar las preguntas pendientes."
        else:
            return f"🔴 Completitud: {session.completeness:.0f}%. Necesito mucha más información. Respondé las preguntas."

    def _generate_spec_document(self, session: SpecSession) -> str:
        """Genera el Spec Document final en Markdown."""
        now = datetime.now()
        entities_table = "\n".join(
            f"| {e['name']} | {', '.join(e.get('fields', [])[:6])} | — |"
            for e in session.entities
        )
        rules_list = "\n".join(f"- RN{i:02d}: {r}" for i, r in enumerate(session.rules, 1))
        roles_table = "\n".join(
            f"| {r['name']} | {r['description']} | — |"
            for r in session.roles
        ) if session.roles else "| (Sin roles definidos) | — | — |"

        return f"""# Especificación — {session.project_name}

| Campo | Valor |
|-------|-------|
| **ID** | {session.id} |
| **Fecha** | {now.strftime('%Y-%m-%d %H:%M:%S')} |
| **Rondas de elicitación** | {session.rounds} |
| **Completitud** | {session.completeness:.0f}% |
| **Skills activados** | {', '.join(session.skills_activated) or 'Ninguno'} |
| **Contexto regulatorio** | {', '.join(session.regulatory_context) or 'N/A'} |

---

## 1. Visión General

{session.understood.get('Tipo de sistema', 'Sistema de software')}
Operaciones principales: {session.understood.get('Operaciones', 'No especificadas')}

## 2. Stakeholders y Roles

| Rol | Descripción | Permisos |
|-----|-------------|----------|
{roles_table}

## 3. Entidades del Dominio

| Entidad | Campos | Relaciones |
|---------|--------|------------|
{entities_table}

## 4. Reglas de Negocio

{rules_list if rules_list else '- (Sin reglas definidas)'}

## 5. Restricciones y Validaciones

{chr(10).join(f'- {r}' for r in session.rules if any(w in r.lower() for w in ['único', 'obligatorio', 'no puede', 'máximo', 'mínimo'])) or '- (Derivar de reglas de negocio)'}

## 6. Requerimientos No Funcionales

- Seguridad: OWASP Top 10 aplicado
- Auth: JWT + bcrypt + bloqueo por fuerza bruta
- Datos: Soft delete (recuperables)
- API: REST con OpenAPI/Swagger
{f'- Regulatorio: dominio {", ".join(session.regulatory_context)}' if session.regulatory_context else ''}

## 7. Fuera de Alcance

{chr(10).join(f'- {s}' for s in session.out_of_scope) if session.out_of_scope else '- (Definir con el usuario)'}

---

*Especificación generada por 🔮 Arcana Spec Engineer — {now.strftime('%Y-%m-%d %H:%M:%S')}*
*Aprobada por el usuario: {'Sí' if session.confirmed else 'Pendiente'}*
"""
