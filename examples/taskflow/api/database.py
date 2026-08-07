"""
Database Configuration — Configuración de base de datos.

NOTA EDUCATIVA:
Este módulo demuestra DIP (Dependency Inversion):
- Provee una función get_db() que retorna una sesión
- Los servicios reciben la sesión como dependencia (no la crean)
- Para testing, se puede inyectar una sesión de test diferente

En producción usarías PostgreSQL.
En tests usamos SQLite en memoria (rápido y descartable).
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from examples.taskflow.api.models import Base

# Base de datos de producción (SQLite para el ejemplo)
_engine = create_engine("sqlite:///taskflow.db", echo=False)
_SessionLocal = sessionmaker(bind=_engine)

# Base de datos de testing (en memoria)
_test_engine = create_engine("sqlite:///:memory:", echo=False)
_TestSession = sessionmaker(bind=_test_engine)


def init_db() -> None:
    """Inicializa la base de datos de producción."""
    Base.metadata.create_all(bind=_engine)


def get_db() -> Session:
    """Obtiene una sesión de producción."""
    db = _SessionLocal()
    try:
        return db
    finally:
        pass  # El caller es responsable de cerrar


def get_test_session() -> Session:
    """
    Obtiene una sesión de testing (SQLite en memoria).

    NOTA EDUCATIVA:
    Cada llamada crea tablas frescas → cada test empieza limpio.
    Esto es clave para tests INDEPENDENT (la I de FIRST).
    """
    Base.metadata.create_all(bind=_test_engine)
    session = _TestSession()
    return session


def reset_test_db() -> None:
    """Resetea la base de datos de testing."""
    Base.metadata.drop_all(bind=_test_engine)
    Base.metadata.create_all(bind=_test_engine)
