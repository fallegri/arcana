"""
Schemas de TaskFlow — Contratos de datos con Pydantic.

NOTA EDUCATIVA:
Los schemas definen QUÉ FORMA tienen los datos que entran y salen.
Pydantic valida automáticamente que los datos cumplan el contrato.

Principio: ISP (Interface Segregation)
- TaskCreate: solo los campos para CREAR (no incluye id, fecha, estado)
- TaskResponse: todos los campos que se RETORNAN
- TaskUpdate: solo los campos que se pueden MODIFICAR
"""

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    """Datos requeridos para crear una tarea."""

    titulo: str = Field(..., min_length=3, max_length=200)
    descripcion: str = Field(default="", max_length=2000)
    prioridad: str = Field(default="media")
    fecha_limite: Optional[date] = None
    etiquetas: List[str] = Field(default_factory=list)


class TaskResponse(BaseModel):
    """Datos que se retornan al usuario."""

    id: int
    titulo: str
    descripcion: str
    estado: str
    prioridad: str
    fecha_creacion: date
    fecha_limite: Optional[date] = None
    etiquetas: List[str] = Field(default_factory=list)

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    """Datos que se pueden modificar."""

    titulo: Optional[str] = Field(None, min_length=3, max_length=200)
    descripcion: Optional[str] = Field(None, max_length=2000)
    estado: Optional[str] = None
    prioridad: Optional[str] = None
    fecha_limite: Optional[date] = None
    etiquetas: Optional[List[str]] = None
