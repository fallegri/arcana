# Guía SOLID Paso a Paso
## Principios de Diseño de Software — La Base de Todo Código Mantenible

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0.0 |
| **Fecha** | 2026-08-03 |
| **Público** | Profesionales multidisciplinarios (universitario+) |
| **Prerrequisitos** | Haber completado las guías BDD y TDD |
| **Duración estimada** | 3-5 horas (taller completo) |
| **Proyecto ejemplo** | TaskFlow — código REAL que aplica cada principio |

---

## Tabla de Contenidos

1. [¿Qué es SOLID?](#1-qué-es-solid)
2. [¿Por qué SOLID importa?](#2-por-qué-solid-importa)
3. [S — Single Responsibility Principle](#3-s--single-responsibility-principle)
4. [O — Open/Closed Principle](#4-o--openclosed-principle)
5. [L — Liskov Substitution Principle](#5-l--liskov-substitution-principle)
6. [I — Interface Segregation Principle](#6-i--interface-segregation-principle)
7. [D — Dependency Inversion Principle](#7-d--dependency-inversion-principle)
8. [SOLID en Acción: El Refactoring de TaskFlow](#8-solid-en-acción-el-refactoring-de-taskflow)
9. [SOLID y la IA Asistida](#9-solid-y-la-ia-asistida)
10. [Ejercicios Prácticos](#10-ejercicios-prácticos)
11. [Anti-patrones y Code Smells](#11-anti-patrones-y-code-smells)
12. [Referencias](#12-referencias)

---

## 1. ¿Qué es SOLID?

### Definición Simple

> **SOLID son 5 reglas para escribir código que sea fácil de entender,
> cambiar y mantener — sin que todo se rompa cada vez que tocas algo.**

### Definición Técnica

SOLID es un acrónimo de 5 principios de diseño orientado a objetos,
propuestos por Robert C. Martin ("Uncle Bob"), que guían la creación de
software flexible, comprensible y mantenible.

| Letra | Principio | En una frase |
|-------|-----------|--------------|
| **S** | Single Responsibility | "Una clase, una razón para cambiar" |
| **O** | Open/Closed | "Abierto para extensión, cerrado para modificación" |
| **L** | Liskov Substitution | "Los hijos deben poder reemplazar al padre" |
| **I** | Interface Segregation | "Interfaces pequeñas y específicas" |
| **D** | Dependency Inversion | "Depende de abstracciones, no de detalles" |

### La Metáfora del Equipo de Cocina 🍳

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│  COCINA SIN SOLID (restaurante que fracasa):                      │
│  Un solo cocinero hace TODO: lava, corta, cocina, sirve, cobra   │
│  → Si se enferma, el restaurante cierra                          │
│  → Si quieres agregar postre, él tiene que aprender              │
│  → Si comete un error, no sabes en cuál paso fue                 │
│                                                                   │
│  COCINA CON SOLID (restaurante estrella Michelin):                │
│  S: Cada persona tiene UN rol (chef, sous-chef, pastelero)       │
│  O: Puedes agregar un pastelero sin cambiar al chef principal    │
│  L: Cualquier sous-chef puede reemplazar a otro sous-chef        │
│  I: El mesero no necesita saber de cocina, solo de servicio      │
│  D: El chef pide "proteína", no "específicamente salmón noruego" │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Mapa de SOLID en Nuestro Proyecto

```
┌──────────────────────────────────────────────────────────────┐
│              SOLID EN AI-DEV-GUIDE / TASKFLOW                  │
│                                                                │
│  S (SRP):  TaskService ← solo coordina                        │
│            TaskValidator ← solo valida                         │
│            TaskRepository ← solo persiste                      │
│                                                                │
│  O (OCP):  AgentRegistry ← agregar agentes sin modificar      │
│            Pipeline ← nuevas fases sin tocar el motor          │
│                                                                │
│  L (LSP):  BaseAgent ← todos los agentes son intercambiables  │
│            BDDAgent, TDDAgent, OWASPAgent... misma interfaz     │
│                                                                │
│  I (ISP):  AgentInput/AgentOutput ← contratos mínimos          │
│            TaskCreate vs TaskResponse vs TaskUpdate             │
│                                                                │
│  D (DIP):  TaskService(repository, validator) ← inyectados     │
│            Pipeline(config, registry) ← no crea dependencias   │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. ¿Por qué SOLID importa?

### El Problema que SOLID Resuelve

```
Sin SOLID:                              Con SOLID:

Cambio pequeño                          Cambio pequeño
     │                                       │
     ▼                                       ▼
Rompe 5 archivos                        Toca 1 archivo
     │                                       │
     ▼                                       ▼
Parcheas los 5                          Tests siguen pasando
     │                                       │
     ▼                                       ▼
Rompe 3 más                             ✅ Listo
     │
     ▼
"Ya fue, reescribimos todo" 💀
```

### Para Cada Perfil

| Perfil | Sin SOLID | Con SOLID |
|--------|-----------|-----------|
| **Empresario** | "Cada feature nueva tarda más que la anterior" | "Las features se agregan a velocidad constante" |
| **Legal** | "El sistema es un black box imposible de auditar" | "Cada módulo tiene una responsabilidad clara y auditable" |
| **Desarrollador** | "Tengo miedo de tocar el código" | "Cambio con confianza, los tests me protegen" |
| **Economista** | "El costo de mantenimiento crece exponencialmente" | "El costo se mantiene lineal" |

### Métricas del Impacto (ISO 25010 — Mantenibilidad)

| Métrica | Sin SOLID | Con SOLID |
|---------|-----------|-----------|
| Tiempo para agregar feature | Crece exponencialmente | Se mantiene constante |
| Bugs al hacer cambios | 3-5 por cambio | 0-1 por cambio |
| Archivos tocados por cambio | 5-10 | 1-3 |
| Tiempo de onboarding | Semanas | Días |
| Tests rotos al cambiar | Muchos | Solo los del módulo |

---


## 3. S — Single Responsibility Principle

### Definición

> **"Una clase debe tener una, y solo una, razón para cambiar."**
> — Robert C. Martin

### En Lenguaje Simple

Cada pieza de código debe hacer **UNA sola cosa**. Si tu clase necesita cambiar
por dos razones diferentes, es que tiene dos responsabilidades y debe dividirse.

### Metáfora: El Restaurante 🍽️

- ❌ **Sin SRP**: Un empleado que cocina, sirve, cobra y lava → si se enferma, todo se detiene
- ✅ **Con SRP**: Chef cocina, mesero sirve, cajero cobra → cada uno tiene un rol claro

### Señales de que Violas SRP (Code Smells)

| Señal | Significado |
|-------|-------------|
| Clase con >200 líneas | Probablemente hace demasiado |
| Nombre con "And" o "Manager" | `UserAndOrderManager` = 2 responsabilidades |
| Método con muchos if/elif | Diferentes razones de cambio mezcladas |
| Necesitas mockear muchas cosas en tests | El objeto depende de demasiado |
| Un cambio rompe tests no relacionados | Responsabilidades acopladas |

### Ejemplo REAL: TaskFlow — El Refactoring de TaskService

#### ❌ ANTES (viola SRP): Todo en un solo método

```python
# ❌ TaskService ANTES del refactoring — "God Method"
# Este método tiene 3 RAZONES para cambiar:
# 1. Si cambian las reglas de validación
# 2. Si cambia cómo se persiste en la base de datos
# 3. Si cambian los permisos de autenticación

class TaskService:
    def __init__(self, db):
        self._db = db

    def create_task(self, titulo, user_id, descripcion="", prioridad="media"):
        # RESPONSABILIDAD 1: Autenticación ← razón de cambio A
        if not user_id:
            raise PermissionError("Se requiere autenticación")

        # RESPONSABILIDAD 2: Validación ← razón de cambio B
        if titulo is None or titulo.strip() == "":
            raise ValueError("El título es obligatorio")
        if len(titulo.strip()) < 3:
            raise ValueError("El título debe tener al menos 3 caracteres")
        if len(titulo.strip()) > 200:
            raise ValueError("El título no puede exceder 200 caracteres")

        # RESPONSABILIDAD 3: Persistencia ← razón de cambio C
        task = Task(
            titulo=titulo.strip(),
            descripcion=descripcion,
            estado="pendiente",
            prioridad=prioridad,
            user_id=user_id,
        )
        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)

        return TaskResponse(id=task.id, titulo=task.titulo, ...)
```

**Problemas**:
- Si cambias la regla de longitud mínima → tocas `create_task`
- Si cambias de SQLAlchemy a MongoDB → tocas `create_task`
- Si cambias el sistema de auth → tocas `create_task`
- Testear validación REQUIERE una base de datos (lento, frágil)

#### ✅ DESPUÉS (aplica SRP): Cada clase tiene UNA responsabilidad

```python
# ✅ TaskValidator — SOLO valida (razón de cambio: reglas de negocio)
class TaskValidator:
    TITLE_MIN = 3
    TITLE_MAX = 200

    def validate_title(self, titulo):
        if titulo is None or titulo.strip() == "":
            raise ValueError("El título es obligatorio")
        clean = titulo.strip()
        if len(clean) < self.TITLE_MIN:
            raise ValueError(f"Mínimo {self.TITLE_MIN} caracteres")
        if len(clean) > self.TITLE_MAX:
            raise ValueError(f"Máximo {self.TITLE_MAX} caracteres")
        return clean


# ✅ TaskRepository — SOLO persiste (razón de cambio: tecnología de DB)
class TaskRepository:
    def __init__(self, db):
        self._db = db

    def save(self, task):
        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)
        return task


# ✅ TaskService — SOLO coordina (razón de cambio: flujo de negocio)
class TaskService:
    def __init__(self, repository, validator):
        self._repository = repository
        self._validator = validator

    def create_task(self, titulo, user_id, descripcion="", prioridad="media"):
        self._require_auth(user_id)                    # Delega
        titulo_limpio = self._validator.validate_title(titulo)  # Delega
        task = Task(titulo=titulo_limpio, ...)
        return self._repository.save(task)             # Delega
```

#### Tabla de Separación

| Clase | Responsabilidad ÚNICA | Razón para cambiar |
|-------|----------------------|-------------------|
| `TaskValidator` | Validar datos | Las reglas de negocio cambian |
| `TaskRepository` | Guardar/leer de DB | La tecnología de DB cambia |
| `TaskService` | Coordinar el flujo | El proceso de negocio cambia |

#### Beneficios Concretos

```python
# ANTES: Para testear validación necesitabas la DB completa
def test_titulo_vacio():
    db = create_real_database()  # ← LENTO, requiere infra
    service = TaskService(db)
    ...

# DESPUÉS: Testeas validación SIN base de datos
def test_titulo_vacio():
    validator = TaskValidator()  # ← RÁPIDO, sin dependencias
    with pytest.raises(ValueError):
        validator.validate_title("")
```

---

## 4. O — Open/Closed Principle

### Definición

> **"Las entidades de software deben estar abiertas para extensión,
> pero cerradas para modificación."**
> — Bertrand Meyer

### En Lenguaje Simple

Puedes **agregar** funcionalidad nueva sin **cambiar** el código que ya funciona.
Es como agregar un nuevo electrodoméstico a tu cocina: enchufas el nuevo
sin rewirear toda la instalación eléctrica.

### Metáfora: Los Enchufes de tu Casa ⚡

- ❌ **Sin OCP**: Para agregar un nuevo electrodoméstico, tienes que abrir la pared y cambiar los cables
- ✅ **Con OCP**: Solo enchufas el nuevo aparato en un enchufe libre

### Ejemplo REAL: El AgentRegistry

```python
# orchestrator/pipeline.py — CERRADO para modificación
# Este código NUNCA cambia cuando agregas un nuevo agente

class Pipeline:
    def __init__(self, config, registry: AgentRegistry):
        self._registry = registry

    async def _run_phase(self, phase_name, phase_config):
        for agent_name in phase_config.agents:
            agent = self._registry.get(agent_name)  # Obtiene por nombre
            output = await agent.run(input_data)    # Ejecuta
            # ← NO hay if/elif para cada agente nuevo

# agents/registry.py — ABIERTO para extensión
class AgentRegistry:
    def register(self, agent: BaseAgent) -> None:
        """Registra un agente nuevo sin tocar NADA más."""
        self._agents[agent.name] = agent

# USO: Agregar un agente nuevo = 0 modificaciones al sistema existente
registry = AgentRegistry()
registry.register(BDDAgent())      # ← Solo agregas aquí
registry.register(TDDAgent())      # ← Y aquí
registry.register(OWASPAgent())    # ← Y aquí
# El Pipeline, la Config, y todo lo demás NO SE TOCAN
```

### Anti-patrón: El `if/elif` Infinito

```python
# ❌ VIOLA OCP — Cada agente nuevo requiere MODIFICAR este código
def run_agent(agent_type: str, input_data):
    if agent_type == "bdd":
        return BDDAgent().execute(input_data)
    elif agent_type == "tdd":
        return TDDAgent().execute(input_data)
    elif agent_type == "owasp":
        return OWASPAgent().execute(input_data)
    # ← Para agregar uno nuevo, MODIFICAS esta función
    # ← Y re-testeas TODA esta función
    # ← Y arriesgas romper los existentes

# ✅ APLICA OCP — El Registry hace innecesario el if/elif
def run_agent(agent_name: str, registry: AgentRegistry, input_data):
    agent = registry.get(agent_name)  # Polimorfismo
    return agent.execute(input_data)  # Mismo contrato para todos
    # ← Para agregar uno nuevo, solo lo registras
    # ← CERO modificaciones al código existente
```

### OCP en la Configuración YAML

```yaml
# config/default.yaml
# Agregar una nueva fase = cambiar configuración, no código
phases:
  security:
    agents:
      - owasp
      - pentest
      - osint
      - new_agent_name  # ← Solo agrego aquí + creo el agente
```

---

## 5. L — Liskov Substitution Principle

### Definición

> **"Los objetos de una clase derivada deben poder sustituir a los objetos
> de la clase base sin alterar el comportamiento correcto del programa."**
> — Barbara Liskov

### En Lenguaje Simple

Si tu código espera un "vehículo", debe funcionar igual de bien con un auto,
una moto o una bicicleta. Si no funciona con alguno, ese "hijo" no es
realmente un vehículo para tu sistema.

### Metáfora: El Control Remoto Universal 📺

- ✅ **Con LSP**: Tu control remoto funciona con cualquier TV (Samsung, LG, Sony) → todos respetan el protocolo infrarrojo
- ❌ **Sin LSP**: Tu control remoto solo funciona con Samsung, y con LG hace cosas raras → el "hijo" no se comporta como el padre

### Ejemplo REAL: BaseAgent y sus Implementaciones

```python
# agents/base.py — El "contrato" que TODOS deben cumplir
class BaseAgent(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def description(self) -> str: ...

    @abstractmethod
    async def execute(self, input_data: AgentInput) -> AgentOutput: ...

    async def run(self, input_data: AgentInput) -> AgentOutput:
        """Método público — la MISMA secuencia para TODOS."""
        errors = self.validate_input(input_data)
        if errors:
            return AgentOutput(agent_name=self.name, status="error", errors=errors)
        await self.on_start(input_data)
        output = await self.execute(input_data)
        await self.on_complete(output)
        return output
```

```python
# Cualquiera de estos puede usarse donde se espera BaseAgent:
class BDDAgent(BaseAgent):        # ✅ Sustituible
class TDDAgent(BaseAgent):        # ✅ Sustituible
class OWASPAgent(BaseAgent):      # ✅ Sustituible
class StressTestAgent(BaseAgent): # ✅ Sustituible

# El Pipeline NO sabe cuál agente concreto usa — y no le importa:
async def _run_phase(self, phase_name, phase_config):
    for agent_name in phase_config.agents:
        agent: BaseAgent = self._registry.get(agent_name)
        output = await agent.run(input_data)  # ← Funciona con CUALQUIERA
```

### ¿Cuándo se VIOLA LSP?

```python
# ❌ VIOLA LSP — El "hijo" no se comporta como el padre
class SyncAgent(BaseAgent):
    async def execute(self, input_data):
        raise NotImplementedError("Este agente no soporta async")
        # ← El Pipeline espera que TODOS soporten run()
        # ← Si este lanza error, rompe el pipeline

# ❌ VIOLA LSP — El "hijo" cambia el tipo de retorno
class WeirdAgent(BaseAgent):
    async def execute(self, input_data):
        return "un string"  # ← Debería retornar AgentOutput
        # ← El Pipeline espera AgentOutput con .status, .metrics, etc.

# ✅ CUMPLE LSP — Se comporta exactamente como el padre promete
class ProperAgent(BaseAgent):
    async def execute(self, input_data) -> AgentOutput:
        # Hace su trabajo específico...
        return AgentOutput(
            agent_name=self.name,
            status="success",
            metrics={"my_metric": 42.0},
        )
```

### Regla Práctica para LSP

> **Si tu código tiene algo como esto, probablemente violas LSP:**
> ```python
> if isinstance(agent, SpecialAgent):
>     agent.special_method()  # ← Necesitas saber el tipo concreto
> else:
>     agent.run()
> ```
>
> **La solución**: todos implementan la misma interfaz y el código
> que los usa NO necesita `isinstance` ni `type()`.

---

## 6. I — Interface Segregation Principle

### Definición

> **"Los clientes no deberían verse forzados a depender de interfaces
> que no utilizan."**
> — Robert C. Martin

### En Lenguaje Simple

No obligues a alguien a implementar cosas que no necesita.
Es mejor tener muchas interfaces pequeñas y específicas
que una sola interfaz enorme que haga todo.

### Metáfora: El Menú del Restaurante 🍽️

- ❌ **Sin ISP**: Un "Menú Universal" donde el cliente de sushi TAMBIÉN tiene que pedir pizza, postre y vino (paquete forzado)
- ✅ **Con ISP**: Menú separado por categoría — pides SOLO lo que necesitas

### Ejemplo REAL: Schemas de Pydantic en TaskFlow

```python
# ❌ VIOLA ISP — Un solo schema "God Interface" para todo
class TaskSchema(BaseModel):
    """Si usas esto para CREAR, te obliga a poner id y fecha_creacion
    (que aún no existen). Si lo usas para LEER, te obliga a poner
    password (que no quieres exponer)."""
    id: int                    # ← No lo tienes al crear
    titulo: str
    descripcion: str
    estado: str
    prioridad: str
    fecha_creacion: date       # ← No lo pasas al crear
    fecha_modificacion: date   # ← No lo pasas al crear
    user_id: int
    password_hash: str         # ← ¡NUNCA debería exponerse!


# ✅ APLICA ISP — Interfaces pequeñas y específicas
class TaskCreate(BaseModel):
    """SOLO lo que necesitas para CREAR."""
    titulo: str
    descripcion: str = ""
    prioridad: str = "media"
    # Sin id, sin fecha, sin password → el creador no los necesita

class TaskResponse(BaseModel):
    """SOLO lo que se RETORNA al usuario."""
    id: int
    titulo: str
    descripcion: str
    estado: str
    prioridad: str
    fecha_creacion: date
    # Sin password_hash → el usuario no debe verlo

class TaskUpdate(BaseModel):
    """SOLO lo que se puede MODIFICAR."""
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    prioridad: Optional[str] = None
    # Sin id, sin fecha_creacion → no se pueden cambiar
```

### ISP en AgentInput/AgentOutput

```python
# ✅ AgentInput — Datos MÍNIMOS que todo agente necesita
@dataclass
class AgentInput:
    phase: str                    # Qué fase ejecuta
    project_path: Path            # Dónde está el proyecto
    config: Dict[str, Any]        # Config específica del agente
    context: SharedContext        # Estado compartido
    previous_results: List[AgentOutput]  # Resultados anteriores

# Cada agente SOLO usa lo que necesita de aquí.
# El BDDAgent usa project_path para encontrar .feature
# El StressAgent usa config para leer umbrales
# Ninguno está forzado a usar campos que no le interesan
```

### ¿Cuándo violas ISP?

```python
# ❌ Interfaz "gorda" — fuerza a implementar lo que no necesitas
class FullReportGenerator(ABC):
    @abstractmethod
    def generate_pdf(self): ...
    @abstractmethod
    def generate_html(self): ...
    @abstractmethod
    def generate_csv(self): ...
    @abstractmethod
    def send_email(self): ...    # ← ¿Y si solo quiero PDF?

# ✅ Interfaces segregadas — implementa SOLO lo que necesitas
class PDFGenerator(ABC):
    @abstractmethod
    def generate_pdf(self): ...

class HTMLGenerator(ABC):
    @abstractmethod
    def generate_html(self): ...

class EmailSender(ABC):
    @abstractmethod
    def send_email(self): ...

# Ahora puedes ser PDFGenerator sin estar obligado a enviar emails
```

---

## 7. D — Dependency Inversion Principle

### Definición

> **"Los módulos de alto nivel no deben depender de módulos de bajo nivel.
> Ambos deben depender de abstracciones."**
> — Robert C. Martin

### En Lenguaje Simple

Tu código de negocio no debe conocer los detalles técnicos.
En lugar de decir "quiero SQLite", dice "quiero algo que guarde datos".
Así puedes cambiar SQLite por PostgreSQL sin tocar la lógica de negocio.

### Metáfora: El Enchufe Eléctrico ⚡

- ❌ **Sin DIP**: Tu laptop tiene los cables soldados directamente a la pared → si cambias de casa, necesitas una laptop nueva
- ✅ **Con DIP**: Tu laptop tiene un enchufe estándar → funciona en cualquier casa, en cualquier país (con adaptador)

El "enchufe" es la **abstracción** — ambos lados (laptop y pared) dependen del estándar del enchufe, no uno del otro directamente.

### Ejemplo REAL: TaskService No Conoce la Base de Datos

```python
# ❌ SIN DIP — El servicio DEPENDE DIRECTAMENTE de SQLAlchemy
class TaskService:
    def __init__(self):
        # Crea su propia conexión (dependencia hardcoded)
        self._db = create_engine("sqlite:///taskflow.db")
        self._session = Session(self._db)

    def create_task(self, titulo, user_id):
        task = Task(titulo=titulo, user_id=user_id)
        self._session.add(task)    # ← Acoplado a SQLAlchemy
        self._session.commit()     # ← Si cambias DB, reescribes TODO
        return task

# Problemas:
# - No puedes testear sin una base de datos real
# - No puedes cambiar de SQLite a PostgreSQL sin reescribir
# - No puedes usar un mock para tests rápidos


# ✅ CON DIP — El servicio depende de una ABSTRACCIÓN (Repository)
class TaskService:
    def __init__(self, repository: TaskRepository, validator: TaskValidator):
        # Recibe dependencias INYECTADAS (no las crea)
        self._repository = repository
        self._validator = validator

    def create_task(self, titulo, user_id):
        titulo_limpio = self._validator.validate_title(titulo)
        task = Task(titulo=titulo_limpio, user_id=user_id)
        return self._repository.save(task)  # ← No sabe cómo se guarda
```

### El Diagrama de Inversión

```
SIN DIP (dependencia directa):
┌──────────────┐         ┌──────────────┐
│  TaskService │────────▶│  SQLAlchemy  │
│ (alto nivel) │         │ (bajo nivel) │
└──────────────┘         └──────────────┘
     El servicio CONOCE la tecnología de DB

CON DIP (dependencia invertida):
┌──────────────┐         ┌──────────────────┐
│  TaskService │────────▶│  TaskRepository  │ ◀── ABSTRACCIÓN
│ (alto nivel) │         │  (interfaz)       │
└──────────────┘         └────────┬─────────┘
                                   │
                                   │ implementa
                                   ▼
                         ┌──────────────────┐
                         │  SQLAlchemy      │
                         │  Repository      │
                         │ (implementación) │
                         └──────────────────┘
     Ambos dependen de la abstracción, no uno del otro
```

### DIP en Tests (el beneficio killer)

```python
# GRACIAS a DIP, puedes testear con un Mock (sin DB real):
def test_create_task_saves_to_repository():
    # Mock del repository — NO necesitas base de datos
    mock_repo = Mock(spec=TaskRepository)
    mock_repo.save.return_value = Task(id=1, titulo="Test")

    service = TaskService(repository=mock_repo, validator=TaskValidator())
    result = service.create_task(titulo="Test", user_id=1)

    # Verificas que SE LLAMÓ a save(), no que la DB funcione
    mock_repo.save.assert_called_once()
    assert result.titulo == "Test"

# Test RÁPIDO (0.001s) vs test con DB real (0.5s)
# 500x más rápido × 53 tests = minutos ahorrados cada ejecución
```

### DIP en el Pipeline (Orquestador)

```python
# orchestrator/pipeline.py — Depende de ABSTRACCIONES
class Pipeline:
    def __init__(self, config: PipelineConfig, registry: AgentRegistry):
        self._config = config      # No conoce YAML internamente
        self._registry = registry  # No conoce agentes concretos

    async def _run_phase(self, ...):
        agent: BaseAgent = self._registry.get(agent_name)
        output = await agent.run(input_data)
        # ← No sabe si es BDDAgent o TDDAgent
        # ← Solo sabe que cumple el contrato de BaseAgent
```

---


## 8. SOLID en Acción: El Refactoring de TaskFlow

### La Historia Completa: De "God Object" a SOLID

Este es el recorrido real que hicimos en el proyecto TaskFlow durante TDD (paso REFACTOR):

```
VERSIÓN 1 (TDD GREEN):            VERSIÓN 2 (TDD REFACTOR):
━━━━━━━━━━━━━━━━━━━━━━            ━━━━━━━━━━━━━━━━━━━━━━━━━━

┌────────────────────┐            ┌──────────────┐
│    TaskService     │            │ TaskService  │ ← Coordina (SRP)
│                    │            │              │
│ • Valida títulos   │    SRP     │ • create()   │
│ • Valida prioridad │ ────────▶  │ • list()     │
│ • Guarda en DB     │            │ • search()   │
│ • Busca en DB      │            └──────┬───────┘
│ • Verifica auth    │                    │
│ • Crea respuesta   │                    │ usa (DIP)
└────────────────────┘                    │
                                   ┌──────┴────────────────┐
                                   │                        │
                              ┌────▼──────┐          ┌─────▼────────┐
                              │Validator  │          │ Repository   │
                              │           │          │              │
                              │ • title() │          │ • save()     │
                              │ • priority│          │ • find()     │
                              │ • state() │          │ • search()   │
                              └───────────┘          └──────────────┘
                                  (SRP)                   (SRP+DIP)
```

### Los 5 Principios Presentes en el Refactoring

| Principio | Dónde se aplica | Antes | Después |
|-----------|----------------|-------|---------|
| **S** | TaskService | Hacía todo | Solo coordina |
| **O** | TaskValidator | Hardcoded en service | Clase extensible independiente |
| **L** | BaseAgent | N/A | Todos intercambiables |
| **I** | Schemas | Un schema gigante | Create, Response, Update separados |
| **D** | TaskService | Creaba su DB | Recibe repository inyectado |

### Métricas del Refactoring

| Métrica | Antes | Después | Mejora |
|---------|-------|---------|--------|
| Líneas por clase | ~150 | ~50 | 3x más conciso |
| Dependencias por clase | 5+ | 1-2 | Acoplamiento -60% |
| Tests que tocan DB | 100% | 40% | Tests 2.5x más rápidos |
| Archivos tocados por cambio | 3-5 | 1 | Impacto -70% |
| Tiempo de tests | ~2s | ~0.4s | 5x más rápido |

---

## 9. SOLID y la IA Asistida

### ¿Por qué SOLID Mejora el Vibe Coding con IA?

| Sin SOLID | Con SOLID |
|-----------|-----------|
| "Arregla el bug en esta función de 200 líneas" | "Arregla el bug en TaskValidator.validate_title()" |
| La IA tiene que entender TODO el contexto | La IA solo necesita 1 clase pequeña |
| El fix puede romper cosas inesperadas | El fix está aislado en su módulo |
| Difícil validar si la IA hizo bien | Ejecutas los tests de ese módulo |

### Prompts Efectivos para SOLID con IA

```markdown
## Para detectar violaciones:
"Analiza esta clase. ¿Viola algún principio SOLID?
Si es así, dime cuál y propón un refactoring."

## Para pedir refactoring SRP:
"Este método tiene {N} responsabilidades: [listar].
Sepáralas en clases independientes siguiendo SRP.
Los tests existentes NO deben modificarse."

## Para pedir refactoring DIP:
"Este servicio crea su propia base de datos internamente.
Refactoriza para que la reciba como parámetro (inyección).
Crea un repository que encapsule el acceso a datos."

## Para verificar OCP:
"Si quiero agregar un nuevo [agente/validador/formato],
¿necesito MODIFICAR código existente? Si sí, ¿cómo lo
rediseñamos para que solo se EXTIENDA?"
```

### La Regla de Oro con IA

> **Cuanto más SOLID es tu código, mejor lo entiende la IA,
> y mejores serán sus sugerencias y fixes.**
>
> Una clase de 50 líneas con una responsabilidad =
> contexto claro para la IA.
>
> Un "God Object" de 500 líneas =
> la IA se confunde y genera fixes parciales.

---


## 10. Ejercicios Prácticos

### Ejercicio 1: Detecta las Violaciones (15 min) 🔍

**Nivel**: Principiante
**Instrucciones**: Identifica qué principio SOLID viola cada código.

```python
# Código A:
class ReportGenerator:
    def generate_report(self, data, format, send_email=False):
        if format == "pdf":
            # 50 líneas generando PDF...
            pass
        elif format == "html":
            # 50 líneas generando HTML...
            pass
        elif format == "csv":
            # 30 líneas generando CSV...
            pass

        if send_email:
            # 20 líneas enviando email...
            pass

# ¿Qué viola? __________ (pista: tiene múltiples razones de cambio)


# Código B:
def process_payment(amount, payment_type):
    if payment_type == "credit_card":
        # procesar con Stripe...
        pass
    elif payment_type == "paypal":
        # procesar con PayPal...
        pass
    elif payment_type == "bitcoin":
        # procesar con Coinbase...
        pass
    # ¿Y si quieres agregar MercadoPago? → Modificas ESTA función

# ¿Qué viola? __________ (pista: no puedes extender sin modificar)


# Código C:
class Animal(ABC):
    @abstractmethod
    def fly(self): ...
    @abstractmethod
    def swim(self): ...
    @abstractmethod
    def run(self): ...

class Penguin(Animal):
    def fly(self):
        raise Exception("¡Los pingüinos no vuelan!")  # ← 💥
    def swim(self):
        return "Nadando..."
    def run(self):
        return "Caminando..."

# ¿Qué viola? __________ (pista: el hijo no cumple el contrato del padre)
```

**Respuestas**: A=SRP, B=OCP, C=LSP (y también ISP)

---

### Ejercicio 2: Refactoring SRP (20 min) 🔧

**Nivel**: Principiante-Intermedio
**Se te da este código**:

```python
class OrderProcessor:
    def process_order(self, order):
        # Valida
        if order.total <= 0:
            raise ValueError("Total inválido")
        if not order.customer_email:
            raise ValueError("Email requerido")

        # Calcula impuestos
        if order.country == "MX":
            tax = order.total * 0.16
        elif order.country == "US":
            tax = order.total * 0.08
        else:
            tax = order.total * 0.20

        # Guarda en base de datos
        db.save(Order(total=order.total + tax, ...))

        # Envía confirmación
        send_email(order.customer_email, f"Pedido confirmado: ${order.total + tax}")
```

**Tu trabajo**:
1. Identifica las responsabilidades (¿cuántas hay?)
2. Crea una clase por responsabilidad
3. El `OrderProcessor` solo debe coordinar

---

### Ejercicio 3: Aplica OCP (25 min) 🔌

**Nivel**: Intermedio
**Contexto**: Sistema de notificaciones que viola OCP.

```python
# ❌ Viola OCP — agregar canal = modificar esta función
def notify_user(user, message, channel):
    if channel == "email":
        send_email(user.email, message)
    elif channel == "sms":
        send_sms(user.phone, message)
    elif channel == "push":
        send_push(user.device_token, message)
    # ¿WhatsApp? ¿Slack? ¿Telegram? → Modificar aquí cada vez
```

**Tu trabajo**:
1. Diseña una interfaz `NotificationChannel`
2. Crea implementaciones: `EmailChannel`, `SMSChannel`, `PushChannel`
3. El `NotificationService` debe funcionar con CUALQUIER canal sin if/elif
4. Agrega `WhatsAppChannel` sin modificar código existente

---

### Ejercicio 4: DIP para tu Profesión (30 min) 🎯

**Nivel**: Intermedio-Avanzado

| Si eres... | Refactoriza esto |
|-----------|-----------------|
| Abogado | `CaseService` que crea su propia DB → inyectar `CaseRepository` |
| Economista | `ReportService` que llama directamente a API del banco → inyectar `DataProvider` |
| Gastrónomo | `RecipeService` que lee de archivo hardcoded → inyectar `RecipeSource` |
| Empresario | `InvoiceService` que genera PDF internamente → inyectar `DocumentGenerator` |

**Instrucciones**:
1. Identifica la dependencia "hardcoded"
2. Define la abstracción (interfaz)
3. Crea la implementación concreta
4. Inyecta la dependencia en el constructor
5. Escribe un test usando Mock

---

### Ejercicio 5: SOLID Completo (45 min) 🚀

**Nivel**: Avanzado
**Contexto**: Refactoriza este "God Object" aplicando los 5 principios.

```python
class AppManager:
    def __init__(self):
        self.db = sqlite3.connect("app.db")
        self.email_server = smtplib.SMTP("mail.server.com")

    def register_user(self, name, email, password):
        # Valida email, hashea password, guarda en DB, envía bienvenida
        ...  # 80 líneas

    def login_user(self, email, password):
        # Busca en DB, verifica hash, genera token, registra login
        ...  # 60 líneas

    def create_report(self, user_id, format="pdf"):
        # Consulta DB, genera reporte, envía por email
        ...  # 100 líneas
```

**Tu trabajo (aplica todo)**:
- **SRP**: Separa en UserService, ReportService, EmailService
- **OCP**: Los reportes deben soportar nuevos formatos sin if/elif
- **LSP**: Todos los generadores de reportes deben ser intercambiables
- **ISP**: Interfaces separadas para crear, leer, y reportar
- **DIP**: Inyecta DB y EmailServer, no los crees internamente

---

## 11. Anti-patrones y Code Smells

### Los Villanos de SOLID

| Anti-patrón | Principio que viola | Señal de alerta | Ejemplo |
|-------------|-------------------|-----------------|---------|
| **God Object** | SRP | Clase >300 líneas | `ApplicationManager` que hace todo |
| **Shotgun Surgery** | SRP | Un cambio toca 10 archivos | Cambiar formato de fecha = editar 12 clases |
| **if/elif infinito** | OCP | Switch con 10+ cases | `if type == "A": ... elif type == "B": ...` |
| **Refused Bequest** | LSP | Hijo lanza `NotImplemented` | `Penguin.fly()` → Exception |
| **Fat Interface** | ISP | Interfaz con 15+ métodos | `IDoEverything` que nadie implementa completo |
| **Hidden Dependency** | DIP | `import` dentro de método | `from database import get_connection` dentro de lógica |

### Tabla de Diagnóstico Rápido

| Si observas... | Probablemente viola... | Solución |
|---------------|----------------------|----------|
| "Tengo miedo de tocar esa clase" | SRP (hace demasiado) | Dividir responsabilidades |
| "Para agregar X tengo que editar Y" | OCP (no extensible) | Usar polimorfismo/registry |
| "Este test necesita 20 líneas de setup" | DIP (dependencias internas) | Inyectar mocks |
| "Algunos hijos lanzan NotImplemented" | LSP (mal heredado) | Repensar la jerarquía |
| "Implemento métodos vacíos para compilar" | ISP (interfaz gorda) | Segregar interfaces |

---

## 12. Referencias

### Libros Fundamentales

| Libro | Autor | Lo que Aporta |
|-------|-------|---------------|
| *Clean Architecture* | Robert C. Martin | SOLID en contexto de arquitectura |
| *Clean Code* | Robert C. Martin | SOLID aplicado a código diario |
| *Design Patterns* | Gang of Four | Patrones que naturalmente aplican SOLID |
| *Head First Design Patterns* | Freeman & Robson | SOLID visual y accesible |
| *Refactoring* | Martin Fowler | Cómo pasar de violación a cumplimiento |

### Conexión con Otros Estándares

| Estándar | Relación con SOLID |
|----------|-------------------|
| **ISO 25010** — Mantenibilidad | SOLID es CÓMO logras modularidad, reusabilidad y testeabilidad |
| **ISO 25023** — Métricas | Complejidad ciclomática y acoplamiento miden cumplimiento SOLID |
| **TDD** | El paso REFACTOR es donde APLICAS SOLID |
| **BDD** | Escenarios independientes reflejan SRP en features |
| **OWASP** | Validación separada (SRP) previene inyecciones (A03) |

### Regla Final

> **SOLID no es un dogma. Es una brújula.**
>
> No apliques SOLID "porque sí". Aplícalo cuando:
> - El código es difícil de testear → probablemente viola DIP
> - Un cambio rompe cosas no relacionadas → probablemente viola SRP
> - Agregar algo nuevo requiere modificar mucho → probablemente viola OCP
>
> Si tu código es simple, pequeño y claro, no lo sobre-ingenierices.
> SOLID brilla cuando la complejidad crece.

---

## Control de Cambios

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0.0 | 2026-08-03 | Versión inicial completa del recurso formativo |

---

> **Este documento es un recurso académico para el taller de Desarrollo Asistido por IA.**
> Está diseñado para usarse DESPUÉS de BDD y TDD, porque SOLID se aplica
> en el paso REFACTOR del ciclo TDD.
>
> Flujo del taller:
> 1. BDD (QUÉ) → 2. TDD (CÓMO) → 3. **SOLID (MEJOR)** → 4. Seguridad (PROTEGER)
>
> Código de referencia:
> - `examples/taskflow/api/services/` — Servicios refactorizados
> - `examples/taskflow/api/validators/` — Validadores extraídos (SRP)
> - `examples/taskflow/api/repositories/` — Repositorios extraídos (DIP)
> - `agents/base.py` — BaseAgent (LSP, OCP)
> - `agents/registry.py` — AgentRegistry (OCP)
