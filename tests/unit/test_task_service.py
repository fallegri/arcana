"""
Tests Unitarios — TaskService (Creación de Tareas)

DERIVADO DE: agents/bdd/features/tasks/crear_tarea.feature
CICLO TDD: Estos tests se escribieron ANTES de la implementación (RED)

Estructura:
- TestCreateTask: Happy path (crear exitosamente)
- TestCreateTaskValidation: Edge cases de validación
- TestCreateTaskAuth: Seguridad/autenticación

Patrón: AAA (Arrange-Act-Assert) = Given-When-Then
"""

import pytest
from datetime import date


class TestCreateTask:
    """
    🔴→🟢 Tests derivados del escenario BDD:
    'Scenario: Crear tarea con solo título (mínimo)'
    """

    def test_create_returns_task_with_id(self, task_service):
        """La tarea creada tiene un ID asignado."""
        result = task_service.create_task(titulo="Comprar insumos", user_id=1)

        assert result is not None
        assert result.id is not None
        assert result.id > 0

    def test_create_preserves_title(self, task_service):
        """El título se guarda correctamente."""
        result = task_service.create_task(titulo="Comprar insumos", user_id=1)

        assert result.titulo == "Comprar insumos"

    def test_create_default_status_pending(self, task_service):
        """Estado por defecto es 'pendiente'."""
        result = task_service.create_task(titulo="Mi tarea", user_id=1)

        assert result.estado == "pendiente"

    def test_create_default_priority_media(self, task_service):
        """Prioridad por defecto es 'media'."""
        result = task_service.create_task(titulo="Mi tarea", user_id=1)

        assert result.prioridad == "media"

    def test_create_sets_today_as_creation_date(self, task_service):
        """Fecha de creación es el día actual."""
        result = task_service.create_task(titulo="Mi tarea", user_id=1)

        assert result.fecha_creacion == date.today()

    def test_create_with_custom_priority(self, task_service):
        """Se puede especificar prioridad distinta a la default."""
        result = task_service.create_task(
            titulo="Urgente", user_id=1, prioridad="alta"
        )

        assert result.prioridad == "alta"

    def test_create_with_description(self, task_service):
        """La descripción se guarda correctamente."""
        result = task_service.create_task(
            titulo="Mi tarea",
            user_id=1,
            descripcion="Detalles importantes",
        )

        assert result.descripcion == "Detalles importantes"

    def test_create_multiple_tasks_have_unique_ids(self, task_service):
        """Cada tarea tiene un ID único."""
        task1 = task_service.create_task(titulo="Tarea 1", user_id=1)
        task2 = task_service.create_task(titulo="Tarea 2", user_id=1)

        assert task1.id != task2.id

    def test_create_duplicate_title_allowed(self, task_service):
        """Títulos duplicados están permitidos (cada uno con ID único)."""
        task1 = task_service.create_task(titulo="Mismo título", user_id=1)
        task2 = task_service.create_task(titulo="Mismo título", user_id=1)

        assert task1.id != task2.id
        assert task1.titulo == task2.titulo


class TestCreateTaskValidation:
    """
    🔴→🟢 Tests derivados de:
    'Scenario: No puedo crear tarea sin título'
    'Scenario: El título tiene un límite de caracteres'
    """

    def test_empty_title_raises_error(self, task_service):
        """Título vacío lanza ValueError."""
        with pytest.raises(ValueError, match="obligatorio"):
            task_service.create_task(titulo="", user_id=1)

    def test_none_title_raises_error(self, task_service):
        """Título None lanza ValueError."""
        with pytest.raises(ValueError, match="obligatorio"):
            task_service.create_task(titulo=None, user_id=1)

    def test_whitespace_title_raises_error(self, task_service):
        """Título con solo espacios lanza ValueError."""
        with pytest.raises(ValueError, match="obligatorio"):
            task_service.create_task(titulo="   ", user_id=1)

    def test_title_too_short_raises_error(self, task_service):
        """Título menor a 3 caracteres lanza ValueError."""
        with pytest.raises(ValueError, match="3"):
            task_service.create_task(titulo="AB", user_id=1)

    def test_title_too_long_raises_error(self, task_service):
        """Título mayor a 200 caracteres lanza ValueError."""
        with pytest.raises(ValueError, match="200"):
            task_service.create_task(titulo="A" * 201, user_id=1)

    def test_title_exactly_200_is_valid(self, task_service):
        """Boundary: 200 caracteres exactos es válido."""
        result = task_service.create_task(titulo="A" * 200, user_id=1)
        assert len(result.titulo) == 200

    def test_title_exactly_3_is_valid(self, task_service):
        """Boundary: 3 caracteres exactos es válido."""
        result = task_service.create_task(titulo="ABC", user_id=1)
        assert result.titulo == "ABC"

    @pytest.mark.parametrize("titulo_invalido", [
        "",
        "  ",
        "\t",
        "\n",
        None,
    ])
    def test_various_empty_titles_raise_error(self, task_service, titulo_invalido):
        """Múltiples variantes de 'vacío' son rechazadas."""
        with pytest.raises(ValueError):
            task_service.create_task(titulo=titulo_invalido, user_id=1)


class TestCreateTaskAuth:
    """
    🔴→🟢 Tests derivados de:
    'Scenario: No puedo crear tareas sin estar autenticada'
    """

    def test_no_user_id_raises_permission_error(self, task_service):
        """Sin user_id → PermissionError."""
        with pytest.raises(PermissionError):
            task_service.create_task(titulo="Válida", user_id=None)

    def test_zero_user_id_raises_permission_error(self, task_service):
        """user_id=0 → PermissionError (0 es falsy)."""
        with pytest.raises(PermissionError):
            task_service.create_task(titulo="Válida", user_id=0)
