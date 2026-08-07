"""
Agent Registry — Registro dinámico de agentes disponibles.

Principio SOLID demostrado: Open/Closed Principle (OCP)
- El registro está ABIERTO para agregar nuevos agentes
- Está CERRADO para modificación (no hay que tocar código existente)

Uso:
    registry = AgentRegistry()
    registry.register(OWASPAgent())
    registry.register(TDDAgent())

    # Obtener agente por nombre
    agent = registry.get("owasp")

    # Obtener agentes por fase
    security_agents = registry.get_by_phase("security")
"""

from typing import Dict, List, Optional

from agents.base import BaseAgent


class AgentNotFoundError(Exception):
    """Se lanza cuando se solicita un agente no registrado."""

    pass


class AgentRegistry:
    """
    Registro central de agentes disponibles.

    Implementa el patrón Registry para desacoplar
    el orquestador de los agentes concretos.
    """

    def __init__(self) -> None:
        self._agents: Dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        """
        Registra un agente en el sistema.

        Args:
            agent: Instancia de un agente que hereda de BaseAgent

        Raises:
            ValueError: Si ya existe un agente con el mismo nombre
        """
        if agent.name in self._agents:
            raise ValueError(
                f"Agent '{agent.name}' is already registered. "
                f"Each agent must have a unique name (SRP)."
            )
        self._agents[agent.name] = agent

    def get(self, name: str) -> BaseAgent:
        """
        Obtiene un agente por su nombre.

        Args:
            name: Identificador único del agente

        Returns:
            Instancia del agente

        Raises:
            AgentNotFoundError: Si el agente no está registrado
        """
        if name not in self._agents:
            available = ", ".join(sorted(self._agents.keys()))
            raise AgentNotFoundError(
                f"Agent '{name}' not found. Available: [{available}]"
            )
        return self._agents[name]

    def get_by_phase(self, phase: str) -> List[BaseAgent]:
        """Obtiene todos los agentes de una fase específica."""
        return [a for a in self._agents.values() if a.phase == phase]

    def list_all(self) -> List[BaseAgent]:
        """Lista todos los agentes registrados."""
        return list(self._agents.values())

    @property
    def count(self) -> int:
        """Número de agentes registrados."""
        return len(self._agents)

    def __contains__(self, name: str) -> bool:
        """Permite usar 'in' para verificar si un agente existe."""
        return name in self._agents
