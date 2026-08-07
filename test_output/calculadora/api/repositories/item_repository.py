"""
Repository para Item — SOLID DIP.
Aísla el acceso a datos del servicio.
Generado por Arcana Builder.
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from api.models import Item


class ItemRepository:
    """Acceso a datos para Item. Solo CRUD puro."""

    def __init__(self, db: Session):
        self._db = db

    def create(self, **kwargs) -> Item:
        """Crea y persiste un item."""
        item = Item(**kwargs, eliminado=False)
        self._db.add(item)
        self._db.commit()
        self._db.refresh(item)
        return item

    def get_by_id(self, item_id: int) -> Optional[Item]:
        """Busca por ID (excluye eliminados)."""
        return self._db.query(Item).filter(
            Item.id == item_id, Item.eliminado == False
        ).first()

    def list_all(self) -> List[Item]:
        """Lista todos los activos."""
        return self._db.query(Item).filter(Item.eliminado == False).all()

    def update(self, item: Item, **kwargs) -> Item:
        """Actualiza campos."""
        for key, value in kwargs.items():
            if value is not None and hasattr(item, key):
                setattr(item, key, value)
        self._db.commit()
        self._db.refresh(item)
        return item

    def soft_delete(self, item: Item) -> Item:
        """Soft delete (recuperable)."""
        item.eliminado = True
        self._db.commit()
        return item
