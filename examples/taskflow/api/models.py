"""
Modelos de TaskFlow — Entidades de base de datos.

NOTA EDUCATIVA:
Los modelos representan las TABLAS de la base de datos.
SQLAlchemy mapea cada clase a una tabla y cada atributo a una columna.

Principio: SRP — Cada modelo representa UNA entidad del dominio.
"""

from datetime import date, datetime
from typing import Optional

from sqlalchemy import Column, Date, DateTime, Integer, String, Text, Boolean, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Task(Base):
    """Modelo de Tarea en la base de datos."""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, default="")
    estado = Column(String(20), default="pendiente")
    prioridad = Column(String(20), default="media")
    user_id = Column(Integer, nullable=False)
    fecha_creacion = Column(Date, default=date.today)
    fecha_limite = Column(Date, nullable=True)
    etiquetas = Column(JSON, default=list)
    eliminado = Column(Boolean, default=False)
    fecha_modificacion = Column(DateTime, nullable=True)


class User(Base):
    """Modelo de Usuario en la base de datos."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    activo = Column(Boolean, default=True)
    intentos_fallidos = Column(Integer, default=0)
    bloqueado_hasta = Column(DateTime, nullable=True)
    fecha_registro = Column(DateTime, default=datetime.now)
