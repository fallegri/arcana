# 🔮 Arcana

## Sistema de Calidad de Software Asistido por IA — Detectar, Corregir, Verificar, Reportar

> **Arcana** (del latín *arcanum*: conocimiento secreto) revela los estándares profesionales
> de ingeniería de software, los aplica automáticamente y genera reportes de auditoría formales.

---

## ¿Qué es Arcana?

Arcana es un **sistema modular de agentes inteligentes** que:

1. **🔍 Detecta** violaciones de SOLID, OWASP, y estándares ISO en tu código
2. **🔧 Corrige** automáticamente las vulnerabilidades y problemas encontrados
3. **✅ Verifica** que las correcciones fueron efectivas (re-análisis)
4. **📄 Reporta** en formato de auditoría formal (ISO 27001 / COBIT / ISO 19011 / ISO 25010)

### Tres formas de usar Arcana:

| Modo | Uso | Para quién |
|------|-----|-----------|
| **CLI** | `python run_pipeline.py --project ./mi-app/` | Desarrolladores, DevOps |
| **MCP Server** | Integrado con opencode, Cursor, Claude Desktop | IA asistida (vibe coding) |
| **Educativo** | 8 guías paso a paso con ejercicios | Talleres, formación |

---

## 🚀 Quick Start

### Instalación

```bash
git clone https://github.com/fallegri/arcana.git
cd arcana
pip install -e .
```

### Uso como CLI

```bash
# Analizar un proyecto completo
python run_pipeline.py --project ./mi-proyecto/

# Solo análisis de seguridad
python run_pipeline.py --project ./mi-proyecto/ --only owasp

# Solo análisis de diseño
python run_pipeline.py --project ./mi-proyecto/ --only solid

# Detectar + Corregir automáticamente
python run_pipeline.py --project ./mi-proyecto/ --fix

# Generar reporte de auditoría formal
python run_pipeline.py --project ./mi-proyecto/ --report audit

# Pipeline completo: detectar → corregir → reportar
python run_pipeline.py --project ./mi-proyecto/ --fix --report audit

# Modo educativo (con explicaciones detalladas)
python run_pipeline.py --project ./mi-proyecto/ --mode beginner
```

### Uso como MCP Server (opencode / Cursor / Claude Desktop)

```jsonc
// Agregar a tu mcp.json o configuración del cliente MCP:
{
  "mcpServers": {
    "arcana": {
      "command": "python",
      "args": ["arcana_mcp_server.py"],
      "cwd": "/ruta/a/arcana/"
    }
  }
}
```

**Tools MCP disponibles:**

| Tool | Descripción |
|------|-------------|
| `arcana_analyze` | Analiza código buscando violaciones SOLID + OWASP |
| `arcana_fix` | Corrige automáticamente + genera backup |
| `arcana_report` | Genera reporte de auditoría ISO 27001/COBIT |
| `arcana_validate` | Re-verifica después de correcciones |

---

## 📊 El Flujo Arcana

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  🔍 DETECT  │────▶│  🔧 FIX     │────▶│  ✅ VERIFY  │────▶│  📄 REPORT  │
│             │     │             │     │             │     │             │
│ SOLID: 25   │     │ 12 fixes    │     │ SOLID: 85+  │     │ ISO 27001   │
│ OWASP: 25   │     │ aplicados   │     │ OWASP: 85+  │     │ COBIT 2019  │
│ 14 hallazgos│     │ backup auto │     │ re-análisis │     │ ISO 19011   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

---

## 🏗️ Arquitectura

```
arcana/
├── run_pipeline.py          # 🖥️ CLI principal (--project --fix --report)
├── arcana_mcp_server.py     # 🔌 MCP Server (4 tools)
├── arcana_reports.py        # 📄 Generador de reportes de auditoría
├── mcp.json                 # ⚙️ Config MCP para opencode/cursor
├── agents/
│   ├── base.py              # BaseAgent + FixAction + FixResult
│   ├── registry.py          # Registro dinámico de agentes
│   ├── solid/agent.py       # Analizador SOLID (AST) + fix()
│   ├── security/owasp/      # Scanner OWASP Top 10 + fix()
│   ├── bdd/                 # Agente BDD (behave + Gherkin)
│   ├── tdd/                 # Agente TDD (pytest + cobertura)
│   ├── stress_testing/      # Escenarios Locust
│   ├── api_validation/      # Rate limiting + Circuit Breaker
│   └── ux_quality/          # Métricas ISO 25010 dashboard
├── examples/
│   ├── taskflow/            # Proyecto ejemplo (bien hecho ✅)
│   └── vulnerable_demo/     # Código malo para demos (❌ → ✅)
├── docs/
│   ├── architecture/SDD.md  # Software Design Document (ISO 42010)
│   ├── adrs/                # Architecture Decision Records
│   └── guides/              # 8 guías paso a paso (taller)
├── tests/unit/              # 53 tests unitarios
└── config/default.yaml      # Configuración del pipeline
```

---

## 📄 Reportes de Auditoría

Arcana genera reportes formales siguiendo estándares internacionales:

### Reporte de Incidencias (pre-fix)

```
┌─────────────────────────────────────────────────────────────┐
│  REPORTE DE AUDITORÍA DE SOFTWARE                            │
│  ID: ARC-AUD-20260804-041700                                 │
│  Estándares: ISO 27001 + COBIT 2019 + ISO 19011 + ISO 25010│
├─────────────────────────────────────────────────────────────┤
│  HAL-001 🔴 CRITICAL  SQL Injection (A03)                    │
│       ISO 27001: A.8.28 — Codificación segura               │
│       COBIT:     DSS05 — Gestionar servicios de seguridad   │
│                                                              │
│  HAL-002 🟠 HIGH      Secret hardcoded (A05)                 │
│       ISO 27001: A.8.4 — Acceso al código fuente            │
│       COBIT:     DSS05 — Gestionar servicios de seguridad   │
└─────────────────────────────────────────────────────────────┘
```

### Reporte de Correcciones (post-fix)

```
┌─────────────────────────────────────────────────────────────┐
│  INFORME DE ACCIONES CORRECTIVAS                             │
│  ID: ARC-FIX-20260804-041800                                 │
├─────────────────────────────────────────────────────────────┤
│  Métrica          │ ANTES  │ DESPUÉS │ Δ Mejora             │
│  Score SOLID      │ 25.0   │ 85.0    │ +60.0                │
│  Score OWASP      │ 25.0   │ 90.0    │ +65.0                │
├─────────────────────────────────────────────────────────────┤
│  Evidencia: backup en .arcana_backup/                        │
│  Verificación: re-análisis automatizado PASS                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 📚 Módulos Educativos (Taller)

| # | Módulo | Guía | Qué enseña |
|---|--------|------|------------|
| 1 | **BDD** | [BDD-paso-a-paso.md](docs/guides/BDD-paso-a-paso.md) | Escenarios Gherkin, Three Amigos |
| 2 | **TDD** | [TDD-paso-a-paso.md](docs/guides/TDD-paso-a-paso.md) | Ciclo Red-Green-Refactor, pytest |
| 3 | **SOLID** | [SOLID-paso-a-paso.md](docs/guides/SOLID-paso-a-paso.md) | 5 principios con código real |
| 4 | **OWASP** | [OWASP-paso-a-paso.md](docs/guides/OWASP-paso-a-paso.md) | Top 10 + controles |
| 5 | **ISO 25010** | [ISO25010-paso-a-paso.md](docs/guides/ISO25010-paso-a-paso.md) | Modelo de calidad |
| 6 | **Stress** | [StressTesting-paso-a-paso.md](docs/guides/StressTesting-paso-a-paso.md) | Locust + patrones |
| 7 | **API Resilience** | [APIValidation-paso-a-paso.md](docs/guides/APIValidation-paso-a-paso.md) | Rate Limit, Circuit Breaker |
| 8 | **UX/ISO 9241** | [UX-ISO9241-paso-a-paso.md](docs/guides/UX-ISO9241-paso-a-paso.md) | Usabilidad + accesibilidad |

---

## 📊 Scores Demostrados

| Proyecto | SOLID | OWASP | ISO 25010 | Veredicto |
|----------|-------|-------|-----------|-----------|
| **TaskFlow** (ejemplo bueno) | 91.7 | 100 | 96.8% | ✅ PRODUCCIÓN |
| **bad_app.py** (ejemplo malo) | 25.0 | 25.0 | — | ❌ INACEPTABLE |
| **bad_app.py** (post-fix) | ~85 | ~85 | — | ✅ CORREGIDO |

---

## 🛠️ Tecnologías

| Categoría | Tecnologías |
|-----------|------------|
| **Core** | Python 3.11+, asyncio, AST |
| **Proyecto ejemplo** | FastAPI, SQLAlchemy, Pydantic, JWT |
| **Testing** | pytest, behave (BDD), Locust (stress) |
| **Seguridad** | bandit, pip-audit, análisis regex+AST |
| **Interfaz** | Rich (CLI), MCP protocol (integraciones) |
| **Estándares** | ISO 42010, 25010, 25022, 25023, 9241, 27001, 19011, COBIT, OWASP |

---

## 📜 Licencia

MIT

---

> *"No basta saber — hay que hacer."*
> *Los arcanos del desarrollo profesional, revelados paso a paso.* 🔮
