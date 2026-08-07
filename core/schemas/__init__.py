"""
Schemas compartidos — Contratos de datos entre módulos.

Cada módulo usa SOLO los schemas que necesita (ISP).
"""

from core.schemas.contracts import (
    AuditorInput,
    BuilderInput,
    TutorInput,
    AnalysisResult,
    FixResult,
    Finding,
    FixAction,
    ChallengeSpec,
    EvaluationResult,
)

__all__ = [
    "AuditorInput",
    "BuilderInput",
    "TutorInput",
    "AnalysisResult",
    "FixResult",
    "Finding",
    "FixAction",
    "ChallengeSpec",
    "EvaluationResult",
]
