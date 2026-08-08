"""
🔮 Arcana PM — Project Manager / Jefe de Proyecto

"No solo hablo con el desarrollador. Coordino con TODOS los involucrados."

5° módulo INDEPENDIENTE de Arcana.

Personalidad: Jefe de Proyecto + Ingeniero de Requisitos Senior
que sabe que un sistema complejo requiere input de MÚLTIPLES personas.

Modos de operación:
  A) Guía al líder: genera cuestionarios para que el usuario entreviste
  B) Cuestionario directo: genera formularios por rol/área para enviar
  C) Workshop: genera agenda de sesión de trabajo facilitada

Flujo:
  1. Detecta tipo de sistema → identifica stakeholders necesarios
  2. Genera cuestionario ESPECÍFICO por stakeholder/área
  3. Recopila respuestas (una por una o todas juntas)
  4. Consolida + detecta conflictos entre áreas
  5. Genera Spec unificada (alimenta al Orchestrator)

MCP Tools:
  pm_identify_stakeholders  → ¿Quiénes deben participar?
  pm_generate_questionnaire → Cuestionario para un stakeholder específico
  pm_submit_response        → Recibe respuesta de un stakeholder
  pm_consolidate            → Unifica todo + detecta conflictos
  pm_export                 → Exporta cuestionarios (email/PDF/formulario)
  pm_workshop               → Genera agenda de workshop facilitado

Uso:
  python -m arcana_pm --project "ERP" --describe "ERP para distribuidora"
"""
