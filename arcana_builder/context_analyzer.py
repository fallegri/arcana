"""
Context Analyzer — Validador de Coherencia y Contexto Regulatorio.

Después de la elicitación básica, este módulo:
1. Valida COHERENCIA de las respuestas (contradicciones, ambigüedades)
2. Detecta necesidad de CONTEXTO REGULATORIO (leyes, normas, reglamentos)
3. Detecta necesidad de PROCESO UX (empathy map, buyer persona, user journey)
4. Solicita BIBLIOGRAFÍA o fuentes cuando el dominio lo requiere
5. Genera requerimientos adicionales derivados del contexto

Dominios que activan contexto regulatorio:
- Asistencia/RRHH → legislación laboral, convenios colectivos
- Salud → regulaciones sanitarias, protección de datos médicos
- Finanzas → normativas bancarias, lavado de dinero
- Educación → reglamentos académicos, acreditación
- Legal → códigos procesales, plazos legales
- Alimentos → normativas bromatológicas, HACCP
- Comercio electrónico → defensa del consumidor, facturación electrónica

Dominios que activan proceso UX completo:
- Cualquier sistema con interfaz de usuario final
- Apps móviles, web apps, kioscos
- Sistemas de atención al público
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class CoherenceIssue:
    """Un problema de coherencia detectado."""
    type: str  # "contradiction", "ambiguity", "incomplete", "unrealistic"
    description: str
    suggestion: str


@dataclass
class RegulatoryRequirement:
    """Un requisito regulatorio detectado."""
    domain: str           # "laboral", "salud", "finanzas", etc.
    regulation: str       # Nombre de la ley/norma
    description: str      # Qué implica para el sistema
    questions: List[str]  # Preguntas específicas al usuario
    bibliography: List[str] = field(default_factory=list)


@dataclass
class UXProcess:
    """Proceso UX requerido."""
    artifacts_needed: List[str]  # empathy_map, buyer_persona, user_journey, etc.
    questions: List[Dict[str, str]]
    bibliography: List[str]


@dataclass
class ContextAnalysis:
    """Resultado del análisis de contexto."""
    coherence_issues: List[CoherenceIssue] = field(default_factory=list)
    regulatory_requirements: List[RegulatoryRequirement] = field(default_factory=list)
    ux_process: Optional[UXProcess] = None
    additional_questions: List[Dict[str, str]] = field(default_factory=list)
    bibliography_needed: List[Dict[str, str]] = field(default_factory=list)
    is_coherent: bool = True
    needs_regulatory_context: bool = False
    needs_ux_process: bool = False


class ContextAnalyzer:
    """
    Analiza coherencia y contexto regulatorio/UX.

    Se ejecuta DESPUÉS del Requirements Engineer y ANTES del Builder.
    Agrega una capa de validación que asegura que no se genere un
    sistema sin considerar el contexto legal, normativo o de UX.
    """

    # Dominios que requieren contexto regulatorio
    REGULATORY_DOMAINS = {
        "asistencia": {
            "domain": "laboral",
            "triggers": ["asistencia", "horario", "turno", "jornada", "vacacion",
                         "licencia", "ausencia", "tardanza", "horas extra", "fichaje"],
            "regulations": [
                "Legislación laboral del país (jornada máxima, descansos obligatorios)",
                "Convenio colectivo de trabajo aplicable",
                "Reglamento interno de la empresa",
                "Normativa de registro de jornada (fichaje obligatorio)",
            ],
            "questions": [
                "¿En qué país/jurisdicción opera? (para legislación laboral aplicable)",
                "¿Cuál es la jornada laboral legal máxima? (ej: 8h diarias, 48h semanales)",
                "¿Hay turnos rotativos? ¿Cuáles?",
                "¿Qué tipos de licencia/ausencia maneja? (enfermedad, vacaciones, maternidad...)",
                "¿Existe convenio colectivo? ¿Tiene reglas especiales de horas extra?",
                "¿El fichaje es obligatorio por ley en tu jurisdicción?",
                "¿Hay tolerancia de minutos para llegada tardía? ¿Cuántos?",
            ],
            "bibliography": [
                "Ley de Contrato de Trabajo (o equivalente del país)",
                "Convenio Colectivo de Trabajo aplicable al sector",
                "Normativa de Registro de Jornada Laboral vigente",
                "Reglamento interno de la empresa (si existe)",
            ],
        },
        "salud": {
            "domain": "salud",
            "triggers": ["paciente", "historia clínica", "diagnóstico", "receta médica",
                         "turno médico", "consultorio", "hospital", "clínica", "laboratorio"],
            "regulations": [
                "Ley de protección de datos de salud (HIPAA / equivalente local)",
                "Normativa de historia clínica electrónica",
                "Regulación de recetas médicas electrónicas",
                "Normativa de consentimiento informado",
            ],
            "questions": [
                "¿En qué país opera? (para normativa de datos de salud)",
                "¿Qué datos sensibles de pacientes se manejan?",
                "¿Se requiere consentimiento informado electrónico?",
                "¿Hay integración con sistemas de obras sociales/seguros?",
                "¿Se manejan recetas médicas electrónicas?",
                "¿Hay requisitos de retención de datos (años)?",
            ],
            "bibliography": [
                "HIPAA (USA) o Ley de Protección de Datos de Salud local",
                "Normativa de Historia Clínica Electrónica del país",
                "Guía de Seguridad de Datos de Salud (ISO 27799)",
            ],
        },
        "finanzas": {
            "domain": "finanzas",
            "triggers": ["banco", "transacción", "cuenta", "tarjeta", "crédito",
                         "préstamo", "inversión", "bolsa", "trading", "pago"],
            "regulations": [
                "Normativa bancaria del país (Banco Central)",
                "Ley de prevención de lavado de dinero",
                "Regulación de medios de pago electrónicos",
                "Normativa PCI-DSS (datos de tarjetas)",
            ],
            "questions": [
                "¿En qué jurisdicción financiera opera?",
                "¿Maneja datos de tarjetas de crédito? (requiere PCI-DSS)",
                "¿Hay requisitos de KYC (Know Your Customer)?",
                "¿Cuál es el monto máximo por transacción?",
                "¿Se requiere doble factor de autenticación para operaciones?",
                "¿Hay requisitos de auditoría financiera (SOX, etc.)?",
            ],
            "bibliography": [
                "Normativa del Banco Central / Regulador financiero local",
                "Ley de Prevención de Lavado de Activos",
                "PCI-DSS v4.0 (si maneja datos de tarjetas)",
                "ISO 27001 Anexo A (controles financieros)",
            ],
        },
        "educacion": {
            "domain": "educación",
            "triggers": ["alumno", "estudiante", "calificación", "nota", "materia",
                         "asignatura", "profesor", "docente", "matrícula", "examen"],
            "regulations": [
                "Reglamento académico institucional",
                "Normativa de evaluación y promoción",
                "Ley de protección de datos de menores (si aplica)",
                "Normativa de accesibilidad educativa",
            ],
            "questions": [
                "¿Es educación primaria, secundaria, superior o corporativa?",
                "¿Cuál es el sistema de calificación? (1-10, A-F, porcentaje...)",
                "¿Hay requisitos de asistencia mínima para aprobar?",
                "¿Se manejan datos de menores de edad? (requiere protección especial)",
                "¿Hay normativa de accesibilidad que cumplir?",
                "¿El sistema debe integrarse con alguna plataforma educativa existente?",
            ],
            "bibliography": [
                "Reglamento Académico de la institución",
                "Normativa de evaluación y promoción vigente",
                "Ley de Protección de Datos Personales (especial para menores)",
            ],
        },
        "legal": {
            "domain": "legal",
            "triggers": ["expediente", "caso", "demanda", "juicio", "sentencia",
                         "abogado", "juzgado", "plazo procesal", "notificación judicial"],
            "regulations": [
                "Código Procesal aplicable (civil, penal, laboral)",
                "Normativa de expediente electrónico judicial",
                "Plazos procesales obligatorios",
                "Normativa de secreto profesional",
            ],
            "questions": [
                "¿Qué fuero(s)? (civil, penal, laboral, comercial...)",
                "¿Hay plazos procesales que el sistema deba alertar?",
                "¿Se maneja información bajo secreto profesional?",
                "¿El sistema debe calcular plazos hábiles/inhábiles?",
                "¿Hay integración con sistemas judiciales electrónicos?",
            ],
            "bibliography": [
                "Código Procesal aplicable al fuero",
                "Normativa de Expediente Judicial Electrónico",
                "Ley de Ejercicio Profesional de la Abogacía",
            ],
        },
        "ecommerce": {
            "domain": "comercio electrónico",
            "triggers": ["tienda", "carrito", "checkout", "envío", "delivery",
                         "e-commerce", "marketplace", "catálogo", "compra online"],
            "regulations": [
                "Ley de defensa del consumidor",
                "Normativa de facturación electrónica",
                "Regulación de comercio electrónico",
                "Normativa de protección de datos personales",
            ],
            "questions": [
                "¿En qué países vende? (para normativa de consumidor)",
                "¿Requiere facturación electrónica? ¿Qué sistema (AFIP, SAT, SII...)?",
                "¿Cuál es la política de devoluciones? (por ley pueden ser obligatorias)",
                "¿Maneja datos de tarjeta o usa pasarela externa?",
                "¿Hay requisitos de accesibilidad web (WCAG)?",
            ],
            "bibliography": [
                "Ley de Defensa del Consumidor aplicable",
                "Normativa de Facturación Electrónica del país",
                "Regulación de Comercio Electrónico",
                "WCAG 2.1 (accesibilidad web)",
            ],
        },
    }

    # Triggers para proceso UX completo
    UX_TRIGGERS = [
        "interfaz", "usuario final", "app", "aplicación", "web", "móvil",
        "portal", "dashboard", "pantalla", "formulario", "cliente",
        "experiencia", "usabilidad", "ux", "ui", "diseño",
        "kiosco", "totem", "atención al público",
    ]

    def analyze(self, user_input: str, entities: List[Dict], rules: List[str]) -> ContextAnalysis:
        """
        Analiza coherencia y detecta necesidad de contexto adicional.

        Args:
            user_input: Todo lo que el usuario ha dicho (original + respuestas)
            entities: Entidades detectadas hasta ahora
            rules: Reglas de negocio detectadas

        Returns:
            ContextAnalysis con issues, requerimientos regulatorios, y proceso UX
        """
        analysis = ContextAnalysis()

        # 1. Validar coherencia
        analysis.coherence_issues = self._check_coherence(user_input, entities, rules)
        analysis.is_coherent = len(analysis.coherence_issues) == 0

        # 2. Detectar necesidad regulatoria
        analysis.regulatory_requirements = self._detect_regulatory_needs(user_input)
        analysis.needs_regulatory_context = len(analysis.regulatory_requirements) > 0

        # 3. Detectar necesidad de proceso UX
        if self._needs_ux_process(user_input):
            analysis.ux_process = self._generate_ux_process(user_input, entities)
            analysis.needs_ux_process = True

        # 4. Compilar bibliografía necesaria
        analysis.bibliography_needed = self._compile_bibliography(analysis)

        # 5. Generar preguntas adicionales
        analysis.additional_questions = self._generate_context_questions(analysis)

        return analysis

    def generate_context_report(self, analysis: ContextAnalysis) -> str:
        """Genera reporte formateado del análisis de contexto."""
        lines = [
            "## 🔮 Arcana — Análisis de Contexto y Coherencia",
            "",
        ]

        # Coherencia
        if analysis.coherence_issues:
            lines.append("### ⚠️ Problemas de Coherencia Detectados")
            lines.append("")
            for issue in analysis.coherence_issues:
                icon = {"contradiction": "🔴", "ambiguity": "🟡",
                        "incomplete": "🟠", "unrealistic": "🔴"}.get(issue.type, "⚪")
                lines.append(f"- {icon} **{issue.type.upper()}**: {issue.description}")
                lines.append(f"  *Sugerencia: {issue.suggestion}*")
            lines.append("")
        else:
            lines.append("### ✅ Coherencia: Sin contradicciones detectadas")
            lines.append("")

        # Contexto regulatorio
        if analysis.needs_regulatory_context:
            lines.append("### 📜 Contexto Regulatorio Necesario")
            lines.append("")
            lines.append("El sistema que describís opera en un dominio **regulado**.")
            lines.append("Necesito información adicional para cumplir con la normativa:")
            lines.append("")

            for reg in analysis.regulatory_requirements:
                lines.append(f"#### 📋 Dominio: {reg.domain.upper()}")
                lines.append("")
                lines.append("**Regulaciones aplicables:**")
                for r in reg.regulation if isinstance(reg.regulation, list) else [reg.regulation]:
                    lines.append(f"- {r}")
                lines.append("")
                lines.append("**Preguntas sobre regulación:**")
                for q in reg.questions:
                    lines.append(f"- ❓ {q}")
                lines.append("")
                if reg.bibliography:
                    lines.append("**📚 Bibliografía/Fuentes necesarias:**")
                    for b in reg.bibliography:
                        lines.append(f"- 📖 {b}")
                    lines.append("")

        # Proceso UX
        if analysis.needs_ux_process:
            lines.append("### 🎨 Proceso UX Requerido")
            lines.append("")
            lines.append("El sistema tiene interacción directa con usuarios finales.")
            lines.append("Se recomienda completar el proceso UX antes de implementar:")
            lines.append("")
            lines.append("**Artefactos UX necesarios:**")
            for artifact in analysis.ux_process.artifacts_needed:
                lines.append(f"- 📐 {artifact}")
            lines.append("")
            lines.append("**Preguntas para el proceso UX:**")
            for q in analysis.ux_process.questions:
                lines.append(f"- ❓ {q['question']}")
                if q.get("hint"):
                    lines.append(f"  *{q['hint']}*")
            lines.append("")
            if analysis.ux_process.bibliography:
                lines.append("**📚 Bibliografía UX recomendada:**")
                for b in analysis.ux_process.bibliography:
                    lines.append(f"- 📖 {b}")
                lines.append("")

        # Bibliografía compilada
        if analysis.bibliography_needed:
            lines.append("### 📚 Bibliografía y Fuentes Requeridas")
            lines.append("")
            lines.append("Para generar un sistema completo y correcto, necesito que consultes")
            lines.append("o me proporciones información de estas fuentes:")
            lines.append("")
            for bib in analysis.bibliography_needed:
                lines.append(f"- 📖 **{bib['source']}** — {bib['reason']}")
            lines.append("")

        return "\n".join(lines)

    # ═══════════════════════════════════════════════════════════════
    # COHERENCIA
    # ═══════════════════════════════════════════════════════════════

    def _check_coherence(self, text: str, entities: List[Dict], rules: List[str]) -> List[CoherenceIssue]:
        """Detecta problemas de coherencia."""
        issues = []
        text_lower = text.lower()

        # Contradicción: "no necesita auth" + "solo admin puede..."
        if "no necesita" in text_lower and "autenticación" in text_lower:
            if any("solo" in r.lower() and any(w in r.lower() for w in ["admin", "usuario", "rol"]) for r in rules):
                issues.append(CoherenceIssue(
                    type="contradiction",
                    description="Dijiste que no necesita autenticación, pero hay reglas que dependen de roles",
                    suggestion="Aclará: ¿necesita login o no? Si hay roles, necesita auth.",
                ))

        # Ambigüedad: menciona "rápido" sin definir qué es rápido
        if any(w in text_lower for w in ["rápido", "veloz", "instantáneo"]) and not any(w in text_lower for w in ["ms", "segundo", "milisegundo"]):
            issues.append(CoherenceIssue(
                type="ambiguity",
                description="Se menciona que debe ser 'rápido' pero no se define un tiempo concreto",
                suggestion="Definí un tiempo máximo aceptable (ej: <200ms, <2 segundos)",
            ))

        # Incompleto: muchas entidades pero pocas relaciones mencionadas
        if len(entities) > 3 and not any(w in text_lower for w in ["pertenece", "tiene", "relación", "asociado", "vinculado"]):
            issues.append(CoherenceIssue(
                type="incomplete",
                description=f"Hay {len(entities)} entidades pero no se especificaron relaciones entre ellas",
                suggestion="Describí cómo se relacionan: ¿un cliente tiene muchos pedidos? ¿un producto pertenece a una categoría?",
            ))

        # Unrealistic: "tiempo real" + "gratis" + "millones de usuarios"
        unrealistic_combos = [
            (["millones", "ilimitad"], ["gratis", "sin costo", "económic"]),
            (["tiempo real"], ["sin servidor", "serverless"]),
        ]
        for ambitious, limiting in unrealistic_combos:
            if any(w in text_lower for w in ambitious) and any(w in text_lower for w in limiting):
                issues.append(CoherenceIssue(
                    type="unrealistic",
                    description="La combinación de requerimientos puede ser técnicamente difícil de lograr",
                    suggestion="Revisá las expectativas de escala vs. presupuesto/infraestructura",
                ))

        return issues

    # ═══════════════════════════════════════════════════════════════
    # REGULATORIO
    # ═══════════════════════════════════════════════════════════════

    def _detect_regulatory_needs(self, text: str) -> List[RegulatoryRequirement]:
        """Detecta si el dominio requiere contexto regulatorio."""
        text_lower = text.lower()
        requirements = []

        for domain_key, domain_data in self.REGULATORY_DOMAINS.items():
            triggers = domain_data["triggers"]
            if any(trigger in text_lower for trigger in triggers):
                requirements.append(RegulatoryRequirement(
                    domain=domain_data["domain"],
                    regulation=domain_data["regulations"],
                    description=f"Sistema en dominio {domain_data['domain']} — requiere contexto normativo",
                    questions=domain_data["questions"],
                    bibliography=domain_data["bibliography"],
                ))

        return requirements

    # ═══════════════════════════════════════════════════════════════
    # PROCESO UX
    # ═══════════════════════════════════════════════════════════════

    def _needs_ux_process(self, text: str) -> bool:
        """Determina si se necesita proceso UX completo."""
        text_lower = text.lower()
        return any(trigger in text_lower for trigger in self.UX_TRIGGERS)

    def _generate_ux_process(self, text: str, entities: List[Dict]) -> UXProcess:
        """Genera el proceso UX necesario."""
        artifacts = [
            "Mapa de Empatía (Empathy Map) — para cada tipo de usuario",
            "Buyer Persona / User Persona — perfil detallado del usuario objetivo",
            "User Journey Map — recorrido del usuario por el sistema",
            "Information Architecture — estructura de navegación",
            "Wireframes de baja fidelidad — esquemas de pantallas principales",
            "Criterios de usabilidad (ISO 9241-110) — los 7 principios aplicados",
        ]

        questions = [
            {
                "question": "¿Quién es tu usuario PRINCIPAL? Describilo: edad, profesión, nivel técnico, frustraciones",
                "hint": "Esto genera el Buyer Persona",
            },
            {
                "question": "¿Qué PROBLEMA le resuelve tu sistema al usuario? ¿Qué dolor tiene HOY sin el sistema?",
                "hint": "Esto alimenta el Mapa de Empatía (sección 'Pains')",
            },
            {
                "question": "¿Cuál es la TAREA más importante que el usuario hace en el sistema? Describí paso a paso",
                "hint": "Esto genera el User Journey Map",
            },
            {
                "question": "¿El usuario es técnico o no técnico? ¿Cuánto tiempo tiene para aprender?",
                "hint": "Define el nivel de complejidad de la interfaz",
            },
            {
                "question": "¿Hay usuarios con discapacidades que deban poder usar el sistema? (visual, motora, cognitiva)",
                "hint": "Activa requisitos de accesibilidad ISO 9241-171",
            },
            {
                "question": "¿En qué CONTEXTO se usa? (oficina, campo, móvil en la calle, con guantes, con prisa...)",
                "hint": "El contexto define restricciones de diseño",
            },
        ]

        bibliography = [
            "Don Norman — 'The Design of Everyday Things' (principios de diseño)",
            "Steve Krug — 'Don't Make Me Think' (usabilidad web)",
            "ISO 9241-110:2020 — Principios de interacción",
            "ISO 9241-210:2019 — Diseño centrado en el humano",
            "Alan Cooper — 'About Face' (diseño de interacción)",
            "Aarron Walter — 'Designing for Emotion' (diseño emocional)",
            "WCAG 2.1 — Web Content Accessibility Guidelines (accesibilidad)",
        ]

        return UXProcess(
            artifacts_needed=artifacts,
            questions=questions,
            bibliography=bibliography,
        )

    # ═══════════════════════════════════════════════════════════════
    # BIBLIOGRAFÍA
    # ═══════════════════════════════════════════════════════════════

    def _compile_bibliography(self, analysis: ContextAnalysis) -> List[Dict[str, str]]:
        """Compila toda la bibliografía necesaria."""
        bibliography = []

        for reg in analysis.regulatory_requirements:
            for bib in reg.bibliography:
                bibliography.append({
                    "source": bib,
                    "reason": f"Requerido por dominio: {reg.domain}",
                })

        if analysis.ux_process:
            for bib in analysis.ux_process.bibliography:
                bibliography.append({
                    "source": bib,
                    "reason": "Proceso UX requerido",
                })

        return bibliography

    def _generate_context_questions(self, analysis: ContextAnalysis) -> List[Dict[str, str]]:
        """Compila preguntas adicionales del contexto."""
        questions = []

        for reg in analysis.regulatory_requirements:
            for q in reg.questions:
                questions.append({
                    "category": f"regulatory_{reg.domain}",
                    "question": q,
                    "priority": "high",
                })

        if analysis.ux_process:
            for q in analysis.ux_process.questions:
                questions.append({
                    "category": "ux",
                    "question": q["question"],
                    "priority": "medium",
                })

        return questions
