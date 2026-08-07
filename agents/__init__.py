"""
AI-Dev-Guide Agents
==================

Módulos de agentes especializados que implementan cada fase
del pipeline de desarrollo profesional.

Cada agente:
- Hereda de BaseAgent (LSP)
- Tiene una sola responsabilidad (SRP)
- Se registra en el AgentRegistry (OCP)
- Se comunica via AgentInput/AgentOutput (ISP)
"""

from agents.base import AgentInput, AgentOutput, BaseAgent, SharedContext, FixAction, FixResult

__all__ = ["BaseAgent", "AgentInput", "AgentOutput", "SharedContext", "FixAction", "FixResult"]
