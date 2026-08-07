# ADR-001: Arquitectura de Agentes Orquestados

## Estado
Aceptada

## Fecha
2026-08-03

## Contexto
Necesitamos un sistema que sea simultáneamente:
- Educativo (enseña desarrollo profesional)
- Demostrativo (su propio código ejemplifica las prácticas)
- Modular (ejecutable parcial o totalmente)
- Extensible (nuevos estándares no rompen lo existente)

## Decisión
Adoptamos una arquitectura de **agentes independientes coordinados por un orquestador central**.

Cada agente:
- Hereda de `BaseAgent` (abstracción común)
- Tiene una sola responsabilidad (SOLID: SRP)
- Se comunica via contratos tipados (`AgentInput`/`AgentOutput`)
- Se registra dinámicamente en el `AgentRegistry` (SOLID: OCP)

El orquestador:
- Lee configuración YAML
- Ejecuta fases secuencialmente o selectivamente
- Mantiene contexto compartido entre agentes
- No conoce implementaciones concretas (SOLID: DIP)

## Consecuencias

### Positivas
- Máxima demostración de SOLID en la propia arquitectura
- Usuarios pueden ejecutar un solo agente o el pipeline completo
- Nuevos estándares = nuevo agente, sin modificar los existentes
- Testeable: cada agente se testea aisladamente

### Negativas
- Mayor complejidad inicial que un monolito
- Requiere diseño cuidadoso de los contratos entre agentes
- El contexto compartido puede crecer si no se gestiona

### Riesgos
- Sobre-ingeniería si los agentes son demasiado granulares
- Mitigación: empezar con 10 agentes máximo, refactorizar según uso

## Alternativas Consideradas

1. **Monolito**: Simple pero no demuestra modularidad ni SOLID
2. **Microservicios**: Demasiada complejidad de infraestructura para un proyecto educativo
3. **Plugins independientes sin orquestador**: Pierde la narrativa del pipeline de desarrollo
