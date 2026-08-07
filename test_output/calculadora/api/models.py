"""
Modelos de datos — Generado por Arcana Builder.

OWASP integrado:
- Password NUNCA en texto plano (solo hash)
- Campos validados por tipo
- Soft delete por defecto
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime, Text, JSON
from sqlalchemy.orm import declarative_base
from datetime import date, datetime

Base = declarative_base()

class User(Base):
    """Modelo User."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    email = Column(String(255))
    password_hash = Column(String(255), nullable=False)  # OWASP A02: NUNCA texto plano
    activo = Column(Boolean)
    eliminado = Column(Boolean, default=False)  # Soft delete


class Item(Base):
    """Modelo Item."""
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    descripcion = Column(String(255))
    estado = Column(String(255))
    user_id = Column(Integer)
    fecha_creacion = Column(String(20))
    eliminado = Column(Boolean, default=False)  # Soft delete

