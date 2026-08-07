"""
Fixtures de pytest — Configuración compartida para tests unitarios.

NOTA EDUCATIVA:
conftest.py es un archivo especial de pytest que:
- Se carga automáticamente (no necesitas importarlo)
- Las fixtures definidas aquí están disponibles en TODOS los tests del directorio
- Evita duplicar setup entre múltiples archivos de test

Patrón: DRY (Don't Repeat Yourself) aplicado a testing.
"""

import sys
from pathlib import Path

import pytest

# Agregar el directorio raíz al path para imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def test_db():
    """
    Crea una base de datos de test fresca.

    NOTA EDUCATIVA:
    Usa 'yield' para separar setup y teardown:
    - Antes de yield: SETUP (crear DB)
    - Después de yield: TEARDOWN (limpiar)

    Cada test recibe una DB limpia → tests INDEPENDIENTES.
    """
    from examples.taskflow.api.database import get_test_session, reset_test_db

    reset_test_db()
    session = get_test_session()
    yield session
    session.close()


@pytest.fixture
def task_validator():
    """Instancia de TaskValidator para tests de validación."""
    from examples.taskflow.api.validators.task_validator import TaskValidator
    return TaskValidator()


@pytest.fixture
def task_repository(test_db):
    """Repositorio de tareas conectado a la DB de test."""
    from examples.taskflow.api.repositories.task_repository import TaskRepository
    return TaskRepository(db=test_db)


@pytest.fixture
def task_service(task_repository, task_validator):
    """
    Servicio de tareas completo listo para testing.

    NOTA EDUCATIVA:
    Observa cómo las fixtures se COMPONEN:
    task_service depende de task_repository y task_validator,
    que a su vez depende de test_db.
    pytest resuelve esta cadena automáticamente.
    """
    from examples.taskflow.api.services.task_service import TaskService
    return TaskService(repository=task_repository, validator=task_validator)


@pytest.fixture
def auth_service(test_db):
    """Servicio de autenticación para tests."""
    from examples.taskflow.api.services.auth_service import AuthService
    return AuthService(db=test_db)


@pytest.fixture
def registered_user(auth_service):
    """Un usuario ya registrado (listo para login)."""
    auth_service.register(
        nombre="María García",
        email="maria@test.com",
        password="MiClave$egura2026"
    )
    return {
        "nombre": "María García",
        "email": "maria@test.com",
        "password": "MiClave$egura2026",
    }
