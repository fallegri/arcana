"""
TaskRepository — Capa de persistencia de tareas.

NOTA EDUCATIVA (REFACTOR - DIP):
Este repositorio fue EXTRAÍDO del TaskService durante REFACTOR.
Antes, el servicio hacía db.add() y db.commit() directamente.
Ahora el servicio depende de una ABSTRACCIÓN (el repositorio).

Beneficios (DIP):
1. Puedes cambiar SQLite → PostgreSQL → MongoDB sin tocar el servicio
2. En tests, puedes usar un InMemoryTaskRepository (sin DB real)
3. El servicio no conoce detalles de SQL/ORM
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from examples.taskflow.api.models import Task


class TaskRepository:
    """
    Repositorio de tareas — acceso a datos.

    DIP: El servicio depende de esta abstracción.
    Si cambias la DB, solo cambias esta clase.
    """

    def __init__(self, db: Session):
        self._db = db

    def save(self, task: Task) -> Task:
        """
        Persiste una tarea (nueva o existente).

        Args:
            task: Entidad Task a guardar

        Returns:
            Task con ID asignado (si es nueva)
        """
        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)
        return task

    def find_by_id(self, task_id: int) -> Optional[Task]:
        """Busca una tarea por su ID."""
        return (
            self._db.query(Task)
            .filter(Task.id == task_id, Task.eliminado == False)
            .first()
        )

    def find_by_user(
        self,
        user_id: int,
        estado: Optional[str] = None,
        prioridad: Optional[str] = None,
    ) -> List[Task]:
        """
        Lista tareas de un usuario con filtros opcionales.

        Args:
            user_id: ID del usuario
            estado: Filtrar por estado (opcional)
            prioridad: Filtrar por prioridad (opcional)
        """
        query = self._db.query(Task).filter(
            Task.user_id == user_id,
            Task.eliminado == False,
        )

        if estado:
            query = query.filter(Task.estado == estado)
        if prioridad:
            query = query.filter(Task.prioridad == prioridad)

        return query.order_by(Task.fecha_creacion.desc()).all()

    def search(self, user_id: int, text: str) -> List[Task]:
        """Busca tareas por texto en título o descripción."""
        return (
            self._db.query(Task)
            .filter(
                Task.user_id == user_id,
                Task.eliminado == False,
                (Task.titulo.contains(text) | Task.descripcion.contains(text)),
            )
            .all()
        )

    def soft_delete(self, task: Task) -> Task:
        """Marca una tarea como eliminada (soft delete)."""
        task.eliminado = True
        self._db.commit()
        return task

    def count_by_user(self, user_id: int) -> int:
        """Cuenta tareas activas de un usuario."""
        return (
            self._db.query(Task)
            .filter(Task.user_id == user_id, Task.eliminado == False)
            .count()
        )
