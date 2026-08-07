"""
🔮 Arcana Tutor — Módulo de Enseñanza Interactiva

"Dime qué quieres aprender y a qué nivel."

Responsabilidades:
- Generar retos de código (bueno y malo) según tema y nivel
- Evaluar correcciones del alumno
- Dar pistas progresivas sin resolver
- Mostrar solución completa cuando el alumno termina
- Trackear progreso

Input: Tema + nivel + tipo de ejercicio (TODO configurable)
Output: Reto + evaluación + retroalimentación

Uso:
  python -m arcana_tutor --topic owasp --level beginner
  python -m arcana_tutor --evaluate ./mi-solucion.py --challenge CH-001
  python -m arcana_tutor --hint --challenge CH-001
"""
