"""
Contratos de Arcana — Interfaces que definen la comunicación.

Estos dataclasses son los CONTRATOS entre módulos.
Si un módulo produce un AnalysisResult, cualquier otro
módulo puede consumirlo sin conocer la implementación interna.

Principios:
- ISP: Cada input es mínimo para su módulo
- DIP: Son abstracciones, no implementaciones
- SRP: Cada schema tiene un propósito claro
"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Literal, Optional


# ═══════════════════════════════════════════════════════════════
# AUDITOR — Input NO negociable
# ═══════════════════════════════════════════════════════════════

@dataclass
class AuditorInput:
    """
    Input del Auditor: SOLO el path al código.
    Los criterios NO son negociables.
    """

    project_path: Path
    apply_fix: bool = False  # Opt-in para correcciones
    report_format: Literal["summary", "audit", "full"] = "summary"


# ═══════════════════════════════════════════════════════════════
# BUILDER — Solo historias de usuario + contexto
# ═══════════════════════════════════════════════════════════════

@dataclass
class BuilderInput:
    """
    Input del Builder: QUÉ construir (no CÓMO).
    Los estándares los aplica Arcana internamente.
    """

    project_name: str
    user_stories: List[str]
    business_context: str
    output_path: Path = Path("./output")
    tech_preferences: Optional[str] = None  # Sugerencia, no mandato


# ═══════════════════════════════════════════════════════════════
# TUTOR — Todo configurable
# ═══════════════════════════════════════════════════════════════

@dataclass
class TutorInput:
    """
    Input del Tutor: TODO es configurable por el alumno.
    """

    topic: Literal["owasp", "solid", "tdd", "bdd", "api_resilience", "stress"]
    level: Literal["beginner", "intermediate", "advanced"] = "beginner"
    subtopic: Optional[str] = None  # "A03", "SRP", etc.
    exercise_type: Literal[
        "fix_code", "identify_bug", "write_test",
        "complete_implementation", "code_review", "multiple_choice"
    ] = "fix_code"
    context: Optional[str] = None  # "Soy abogado, usa ejemplos legales"
    hints_enabled: bool = True
    language: str = "es"


# ═══════════════════════════════════════════════════════════════
# RESULTADOS — Outputs compartidos
# ═══════════════════════════════════════════════════════════════

@dataclass
class Finding:
    """Un hallazgo individual (usado por Auditor y Tutor)."""

    id: str
    category: str       # "OWASP-A03", "SOLID-SRP", etc.
    severity: Literal["critical", "high", "medium", "low"]
    description: str
    file_path: str
    line_number: int
    evidence: str       # Código vulnerable/violación
    remediation: str    # Cómo corregirlo
    iso27001_control: Optional[str] = None
    cobit_objective: Optional[str] = None


@dataclass
class AnalysisResult:
    """Resultado de un análisis (output del Auditor)."""

    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    project_path: str = ""
    scores: Dict[str, float] = field(default_factory=dict)
    findings: List[Finding] = field(default_factory=list)
    overall_status: Literal["CONFORME", "NO CONFORME", "PARCIALMENTE CONFORME"] = "NO CONFORME"
    recommendations: List[str] = field(default_factory=list)

    @property
    def critical_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "critical")

    @property
    def is_conforming(self) -> bool:
        return self.overall_status == "CONFORME"


@dataclass
class FixAction:
    """Una corrección individual aplicada."""

    file_path: str
    line_number: int
    original_code: str
    fixed_code: str
    description: str
    category: str
    severity: str


@dataclass
class FixResult:
    """Resultado de la operación de fix (output del Auditor con --fix)."""

    fixes_applied: List[FixAction] = field(default_factory=list)
    fixes_skipped: List[str] = field(default_factory=list)
    files_modified: List[str] = field(default_factory=list)
    pre_scores: Dict[str, float] = field(default_factory=dict)
    post_scores: Dict[str, float] = field(default_factory=dict)

    @property
    def improvement(self) -> Dict[str, float]:
        return {k: self.post_scores.get(k, 0) - v for k, v in self.pre_scores.items()}


# ═══════════════════════════════════════════════════════════════
# TUTOR — Retos y evaluaciones
# ═══════════════════════════════════════════════════════════════

@dataclass
class ChallengeSpec:
    """Especificación de un reto generado por el Tutor."""

    id: str
    topic: str
    subtopic: str
    level: str
    title: str
    description: str           # Instrucciones para el alumno
    bad_code: str              # Código con el problema
    good_code: str             # Solución correcta (oculta)
    hints: List[str]           # Pistas progresivas
    evaluation_criteria: List[str]  # Qué se evalúa
    max_score: int = 10
    time_suggested_minutes: int = 15


@dataclass
class EvaluationResult:
    """Resultado de evaluar la solución del alumno."""

    challenge_id: str
    score: int                  # 0-10
    max_score: int = 10
    passed: bool = False
    feedback: List[str] = field(default_factory=list)
    missing_fixes: List[str] = field(default_factory=list)
    extra_credit: List[str] = field(default_factory=list)
    solution_shown: bool = False
    next_challenge: Optional[str] = None  # Sugerencia de siguiente reto
