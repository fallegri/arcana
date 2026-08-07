"""
TaskService — Servicio de gestión de tareas (versión REFACTORIZADA).

NOTA EDUCATIVA:
Este archivo muestra la versión FINAL después del ciclo TDD completo:
1. RED: Tests escritos (tests/unit/test_task_service.py)
2. GREEN: Implementación mínima que los pasa
3. REFACTOR: Extracción de Validator y Repository (SOLID)

Principios SOLID aplicados:
- SRP: Solo COORDINA (no valida, no persiste)
- OCP: Agregar validaciones = modificar TaskValidator, no este archivo
- DIP: Depende de abstracciones (Repository, Validator)
- LSP: Cualquier Repository que cumpla el contrato funciona aquí
"""

from datetime import date
from typing import List, Optional

from examples.taskflow.api.models import Task
from examples.taskflow.api.repositories.task_repository import TaskRepository
from examples.taskflow.api.schemas import TaskResponse
from examples.taskflow.api.validators.task_validator import TaskValidator


class TaskService:
    """
    Servicio de gestión de tareas.

    Responsabilidades:
    - Coordinar la creación, lectura, actualización y eliminación de tareas
    - Verificar autenticación (delegar a middleware en el futuro)
    - Orquestar validación y persistencia

    NO hace:
    - Validar datos (→ TaskValidator)
    - Acceder a la DB directamente (→ TaskRepository)
    - Manejar HTTP (→ Router/Controller)
    """

    def __init__(
        self,
        repository: TaskRepository,
        validator: Optional[TaskValidator] = None,
    ):
        self._repository = repository
        self._validator = validator or TaskValidator()

    def create_task(
        self,
        titulo: Optional[str],
        user_id: Optional[int],
        descripcion: str = "",
        prioridad: str = "media",
        fecha_limite: Optional[date] = None,
        etiquetas: Optional[List[str]] = None,
    ) -> TaskResponse:
        """
        Crea una nueva tarea.

        Args:
            titulo: Título de la tarea (3-200 caracteres)
            user_id: ID del usuario autenticado
            descripcion: Descripción opcional
            prioridad: baja|media|alta|urgente
            fecha_limite: Fecha límite opcional
            etiquetas: Lista de etiquetas opcionales

        Returns:
            TaskResponse con la tarea creada

        Raises:
            PermissionError: Si no hay usuario autenticado
            ValueError: Si los datos son inválidos
        """
        # 1. Verificar autenticación
        self._require_authentication(user_id)

        # 2. Validar datos (delegado a Validator — SRP)
        titulo_limpio = self._validator.validate_title(titulo)
        if prioridad != "media":
            self._validator.validate_priority(prioridad)
        if descripcion:
            descripcion = self._validator.validate_description(descripcion)

        # 3. Crear entidad
        task = Task(
            titulo=titulo_limpio,
            descripcion=descripcion,
            estado="pendiente",
            prioridad=prioridad,
            user_id=user_id,
            fecha_creacion=date.today(),
            fecha_limite=fecha_limite,
            etiquetas=etiquetas or [],
        )

        # 4. Persistir (delegado a Repository — DIP)
        saved_task = self._repository.save(task)

        # 5. Retornar respuesta tipada
        return TaskResponse(
            id=saved_task.id,
            titulo=saved_task.titulo,
            descripcion=saved_task.descripcion,
            estado=saved_task.estado,
            prioridad=saved_task.prioridad,
            fecha_creacion=saved_task.fecha_creacion,
            fecha_limite=saved_task.fecha_limite,
            etiquetas=saved_task.etiquetas or [],
        )

    def list_tasks(
        self,
        user_id: int,
        estado: Optional[str] = None,
        prioridad: Optional[str] = None,
    ) -> List[TaskResponse]:
        """Lista las tareas de un usuario con filtros opcionales."""
        self._require_authentication(user_id)

        tasks = self._repository.find_by_user(
            user_id=user_id,
            estado=estado,
            prioridad=prioridad,
        )

        return [
            TaskResponse(
                id=t.id,
                titulo=t.titulo,
                descripcion=t.descripcion,
                estado=t.estado,
                prioridad=t.prioridad,
                fecha_creacion=t.fecha_creacion,
                fecha_limite=t.fecha_limite,
                etiquetas=t.etiquetas or [],
            )
            for t in tasks
        ]

    def search_tasks(self, user_id: int, query: str) -> List[TaskResponse]:
        """Busca tareas por texto."""
        self._require_authentication(user_id)
        tasks = self._repository.search(user_id=user_id, text=query)
        return [TaskResponse.model_validate(t) for t in tasks]

    def _require_authentication(self, user_id: Optional[int]) -> None:
        """Verifica que hay un usuario autenticado."""
        if not user_id:
            raise PermissionError(
                "Se requiere autenticación para realizar esta operación"
            )
