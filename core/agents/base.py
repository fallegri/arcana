"""
Base Agent — Clase abstracta para todos los agentes del sistema.

Principios SOLID demostrados:
- SRP: Define el contrato mínimo de un agente
- LSP: Cualquier subclase es sustituible por BaseAgent
- ISP: Interfaz mínima (execute + validate + report)
- DIP: El orquestador depende de esta abstracción

ISO 42010: Este módulo implementa la "Vista de Desarrollo" del SDD,
definiendo la interfaz común que todos los agentes deben cumplir.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional


@dataclass
class FixAction:
    """Una corrección individual aplicada."""

    file_path: str
    line_number: int
    original_code: str
    fixed_code: str
    description: str
    principle: str  # SOLID letter, OWASP category, etc.
    severity: str   # critical, high, medium, low


@dataclass
class FixResult:
    """Resultado de la operación de auto-fix."""

    agent_name: str
    fixes_applied: List[FixAction] = field(default_factory=list)
    fixes_skipped: List[str] = field(default_factory=list)
    files_modified: List[str] = field(default_factory=list)
    backup_path: Optional[Path] = None

    @property
    def total_fixes(self) -> int:
        return len(self.fixes_applied)

    @property
    def success(self) -> bool:
        return self.total_fixes > 0


@dataclass
class SharedContext:
    """Estado compartido entre agentes durante la ejecución del pipeline."""

    project_path: Path
    phase_results: Dict[str, "AgentOutput"] = field(default_factory=dict)
    metrics: Dict[str, float] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)
    educational_mode: Literal["beginner", "standard", "expert"] = "standard"

    def add_metric(self, name: str, value: float) -> None:
        """Registra una métrica en el contexto compartido."""
        self.metrics[name] = value

    def add_warning(self, message: str) -> None:
        """Registra un warning visible para fases posteriores."""
        self.warnings.append(message)


@dataclass
class AgentInput:
    """Datos de entrada para cualquier agente."""

    phase: str
    project_path: Path
    config: Dict[str, Any]
    context: SharedContext
    previous_results: List["AgentOutput"] = field(default_factory=list)


@dataclass
class AgentOutput:
    """Resultado estandarizado de cualquier agente."""

    agent_name: str
    status: Literal["success", "warning", "error"]
    artifacts: List[Path] = field(default_factory=list)
    metrics: Dict[str, float] = field(default_factory=dict)
    recommendations: List[str] = field(default_factory=list)
    educational_notes: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    @property
    def is_successful(self) -> bool:
        """El agente completó sin errores críticos."""
        return self.status in ("success", "warning")


class BaseAgent(ABC):
    """
    Clase base abstracta para todos los agentes del sistema.

    Cada agente concreto debe implementar:
    - name: Identificador único del agente
    - description: Descripción para el usuario
    - execute(): Lógica principal del agente
    - validate_input(): Validación de precondiciones

    Opcionalmente puede sobreescribir:
    - on_start(): Hook pre-ejecución
    - on_complete(): Hook post-ejecución
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Identificador único del agente."""
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        """Descripción legible del agente para el usuario."""
        ...

    @property
    def phase(self) -> str:
        """Fase del pipeline a la que pertenece el agente."""
        return "unassigned"

    @abstractmethod
    async def execute(self, input_data: AgentInput) -> AgentOutput:
        """
        Ejecuta la lógica principal del agente.

        Args:
            input_data: Datos de entrada con configuración y contexto

        Returns:
            AgentOutput con resultados, métricas y notas educativas
        """
        ...

    def validate_input(self, input_data: AgentInput) -> List[str]:
        """
        Valida que el input cumple las precondiciones del agente.

        Returns:
            Lista de errores de validación (vacía si todo es correcto)
        """
        errors = []
        if not input_data.project_path.exists():
            errors.append(f"Project path does not exist: {input_data.project_path}")
        return errors

    async def on_start(self, input_data: AgentInput) -> None:
        """Hook ejecutado antes de execute(). Override opcional."""
        pass

    async def on_complete(self, output: AgentOutput) -> None:
        """Hook ejecutado después de execute(). Override opcional."""
        pass

    async def fix(self, input_data: AgentInput, analysis: AgentOutput) -> Optional["FixResult"]:
        """
        Aplica correcciones automáticas basadas en el análisis previo.

        Override en subclases que soporten auto-fix.
        Por defecto retorna None (no soporta fix).

        Args:
            input_data: Datos de entrada originales
            analysis: Resultado del execute() con las violaciones detectadas

        Returns:
            FixResult con los cambios aplicados, o None si no soporta fix
        """
        return None

    @property
    def supports_fix(self) -> bool:
        """Indica si este agente puede corregir automáticamente."""
        return False

    async def run(self, input_data: AgentInput) -> AgentOutput:
        """
        Método público que orquesta la ejecución completa del agente.
        NO sobreescribir — usar execute() para la lógica específica.

        Flujo: validate → on_start → execute → on_complete
        """
        # Validación
        validation_errors = self.validate_input(input_data)
        if validation_errors:
            return AgentOutput(
                agent_name=self.name,
                status="error",
                errors=validation_errors,
            )

        # Ejecución
        await self.on_start(input_data)
        output = await self.execute(input_data)
        await self.on_complete(output)

        return output
