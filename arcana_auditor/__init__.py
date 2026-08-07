"""
🔮 Arcana Auditor — Módulo de Auditoría de Software

"Yo no negocio. El estándar es el estándar."

Responsabilidades:
- Detectar violaciones SOLID y OWASP (no negociable)
- Reportar en formato ISO 27001/COBIT/ISO 19011/25010
- Opcionalmente corregir (--fix) con evidencia y backup

Input: SOLO el path al código.
Los criterios NO son configurables por el usuario.

Uso:
  python -m arcana_auditor --project ./mi-app/
  python -m arcana_auditor --project ./mi-app/ --fix
  python -m arcana_auditor --project ./mi-app/ --report audit
"""
