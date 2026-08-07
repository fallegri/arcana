"""
Pipeline Engine — Motor de ejecución del pipeline de desarrollo.

Este módulo coordina la ejecución secuencial de fases y agentes.
Es el "corazón" del orquestador.

Principios SOLID demostrados:
- SRP: Solo orquesta, no implementa lógica de agentes
- OCP: Nuevas fases/agentes no requieren modificar este código
- DIP: Depende de BaseAgent (abstracción) via AgentRegistry

ISO 42010 — Vista Funcional: Este módulo implementa el flujo
principal descrito en la Sección 2.1 del SDD.
"""

import asyncio
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from agents.base import AgentInput, AgentOutput, BaseAgent, SharedContext
from agents.registry import AgentRegistry
from orchestrator.config import PipelineConfig


@dataclass
class PhaseResult:
    """Resultado de una fase completa del pipeline."""

    phase_name: str
    agent_outputs: List[AgentOutput] = field(default_factory=list)
    skipped: bool = False
    skip_reason: Optional[str] = None

    @property
    def is_successful(self) -> bool:
        """La fase fue exitosa si todos sus agentes lo fueron."""
        if self.skipped:
            return True
        return all(output.is_successful for output in self.agent_outputs)

    @property
    def total_metrics(self) -> Dict[str, float]:
        """Métricas combinadas de todos los agentes de la fase."""
        metrics: Dict[str, float] = {}
        for output in self.agent_outputs:
            metrics.update(output.metrics)
        return metrics


@dataclass
class PipelineResult:
    """Resultado completo de la ejecución del pipeline."""

    phase_results: List[PhaseResult] = field(default_factory=list)
    overall_status: str = "not_started"
    total_duration_seconds: float = 0.0

    @property
    def is_successful(self) -> bool:
        return all(pr.is_successful for pr in self.phase_results)

    @property
    def all_metrics(self) -> Dict[str, float]:
        metrics: Dict[str, float] = {}
        for pr in self.phase_results:
            metrics.update(pr.total_metrics)
        return metrics

    @property
    def all_recommendations(self) -> List[str]:
        recs: List[str] = []
        for pr in self.phase_results:
            for output in pr.agent_outputs:
                recs.extend(output.recommendations)
        return recs


class Pipeline:
    """
    Motor de ejecución del pipeline de desarrollo.

    Responsabilidades:
    1. Cargar configuración y validarla
    2. Resolver qué agentes ejecutar en qué orden
    3. Ejecutar cada fase pasando contexto entre agentes
    4. Recopilar resultados y métricas
    5. Decidir si continuar o parar ante errores
    """

    def __init__(self, config: PipelineConfig, registry: AgentRegistry) -> None:
        self._config = config
        self._registry = registry
        self._context = SharedContext(
            project_path=config.project_path,
            educational_mode=config.educational_mode,
        )

    async def run(self, phases: Optional[List[str]] = None) -> PipelineResult:
        """
        Ejecuta el pipeline completo o fases seleccionadas.

        Args:
            phases: Lista de fases a ejecutar (None = todas las habilitadas)

        Returns:
            PipelineResult con todos los resultados y métricas
        """
        import time

        start_time = time.monotonic()
        result = PipelineResult(overall_status="running")

        # Determinar fases a ejecutar
        target_phases = phases or list(self._config.phases.keys())

        for phase_name in target_phases:
            phase_config = self._config.phases.get(phase_name)

            # Fase no configurada
            if phase_config is None:
                result.phase_results.append(PhaseResult(
                    phase_name=phase_name,
                    skipped=True,
                    skip_reason=f"Phase '{phase_name}' not found in configuration",
                ))
                continue

            # Fase deshabilitada
            if not phase_config.enabled:
                result.phase_results.append(PhaseResult(
                    phase_name=phase_name,
                    skipped=True,
                    skip_reason="Phase disabled in configuration",
                ))
                continue

            # Ejecutar fase
            phase_result = await self._run_phase(phase_name, phase_config)
            result.phase_results.append(phase_result)

            # Parar si la fase falló y está configurado stop_on_error
            if not phase_result.is_successful and phase_config.stop_on_error:
                result.overall_status = "failed"
                break
        else:
            result.overall_status = "success" if result.is_successful else "completed_with_warnings"

        result.total_duration_seconds = time.monotonic() - start_time
        return result

    async def _run_phase(self, phase_name: str, phase_config) -> PhaseResult:
        """Ejecuta todos los agentes de una fase."""
        phase_result = PhaseResult(phase_name=phase_name)

        for agent_name in phase_config.agents:
            # Verificar que el agente existe
            if agent_name not in self._registry:
                phase_result.agent_outputs.append(AgentOutput(
                    agent_name=agent_name,
                    status="error",
                    errors=[f"Agent '{agent_name}' not registered"],
                ))
                continue

            agent = self._registry.get(agent_name)

            # Preparar input
            agent_input = AgentInput(
                phase=phase_name,
                project_path=self._config.project_path,
                config=self._config.api_policies.get(agent_name, {}),
                context=self._context,
                previous_results=phase_result.agent_outputs.copy(),
            )

            # Ejecutar agente
            output = await agent.run(agent_input)
            phase_result.agent_outputs.append(output)

            # Actualizar contexto compartido
            self._context.phase_results[agent_name] = output
            for key, value in output.metrics.items():
                self._context.add_metric(f"{agent_name}.{key}", value)

        return phase_result
