"""
Core Config — Umbrales y estándares NO negociables.

Estos valores son los que el Auditor aplica sin negociar.
El Builder los usa para validar lo que genera.
El Tutor los usa para evaluar respuestas.
"""

# Umbrales ISO 25010 / OWASP / SOLID (no negociables)
THRESHOLDS = {
    "solid_min_score": 80.0,
    "owasp_min_score": 80.0,
    "owasp_critical_max": 0,
    "owasp_high_max": 0,
    "code_coverage_min": 80.0,
    "cyclomatic_complexity_max": 10,
    "method_max_lines": 30,
    "class_max_public_methods": 10,
    "title_min_length": 3,
    "title_max_length": 200,
}
