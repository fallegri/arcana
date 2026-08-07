"""
Router para Item — Endpoints REST completos.
Generado por Arcana Builder.

Endpoints:
  GET    /items         → Listar todos
  POST   /items         → Crear nuevo
  GET    /items/{id}   → Obtener por ID
  PATCH  /items/{id}   → Actualizar
  DELETE /items/{id}   → Eliminar (soft delete)
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.database import get_db
from api.services.item_service import ItemService
from api.schemas.item import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter(prefix="/items", tags=["Item"])


@router.get("/", response_model=List[ItemResponse])
def list_items(db: Session = Depends(get_db)):
    """Lista todos los items activos."""
    service = ItemService(db)
    return service.list_all()


@router.post("/", response_model=ItemResponse, status_code=201)
def create_item(data: ItemCreate, db: Session = Depends(get_db)):
    """Crea un nuevo item."""
    service = ItemService(db)
    return service.create(data)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """Obtiene un item por ID."""
    service = ItemService(db)
    result = service.get_by_id(item_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return result


@router.patch("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, data: ItemUpdate, db: Session = Depends(get_db)):
    """Actualiza un item."""
    service = ItemService(db)
    result = service.update(item_id, data)
    if result is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return result


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Elimina un item (soft delete)."""
    service = ItemService(db)
    deleted = service.delete(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return None
