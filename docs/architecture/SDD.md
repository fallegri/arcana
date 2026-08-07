# Software Design Document (SDD)
## AI-Dev-Guide: Sistema Educativo de Desarrollo Asistido por IA

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0.0 |
| **Fecha** | 2026-08-03 |
| **Estado** | En Diseño |
| **Estándar Base** | ISO/IEC/IEEE 42010:2022 — Descripción de Arquitectura |
| **Autor** | Equipo AI-Dev-Guide (asistido por Kiro) |

---

## Tabla de Contenidos

1. [Propósito, Alcance y Stakeholders](#1-propósito-alcance-y-stakeholders)
2. [Vistas Arquitectónicas](#2-vistas-arquitectónicas)
3. [Decisiones Arquitectónicas (ADRs)](#3-decisiones-arquitectónicas-adrs)
4. [Modelo de Calidad](#4-modelo-de-calidad-iso-250102502225023)
5. [Requisitos de Seguridad](#5-requisitos-de-seguridad-owasp)
6. [Estrategia de Testing](#6-estrategia-de-testing-tddbddstress)
7. [Diseño UX/UI](#7-diseño-uxui-iso-9241)
8. [Validación de APIs y Resiliencia](#8-validación-de-apis-y-resiliencia)
9. [Apéndices](#9-apéndices)

---


## 1. Propósito, Alcance y Stakeholders

### 1.1 Propósito del Sistema

**AI-Dev-Guide** es un sistema modular de agentes orquestados que sirve simultáneamente como:

1. **Herramienta educativa**: Guía paso a paso para aprender desarrollo de software profesional asistido por IA
2. **Ejemplo vivo**: El propio código del sistema demuestra cada estándar y práctica que enseña
3. **Framework reutilizable**: Los agentes pueden aplicarse a proyectos reales de los usuarios

> **Principio rector**: "Eat your own dog food" — el sistema se construye, testea y documenta
> usando exactamente las mismas prácticas que enseña.

### 1.2 Alcance

#### Dentro del alcance:
- Pipeline completo de desarrollo: diseño → código → testing → seguridad → calidad
- Proyecto ejemplo funcional (API REST + frontend mínimo)
- Documentación educativa integrada en cada módulo
- Validación automatizada de calidad según ISO 25023
- Análisis de seguridad según OWASP Top 10

#### Fuera del alcance:
- Certificación oficial de estándares ISO
- Herramientas de pentest ofensivo en producción
- Soporte para lenguajes distintos a Python (v1.0)
- Despliegue en la nube (se documenta pero no se ejecuta)


### 1.3 Stakeholders (ISO 42010 - Partes Interesadas)

| ID | Stakeholder | Rol | Concerns (Intereses) | Viewpoints Relevantes |
|----|-------------|-----|---------------------|----------------------|
| S1 | **Profesional multidisciplinario** | Usuario final / Aprendiz | "¿Cómo uso IA para desarrollar software con estándares profesionales sin ser programador experto?" | Funcional, UX |
| S2 | **Desarrollador junior** | Usuario avanzado | "¿Cómo estructuro mi código siguiendo SOLID, TDD y estándares de industria?" | Desarrollo, Testing |
| S3 | **Líder técnico / Arquitecto** | Evaluador | "¿Cómo valido que el sistema cumple ISO 25010 y OWASP?" | Calidad, Seguridad |
| S4 | **Empresario / Product Owner** | Decisor | "¿Cómo me aseguro de que mi producto cumple estándares de calidad y seguridad?" | Funcional, Calidad |
| S5 | **Profesional legal** | Compliance | "¿Cómo verifico que el software cumple normativas y estándares?" | Seguridad, Calidad |
| S6 | **Educador / Facilitador** | Multiplicador | "¿Cómo uso esto para enseñar desarrollo profesional?" | Todas las vistas |

### 1.4 Concerns (Preocupaciones Arquitectónicas)

Siguiendo ISO 42010, identificamos las preocupaciones que la arquitectura debe abordar:

| ID | Concern | Descripción | Stakeholders |
|----|---------|-------------|--------------|
| C1 | **Comprensibilidad** | El sistema debe ser entendible por no-programadores | S1, S4, S5 |
| C2 | **Progresividad** | Aprendizaje gradual, de simple a complejo | S1, S2, S6 |
| C3 | **Demostrabilidad** | Cada módulo demuestra lo que enseña | Todos |
| C4 | **Independencia modular** | Cada agente funciona solo o en conjunto | S2, S3 |
| C5 | **Seguridad inherente** | El sistema no introduce vulnerabilidades | S3, S5 |
| C6 | **Medibilidad** | Calidad cuantificable con métricas ISO | S3, S4 |
| C7 | **Resiliencia de APIs** | No saturar servicios externos | S2, S3 |
| C8 | **Accesibilidad** | Interfaz usable según ISO 9241 | S1, S4, S6 |


### 1.5 Proyecto Ejemplo: "TaskFlow"

Para demostrar todos los conceptos, construiremos **TaskFlow** — un sistema de gestión de tareas colaborativo que incluye:

| Componente | Justificación Educativa |
|-----------|------------------------|
| **API REST** (FastAPI) | Demuestra: SOLID, OWASP, validación de APIs, rate limiting, TDD |
| **Base de datos** (SQLite → PostgreSQL) | Demuestra: migraciones, inyección SQL (OWASP), testing |
| **Frontend CLI** (Rich/Textual) | Demuestra: ISO 9241 (usabilidad), UX accesible, ISO 25022 |
| **Autenticación** (JWT) | Demuestra: OWASP auth, pentest, tokens seguros |
| **Documentación** (MkDocs) | Demuestra: ISO 42010, SDD viviente |

#### ¿Por qué TaskFlow?

1. **Universalmente comprensible**: Todos gestionan tareas, sin importar su profesión
2. **Suficientemente complejo**: Tiene CRUD, auth, relaciones, permisos — suficiente para demostrar seguridad
3. **Suficientemente simple**: No requiere dominio técnico específico para entender el problema
4. **Escalable didácticamente**: Se puede empezar con un TODO simple y evolucionar

---


## 2. Vistas Arquitectónicas

> ISO 42010 define que una arquitectura se describe mediante **vistas** (views),
> cada una gobernada por un **punto de vista** (viewpoint) que responde a los concerns
> de stakeholders específicos.

### 2.1 Vista Funcional (Viewpoint: Capacidades del Sistema)

**Stakeholders atendidos**: S1, S2, S4, S6
**Concerns atendidos**: C1, C2, C3

```
┌─────────────────────────────────────────────────────────────────┐
│                    ORQUESTADOR (pipeline.py)                      │
│  Coordina la ejecución secuencial o selectiva de agentes         │
└──────────┬──────────┬──────────┬──────────┬──────────┬──────────┘
           │          │          │          │          │
     ┌─────▼────┐┌───▼────┐┌───▼────┐┌───▼────┐┌───▼────┐
     │  FASE 1  ││ FASE 2 ││ FASE 3 ││ FASE 4 ││ FASE 5 │
     │  DISEÑO  ││ CÓDIGO ││  TEST  ││ SEGUR. ││CALIDAD │
     └─────┬────┘└───┬────┘└───┬────┘└───┬────┘└───┬────┘
           │          │          │          │          │
           ▼          ▼          ▼          ▼          ▼
     ┌──────────────────────────────────────────────────────┐
     │              PROYECTO EJEMPLO (TaskFlow)               │
     │  El artefacto sobre el cual operan todos los agentes  │
     └──────────────────────────────────────────────────────┘
```

#### Descripción de Fases:

| Fase | Agentes | Input | Output |
|------|---------|-------|--------|
| 1. Diseño | `architecture`, `requirements` | Idea/problema del usuario | SDD, diagramas, escenarios BDD |
| 2. Código | `coder`, `tdd` | SDD + escenarios | Código funcional con tests unitarios |
| 3. Testing | `bdd`, `stress`, `api_validator` | Código + escenarios | Reportes de calidad, métricas |
| 4. Seguridad | `owasp`, `pentest`, `osint` | Código + config | Vulnerabilidades, remediaciones |
| 5. Calidad | `ux_quality`, `metrics` | Sistema completo | Scores ISO 25010, recomendaciones UX |


### 2.2 Vista de Información (Viewpoint: Flujo de Datos)

**Stakeholders atendidos**: S2, S3
**Concerns atendidos**: C4, C6, C7

```
┌──────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────┐
│  CONFIG  │────▶│ ORQUESTADOR  │────▶│   AGENTE N   │────▶│ REPORTE  │
│  (YAML)  │     │              │     │              │     │  (JSON)  │
└──────────┘     └──────┬───────┘     └──────┬───────┘     └──────────┘
                        │                     │
                        ▼                     ▼
                 ┌──────────────┐     ┌──────────────┐
                 │   CONTEXTO   │     │  ARTEFACTOS  │
                 │  COMPARTIDO  │     │  GENERADOS   │
                 │   (state/)   │     │  (output/)   │
                 └──────────────┘     └──────────────┘
```

#### Modelo de Datos Principal:

```python
# Contratos entre agentes (tipado fuerte)
@dataclass
class AgentInput:
    phase: str                    # Fase actual del pipeline
    project_path: Path            # Ruta al proyecto ejemplo
    config: Dict[str, Any]        # Configuración del agente
    context: SharedContext        # Estado compartido entre agentes
    previous_results: List[AgentOutput]  # Resultados de fases anteriores

@dataclass
class AgentOutput:
    agent_name: str               # Identificador del agente
    status: Literal["success", "warning", "error"]
    artifacts: List[Path]         # Archivos generados
    metrics: Dict[str, float]     # Métricas cuantificables (ISO 25023)
    recommendations: List[str]    # Sugerencias de mejora
    educational_notes: List[str]  # Explicaciones didácticas
```

### 2.3 Vista de Desarrollo (Viewpoint: Estructura del Código)

**Stakeholders atendidos**: S2, S3, S6
**Concerns atendidos**: C3, C4 (Demostrabilidad, Independencia modular)

```
ai-dev-guide/
├── pyproject.toml              # Configuración del proyecto (PEP 621)
├── orchestrator/
│   ├── __init__.py
│   ├── pipeline.py             # Motor de ejecución de fases
│   ├── config.py               # Carga y validación de configuración
│   ├── context.py              # Estado compartido (SharedContext)
│   └── cli.py                  # Interfaz de línea de comandos (Rich)
├── agents/
│   ├── base.py                 # Clase abstracta BaseAgent (SOLID: LSP)
│   ├── registry.py             # Registro dinámico de agentes (SOLID: OCP)
│   ├── architecture/
│   │   ├── __init__.py
│   │   ├── agent.py            # ArchitectureAgent(BaseAgent)
│   │   ├── templates/          # Plantillas ISO 42010
│   │   └── README.md           # Guía educativa de esta fase
│   ├── tdd/
│   │   ├── agent.py            # TDDAgent(BaseAgent)
│   │   ├── generators/         # Generadores de tests
│   │   └── README.md
│   ├── bdd/
│   │   ├── agent.py            # BDDAgent(BaseAgent)
│   │   ├── features/           # Archivos .feature (Gherkin)
│   │   └── README.md
│   ├── solid/
│   │   ├── agent.py            # SOLIDAgent(BaseAgent)
│   │   ├── analyzers/          # Analizadores por principio
│   │   └── README.md
│   ├── security/
│   │   ├── owasp/
│   │   │   ├── agent.py        # OWASPAgent(BaseAgent)
│   │   │   ├── rules/          # Reglas por categoría OWASP
│   │   │   └── README.md
│   │   ├── pentest/
│   │   │   ├── agent.py        # PentestAgent(BaseAgent)
│   │   │   └── README.md
│   │   └── osint/
│   │       ├── agent.py        # OSINTAgent(BaseAgent)
│   │       └── README.md
│   ├── api_validation/
│   │   ├── agent.py            # APIValidatorAgent(BaseAgent)
│   │   ├── policies/           # Rate limiting, circuit breaker
│   │   └── README.md
│   ├── stress_testing/
│   │   ├── agent.py            # StressTestAgent(BaseAgent)
│   │   ├── scenarios/          # Escenarios de carga (Locust)
│   │   └── README.md
│   └── ux_quality/
│       ├── agent.py            # UXQualityAgent(BaseAgent)
│       ├── checklists/         # Checklists ISO 9241, 25010
│       └── README.md
├── examples/
│   └── taskflow/               # Proyecto ejemplo completo
│       ├── api/                # FastAPI backend
│       ├── cli_app/            # Frontend CLI (Rich/Textual)
│       ├── tests/              # Tests del ejemplo
│       └── docs/               # Docs del ejemplo
├── docs/
│   ├── architecture/
│   │   └── SDD.md              # ← ESTE DOCUMENTO
│   ├── adrs/                   # Architecture Decision Records
│   └── guides/                 # Guías paso a paso
├── tests/                      # Tests del framework mismo
│   ├── unit/
│   ├── integration/
│   └── conftest.py
└── .kiro/
    └── steering/               # Reglas del proyecto
```


### 2.4 Vista de Despliegue (Viewpoint: Entorno de Ejecución)

**Stakeholders atendidos**: S2, S3
**Concerns atendidos**: C5, C7

```
┌─────────────────────────────────────────────────────────┐
│                 MÁQUINA DEL USUARIO                       │
│                                                           │
│  ┌─────────────┐    ┌─────────────┐    ┌────────────┐  │
│  │  Python     │    │   SQLite    │    │   CLI      │  │
│  │  3.11+      │    │   (local)   │    │  (Rich)    │  │
│  └──────┬──────┘    └──────┬──────┘    └─────┬──────┘  │
│         │                   │                  │         │
│         ▼                   ▼                  ▼         │
│  ┌──────────────────────────────────────────────────┐   │
│  │            AI-DEV-GUIDE (virtualenv)              │   │
│  │                                                    │   │
│  │  orchestrator ←→ agents ←→ examples/taskflow      │   │
│  └──────────────────────────┬───────────────────────┘   │
│                              │                           │
└──────────────────────────────┼───────────────────────────┘
                               │ (controlado por api_validation)
                               ▼
                ┌──────────────────────────────┐
                │    SERVICIOS EXTERNOS         │
                │  (APIs de IA, bases remotas)  │
                │                               │
                │  • Rate limiting aplicado     │
                │  • Circuit breaker activo     │
                │  • Retry con backoff          │
                └──────────────────────────────┘
```

#### Requisitos del Entorno:

| Requisito | Mínimo | Recomendado |
|-----------|--------|-------------|
| Python | 3.11 | 3.12+ |
| RAM | 4 GB | 8 GB |
| Disco | 500 MB | 2 GB |
| Red | Opcional (modo offline parcial) | Conexión estable |
| SO | Linux, macOS, Windows (WSL) | Linux/macOS |

### 2.5 Vista de Seguridad (Viewpoint: Amenazas y Controles)

**Stakeholders atendidos**: S3, S5
**Concerns atendidos**: C5, C7

```
┌─────────────────────────────────────────────────────────┐
│                    PERÍMETRO DE SEGURIDAD                 │
│                                                           │
│  ┌─────────┐   ┌──────────┐   ┌──────────────────────┐ │
│  │ INPUT   │──▶│VALIDACIÓN│──▶│   PROCESAMIENTO      │ │
│  │USUARIO  │   │(sanitize)│   │   (sandboxed)        │ │
│  └─────────┘   └──────────┘   └──────────┬───────────┘ │
│                                            │             │
│  ┌─────────────────────────────────────────▼───────────┐│
│  │              CAPA DE CONTROL DE APIS                  ││
│  │  • Token rotation    • Rate limiting (token bucket)  ││
│  │  • Request signing   • Response validation           ││
│  │  • Circuit breaker   • Audit logging                 ││
│  └──────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────┘
```

---


## 3. Decisiones Arquitectónicas (ADRs)

> Formato: [MADR](https://adr.github.io/madr/) (Markdown Any Decision Record)
> Cada ADR se documenta también en `docs/adrs/` como archivo independiente.

### ADR-001: Arquitectura de Agentes Orquestados

| Campo | Valor |
|-------|-------|
| **Estado** | Aceptada |
| **Fecha** | 2026-08-03 |
| **Contexto** | Necesitamos un sistema que sea modular, educativo y que demuestre las prácticas que enseña |

**Decisión**: Adoptar arquitectura de agentes independientes coordinados por un orquestador central.

**Consecuencias**:
- ✅ Cada agente demuestra Responsabilidad Única (SOLID: SRP)
- ✅ Nuevos estándares = nuevos agentes sin modificar existentes (SOLID: OCP)
- ✅ El usuario puede ejecutar agentes individuales o el pipeline completo
- ⚠️ Requiere definir contratos claros entre agentes (interfaces)
- ⚠️ Mayor complejidad inicial vs. monolito

### ADR-002: Python como Lenguaje Único (v1.0)

| Campo | Valor |
|-------|-------|
| **Estado** | Aceptada |
| **Fecha** | 2026-08-03 |
| **Contexto** | El público es multidisciplinario, necesitamos un lenguaje accesible con ecosistema rico |

**Decisión**: Usar Python 3.11+ como único lenguaje del sistema y del proyecto ejemplo.

**Justificación**:
- Ecosistema completo: FastAPI, pytest, behave, locust, bandit, rich
- Sintaxis legible para no-programadores
- Tipado gradual (type hints) para demostrar buenas prácticas sin complejidad
- Mayor comunidad de IA/ML

**Consecuencias**:
- ✅ Barrera de entrada baja para el público objetivo
- ✅ Un solo entorno, un solo lenguaje que aprender
- ⚠️ No demuestra interoperabilidad multi-lenguaje (futuro v2.0)

### ADR-003: FastAPI para el Proyecto Ejemplo

| Campo | Valor |
|-------|-------|
| **Estado** | Aceptada |
| **Fecha** | 2026-08-03 |
| **Contexto** | Necesitamos un framework web que sea moderno, tipado y fácil de testear |

**Decisión**: Usar FastAPI para la API REST del proyecto ejemplo (TaskFlow).

**Justificación**:
- Validación automática con Pydantic (demuestra contratos de datos)
- OpenAPI/Swagger integrado (demuestra documentación de APIs)
- Async nativo (demuestra concurrencia para stress testing)
- Dependency Injection integrado (demuestra SOLID: DIP)

### ADR-004: CLI sobre Web UI para la Interfaz Principal

| Campo | Valor |
|-------|-------|
| **Estado** | Aceptada |
| **Fecha** | 2026-08-03 |
| **Contexto** | Necesitamos una interfaz que sea usable, accesible y que no requiera infraestructura web |

**Decisión**: La interfaz principal del framework es CLI con Rich/Textual, no una webapp.

**Justificación**:
- Elimina complejidad de despliegue web
- Rich permite UI sofisticada en terminal (tablas, progreso, colores)
- ISO 9241 aplica también a interfaces de texto
- El público ya usa terminal para vibe coding con IA
- Textual permite TUI (Text User Interface) interactiva si se necesita

**Consecuencias**:
- ✅ Cero dependencias de infraestructura web para el framework
- ✅ Funciona en cualquier entorno con terminal
- ⚠️ El proyecto ejemplo (TaskFlow) SÍ tiene API web para demostrar OWASP

### ADR-005: Configuración Declarativa con YAML

| Campo | Valor |
|-------|-------|
| **Estado** | Aceptada |
| **Fecha** | 2026-08-03 |
| **Contexto** | Los usuarios deben poder personalizar qué fases ejecutar y con qué parámetros |

**Decisión**: Toda configuración del pipeline se define en archivos YAML validados con Pydantic.

**Justificación**:
- YAML es legible por humanos no-técnicos
- Pydantic valida la configuración al cargar (fail-fast)
- Permite configuraciones parciales (solo ejecutar seguridad, solo testing, etc.)

---


## 4. Modelo de Calidad (ISO 25010/25022/25023)

### 4.1 Modelo de Calidad del Producto (ISO 25010)

El sistema se evaluará contra las 8 características de calidad definidas en ISO/IEC 25010:

| Característica | Sub-característica Prioritaria | Métrica (ISO 25023) | Meta |
|---------------|-------------------------------|--------------------|----|
| **Adecuación Funcional** | Completitud funcional | % de funciones implementadas vs. especificadas | ≥ 95% |
| **Eficiencia de Desempeño** | Comportamiento temporal | Tiempo de respuesta p95 de API | ≤ 200ms |
| **Eficiencia de Desempeño** | Utilización de recursos | Uso de memoria en ejecución | ≤ 512MB |
| **Compatibilidad** | Interoperabilidad | APIs con contrato OpenAPI válido | 100% |
| **Usabilidad** | Operabilidad | Tareas completadas sin error (ISO 9241) | ≥ 90% |
| **Usabilidad** | Aprendibilidad | Tiempo para completar tutorial básico | ≤ 30 min |
| **Fiabilidad** | Madurez | Densidad de defectos por KLOC | ≤ 2 |
| **Fiabilidad** | Disponibilidad | Uptime del ejemplo desplegado | ≥ 99% |
| **Seguridad** | Confidencialidad | Vulnerabilidades OWASP críticas | 0 |
| **Seguridad** | Integridad | Inputs sin sanitizar | 0 |
| **Mantenibilidad** | Modularidad | Acoplamiento entre agentes | Bajo (≤ 3 deps) |
| **Mantenibilidad** | Testeabilidad | Cobertura de código | ≥ 80% |
| **Portabilidad** | Adaptabilidad | SOs soportados sin cambios | ≥ 3 |

### 4.2 Modelo de Calidad en Uso (ISO 25022)

Métricas de cómo los usuarios REALES experimentan el sistema:

| Característica | Métrica | Método de Medición | Meta |
|---------------|---------|-------------------|------|
| **Efectividad** | Tasa de completitud de tareas | % usuarios que completan el pipeline completo | ≥ 85% |
| **Eficiencia** | Productividad | Tareas/hora vs. desarrollo manual | 3x mejora |
| **Satisfacción** | Utilidad percibida | Encuesta post-uso (1-5) | ≥ 4.0 |
| **Satisfacción** | Confianza | "¿Confiaría en este output para producción?" | ≥ 70% sí |
| **Libertad de riesgo** | Riesgo económico | Falsos positivos en seguridad | ≤ 5% |
| **Cobertura de contexto** | Flexibilidad | % de tipos de proyecto soportados | ≥ 80% APIs |

### 4.3 Métricas de Medición Interna (ISO 25023)

Métricas técnicas que los agentes calculan automáticamente:

```python
@dataclass
class QualityMetrics:
    """Métricas calculadas por agent-metrics según ISO 25023"""

    # Adecuación funcional
    functional_completeness: float    # Funciones impl / funciones spec
    functional_correctness: float     # Tests pasando / tests totales

    # Eficiencia de desempeño
    response_time_p50: float          # Percentil 50 en ms
    response_time_p95: float          # Percentil 95 en ms
    response_time_p99: float          # Percentil 99 en ms
    memory_peak_mb: float             # Pico de memoria
    cpu_utilization: float            # % CPU promedio

    # Seguridad
    vulnerabilities_critical: int     # OWASP críticas
    vulnerabilities_high: int         # OWASP altas
    vulnerabilities_medium: int       # OWASP medias
    attack_surface_score: float       # Score OSINT (0-10)

    # Mantenibilidad
    code_coverage: float              # % cobertura
    cyclomatic_complexity_avg: float  # Complejidad ciclomática
    coupling_between_modules: int     # Dependencias entre módulos
    documentation_coverage: float     # % funciones documentadas

    # Usabilidad
    task_completion_rate: float       # ISO 9241: tareas exitosas
    error_rate: float                 # Errores por sesión
    learnability_time_minutes: float  # Tiempo hasta primera tarea exitosa
```

---


## 5. Requisitos de Seguridad (OWASP)

### 5.1 Mapeo OWASP Top 10 (2021) al Sistema

| # | Categoría OWASP | Aplica a | Control Implementado | Agente Responsable |
|---|----------------|----------|---------------------|-------------------|
| A01 | **Broken Access Control** | TaskFlow API | RBAC + JWT + middleware de permisos | `owasp` |
| A02 | **Cryptographic Failures** | Tokens, passwords | bcrypt + JWT RS256 + secrets rotation | `owasp` |
| A03 | **Injection** | Queries DB, inputs | SQLAlchemy ORM + Pydantic validation | `owasp`, `pentest` |
| A04 | **Insecure Design** | Arquitectura | Threat modeling en fase de diseño | `architecture` |
| A05 | **Security Misconfiguration** | Config, env vars | Pydantic Settings + .env validation | `owasp` |
| A06 | **Vulnerable Components** | Dependencies | `pip-audit` + dependabot alerts | `osint` |
| A07 | **Auth Failures** | Login, sessions | Rate limiting + account lockout + MFA ready | `pentest` |
| A08 | **Data Integrity Failures** | CI/CD, updates | Hash verification + signed commits | `osint` |
| A09 | **Logging Failures** | Audit trail | Structured logging + alertas | `owasp` |
| A10 | **SSRF** | API calls externas | URL allowlisting + request validation | `api_validation` |

### 5.2 Estrategia de Seguridad por Capas

```
┌─────────────────────────────────────────────────────────────┐
│ CAPA 1: PREVENCIÓN (Shift-Left)                              │
│ • Análisis estático (bandit, semgrep)                        │
│ • Validación de inputs (Pydantic strict mode)                │
│ • Dependencias auditadas (pip-audit)                         │
├─────────────────────────────────────────────────────────────┤
│ CAPA 2: DETECCIÓN (Runtime)                                  │
│ • Logging estructurado de eventos de seguridad               │
│ • Rate limiting por IP y por usuario                         │
│ • Anomaly detection en patrones de acceso                    │
├─────────────────────────────────────────────────────────────┤
│ CAPA 3: RESPUESTA (Post-incident)                            │
│ • Audit trail inmutable                                      │
│ • Token revocation automática                                │
│ • Alertas configurables                                      │
├─────────────────────────────────────────────────────────────┤
│ CAPA 4: VERIFICACIÓN (Continuous)                            │
│ • Pentest automatizado (agente pentest)                      │
│ • OSINT de superficie de ataque                              │
│ • Reporte de vulnerabilidades con remediación                │
└─────────────────────────────────────────────────────────────┘
```

### 5.3 OSINT — Reconocimiento de Superficie de Ataque

El agente `osint` realiza reconocimiento NO intrusivo:

| Técnica | Propósito | Herramienta |
|---------|-----------|-------------|
| DNS enumeration | Descubrir subdominios expuestos | `dnspython` |
| Header analysis | Detectar tecnologías y versiones | `requests` + análisis |
| Certificate transparency | Verificar certificados SSL | CT logs API |
| Dependency scanning | Vulnerabilidades conocidas (CVE) | `pip-audit`, `safety` |
| API discovery | Endpoints no documentados | Fuzzing controlado |
| Metadata analysis | Información filtrada en metadatos | Análisis de respuestas |

> ⚠️ **Nota ética**: El agente OSINT solo opera sobre el sistema propio del usuario.
> Nunca realiza reconocimiento sobre sistemas de terceros sin autorización explícita.

---


## 6. Estrategia de Testing (TDD/BDD/Stress)

### 6.1 Pirámide de Testing

```
              ╱╲
             ╱  ╲          E2E / Stress Tests
            ╱ E2E╲         (Locust, Playwright)
           ╱──────╲        ~10% de los tests
          ╱        ╲
         ╱Integration╲     Integration Tests
        ╱──────────────╲   (pytest + TestClient)
       ╱                ╲   ~20% de los tests
      ╱   Unit Tests     ╲
     ╱────────────────────╲ Unit Tests
    ╱                      ╲ (pytest + mocks)
   ╱________________________╲ ~70% de los tests
```

### 6.2 TDD — Test-Driven Development

El agente `tdd` implementa el ciclo Red-Green-Refactor:

```python
# PASO 1: RED — Escribir test que falla
def test_create_task_returns_201():
    """Un usuario puede crear una tarea con título y descripción."""
    response = client.post("/tasks", json={"title": "Mi tarea", "description": "Detalle"})
    assert response.status_code == 201
    assert response.json()["title"] == "Mi tarea"

# PASO 2: GREEN — Implementación mínima para pasar
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate) -> TaskResponse:
    return TaskResponse(id=1, title=task.title, description=task.description)

# PASO 3: REFACTOR — Mejorar sin romper tests
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)) -> TaskResponse:
    db_task = TaskModel(**task.model_dump())
    db.add(db_task)
    db.commit()
    return TaskResponse.model_validate(db_task)
```

#### Flujo del Agente TDD:

1. Lee los escenarios BDD (Gherkin)
2. Genera tests unitarios que fallan (RED)
3. Genera implementación mínima (GREEN)
4. Aplica análisis SOLID para refactorizar (REFACTOR)
5. Verifica cobertura ≥ 80%

### 6.3 BDD — Behavior-Driven Development

El agente `bdd` trabaja con escenarios Gherkin que son comprensibles por TODOS los stakeholders:

```gherkin
# features/tasks/create_task.feature

Feature: Creación de Tareas
  Como usuario del sistema TaskFlow
  Quiero poder crear tareas nuevas
  Para organizar mi trabajo pendiente

  Background:
    Given un usuario autenticado "María"
    And el sistema está disponible

  Scenario: Crear tarea exitosamente
    When María crea una tarea con título "Revisar contrato"
    And descripción "Revisar cláusulas del contrato de servicio"
    Then la tarea se crea con estado "pendiente"
    And María recibe confirmación con el ID de la tarea
    And la tarea aparece en su lista de tareas

  Scenario: Crear tarea sin título falla
    When María intenta crear una tarea sin título
    Then recibe un error de validación
    And el mensaje indica "El título es obligatorio"
    And no se crea ninguna tarea

  Scenario: Crear tarea con título duplicado
    Given María ya tiene una tarea "Revisar contrato"
    When María crea otra tarea con título "Revisar contrato"
    Then ambas tareas coexisten (títulos duplicados permitidos)
    And cada una tiene un ID único
```

#### Conexión BDD → TDD:

```
Escenario Gherkin  →  Step Definitions  →  Tests Unitarios  →  Implementación
   (negocio)           (traducción)          (técnico)          (código)
```

### 6.4 Pruebas de Stress (ISO 25023 - Eficiencia de Desempeño)

El agente `stress_testing` usa Locust para pruebas de carga:

```python
# scenarios/taskflow_load.py
from locust import HttpUser, task, between

class TaskFlowUser(HttpUser):
    """Simula usuarios concurrentes de TaskFlow."""
    wait_time = between(1, 3)  # 1-3 segundos entre acciones

    @task(3)  # Peso: 3x más frecuente
    def list_tasks(self):
        self.client.get("/tasks", headers=self.auth_headers)

    @task(2)
    def create_task(self):
        self.client.post("/tasks", json={
            "title": f"Tarea {self.task_counter}",
            "description": "Tarea generada por stress test"
        }, headers=self.auth_headers)

    @task(1)
    def complete_task(self):
        self.client.patch(f"/tasks/{self.random_task_id}/complete",
                         headers=self.auth_headers)
```

#### Métricas de Stress (reportadas según ISO 25023):

| Métrica | Descripción | Umbral Aceptable | Umbral Crítico |
|---------|-------------|-----------------|----------------|
| RPS | Requests por segundo sostenidos | ≥ 100 | < 50 |
| p95 Latency | Percentil 95 de tiempo de respuesta | ≤ 500ms | > 2000ms |
| Error Rate | % de respuestas con error | ≤ 1% | > 5% |
| Throughput | MB/s procesados | ≥ 10 MB/s | < 5 MB/s |
| Concurrent Users | Usuarios simultáneos soportados | ≥ 50 | < 20 |
| Recovery Time | Tiempo para recuperarse tras pico | ≤ 30s | > 120s |

---


## 7. Diseño UX/UI (ISO 9241)

### 7.1 Principios de Usabilidad Aplicados (ISO 9241-110)

| Principio ISO 9241-110 | Aplicación en AI-Dev-Guide | Implementación |
|------------------------|---------------------------|----------------|
| **Adecuación a la tarea** | Cada comando hace exactamente una cosa clara | CLI con verbos intuitivos: `guide run`, `guide check`, `guide report` |
| **Auto-descriptividad** | El sistema explica qué hace y por qué | `--explain` flag en cada comando, notas educativas en output |
| **Conformidad con expectativas** | Sigue convenciones CLI estándar | `--help`, `--verbose`, `--quiet`, `--output json/table/markdown` |
| **Tolerancia a errores** | Errores del usuario no causan daño | Confirmación antes de acciones destructivas, `--dry-run` |
| **Controlabilidad** | El usuario controla el ritmo y profundidad | Modo interactivo vs. batch, `--skip-phase`, `--only-phase` |
| **Individualizabilidad** | Adaptable a preferencias | `config.yaml` personalizable, perfiles de ejecución |
| **Aptitud para el aprendizaje** | Progresivo, de simple a complejo | Modo `--beginner` con explicaciones extra, modo `--expert` conciso |

### 7.2 Diseño de la Interfaz CLI

```
$ guide run --project ./taskflow --explain

╭─────────────────────────────────────────────────────────────╮
│  🚀 AI-Dev-Guide v1.0 — Pipeline de Desarrollo Profesional  │
╰─────────────────────────────────────────────────────────────╯

 Fase 1/5: Diseño y Arquitectura
 ├── ✅ Verificando estructura del proyecto...
 ├── ✅ Validando SDD contra ISO 42010...
 ├── 📝 Generando vistas arquitectónicas...
 │
 │  💡 NOTA EDUCATIVA:
 │  ISO 42010 requiere que cada vista responda a un "concern"
 │  de un stakeholder. Tu SDD tiene 3 vistas definidas.
 │  Recomendación: agregar vista de seguridad (concern C5).
 │
 └── ✅ Fase 1 completada (4 artefactos generados)

 Fase 2/5: Implementación con TDD
 ├── 🔴 Generando tests (RED)... 12 tests creados
 ├── 🟢 Verificando implementación (GREEN)... 10/12 pasan
 ├── ⚠️  2 tests fallando:
 │   • test_task_permissions_owner_only (auth no implementada)
 │   • test_task_soft_delete (delete no implementado)
 │
 │  💡 NOTA EDUCATIVA:
 │  TDD espera que los tests fallen primero (RED).
 │  Los 2 tests fallidos indican funcionalidad pendiente.
 │  Esto es NORMAL y deseable en el flujo TDD.
 │
 └── 🔄 Fase 2 en progreso (requiere implementación)

 ⏸️  Pipeline pausado. ¿Continuar? [s/n/ver detalles]
```

### 7.3 Modelo de Interacción (ISO 9241-210: Diseño Centrado en el Humano)

```
┌─────────────────────────────────────────────────────────────┐
│                CICLO DE INTERACCIÓN                           │
│                                                               │
│  ┌──────────┐    ┌───────────┐    ┌──────────────┐          │
│  │ CONTEXTO │───▶│ EJECUCIÓN │───▶│  EVALUACIÓN  │          │
│  │ (entender│    │ (ejecutar │    │  (verificar  │          │
│  │  qué va  │    │  la fase) │    │  resultados) │          │
│  │  a pasar)│    │           │    │              │          │
│  └──────────┘    └───────────┘    └──────┬───────┘          │
│       ▲                                    │                  │
│       │          ┌───────────┐             │                  │
│       └──────────│ FEEDBACK  │◀────────────┘                  │
│                  │(aprender) │                                 │
│                  └───────────┘                                 │
└─────────────────────────────────────────────────────────────┘
```

### 7.4 Accesibilidad (ISO 9241-171)

| Requisito | Implementación |
|-----------|---------------|
| Sin dependencia de color | Símbolos además de colores: ✅ ⚠️ ❌ 🔄 |
| Salida legible por screen readers | Modo `--no-color --plain` |
| Textos claros y concisos | Mensajes en lenguaje no-técnico (modo beginner) |
| Configuración de verbosidad | `--quiet` (solo errores), `--verbose` (todo), default (balanceado) |
| Internacionalización ready | Strings externalizados (i18n-ready para v2.0) |

### 7.5 Métricas de Usabilidad (ISO 25022 aplicadas)

| Métrica | Cómo se mide | Meta |
|---------|-------------|------|
| **Efectividad de tarea** | % comandos exitosos / comandos totales | ≥ 90% |
| **Eficiencia temporal** | Tiempo promedio por fase del pipeline | ≤ 5 min/fase |
| **Tasa de error del usuario** | Errores de sintaxis CLI / total comandos | ≤ 10% |
| **Satisfacción** | Calificación post-ejecución (opcional) | ≥ 4/5 |
| **Aprendibilidad** | Sesiones hasta uso autónomo | ≤ 3 sesiones |

---


## 8. Validación de APIs y Resiliencia

### 8.1 Problema: Saturación y Bloqueo de APIs Externas

El sistema interactúa con APIs externas (LLMs, servicios de análisis). Sin control:
- **Saturación**: Exceder rate limits → bloqueo temporal o permanente
- **Costos**: Llamadas innecesarias → facturación descontrolada
- **Fragilidad**: API caída → sistema entero falla

### 8.2 Patrones de Resiliencia Implementados

#### 8.2.1 Rate Limiting (Token Bucket Algorithm)

```python
class TokenBucketRateLimiter:
    """
    Implementa Token Bucket para controlar tasa de requests.

    Educativo: Este patrón es el mismo que usan las APIs
    para limitar TUS requests. Aquí lo usamos para
    auto-limitarnos y no ser bloqueados.
    """

    def __init__(self, rate: float, capacity: int):
        self.rate = rate          # Tokens por segundo
        self.capacity = capacity  # Máximo de tokens acumulados
        self.tokens = capacity    # Tokens disponibles ahora
        self.last_refill = time.monotonic()

    async def acquire(self, tokens: int = 1) -> float:
        """Adquiere tokens. Retorna tiempo de espera si no hay suficientes."""
        self._refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return 0.0  # Sin espera
        wait_time = (tokens - self.tokens) / self.rate
        await asyncio.sleep(wait_time)
        self.tokens = 0
        return wait_time
```

#### 8.2.2 Circuit Breaker

```python
class CircuitBreaker:
    """
    Implementa Circuit Breaker para proteger contra APIs fallidas.

    Estados:
    - CLOSED: Funcionando normal, dejando pasar requests
    - OPEN: API fallando, rechazando requests inmediatamente
    - HALF-OPEN: Probando si la API se recuperó

    Educativo: Esto evita que tu aplicación se quede "colgada"
    esperando una API que no va a responder.
    """

    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

    def __init__(self, failure_threshold: int = 5,
                 recovery_timeout: float = 30.0,
                 success_threshold: int = 3):
        self.state = self.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold
        self.last_failure_time = None
```

#### 8.2.3 Retry con Exponential Backoff + Jitter

```python
class RetryPolicy:
    """
    Reintenta operaciones fallidas con backoff exponencial.

    Educativo: El "jitter" (aleatorización) evita que múltiples
    clientes reintenten al mismo tiempo (thundering herd problem).
    """

    def __init__(self, max_retries: int = 3,
                 base_delay: float = 1.0,
                 max_delay: float = 60.0,
                 exponential_base: float = 2.0):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base

    def calculate_delay(self, attempt: int) -> float:
        """Calcula delay con exponential backoff + jitter."""
        delay = self.base_delay * (self.exponential_base ** attempt)
        delay = min(delay, self.max_delay)
        jitter = random.uniform(0, delay * 0.1)  # 10% jitter
        return delay + jitter
```

### 8.3 Configuración de Resiliencia por API

```yaml
# config/api_policies.yaml
apis:
  openai:
    rate_limit:
      requests_per_minute: 60
      tokens_per_minute: 90000
    circuit_breaker:
      failure_threshold: 3
      recovery_timeout: 60
    retry:
      max_retries: 3
      base_delay: 2.0
    budget:
      max_daily_cost_usd: 10.0
      alert_threshold_usd: 8.0

  local_api:  # TaskFlow API (ejemplo)
    rate_limit:
      requests_per_minute: 1000
    circuit_breaker:
      failure_threshold: 10
      recovery_timeout: 5
    retry:
      max_retries: 1
      base_delay: 0.5
```

### 8.4 Monitoreo y Alertas

```python
@dataclass
class APIHealthMetrics:
    """Métricas de salud de APIs monitoreadas."""

    api_name: str
    total_requests: int
    successful_requests: int
    failed_requests: int
    avg_response_time_ms: float
    circuit_state: str           # closed/open/half_open
    tokens_remaining: int        # Rate limiter
    budget_remaining_usd: float  # Presupuesto restante
    last_error: Optional[str]
    uptime_percentage: float
```

### 8.5 Validación de Contratos de API

| Validación | Propósito | Herramienta |
|-----------|-----------|-------------|
| Schema validation | Respuestas cumplen contrato | Pydantic + OpenAPI |
| Contract testing | API no rompe compatibilidad | Pact (consumer-driven) |
| Idempotency check | Requests repetidos no causan daño | Tests automatizados |
| Timeout validation | Todas las calls tienen timeout | Configuración global |
| Response size limits | Prevenir memory exhaustion | Streaming + límites |

---


## 9. Apéndices

### Apéndice A: Principios SOLID Aplicados en el Sistema

| Principio | Significado | Dónde se aplica |
|-----------|-------------|-----------------|
| **S** — Single Responsibility | Una clase, una razón para cambiar | Cada agente tiene una sola responsabilidad (security vs. testing vs. UX) |
| **O** — Open/Closed | Abierto para extensión, cerrado para modificación | `registry.py` permite agregar agentes sin modificar el orquestador |
| **L** — Liskov Substitution | Subtipos sustituibles por su tipo base | Todos los agentes implementan `BaseAgent` y son intercambiables |
| **I** — Interface Segregation | Interfaces pequeñas y específicas | `AgentInput`/`AgentOutput` son contratos mínimos |
| **D** — Dependency Inversion | Depender de abstracciones, no de concreciones | El orquestador depende de `BaseAgent` (abstracto), no de agentes concretos |

### Apéndice B: Mapeo de Estándares a Agentes

| Estándar/Práctica | Agente Principal | Agentes de Soporte |
|-------------------|-----------------|-------------------|
| ISO 42010 | `architecture` | `requirements` |
| SDD | `architecture` | todos (cada uno documenta su sección) |
| TDD | `tdd` | `bdd` |
| BDD | `bdd` | `tdd`, `ux_quality` |
| SOLID | `solid` | `tdd` (refactoring) |
| OWASP Top 10 | `owasp` | `pentest`, `osint` |
| Pentest | `pentest` | `owasp`, `api_validation` |
| OSINT | `osint` | `pentest` |
| ISO 9241 | `ux_quality` | `metrics` |
| ISO 25010 | `metrics` | todos (cada uno reporta sus métricas) |
| ISO 25022 | `metrics` | `ux_quality` |
| ISO 25023 | `metrics` | `stress_testing` |
| Stress Testing | `stress_testing` | `api_validation` |
| API Validation | `api_validation` | `owasp`, `stress_testing` |

### Apéndice C: Glosario

| Término | Definición |
|---------|-----------|
| **ADR** | Architecture Decision Record — registro formal de una decisión arquitectónica |
| **BDD** | Behavior-Driven Development — desarrollo guiado por comportamiento |
| **Circuit Breaker** | Patrón que corta conexión a servicio fallido para evitar cascada de errores |
| **Concern** | (ISO 42010) Interés o preocupación de un stakeholder que la arquitectura debe abordar |
| **DAST** | Dynamic Application Security Testing — análisis de seguridad en ejecución |
| **Gherkin** | Lenguaje de especificación Given-When-Then para escenarios BDD |
| **OSINT** | Open Source Intelligence — inteligencia basada en fuentes abiertas |
| **Rate Limiting** | Control de tasa de requests para evitar saturación |
| **SAST** | Static Application Security Testing — análisis de seguridad en código fuente |
| **SDD** | Software Design Document — documento de diseño de software |
| **Stakeholder** | Persona o rol con interés en el sistema |
| **TDD** | Test-Driven Development — desarrollo guiado por tests |
| **Token Bucket** | Algoritmo de rate limiting basado en tokens que se recargan a tasa constante |
| **Viewpoint** | (ISO 42010) Perspectiva desde la cual se describe la arquitectura |

### Apéndice D: Referencias Normativas

| Estándar | Título | Uso en el proyecto |
|----------|--------|-------------------|
| ISO/IEC/IEEE 42010:2022 | Systems and software engineering — Architecture description | Estructura del SDD y vistas |
| ISO/IEC 25010:2023 | Systems and software quality models | Modelo de calidad del producto |
| ISO/IEC 25022:2016 | Measurement of quality in use | Métricas de experiencia de usuario |
| ISO/IEC 25023:2016 | Measurement of system and software product quality | Métricas internas del producto |
| ISO 9241-110:2020 | Ergonomics of human-system interaction — Interaction principles | Principios de usabilidad CLI |
| ISO 9241-210:2019 | Human-centred design for interactive systems | Proceso de diseño UX |
| ISO 9241-171:2008 | Guidance on software accessibility | Accesibilidad de la interfaz |
| OWASP Top 10:2021 | Top 10 Web Application Security Risks | Requisitos de seguridad |
| OWASP ASVS 4.0 | Application Security Verification Standard | Verificación de controles |

---

## Control de Cambios

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0.0 | 2026-08-03 | Equipo AI-Dev-Guide | Versión inicial del SDD completo |

---

> **Este documento es un artefacto vivo.** Se actualiza conforme el sistema evoluciona.
> Cada agente es responsable de mantener actualizada su sección correspondiente.
> El agente `architecture` valida la consistencia del SDD en cada ejecución del pipeline.
