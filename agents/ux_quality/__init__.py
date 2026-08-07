"""
Agente de Métricas de Calidad — ISO 25010/25022/25023.

Recopila métricas de todos los agentes y genera un dashboard
de calidad unificado según el modelo ISO 25010.
"""

from agents.ux_quality.agent import MetricsAgent

__all__ = ["MetricsAgent"]
