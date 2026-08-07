# calculadora

> Generado por 🔮 Arcana Builder — con estándares profesionales integrados.

## Estándares Aplicados

| Estándar | Cómo se aplica |
|----------|---------------|
| **BDD** | Escenarios en `features/*.feature` |
| **TDD** | Tests en `tests/` (ejecutar con `pytest`) |
| **SOLID** | Separación services/repositories/validators |
| **OWASP** | Auth JWT, password hashing, validación |

## Entidades

User, Item

## Historias de Usuario

- Como usuario quiero sumar dos números
- Como usuario quiero restar dos números
- Como usuario quiero multiplicar dos números
- Como usuario quiero dividir dos números
- Como usuario quiero ver el historial de operaciones

## Quick Start

```bash
pip install -e .
pytest tests/ -v
uvicorn api.main:app --reload
```

---
*Generado por Arcana Builder — "Dime QUÉ necesitas. El CÓMO es mi trabajo."*
