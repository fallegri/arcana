"""
Core Agents — Implementaciones compartidas de análisis.

Estos agentes son usados por los módulos que los necesitan:
- Auditor usa: SOLIDAgent, OWASPAgent (analyze + fix)
- Builder usa: SOLIDAgent, OWASPAgent (validate lo que genera)
- Tutor usa: SOLIDAgent, OWASPAgent (evaluar respuestas del alumno)

Cada módulo importa SOLO lo que necesita (ISP).
"""
