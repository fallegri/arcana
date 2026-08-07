"""
Database — Configuración de base de datos.
Generado por Arcana Builder.

SOLID DIP: Los servicios reciben la sesión, no la crean.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from api.models import Base

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Crea las tablas en la base de datos."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency injection para FastAPI — provee sesión de DB."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Testing
_test_engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
TestSession = sessionmaker(autocommit=False, autoflush=False, bind=_test_engine)


def get_test_db():
    """Sesión de test (SQLite en memoria)."""
    Base.metadata.create_all(bind=_test_engine)
    db = TestSession()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=_test_engine)
