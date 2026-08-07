"""
conftest.py — Fixtures compartidas para tests.
Generado por Arcana Builder.

Provee: client de test (TestClient) + DB en memoria.

NOTA TÉCNICA: SQLite en memoria requiere una conexión compartida
para que las tablas creadas sean visibles por el TestClient.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from api.main import app
from api.database import get_db
from api.models import Base

# DB de test: SQLite en memoria con pool compartido
test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # Una sola conexión compartida
)
TestSession = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(autouse=True)
def setup_db():
    """Crea tablas antes de cada test, las borra después."""
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def client(setup_db):
    """TestClient de FastAPI con DB de test inyectada."""
    def override_get_db():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
