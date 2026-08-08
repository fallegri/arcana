"""
Questionnaire Generator — Genera cuestionarios específicos por stakeholder.

Cada stakeholder recibe preguntas DIFERENTES según su rol y área.
No es un formulario genérico — es una entrevista diseñada por un
Ingeniero de Requisitos Senior para extraer la información precisa
que necesita de esa persona.
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Question:
    """Una pregunta del cuestionario."""
    id: str
    text: str
    type: str  # "open", "choice", "scale", "list", "yes_no"
    category: str  # "process", "data", "rules", "integration", "security"
    required: bool = True
    options: List[str] = field(default_factory=list)  # Para type="choice"
    hint: str = ""
    follow_up: str = ""  # Si responde X, preguntar Y


@dataclass
class Questionnaire:
    """Cuestionario completo para un stakeholder."""
    stakeholder_id: str
    stakeholder_role: str
    stakeholder_area: str
    introduction: str
    questions: List[Question] = field(default_factory=list)
    estimated_time_minutes: int = 15


class QuestionnaireGenerator:
    """Genera cuestionarios adaptados por stakeholder."""

    def generate(self, stakeholder: Dict, project_context: str) -> Questionnaire:
        """
        Genera cuestionario específico para un stakeholder.

        Args:
            stakeholder: Dict con role, area, topics, type
            project_context: Descripción general del proyecto
        """
        role = stakeholder["role"]
        area = stakeholder["area"]
        topics = stakeholder.get("topics", [])
        sh_type = stakeholder.get("type", "informador")

        # Introducción personalizada
        intro = self._generate_intro(role, area, project_context)

        # Preguntas base por topics
        questions = []
        q_id = 1

        for topic in topics:
            topic_questions = self._questions_for_topic(topic, area, sh_type)
            for q in topic_questions:
                q.id = f"Q{q_id:02d}"
                questions.append(q)
                q_id += 1

        # Preguntas transversales (siempre)
        questions.extend(self._transversal_questions(q_id, sh_type))

        return Questionnaire(
            stakeholder_id=stakeholder["id"],
            stakeholder_role=role,
            stakeholder_area=area,
            introduction=intro,
            questions=questions,
            estimated_time_minutes=max(10, len(questions) * 2),
        )

    def format_for_email(self, questionnaire: Questionnaire) -> str:
        """Formatea el cuestionario para enviar por email."""
        lines = [
            f"# Cuestionario — {questionnaire.stakeholder_role}",
            f"## Área: {questionnaire.stakeholder_area}",
            "",
            questionnaire.introduction,
            "",
            f"*Tiempo estimado: {questionnaire.estimated_time_minutes} minutos*",
            "",
            "---",
            "",
        ]

        for q in questionnaire.questions:
            required_mark = " *(obligatorio)*" if q.required else ""
            lines.append(f"### {q.id}. {q.text}{required_mark}")
            if q.hint:
                lines.append(f"*Pista: {q.hint}*")
            if q.type == "choice" and q.options:
                for opt in q.options:
                    lines.append(f"- [ ] {opt}")
            elif q.type == "yes_no":
                lines.append("- [ ] Sí")
                lines.append("- [ ] No")
            elif q.type == "scale":
                lines.append("Escala: 1 (muy bajo) — 5 (muy alto)")
            else:
                lines.append("*Respuesta:*")
                lines.append("")
            lines.append("")

        lines.extend([
            "---",
            "",
            "*Gracias por tu tiempo. Tus respuestas son fundamentales para",
            "diseñar un sistema que se adapte a las necesidades reales del área.*",
            "",
            "*— Generado por 🔮 Arcana PM*",
        ])

        return "\n".join(lines)

    def _generate_intro(self, role: str, area: str, context: str) -> str:
        """Genera introducción personalizada."""
        return (
            f"Estimado/a {role},\n\n"
            f"Estamos relevando información para el desarrollo de un nuevo sistema "
            f"({context[:100]}). Como responsable del área de {area}, tu perspectiva "
            f"es fundamental para asegurar que el sistema cubra las necesidades reales.\n\n"
            f"Te pedimos que respondas las siguientes preguntas con la mayor claridad posible. "
            f"No hay respuestas incorrectas — necesitamos entender cómo trabajás HOY "
            f"para diseñar el sistema del mañana."
        )

    def _questions_for_topic(self, topic: str, area: str, sh_type: str) -> List[Question]:
        """Genera preguntas específicas para un topic."""
        questions = []
        topic_lower = topic.lower()

        # Pregunta principal del topic
        questions.append(Question(
            id="", text=f"Respecto a '{topic}': ¿cómo funciona este proceso actualmente en tu área?",
            type="open", category="process",
            hint="Describí el paso a paso, desde que inicia hasta que termina.",
        ))

        # Preguntas específicas por tipo de topic
        if any(w in topic_lower for w in ["proceso", "flujo", "gestión"]):
            questions.append(Question(
                id="", text=f"¿Cuántas personas participan en este proceso? ¿Quién aprueba?",
                type="open", category="process",
            ))
            questions.append(Question(
                id="", text=f"¿Qué problemas o cuellos de botella tiene este proceso hoy?",
                type="open", category="process",
                hint="Pensá en demoras, errores frecuentes, información que se pierde.",
            ))

        if any(w in topic_lower for w in ["reporte", "informe", "dashboard"]):
            questions.append(Question(
                id="", text=f"¿Qué reportes generás actualmente? ¿Con qué frecuencia?",
                type="open", category="data",
            ))
            questions.append(Question(
                id="", text=f"¿Qué información te FALTA hoy y te gustaría tener?",
                type="open", category="data",
            ))

        if any(w in topic_lower for w in ["seguridad", "acceso", "permiso"]):
            questions.append(Question(
                id="", text=f"¿Quién debe tener acceso a qué información? ¿Hay datos confidenciales?",
                type="open", category="security",
            ))

        if any(w in topic_lower for w in ["integración", "sistema", "herramienta"]):
            questions.append(Question(
                id="", text=f"¿Qué herramientas o sistemas usás hoy para esta función?",
                type="open", category="integration",
                hint="Excel, otro software, papel, email...",
            ))

        return questions

    def _transversal_questions(self, start_id: int, sh_type: str) -> List[Question]:
        """Preguntas que se hacen a TODOS los stakeholders."""
        questions = [
            Question(
                id=f"Q{start_id:02d}",
                text="¿Cuál es la tarea que más tiempo te consume hoy y que un sistema debería automatizar?",
                type="open", category="process", required=True,
            ),
            Question(
                id=f"Q{start_id+1:02d}",
                text="Si pudieras cambiar UNA cosa del proceso actual, ¿cuál sería?",
                type="open", category="process", required=True,
            ),
            Question(
                id=f"Q{start_id+2:02d}",
                text="¿Hay alguna restricción legal o normativa que el sistema deba cumplir en tu área?",
                type="open", category="rules", required=False,
                hint="Leyes, regulaciones, normativa interna, auditorías...",
            ),
        ]

        if sh_type == "decisor":
            questions.append(Question(
                id=f"Q{start_id+3:02d}",
                text="¿Cuál es el presupuesto y plazo esperado para este proyecto?",
                type="open", category="process", required=True,
            ))

        return questions
