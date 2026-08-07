"""
Pipeline Configuration — Carga y validación de configuración YAML.

Principio demostrado: Fail-Fast
La configuración se valida completamente al inicio usando Pydantic.
Si hay errores, el sistema falla inmediatamente con mensajes claros
en lugar de fallar a mitad de ejecución.

ADR-005: Configuración Declarativa con YAML
"""

from pathlib import Path
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field, field_validator


class APIPolicy(BaseModel):
    """Política de resiliencia para una API externa."""

    requests_per_minute: int = Field(ge=1, le=10000, default=60)
    failure_threshold: int = Field(ge=1, le=100, default=5)
    recovery_timeout_seconds: float = Field(ge=1.0, le=300.0, default=30.0)
    max_retries: int = Field(ge=0, le=10, default=3)
    base_delay_seconds: float = Field(ge=0.1, le=60.0, default=1.0)
    max_daily_cost_usd: Optional[float] = Field(ge=0.0, default=None)


class PhaseConfig(BaseModel):
    """Configuración de una fase del pipeline."""

    enabled: bool = True
    agents: List[str] = Field(default_factory=list)
    stop_on_error: bool = True
    timeout_seconds: float = Field(ge=10.0, le=3600.0, default=300.0)


class PipelineConfig(BaseModel):
    """Configuración completa del pipeline de AI-Dev-Guide."""

    # General
    project_name: str = "my-project"
    project_path: Path = Path(".")
    educational_mode: Literal["beginner", "standard", "expert"] = "standard"
    output_format: Literal["rich", "json", "markdown", "plain"] = "rich"

    # Fases
    phases: Dict[str, PhaseConfig] = Field(default_factory=lambda: {
        "design": PhaseConfig(agents=["architecture", "requirements"]),
        "implementation": PhaseConfig(agents=["coder", "tdd"]),
        "testing": PhaseConfig(agents=["bdd", "stress_testing", "api_validation"]),
        "security": PhaseConfig(agents=["owasp", "pentest", "osint"]),
        "quality": PhaseConfig(agents=["ux_quality", "metrics"]),
    })

    # APIs externas
    api_policies: Dict[str, APIPolicy] = Field(default_factory=dict)

    # Umbrales de calidad (ISO 25010/25023)
    quality_thresholds: Dict[str, float] = Field(default_factory=lambda: {
        "code_coverage_min": 80.0,
        "response_time_p95_max_ms": 500.0,
        "vulnerabilities_critical_max": 0,
        "cyclomatic_complexity_max": 10.0,
    })

    @field_validator("project_path")
    @classmethod
    def validate_project_path(cls, v: Path) -> Path:
        """El path del proyecto debe existir si se especifica."""
        if str(v) != "." and not v.exists():
            raise ValueError(f"Project path does not exist: {v}")
        return v

    @classmethod
    def from_yaml(cls, path: Path) -> "PipelineConfig":
        """Carga configuración desde archivo YAML."""
        import yaml

        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")

        with open(path) as f:
            data = yaml.safe_load(f)

        return cls(**data) if data else cls()

    @classmethod
    def default(cls) -> "PipelineConfig":
        """Retorna configuración por defecto (para inicio rápido)."""
        return cls()
