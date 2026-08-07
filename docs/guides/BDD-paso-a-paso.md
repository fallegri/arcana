# Guía BDD Paso a Paso
## Behavior-Driven Development — Desarrollo Guiado por Comportamiento

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0.0 |
| **Fecha** | 2026-08-03 |
| **Público** | Profesionales multidisciplinarios (universitario+) |
| **Prerrequisitos** | Conocimiento básico de prompts con IA, ninguno de programación |
| **Duración estimada** | 4-6 horas (taller completo) |
| **Proyecto ejemplo** | TaskFlow — Sistema de gestión de tareas |

---

## Tabla de Contenidos

1. [¿Qué es BDD?](#1-qué-es-bdd)
2. [¿Por qué BDD importa?](#2-por-qué-bdd-importa)
3. [Los Three Amigos](#3-los-three-amigos)
4. [El Lenguaje Gherkin](#4-el-lenguaje-gherkin)
5. [Escribiendo tu Primer Escenario](#5-escribiendo-tu-primer-escenario)
6. [Escenarios Completos: TaskFlow](#6-escenarios-completos-taskflow)
7. [De Gherkin a Código: Step Definitions](#7-de-gherkin-a-código-step-definitions)
8. [Conexión BDD → TDD → Implementación](#8-conexión-bdd--tdd--implementación)
9. [Living Documentation](#9-living-documentation)
10. [Ejercicios Prácticos](#10-ejercicios-prácticos)
11. [Errores Comunes y Cómo Evitarlos](#11-errores-comunes-y-cómo-evitarlos)
12. [Referencias](#12-referencias)

---

## 1. ¿Qué es BDD?

### Definición Simple

> **BDD es una forma de describir QUÉ debe hacer el software usando lenguaje humano,
> ANTES de escribir una sola línea de código.**

Imagina que estás en una reunión con:
- Un abogado que necesita un sistema de contratos
- Un programador que lo va a construir
- Un tester que va a verificarlo

BDD es el **idioma común** que los tres pueden usar para ponerse de acuerdo
sobre qué debe hacer el sistema.

### Definición Técnica

BDD (Behavior-Driven Development) es una metodología de desarrollo de software que:

1. **Especifica comportamiento** en lugar de requisitos técnicos
2. **Usa lenguaje natural estructurado** (Gherkin) comprensible por todos
3. **Automatiza la verificación** de que el software cumple lo especificado
4. **Genera documentación viva** que siempre está actualizada

### La Metáfora del Restaurante 🍽️

Piensa en BDD como el proceso de un restaurante:

```
┌──────────────────────────────────────────────────────────┐
│                                                            │
│  MENÚ (Feature file)                                       │
│  "Plato: Pasta Carbonara"                                  │
│  "Como comensal hambriento"                                │
│  "Quiero una pasta cremosa"                                │
│  "Para satisfacer mi apetito"                              │
│                                                            │
│  RECETA (Step Definitions)                                 │
│  Given: Tengo los ingredientes (pasta, huevo, panceta)     │
│  When: Cocino siguiendo la técnica                         │
│  Then: Obtengo una carbonara auténtica                     │
│                                                            │
│  DEGUSTACIÓN (Tests ejecutados)                            │
│  ✅ ¿Tiene pasta al dente? SÍ                             │
│  ✅ ¿La salsa es cremosa? SÍ                              │
│  ✅ ¿Tiene panceta crujiente? SÍ                          │
│  → PLATO APROBADO                                          │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

### BDD vs TDD vs Testing Tradicional

| Aspecto | Testing Tradicional | TDD | BDD |
|---------|-------------------|-----|-----|
| **¿Quién escribe?** | Testers | Desarrolladores | Todos (Three Amigos) |
| **¿Cuándo?** | Después del código | Antes del código | Antes del diseño |
| **¿En qué idioma?** | Técnico | Código | Lenguaje natural |
| **¿Qué describe?** | Cómo falla | Cómo funciona | Qué comportamiento se espera |
| **¿Quién lo entiende?** | Técnicos | Programadores | TODOS |
| **Ejemplo** | `assert x == 5` | `test_sum_returns_5()` | `Then el total es 5` |

---

## 2. ¿Por qué BDD importa?

### Para el Empresario/Product Owner
- ✅ Verificas que se construye LO QUE PEDISTE (no lo que el programador interpretó)
- ✅ Los escenarios son tu contrato con el equipo técnico
- ✅ Puedes leer y validar los tests sin saber programar

### Para el Profesional Legal
- ✅ Los escenarios documentan reglas de negocio de forma auditable
- ✅ Cada comportamiento tiene trazabilidad (requisito → test → código)
- ✅ Es evidencia de que se siguió un proceso formal de validación

### Para el Desarrollador
- ✅ Sabes EXACTAMENTE qué construir antes de escribir código
- ✅ Los escenarios son tu definición de "terminado" (Definition of Done)
- ✅ Tests de aceptación automatizados desde el día 1

### Para el Economista/Analista
- ✅ Reduces retrabajo (el 60% de bugs vienen de requisitos mal entendidos)
- ✅ Time-to-market más predecible
- ✅ ROI medible: menos defectos = menos costo de corrección

### El Costo de No Usar BDD

```
Costo de corregir un bug:
┌────────────────────────────────────────────────────────────┐
│                                                              │
│  Fase de Requisitos:    $1     ← BDD detecta aquí           │
│  Fase de Diseño:        $5                                   │
│  Fase de Código:        $10    ← TDD detecta aquí           │
│  Fase de Testing:       $50    ← Testing tradicional         │
│  En Producción:         $500   ← Sin BDD ni TDD             │
│                                                              │
│  BDD + TDD = detectar el 90% de problemas cuando            │
│  corregirlos cuesta $1-$10, no $500                          │
│                                                              │
└────────────────────────────────────────────────────────────┘
```

---

## 3. Los Three Amigos

### ¿Qué es la Sesión de Three Amigos?

Es una reunión corta (30-60 min) donde **tres perspectivas** definen el comportamiento:

```
         ┌──────────────┐
         │   NEGOCIO    │
         │ (Product      │
         │  Owner)       │
         └──────┬───────┘
                │
                │  "¿QUÉ necesitamos?"
                │
    ┌───────────┼───────────┐
    │                       │
    ▼                       ▼
┌──────────┐         ┌──────────┐
│DESARROLLO│         │ TESTING  │
│(Dev)     │         │ (QA)     │
└──────────┘         └──────────┘
"¿CÓMO lo             "¿QUÉ podría
 construimos?"         salir mal?"
```

### Roles en el Contexto de IA Asistida

| Rol Tradicional | En tu contexto (vibe coding) | Pregunta clave |
|----------------|------------------------------|----------------|
| **Product Owner** | TÚ (el que tiene la idea) | "¿Qué quiero que haga?" |
| **Desarrollador** | IA (Kiro, Copilot, etc.) | "¿Cómo lo implemento?" |
| **Tester** | TÚ + IA (validación cruzada) | "¿Qué pasa si algo sale mal?" |

### Ejemplo de Sesión Three Amigos para TaskFlow

```
👤 Negocio: "Necesito que los usuarios puedan crear tareas"

🧑‍💻 Dev: "¿Qué datos tiene una tarea? ¿Título, descripción, fecha límite?"

👤 Negocio: "Título obligatorio, descripción opcional, fecha límite opcional"

🧪 QA: "¿Qué pasa si el título está vacío? ¿Y si tiene 1000 caracteres?"

👤 Negocio: "Título mínimo 3 caracteres, máximo 200"

🧪 QA: "¿Puede un usuario ver las tareas de otro?"

👤 Negocio: "No, cada usuario solo ve las suyas. Excepto el admin."

🧑‍💻 Dev: "Entonces necesitamos autenticación y permisos por rol"

→ RESULTADO: Escenarios Gherkin claros y completos
```

---

## 4. El Lenguaje Gherkin

### Estructura Básica

Gherkin es un lenguaje con palabras clave que estructuran el comportamiento:

```gherkin
Feature: [Nombre de la funcionalidad]
  Como [rol/persona]
  Quiero [acción/capacidad]
  Para [beneficio/valor]

  Scenario: [Nombre del escenario específico]
    Given [contexto/precondición]
    When [acción que el usuario realiza]
    Then [resultado esperado]
```

### Palabras Clave en Español

| Keyword (inglés) | En español | Propósito | Ejemplo |
|-----------------|------------|-----------|---------|
| `Feature` | Característica | Agrupa escenarios relacionados | `Feature: Gestión de Tareas` |
| `Scenario` | Escenario | Un caso de uso específico | `Scenario: Crear tarea exitosamente` |
| `Given` | Dado/Dado que | Establece el contexto inicial | `Given un usuario autenticado` |
| `When` | Cuando | La acción que se realiza | `When crea una tarea nueva` |
| `Then` | Entonces | El resultado esperado | `Then la tarea aparece en su lista` |
| `And` | Y | Agrega condiciones | `And recibe confirmación` |
| `But` | Pero | Condición negativa | `But no puede ver tareas de otros` |
| `Background` | Antecedentes | Contexto común a todos los escenarios | `Background: usuario logueado` |
| `Scenario Outline` | Esquema | Escenario con múltiples datos | Para probar con varios inputs |
| `Examples` | Ejemplos | Tabla de datos para Outline | Datos tabulares |

### Anatomía de un Buen Escenario

```gherkin
# ✅ BUENO — Claro, conciso, orientado al comportamiento
Scenario: Usuario crea tarea con datos válidos
  Given María está autenticada en el sistema
  When María crea una tarea con título "Preparar presentación"
  Then la tarea se registra exitosamente
  And María ve la tarea en su lista de pendientes

# ❌ MALO — Demasiado técnico, habla de implementación
Scenario: POST /api/tasks con JSON válido retorna 201
  Given un token JWT válido en el header Authorization
  When se envía POST a /api/tasks con body {"title": "test"}
  Then el status code es 201
  And el response tiene campo "id" tipo integer
```

### Regla de Oro

> **Escribe escenarios como si se los explicaras a alguien que NO sabe programar,
> pero SÍ entiende el problema de negocio.**

---

## 5. Escribiendo tu Primer Escenario

### Paso 1: Identifica la Funcionalidad

Pregúntate: "¿Qué necesita poder hacer el usuario?"

```
Respuesta: "Crear una tarea nueva para organizar su trabajo"
```

### Paso 2: Define el Valor (User Story)

```gherkin
Feature: Creación de Tareas
  Como profesional con múltiples responsabilidades
  Quiero crear tareas con título y descripción
  Para organizar y no olvidar mi trabajo pendiente
```

### Paso 3: Piensa en el "Camino Feliz" (Happy Path)

```gherkin
  Scenario: Crear tarea con todos los datos
    Given estoy autenticado como "María García"
    When creo una tarea con:
      | campo       | valor                              |
      | título      | Revisar contrato de servicios      |
      | descripción | Verificar cláusulas de renovación  |
      | prioridad   | alta                               |
    Then la tarea se crea exitosamente
    And aparece en mi lista de tareas pendientes
    And tiene estado "pendiente"
```

### Paso 4: Piensa en lo que Puede Salir Mal (Edge Cases)

```gherkin
  Scenario: No puedo crear tarea sin título
    Given estoy autenticado como "María García"
    When intento crear una tarea sin título
    Then recibo un mensaje de error claro
    And el mensaje dice "El título es obligatorio"
    And no se crea ninguna tarea

  Scenario: El título tiene un límite de caracteres
    Given estoy autenticado como "María García"
    When intento crear una tarea con un título de 250 caracteres
    Then recibo un mensaje de error
    And el mensaje dice "El título no puede exceder 200 caracteres"
```

### Paso 5: Piensa en Permisos y Seguridad

```gherkin
  Scenario: No puedo crear tareas sin estar autenticado
    Given no estoy autenticado
    When intento crear una tarea
    Then recibo un error de acceso denegado
    And el sistema me sugiere iniciar sesión
```

### Resumen Visual del Proceso

```
┌────────────┐     ┌────────────┐     ┌────────────┐     ┌────────────┐
│   PASO 1   │────▶│   PASO 2   │────▶│   PASO 3   │────▶│   PASO 4   │
│ ¿Qué hace? │     │ ¿Para qué? │     │ ¿Cuándo    │     │ ¿Qué puede │
│(Feature)   │     │(User Story)│     │  funciona? │     │  fallar?   │
│            │     │            │     │(Happy Path)│     │(Edge Cases)│
└────────────┘     └────────────┘     └────────────┘     └────────────┘
                                                                │
                                                                ▼
                                                         ┌────────────┐
                                                         │   PASO 5   │
                                                         │ ¿Es seguro?│
                                                         │(Seguridad) │
                                                         └────────────┘
```

---


## 6. Escenarios Completos: TaskFlow

A continuación presentamos los escenarios BDD completos del proyecto TaskFlow,
organizados por feature. Estos mismos archivos están en `agents/bdd/features/`.

### 6.1 Feature: Autenticación

```gherkin
# features/auth/registro.feature

Feature: Registro de Usuarios
  Como persona interesada en usar TaskFlow
  Quiero poder crear una cuenta
  Para gestionar mis tareas de forma segura

  Scenario: Registro exitoso con datos válidos
    Given soy un visitante nuevo del sistema
    When me registro con:
      | campo    | valor                |
      | nombre   | María García         |
      | email    | maria@ejemplo.com    |
      | password | MiClave$egura2026    |
    Then mi cuenta se crea exitosamente
    And recibo un mensaje de bienvenida
    And puedo iniciar sesión inmediatamente

  Scenario: No puedo registrarme con email ya existente
    Given ya existe un usuario con email "maria@ejemplo.com"
    When intento registrarme con email "maria@ejemplo.com"
    Then recibo un error indicando "Este email ya está registrado"
    And no se crea una cuenta duplicada

  Scenario: La contraseña debe cumplir requisitos de seguridad
    Given soy un visitante nuevo del sistema
    When intento registrarme con contraseña "123"
    Then recibo un error de validación
    And el mensaje indica los requisitos:
      | requisito                          |
      | Mínimo 8 caracteres               |
      | Al menos una mayúscula            |
      | Al menos un número                |
      | Al menos un carácter especial     |

  Scenario Outline: Validación de formato de email
    Given soy un visitante nuevo del sistema
    When intento registrarme con email "<email>"
    Then recibo un error indicando "Formato de email inválido"

    Examples:
      | email              |
      | sin-arroba.com     |
      | @sin-usuario.com   |
      | espacios @mail.com |
      |                    |
```

```gherkin
# features/auth/login.feature

Feature: Inicio de Sesión
  Como usuario registrado
  Quiero iniciar sesión de forma segura
  Para acceder a mis tareas

  Background:
    Given existe un usuario registrado:
      | nombre | email             | password          |
      | María  | maria@ejemplo.com | MiClave$egura2026 |

  Scenario: Login exitoso con credenciales correctas
    When inicio sesión con email "maria@ejemplo.com" y password "MiClave$egura2026"
    Then accedo al sistema exitosamente
    And recibo un token de sesión válido
    And veo mi nombre "María" en la interfaz

  Scenario: Login fallido con contraseña incorrecta
    When inicio sesión con email "maria@ejemplo.com" y password "ClaveIncorrecta"
    Then recibo un error de credenciales inválidas
    And el mensaje NO revela si el email existe o no
    And se registra el intento fallido

  Scenario: Bloqueo de cuenta tras múltiples intentos fallidos
    When inicio sesión con password incorrecta 5 veces consecutivas
    Then mi cuenta se bloquea temporalmente por 15 minutos
    And recibo un mensaje indicando el bloqueo
    And se envía una alerta de seguridad a mi email

  Scenario: Login exitoso después de esperar el tiempo de bloqueo
    Given mi cuenta está bloqueada por intentos fallidos
    And han pasado 15 minutos desde el bloqueo
    When inicio sesión con credenciales correctas
    Then accedo al sistema exitosamente
    And el contador de intentos se reinicia
```

### 6.2 Feature: Gestión de Tareas

```gherkin
# features/tasks/crear_tarea.feature

Feature: Creación de Tareas
  Como usuario autenticado de TaskFlow
  Quiero crear tareas con diferentes niveles de detalle
  Para organizar mi trabajo de forma flexible

  Background:
    Given un usuario autenticado "María García"
    And el sistema está operativo

  Scenario: Crear tarea con solo título (mínimo)
    When María crea una tarea con título "Comprar insumos"
    Then la tarea se crea exitosamente
    And tiene estado "pendiente" por defecto
    And tiene prioridad "media" por defecto
    And la fecha de creación es hoy

  Scenario: Crear tarea completa con todos los campos
    When María crea una tarea con:
      | campo            | valor                                |
      | título           | Preparar informe trimestral          |
      | descripción      | Incluir métricas de ventas Q2 2026   |
      | prioridad        | alta                                 |
      | fecha_limite     | 2026-08-15                           |
      | etiquetas        | informe, ventas, Q2                  |
    Then la tarea se crea con todos los datos especificados
    And cada campo refleja exactamente lo que ingresé
    And recibo el ID único de la tarea

  Scenario: Crear múltiples tareas mantiene el orden
    When María crea las siguientes tareas:
      | título                    | prioridad |
      | Revisar contrato          | alta      |
      | Enviar propuesta          | media     |
      | Actualizar presentación   | baja      |
    Then las tres tareas aparecen en su lista
    And están ordenadas por prioridad (alta primero)

  Scenario: Título duplicado es permitido
    Given María ya tiene una tarea "Revisar contrato"
    When María crea otra tarea con título "Revisar contrato"
    Then ambas tareas coexisten en el sistema
    And cada una tiene un ID único diferente
```

```gherkin
# features/tasks/editar_tarea.feature

Feature: Edición de Tareas
  Como usuario que necesita actualizar su trabajo
  Quiero poder modificar tareas existentes
  Para mantener mi organización actualizada

  Background:
    Given un usuario autenticado "María García"
    And María tiene una tarea:
      | id | título             | estado    | prioridad |
      | 1  | Revisar contrato   | pendiente | alta      |

  Scenario: Cambiar el título de una tarea
    When María cambia el título de la tarea 1 a "Revisar contrato v2"
    Then el título se actualiza exitosamente
    And la fecha de modificación se actualiza a hoy
    And el estado NO cambia

  Scenario: Marcar tarea como completada
    When María marca la tarea 1 como "completada"
    Then el estado cambia a "completada"
    And se registra la fecha de completado
    And la tarea se mueve a la sección "Completadas"

  Scenario: No puedo editar una tarea que no es mía
    Given existe una tarea de otro usuario "Carlos"
    When María intenta editar la tarea de Carlos
    Then recibe un error de permisos
    And la tarea de Carlos permanece sin cambios

  Scenario: Editar tarea preserva el historial
    When María cambia la prioridad de la tarea 1 a "baja"
    Then la prioridad se actualiza
    And el historial registra:
      | campo     | valor_anterior | valor_nuevo | fecha      |
      | prioridad | alta           | baja        | 2026-08-03 |
```

```gherkin
# features/tasks/eliminar_tarea.feature

Feature: Eliminación de Tareas
  Como usuario que quiere mantener su lista limpia
  Quiero poder eliminar tareas que ya no necesito
  Para mantener el foco en lo importante

  Background:
    Given un usuario autenticado "María García"
    And María tiene 5 tareas en su lista

  Scenario: Eliminar tarea requiere confirmación
    When María solicita eliminar la tarea "Comprar insumos"
    Then el sistema pide confirmación
    And muestra el título de la tarea a eliminar
    When María confirma la eliminación
    Then la tarea se elimina (soft-delete)
    And ya no aparece en su lista activa
    And María tiene 4 tareas en su lista

  Scenario: Cancelar eliminación no borra nada
    When María solicita eliminar la tarea "Comprar insumos"
    And el sistema pide confirmación
    When María cancela la operación
    Then la tarea permanece intacta
    And María sigue teniendo 5 tareas

  Scenario: Tarea eliminada es recuperable por 30 días
    Given María eliminó la tarea "Comprar insumos" hace 5 días
    When María accede a "Tareas eliminadas"
    Then puede ver "Comprar insumos" en la papelera
    And puede restaurarla a su lista activa

  Scenario: Tarea eliminada se purga después de 30 días
    Given María eliminó la tarea "Comprar insumos" hace 31 días
    When el sistema ejecuta la limpieza automática
    Then la tarea se elimina permanentemente
    And ya no es recuperable
```

### 6.3 Feature: Búsqueda y Filtrado

```gherkin
# features/tasks/busqueda.feature

Feature: Búsqueda y Filtrado de Tareas
  Como usuario con muchas tareas
  Quiero poder buscar y filtrar mi lista
  Para encontrar rápidamente lo que necesito

  Background:
    Given un usuario autenticado "María García"
    And María tiene las siguientes tareas:
      | título                    | estado     | prioridad | etiquetas        |
      | Revisar contrato legal    | pendiente  | alta      | legal, urgente   |
      | Preparar presentación     | en_proceso | media     | ventas           |
      | Comprar insumos oficina   | pendiente  | baja      | oficina          |
      | Informe financiero Q2     | completada | alta      | finanzas, Q2     |
      | Llamar al proveedor       | pendiente  | media     | compras          |

  Scenario: Buscar por texto en título
    When María busca "contrato"
    Then obtiene 1 resultado
    And el resultado es "Revisar contrato legal"

  Scenario: Filtrar por estado
    When María filtra por estado "pendiente"
    Then obtiene 3 resultados
    And todos tienen estado "pendiente"

  Scenario: Filtrar por prioridad
    When María filtra por prioridad "alta"
    Then obtiene 2 resultados:
      | título                  |
      | Revisar contrato legal  |
      | Informe financiero Q2   |

  Scenario: Combinación de filtros
    When María filtra con:
      | filtro    | valor     |
      | estado    | pendiente |
      | prioridad | alta      |
    Then obtiene 1 resultado
    And el resultado es "Revisar contrato legal"

  Scenario: Búsqueda sin resultados muestra mensaje amigable
    When María busca "vacaciones"
    Then obtiene 0 resultados
    And ve el mensaje "No se encontraron tareas con ese criterio"
    And se sugiere "Intenta con otros términos o revisa los filtros"

  Scenario: Filtrar por etiqueta
    When María filtra por etiqueta "legal"
    Then obtiene 1 resultado
    And el resultado es "Revisar contrato legal"
```

### 6.4 Feature: Permisos y Roles

```gherkin
# features/security/permisos.feature

Feature: Control de Acceso por Roles
  Como administrador del sistema
  Quiero que cada usuario solo pueda hacer lo que su rol permite
  Para mantener la seguridad y privacidad de los datos

  Scenario: Usuario normal solo ve sus propias tareas
    Given "María" tiene rol "usuario"
    And "Carlos" tiene rol "usuario"
    And María tiene 3 tareas
    And Carlos tiene 5 tareas
    When María consulta su lista de tareas
    Then ve exactamente 3 tareas
    And ninguna pertenece a Carlos

  Scenario: Administrador puede ver todas las tareas
    Given "Admin" tiene rol "administrador"
    And existen 20 tareas de diversos usuarios
    When Admin consulta todas las tareas
    Then ve las 20 tareas
    And puede filtrar por usuario

  Scenario: Usuario no puede cambiar su propio rol
    Given "María" tiene rol "usuario"
    When María intenta cambiar su rol a "administrador"
    Then recibe un error de permisos
    And su rol permanece como "usuario"
    And se registra el intento como evento de seguridad

  Scenario: Administrador puede desactivar usuarios
    Given "Admin" tiene rol "administrador"
    And "Carlos" tiene una cuenta activa
    When Admin desactiva la cuenta de Carlos
    Then Carlos no puede iniciar sesión
    And las tareas de Carlos se preservan
    And Admin puede reactivar la cuenta posteriormente
```

### 6.5 Feature: Validación de APIs

```gherkin
# features/api/rate_limiting.feature

Feature: Protección contra Saturación de API
  Como sistema que consume APIs externas
  Quiero controlar la tasa de requests
  Para no ser bloqueado ni generar costos excesivos

  Scenario: Rate limiting permite requests dentro del límite
    Given el límite configurado es 60 requests por minuto
    And he realizado 50 requests en el último minuto
    When realizo 1 request más
    Then el request se procesa normalmente
    And recibo la respuesta esperada

  Scenario: Rate limiting bloquea requests que exceden el límite
    Given el límite configurado es 60 requests por minuto
    And he realizado 60 requests en el último minuto
    When intento realizar 1 request más
    Then el request se pone en cola de espera
    And recibo la respuesta después de esperar
    And NO recibo un error

  Scenario: Circuit breaker se activa tras fallos consecutivos
    Given el umbral de fallos es 5
    And la API externa ha fallado 5 veces consecutivas
    When intento hacer un request
    Then el sistema NO contacta la API (circuit OPEN)
    And recibo un mensaje "Servicio temporalmente no disponible"
    And el sistema reintentará automáticamente en 30 segundos

  Scenario: Circuit breaker se recupera cuando la API vuelve
    Given el circuit breaker está en estado "OPEN"
    And han pasado 30 segundos desde la apertura
    When el sistema prueba la API (estado HALF-OPEN)
    And la API responde exitosamente
    Then el circuit breaker vuelve a estado "CLOSED"
    And los requests se procesan normalmente

  Scenario: Presupuesto diario previene gastos excesivos
    Given el presupuesto diario es $10 USD
    And el gasto acumulado hoy es $9.50
    When realizo un request que cuesta $0.60
    Then el request se rechaza
    And recibo una alerta "Presupuesto diario alcanzado"
    And el sistema sugiere "Continúa mañana o aumenta el límite"
```

---


## 7. De Gherkin a Código: Step Definitions

### ¿Qué son los Step Definitions?

Los Step Definitions son el **puente** entre el lenguaje humano (Gherkin)
y el código ejecutable (Python). Son la "traducción" que permite que
los escenarios se conviertan en tests automatizados.

```
┌──────────────┐         ┌──────────────────┐         ┌──────────────┐
│   GHERKIN    │  match   │ STEP DEFINITIONS │  calls  │  APPLICATION │
│ (lenguaje    │────────▶│   (Python)       │────────▶│    CODE      │
│  humano)     │         │                  │         │              │
│              │         │ @given("...")     │         │  FastAPI     │
│ Given...     │         │ def step(ctx):   │         │  endpoints   │
│ When...      │         │     ...          │         │              │
│ Then...      │         │                  │         │              │
└──────────────┘         └──────────────────┘         └──────────────┘
```

### Herramienta: Behave (Python)

Usamos **behave** — el framework BDD más popular para Python.

```bash
# Instalación
pip install behave

# Estructura de archivos
features/
├── auth/
│   ├── registro.feature          # Escenarios en Gherkin
│   └── login.feature
├── tasks/
│   ├── crear_tarea.feature
│   ├── editar_tarea.feature
│   └── busqueda.feature
├── steps/                         # Step Definitions (Python)
│   ├── auth_steps.py
│   ├── task_steps.py
│   └── common_steps.py
└── environment.py                 # Setup/teardown global
```

### Ejemplo Completo: Del Escenario al Código

#### El Escenario (Gherkin):

```gherkin
Scenario: Crear tarea con solo título
  Given un usuario autenticado "María García"
  When María crea una tarea con título "Comprar insumos"
  Then la tarea se crea exitosamente
  And tiene estado "pendiente" por defecto
```

#### Los Step Definitions (Python):

```python
# features/steps/task_steps.py
"""
Step Definitions para la feature de Tareas.

NOTA EDUCATIVA:
- Cada función corresponde a una línea del escenario Gherkin
- El decorador (@given, @when, @then) indica el tipo de paso
- El texto entre comillas debe coincidir EXACTAMENTE con el Gherkin
- Los parámetros entre {llaves} capturan valores dinámicos
"""

from behave import given, when, then
from hamcrest import assert_that, equal_to, is_not, none


@given('un usuario autenticado "{nombre}"')
def step_usuario_autenticado(context, nombre):
    """
    Establece el contexto: un usuario ya logueado.

    ¿Qué hace?
    1. Crea un usuario de prueba (si no existe)
    2. Obtiene un token de autenticación
    3. Guarda el token en el contexto para los siguientes pasos

    PRINCIPIO: Cada step debe ser independiente y auto-contenido.
    """
    # Registrar usuario de prueba
    response = context.client.post("/auth/register", json={
        "nombre": nombre,
        "email": f"{nombre.lower().replace(' ', '.')}@test.com",
        "password": "TestPassword$123"
    })

    # Obtener token
    login_response = context.client.post("/auth/login", json={
        "email": f"{nombre.lower().replace(' ', '.')}@test.com",
        "password": "TestPassword$123"
    })

    # Guardar en contexto compartido
    context.auth_token = login_response.json()["token"]
    context.user_name = nombre
    context.headers = {"Authorization": f"Bearer {context.auth_token}"}


@when('María crea una tarea con título "{titulo}"')
def step_crear_tarea_con_titulo(context, titulo):
    """
    Ejecuta la acción: crear una tarea.

    NOTA EDUCATIVA:
    - Los steps @when representan la ACCIÓN del usuario
    - Guardamos la respuesta para verificarla en @then
    """
    context.response = context.client.post(
        "/tasks",
        json={"titulo": titulo},
        headers=context.headers
    )
    context.created_task = context.response.json()


@then('la tarea se crea exitosamente')
def step_tarea_creada_exitosamente(context):
    """
    Verifica: la creación fue exitosa.

    NOTA EDUCATIVA:
    - Los steps @then VERIFICAN resultados
    - Usamos assert para que el test falle si no se cumple
    - Mensajes de error claros ayudan a diagnosticar fallos
    """
    assert_that(
        context.response.status_code,
        equal_to(201),
        "La tarea debería crearse con status 201 (Created)"
    )
    assert_that(
        context.created_task.get("id"),
        is_not(none()),
        "La tarea creada debe tener un ID asignado"
    )


@then('tiene estado "{estado}" por defecto')
def step_tiene_estado_por_defecto(context, estado):
    """
    Verifica: el estado por defecto es el esperado.

    NOTA EDUCATIVA:
    - Verificamos valores por defecto explícitamente
    - Esto documenta el comportamiento esperado del sistema
    """
    assert_that(
        context.created_task["estado"],
        equal_to(estado),
        f"El estado por defecto debería ser '{estado}'"
    )
```

### Step Definitions para Autenticación:

```python
# features/steps/auth_steps.py
"""
Step Definitions para features de Autenticación.

NOTA EDUCATIVA sobre seguridad (OWASP):
- Nunca guardamos passwords en texto plano en los tests
- Los mensajes de error no revelan si un email existe
- Verificamos el bloqueo de cuenta (rate limiting)
"""

from behave import given, when, then


@given('existe un usuario registrado')
def step_existe_usuario(context):
    """Crea un usuario usando la tabla del Background."""
    for row in context.table:
        context.client.post("/auth/register", json={
            "nombre": row["nombre"],
            "email": row["email"],
            "password": row["password"]
        })
        context.test_user = dict(row)


@when('inicio sesión con email "{email}" y password "{password}"')
def step_login(context, email, password):
    """Intenta iniciar sesión."""
    context.response = context.client.post("/auth/login", json={
        "email": email,
        "password": password
    })


@when('inicio sesión con password incorrecta {veces:d} veces consecutivas')
def step_login_multiple_fallidos(context, veces):
    """
    Simula múltiples intentos fallidos.

    NOTA EDUCATIVA (OWASP A07 - Authentication Failures):
    Este escenario verifica que el sistema implementa
    protección contra ataques de fuerza bruta.
    """
    context.responses = []
    for i in range(veces):
        response = context.client.post("/auth/login", json={
            "email": context.test_user["email"],
            "password": f"PasswordIncorrecta{i}"
        })
        context.responses.append(response)
    context.response = context.responses[-1]


@then('mi cuenta se bloquea temporalmente por {minutos:d} minutos')
def step_cuenta_bloqueada(context, minutos):
    """Verifica que la cuenta está bloqueada."""
    # Intentar login con credenciales correctas
    response = context.client.post("/auth/login", json={
        "email": context.test_user["email"],
        "password": context.test_user["password"]
    })
    assert response.status_code == 429  # Too Many Requests
    assert "bloqueada" in response.json()["message"].lower()


@then('el mensaje NO revela si el email existe o no')
def step_mensaje_generico(context):
    """
    NOTA EDUCATIVA (OWASP):
    El mensaje de error debe ser GENÉRICO para no facilitar
    la enumeración de usuarios. Nunca decir "email no encontrado"
    ni "contraseña incorrecta" por separado.
    """
    message = context.response.json()["message"]
    assert "credenciales inválidas" in message.lower()
    assert "email no encontrado" not in message.lower()
    assert "password incorrecta" not in message.lower()
```

### El archivo environment.py (Setup Global):

```python
# features/environment.py
"""
Configuración global de Behave.

Este archivo se ejecuta antes/después de cada feature, scenario, etc.
Aquí preparamos el entorno de testing.

NOTA EDUCATIVA:
- before_all: Se ejecuta UNA vez al inicio de todos los tests
- before_scenario: Se ejecuta antes de CADA escenario
- after_scenario: Limpia después de cada escenario
- Esto asegura que cada test es INDEPENDIENTE (no depende de otros)
"""

from fastapi.testclient import TestClient

from examples.taskflow.api.main import create_app
from examples.taskflow.api.database import reset_test_database


def before_all(context):
    """Inicializa la aplicación de test."""
    context.app = create_app(testing=True)
    context.client = TestClient(context.app)


def before_scenario(context, scenario):
    """Prepara un estado limpio para cada escenario."""
    reset_test_database()
    context.auth_token = None
    context.headers = {}
    context.response = None


def after_scenario(context, scenario):
    """Limpieza post-escenario."""
    # Log si el escenario falló (útil para debugging)
    if scenario.status == "failed":
        print(f"\n❌ FALLÓ: {scenario.name}")
        if context.response:
            print(f"   Último response: {context.response.status_code}")
            print(f"   Body: {context.response.text[:200]}")
```

---


## 8. Conexión BDD → TDD → Implementación

### El Flujo Completo: De la Idea al Código Funcionando

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    FLUJO BDD → TDD → IMPLEMENTACIÓN                      │
│                                                                           │
│  ① DESCUBRIMIENTO          ② FORMULACIÓN         ③ AUTOMATIZACIÓN        │
│  (Three Amigos)            (Gherkin)             (Step Definitions)      │
│                                                                           │
│  "¿Qué debe hacer?"  →  "Dado/Cuando/Ent." →  "Python + behave"        │
│                                                                           │
│                                     │                                     │
│                                     ▼                                     │
│                                                                           │
│  ④ TDD: RED                ⑤ TDD: GREEN          ⑥ TDD: REFACTOR        │
│  (Tests unitarios)         (Impl. mínima)        (Mejora + SOLID)       │
│                                                                           │
│  test_create_task()  →  def create_task(): →  Aplicar SRP, DIP          │
│  FALLA ❌               PASA ✅               SIGUE PASANDO ✅           │
│                                                                           │
│                                     │                                     │
│                                     ▼                                     │
│                                                                           │
│  ⑦ VERIFICACIÓN BDD       ⑧ DOCUMENTACIÓN       ⑨ DEPLOYMENT            │
│  (behave ejecuta)          (Living Docs)         (CI/CD)                │
│                                                                           │
│  "Scenario: ✅ PASS" →  Docs actualizados  →  Deploy con confianza      │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### Ejemplo Paso a Paso: "Crear Tarea"

#### PASO ①: Descubrimiento (Conversación)

```
👤 "Necesito que los usuarios puedan crear tareas"
🤖 "¿Qué datos tiene una tarea? ¿Quién puede crearlas?"
👤 "Título obligatorio, descripción opcional. Solo usuarios logueados."
🤖 "¿Qué pasa con títulos vacíos o muy largos?"
👤 "Mínimo 3 caracteres, máximo 200."
```

#### PASO ②: Formulación (Escenario Gherkin)

```gherkin
Scenario: Crear tarea con título válido
  Given un usuario autenticado "María"
  When María crea una tarea con título "Comprar insumos"
  Then la tarea se crea exitosamente
  And tiene estado "pendiente" por defecto
```

#### PASO ③: Automatización (Step Definition — ya mostrado en Sección 7)

#### PASO ④: TDD RED — Test Unitario que Falla

```python
# tests/unit/test_task_service.py
"""
NOTA EDUCATIVA:
Este test se escribe ANTES de implementar create_task().
El objetivo es que FALLE (RED) para confirmar que estamos
testeando algo que aún no existe.
"""
import pytest
from datetime import date

from examples.taskflow.api.services.task_service import TaskService
from examples.taskflow.api.schemas import TaskCreate


class TestCreateTask:
    """Tests unitarios derivados del escenario BDD 'Crear tarea'."""

    def setup_method(self):
        """Setup para cada test — base de datos limpia."""
        self.service = TaskService(db=fake_db_session())

    def test_create_task_with_valid_title(self):
        """
        Derivado de: 'When María crea una tarea con título "Comprar insumos"'
        Verifica: La tarea se crea y tiene los campos esperados.
        """
        task_data = TaskCreate(titulo="Comprar insumos")
        result = self.service.create_task(task_data, user_id=1)

        assert result.id is not None
        assert result.titulo == "Comprar insumos"
        assert result.estado == "pendiente"  # Default
        assert result.fecha_creacion == date.today()

    def test_create_task_without_title_raises_error(self):
        """
        Derivado de: 'When intento crear una tarea sin título'
        Verifica: Se rechaza con ValidationError.
        """
        with pytest.raises(ValueError, match="título es obligatorio"):
            task_data = TaskCreate(titulo="")
            self.service.create_task(task_data, user_id=1)

    def test_create_task_requires_authentication(self):
        """
        Derivado de: 'Given un usuario autenticado'
        Verifica: Sin user_id, la operación falla.
        """
        task_data = TaskCreate(titulo="Test")
        with pytest.raises(PermissionError):
            self.service.create_task(task_data, user_id=None)

    def test_create_task_title_max_length(self):
        """
        Derivado de: conversación Three Amigos (máx 200 chars)
        Verifica: Títulos >200 caracteres se rechazan.
        """
        long_title = "A" * 201
        with pytest.raises(ValueError, match="no puede exceder 200"):
            task_data = TaskCreate(titulo=long_title)
            self.service.create_task(task_data, user_id=1)
```

**Ejecutamos → TODO FALLA ❌** (porque `TaskService` no existe aún)

```bash
$ pytest tests/unit/test_task_service.py -v
FAILED test_create_task_with_valid_title - ModuleNotFoundError: No module 'task_service'
FAILED test_create_task_without_title_raises_error - ModuleNotFoundError
FAILED test_create_task_requires_authentication - ModuleNotFoundError
FAILED test_create_task_title_max_length - ModuleNotFoundError
```

#### PASO ⑤: TDD GREEN — Implementación Mínima

```python
# examples/taskflow/api/services/task_service.py
"""
TaskService — Servicio de gestión de tareas.

NOTA EDUCATIVA:
Esta es la implementación MÍNIMA que hace pasar los tests.
En el paso REFACTOR la mejoraremos aplicando SOLID.

Principios demostrados:
- SRP: Este servicio SOLO gestiona tareas (no auth, no notificaciones)
- DIP: Recibe db como dependencia inyectada (no crea su propia conexión)
"""

from datetime import date
from typing import Optional

from examples.taskflow.api.schemas import TaskCreate, TaskResponse
from examples.taskflow.api.models import TaskModel


class TaskService:
    """Servicio para operaciones CRUD de tareas."""

    def __init__(self, db):
        self._db = db

    def create_task(self, task_data: TaskCreate, user_id: Optional[int]) -> TaskResponse:
        """
        Crea una nueva tarea.

        Args:
            task_data: Datos de la tarea (título, descripción, etc.)
            user_id: ID del usuario autenticado

        Returns:
            TaskResponse con la tarea creada

        Raises:
            PermissionError: Si no hay usuario autenticado
            ValueError: Si los datos no son válidos
        """
        # Verificar autenticación
        if user_id is None:
            raise PermissionError("Se requiere autenticación para crear tareas")

        # Validar título
        if not task_data.titulo or len(task_data.titulo.strip()) == 0:
            raise ValueError("El título es obligatorio")

        if len(task_data.titulo) > 200:
            raise ValueError("El título no puede exceder 200 caracteres")

        if len(task_data.titulo) < 3:
            raise ValueError("El título debe tener al menos 3 caracteres")

        # Crear tarea
        task = TaskModel(
            titulo=task_data.titulo,
            descripcion=task_data.descripcion or "",
            estado="pendiente",
            prioridad=task_data.prioridad or "media",
            user_id=user_id,
            fecha_creacion=date.today(),
        )

        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)

        return TaskResponse.model_validate(task)
```

**Ejecutamos → TODO PASA ✅**

```bash
$ pytest tests/unit/test_task_service.py -v
PASSED test_create_task_with_valid_title
PASSED test_create_task_without_title_raises_error
PASSED test_create_task_requires_authentication
PASSED test_create_task_title_max_length

4 passed in 0.12s ✅
```

#### PASO ⑥: TDD REFACTOR — Mejora con SOLID

```python
# REFACTOR: Extraemos validación a su propia clase (SRP)

class TaskValidator:
    """
    Validador de datos de tareas.
    SRP: Solo se encarga de validación, no de persistencia.
    """

    TITLE_MIN_LENGTH = 3
    TITLE_MAX_LENGTH = 200

    @classmethod
    def validate_create(cls, task_data: TaskCreate) -> list[str]:
        """Valida datos de creación. Retorna lista de errores."""
        errors = []

        if not task_data.titulo or len(task_data.titulo.strip()) == 0:
            errors.append("El título es obligatorio")
        elif len(task_data.titulo) < cls.TITLE_MIN_LENGTH:
            errors.append(f"El título debe tener al menos {cls.TITLE_MIN_LENGTH} caracteres")
        elif len(task_data.titulo) > cls.TITLE_MAX_LENGTH:
            errors.append(f"El título no puede exceder {cls.TITLE_MAX_LENGTH} caracteres")

        return errors


class TaskService:
    """Servicio refactorizado — usa TaskValidator (SRP + DIP)."""

    def __init__(self, db, validator: TaskValidator = None):
        self._db = db
        self._validator = validator or TaskValidator()

    def create_task(self, task_data: TaskCreate, user_id: Optional[int]) -> TaskResponse:
        if user_id is None:
            raise PermissionError("Se requiere autenticación para crear tareas")

        errors = self._validator.validate_create(task_data)
        if errors:
            raise ValueError("; ".join(errors))

        task = TaskModel(
            titulo=task_data.titulo.strip(),
            descripcion=task_data.descripcion or "",
            estado="pendiente",
            prioridad=task_data.prioridad or "media",
            user_id=user_id,
            fecha_creacion=date.today(),
        )
        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)
        return TaskResponse.model_validate(task)
```

**Ejecutamos → SIGUE PASANDO ✅** (refactoring no rompe tests)

#### PASO ⑦: Verificación BDD

```bash
$ behave features/tasks/crear_tarea.feature

Feature: Creación de Tareas

  Scenario: Crear tarea con solo título (mínimo)        ✅ PASSED
  Scenario: Crear tarea completa con todos los campos   ✅ PASSED
  Scenario: Crear múltiples tareas mantiene el orden    ✅ PASSED
  Scenario: Título duplicado es permitido               ✅ PASSED

4 scenarios (4 passed)
12 steps (12 passed)
Elapsed time: 0.34s
```

### Diagrama de Trazabilidad

```
REQUISITO         ESCENARIO BDD        TEST UNITARIO           CÓDIGO
─────────────────────────────────────────────────────────────────────────
"Crear tarea"  →  crear_tarea.feature → test_create_task*()  → TaskService
  ↓                     ↓                     ↓                    ↓
"Con título"   →  "título Comprar..."  → test_valid_title()  → validate()
  ↓                     ↓                     ↓                    ↓
"Solo auth"    →  "usuario autenticado" → test_requires_auth() → user_id
  ↓                     ↓                     ↓                    ↓
"Max 200"      →  (Three Amigos conv.) → test_max_length()  → TITLE_MAX
```

---


## 9. Living Documentation (Documentación Viva)

### ¿Qué es Living Documentation?

> Es documentación que **se genera automáticamente** a partir de los escenarios BDD
> y **siempre está actualizada** porque si el código cambia y los tests fallan,
> la documentación refleja que algo no está cumpliendo lo especificado.

### ¿Por qué es Revolucionario?

| Documentación Tradicional | Living Documentation |
|--------------------------|---------------------|
| Se escribe una vez y se olvida | Se actualiza con cada ejecución de tests |
| Nadie sabe si está vigente | Si los tests pasan, la doc es correcta |
| Requiere mantenimiento manual | Se mantiene sola |
| Separada del código | ES el código (en forma legible) |

### Ejemplo de Reporte Generado

```
╭─────────────────────────────────────────────────────────────╮
│          📋 TASKFLOW — Living Documentation                  │
│          Generado: 2026-08-03 14:30:00                       │
╰─────────────────────────────────────────────────────────────╯

MÓDULO: Gestión de Tareas
━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Funcionalidad: Creación de Tareas (4/4 escenarios pasan)
   • Crear tarea con solo título ✅
   • Crear tarea completa ✅
   • Múltiples tareas mantiene orden ✅
   • Título duplicado permitido ✅

✅ Funcionalidad: Edición de Tareas (4/4 escenarios pasan)
   • Cambiar título ✅
   • Marcar como completada ✅
   • No editar tarea ajena ✅
   • Preserva historial ✅

⚠️ Funcionalidad: Eliminación de Tareas (3/4 escenarios pasan)
   • Eliminación requiere confirmación ✅
   • Cancelar no borra ✅
   • Recuperable por 30 días ✅
   • Purga después de 30 días ❌ (NO IMPLEMENTADO)

MÓDULO: Seguridad
━━━━━━━━━━━━━━━━━

✅ Funcionalidad: Registro (4/4) ✅
✅ Funcionalidad: Login (4/4) ✅
✅ Funcionalidad: Permisos (4/4) ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL: 23/24 escenarios pasan (95.8%)
COBERTURA BDD: 95.8%
ESTADO: ⚠️ CASI COMPLETO — 1 funcionalidad pendiente
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Cómo la IA Asistida Potencia Living Documentation

En el flujo de vibe coding con IA:

1. **TÚ** describes el comportamiento en Gherkin (o la IA te ayuda)
2. **LA IA** genera los step definitions
3. **LA IA** genera la implementación (TDD)
4. **EL SISTEMA** ejecuta y genera la documentación viva

```
Tu idea → Gherkin → Steps (IA) → Código (IA) → Tests (auto) → Docs (auto)
                                                                    ↑
                                                    SIEMPRE ACTUALIZADA
```

---

## 10. Ejercicios Prácticos

### Ejercicio 1: Tu Primer Escenario (15 min) 🌱

**Nivel**: Principiante
**Contexto**: Eres el dueño de una pastelería y quieres un sistema de pedidos.

**Instrucciones**:
1. Escribe la **Feature** (¿qué funcionalidad?)
2. Escribe la **User Story** (Como... Quiero... Para...)
3. Escribe **1 escenario** del camino feliz (happy path)
4. Escribe **1 escenario** de error

**Plantilla para completar**:

```gherkin
Feature: ___________________________________
  Como ___________________________________
  Quiero ___________________________________
  Para ___________________________________

  Scenario: _________________________________ (Happy Path)
    Given ___________________________________
    When ___________________________________
    Then ___________________________________

  Scenario: _________________________________ (Error)
    Given ___________________________________
    When ___________________________________
    Then ___________________________________
```

**Pista**: Piensa en "Un cliente hace un pedido de un pastel de cumpleaños"

---

### Ejercicio 2: Three Amigos Simulado (20 min) 👥

**Nivel**: Principiante
**Contexto**: Sistema de reservas de un restaurante.

**Instrucciones**:
Asume los 3 roles y escribe las preguntas/respuestas:

| Rol | Pregunta/Respuesta |
|-----|-------------------|
| 👤 Negocio | "Necesito que los clientes puedan reservar una mesa" |
| 🧑‍💻 Dev | (Pregunta: ¿___?) |
| 🧪 QA | (Pregunta: ¿___?) |
| 👤 Negocio | (Responde) |
| 🧪 QA | (Otra pregunta: ¿___?) |
| 👤 Negocio | (Responde) |

**Resultado**: Escribe 3 escenarios Gherkin derivados de la conversación.

---

### Ejercicio 3: De Gherkin a Tests (30 min) 🔧

**Nivel**: Intermedio
**Contexto**: TaskFlow — Feature de notificaciones.

**Se te da el escenario**:

```gherkin
Feature: Notificaciones de Tareas
  Como usuario con tareas con fecha límite
  Quiero recibir notificaciones antes del vencimiento
  Para no olvidar mis compromisos

  Scenario: Notificación 24 horas antes del vencimiento
    Given María tiene una tarea "Entregar informe" con fecha límite mañana
    When el sistema verifica tareas próximas a vencer
    Then María recibe una notificación
    And el mensaje dice "Tu tarea 'Entregar informe' vence mañana"
    And la notificación tiene prioridad "alta"
```

**Tu trabajo**:
1. Escribe el **step definition** para cada línea (pseudocódigo está bien)
2. Escribe **2 tests unitarios** que se derivarían de este escenario
3. Escribe **1 escenario adicional** que cubra un edge case

---

### Ejercicio 4: BDD para tu Profesión (30 min) 🎯

**Nivel**: Intermedio-Avanzado
**Contexto**: Aplica BDD a un problema de TU área profesional.

| Si eres... | Sistema sugerido |
|-----------|-----------------|
| Abogado | Sistema de seguimiento de expedientes |
| Economista | Dashboard de indicadores financieros |
| Gastrónomo | Sistema de inventario y recetas |
| Empresario | CRM de clientes y oportunidades |
| Educador | Plataforma de calificaciones |
| Informático | Ya sabes qué hacer 😉 |

**Instrucciones**:
1. Define **1 Feature** de tu sistema
2. Escribe **3 escenarios** (1 happy path, 1 error, 1 seguridad)
3. Para cada escenario, identifica qué **Concern ISO 42010** atiende
4. Identifica qué categoría **OWASP** podría ser relevante

---

### Ejercicio 5: Pipeline Completo con IA (45 min) 🚀

**Nivel**: Avanzado
**Contexto**: Usa tu herramienta de IA favorita para completar el ciclo.

**Instrucciones**:

1. **Escribe un Feature completo** (3+ escenarios) para una funcionalidad nueva de TaskFlow
2. **Pide a la IA** que genere los step definitions
3. **Pide a la IA** que genere tests unitarios (TDD RED)
4. **Pide a la IA** que implemente el código (TDD GREEN)
5. **Revisa** si la IA aplicó SOLID correctamente
6. **Documenta** qué decidiste cambiar y por qué (mini-ADR)

**Reflexión post-ejercicio**:
- ¿La IA entendió mejor con Gherkin que con instrucciones vagas?
- ¿El código generado cumple los escenarios?
- ¿Qué escenarios de seguridad agregarías?

---

### Ejercicio 6: Auditoría BDD (20 min) 🔍

**Nivel**: Para todos
**Contexto**: Evalúa la calidad de estos escenarios.

**Escenarios a evaluar** (marca cuáles son buenos ✅ y cuáles malos ❌):

```gherkin
# A)
Scenario: Test de login
  Given datos en la base de datos
  When llamo al endpoint POST /login con JSON
  Then status 200

# B)
Scenario: Usuario olvida su contraseña
  Given soy un usuario registrado que olvidó su contraseña
  When solicito un restablecimiento de contraseña con mi email
  Then recibo un enlace temporal en mi correo
  And el enlace expira en 24 horas

# C)
Scenario: Crear usuario
  Given un admin
  When crea usuario
  Then funciona

# D)
Scenario: Búsqueda de tareas por fecha devuelve resultados ordenados
  Given tengo tareas con fechas "2026-08-01", "2026-08-03", "2026-08-02"
  When busco tareas entre "2026-08-01" y "2026-08-03"
  Then obtengo 3 resultados
  And están ordenados cronológicamente
```

**Para cada uno**: ¿Por qué es bueno o malo? ¿Cómo lo mejorarías?

---

## 11. Errores Comunes y Cómo Evitarlos

### Error 1: Escribir escenarios demasiado técnicos

```gherkin
# ❌ MAL — Esto es un test de API, no un escenario de comportamiento
Scenario: POST /api/tasks retorna 201
  Given header "Content-Type: application/json"
  When POST "/api/tasks" con body {"title": "test", "user_id": 1}
  Then response status code es 201
  And response body contiene campo "id"

# ✅ BIEN — Describe comportamiento, no implementación
Scenario: Usuario crea una tarea nueva
  Given un usuario autenticado "María"
  When María crea una tarea con título "Preparar presentación"
  Then la tarea se registra exitosamente
  And aparece en la lista de María
```

**Regla**: Si necesitas saber HTTP, JSON o SQL para entender el escenario, está mal escrito.

### Error 2: Escenarios que dependen unos de otros

```gherkin
# ❌ MAL — El Scenario 2 asume que Scenario 1 ya se ejecutó
Scenario: Crear usuario
  When creo el usuario "María"
  Then se crea exitosamente

Scenario: El usuario creado puede loguearse
  When María inicia sesión     # ← ¿Y si el test anterior falló?
  Then accede al sistema

# ✅ BIEN — Cada escenario es independiente
Scenario: Usuario registrado puede iniciar sesión
  Given existe un usuario "María" con credenciales válidas  # ← Se crea aquí
  When María inicia sesión
  Then accede al sistema
```

**Regla**: Cada escenario debe funcionar solo, sin importar el orden.

### Error 3: Escenarios demasiado largos

```gherkin
# ❌ MAL — 15 pasos, mezcla múltiples comportamientos
Scenario: Flujo completo
  Given un usuario
  And está registrado
  And está logueado
  And tiene el rol admin
  When crea una tarea
  And le pone título
  And le pone descripción
  And le asigna prioridad
  And la guarda
  Then la tarea se crea
  And aparece en la lista
  And se puede editar
  And se puede eliminar
  And notifica al usuario
  And actualiza las métricas

# ✅ BIEN — Un escenario por comportamiento
Scenario: Admin crea tarea completa
  Given un administrador autenticado
  When crea una tarea con título, descripción y prioridad alta
  Then la tarea se registra exitosamente

Scenario: Creación de tarea genera notificación
  Given un usuario acaba de crear una tarea
  Then recibe una confirmación
```

**Regla**: Un escenario = un comportamiento. Si tiene más de 7 líneas, divídelo.

### Error 4: No cubrir los casos negativos

```gherkin
# ❌ INCOMPLETO — Solo el happy path
Feature: Login
  Scenario: Login exitoso
    Given usuario registrado
    When inicia sesión con datos correctos
    Then accede al sistema

# ✅ COMPLETO — Happy path + errores + seguridad
Feature: Login
  Scenario: Login exitoso con credenciales correctas
    ...
  Scenario: Login fallido con contraseña incorrecta
    ...
  Scenario: Login bloqueado tras 5 intentos fallidos
    ...
  Scenario: Login con cuenta desactivada
    ...
```

**Regla**: Por cada happy path, escribe al menos 2 escenarios de error/edge case.

### Error 5: Usar BDD para todo (over-BDD)

```gherkin
# ❌ INNECESARIO — Esto es un detalle técnico, no comportamiento
Scenario: La base de datos usa índice en campo email
  Given la tabla users
  When consulto el schema
  Then el campo email tiene un índice B-tree

# ✅ ESTO SÍ ES BDD — Comportamiento observable por el usuario
Scenario: Búsqueda por email es rápida
  Given existen 10,000 usuarios registrados
  When busco un usuario por email
  Then obtengo el resultado en menos de 100ms
```

**Regla**: BDD es para COMPORTAMIENTO visible. Detalles técnicos van en tests unitarios.

---

## 12. Referencias

### Libros Fundamentales

| Libro | Autor | Lo que Aporta |
|-------|-------|---------------|
| *BDD in Action* (2nd Ed.) | John Ferguson Smart | Guía completa de BDD |
| *The Cucumber Book* | Matt Wynne, Aslak Hellesøy | Gherkin y Cucumber en detalle |
| *Specification by Example* | Gojko Adzic | Colaboración con ejemplos |
| *Writing Great Specifications* | Kamil Nicieja | Cómo escribir buenos escenarios |

### Herramientas

| Herramienta | Lenguaje | Uso |
|-------------|----------|-----|
| **behave** | Python | Framework BDD usado en este proyecto |
| **pytest-bdd** | Python | Alternativa que integra con pytest |
| **Cucumber** | Multi (Ruby, Java, JS) | El framework BDD original |
| **SpecFlow** | .NET | BDD para ecosistema Microsoft |

### Estándares Relacionados

| Estándar | Conexión con BDD |
|----------|-----------------|
| ISO 42010 | Los escenarios documentan concerns de stakeholders |
| ISO 25010 | BDD verifica adecuación funcional y usabilidad |
| ISO 25022 | Los escenarios miden efectividad (quality in use) |
| ISO 9241 | Escenarios de UX validan principios de usabilidad |
| OWASP | Escenarios de seguridad verifican controles |

### Enlaces Útiles

- [behave Documentation](https://behave.readthedocs.io/)
- [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)
- [BDD Practices](https://cucumber.io/docs/bdd/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

---

## Control de Cambios

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0.0 | 2026-08-03 | Versión inicial completa del recurso formativo |

---

> **Este documento es un recurso académico para el taller de Desarrollo Asistido por IA.**
> Está diseñado para ser usado progresivamente: de la Sección 1 a la 11 durante el taller,
> con los ejercicios intercalados para reforzar cada concepto.
>
> Los archivos de features y step definitions completos están en:
> - `agents/bdd/features/` — Escenarios Gherkin
> - `agents/bdd/features/steps/` — Step Definitions
> - `examples/taskflow/` — Proyecto ejemplo
