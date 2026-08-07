# AI-Dev-Guide — Estándares del Proyecto

## Principios Fundamentales

1. **Eat your own dog food**: El código del sistema DEBE demostrar las prácticas que enseña
2. **Progresividad**: Todo output tiene modo `--beginner` (explicativo) y `--expert` (conciso)
3. **Medibilidad**: Toda calidad se expresa en métricas cuantificables (ISO 25023)

## Estándares de Código

- Python 3.11+ con type hints obligatorios
- Formateo: `black` + `isort` + `ruff`
- Docstrings: Google style, obligatorias en toda función pública
- Complejidad ciclomática máxima por función: 10
- Cobertura de tests mínima: 80%

## Arquitectura

- Patrón: Agentes orquestados con contratos tipados
- Toda comunicación entre agentes via `AgentInput`/`AgentOutput`
- Dependencias inyectadas, nunca hardcoded (SOLID: DIP)
- Nuevas funcionalidades = nuevos agentes, nunca modificar existentes (SOLID: OCP)

## Seguridad

- Todo input del usuario se valida con Pydantic (strict mode)
- Toda API call externa pasa por Rate Limiter + Circuit Breaker
- Cero secrets en código; todo via environment variables
- Análisis estático obligatorio: `bandit` + `semgrep`

## Testing

- TDD para lógica de negocio (Red-Green-Refactor)
- BDD para funcionalidades de usuario (Gherkin)
- Stress testing para endpoints expuestos (Locust)
- Cada PR debe incluir tests que cubran los cambios

## Documentación

- Cada agente tiene su propio README.md educativo
- El SDD se mantiene actualizado (docs/architecture/SDD.md)
- ADRs para toda decisión arquitectónica significativa (docs/adrs/)

## Referencia

- SDD completo: #[[file:docs/architecture/SDD.md]]
