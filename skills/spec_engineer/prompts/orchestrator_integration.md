# Integración con el Orchestrator MCP

## Flujo Completo (Spec → Plan → Build)

```
FASE 0: SPEC (NUEVA — interactiva)
│
│  orchestrator_spec_start → Analiza + genera preguntas
│  ↕ (loop interactivo)
│  orchestrator_spec_answer → Recibe respuestas + pregunta más
│  ↕ (repite hasta ready)
│  orchestrator_spec_confirm → Usuario confirma → genera Spec Document
│
▼
FASE 1: PLAN (existente)
│  orchestrator_start → Genera plan de 10 pasos
│
▼
FASE 2: BUILD (existente)
│  orchestrator_step → Instrucciones paso a paso
│  orchestrator_verify → Verifica cada paso
│
▼
FASE 3: DOC (existente)
│  Genera documento técnico completo (11 secciones)
```

## MCP Tool: orchestrator_spec_start

**Input:** Descripción inicial del usuario (texto libre)
**Output:** 
- Lo que entendió (resumen)
- Entidades detectadas (propuestas)
- Preguntas (3-5 específicas)
- Completeness score (0-100%)
- ready: false (todavía no puede generar)

## MCP Tool: orchestrator_spec_answer

**Input:** Respuestas del usuario a las preguntas
**Output:**
- Actualización de entendimiento
- Nuevas preguntas (si surgen)
- Completeness actualizado
- ready: true/false

## MCP Tool: orchestrator_spec_confirm

**Input:** Confirmación del usuario ("sí, adelante")
**Output:**
- Spec Document completo (Markdown)
- Listo para llamar a orchestrator_start con la spec completa

## Comportamiento esperado de la IA (opencode)

La IA que usa estas tools DEBE:

1. Llamar orchestrator_spec_start con la descripción
2. Mostrar al usuario las preguntas
3. Recopilar respuestas
4. Llamar orchestrator_spec_answer con las respuestas
5. Si ready=false → mostrar nuevas preguntas → repetir
6. Si ready=true → llamar orchestrator_spec_confirm
7. Solo DESPUÉS llamar orchestrator_start con la spec completa

La IA NUNCA debe:
- Saltarse la fase Spec
- Asumir respuestas que el usuario no dio
- Proceder sin confirmación explícita
