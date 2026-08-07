"""
calculadora API — Generado por Arcana Builder.

Estándares integrados:
- SOLID: services/ + repositories/ + routers/ (SRP, DIP)
- OWASP: debug=False, validación Pydantic, soft delete
- ISO 42010: Arquitectura documentada en README
"""

from fastapi import FastAPI
from api.database import init_db
from api.routers.item_router import router as item_router

app = FastAPI(
    title="calculadora",
    description="API generada por Arcana Builder con estándares profesionales",
    version="1.0.0",
    debug=False,  # OWASP A05: NUNCA True en producción
)

# Registrar routers
app.include_router(item_router)


@app.get("/health")
def health_check():
    """Endpoint de salud del sistema."""
    return {"status": "ok", "service": "calculadora"}


@app.on_event("startup")
def startup():
    """Inicializa la base de datos al arrancar."""
    init_db()
