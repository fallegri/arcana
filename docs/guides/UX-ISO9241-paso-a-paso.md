# Guía UX/UI Paso a Paso
## Usabilidad según ISO 9241 — Diseño Centrado en el Humano

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0.0 |
| **Fecha** | 2026-08-03 |
| **Público** | Profesionales multidisciplinarios (universitario+) |
| **Prerrequisitos** | Haber completado BDD, TDD, SOLID, OWASP, ISO 25010, Stress, APIs |
| **Duración estimada** | 3-4 horas (taller completo) |
| **Estándares** | ISO 9241-110, ISO 9241-210, ISO 9241-171 |
| **Proyecto ejemplo** | TaskFlow — CLI usable y accesible |

---

## Tabla de Contenidos

1. [¿Qué es UX/UI?](#1-qué-es-uxui)
2. [ISO 9241: La Norma de Usabilidad](#2-iso-9241-la-norma-de-usabilidad)
3. [Los 7 Principios de Interacción](#3-los-7-principios-de-interacción)
4. [Diseño Centrado en el Humano](#4-diseño-centrado-en-el-humano)
5. [UX en CLI (Interfaz de Texto)](#5-ux-en-cli-interfaz-de-texto)
6. [Accesibilidad (ISO 9241-171)](#6-accesibilidad-iso-9241-171)
7. [Heurísticas de Nielsen](#7-heurísticas-de-nielsen)
8. [Métricas de Usabilidad (ISO 25022)](#8-métricas-de-usabilidad-iso-25022)
9. [UX y la IA Asistida](#9-ux-y-la-ia-asistida)
10. [Ejercicios Prácticos](#10-ejercicios-prácticos)
11. [Anti-patrones de UX](#11-anti-patrones-de-ux)
12. [Referencias](#12-referencias)

---

## 1. ¿Qué es UX/UI?

### Definición Simple

> **UX (User Experience)** = Cómo se SIENTE el usuario al usar tu sistema.
> **UI (User Interface)** = Cómo se VE y se OPERA tu sistema.

UX es la experiencia completa. UI es lo que el usuario toca/ve.


### La Diferencia Clave

```
┌──────────────────────────────────────────────────────────────┐
│                                                                │
│  UI = La cuchara             UX = La experiencia de comer      │
│                                                                │
│  • ¿Es bonita?              • ¿La comida llegó a tiempo?       │
│  • ¿Tiene buen agarre?     • ¿El mesero fue amable?           │
│  • ¿Es del tamaño correcto?• ¿Encontré el restaurante fácil?  │
│  • ¿El material es bueno?  • ¿Repetiría la experiencia?       │
│                                                                │
│  Puedes tener una cuchara HERMOSA (buena UI)                  │
│  pero una experiencia TERRIBLE (mala UX) si:                  │
│  - Esperaste 2 horas por la comida                            │
│  - El menú era incomprensible                                 │
│  - No sabías dónde pagar                                      │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

### ¿Por qué Importa para TODOS?

| Perfil | Sin buena UX | Con buena UX |
|--------|-------------|-------------|
| **Empresario** | Clientes abandonan el producto | Retención alta, recomendaciones |
| **Abogado** | Pierde tiempo buscando expedientes | Flujo natural, encuentra al instante |
| **Economista** | Reportes confusos, errores de lectura | Datos claros, decisiones informadas |
| **Gastrónomo** | Pedidos mal tomados, quejas | Proceso fluido, clientes contentos |
| **Educador** | Alumnos frustrados con la plataforma | Aprendizaje sin fricción |

---

## 2. ISO 9241: La Norma de Usabilidad

### ¿Qué es ISO 9241?

> **ISO 9241 es la norma internacional que define QUÉ significa que un sistema
> sea "usable" — y CÓMO diseñar interacciones centradas en el humano.**

### Partes Relevantes

| Parte | Título | Contenido |
|-------|--------|-----------|
| **ISO 9241-110** | Principios de interacción | Los 7 principios de diseño |
| **ISO 9241-210** | Diseño centrado en el humano | El PROCESO de diseño UX |
| **ISO 9241-171** | Accesibilidad del software | Diseño para personas con discapacidades |
| **ISO 9241-11** | Usabilidad: definiciones | Efectividad, eficiencia, satisfacción |

### Definición de Usabilidad (ISO 9241-11)

```
USABILIDAD = Efectividad + Eficiencia + Satisfacción

• Efectividad: ¿El usuario LOGRA su objetivo?
• Eficiencia:  ¿Lo logra en un tiempo RAZONABLE?
• Satisfacción: ¿Está CONTENTO con la experiencia?
```

---

## 3. Los 7 Principios de Interacción (ISO 9241-110)

### Vista General

```
┌──────────────────────────────────────────────────────────────────┐
│            7 PRINCIPIOS DE INTERACCIÓN — ISO 9241-110             │
├──────────────────────────────────────────────────────────────────┤
│                                                                    │
│  1. Adecuación a la tarea       "Hace lo que necesito"            │
│  2. Auto-descriptividad         "Me explica qué pasa"            │
│  3. Conformidad con expectativas "Se comporta como espero"        │
│  4. Aptitud para el aprendizaje  "Puedo aprender sin manual"      │
│  5. Controlabilidad             "Yo tengo el control"            │
│  6. Tolerancia a errores         "Si me equivoco, no es grave"    │
│  7. Individualización           "Se adapta a mí"                 │
│                                                                    │
└──────────────────────────────────────────────────────────────────┘
```

### Cada Principio con Ejemplo en TaskFlow

| # | Principio | ❌ Viola | ✅ Cumple (TaskFlow) |
|---|-----------|---------|---------------------|
| 1 | **Adecuación a la tarea** | Pedir 10 datos para crear una tarea simple | Solo título obligatorio, el resto opcional |
| 2 | **Auto-descriptividad** | "Error 422" sin explicación | "El título debe tener al menos 3 caracteres" |
| 3 | **Conformidad** | `Ctrl+S` no guarda | `--help` funciona como en todo CLI |
| 4 | **Aprendibilidad** | Sin ejemplos ni tutorial | Modo `--beginner` con explicaciones |
| 5 | **Controlabilidad** | Ejecuta TODO sin preguntar | `--dry-run`, `--skip-phase`, `--only` |
| 6 | **Tolerancia a errores** | Borra sin confirmar | "¿Estás seguro? [s/n]" + undo por 30 días |
| 7 | **Individualización** | Un solo modo para todos | `beginner/standard/expert` configurable |

---

## 4. Diseño Centrado en el Humano (ISO 9241-210)

### El Proceso Iterativo

```
         ┌────────────────────────────────────────────┐
         │                                              │
         │      DISEÑO CENTRADO EN EL HUMANO            │
         │          (ISO 9241-210)                      │
         │                                              │
         │  ┌──────────┐                               │
         │  │ ENTENDER │ ← ¿Quién es el usuario?       │
         │  │ contexto │   ¿Qué necesita?              │
         │  └─────┬────┘   ¿En qué contexto?           │
         │        │                                     │
         │        ▼                                     │
         │  ┌──────────┐                               │
         │  │ESPECIFICAR│ ← Requisitos de usabilidad   │
         │  │ requisitos│   (escenarios BDD de UX)     │
         │  └─────┬────┘                               │
         │        │                                     │
         │        ▼                                     │
         │  ┌──────────┐                               │
         │  │ DISEÑAR  │ ← Prototipos, wireframes      │
         │  │soluciones│   (mocks de la CLI)           │
         │  └─────┬────┘                               │
         │        │                                     │
         │        ▼                                     │
         │  ┌──────────┐                               │
         │  │ EVALUAR  │ ← ¿Cumple las métricas?       │
         │  │          │   (ISO 25022: satisfacción)   │
         │  └─────┬────┘                               │
         │        │                                     │
         │        └────── ¿Cumple? ──→ SÍ: Lanzar      │
         │                    │                         │
         │                    NO: Iterar ──────────┘    │
         │                                              │
         └────────────────────────────────────────────┘
```

### Conexión con BDD

```gherkin
# BDD ES diseño centrado en el humano:
# El escenario describe la experiencia DESEADA del usuario

Feature: Creación de Tareas (UX)
  Como profesional con poco tiempo
  Quiero crear tareas con mínimo esfuerzo
  Para no perder mi flujo de trabajo

  Scenario: Creación rápida con solo título
    Given estoy en la línea de comandos
    When escribo "guide task add 'Comprar insumos'"
    Then la tarea se crea en menos de 1 segundo
    And veo confirmación "✅ Tarea creada: Comprar insumos"
    And NO me pidió más datos innecesarios

  Scenario: Mensaje de error claro y accionable
    When intento crear una tarea sin título
    Then veo un mensaje en ROJO con el problema específico
    And me sugiere cómo corregirlo
    And NO veo un stack trace técnico
```

---

## 5. UX en CLI (Interfaz de Texto)

### ¿CLI puede tener buena UX?

**¡SÍ!** La UX no es exclusiva de interfaces gráficas.
Un CLI bien diseñado es MÁS eficiente que una GUI para usuarios técnicos.

### Principios de UX para CLI

| Principio | Implementación en TaskFlow |
|-----------|---------------------------|
| **Progressive disclosure** | Solo muestra lo esencial; detalles con `--verbose` |
| **Feedback inmediato** | Spinners, barras de progreso, confirmaciones |
| **Consistencia** | Mismo patrón siempre: `guide <verbo> <sustantivo> [opciones]` |
| **Recuperabilidad** | `--dry-run` antes de ejecutar, undo disponible |
| **Personalización** | `config.yaml` para defaults, perfiles de usuario |

### Diseño de la CLI de TaskFlow

```
$ guide --help

╭─────────────────────────────────────────────────────────────╮
│  🚀 AI-Dev-Guide v1.0 — Pipeline de Desarrollo Profesional  │
╰─────────────────────────────────────────────────────────────╯

Uso: guide <comando> [opciones]

Comandos:
  run          Ejecutar el pipeline completo
  check        Verificar un aspecto específico (solid, owasp, bdd...)
  report       Generar reporte de calidad (ISO 25010)
  task         Gestionar tareas del proyecto ejemplo

Opciones globales:
  --help, -h          Mostrar esta ayuda
  --verbose, -v       Salida detallada
  --quiet, -q         Solo errores
  --explain           Incluir notas educativas
  --mode [beginner|standard|expert]
  --output [rich|json|markdown|plain]
  --dry-run           Simular sin ejecutar

Ejemplos:
  guide run --project ./taskflow --explain
  guide check owasp --project ./mi-api
  guide report --output markdown > report.md
```

### Anatomía de un Buen Output CLI

```
$ guide check solid --project ./taskflow

 Análisis SOLID                                          [2/5 fases]
 ├── Escaneando archivos... 12 clases encontradas         ✅
 ├── Verificando SRP... 1 violación                       ⚠️
 │   └── AuthService.login: 45 líneas → Extraer validación
 ├── Verificando OCP... 1 violación                       ⚠️
 │   └── AuthService._validate_password: 5 condicionales
 ├── Verificando LSP... sin violaciones                   ✅
 ├── Verificando ISP... sin violaciones                   ✅
 └── Verificando DIP... sin violaciones                   ✅

 Score: 91.7/100 | 4 violaciones | 12 clases analizadas

 💡 Sugerencia: Extrae la validación de password a una clase
    PasswordValidator para mejorar SRP y OCP.

 📖 Más info: docs/guides/SOLID-paso-a-paso.md
```

### Lo que hace BUENA esta interfaz:

| Elemento | Principio ISO 9241 | Por qué funciona |
|----------|-------------------|-----------------|
| Árbol visual `├──` | Auto-descriptividad | Ves la estructura y el progreso |
| Íconos ✅ ⚠️ | Tolerancia a errores | Identificas el problema sin leer todo |
| Score numérico | Conformidad | Esperabas un resultado cuantificable |
| Sugerencia específica | Adecuación a la tarea | No solo dice qué está mal, dice qué HACER |
| Link a documentación | Aprendibilidad | Puedes profundizar si quieres |

---


## 6. Accesibilidad (ISO 9241-171)

### ¿Qué es?

> **Accesibilidad = que TODAS las personas puedan usar tu sistema,
> incluyendo quienes tienen discapacidades visuales, motoras o cognitivas.**

### Implementación en TaskFlow CLI

| Requisito | Solución | Implementación |
|-----------|----------|---------------|
| Sin dependencia de color | Símbolos + texto | ✅ ⚠️ ❌ además de colores |
| Screen readers | Modo texto puro | `--plain` sin formato ANSI |
| Baja visión | Verbosidad configurable | `--verbose` con más contexto |
| Discapacidad cognitiva | Lenguaje simple | Modo `--beginner` sin jerga |
| Movilidad reducida | Mínimos keystrokes | Aliases: `guide r` = `guide run` |

### Checklist de Accesibilidad CLI

```python
ACCESSIBILITY_CHECKLIST = {
    "no_color_dependency": {
        "description": "Información transmitida sin depender solo del color",
        "implementation": "Símbolos: ✅=pass, ⚠️=warning, ❌=fail, 🔄=in_progress",
        "test": "Ejecutar con --no-color y verificar que se entiende todo",
    },
    "screen_reader_compatible": {
        "description": "Output legible por lectores de pantalla",
        "implementation": "Flag --plain que elimina ANSI escapes y arte ASCII",
        "test": "Pipe output a 'cat' y verificar legibilidad",
    },
    "configurable_verbosity": {
        "description": "Nivel de detalle ajustable",
        "implementation": "--quiet (errores) / default / --verbose (todo)",
        "test": "Cada nivel muestra información coherente",
    },
    "clear_error_messages": {
        "description": "Errores en lenguaje simple con acción sugerida",
        "implementation": "Nunca stack traces al usuario; siempre mensaje + sugerencia",
        "test": "Provocar errores y verificar mensajes",
    },
}
```

---

## 7. Heurísticas de Nielsen

### Los 10 Principios de Jakob Nielsen

Complementan ISO 9241 con reglas prácticas:

| # | Heurística | En TaskFlow CLI |
|---|-----------|-----------------|
| 1 | **Visibilidad del estado** | Barras de progreso, spinners, fase actual |
| 2 | **Coincidencia sistema-mundo real** | Verbos naturales: `add`, `list`, `search` |
| 3 | **Control del usuario** | `Ctrl+C` siempre funciona, `--dry-run` |
| 4 | **Consistencia** | Misma estructura: `guide <verb> <noun> [--opts]` |
| 5 | **Prevención de errores** | Validación antes de ejecutar, confirmaciones |
| 6 | **Reconocer vs recordar** | `--help` siempre disponible, autocompletado |
| 7 | **Flexibilidad** | Aliases cortos + comandos largos |
| 8 | **Diseño minimalista** | Solo info relevante; detalles con `--verbose` |
| 9 | **Recuperación de errores** | Mensajes claros + cómo corregir + undo |
| 10 | **Documentación** | `--help`, `--explain`, links a guías |

---

## 8. Métricas de Usabilidad (ISO 25022)

### Cómo Medir UX Objetivamente

| Métrica | Fórmula | Meta | Método |
|---------|---------|------|--------|
| **Efectividad** | Tareas exitosas / intentadas × 100 | ≥ 90% | Observación |
| **Eficiencia** | Tiempo real / tiempo óptimo | ≤ 1.5x | Cronómetro |
| **Satisfacción** | Promedio encuesta (1-5) | ≥ 4.0 | Cuestionario |
| **Aprendibilidad** | Sesiones hasta autonomía | ≤ 3 | Seguimiento |
| **Error rate** | Errores del usuario / operaciones | ≤ 10% | Log analysis |

### Encuesta de Satisfacción (SUS - System Usability Scale)

```
Responde del 1 (totalmente en desacuerdo) al 5 (totalmente de acuerdo):

1. Creo que usaría este sistema frecuentemente
2. Encontré el sistema innecesariamente complejo
3. Pensé que el sistema era fácil de usar
4. Creo que necesitaría soporte técnico para usarlo
5. Las funciones del sistema están bien integradas
6. Pensé que había mucha inconsistencia en el sistema
7. La mayoría de personas aprenderían rápidamente
8. Encontré el sistema muy incómodo de usar
9. Me sentí seguro/a usando el sistema
10. Necesité aprender muchas cosas antes de poder usarlo

Score SUS = ((suma_impares - 5) + (25 - suma_pares)) × 2.5
Rango: 0-100 | Promedio industria: 68 | Meta TaskFlow: ≥ 75
```

---

## 9. UX y la IA Asistida

### El Paradigma del Vibe Coding

En la era de la IA asistida, la UX cambia radicalmente:

| UX Tradicional | UX con IA (Vibe Coding) |
|---------------|------------------------|
| El usuario navega menús | El usuario DESCRIBE lo que quiere |
| La interfaz muestra opciones | La IA SUGIERE lo que puede hacer |
| El usuario aprende la herramienta | La herramienta aprende al USUARIO |
| Error: "re-lee el manual" | Error: la IA EXPLICA y sugiere |

### Principios de UX para IA Asistida

| Principio | Aplicación | En AI-Dev-Guide |
|-----------|-----------|-----------------|
| **Transparencia** | La IA explica QUÉ hizo y POR QUÉ | Notas educativas en cada output |
| **Control** | El usuario puede overridear la IA | `--skip-phase`, `--only`, `--dry-run` |
| **Progresividad** | De simple a complejo según el usuario | Modos beginner/standard/expert |
| **Verificabilidad** | El usuario puede validar el output | Tests, scores, métricas visibles |
| **Reversibilidad** | Se puede deshacer lo que la IA hizo | `--dry-run`, soft delete, undo |

---

## 10. Ejercicios Prácticos

### Ejercicio 1: Evaluación Heurística (20 min) 🔍

**Nivel**: Principiante

Evalúa una app que uses diariamente con las 10 heurísticas de Nielsen:

| Heurística | Score (1-5) | Ejemplo de problema |
|-----------|------------|-------------------|
| 1. Visibilidad | ___ | |
| 2. Mundo real | ___ | |
| 3. Control | ___ | |
| 4. Consistencia | ___ | |
| 5. Prevención errores | ___ | |
| 6. Reconocer vs recordar | ___ | |
| 7. Flexibilidad | ___ | |
| 8. Minimalismo | ___ | |
| 9. Recuperación errores | ___ | |
| 10. Documentación | ___ | |

### Ejercicio 2: Diseña un CLI Usable (25 min) 📝

**Nivel**: Intermedio

Diseña la interfaz CLI para un sistema de TU profesión:

1. Define 5 comandos principales
2. Muestra cómo sería el `--help`
3. Diseña el output de un comando exitoso
4. Diseña el mensaje de error (claro + accionable)
5. Verifica contra los 7 principios ISO 9241-110

### Ejercicio 3: Test de Usabilidad (30 min) 👥

**Nivel**: Intermedio-Avanzado

Con un compañero:
1. Uno es el "usuario" (no ha visto el sistema antes)
2. El otro OBSERVA (no ayuda)
3. Pide al usuario completar 3 tareas en TaskFlow CLI
4. Registra: tiempo, errores, comentarios
5. Calcula métricas ISO 25022

### Ejercicio 4: Escenarios BDD de UX (20 min) 📋

**Nivel**: Todos

Escribe escenarios Gherkin que verifiquen buena UX:

```gherkin
Feature: Experiencia de Usuario
  Scenario: Mensaje de error es comprensible sin conocimientos técnicos
    Given un usuario principiante
    When comete un error de validación
    Then el mensaje explica EL PROBLEMA en lenguaje simple
    And sugiere CÓMO corregirlo
    And NO muestra código ni stack traces
```

Escribe 3 escenarios más para: onboarding, recuperación de errores, personalización.

---

## 11. Anti-patrones de UX

### Los 7 Pecados Capitales de la UX

| Anti-patrón | Principio que viola | Ejemplo | Solución |
|-------------|-------------------|---------|----------|
| **Wall of text** | Minimalismo | 50 líneas de output sin estructura | Progressive disclosure |
| **Error críptico** | Auto-descriptividad | "Error: NoneType has no attribute 'id'" | "No se encontró la tarea. ¿Verificaste el ID?" |
| **Sin feedback** | Visibilidad | Comando ejecuta 30s sin mostrar nada | Spinner + barra de progreso |
| **Destructivo sin confirmar** | Tolerancia | `delete` sin preguntar "¿estás seguro?" | Confirmación + soft delete |
| **Jerga técnica** | Aprendibilidad | "Validating JWT RS256 HMAC signature" | "Verificando tu sesión..." |
| **Un solo modo** | Individualización | Misma complejidad para novato y experto | Modos beginner/expert |
| **Sin undo** | Control | Acción irreversible sin advertencia | Undo + papelera de reciclaje |

---

## 12. Referencias

### Estándares ISO

| Estándar | Uso |
|----------|-----|
| ISO 9241-110:2020 | Los 7 principios de interacción |
| ISO 9241-210:2019 | Proceso de diseño centrado en el humano |
| ISO 9241-171:2008 | Accesibilidad del software |
| ISO 9241-11:2018 | Definición de usabilidad |

### Libros Recomendados

| Libro | Autor | Lo que Aporta |
|-------|-------|---------------|
| *Don't Make Me Think* | Steve Krug | UX para web, principios aplicables a CLI |
| *The Design of Everyday Things* | Don Norman | Affordances y modelo mental |
| *About Face* | Alan Cooper | Diseño de interacción profundo |
| *CLI Style Guide* | Heroku/12factor | Convenciones de CLI moderno |

### Conexión con el Taller Completo

| Módulo | Conexión con UX |
|--------|----------------|
| **BDD** | Los escenarios DESCRIBEN la experiencia deseada |
| **TDD** | Tests verifican que los mensajes son claros |
| **SOLID** | SRP en UI: cada componente tiene una función |
| **OWASP** | Mensajes genéricos de seguridad (no revelar info) |
| **ISO 25010** | Usabilidad es una de las 8 características |
| **Stress** | Timeout UX: respuesta <3s para mantener atención |
| **APIs** | Circuit breaker muestra "servicio no disponible" amigable |

---

## Control de Cambios

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0.0 | 2026-08-03 | Versión inicial completa |

---

> **UX no es un "nice to have" — es lo que determina si alguien USA tu software o lo abandona.**
>
> ISO 9241 te da el MARCO teórico.
> Las heurísticas de Nielsen te dan REGLAS prácticas.
> ISO 25022 te da MÉTRICAS para medir.
> Y BDD te da la HERRAMIENTA para especificar la experiencia esperada.
>
> Flujo completo del taller:
> BDD → TDD → SOLID → OWASP → ISO 25010 → Stress → APIs → **UX/UI** ✅
