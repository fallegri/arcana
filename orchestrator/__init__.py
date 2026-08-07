"""
AI-Dev-Guide Orchestrator
========================

Motor de orquestación del pipeline de desarrollo profesional.
Coordina la ejecución de agentes según configuración YAML.

Principios aplicados:
- SRP: Solo coordina, no implementa lógica de agentes
- OCP: Nuevos agentes se registran sin modificar este módulo
- DIP: Depende de BaseAgent (abstracción), no de agentes concretos
"""

__version__ = "1.0.0"
