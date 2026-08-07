"""
🔮 Arcana Orchestrator — Director de Obra de Desarrollo

"Dame los requerimientos. Yo dirijo a la IA hasta que el sistema esté COMPLETO."

Filosofía:
- Recibe requerimientos del usuario (historias, reglas de negocio, contexto)
- Genera un PLAN DE DESARROLLO paso a paso
- Cada paso es una INSTRUCCIÓN para la IA (opencode/cursor)
- Después de cada paso, VERIFICA que se cumplió
- Repite hasta tener sistema completo + tests pasando + OWASP limpio

Diferencia con Builder:
- Builder genera scaffolding genérico en 2 segundos
- Orchestrator DIRIGE desarrollo completo con lógica real

Uso MCP:
  orchestrator_start   → Recibe requerimientos, genera plan completo
  orchestrator_step    → Retorna la instrucción del paso actual
  orchestrator_verify  → Verifica que el paso se implementó bien
  orchestrator_status  → Muestra progreso general

Uso CLI:
  python -m arcana_orchestrator --requirements reqs.md --output ./mi-sistema/
"""
