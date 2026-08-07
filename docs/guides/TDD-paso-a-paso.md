# Guía TDD Paso a Paso
## Test-Driven Development — Desarrollo Guiado por Tests

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0.0 |
| **Fecha** | 2026-08-03 |
| **Público** | Profesionales multidisciplinarios (universitario+) |
| **Prerrequisitos** | Haber completado la guía BDD (docs/guides/BDD-paso-a-paso.md) |
| **Duración estimada** | 4-6 horas (taller completo) |
| **Proyecto ejemplo** | TaskFlow — Sistema de gestión de tareas |

---

## Tabla de Contenidos

1. [¿Qué es TDD?](#1-qué-es-tdd)
2. [¿Por qué TDD importa?](#2-por-qué-tdd-importa)
3. [El Ciclo Red-Green-Refactor](#3-el-ciclo-red-green-refactor)
4. [Las Reglas de TDD](#4-las-reglas-de-tdd)
5. [De BDD a TDD: El Puente](#5-de-bdd-a-tdd-el-puente)
6. [TDD en Acción: TaskFlow](#6-tdd-en-acción-taskflow)
7. [El Paso REFACTOR con SOLID](#7-el-paso-refactor-con-solid)
8. [Patrones de Testing](#8-patrones-de-testing)
9. [TDD y la IA Asistida](#9-tdd-y-la-ia-asistida)
10. [Ejercicios Prácticos](#10-ejercicios-prácticos)
11. [Errores Comunes](#11-errores-comunes)
12. [Referencias](#12-referencias)

---

## 1. ¿Qué es TDD?

### Definición Simple

> **TDD es escribir la prueba de lo que quieres que haga el código ANTES
> de escribir el código que lo hace.**

Es como un GPS: primero defines el destino (test), y luego conduces (código)
hasta llegar ahí.

### Definición Técnica

TDD (Test-Driven Development) es una disciplina de desarrollo donde:

1. **Escribes un test** que describe un comportamiento esperado
2. **Verificas que falla** (porque el código no existe aún)
3. **Escribes el código mínimo** para que el test pase
4. **Refactorizas** el código sin romper el test
5. **Repites** para el siguiente comportamiento

### La Metáfora del Arquitecto 🏗️

```
┌──────────────────────────────────────────────────────────────┐
│                                                                │
│  CONSTRUCCIÓN TRADICIONAL:                                     │
│  "Construye la casa, y al final vemos si quedó bien"          │
│  → Descubres que una pared está torcida cuando ya pintaste    │
│                                                                │
│  CONSTRUCCIÓN CON TDD:                                         │
│  "Antes de poner cada ladrillo, verifico con la plomada"      │
│  → Cada pieza se valida ANTES de avanzar a la siguiente       │
│                                                                │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐                   │
│  │ PLOMADA │───▶│ LADRILLO│───▶│VERIFICAR│───▶ Siguiente      │
│  │ (test)  │    │ (código)│    │(pasa?)  │    ladrillo        │
│  └─────────┘    └─────────┘    └─────────┘                   │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

### TDD vs Testing Tradicional

| Aspecto | Testing Tradicional | TDD |
|---------|-------------------|-----|
| **Orden** | Código primero → tests después | Tests primero → código después |
| **Propósito del test** | Encontrar bugs | Guiar el diseño |
| **¿Cuándo se escriben?** | Al final (si hay tiempo) | Desde el principio |
| **Cobertura** | Variable (a veces 30-50%) | Alta por naturaleza (80-100%) |
| **Confianza para cambiar** | "Tengo miedo de tocar eso" | "Cambio y los tests me avisan" |
| **Diseño del código** | Puede ser desordenado | Tiende a ser limpio (testeable = bien diseñado) |

---

## 2. ¿Por qué TDD importa?

### Para el Empresario / Product Owner


- ✅ **Menos bugs en producción** — Los defectos se detectan antes de llegar al usuario
- ✅ **Velocidad sostenible** — El equipo no frena por "deuda técnica acumulada"
- ✅ **Cambios sin miedo** — Puedes pivotar funcionalidades sin romper lo existente
- ✅ **Costo predecible** — Menos sorpresas, menos hotfixes de emergencia

### Para el Profesional Legal / Compliance
- ✅ **Evidencia auditable** — Cada funcionalidad tiene un test que la verifica
- ✅ **Trazabilidad** — Del requisito al test al código: cadena verificable
- ✅ **Regresión controlada** — Si algo se rompe, se detecta inmediatamente

### Para el Desarrollador
- ✅ **Diseño emergente** — El código se diseña para ser testeable = bien diseñado
- ✅ **Red de seguridad** — Refactorizar sin miedo, los tests te protegen
- ✅ **Documentación ejecutable** — Los tests documentan cómo se usa el código
- ✅ **Flow state** — Ciclos cortos de feedback mantienen el foco

### Para el Economista / Analista
- ✅ **ROI demostrable**: Estudios muestran reducción de 40-90% de bugs post-release
- ✅ **TCO menor**: Código TDD cuesta más inicialmente pero menos a largo plazo

### El Costo de un Bug por Fase

```
Costo relativo de corregir un defecto:

    $500 ┤                                          ████
         │                                          ████
    $200 ┤                              ████        ████
         │                              ████        ████
     $50 ┤                  ████        ████        ████
         │                  ████        ████        ████
     $10 ┤      ████        ████        ████        ████
         │      ████        ████        ████        ████
      $1 ┤████  ████        ████        ████        ████
         │████  ████        ████        ████        ████
         └──────────────────────────────────────────────
          TDD   Diseño    Coding     Testing    Producción
          ↑
     "AQUÍ detectas con TDD"
```

---

## 3. El Ciclo Red-Green-Refactor

### El Corazón de TDD

```
         ┌─────────────────────────────────────┐
         │                                       │
         │        🔴 RED                         │
         │    "Escribe un test que FALLA"        │
         │                                       │
         └──────────────────┬──────────────────┘
                            │
                            ▼
         ┌─────────────────────────────────────┐
         │                                       │
         │        🟢 GREEN                       │
         │    "Escribe el código MÍNIMO          │
         │     para que el test PASE"            │
         │                                       │
         └──────────────────┬──────────────────┘
                            │
                            ▼
         ┌─────────────────────────────────────┐
         │                                       │
         │        🔵 REFACTOR                    │
         │    "Mejora el código SIN romper       │
         │     los tests"                        │
         │                                       │
         └──────────────────┬──────────────────┘
                            │
                            └──────────▶ Vuelve a 🔴
```

### ¿Qué significa cada color?

| Fase | Color | Duración | Qué haces | Qué NO haces |
|------|-------|----------|-----------|--------------|
| **RED** | 🔴 | 1-3 min | Escribes UN test que falla | No escribes código de producción |
| **GREEN** | 🟢 | 3-5 min | Escribes lo MÍNIMO para pasar | No optimizas, no refactorizas |
| **REFACTOR** | 🔵 | 3-10 min | Mejoras diseño y limpieza | No agregas funcionalidad nueva |

### Ejemplo Trivial (para entender el ciclo)

Queremos una función que sume dos números:

```python
# ═══════════════════════════════════════════
# 🔴 RED — El test (sumador NO existe aún)
# ═══════════════════════════════════════════
def test_suma_dos_numeros():
    resultado = sumar(2, 3)
    assert resultado == 5

# Ejecuto → ❌ FALLA: NameError: name 'sumar' is not defined
# ¡PERFECTO! Eso es lo que queremos en RED.


# ═══════════════════════════════════════════
# 🟢 GREEN — Implementación MÍNIMA
# ═══════════════════════════════════════════
def sumar(a, b):
    return a + b

# Ejecuto → ✅ PASA
# ¡Funciona! Pero es tan simple que no necesita refactor.


# ═══════════════════════════════════════════
# 🔴 RED — Siguiente test (más complejo)
# ═══════════════════════════════════════════
def test_suma_no_acepta_strings():
    with pytest.raises(TypeError):
        sumar("hola", 3)

# Ejecuto → ❌ FALLA (Python sí concatena "hola" + 3... bueno, da error)
# Hmm, veamos...


# ═══════════════════════════════════════════
# 🟢 GREEN — Agrego validación mínima
# ═══════════════════════════════════════════
def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Solo se pueden sumar números")
    return a + b

# Ejecuto → ✅ AMBOS tests pasan


# ═══════════════════════════════════════════
# 🔵 REFACTOR — Mejoro sin romper tests
# ═══════════════════════════════════════════
from typing import Union

Number = Union[int, float]

def sumar(a: Number, b: Number) -> Number:
    """Suma dos números con validación de tipos."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Solo se pueden sumar números")
    return a + b

# Ejecuto → ✅ SIGUE PASANDO (refactor exitoso)
```

---

## 4. Las Reglas de TDD

### Las 3 Leyes de TDD (Robert C. Martin)

> **Ley 1**: No puedes escribir código de producción sin antes tener un test que falle.
>
> **Ley 2**: No puedes escribir más de un test unitario que sea suficiente para fallar
> (no compilar cuenta como fallar).
>
> **Ley 3**: No puedes escribir más código de producción del estrictamente necesario
> para que el test pase.

### Traducido a Lenguaje Cotidiano

| Ley | En simple | Analogía |
|-----|-----------|----------|
| **Ley 1** | "No construyas sin plano" | No pones un ladrillo sin saber dónde va |
| **Ley 2** | "Un paso a la vez" | No haces 5 preguntas a la vez en un examen |
| **Ley 3** | "No te adelantes" | No pintas la pared antes de que seque el cemento |

### Reglas Prácticas Adicionales

| Regla | Significado | Ejemplo |
|-------|-------------|---------|
| **KISS** | Keep It Simple, Stupid | La solución más simple que pase el test |
| **YAGNI** | You Ain't Gonna Need It | No agregues "por si acaso" |
| **One assert** | Un test, una verificación principal | No testees 10 cosas en un test |
| **Arrange-Act-Assert** | Estructura clara en 3 partes | Given-When-Then del test |
| **F.I.R.S.T.** | Fast, Independent, Repeatable, Self-validating, Timely | Tests de calidad |

### F.I.R.S.T. — Características de Buenos Tests

| Letra | Significado | Por qué importa |
|-------|-------------|-----------------|
| **F**ast | Rápidos (ms, no segundos) | Si son lentos, no los ejecutas seguido |
| **I**ndependent | No dependen de otros tests | Puedes ejecutar uno solo sin problemas |
| **R**epeatable | Mismo resultado siempre | No fallan "a veces" (flaky tests) |
| **S**elf-validating | Pasan o fallan (boolean) | No necesitas revisar logs manualmente |
| **T**imely | Se escriben a tiempo (ANTES) | Si los escribes después, ya no es TDD |

---

## 5. De BDD a TDD: El Puente

### ¿Cómo se conectan BDD y TDD?

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                       │
│  BDD (MACRO)                    TDD (MICRO)                          │
│  ───────────                    ──────────                           │
│  "QUÉ debe hacer               "CÓMO funciona                       │
│   el sistema"                    internamente"                        │
│                                                                       │
│  Escenario Gherkin              Test Unitario                        │
│  (lenguaje humano)              (lenguaje código)                    │
│                                                                       │
│  ┌────────────────┐            ┌────────────────────┐               │
│  │ Scenario:      │  genera    │ def test_create_   │               │
│  │ Crear tarea    │──────────▶ │     task():        │               │
│  │ Given...       │  múltiples │   assert ...       │               │
│  │ When...        │  tests     │                    │               │
│  │ Then...        │            │ def test_task_     │               │
│  └────────────────┘            │     validation():  │               │
│                                │   assert ...       │               │
│                                └────────────────────┘               │
│                                                                       │
│  SCOPE: Comportamiento          SCOPE: Una función/método            │
│  QUIÉN: Negocio + Dev + QA      QUIÉN: Desarrollador                 │
│  NIVEL: Aceptación              NIVEL: Unitario                      │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

### Tabla de Traducción: Escenario BDD → Tests TDD

| Escenario BDD | Tests TDD Derivados |
|---------------|-------------------|
| "Crear tarea exitosamente" | `test_create_task_returns_task_with_id` |
| | `test_create_task_sets_default_status_pending` |
| | `test_create_task_sets_creation_date_today` |
| "No puedo crear sin título" | `test_create_task_empty_title_raises_error` |
| | `test_create_task_none_title_raises_error` |
| "Título max 200 chars" | `test_create_task_title_201_chars_raises_error` |
| | `test_create_task_title_200_chars_ok` |
| "Solo autenticados" | `test_create_task_no_user_raises_permission_error` |

### La Regla de Derivación

> **Un escenario BDD genera N tests unitarios**, donde N = (condiciones × verificaciones).
> - Cada **Given** puede generar tests de precondiciones
> - Cada **When** genera tests de la acción
> - Cada **Then** genera tests de verificación

---


## 6. TDD en Acción: TaskFlow

### Ciclo Completo #1: Crear Tarea

Vamos a implementar la creación de tareas usando TDD puro.
Cada paso está numerado y explicado.

#### 🔴 RED — Escribimos tests que FALLAN

```python
# tests/unit/test_task_service.py
"""
Tests unitarios para TaskService — derivados del escenario BDD:
'Feature: Creación de Tareas'

NOTA EDUCATIVA:
- Estos tests se escriben ANTES del código
- DEBEN fallar cuando los ejecutas por primera vez
- Si no fallan, algo está mal (el test no está testeando nada nuevo)

Patrón: Arrange-Act-Assert (equivalente a Given-When-Then)
"""

import pytest
from datetime import date


class TestCreateTask:
    """
    Tests derivados del escenario BDD:
    'Scenario: Crear tarea con solo título (mínimo)'

    Escenario original (Gherkin):
      Given un usuario autenticado "María García"
      When María crea una tarea con título "Comprar insumos"
      Then la tarea se crea exitosamente
      And tiene estado "pendiente" por defecto
      And tiene prioridad "media" por defecto
      And la fecha de creación es hoy
    """

    def test_create_task_with_valid_title_returns_task(self):
        """
        Derivado de: 'Then la tarea se crea exitosamente'
        Verifica que la operación retorna una tarea con ID.
        """
        # Arrange (Given)
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        # Act (When)
        result = service.create_task(
            titulo="Comprar insumos",
            user_id=1
        )

        # Assert (Then)
        assert result is not None
        assert result.id is not None
        assert result.id > 0
        assert result.titulo == "Comprar insumos"

    def test_create_task_default_status_is_pending(self):
        """
        Derivado de: 'And tiene estado "pendiente" por defecto'
        """
        # Arrange
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        # Act
        result = service.create_task(titulo="Mi tarea", user_id=1)

        # Assert
        assert result.estado == "pendiente"

    def test_create_task_default_priority_is_media(self):
        """
        Derivado de: 'And tiene prioridad "media" por defecto'
        """
        # Arrange
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        # Act
        result = service.create_task(titulo="Mi tarea", user_id=1)

        # Assert
        assert result.prioridad == "media"

    def test_create_task_sets_today_as_creation_date(self):
        """
        Derivado de: 'And la fecha de creación es hoy'
        """
        # Arrange
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        # Act
        result = service.create_task(titulo="Mi tarea", user_id=1)

        # Assert
        assert result.fecha_creacion == date.today()

    def get_test_db(self):
        """Helper: retorna una sesión de DB de test."""
        from examples.taskflow.api.database import get_test_session
        return get_test_session()


class TestCreateTaskValidation:
    """
    Tests derivados del escenario BDD:
    'Scenario: No puedo crear tarea sin título'

    Escenario original (Gherkin):
      When María intenta crear una tarea sin título
      Then recibe un mensaje de error claro
      And el mensaje dice "El título es obligatorio"
      And no se crea ninguna tarea
    """

    def test_empty_title_raises_value_error(self):
        """
        Derivado de: 'When María intenta crear una tarea sin título'
        Título vacío ("") es inválido.
        """
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        with pytest.raises(ValueError) as exc_info:
            service.create_task(titulo="", user_id=1)

        assert "título es obligatorio" in str(exc_info.value).lower()

    def test_none_title_raises_value_error(self):
        """
        Caso adicional: título None también es inválido.
        """
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        with pytest.raises(ValueError):
            service.create_task(titulo=None, user_id=1)

    def test_whitespace_only_title_raises_value_error(self):
        """
        Caso adicional: título con solo espacios no es válido.
        """
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        with pytest.raises(ValueError) as exc_info:
            service.create_task(titulo="   ", user_id=1)

        assert "título es obligatorio" in str(exc_info.value).lower()

    def test_title_too_long_raises_value_error(self):
        """
        Derivado de: 'Scenario: El título tiene un límite de caracteres'
        """
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        titulo_largo = "A" * 201

        with pytest.raises(ValueError) as exc_info:
            service.create_task(titulo=titulo_largo, user_id=1)

        assert "200" in str(exc_info.value)

    def test_title_exactly_200_chars_is_valid(self):
        """
        Boundary test: exactamente 200 caracteres SÍ es válido.

        NOTA EDUCATIVA:
        Los 'boundary tests' prueban los LÍMITES exactos.
        Si el máximo es 200, pruebas: 200 (ok) y 201 (error).
        """
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        titulo_limite = "A" * 200
        result = service.create_task(titulo=titulo_limite, user_id=1)

        assert result.titulo == titulo_limite

    def test_title_too_short_raises_value_error(self):
        """
        Derivado de: Three Amigos (mínimo 3 caracteres).
        """
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        with pytest.raises(ValueError) as exc_info:
            service.create_task(titulo="AB", user_id=1)

        assert "3" in str(exc_info.value)

    def get_test_db(self):
        from examples.taskflow.api.database import get_test_session
        return get_test_session()


class TestCreateTaskAuthentication:
    """
    Tests derivados del escenario BDD:
    'Scenario: No puedo crear tareas sin estar autenticada'

    Escenario original (Gherkin):
      Given que no estoy autenticada
      When intento crear una tarea
      Then recibo un error de acceso denegado
    """

    def test_no_user_id_raises_permission_error(self):
        """
        Derivado de: 'Then recibo un error de acceso denegado'
        Sin user_id, la operación debe ser rechazada.
        """
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        with pytest.raises(PermissionError):
            service.create_task(titulo="Tarea válida", user_id=None)

    def test_user_id_zero_raises_permission_error(self):
        """
        Caso adicional: user_id=0 tampoco es válido.
        """
        from examples.taskflow.api.services.task_service import TaskService
        service = TaskService(db=self.get_test_db())

        with pytest.raises(PermissionError):
            service.create_task(titulo="Tarea válida", user_id=0)

    def get_test_db(self):
        from examples.taskflow.api.database import get_test_session
        return get_test_session()
```

**Ejecutamos → TODO FALLA ❌** (¡exactamente lo que queremos!)

```bash
$ pytest tests/unit/test_task_service.py -v --tb=short

FAILED test_create_task_with_valid_title_returns_task
    ModuleNotFoundError: No module named 'examples.taskflow.api.services'
FAILED test_create_task_default_status_is_pending
    ModuleNotFoundError: No module named 'examples.taskflow.api.services'
FAILED test_empty_title_raises_value_error
    ModuleNotFoundError: No module named 'examples.taskflow.api.services'
... (10 tests más)

══════════════ 13 FAILED in 0.08s ══════════════
```

**¿Por qué celebramos que todo falla? 🎉**

Porque confirma que:
1. Los tests están bien escritos (detectan la ausencia del código)
2. No tenemos "falsos positivos" (tests que pasan sin razón)
3. Sabemos exactamente QUÉ necesitamos implementar

---


#### 🟢 GREEN — Escribimos el código MÍNIMO para que pase

```python
# examples/taskflow/api/services/task_service.py
"""
TaskService — Primera implementación (GREEN).

NOTA EDUCATIVA:
Esta es la implementación MÍNIMA que hace pasar los tests.
- NO está optimizada
- NO está bonita
- NO sigue SOLID perfectamente todavía
- PERO hace pasar los tests → eso es lo único que importa en GREEN

La belleza viene en REFACTOR. Ahora solo importa que FUNCIONE.
"""

from datetime import date
from typing import Optional

from examples.taskflow.api.models import Task
from examples.taskflow.api.schemas import TaskResponse


class TaskService:
    """Servicio de gestión de tareas (versión GREEN — mínima)."""

    def __init__(self, db):
        self._db = db

    def create_task(
        self,
        titulo: Optional[str],
        user_id: Optional[int],
        descripcion: str = "",
        prioridad: str = "media",
    ) -> TaskResponse:
        """
        Crea una nueva tarea.

        Raises:
            PermissionError: Si no hay usuario autenticado
            ValueError: Si los datos son inválidos
        """
        # Validar autenticación
        if not user_id:
            raise PermissionError("Se requiere autenticación")

        # Validar título
        if titulo is None or titulo.strip() == "":
            raise ValueError("El título es obligatorio")

        titulo_limpio = titulo.strip()

        if len(titulo_limpio) < 3:
            raise ValueError("El título debe tener al menos 3 caracteres")

        if len(titulo_limpio) > 200:
            raise ValueError("El título no puede exceder 200 caracteres")

        # Crear tarea
        task = Task(
            titulo=titulo_limpio,
            descripcion=descripcion,
            estado="pendiente",
            prioridad=prioridad,
            user_id=user_id,
            fecha_creacion=date.today(),
        )

        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)

        return TaskResponse(
            id=task.id,
            titulo=task.titulo,
            descripcion=task.descripcion,
            estado=task.estado,
            prioridad=task.prioridad,
            fecha_creacion=task.fecha_creacion,
        )
```

**Ejecutamos → TODOS PASAN ✅**

```bash
$ pytest tests/unit/test_task_service.py -v

PASSED test_create_task_with_valid_title_returns_task
PASSED test_create_task_default_status_is_pending
PASSED test_create_task_default_priority_is_media
PASSED test_create_task_sets_today_as_creation_date
PASSED test_empty_title_raises_value_error
PASSED test_none_title_raises_value_error
PASSED test_whitespace_only_title_raises_value_error
PASSED test_title_too_long_raises_value_error
PASSED test_title_exactly_200_chars_is_valid
PASSED test_title_too_short_raises_value_error
PASSED test_no_user_id_raises_permission_error
PASSED test_user_id_zero_raises_permission_error

══════════════ 12 passed in 0.15s ══════════════
```

---

### Ciclo Completo #2: Autenticación (con seguridad OWASP)

#### 🔴 RED — Tests de autenticación

```python
# tests/unit/test_auth_service.py
"""
Tests unitarios para AuthService — derivados del escenario BDD:
'Feature: Inicio de Sesión'

NOTA EDUCATIVA (OWASP A07):
Estos tests verifican controles de seguridad:
- Mensajes genéricos (no revelar información)
- Bloqueo por fuerza bruta (rate limiting)
- Hash seguro de contraseñas (nunca texto plano)
"""

import pytest
from datetime import datetime, timedelta


class TestLogin:
    """
    Derivado de: 'Scenario: Login exitoso con credenciales correctas'
    """

    def test_login_with_correct_credentials_returns_token(self):
        """El login exitoso retorna un token JWT."""
        from examples.taskflow.api.services.auth_service import AuthService
        service = AuthService(db=self.get_test_db())

        # Primero registramos
        service.register(
            nombre="María",
            email="maria@test.com",
            password="MiClave$egura2026"
        )

        # Login
        result = service.login(email="maria@test.com", password="MiClave$egura2026")

        assert result is not None
        assert "token" in result
        assert len(result["token"]) > 0

    def test_login_returns_user_name(self):
        """El login exitoso incluye el nombre del usuario."""
        from examples.taskflow.api.services.auth_service import AuthService
        service = AuthService(db=self.get_test_db())

        service.register(nombre="María", email="maria@test.com", password="Clave$123")
        result = service.login(email="maria@test.com", password="Clave$123")

        assert result["nombre"] == "María"

    def get_test_db(self):
        from examples.taskflow.api.database import get_test_session
        return get_test_session()


class TestLoginSecurity:
    """
    Derivado de: 'Scenario: Login fallido con contraseña incorrecta'

    OWASP A07 — Estos tests verifican que la autenticación
    NO revela información útil a un atacante.
    """

    def test_wrong_password_raises_auth_error(self):
        """Contraseña incorrecta da error genérico."""
        from examples.taskflow.api.services.auth_service import AuthService
        service = AuthService(db=self.get_test_db())

        service.register(nombre="María", email="maria@test.com", password="Correcta$123")

        with pytest.raises(AuthenticationError) as exc_info:
            service.login(email="maria@test.com", password="Incorrecta")

        # OWASP: El mensaje NO debe decir "contraseña incorrecta"
        assert "credenciales inválidas" in str(exc_info.value).lower()

    def test_nonexistent_email_raises_same_error(self):
        """
        Email inexistente da el MISMO error que contraseña incorrecta.

        NOTA EDUCATIVA (OWASP):
        Si el mensaje fuera diferente para "email no existe" vs "password mal",
        un atacante podría ENUMERAR emails válidos probando miles de emails
        y viendo cuáles dan "password incorrecta" (= email existe).
        """
        from examples.taskflow.api.services.auth_service import AuthService
        service = AuthService(db=self.get_test_db())

        with pytest.raises(AuthenticationError) as exc_info:
            service.login(email="noexiste@test.com", password="Cualquiera")

        # MISMO mensaje que contraseña incorrecta
        assert "credenciales inválidas" in str(exc_info.value).lower()

    def test_password_never_stored_in_plain_text(self):
        """
        La contraseña NUNCA se guarda en texto plano.

        NOTA EDUCATIVA (OWASP A02 — Cryptographic Failures):
        Si alguien accede a la base de datos, NO debe poder leer passwords.
        Se almacena un HASH (irreversible) + SALT (aleatorio).
        """
        from examples.taskflow.api.services.auth_service import AuthService
        service = AuthService(db=self.get_test_db())

        service.register(nombre="María", email="maria@test.com", password="MiClave$123")

        # Verificar directamente en DB
        user = self.get_test_db().query(User).filter_by(email="maria@test.com").first()

        assert user.password_hash != "MiClave$123"  # No está en texto plano
        assert len(user.password_hash) > 50  # Un hash tiene mínimo ~60 chars

    def get_test_db(self):
        from examples.taskflow.api.database import get_test_session
        return get_test_session()


class TestBruteForceProtection:
    """
    Derivado de: 'Scenario: Bloqueo de cuenta tras múltiples intentos fallidos'

    NOTA EDUCATIVA (OWASP A07):
    Sin protección contra fuerza bruta, un atacante puede probar
    MILLONES de contraseñas por minuto hasta acertar.
    El bloqueo temporal limita los intentos.
    """

    def test_account_locks_after_5_failed_attempts(self):
        """La cuenta se bloquea tras 5 intentos fallidos."""
        from examples.taskflow.api.services.auth_service import AuthService
        service = AuthService(db=self.get_test_db())

        service.register(nombre="María", email="maria@test.com", password="Correcta$123")

        # 5 intentos fallidos
        for i in range(5):
            with pytest.raises(AuthenticationError):
                service.login(email="maria@test.com", password=f"Incorrecta{i}")

        # El 6to intento, incluso con password correcta, falla por bloqueo
        with pytest.raises(AccountLockedError) as exc_info:
            service.login(email="maria@test.com", password="Correcta$123")

        assert "bloqueada" in str(exc_info.value).lower()

    def test_account_unlocks_after_timeout(self):
        """La cuenta se desbloquea después del tiempo configurado."""
        from examples.taskflow.api.services.auth_service import AuthService
        from unittest.mock import patch

        service = AuthService(db=self.get_test_db())
        service.register(nombre="María", email="maria@test.com", password="Correcta$123")

        # Bloquear cuenta
        for i in range(5):
            try:
                service.login(email="maria@test.com", password=f"Wrong{i}")
            except Exception:
                pass

        # Simular que pasaron 15 minutos
        future = datetime.now() + timedelta(minutes=16)
        with patch('examples.taskflow.api.services.auth_service.datetime') as mock_dt:
            mock_dt.now.return_value = future
            mock_dt.side_effect = lambda *args, **kw: datetime(*args, **kw)

            # Ahora SÍ debe funcionar
            result = service.login(email="maria@test.com", password="Correcta$123")
            assert "token" in result

    def test_failed_attempts_counter_resets_after_success(self):
        """Login exitoso reinicia el contador de intentos."""
        from examples.taskflow.api.services.auth_service import AuthService
        service = AuthService(db=self.get_test_db())

        service.register(nombre="María", email="maria@test.com", password="Correcta$123")

        # 3 intentos fallidos (no llega al límite de 5)
        for i in range(3):
            try:
                service.login(email="maria@test.com", password=f"Wrong{i}")
            except Exception:
                pass

        # Login exitoso
        result = service.login(email="maria@test.com", password="Correcta$123")
        assert "token" in result

        # Otros 3 intentos fallidos (si no se reinició, serían 6 y bloquearía)
        for i in range(3):
            with pytest.raises(AuthenticationError):
                service.login(email="maria@test.com", password=f"Wrong{i}")

        # Todavía no está bloqueada (porque se reinició el contador)
        result = service.login(email="maria@test.com", password="Correcta$123")
        assert "token" in result

    def get_test_db(self):
        from examples.taskflow.api.database import get_test_session
        return get_test_session()
```

---


## 7. El Paso REFACTOR con SOLID

### ¿Cuándo y por qué refactorizar?

| Señal | Problema | Solución SOLID |
|-------|----------|----------------|
| Método con >20 líneas | Hace demasiadas cosas | **SRP**: Extraer a clase/método separado |
| `if/elif/elif` largo | Difícil de extender | **OCP**: Usar polimorfismo o strategy |
| Cambiar un archivo rompe otro | Acoplamiento alto | **DIP**: Inyectar dependencias |
| Tests requieren mucho setup | Objeto hace demasiado | **ISP**: Interfaces más pequeñas |
| Copy-paste de lógica | Duplicación | **DRY** + extraer abstracción |

### Refactoring #1: Extraer Validación (SRP)

**ANTES** (todo en un método):

```python
class TaskService:
    def create_task(self, titulo, user_id, ...):
        # Autenticación (responsabilidad 1)
        if not user_id:
            raise PermissionError(...)

        # Validación (responsabilidad 2)
        if titulo is None or titulo.strip() == "":
            raise ValueError(...)
        if len(titulo.strip()) < 3:
            raise ValueError(...)
        if len(titulo.strip()) > 200:
            raise ValueError(...)

        # Persistencia (responsabilidad 3)
        task = Task(...)
        self._db.add(task)
        ...
```

**DESPUÉS** (cada clase tiene UNA responsabilidad):

```python
# validators/task_validator.py
class TaskValidator:
    """
    SRP: Solo se encarga de validar datos de tareas.
    No persiste, no autentica, no notifica.
    """

    TITLE_MIN = 3
    TITLE_MAX = 200

    def validate_title(self, titulo: Optional[str]) -> str:
        """Valida y limpia el título. Retorna título limpio o lanza error."""
        if titulo is None or titulo.strip() == "":
            raise ValueError("El título es obligatorio")

        clean = titulo.strip()

        if len(clean) < self.TITLE_MIN:
            raise ValueError(
                f"El título debe tener al menos {self.TITLE_MIN} caracteres"
            )
        if len(clean) > self.TITLE_MAX:
            raise ValueError(
                f"El título no puede exceder {self.TITLE_MAX} caracteres"
            )

        return clean


# services/task_service.py
class TaskService:
    """
    SRP: Coordina la creación de tareas.
    Delega validación a TaskValidator y persistencia a TaskRepository.
    DIP: Recibe dependencias inyectadas (no las crea).
    """

    def __init__(self, db, validator: TaskValidator = None):
        self._db = db
        self._validator = validator or TaskValidator()

    def create_task(self, titulo, user_id, descripcion="", prioridad="media"):
        # Auth check (podría extraerse a un decorador en el futuro)
        if not user_id:
            raise PermissionError("Se requiere autenticación")

        # Validación delegada (SRP)
        titulo_limpio = self._validator.validate_title(titulo)

        # Persistencia
        task = Task(
            titulo=titulo_limpio,
            descripcion=descripcion,
            estado="pendiente",
            prioridad=prioridad,
            user_id=user_id,
            fecha_creacion=date.today(),
        )
        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)

        return TaskResponse(...)
```

**Verificamos → SIGUE PASANDO ✅** (refactoring exitoso)

### Refactoring #2: Extraer Repositorio (DIP)

```python
# repositories/task_repository.py
class TaskRepository:
    """
    DIP: El servicio depende de esta abstracción, no de SQLAlchemy directamente.
    Esto permite cambiar la DB (SQLite → PostgreSQL) sin tocar el servicio.

    NOTA EDUCATIVA:
    Si mañana quieres cambiar de SQLAlchemy a MongoDB,
    solo creas un MongoTaskRepository que cumpla el mismo contrato.
    El servicio no se entera del cambio.
    """

    def __init__(self, db_session):
        self._db = db_session

    def save(self, task: Task) -> Task:
        """Persiste una tarea y retorna con ID asignado."""
        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)
        return task

    def find_by_id(self, task_id: int) -> Optional[Task]:
        """Busca tarea por ID."""
        return self._db.query(Task).filter(Task.id == task_id).first()

    def find_by_user(self, user_id: int) -> List[Task]:
        """Lista todas las tareas de un usuario."""
        return self._db.query(Task).filter(Task.user_id == user_id).all()


# services/task_service.py (versión final refactorizada)
class TaskService:
    """
    Versión final aplicando SOLID:
    - SRP: Solo coordina (no valida ni persiste directamente)
    - OCP: Agregar validaciones = agregar al Validator, no tocar esto
    - DIP: Depende de abstracciones (Validator, Repository)
    """

    def __init__(
        self,
        repository: TaskRepository,
        validator: TaskValidator,
    ):
        self._repository = repository
        self._validator = validator

    def create_task(self, titulo, user_id, descripcion="", prioridad="media"):
        if not user_id:
            raise PermissionError("Se requiere autenticación")

        titulo_limpio = self._validator.validate_title(titulo)

        task = Task(
            titulo=titulo_limpio,
            descripcion=descripcion,
            estado="pendiente",
            prioridad=prioridad,
            user_id=user_id,
            fecha_creacion=date.today(),
        )

        return self._repository.save(task)
```

### Tabla de Refactorings Aplicados

| Antes | Después | Principio | Beneficio |
|-------|---------|-----------|-----------|
| Validación dentro del servicio | `TaskValidator` separado | SRP | Puedes testear validación sin DB |
| `self._db.add()` en el servicio | `TaskRepository.save()` | DIP | Puedes cambiar DB sin tocar servicio |
| Strings hardcoded ("pendiente") | Constantes/Enum | OCP | Agregar estados sin buscar strings |
| Todo en un archivo | Módulos separados | SRP, ISP | Cada archivo tiene un propósito claro |

### La Regla de Oro del Refactoring

> **Si después del refactoring los tests SIGUEN PASANDO sin modificarlos,
> el refactoring fue exitoso.**
>
> Si tuviste que cambiar tests, probablemente cambiaste COMPORTAMIENTO
> (no solo estructura), y eso ya no es refactoring.

---

## 8. Patrones de Testing

### Patrón AAA: Arrange-Act-Assert

```python
def test_example():
    # ARRANGE — Preparar el escenario (Given)
    service = TaskService(db=fake_db, validator=TaskValidator())
    titulo = "Mi tarea de prueba"

    # ACT — Ejecutar la acción (When)
    result = service.create_task(titulo=titulo, user_id=1)

    # ASSERT — Verificar resultado (Then)
    assert result.titulo == titulo
    assert result.estado == "pendiente"
```

### Patrón: Test Fixtures con pytest

```python
# conftest.py — Fixtures compartidas entre tests
import pytest

@pytest.fixture
def test_db():
    """
    Crea base de datos de test fresca para cada test.

    NOTA EDUCATIVA:
    Los fixtures de pytest son funciones que preparan el entorno.
    Usando 'yield', el código DESPUÉS limpia todo al final.
    """
    db = create_test_database()
    yield db
    db.rollback()
    db.close()


@pytest.fixture
def task_service(test_db):
    """Servicio de tareas listo para usar en tests."""
    return TaskService(
        repository=TaskRepository(test_db),
        validator=TaskValidator(),
    )


@pytest.fixture
def authenticated_user(test_db):
    """Un usuario registrado y autenticado."""
    from examples.taskflow.api.services.auth_service import AuthService
    service = AuthService(db=test_db)
    service.register(nombre="Test User", email="test@test.com", password="Valid$123")
    return {"id": 1, "nombre": "Test User", "email": "test@test.com"}


# Uso en tests — mucho más limpio:
class TestWithFixtures:
    def test_create_task(self, task_service, authenticated_user):
        result = task_service.create_task(
            titulo="Mi tarea",
            user_id=authenticated_user["id"]
        )
        assert result.titulo == "Mi tarea"
```

### Patrón: Parametrize (múltiples casos en un test)

```python
@pytest.mark.parametrize("titulo_invalido,error_esperado", [
    ("", "título es obligatorio"),
    ("  ", "título es obligatorio"),
    ("AB", "al menos 3"),
    ("A" * 201, "no puede exceder 200"),
    (None, "título es obligatorio"),
])
def test_create_task_invalid_titles(task_service, titulo_invalido, error_esperado):
    """
    NOTA EDUCATIVA:
    @parametrize ejecuta el MISMO test con DIFERENTES datos.
    En lugar de 5 tests casi idénticos, tienes 1 test con 5 casos.
    Esto es DRY aplicado a testing.
    """
    with pytest.raises(ValueError) as exc_info:
        task_service.create_task(titulo=titulo_invalido, user_id=1)
    assert error_esperado in str(exc_info.value).lower()
```

### Patrón: Mocking (simular dependencias externas)

```python
from unittest.mock import Mock, patch

def test_create_task_calls_repository_save(self):
    """
    NOTA EDUCATIVA:
    Un Mock es un 'doble' que simula un objeto real.
    Útil cuando no quieres llamar a la DB real en un test unitario.
    El test verifica que se LLAMÓ al método, no que la DB funcione.
    """
    # Arrange
    mock_repo = Mock(spec=TaskRepository)
    mock_repo.save.return_value = Task(id=1, titulo="Test", estado="pendiente")

    service = TaskService(repository=mock_repo, validator=TaskValidator())

    # Act
    service.create_task(titulo="Test", user_id=1)

    # Assert — verificamos que se LLAMÓ a save()
    mock_repo.save.assert_called_once()
    saved_task = mock_repo.save.call_args[0][0]
    assert saved_task.titulo == "Test"
```

---

## 9. TDD y la IA Asistida

### El Flujo con IA (Vibe Coding + TDD)

```
┌──────────────────────────────────────────────────────────────────┐
│                 TDD CON IA ASISTIDA                                │
│                                                                    │
│  TÚ escribes:              LA IA genera:         TÚ verificas:    │
│                                                                    │
│  ┌──────────────┐         ┌──────────────┐     ┌──────────────┐  │
│  │ Escenario BDD│────────▶│ Test (RED)   │────▶│ ¿Tiene       │  │
│  │ (qué quiero) │         │              │     │  sentido?    │  │
│  └──────────────┘         └──────────────┘     └──────┬───────┘  │
│                                                         │          │
│                            ┌──────────────┐            │          │
│  TÚ validas:             │ Código(GREEN)│◀───────────┘          │
│                            │              │                       │
│  ┌──────────────┐         └──────┬───────┘                       │
│  │ ¿Tests pasan?│◀───────────────┘                               │
│  │ ¿Es correcto?│                                                 │
│  └──────┬───────┘                                                 │
│         │                                                          │
│         ▼                                                          │
│  ┌──────────────┐         ┌──────────────┐                       │
│  │ Pide REFACTOR│────────▶│ Código limpio│                       │
│  │ a la IA      │         │ (SOLID)      │                       │
│  └──────────────┘         └──────────────┘                       │
│                                                                    │
└──────────────────────────────────────────────────────────────────┘
```

### ¿Por qué TDD es MEJOR con IA que sin ella?

| Sin IA | Con IA + TDD |
|--------|-------------|
| TÚ escribes test + código (más lento) | TÚ escribes test, IA genera código |
| El test puede ser incompleto | IA sugiere edge cases que no pensaste |
| Refactoring manual | IA refactoriza aplicando SOLID automáticamente |
| Cobertura depende de tu disciplina | IA puede generar tests hasta llegar al 80% |

### Prompt Efectivo para TDD con IA

```markdown
## Prompt para generar tests (RED):
"Dado este escenario BDD:
[pegar escenario Gherkin]

Genera tests unitarios en pytest que:
1. Usen patrón Arrange-Act-Assert
2. Cubran happy path y edge cases
3. Incluyan boundary tests
4. Sigan principio FIRST
Los tests DEBEN FALLAR porque el código aún no existe."

## Prompt para implementar (GREEN):
"Estos tests están fallando:
[pegar tests]

Implementa el código MÍNIMO que los haga pasar.
- No optimices aún
- No agregues funcionalidad extra
- Solo lo necesario para que pytest pase"

## Prompt para refactorizar (REFACTOR):
"Este código pasa todos los tests:
[pegar código GREEN]

Refactoriza aplicando SOLID:
- SRP: ¿Hay métodos con más de una responsabilidad?
- DIP: ¿Hay dependencias hardcoded?
- OCP: ¿Hay if/elif que deberían ser polimorfismo?
Los tests NO deben modificarse y DEBEN seguir pasando."
```

### Lo que TDD le da a la IA

> Cuando le das tests a la IA, le estás dando:
> - **Especificación exacta** de qué debe hacer el código
> - **Criterio de éxito** verificable (pasa o no pasa)
> - **Restricciones claras** (qué errores lanzar, qué retornar)
>
> Es mucho más preciso que decir "haz una función para crear tareas".

---


## 10. Ejercicios Prácticos

### Ejercicio 1: Tu Primer Ciclo TDD (15 min) 🌱

**Nivel**: Principiante
**Contexto**: Vamos a implementar una calculadora de propinas.

**Instrucciones**:

1. **RED**: Escribe estos tests (SÍ, antes del código):

```python
def test_propina_15_porciento():
    assert calcular_propina(100, 15) == 15.0

def test_propina_20_porciento():
    assert calcular_propina(80, 20) == 16.0

def test_cuenta_cero_retorna_cero():
    assert calcular_propina(0, 15) == 0.0

def test_porcentaje_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_propina(100, -5)
```

2. **GREEN**: Implementa `calcular_propina(cuenta, porcentaje)` mínima
3. **REFACTOR**: Agrega type hints y docstring

**Pregunta de reflexión**: ¿Qué test te faltó? (Pista: ¿qué pasa con una cuenta negativa?)

---

### Ejercicio 2: TDD desde BDD (20 min) 👥

**Nivel**: Principiante-Intermedio
**Contexto**: Convierte este escenario BDD en tests unitarios.

**Se te da el escenario**:

```gherkin
Feature: Cálculo de Descuentos
  Como tienda online
  Quiero aplicar descuentos automáticamente
  Para incentivar compras mayores

  Scenario: Compra mayor a $100 tiene 10% de descuento
    Given un carrito con total de $150
    When aplico los descuentos
    Then el total con descuento es $135

  Scenario: Compra menor a $100 no tiene descuento
    Given un carrito con total de $80
    When aplico los descuentos
    Then el total con descuento es $80

  Scenario: Compra exactamente $100 tiene descuento
    Given un carrito con total de $100
    When aplico los descuentos
    Then el total con descuento es $90
```

**Tu trabajo**:
1. Escribe los tests unitarios derivados (mínimo 5 tests)
2. Implementa el código mínimo (GREEN)
3. Identifica qué principio SOLID aplicarías en refactor

---

### Ejercicio 3: Red-Green-Refactor con Validación (30 min) 🔧

**Nivel**: Intermedio
**Contexto**: Sistema de validación de emails para TaskFlow.

**Requisitos** (de la sesión Three Amigos):
- Formato válido: tiene @ y dominio con punto
- No permite espacios
- Máximo 254 caracteres (estándar RFC)
- No permite dominios desechables (mailinator, tempmail)

**Tu trabajo**:
1. Escribe 8+ tests que cubran todos los requisitos
2. Implementa un `EmailValidator` mínimo
3. Refactoriza separando: formato, longitud, dominio prohibido (SRP)

**Plantilla**:
```python
class TestEmailValidator:
    def test_valid_email_passes(self):
        ...
    def test_no_arroba_fails(self):
        ...
    def test_spaces_fail(self):
        ...
    def test_too_long_fails(self):
        ...
    def test_disposable_domain_fails(self):
        ...
    # Agrega más...
```

---

### Ejercicio 4: TDD para tu Profesión (30 min) 🎯

**Nivel**: Intermedio-Avanzado
**Contexto**: Aplica TDD a un problema de TU área profesional.

| Si eres... | Función a implementar con TDD |
|-----------|-------------------------------|
| Abogado | `calcular_honorarios(horas, tipo_caso, urgencia)` |
| Economista | `calcular_roi(inversion, retorno, periodo_meses)` |
| Gastrónomo | `ajustar_receta(porciones_original, porciones_deseadas, ingredientes)` |
| Empresario | `calcular_punto_equilibrio(costos_fijos, precio_venta, costo_variable)` |
| Educador | `calcular_nota_final(parciales, pesos, asistencia_bonus)` |

**Instrucciones**:
1. Escribe 5+ tests ANTES de implementar
2. Incluye: happy path, validaciones, boundary tests
3. Implementa el código mínimo
4. Refactoriza aplicando al menos 1 principio SOLID

---

### Ejercicio 5: TDD con Mocking (30 min) 🧪

**Nivel**: Avanzado
**Contexto**: Test de un servicio que depende de API externa.

```python
# El servicio que debes testear:
class WeatherService:
    def __init__(self, api_client):
        self._api = api_client

    def should_water_plants(self, city: str) -> bool:
        """Retorna True si no va a llover en las próximas 24h."""
        forecast = self._api.get_forecast(city, hours=24)
        return not any(h["rain_probability"] > 50 for h in forecast)
```

**Tu trabajo**:
1. Crea un Mock del `api_client`
2. Escribe tests para:
   - Cuando NO va a llover → True (regar)
   - Cuando SÍ va a llover → False (no regar)
   - Cuando la API falla → manejo de error
   - Cuando la probabilidad es exactamente 50% → boundary
3. NO llames a una API real (usa Mocks)

---

### Ejercicio 6: Ciclo Completo con IA (45 min) 🚀

**Nivel**: Avanzado
**Contexto**: Usa tu IA favorita para completar un ciclo TDD real.

**Instrucciones**:

1. Escribe un **escenario BDD** para una nueva funcionalidad de TaskFlow
   (ej: "asignar tarea a otro usuario", "agregar comentario a tarea")

2. **Pide a la IA** que genere tests unitarios derivados del escenario
   - Revisa: ¿son tests F.I.R.S.T.? ¿Cubren edge cases?

3. **Pide a la IA** que implemente el código GREEN
   - Revisa: ¿es realmente mínimo? ¿No agregó cosas extra?

4. **Pide a la IA** que refactorice aplicando SOLID
   - Revisa: ¿los tests SIGUEN pasando sin modificarse?

5. **Documenta** tu experiencia:
   - ¿La IA generó buenos tests o tuviste que corregir?
   - ¿El código GREEN era realmente mínimo?
   - ¿El refactoring mejoró el diseño?
   - ¿Qué aprendiste sobre guiar a la IA con tests?

---

## 11. Errores Comunes

### Error 1: Escribir código antes del test

```python
# ❌ MAL — "Ya sé qué necesito, escribo el código y luego le pongo tests"
class UserService:
    def register(self, name, email, password):
        # 100 líneas de código...
        pass

# Tests escritos DESPUÉS (vicio: adaptan el test al código, no al revés)
def test_register():
    # Este test solo verifica lo que YA EXISTE, no guía el diseño
    ...

# ✅ BIEN — Test primero, siempre
def test_register_creates_user():
    """Escribo esto ANTES de que UserService exista."""
    service = UserService(db=test_db)
    result = service.register(name="Ana", email="ana@test.com", password="Valid$123")
    assert result.id is not None  # Esto define el CONTRATO
```

**Regla**: Si el test pasa la primera vez que lo ejecutas, NO es TDD.

### Error 2: Tests que testean la implementación, no el comportamiento

```python
# ❌ MAL — Testea CÓMO funciona internamente
def test_uses_bcrypt_to_hash():
    service = AuthService(db=test_db)
    service.register(name="Ana", email="ana@test.com", password="123")
    user = db.query(User).first()
    assert user.password.startswith("$2b$")  # Detalle de bcrypt

# ✅ BIEN — Testea QUÉ hace (comportamiento)
def test_password_is_not_stored_in_plain_text():
    service = AuthService(db=test_db)
    service.register(name="Ana", email="ana@test.com", password="MiClave123")
    user = db.query(User).first()
    assert user.password_hash != "MiClave123"  # No importa CÓMO hashea
```

**Regla**: Si cambias la implementación (ej: de bcrypt a argon2) y el test se rompe, estás testeando implementación.

### Error 3: Tests demasiado grandes (God Tests)

```python
# ❌ MAL — Un test que verifica 10 cosas
def test_everything_about_task_creation():
    service = TaskService(...)
    result = service.create_task("Test", user_id=1)
    assert result.id > 0
    assert result.titulo == "Test"
    assert result.estado == "pendiente"
    assert result.prioridad == "media"
    assert result.fecha_creacion == date.today()
    assert result.user_id == 1
    # Si falla, ¿CUÁL de las 6 verificaciones falló?

# ✅ BIEN — Tests enfocados (uno o dos asserts)
def test_create_task_assigns_id(self, task_service):
    result = task_service.create_task("Test", user_id=1)
    assert result.id > 0

def test_create_task_default_status(self, task_service):
    result = task_service.create_task("Test", user_id=1)
    assert result.estado == "pendiente"
```

**Regla**: Un test debería tener 1-2 `assert` sobre un aspecto específico.

### Error 4: Saltar el paso REFACTOR

```python
# ❌ MAL — "Ya pasa, a lo que sigue"
# Resultado: código espagueti que "funciona" pero es imposible de mantener

# ✅ BIEN — Después de GREEN, siempre preguntarse:
# 1. ¿Este método hace más de una cosa? → Extraer
# 2. ¿Hay duplicación? → Abstraer
# 3. ¿Los nombres son claros? → Renombrar
# 4. ¿Puedo testear cada parte independiente? → Separar
```

**Regla**: GREEN te da permiso de avanzar. REFACTOR te da permiso de mantener velocidad mañana.

### Error 5: Tests que dependen del orden de ejecución

```python
# ❌ MAL — test_2 asume que test_1 ya creó el usuario
def test_1_create_user():
    service.register("Ana", "ana@test.com", "Pass$123")

def test_2_login_user():
    result = service.login("ana@test.com", "Pass$123")  # ¿Y si test_1 no corrió?
    assert "token" in result

# ✅ BIEN — Cada test crea su propio estado
def test_login_with_registered_user():
    service.register("Ana", "ana@test.com", "Pass$123")  # Setup propio
    result = service.login("ana@test.com", "Pass$123")
    assert "token" in result
```

**Regla**: Cada test debe funcionar si lo ejecutas SOLO, en cualquier orden.

---

## 12. Referencias

### Libros Fundamentales

| Libro | Autor | Lo que Aporta |
|-------|-------|---------------|
| *Test-Driven Development: By Example* | Kent Beck | El libro original de TDD |
| *Clean Code* | Robert C. Martin | Código limpio + SOLID |
| *Refactoring* | Martin Fowler | Catálogo de refactorings |
| *Working Effectively with Legacy Code* | Michael Feathers | TDD en código existente |
| *The Art of Unit Testing* | Roy Osherove | Testing práctico profundo |

### Herramientas

| Herramienta | Uso | Instalación |
|-------------|-----|-------------|
| **pytest** | Framework de testing para Python | `pip install pytest` |
| **pytest-cov** | Cobertura de código | `pip install pytest-cov` |
| **pytest-mock** | Mocking integrado | `pip install pytest-mock` |
| **hypothesis** | Property-based testing | `pip install hypothesis` |
| **mutmut** | Mutation testing | `pip install mutmut` |

### Comandos Útiles de pytest

```bash
# Ejecutar todos los tests
pytest

# Con detalles (verbose)
pytest -v

# Solo tests que fallaron la última vez
pytest --lf

# Con cobertura
pytest --cov=examples/taskflow --cov-report=html

# Un solo test
pytest tests/unit/test_task_service.py::TestCreateTask::test_create_task_with_valid_title

# Tests que contienen "auth" en el nombre
pytest -k "auth"

# Parar al primer fallo
pytest -x

# Mostrar prints (no capturar output)
pytest -s
```

### Métricas de Calidad de Tests (ISO 25023)

| Métrica | Qué mide | Meta |
|---------|----------|------|
| **Cobertura de líneas** | % de líneas ejecutadas por tests | ≥ 80% |
| **Cobertura de ramas** | % de if/else cubiertos | ≥ 70% |
| **Mutation score** | % de mutantes detectados | ≥ 60% |
| **Test execution time** | Tiempo total de la suite | < 30s |
| **Flakiness rate** | % tests que fallan intermitentemente | 0% |

---

## Control de Cambios

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0.0 | 2026-08-03 | Versión inicial completa del recurso formativo |

---

> **Este documento es un recurso académico para el taller de Desarrollo Asistido por IA.**
> Está diseñado para usarse DESPUÉS de la guía BDD, ya que TDD se alimenta
> de los escenarios definidos en BDD.
>
> Flujo recomendado del taller:
> 1. BDD (entender QUÉ) → 2. TDD (implementar CÓMO) → 3. SOLID (mejorar) → 4. Seguridad (proteger)
>
> Los archivos de tests y código están en:
> - `tests/unit/` — Tests unitarios (RED)
> - `examples/taskflow/api/services/` — Implementación (GREEN)
> - `examples/taskflow/api/validators/` — Validadores extraídos (REFACTOR)
