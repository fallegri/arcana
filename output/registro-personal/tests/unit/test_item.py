"""Tests REALES de Item — usan TestClient + DB en memoria."""
import pytest


class TestCreateItem:
    """CRUD: Crear item."""

    def test_create_returns_201(self, client):
        """POST /items con datos válidos retorna 201."""
        response = client.post("/items/", json={"nombre": "Test Value", "descripcion": "Test Value", "estado": "Test Value", "fecha_creacion": "2026-08-04"})
        assert response.status_code == 201, f"Esperaba 201, recibí {response.status_code}: {response.text}"

    def test_create_returns_id(self, client):
        """El item creado tiene un ID asignado."""
        response = client.post("/items/", json={"nombre": "Test Value", "descripcion": "Test Value", "estado": "Test Value", "fecha_creacion": "2026-08-04"})
        data = response.json()
        assert "id" in data
        assert data["id"] > 0

    def test_create_preserves_data(self, client):
        """Los datos enviados se preservan en la respuesta."""
        response = client.post("/items/", json={"nombre": "Test Value", "descripcion": "Test Value", "estado": "Test Value", "fecha_creacion": "2026-08-04"})
        data = response.json()
        assert data is not None


class TestListItem:
    """CRUD: Listar items."""

    def test_list_empty_returns_empty_array(self, client):
        """Sin datos, retorna lista vacía (no error)."""
        response = client.get("/items/")
        assert response.status_code == 200
        assert response.json() == []

    def test_list_after_create_returns_items(self, client):
        """Después de crear, aparece en la lista."""
        client.post("/items/", json={"nombre": "Test Value", "descripcion": "Test Value", "estado": "Test Value", "fecha_creacion": "2026-08-04"})
        response = client.get("/items/")
        assert response.status_code == 200
        assert len(response.json()) == 1


class TestGetItem:
    """CRUD: Obtener item por ID."""

    def test_get_existing_returns_200(self, client):
        """GET /items/{id} con ID válido retorna 200."""
        create = client.post("/items/", json={"nombre": "Test Value", "descripcion": "Test Value", "estado": "Test Value", "fecha_creacion": "2026-08-04"})
        item_id = create.json()["id"]
        response = client.get(f"/items/{item_id}")
        assert response.status_code == 200

    def test_get_nonexistent_returns_404(self, client):
        """GET /items/999 retorna 404."""
        response = client.get("/items/999")
        assert response.status_code == 404


class TestDeleteItem:
    """CRUD: Eliminar item (soft delete)."""

    def test_delete_existing_returns_204(self, client):
        """DELETE /items/{id} retorna 204."""
        create = client.post("/items/", json={"nombre": "Test Value", "descripcion": "Test Value", "estado": "Test Value", "fecha_creacion": "2026-08-04"})
        item_id = create.json()["id"]
        response = client.delete(f"/items/{item_id}")
        assert response.status_code == 204

    def test_deleted_not_in_list(self, client):
        """Después de delete, no aparece en la lista."""
        create = client.post("/items/", json={"nombre": "Test Value", "descripcion": "Test Value", "estado": "Test Value", "fecha_creacion": "2026-08-04"})
        item_id = create.json()["id"]
        client.delete(f"/items/{item_id}")
        response = client.get("/items/")
        assert len(response.json()) == 0

    def test_delete_nonexistent_returns_404(self, client):
        """DELETE /items/999 retorna 404."""
        response = client.delete("/items/999")
        assert response.status_code == 404
