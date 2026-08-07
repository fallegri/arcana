"""Schemas para Item — ISP: interfaces separadas por operación."""
from pydantic import BaseModel
from typing import List, Optional


class ItemCreate(BaseModel):
    """Datos para CREAR un item."""
    nombre: str
    descripcion: str
    estado: str
    fecha_creacion: Optional[str]


class ItemResponse(BaseModel):
    """Datos que se RETORNAN al usuario."""
    id: int
    nombre: str
    descripcion: str
    estado: str
    fecha_creacion: Optional[str]

    class Config:
        from_attributes = True


class ItemUpdate(BaseModel):
    """Datos que se pueden MODIFICAR (todos opcionales)."""
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    fecha_creacion: Optional[Optional[str]] = None
