"""
🔮 Arcana Skills — Conocimiento Especializado Activable

Los Skills son "libros de consulta" que Arcana carga cuando el dominio
del proyecto lo requiere. No modifican el core — lo ENRIQUECEN.

Estructura de cada skill:
  skills/{nombre}/
  ├── skill.yaml       # Metadata: triggers, descripción, dependencias
  ├── templates/       # Plantillas de código/diseño base
  └── prompts/         # Instrucciones expertas para la IA

Activación automática:
  El SkillMatcher analiza el texto del usuario y activa skills relevantes.
  Ejemplo: "landing page" → activa web_design skill
"""
