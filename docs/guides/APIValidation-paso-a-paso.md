# Guía API Validation Paso a Paso
## Resiliencia de APIs — Evitar Saturación, Bloqueo y Costos Descontrolados

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0.0 |
| **Fecha** | 2026-08-03 |
| **Público** | Profesionales multidisciplinarios (universitario+) |
| **Prerrequisitos** | Haber completado BDD, TDD, SOLID, OWASP, ISO 25010, Stress |
| **Duración estimada** | 3-4 horas (taller completo) |
| **Proyecto ejemplo** | TaskFlow — patrones de resiliencia implementados |

---

## Tabla de Contenidos

1. [¿Qué es API Validation?](#1-qué-es-api-validation)
2. [¿Por qué necesitas resiliencia?](#2-por-qué-necesitas-resiliencia)
3. [Los 3 Problemas Mortales](#3-los-3-problemas-mortales)
4. [Patrón 1: Rate Limiting](#4-patrón-1-rate-limiting)
5. [Patrón 2: Circuit Breaker](#5-patrón-2-circuit-breaker)
6. [Patrón 3: Retry con Backoff](#6-patrón-3-retry-con-backoff)
7. [Patrón 4: Timeout](#7-patrón-4-timeout)
8. [Patrón 5: Bulkhead (Aislamiento)](#8-patrón-5-bulkhead-aislamiento)
9. [Presupuesto y Control de Costos](#9-presupuesto-y-control-de-costos)
10. [Implementación en TaskFlow](#10-implementación-en-taskflow)
11. [Ejercicios Prácticos](#11-ejercicios-prácticos)
12. [Referencias](#12-referencias)

---

## 1. ¿Qué es API Validation?

### Definición Simple

> **API Validation es el conjunto de controles que evitan que tu sistema
> sature, bloquee o gaste de más al comunicarse con servicios externos.**

Es como un "regulador" entre tu aplicación y el mundo exterior.


### Definición Técnica

API Validation (o API Resilience) engloba patrones de diseño que:

1. **Rate Limiting**: Controla cuántos requests envías por unidad de tiempo
2. **Circuit Breaker**: Corta la comunicación si el servicio está fallando
3. **Retry con Backoff**: Reintenta con espera creciente ante fallos transitorios
4. **Timeout**: Establece un tiempo máximo de espera por respuesta
5. **Bulkhead**: Aísla fallos para que no se propagen
6. **Budget Control**: Limita el gasto diario/mensual en APIs de pago

### Metáfora: El Sistema Eléctrico de tu Casa ⚡

```
┌──────────────────────────────────────────────────────────────┐
│                                                                │
│  TU SISTEMA = CASA       APIS EXTERNAS = RED ELÉCTRICA        │
│                                                                │
│  Rate Limiting    = Fusibles (limitan amperaje)               │
│  Circuit Breaker  = Interruptor diferencial (corta si hay fallo)│
│  Retry + Backoff  = Reconectador automático (espera y reintenta)│
│  Timeout          = Temporizador (si tarda mucho, corta)       │
│  Bulkhead         = Circuitos separados (cocina ≠ habitaciones)│
│  Budget           = Medidor prepago (se acaba el saldo, corta) │
│                                                                │
│  Sin estos controles: un cortocircuito en la cocina            │
│  te deja SIN LUZ en TODA la casa.                              │
│                                                                │
│  Con estos controles: se va la luz SOLO en la cocina,          │
│  el resto sigue funcionando.                                   │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. ¿Por qué necesitas resiliencia?

### El Contexto: IA Asistida = APIs Externas

En el desarrollo con IA (vibe coding), dependes de APIs externas:
- OpenAI / Claude / Gemini (LLMs)
- APIs de análisis (bandit, semgrep cloud)
- Bases de datos remotas
- Servicios de terceros

### ¿Qué pasa SIN controles?

| Situación | Sin controles | Con controles |
|-----------|---------------|---------------|
| API rate-limited | 🔴 Te bloquean por horas/días | ✅ Auto-limitas antes del bloqueo |
| API caída (500) | 🔴 Tu app se congela esperando | ✅ Circuit breaker corta, modo degradado |
| API lenta (timeout) | 🔴 Usuarios esperan 30+ segundos | ✅ Timeout a 5s + retry |
| API cara (GPT-4) | 🔴 Factura de $500 en un bug loop | ✅ Budget max $10/día → pausa |
| Pico de tráfico | 🔴 Mandas 1000 req/s → bloqueo | ✅ Rate limiter suaviza a 60 req/min |

### Para Cada Perfil

| Perfil | Riesgo sin resiliencia | Ejemplo |
|--------|----------------------|---------|
| **Empresario** | Factura de API de $5,000 por un bug | Loop infinito llamando GPT-4 |
| **Abogado** | Sistema de consultas se cae en audiencia | API del juzgado offline |
| **Economista** | Reportes no se generan por API saturada | Bloomberg API rate limited |
| **Gastrónomo** | Pedidos se pierden porque la pasarela falló | Stripe timeout en hora pico |
| **Educador** | Plataforma muerta en examen final | API de videoconferencia colapsada |

---

## 3. Los 3 Problemas Mortales

### Problema 1: Saturación (Rate Limit Exceeded)

```
TU APP:  "Dame datos, dame datos, dame datos, dame datos..."
API:     "¡BASTA! Bloqueado por 1 hora." 🚫

Resultado: Tu app no puede hacer NADA por 1 hora.
Los usuarios ven: "Servicio no disponible"
```

### Problema 2: Cascada de Fallos (Cascade Failure)

```
API externa falla
     │
     ▼
Tu servicio A espera... espera... timeout (30s)
     │
     ▼
Servicio B que depende de A... espera... timeout
     │
     ▼
Servicio C que depende de B... espera... timeout
     │
     ▼
TODO EL SISTEMA CONGELADO 🧊

"Un fallo en un servicio externo tumba toda tu aplicación"
```

### Problema 3: Costos Descontrolados (Budget Explosion)

```
Bug: Loop que llama a OpenAI cada 100ms

Sin budget control:
  10 req/s × $0.03/req × 3600s = $1,080 por hora 💸

Con budget control ($10/día):
  Después de 333 requests → PAUSA automática
  Gasto máximo: $10 ✅
```

---


## 4. Patrón 1: Rate Limiting

### ¿Qué es?

> **Rate Limiting = controlar cuántos requests envías por minuto/segundo
> para NO ser bloqueado por la API destino.**

### Metáfora: El Grifo de Agua 🚰

- Sin rate limiting: abres el grifo al máximo → la tubería revienta
- Con rate limiting: abres moderado → flujo constante y sostenible

### Algoritmo: Token Bucket

```
┌──────────────────────────────────────────────────────────────┐
│              TOKEN BUCKET — Cómo Funciona                      │
│                                                                │
│  Imagina un balde con fichas:                                  │
│                                                                │
│  • El balde tiene capacidad máxima (ej: 60 fichas)            │
│  • Cada segundo se AGREGA 1 ficha (tasa de recarga)           │
│  • Cada request CONSUME 1 ficha                                │
│  • Si no hay fichas → ESPERAR hasta que se recargue           │
│                                                                │
│  ┌─────────┐                                                   │
│  │ 🪙🪙🪙🪙 │ ← Fichas disponibles (tokens)                    │
│  │ 🪙🪙🪙  │                                                   │
│  │ 🪙🪙    │ ← Se van consumiendo con cada request             │
│  │ 🪙      │                                                   │
│  └─────────┘                                                   │
│       ↑                                                        │
│       │ +1 ficha/segundo (recarga constante)                   │
│                                                                │
│  Resultado: Máximo 60 requests/minuto sostenidos               │
│             Permite ráfagas cortas (usa fichas acumuladas)      │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

### Implementación Python

```python
import asyncio
import time


class TokenBucketRateLimiter:
    """
    Rate Limiter con algoritmo Token Bucket.

    NOTA EDUCATIVA:
    Este es el MISMO algoritmo que las APIs usan para limitarte.
    Aquí lo usamos para AUTO-limitarnos y no ser bloqueados.

    Ventajas vs. simple contador:
    - Permite ráfagas cortas (si hay tokens acumulados)
    - Suaviza el tráfico (no envía todo de golpe)
    - Es el estándar de la industria
    """

    def __init__(self, rate: float, capacity: int):
        """
        Args:
            rate: Tokens que se agregan por segundo (ej: 1.0 = 60/min)
            capacity: Máximo de tokens acumulados (tamaño del balde)
        """
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity  # Empieza lleno
        self.last_refill = time.monotonic()

    def _refill(self):
        """Agrega tokens según el tiempo transcurrido."""
        now = time.monotonic()
        elapsed = now - self.last_refill
        new_tokens = elapsed * self.rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill = now

    async def acquire(self, tokens: int = 1) -> float:
        """
        Adquiere tokens. Si no hay suficientes, ESPERA.

        Returns:
            Tiempo que tuvo que esperar (0.0 si no esperó)
        """
        self._refill()

        if self.tokens >= tokens:
            self.tokens -= tokens
            return 0.0  # Sin espera

        # Calcular cuánto esperar
        deficit = tokens - self.tokens
        wait_time = deficit / self.rate

        await asyncio.sleep(wait_time)
        self._refill()
        self.tokens -= tokens
        return wait_time

    @property
    def available(self) -> float:
        """Tokens disponibles ahora."""
        self._refill()
        return self.tokens
```

### Uso Práctico

```python
# Configurar: máximo 60 requests por minuto
limiter = TokenBucketRateLimiter(rate=1.0, capacity=60)

async def call_external_api(data):
    """Llama a API externa respetando el rate limit."""
    wait = await limiter.acquire()
    if wait > 0:
        print(f"⏳ Rate limited: esperé {wait:.1f}s")

    # Ahora sí, hacer el request
    response = await httpx.get("https://api.externa.com/data")
    return response.json()
```

---

## 5. Patrón 2: Circuit Breaker

### ¿Qué es?

> **Circuit Breaker = si la API externa falla repetidamente,
> deja de intentar durante un tiempo (para no empeorar las cosas).**

### Metáfora: El Interruptor Diferencial ⚡

Cuando hay un cortocircuito, el interruptor CORTA la electricidad
automáticamente para que no se queme la casa.
Después de un tiempo, puedes volver a subirlo (probar si se arregló).

### Estados del Circuit Breaker

```
                    ┌─────────────────────────────────────────┐
                    │                                           │
                    ▼                                           │
            ┌──────────────┐     fallo #N          ┌──────────┴───┐
  start ──▶ │   CLOSED     │ ────────────────────▶ │    OPEN       │
            │ (funcionando) │                       │ (cortado)     │
            │               │                       │               │
            │ Deja pasar    │                       │ RECHAZA todo  │
            │ requests      │                       │ inmediatamente│
            └──────┬───────┘                       └──────┬────────┘
                   ▲                                       │
                   │                                       │ timeout
                   │                                       ▼
                   │         éxito            ┌────────────────────┐
                   └──────────────────────────│    HALF-OPEN       │
                                              │ (probando)         │
                                              │                    │
                                              │ Deja pasar UNO     │
                                              │ para ver si ya     │
                                              │ funciona           │
                                              └────────────────────┘
                                                       │
                                                       │ fallo
                                                       ▼
                                                   Vuelve a OPEN
```

### Implementación Python

```python
import time
from enum import Enum
from typing import Optional


class CircuitState(Enum):
    CLOSED = "closed"      # Funcionando normal
    OPEN = "open"          # Cortado (rechaza todo)
    HALF_OPEN = "half_open"  # Probando si se recuperó


class CircuitBreaker:
    """
    Circuit Breaker — Protege contra APIs fallidas.

    NOTA EDUCATIVA:
    Sin circuit breaker, tu app se queda "colgada" esperando
    una API que no va a responder. Con circuit breaker:
    - Falla RÁPIDO (no esperas 30s por cada request)
    - Da tiempo a la API de recuperarse
    - Tu app puede funcionar en modo degradado

    Configuración típica:
    - failure_threshold=5: 5 fallos consecutivos → OPEN
    - recovery_timeout=30: esperar 30s antes de reintentar
    - success_threshold=3: 3 éxitos en HALF_OPEN → CLOSED
    """

    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
        success_threshold: int = 3,
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time: Optional[float] = None

    def can_execute(self) -> bool:
        """¿Se puede hacer un request?"""
        if self.state == CircuitState.CLOSED:
            return True

        if self.state == CircuitState.OPEN:
            # ¿Ya pasó el tiempo de recovery?
            if time.monotonic() - self.last_failure_time >= self.recovery_timeout:
                self.state = CircuitState.HALF_OPEN
                self.success_count = 0
                return True  # Permitir un intento de prueba
            return False  # Aún cortado

        # HALF_OPEN: permitir
        return True

    def record_success(self):
        """Registra un request exitoso."""
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                # ¡Se recuperó! Volver a CLOSED
                self.state = CircuitState.CLOSED
                self.failure_count = 0
        else:
            self.failure_count = 0  # Reset en CLOSED

    def record_failure(self):
        """Registra un request fallido."""
        self.failure_count += 1
        self.last_failure_time = time.monotonic()

        if self.state == CircuitState.HALF_OPEN:
            # Falló en prueba → volver a OPEN
            self.state = CircuitState.OPEN

        elif self.failure_count >= self.failure_threshold:
            # Muchos fallos → abrir circuito
            self.state = CircuitState.OPEN

    @property
    def is_open(self) -> bool:
        return self.state == CircuitState.OPEN
```

---

## 6. Patrón 3: Retry con Backoff

### ¿Qué es?

> **Retry con Backoff = si un request falla, reintenta pero esperando
> cada vez MÁS tiempo entre intentos.**

### ¿Por qué NO reintentar inmediatamente?

```
Sin backoff (retry inmediato):
  Intento 1: falla (API sobrecargada)
  Intento 2: falla (API aún más sobrecargada por tu retry)
  Intento 3: falla (la estás empeorando)
  ...
  → Efecto "thundering herd": todos reintentan a la vez → colapso

Con exponential backoff + jitter:
  Intento 1: falla → esperar 1s
  Intento 2: falla → esperar 2s + random(0-0.2s)
  Intento 3: falla → esperar 4s + random(0-0.4s)
  Intento 4: ¡éxito! (la API tuvo tiempo de recuperarse)
```

### Implementación Python

```python
import asyncio
import random


class RetryPolicy:
    """
    Retry con Exponential Backoff + Jitter.

    NOTA EDUCATIVA:
    - "Exponential": cada retry espera el DOBLE que el anterior
    - "Jitter": se agrega una aleatorización para que no todos
      los clientes reintenten al MISMO tiempo
    - "Max retries": un límite para no reintentar infinitamente
    """

    def __init__(
        self,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        exponential_base: float = 2.0,
        jitter_factor: float = 0.1,
    ):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        self.jitter_factor = jitter_factor

    def calculate_delay(self, attempt: int) -> float:
        """
        Calcula el tiempo de espera para el intento N.

        Ejemplo con defaults:
          attempt 0: 1.0s + jitter
          attempt 1: 2.0s + jitter
          attempt 2: 4.0s + jitter
          attempt 3: 8.0s + jitter (capped a max_delay)
        """
        delay = self.base_delay * (self.exponential_base ** attempt)
        delay = min(delay, self.max_delay)
        jitter = random.uniform(0, delay * self.jitter_factor)
        return delay + jitter

    async def execute_with_retry(self, func, *args, **kwargs):
        """
        Ejecuta una función con reintentos automáticos.

        Returns:
            El resultado de la función si tiene éxito

        Raises:
            El último error si se agotaron los reintentos
        """
        last_error = None

        for attempt in range(self.max_retries + 1):
            try:
                result = await func(*args, **kwargs)
                return result

            except Exception as e:
                last_error = e

                if attempt == self.max_retries:
                    break  # No más reintentos

                delay = self.calculate_delay(attempt)
                print(f"⚠️ Intento {attempt+1} falló: {e}. "
                      f"Reintentando en {delay:.1f}s...")
                await asyncio.sleep(delay)

        raise last_error
```

---


## 7. Patrón 4: Timeout

### ¿Qué es?

> **Timeout = tiempo MÁXIMO que esperas una respuesta.
> Si la API no responde en X segundos, CANCELAS y sigues.**

Sin timeout, tu aplicación puede quedarse esperando PARA SIEMPRE.

### Regla de Oro

```
Timeout = 2× el tiempo NORMAL de respuesta

Si la API normalmente responde en 200ms:
  Timeout = 500ms (2.5×)

Si normalmente responde en 2s:
  Timeout = 5s

NUNCA más de 30s para una interacción de usuario.
NUNCA sin timeout (= esperar infinito).
```

### Implementación

```python
import httpx

async def call_with_timeout(url: str, timeout: float = 5.0):
    """Toda llamada externa DEBE tener timeout."""
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            response = await client.get(url)
            return response.json()
        except httpx.TimeoutException:
            # ← No esperar más. Informar y seguir.
            raise ServiceUnavailableError(
                f"API no respondió en {timeout}s. Intenta más tarde."
            )
```

---

## 8. Patrón 5: Bulkhead (Aislamiento)

### ¿Qué es?

> **Bulkhead = aislar los fallos para que el problema de UN servicio
> no tumbe a TODOS los demás.**

El nombre viene de los compartimentos estancos de un barco: si un
compartimento se inunda, los demás siguen a flote.

### Implementación: Thread Pools Separados

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Pool separado para cada servicio externo
openai_pool = ThreadPoolExecutor(max_workers=5, thread_name_prefix="openai")
analytics_pool = ThreadPoolExecutor(max_workers=3, thread_name_prefix="analytics")

# Si OpenAI se satura y agota sus 5 workers...
# ... analytics sigue funcionando con sus 3 workers independientes

async def call_openai(prompt):
    """Usa su propio pool aislado."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(openai_pool, _sync_openai_call, prompt)

async def call_analytics(data):
    """Pool independiente — no afectado por OpenAI."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(analytics_pool, _sync_analytics_call, data)
```

---

## 9. Presupuesto y Control de Costos

### ¿Por qué?

Las APIs de IA cobran POR USO. Un bug que hace un loop = factura enorme.

### Implementación

```python
from dataclasses import dataclass, field
from datetime import date
from typing import Dict


@dataclass
class BudgetController:
    """
    Controla el gasto diario en APIs de pago.

    NOTA EDUCATIVA:
    Esto evita la situación de "desperté con una factura de $500
    porque mi script tenía un loop infinito llamando a GPT-4".
    """

    daily_limit_usd: float = 10.0
    alert_threshold_usd: float = 8.0  # Alerta al 80%
    cost_per_request: Dict[str, float] = field(default_factory=lambda: {
        "gpt-4": 0.03,
        "gpt-3.5": 0.002,
        "claude": 0.015,
    })
    _daily_spend: float = 0.0
    _last_reset: date = field(default_factory=date.today)

    def can_spend(self, model: str, tokens: int = 1) -> bool:
        """¿Hay presupuesto para este request?"""
        self._check_daily_reset()
        cost = self.cost_per_request.get(model, 0.01) * tokens
        return (self._daily_spend + cost) <= self.daily_limit_usd

    def record_spend(self, model: str, tokens: int = 1):
        """Registra el gasto."""
        cost = self.cost_per_request.get(model, 0.01) * tokens
        self._daily_spend += cost

        if self._daily_spend >= self.alert_threshold_usd:
            print(f"⚠️ ALERTA: Gasto diario en {self._daily_spend:.2f}/"
                  f"{self.daily_limit_usd:.2f} USD")

    @property
    def remaining_budget(self) -> float:
        """Presupuesto restante hoy."""
        self._check_daily_reset()
        return self.daily_limit_usd - self._daily_spend

    def _check_daily_reset(self):
        """Reinicia el contador cada nuevo día."""
        today = date.today()
        if today > self._last_reset:
            self._daily_spend = 0.0
            self._last_reset = today
```

---

## 10. Implementación en TaskFlow

### Clase Unificada: ResilientAPIClient

```python
class ResilientAPIClient:
    """
    Cliente HTTP con TODOS los patrones de resiliencia integrados.

    Orden de ejecución:
    1. Budget check (¿hay presupuesto?)
    2. Rate limiter (¿hay tokens disponibles?)
    3. Circuit breaker (¿el circuito está cerrado?)
    4. Timeout (máximo X segundos de espera)
    5. Retry con backoff (si falla, reintentar)

    NOTA EDUCATIVA:
    Esta clase COMPONE todos los patrones que vimos.
    Es un ejemplo de SOLID aplicado:
    - SRP: cada patrón es una clase independiente
    - OCP: puedes agregar más patrones sin modificar los existentes
    - DIP: el cliente recibe los patrones inyectados
    """

    def __init__(
        self,
        rate_limiter: TokenBucketRateLimiter,
        circuit_breaker: CircuitBreaker,
        retry_policy: RetryPolicy,
        budget: BudgetController,
        timeout: float = 5.0,
    ):
        self._rate_limiter = rate_limiter
        self._circuit_breaker = circuit_breaker
        self._retry = retry_policy
        self._budget = budget
        self._timeout = timeout

    async def request(self, method: str, url: str, **kwargs) -> dict:
        """
        Ejecuta un request con todas las protecciones.

        Flujo:
        ┌─────────┐  ┌──────────┐  ┌─────────────┐  ┌─────────┐  ┌───────┐
        │ Budget? │→ │Rate Limit│→ │Circuit Open?│→ │ Request │→ │Retry? │
        │ ¿Hay $? │  │ ¿Token?  │  │ ¿Cortado?   │  │+Timeout │  │¿Fallo?│
        └─────────┘  └──────────┘  └─────────────┘  └─────────┘  └───────┘
        """
        # 1. Budget check
        if not self._budget.can_spend("default"):
            raise BudgetExhaustedError(
                f"Presupuesto diario agotado. Restante: ${self._budget.remaining_budget:.2f}"
            )

        # 2. Rate limiting
        wait = await self._rate_limiter.acquire()
        if wait > 0:
            pass  # Ya esperó dentro de acquire()

        # 3. Circuit breaker
        if not self._circuit_breaker.can_execute():
            raise CircuitOpenError(
                "Servicio temporalmente no disponible. "
                f"Reintentando en {self._circuit_breaker.recovery_timeout}s."
            )

        # 4. Request con timeout + 5. Retry
        async def _do_request():
            import httpx
            async with httpx.AsyncClient(timeout=self._timeout) as client:
                response = await client.request(method, url, **kwargs)
                response.raise_for_status()
                return response.json()

        try:
            result = await self._retry.execute_with_retry(_do_request)
            self._circuit_breaker.record_success()
            self._budget.record_spend("default")
            return result

        except Exception as e:
            self._circuit_breaker.record_failure()
            raise
```

### Configuración YAML (de nuestro config/default.yaml)

```yaml
api_policies:
  openai:
    requests_per_minute: 60
    failure_threshold: 3
    recovery_timeout_seconds: 60
    max_retries: 3
    base_delay_seconds: 2.0
    max_daily_cost_usd: 10.0

  local_taskflow_api:
    requests_per_minute: 1000
    failure_threshold: 10
    recovery_timeout_seconds: 5
    max_retries: 1
    base_delay_seconds: 0.5
```

---

## 11. Ejercicios Prácticos

### Ejercicio 1: Diseña tu Política de Resiliencia (15 min) 📋

**Nivel**: Principiante

Para una API que usas (ej: OpenAI, Stripe, Google Maps), define:

| Parámetro | Tu valor | ¿Por qué? |
|-----------|----------|-----------|
| Rate limit (req/min) | ___ | |
| Circuit breaker threshold | ___ fallos | |
| Recovery timeout | ___ segundos | |
| Retry attempts | ___ | |
| Timeout | ___ segundos | |
| Budget diario | $___ | |

### Ejercicio 2: Implementa un Rate Limiter (25 min) 🔧

**Nivel**: Intermedio

Implementa un `SlidingWindowRateLimiter` (alternativa al Token Bucket):
- Mantén un registro de timestamps de los últimos N requests
- Si hay más de N en la ventana de 1 minuto, bloquear
- Escribe 3 tests que verifiquen el comportamiento

### Ejercicio 3: Simula Fallos (30 min) 🧪

**Nivel**: Intermedio-Avanzado

1. Crea un "servidor falso" que falle el 50% de las veces
2. Conecta tu ResilientAPIClient
3. Verifica que:
   - El circuit breaker se ABRE después de N fallos
   - Los retries funcionan con backoff creciente
   - El circuit pasa a HALF_OPEN después del timeout
   - Se recupera cuando el servidor vuelve

### Ejercicio 4: Escenario BDD de Resiliencia (20 min) 📝

**Nivel**: Todos

Escribe escenarios Gherkin para:

```gherkin
Feature: Protección contra saturación de API
  Scenario: Rate limiting previene bloqueo
    Given ...
    When ...
    Then ...

  Scenario: Circuit breaker protege contra API caída
    Given ...
    When ...
    Then ...

  Scenario: Budget controller previene gastos excesivos
    Given ...
    When ...
    Then ...
```

---

## 12. Referencias

### Patrones de Resiliencia

| Patrón | Referencia | Implementación |
|--------|-----------|----------------|
| Circuit Breaker | Michael Nygard — *Release It!* | `agents/api_validation/` |
| Token Bucket | RFC 6585 | Rate limiter del proyecto |
| Bulkhead | *Release It!* | Thread pools separados |
| Retry + Backoff | AWS Architecture Blog | RetryPolicy class |

### Conexión con el Taller

| Módulo | Conexión con API Validation |
|--------|----------------------------|
| **BDD** | Escenarios de resiliencia en Gherkin |
| **TDD** | Tests unitarios de cada patrón |
| **SOLID** | Cada patrón es una clase (SRP), inyectada (DIP) |
| **OWASP** | A10 (SSRF) + rate limiting previene A07 |
| **ISO 25010** | Fiabilidad + Eficiencia de Desempeño |
| **Stress** | Stress testing DESCUBRE los límites, API Validation los PROTEGE |

---

## Control de Cambios

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0.0 | 2026-08-03 | Versión inicial completa |

---

> **API Validation es el "sistema inmunológico" de tu aplicación.**
> Protege contra amenazas externas (APIs caídas, saturación, costos)
> sin que el usuario lo note.
>
> Flujo del taller:
> BDD → TDD → SOLID → OWASP → ISO 25010 → Stress → **API Validation** → UX
