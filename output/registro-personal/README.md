# registro-personal

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

- Como RRHH quiero registrar empleados con datos personales y laborales
- Como RRHH quiero gestionar departamentos y cargos
- Como RRHH quiero registrar contratos de trabajo
- Como jefe quiero ver empleados de mi departamento
- Como RRHH quiero registrar y aprobar vacaciones
- Como empleado quiero ver mi información y vacaciones

## Quick Start

```bash
pip install -e .
pytest tests/ -v
uvicorn api.main:app --reload
```

---
*Generado por Arcana Builder — "Dime QUÉ necesitas. El CÓMO es mi trabajo."*
