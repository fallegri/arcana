"""
Service para Item — SOLID SRP.
Solo lógica de negocio (no acceso a datos, no HTTP).
Generado por Arcana Builder.
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from api.repositories.item_repository import ItemRepository
from api.schemas.item import ItemCreate, ItemUpdate, ItemResponse


class ItemService:
    """Servicio de Item — coordina validación y persistencia."""

    def __init__(self, db: Session):
        self._repo = ItemRepository(db)

    def create(self, data: ItemCreate) -> ItemResponse:
        """Crea un nuevo item."""
        item = self._repo.create(**data.model_dump())
        return ItemResponse.model_validate(item)

    def get_by_id(self, item_id: int) -> Optional[ItemResponse]:
        """Obtiene un item por ID."""
        item = self._repo.get_by_id(item_id)
        if item is None:
            return None
        return ItemResponse.model_validate(item)

    def list_all(self) -> List[ItemResponse]:
        """Lista todos los items activos."""
        items = self._repo.list_all()
        return [ItemResponse.model_validate(i) for i in items]

    def update(self, item_id: int, data: ItemUpdate) -> Optional[ItemResponse]:
        """Actualiza un item."""
        item = self._repo.get_by_id(item_id)
        if item is None:
            return None
        updated = self._repo.update(item, **data.model_dump(exclude_unset=True))
        return ItemResponse.model_validate(updated)

    def delete(self, item_id: int) -> bool:
        """Soft-delete de un item."""
        item = self._repo.get_by_id(item_id)
        if item is None:
            return False
        self._repo.soft_delete(item)
        return True
