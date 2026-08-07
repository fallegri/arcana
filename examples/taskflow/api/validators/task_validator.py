"""
TaskValidator — Validador de datos de tareas.

NOTA EDUCATIVA (REFACTOR - SRP):
Este validador fue EXTRAÍDO del TaskService durante el paso REFACTOR.
Antes, toda la validación estaba dentro de create_task().
Ahora tiene su propia clase con una sola responsabilidad: VALIDAR.

Beneficios:
1. Se puede testear la validación SIN base de datos
2. Se puede reutilizar en otros servicios (ej: update_task)
3. Se puede extender sin modificar TaskService (OCP)
"""

from typing import Optional


class TaskValidator:
    """
    Valida datos de tareas según reglas de negocio.

    SRP: Solo valida. No persiste, no autentica, no notifica.
    """

    TITLE_MIN_LENGTH: int = 3
    TITLE_MAX_LENGTH: int = 200
    DESCRIPTION_MAX_LENGTH: int = 2000
    VALID_PRIORITIES: set = {"baja", "media", "alta", "urgente"}
    VALID_STATES: set = {"pendiente", "en_proceso", "completada", "cancelada"}

    def validate_title(self, titulo: Optional[str]) -> str:
        """
        Valida y limpia el título de una tarea.

        Args:
            titulo: Título a validar (puede ser None, vacío, etc.)

        Returns:
            Título limpio (stripped) si es válido

        Raises:
            ValueError: Si el título no cumple las reglas
        """
        if titulo is None or titulo.strip() == "":
            raise ValueError("El título es obligatorio")

        clean_title = titulo.strip()

        if len(clean_title) < self.TITLE_MIN_LENGTH:
            raise ValueError(
                f"El título debe tener al menos {self.TITLE_MIN_LENGTH} caracteres"
            )

        if len(clean_title) > self.TITLE_MAX_LENGTH:
            raise ValueError(
                f"El título no puede exceder {self.TITLE_MAX_LENGTH} caracteres"
            )

        return clean_title

    def validate_priority(self, prioridad: str) -> str:
        """Valida que la prioridad sea un valor permitido."""
        if prioridad not in self.VALID_PRIORITIES:
            raise ValueError(
                f"Prioridad inválida: '{prioridad}'. "
                f"Valores permitidos: {sorted(self.VALID_PRIORITIES)}"
            )
        return prioridad

    def validate_state(self, estado: str) -> str:
        """Valida que el estado sea un valor permitido."""
        if estado not in self.VALID_STATES:
            raise ValueError(
                f"Estado inválido: '{estado}'. "
                f"Valores permitidos: {sorted(self.VALID_STATES)}"
            )
        return estado

    def validate_description(self, descripcion: str) -> str:
        """Valida la descripción."""
        if len(descripcion) > self.DESCRIPTION_MAX_LENGTH:
            raise ValueError(
                f"La descripción no puede exceder {self.DESCRIPTION_MAX_LENGTH} caracteres"
            )
        return descripcion.strip()
