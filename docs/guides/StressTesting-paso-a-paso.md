# Guía Stress Testing Paso a Paso
## Pruebas de Carga y Rendimiento — ¿Cuánto Aguanta tu Sistema?

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0.0 |
| **Fecha** | 2026-08-03 |
| **Público** | Profesionales multidisciplinarios (universitario+) |
| **Prerrequisitos** | Haber completado BDD, TDD, SOLID, OWASP, ISO 25010 |
| **Duración estimada** | 3-4 horas (taller completo) |
| **Herramienta principal** | Locust (Python) |
| **Proyecto ejemplo** | TaskFlow — pruebas de carga reales |

---

## Tabla de Contenidos

1. [¿Qué es Stress Testing?](#1-qué-es-stress-testing)
2. [¿Por qué probar bajo carga?](#2-por-qué-probar-bajo-carga)
3. [Tipos de Pruebas de Rendimiento](#3-tipos-de-pruebas-de-rendimiento)
4. [Métricas Clave (ISO 25023)](#4-métricas-clave-iso-25023)
5. [Locust: La Herramienta](#5-locust-la-herramienta)
6. [Escenarios de Carga para TaskFlow](#6-escenarios-de-carga-para-taskflow)
7. [Perfiles de Usuario](#7-perfiles-de-usuario)
8. [Análisis de Resultados](#8-análisis-de-resultados)
9. [Patrones de Degradación](#9-patrones-de-degradación)
10. [Stress Testing + API Validation](#10-stress-testing--api-validation)
11. [Ejercicios Prácticos](#11-ejercicios-prácticos)
12. [Referencias](#12-referencias)

---

## 1. ¿Qué es Stress Testing?

### Definición Simple

> **Stress Testing es llevar tu sistema al LÍMITE a propósito,
> para descubrir cuándo se rompe y cómo se comporta bajo presión.**

Es como un "crash test" para software: no esperas a que choque en la
carretera — lo estrellas en el laboratorio para saber qué pasa.


### Definición Técnica

Stress Testing (pruebas de estrés) es un tipo de prueba de rendimiento que:

1. **Simula** múltiples usuarios concurrentes usando el sistema
2. **Incrementa** la carga gradualmente hasta encontrar el punto de quiebre
3. **Mide** tiempos de respuesta, errores y consumo de recursos
4. **Identifica** cuellos de botella antes de que lleguen usuarios reales

### Metáfora: El Puente y los Camiones 🌉

```
┌──────────────────────────────────────────────────────────────┐
│                                                                │
│  TU APLICACIÓN = UN PUENTE                                    │
│                                                                │
│  Stress Testing responde:                                      │
│  • ¿Cuántos camiones puede soportar a la vez?  (capacidad)    │
│  • ¿A qué velocidad pueden pasar?              (throughput)    │
│  • ¿Cuándo empieza a crujir?                   (degradación)  │
│  • ¿A cuántos colapsa?                         (punto quiebre)│
│  • ¿Se puede reparar solo después?             (recuperación)  │
│                                                                │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐                        │
│  │ 🚛 │ │ 🚛 │ │ 🚛 │ │ 🚛 │ │ 🚛 │  ← Usuarios            │
│  └────┘ └────┘ └────┘ └────┘ └────┘                        │
│  ══════════════════════════════════════  ← Tu API             │
│            ¿Cuánto aguanta?                                    │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. ¿Por qué probar bajo carga?

### El Problema: "En mi máquina funciona" 🤷

| En desarrollo (1 usuario) | En producción (1000 usuarios) |
|---------------------------|-------------------------------|
| Responde en 5ms | Responde en 15 SEGUNDOS |
| 0% errores | 30% timeouts |
| 50MB RAM | 8GB RAM → crash |
| "Todo perfecto" | "¡Se cayó el sistema!" 🔥 |

### Para Cada Perfil

| Perfil | Riesgo sin Stress Testing | Ejemplo real |
|--------|--------------------------|--------------|
| **Empresario** | Lanzas producto → se cae el primer día | Twitter se caía con cada evento viral |
| **Abogado** | Sistema de expedientes lento en hora pico | Juzgados con sistema colapsado los lunes |
| **Economista** | Reportes que tardan horas en generarse | Bloomberg terminal lento en apertura de mercado |
| **Gastrónomo** | Sistema de pedidos saturado viernes noche | Apps de delivery caen en hora de cena |
| **Educador** | Plataforma colapsa en época de exámenes | Moodle caído en semana de finales |

### El Costo de NO Hacer Stress Testing

```
Costo de downtime por industria (por hora):

  E-commerce:      $250,000/hora
  Finanzas:        $500,000/hora
  Salud:           $150,000/hora
  Educación:        $50,000/hora

  Costo de stress testing:  ~$5,000 (una vez)
  ROI: 50x-100x en la primera caída evitada
```

---

## 3. Tipos de Pruebas de Rendimiento

### Mapa de Tipos

```
┌─────────────────────────────────────────────────────────────────┐
│           TIPOS DE PRUEBAS DE RENDIMIENTO                        │
│                                                                   │
│  Carga ─────────────────────────────────────────────── Tiempo    │
│    │                                                              │
│    │   ┌───────────────┐                                         │
│    │   │  SMOKE TEST   │  Pocos usuarios, verificar que funciona │
│    │   │  (humo)       │  5-10 usuarios por 5 minutos            │
│    │   └───────────────┘                                         │
│    │                                                              │
│    │         ┌────────────────┐                                  │
│    │         │  LOAD TEST     │  Carga esperada normal           │
│    │         │  (carga)       │  50-100 usuarios por 30 min      │
│    │         └────────────────┘                                  │
│    │                                                              │
│    │               ┌─────────────────┐                           │
│    │               │  STRESS TEST    │  Más allá del límite      │
│    │               │  (estrés)       │  200+ usuarios, ver qué pasa │
│    │               └─────────────────┘                           │
│    │                                                              │
│    │                     ┌──────────────────┐                    │
│    │                     │  SPIKE TEST      │  Pico repentino    │
│    │                     │  (pico)          │  0→500 en 10 seg   │
│    │                     └──────────────────┘                    │
│    │                                                              │
│    │  ┌─────────────────────────────────────────────────┐       │
│    │  │  SOAK TEST (resistencia) — Carga media por horas │       │
│    │  │  50 usuarios por 8 horas → detectar memory leaks │       │
│    │  └─────────────────────────────────────────────────┘       │
│    ▼                                                              │
└─────────────────────────────────────────────────────────────────┘
```

### Tabla Comparativa

| Tipo | Propósito | Usuarios | Duración | Qué busca |
|------|-----------|----------|----------|-----------|
| **Smoke** | ¿Funciona básicamente? | 5-10 | 5 min | Errores graves |
| **Load** | ¿Soporta la carga normal? | 50-100 | 30 min | Latencia aceptable |
| **Stress** | ¿Dónde se rompe? | 200-500+ | 15-30 min | Punto de quiebre |
| **Spike** | ¿Sobrevive un pico repentino? | 0→500 | 1 min ramp | Recuperación |
| **Soak** | ¿Funciona por tiempo prolongado? | 50 | 4-8 horas | Memory leaks |

---

## 4. Métricas Clave (ISO 25023)

### Las 6 Métricas que Importan

| Métrica | Qué mide | Analogía | Meta TaskFlow |
|---------|----------|----------|---------------|
| **Latencia p95** | Tiempo de respuesta (95% de requests) | "¿Cuánto espera el usuario?" | ≤ 500ms |
| **Throughput (RPS)** | Requests procesados por segundo | "¿Cuántos camiones pasan?" | ≥ 100 |
| **Error Rate** | % de requests que fallan | "¿Cuántos camiones caen?" | ≤ 1% |
| **Concurrent Users** | Usuarios simultáneos soportados | "¿Cuántos caben en el puente?" | ≥ 50 |
| **Memory Usage** | RAM consumida bajo carga | "¿Se expande hasta reventar?" | ≤ 512MB |
| **Recovery Time** | Tiempo para volver a la normalidad | "¿Cuánto tarda en repararse?" | ≤ 30s |

### Percentiles Explicados

```
Si tienes 100 requests, ordenados de más rápido a más lento:

  p50 (mediana):  El request #50 — "el típico"
  p95:            El request #95 — "el caso malo (pero no el peor)"
  p99:            El request #99 — "el caso casi peor"
  max:            El request #100 — "el peor de todos"

  ¿Por qué p95 y no promedio?
  Porque el promedio ESCONDE los casos malos.

  Ejemplo:
  99 requests de 10ms + 1 request de 10,000ms
  Promedio = 109ms  ← "parece bien"
  p99 = 10,000ms   ← "¡un usuario esperó 10 SEGUNDOS!"
```

---

## 5. Locust: La Herramienta

### ¿Por qué Locust?

| Característica | Locust | Otras (JMeter, k6) |
|---------------|--------|---------------------|
| **Lenguaje** | Python puro | JMeter: XML/GUI, k6: JavaScript |
| **Curva de aprendizaje** | Baja (es código Python) | JMeter: Alta (GUI compleja) |
| **Extensibilidad** | Total (es Python) | Limitada |
| **Integración CI** | Simple (CLI) | Requiere plugins |
| **Escalabilidad** | Distribuido nativo | Requiere configuración extra |

### Instalación

```bash
pip install locust
```

### Estructura Básica de un Locustfile

```python
# locustfile.py — Un archivo de Locust tiene 3 partes:

from locust import HttpUser, task, between

class MiUsuario(HttpUser):
    """
    1. QUIÉN es el usuario simulado
    2. QUÉ acciones realiza
    3. A QUÉ ritmo las hace
    """

    # Tiempo de espera entre acciones (simula "pensar")
    wait_time = between(1, 3)  # 1-3 segundos entre cada acción

    # Las acciones que el usuario realiza
    @task(3)  # Peso 3: esta acción es 3x más frecuente
    def accion_frecuente(self):
        self.client.get("/endpoint-comun")

    @task(1)  # Peso 1: esta acción es menos frecuente
    def accion_rara(self):
        self.client.post("/endpoint-raro", json={"data": "test"})
```

### Ejecución

```bash
# Modo web (con dashboard visual)
locust -f locustfile.py --host=http://localhost:8000

# Modo headless (para CI/CD)
locust -f locustfile.py --host=http://localhost:8000 \
    --headless --users 50 --spawn-rate 5 --run-time 60s
```

---


## 6. Escenarios de Carga para TaskFlow

### Locustfile Completo: TaskFlow

```python
# agents/stress_testing/scenarios/taskflow_load.py
"""
Escenarios de carga para TaskFlow.

NOTA EDUCATIVA:
Este archivo simula usuarios REALES del sistema:
- Se registran y loguean
- Crean, leen y buscan tareas
- Cada acción tiene un peso (frecuencia realista)

Los pesos reflejan el uso real:
- Listar tareas (más frecuente — es lo primero que haces)
- Crear tarea (frecuente)
- Buscar (medio)
- Completar (menos frecuente)
"""

import random
import string
from locust import HttpUser, task, between, events


class TaskFlowUser(HttpUser):
    """Simula un usuario típico de TaskFlow."""

    wait_time = between(1, 3)  # Pausa realista entre acciones
    host = "http://localhost:8000"

    def on_start(self):
        """
        Se ejecuta UNA vez cuando el usuario virtual "nace".
        Registra un usuario único y obtiene token.

        NOTA EDUCATIVA:
        on_start() simula que el usuario ya está logueado
        cuando empieza a usar el sistema. Es como el "Given"
        de BDD: establece el contexto inicial.
        """
        # Crear usuario único para este virtual user
        suffix = ''.join(random.choices(string.ascii_lowercase, k=8))
        self.email = f"loadtest_{suffix}@test.com"
        self.password = "LoadTest$2026"
        self.task_ids = []

        # Registrar
        self.client.post("/auth/register", json={
            "nombre": f"LoadTest User {suffix}",
            "email": self.email,
            "password": self.password,
        })

        # Login
        response = self.client.post("/auth/login", json={
            "email": self.email,
            "password": self.password,
        })

        if response.status_code == 200:
            self.token = response.json()["token"]
            self.headers = {"Authorization": f"Bearer {self.token}"}
        else:
            self.token = None
            self.headers = {}

    @task(5)  # Peso 5: acción más frecuente
    def list_tasks(self):
        """
        LECTURA — Lo más frecuente.
        Los usuarios pasan más tiempo VIENDO que CREANDO.
        """
        with self.client.get(
            "/tasks",
            headers=self.headers,
            catch_response=True,
            name="/tasks [LIST]"
        ) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code == 401:
                response.failure("Auth expired")
            else:
                response.failure(f"Status {response.status_code}")

    @task(3)  # Peso 3: frecuente
    def create_task(self):
        """
        ESCRITURA — Crear tareas.
        Genera carga en la base de datos.
        """
        task_data = {
            "titulo": f"Task {random.randint(1, 99999)}",
            "descripcion": "Tarea generada por stress test",
            "prioridad": random.choice(["baja", "media", "alta"]),
        }

        with self.client.post(
            "/tasks",
            json=task_data,
            headers=self.headers,
            catch_response=True,
            name="/tasks [CREATE]"
        ) as response:
            if response.status_code == 201:
                task_id = response.json().get("id")
                if task_id:
                    self.task_ids.append(task_id)
                response.success()
            else:
                response.failure(f"Status {response.status_code}")

    @task(2)  # Peso 2: medio
    def search_tasks(self):
        """
        BÚSQUEDA — Carga media.
        Las queries de búsqueda son más pesadas para la DB.
        """
        search_terms = ["informe", "revisar", "comprar", "llamar", "tarea"]
        term = random.choice(search_terms)

        self.client.get(
            f"/tasks?search={term}",
            headers=self.headers,
            name="/tasks [SEARCH]"
        )

    @task(1)  # Peso 1: menos frecuente
    def complete_task(self):
        """
        ACTUALIZACIÓN — Completar una tarea.
        """
        if self.task_ids:
            task_id = random.choice(self.task_ids)
            self.client.patch(
                f"/tasks/{task_id}",
                json={"estado": "completada"},
                headers=self.headers,
                name="/tasks/{id} [COMPLETE]"
            )


class AdminUser(HttpUser):
    """
    Simula un admin (menos frecuente, operaciones más pesadas).
    Peso menor: 1 admin por cada 10 usuarios normales.
    """

    weight = 1  # vs TaskFlowUser que tiene weight=10 por defecto
    wait_time = between(5, 10)  # Admins hacen cosas menos seguido

    def on_start(self):
        """Login como admin."""
        response = self.client.post("/auth/login", json={
            "email": "admin@taskflow.com",
            "password": "AdminPassword$2026",
        })
        if response.status_code == 200:
            self.headers = {"Authorization": f"Bearer {response.json()['token']}"}
        else:
            self.headers = {}

    @task
    def list_all_users(self):
        """Admin ve todos los usuarios (query pesada)."""
        self.client.get("/admin/users", headers=self.headers, name="/admin/users")
```

---

## 7. Perfiles de Usuario

### ¿Por qué múltiples perfiles?

En producción, NO todos los usuarios se comportan igual:

```
┌──────────────────────────────────────────────────────────────┐
│            DISTRIBUCIÓN DE USUARIOS REALES                     │
│                                                                │
│  70% ─ Lectores (solo ven sus tareas)                         │
│         → @task(5) list_tasks                                  │
│                                                                │
│  20% ─ Creadores activos (crean y completan)                   │
│         → @task(3) create + @task(1) complete                  │
│                                                                │
│   8% ─ Buscadores (usan mucho el search)                       │
│         → @task(2) search_tasks                                │
│                                                                │
│   2% ─ Admins (operaciones pesadas, poco frecuentes)           │
│         → AdminUser class (weight=1)                           │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

### Tabla de Perfiles

| Perfil | % del tráfico | Acción principal | Impacto en sistema |
|--------|--------------|-----------------|-------------------|
| **Lector** | 45% | GET /tasks | Bajo (solo lectura) |
| **Creador** | 27% | POST /tasks | Medio (escritura DB) |
| **Buscador** | 18% | GET /tasks?search= | Alto (query pesada) |
| **Admin** | 10% | GET /admin/* | Alto (queries amplias) |

---

## 8. Análisis de Resultados

### Ejemplo de Output de Locust

```
╭──────────────────────────────────────────────────────────────╮
│           📊 STRESS TEST RESULTS — TaskFlow                   │
│           Duration: 60s | Peak Users: 50                      │
╰──────────────────────────────────────────────────────────────╯

┌─────────────────────┬────────┬─────────┬─────────┬────────┐
│ Endpoint            │  RPS   │  p50    │  p95    │ Errors │
├─────────────────────┼────────┼─────────┼─────────┼────────┤
│ /tasks [LIST]       │  45.2  │   8ms   │   35ms  │  0.0%  │
│ /tasks [CREATE]     │  27.1  │  12ms   │   52ms  │  0.0%  │
│ /tasks [SEARCH]     │  18.3  │  22ms   │   95ms  │  0.0%  │
│ /tasks/{id} [COMPL] │   9.1  │  10ms   │   40ms  │  0.0%  │
│ /admin/users        │   2.3  │  45ms   │  180ms  │  0.0%  │
├─────────────────────┼────────┼─────────┼─────────┼────────┤
│ TOTAL               │ 102.0  │  12ms   │   65ms  │  0.0%  │
└─────────────────────┴────────┴─────────┴─────────┴────────┘

Métricas de Recursos:
  Memory: 85MB (peak) / 512MB (limit) ✅
  CPU: 12% avg / 45% peak ✅

Veredicto: ✅ PASA — Soporta 50 usuarios con p95 < 100ms
```

### Cómo Interpretar los Resultados

| Métrica | Valor | Significado |
|---------|-------|-------------|
| RPS = 102 | 102 requests/segundo | El sistema procesa ~6000 requests/minuto |
| p50 = 12ms | La mitad responde en <12ms | Experiencia típica: EXCELENTE |
| p95 = 65ms | 95% responde en <65ms | Incluso los lentos son aceptables |
| Error Rate = 0% | Ningún request falló | El sistema es estable a 50 usuarios |
| Memory = 85MB | Muy lejos del límite de 512MB | Hay mucho margen |

### ¿Cuándo PREOCUPARTE?

| Señal de alarma | Significado | Acción |
|-----------------|-------------|--------|
| p95 > 500ms | Los usuarios sienten lentitud | Optimizar queries |
| Error Rate > 1% | Usuarios ven errores | Investigar causa |
| Memory creciendo linealmente | Memory leak | Profiling |
| p95 diverge mucho de p50 | Algunos requests son MUY lentos | Encontrar outliers |
| RPS cae al subir usuarios | El sistema se satura | Escalar o optimizar |

---

## 9. Patrones de Degradación

### ¿Cómo se "rompe" un sistema?

```
Rendimiento
    │
100%├──────────────────────┐
    │                      │ ← "Zona saludable"
    │                      │
 80%├──────────────────────┤
    │                       ╲
    │                        ╲ ← "Degradación gradual" (aceptable)
 60%├─────────────────────────╲
    │                          │
    │                          │ ← "Punto de inflexión"
 40%├──────────────────────────┤
    │                           ╲
    │                            ╲ ← "Colapso" (inaceptable)
 20%├─────────────────────────────╲
    │                              ╲________
  0%└──────────────────────────────────────────
    0     25     50     75     100    125    150
                    Usuarios concurrentes
```

### Los 3 Patrones

| Patrón | Comportamiento | Causa Típica | En TaskFlow |
|--------|---------------|--------------|-------------|
| **Degradación gradual** | Latencia sube linealmente | Recursos compartidos | Queries más lentas con más datos |
| **Punto de quiebre** | Todo colapsa de repente | Pool de conexiones agotado | DB connections limit |
| **Recuperación** | Vuelve a la normalidad al bajar carga | Buen diseño de resiliencia | Circuit breaker + auto-scaling |

---

## 10. Stress Testing + API Validation

### Conexión: Rate Limiting Protege contra Stress Involuntario

```
┌──────────────────────────────────────────────────────────────┐
│                                                                │
│  STRESS TESTING detecta:       API VALIDATION previene:       │
│  "A 200 usuarios, la API       "Si alguien manda 1000 req/s, │
│   externa colapsa"              el rate limiter lo frena"     │
│                                                                │
│  ┌─────────────┐              ┌──────────────────────────┐   │
│  │ Stress Test │  informa →   │ Configurar Rate Limiter  │   │
│  │ "límite=150 │              │ "max 100 req/min"        │   │
│  │  req/s"     │              │                          │   │
│  └─────────────┘              └──────────────────────────┘   │
│                                                                │
│  Uno ENCUENTRA el límite. El otro LO PROTEGE.                 │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

---

## 11. Ejercicios Prácticos

### Ejercicio 1: Diseña un Plan de Carga (15 min) 📋

**Nivel**: Principiante

Para tu sistema profesional, define:

| Pregunta | Tu respuesta |
|----------|-------------|
| ¿Cuántos usuarios simultáneos esperas? | ___ |
| ¿Cuál es tu endpoint más usado? | ___ |
| ¿Cuál es tu endpoint más pesado? | ___ |
| ¿Qué latencia p95 es aceptable? | ___ ms |
| ¿Qué error rate es tolerable? | ___ % |

### Ejercicio 2: Escribe tu Primer Locustfile (20 min) 🐛

**Nivel**: Principiante-Intermedio

Escribe un locustfile para un sistema de tu profesión:

```python
from locust import HttpUser, task, between

class MiUsuario(HttpUser):
    wait_time = between(__, __)  # ¿Cuánto "piensa" tu usuario?

    @task(__)  # ¿Qué peso tiene esta acción?
    def accion_principal(self):
        # ¿Cuál es la acción más frecuente?
        self.client.get("/___")

    @task(__)
    def accion_secundaria(self):
        # ¿Cuál es menos frecuente pero más pesada?
        self.client.post("/___", json={...})
```

### Ejercicio 3: Interpreta Resultados (20 min) 📊

**Nivel**: Intermedio

Dados estos resultados, ¿qué conclusiones sacas?

```
Users: 100 | Duration: 120s

/api/products [GET]:    RPS=45  p50=15ms  p95=800ms   Errors=0%
/api/orders [POST]:     RPS=12  p50=50ms  p95=3200ms  Errors=8%
/api/search [GET]:      RPS=30  p50=25ms  p95=450ms   Errors=0%
```

Preguntas:
1. ¿Cuál endpoint es problemático?
2. ¿Por qué el p95 de orders es tan alto vs su p50?
3. ¿8% de errores en orders es aceptable?
4. ¿Qué harías primero para mejorar?

### Ejercicio 4: Ejecuta un Smoke Test (30 min) 🔥

**Nivel**: Avanzado

1. Levanta TaskFlow localmente (`uvicorn examples.taskflow.api.main:app`)
2. Ejecuta locust con 5 usuarios por 60 segundos
3. Documenta los resultados
4. ¿Cumple las metas ISO 25023?

---

## 12. Referencias

### Herramientas

| Herramienta | Lenguaje | Uso |
|-------------|----------|-----|
| **Locust** | Python | Framework principal del proyecto |
| **k6** | JavaScript | Alternativa popular, buena para CI |
| **Apache JMeter** | Java/GUI | El clásico (más complejo) |
| **Artillery** | JS/YAML | Simple para APIs REST |
| **Gatling** | Scala | Alto rendimiento |

### Conexión con ISO 25010

| Métrica Stress | Característica ISO 25010 | Sub-característica |
|---------------|--------------------------|-------------------|
| Latencia p95 | Eficiencia de Desempeño | Comportamiento temporal |
| Memory usage | Eficiencia de Desempeño | Utilización de recursos |
| Concurrent users | Eficiencia de Desempeño | Capacidad |
| Error rate bajo carga | Fiabilidad | Tolerancia a fallos |
| Recovery time | Fiabilidad | Recuperabilidad |

---

## Control de Cambios

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0.0 | 2026-08-03 | Versión inicial completa |

---

> **Stress Testing responde la pregunta que nadie hace hasta que es tarde:**
> "¿Qué pasa cuando TODOS usan el sistema al mismo tiempo?"
>
> Flujo del taller:
> BDD → TDD → SOLID → OWASP → ISO 25010 → **Stress** → UX → APIs
