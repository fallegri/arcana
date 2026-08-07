# Guía OWASP Paso a Paso
## Seguridad de Aplicaciones Web — Los 10 Riesgos Más Críticos

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0.0 |
| **Fecha** | 2026-08-03 |
| **Público** | Profesionales multidisciplinarios (universitario+) |
| **Prerrequisitos** | Haber completado las guías BDD, TDD y SOLID |
| **Duración estimada** | 4-6 horas (taller completo) |
| **Proyecto ejemplo** | TaskFlow — vulnerabilidades reales y sus correcciones |
| **Referencia** | OWASP Top 10:2021 |

---

## Tabla de Contenidos

1. [¿Qué es OWASP?](#1-qué-es-owasp)
2. [¿Por qué la Seguridad importa?](#2-por-qué-la-seguridad-importa)
3. [A01 — Broken Access Control](#3-a01--broken-access-control)
4. [A02 — Cryptographic Failures](#4-a02--cryptographic-failures)
5. [A03 — Injection](#5-a03--injection)
6. [A04 — Insecure Design](#6-a04--insecure-design)
7. [A05 — Security Misconfiguration](#7-a05--security-misconfiguration)
8. [A06 — Vulnerable Components](#8-a06--vulnerable-components)
9. [A07 — Authentication Failures](#9-a07--authentication-failures)
10. [A08 — Data Integrity Failures](#10-a08--data-integrity-failures)
11. [A09 — Logging & Monitoring Failures](#11-a09--logging--monitoring-failures)
12. [A10 — SSRF](#12-a10--ssrf)
13. [Seguridad con IA Asistida](#13-seguridad-con-ia-asistida)
14. [Ejercicios Prácticos](#14-ejercicios-prácticos)
15. [Referencias](#15-referencias)

---

## 1. ¿Qué es OWASP?

### Definición Simple

> **OWASP es una lista de los 10 errores de seguridad más comunes y peligrosos
> que los desarrolladores cometen al crear aplicaciones web.**

Es como un "Top 10 de formas en que te pueden hackear" — y cómo evitarlo.

### Definición Técnica

OWASP (Open Web Application Security Project) es una fundación sin fines de lucro
que publica estándares, herramientas y guías de seguridad. Su documento más conocido
es el **OWASP Top 10**, actualizado periódicamente, que lista los 10 riesgos
de seguridad más críticos para aplicaciones web.

### Metáfora: La Casa y sus Cerraduras 🏠

```
┌──────────────────────────────────────────────────────────────┐
│                                                                │
│  TU APLICACIÓN = TU CASA                                      │
│                                                                │
│  A01 (Access Control)   = Quién tiene llave de qué puerta     │
│  A02 (Crypto)           = La calidad de las cerraduras         │
│  A03 (Injection)        = Alguien mete algo por debajo de la puerta │
│  A04 (Insecure Design)  = Casa diseñada sin cerraduras         │
│  A05 (Misconfiguration) = Dejaste la puerta abierta           │
│  A06 (Components)       = La cerradura tiene un defecto conocido │
│  A07 (Auth Failures)    = Las llaves se pueden copiar fácil    │
│  A08 (Integrity)        = Alguien cambió la cerradura sin que sepas │
│  A09 (Logging)          = No tienes cámaras de seguridad      │
│  A10 (SSRF)             = Tu mayordomo abre la puerta a cualquiera │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. ¿Por qué la Seguridad importa?

### Para Cada Perfil Profesional

| Perfil | Riesgo Real | Consecuencia |
|--------|-------------|-------------|
| **Empresario** | Datos de clientes filtrados | Multas GDPR, pérdida de confianza, cierre |
| **Abogado** | Expedientes accesibles sin permiso | Violación de secreto profesional, demandas |
| **Economista** | Datos financieros manipulados | Fraude, reportes incorrectos, pérdidas |
| **Gastrónomo** | Sistema de pedidos hackeado | Pedidos falsos, datos de tarjetas robados |
| **Educador** | Calificaciones modificadas | Fraude académico, pérdida de credibilidad |
| **Informático** | Código con vulnerabilidades | Responsabilidad legal, reputación dañada |

### El Costo de NO Asegurar

```
Costo promedio de un data breach (IBM, 2024):

    $4.45M ┤████████████████████████████████████████
           │
    $3.0M  ┤                            Detección tardía
           │
    $1.5M  ┤              Detección temprana
           │
    $150K  ┤  Prevención (OWASP desde el diseño)
           │
           └─────────────────────────────────────────
            Prevenir    Detectar    Detectar    Breach
            (OWASP)    temprano    tarde       público
```

---


## 3. A01 — Broken Access Control

### ¿Qué es?

> **Broken Access Control** = Los usuarios pueden hacer cosas que NO deberían poder hacer.

Ejemplo cotidiano: Imagina que en un edificio de oficinas, cualquier empleado
puede entrar a la oficina del director, revisar su computadora y modificar
los contratos. Eso es "acceso roto".

### Impacto

| Ataque | Consecuencia | En TaskFlow |
|--------|-------------|-------------|
| Un usuario ve tareas de otro | Privacidad violada | María ve los pendientes de Carlos |
| Un usuario se auto-promueve a admin | Escalamiento de privilegios | Usuario normal se da permisos de admin |
| Acceso a endpoint sin autenticación | Exposición de datos | `/admin/users` accesible sin login |

### ❌ Código VULNERABLE en TaskFlow

```python
# ❌ VULNERABLE — No verifica que la tarea pertenece al usuario
@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    return task  # ← Cualquier usuario puede ver CUALQUIER tarea
    # María pide GET /tasks/42 y ve la tarea de Carlos

# ❌ VULNERABLE — No verifica permisos para eliminar
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(task)  # ← Cualquiera puede borrar la tarea de otro
    db.commit()
```

### ✅ Código SEGURO en TaskFlow

```python
# ✅ SEGURO — Verifica propiedad de la tarea
@app.get("/tasks/{task_id}")
def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),  # ← Auth obligatoria
    db: Session = Depends(get_db),
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id  # ← Solo sus propias tareas
    ).first()

    if task is None:
        raise HTTPException(
            status_code=404,  # ← 404, no 403 (no revelar que existe)
            detail="Tarea no encontrada"
        )
    return task


# ✅ SEGURO — Control de acceso por rol
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id  # ← Solo el dueño puede borrar
    ).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    task.eliminado = True  # ← Soft delete (recuperable)
    db.commit()
    return {"message": "Tarea eliminada"}
```

### Controles Implementados

| Control | Cómo funciona | Dónde |
|---------|-------------|-------|
| `Depends(get_current_user)` | Verifica JWT en cada request | Endpoints protegidos |
| `Task.user_id == current_user.id` | Filtra por propiedad | Queries a DB |
| `404` en vez de `403` | No revelar existencia | Respuestas de error |
| Roles RBAC | admin vs usuario normal | Middleware de permisos |

### Escenario BDD de Verificación

```gherkin
Scenario: No puedo ver tareas de otro usuario
  Given "María" está autenticada
  And "Carlos" tiene una tarea con id 42
  When María intenta acceder a GET /tasks/42
  Then recibe un error 404 "Tarea no encontrada"
  And NO ve el contenido de la tarea de Carlos
```

---


## 4. A02 — Cryptographic Failures

### ¿Qué es?

> **Cryptographic Failures** = Los datos sensibles no están protegidos correctamente.
> Contraseñas en texto plano, tokens predecibles, transmisión sin cifrar.

Ejemplo cotidiano: Es como escribir tu PIN del banco en un post-it pegado
en la tarjeta. Técnicamente "guardaste" el PIN, pero cualquiera lo lee.

### Impacto

| Fallo | Consecuencia | En TaskFlow |
|-------|-------------|-------------|
| Password en texto plano | Si hackean la DB, leen TODAS las contraseñas | Acceso a todas las cuentas |
| Token predecible | Cualquiera puede generar tokens válidos | Suplantación de identidad |
| Sin HTTPS | Interceptan datos en tránsito | Roban credenciales en red pública |

### ❌ Código VULNERABLE

```python
# ❌ VULNERABLE — Password en texto plano
class AuthService:
    def register(self, email, password):
        user = User(
            email=email,
            password=password  # ← ¡TEXTO PLANO en la base de datos!
        )
        db.add(user)
        db.commit()

    def login(self, email, password):
        user = db.query(User).filter_by(email=email).first()
        if user.password == password:  # ← Comparación directa
            return {"token": f"token-{user.id}"}  # ← Token predecible


# ❌ VULNERABLE — Token predecible
def generate_token(user_id):
    return f"token-{user_id}"  # ← Cualquiera adivina: token-1, token-2...
```

### ✅ Código SEGURO en TaskFlow

```python
# ✅ SEGURO — Nuestra implementación real en AuthService
class AuthService:
    def register(self, nombre, email, password):
        # Validar requisitos de contraseña
        self._validate_password(password)

        # HASHEAR con bcrypt (irreversible + salt automático)
        password_hash = self._hash_password(password)

        user = User(
            nombre=nombre,
            email=email,
            password_hash=password_hash,  # ← HASH, nunca texto plano
        )
        # ...

    def _hash_password(self, password: str) -> str:
        """
        bcrypt genera:
        - Salt aleatorio (protege contra rainbow tables)
        - Hash irreversible (no puedes "des-hashear")
        - Cost factor configurable (más lento = más seguro)

        Resultado: '$2b$12$LJ3m4bG...' (60+ caracteres)
        """
        from passlib.hash import bcrypt
        return bcrypt.hash(password)

    def _verify_password(self, password: str, hash: str) -> bool:
        """Verifica sin NUNCA almacenar el password original."""
        from passlib.hash import bcrypt
        return bcrypt.verify(password, hash)

    def _generate_token(self, user: User) -> str:
        """
        JWT con:
        - Firma criptográfica (no se puede falsificar)
        - Expiración (24h — limita ventana de ataque)
        - Claims mínimos (no expone datos sensibles)
        """
        from jose import jwt
        payload = {
            "sub": str(user.id),     # Subject (quién)
            "exp": datetime.now() + timedelta(hours=24),  # Expira
            "iat": datetime.now(),   # Emitido
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
```

### Test que Verifica la Criptografía

```python
# De nuestro test_auth_service.py (ya funciona ✅)
def test_password_not_stored_plain_text(self, auth_service, test_db):
    """OWASP A02: Contraseña NUNCA en texto plano."""
    auth_service.register(nombre="Ana", email="ana@test.com", password="MiClave$123")

    user = test_db.query(User).filter_by(email="ana@test.com").first()
    assert user.password_hash != "MiClave$123"  # ← No es texto plano
    assert len(user.password_hash) > 20          # ← Es un hash largo
```

---


## 5. A03 — Injection

### ¿Qué es?

> **Injection** = Un atacante mete código malicioso dentro de tus datos,
> y tu sistema lo EJECUTA como si fuera instrucción legítima.

Ejemplo cotidiano: Imagina un formulario donde escribes tu nombre.
En lugar de "María", alguien escribe: `María"; DROP TABLE users; --`
Y tu sistema BORRA toda la tabla de usuarios.

### Impacto: EL MÁS PELIGROSO

| Tipo de Injection | Qué hace | Gravedad |
|-------------------|----------|----------|
| **SQL Injection** | Lee/modifica/borra la base de datos | 🔴 Crítica |
| **Command Injection** | Ejecuta comandos en el servidor | 🔴 Crítica |
| **XSS (Cross-Site Script)** | Ejecuta JavaScript en el browser del usuario | 🟡 Alta |
| **Template Injection** | Ejecuta código en el motor de plantillas | 🔴 Crítica |

### ❌ Código VULNERABLE — SQL Injection

```python
# ❌ MUY VULNERABLE — SQL construido concatenando strings
@app.get("/tasks/search")
def search_tasks(query: str):
    # Si query = ' OR 1=1 -- ', retorna TODAS las tareas de TODOS
    # Si query = '; DROP TABLE tasks; --', BORRA la tabla
    sql = f"SELECT * FROM tasks WHERE titulo LIKE '%{query}%'"
    results = db.execute(sql)  # ← ¡EJECUTA lo que el atacante quiera!
    return results


# ❌ VULNERABLE — Ejemplo de ataque
# GET /tasks/search?query=' OR '1'='1' --
# SQL resultante: SELECT * FROM tasks WHERE titulo LIKE '%' OR '1'='1' --%'
# ← Retorna TODAS las tareas (bypass de filtro)

# GET /tasks/search?query='; DROP TABLE tasks; --
# SQL resultante: SELECT * FROM tasks WHERE titulo LIKE '%'; DROP TABLE tasks; --%'
# ← ¡BORRA la tabla entera!
```

### ✅ Código SEGURO en TaskFlow (Doble Protección)

```python
# ✅ PROTECCIÓN 1: SQLAlchemy ORM (queries parametrizadas)
class TaskRepository:
    def search(self, user_id: int, text: str) -> List[Task]:
        """
        SQLAlchemy NUNCA concatena strings en SQL.
        Usa queries parametrizadas que tratan el input
        SIEMPRE como DATOS, nunca como INSTRUCCIONES.
        """
        return (
            self._db.query(Task)
            .filter(
                Task.user_id == user_id,       # ← Parámetro seguro
                Task.titulo.contains(text),     # ← Parámetro seguro
            )
            .all()
        )
        # Si text = "'; DROP TABLE tasks; --"
        # SQLAlchemy genera: WHERE titulo LIKE '%''; DROP TABLE tasks; --%'
        # ← Lo trata como TEXTO literal, no como SQL


# ✅ PROTECCIÓN 2: Pydantic valida ANTES de llegar al código
class TaskCreate(BaseModel):
    """
    Pydantic rechaza datos que no cumplan el schema.
    Si el título tiene caracteres sospechosos o es demasiado largo,
    se rechaza ANTES de tocar la base de datos.
    """
    titulo: str = Field(..., min_length=3, max_length=200)
    descripcion: str = Field(default="", max_length=2000)


# ✅ PROTECCIÓN 3: El Validator limpia el input
class TaskValidator:
    def validate_title(self, titulo):
        """Strip elimina caracteres peligrosos al inicio/fin."""
        clean = titulo.strip()
        # El título limpio pasa a SQLAlchemy que lo parametriza
        return clean
```

### Diagrama de Defensa en Profundidad contra Injection

```
Input del usuario: "'; DROP TABLE tasks; --"
         │
         ▼
┌─────────────────────┐
│  CAPA 1: Pydantic   │  → Valida largo, tipo, formato
│  (Schema Validation) │  → Si no cumple: RECHAZA (422)
└──────────┬──────────┘
           │ (pasó validación de formato)
           ▼
┌─────────────────────┐
│  CAPA 2: Validator  │  → Strip, sanitize, reglas de negocio
│  (Business Rules)    │  → Si no cumple: RECHAZA (ValueError)
└──────────┬──────────┘
           │ (pasó validación de negocio)
           ▼
┌─────────────────────┐
│  CAPA 3: SQLAlchemy │  → Query parametrizada
│  (ORM)               │  → NUNCA concatena SQL
│                      │  → El input es DATA, no INSTRUCCIÓN
└──────────┬──────────┘
           │ (query segura)
           ▼
┌─────────────────────┐
│  BASE DE DATOS      │  → Solo recibe queries bien formadas
└─────────────────────┘
```

---


## 6. A04 — Insecure Design

### ¿Qué es?

> **Insecure Design** = El sistema fue DISEÑADO sin pensar en seguridad.
> No es un bug de código — es un defecto en la ARQUITECTURA.

La diferencia clave: A03 (Injection) es un error de implementación que puedes
parchear. A04 es que NUNCA pensaste en el ataque desde el diseño.

### Ejemplo en TaskFlow

| Diseño Inseguro | Diseño Seguro |
|-----------------|---------------|
| "Las tareas son públicas por defecto" | "Las tareas son PRIVADAS por defecto" |
| "No necesitamos rate limiting" | "Todos los endpoints tienen rate limit" |
| "El admin puede hacer todo sin auditoría" | "Toda acción admin se audita" |

### Cómo lo Resolvemos: Threat Modeling en el SDD

En nuestro SDD (Sección 2.5 — Vista de Seguridad), diseñamos la seguridad
ANTES de escribir código:

```
Principio: "Secure by Default"
- Todo endpoint requiere autenticación (opt-OUT, no opt-IN)
- Todo dato es privado (el usuario solo ve lo suyo)
- Todo input se valida (Pydantic strict mode)
- Toda API externa tiene rate limiting
```

### Conexión con BDD

```gherkin
# Este escenario se escribió en FASE DE DISEÑO (antes del código)
Scenario: No puedo ver tareas de otro usuario
  Given "María" está autenticada
  And "Carlos" tiene tareas privadas
  When María intenta listar las tareas de Carlos
  Then recibe error 404
  And NO puede ver el contenido
```

> **A04 se previene en la fase BDD**: si escribes escenarios de seguridad
> ANTES de codificar, el diseño es seguro desde el inicio.

---

## 7. A05 — Security Misconfiguration

### ¿Qué es?

> **Security Misconfiguration** = Todo está bien codificado, pero MAL configurado.
> Es como tener la mejor cerradura del mundo... pero dejar la llave puesta.

### Ejemplos Comunes

| Misconfiguration | Riesgo | En TaskFlow |
|-----------------|--------|-------------|
| Debug mode en producción | Expone stack traces con código fuente | `app = FastAPI(debug=True)` en prod |
| Secret key hardcoded | Cualquiera puede firmar tokens JWT | `SECRET = "mi-secreto"` en el código |
| CORS permisivo (`*`) | Cualquier sitio puede hacer requests | `allow_origins=["*"]` |
| Endpoints de admin expuestos | Acceso sin restricción | `/docs` con Swagger abierto |

### ✅ Configuración SEGURA en TaskFlow

```python
# ✅ SEGURO — Configuración con Pydantic Settings
from pydantic_settings import BaseSettings

class SecurityConfig(BaseSettings):
    """
    OWASP A05: Toda configuración sensible viene de variables de entorno.
    NUNCA hardcoded en el código.

    Uso: SECRET_KEY=xxx JWT_ALGORITHM=HS256 python -m uvicorn main:app
    """

    secret_key: str  # ← OBLIGATORIO desde env (falla si no existe)
    jwt_algorithm: str = "HS256"
    jwt_expiration_hours: int = 24
    debug: bool = False  # ← False por defecto (seguro por defecto)
    allowed_origins: list = ["https://midominio.com"]  # ← NO usar "*"
    max_login_attempts: int = 5
    lockout_minutes: int = 15

    class Config:
        env_file = ".env"  # Carga de archivo .env (no commitear)


# ✅ Archivo .env (en .gitignore — NUNCA en el repositorio)
# SECRET_KEY=una-clave-larga-y-aleatoria-de-64-caracteres-minimo
# DATABASE_URL=postgresql://user:pass@localhost/taskflow
# DEBUG=false
```

### Checklist de Configuración Segura

| Item | Verificación | Herramienta |
|------|-------------|-------------|
| Secrets en env vars | `grep -r "password\|secret\|key" *.py` | bandit |
| Debug desactivado | `debug=False` en producción | Config check |
| CORS restrictivo | Solo dominios específicos | Revisión manual |
| Headers de seguridad | X-Frame, CSP, HSTS | SecurityHeaders.com |
| .env en .gitignore | No commitear secrets | `git status` |

---

## 8. A06 — Vulnerable and Outdated Components

### ¿Qué es?

> **Vulnerable Components** = Usas una librería que tiene un bug de seguridad
> conocido y publicado. Los atacantes ya saben CÓMO explotarlo.

Ejemplo cotidiano: Es como tener una cerradura de la que el fabricante
ya publicó que tiene un defecto, y los ladrones ya tienen la herramienta
para abrirla — pero tú no la has cambiado.

### Cómo se Verifica en TaskFlow

```bash
# Herramienta: pip-audit — escanea dependencias por CVEs conocidos
$ pip-audit

Found 2 known vulnerabilities in 1 package:
  pyjwt 2.4.0 has 1 vulnerability:
    CVE-2022-29217: Algorithm confusion attack (HIGH)

  requests 2.28.0 has 1 vulnerability:
    CVE-2023-32681: Proxy credential leak (MEDIUM)

# Solución: actualizar
$ pip install --upgrade pyjwt requests
```

### Controles en el Proyecto

| Control | Herramienta | Cuándo |
|---------|-------------|--------|
| Escaneo de CVEs | `pip-audit` | Cada build/CI |
| Dependencias actualizadas | `pip list --outdated` | Semanal |
| Lock file | `requirements.txt` con versiones fijas | Siempre |
| Alertas automáticas | Dependabot / Safety | Continuo |

---

## 9. A07 — Identification and Authentication Failures

### ¿Qué es?

> **Authentication Failures** = El sistema de login/registro tiene debilidades
> que permiten a un atacante acceder como otro usuario.

### Lo que YA Implementamos en TaskFlow (tests pasando ✅)

| Control | Implementación | Test que lo verifica |
|---------|---------------|---------------------|
| Bloqueo por fuerza bruta | 5 intentos → bloqueo 15 min | `test_account_locks_after_5_failures` |
| Mensajes genéricos | "Credenciales inválidas" (no revela qué falló) | `test_nonexistent_email_same_error` |
| Password hasheado | bcrypt con salt automático | `test_password_not_stored_plain_text` |
| Requisitos de contraseña | Min 8 chars + mayúscula + número + especial | `test_register_weak_password_raises_error` |
| Counter reset | Login exitoso reinicia contador | `test_successful_login_resets_counter` |

### Diagrama de Flujo Seguro de Login

```
┌─────────────┐
│ Login Request│
└──────┬──────┘
       │
       ▼
┌──────────────┐     ┌──────────────────┐
│ ¿Cuenta      │ SÍ  │ Retornar error   │
│ bloqueada?   │────▶│ "Cuenta bloqueada│
└──────┬───────┘     │  temporalmente"  │
       │ NO          └──────────────────┘
       ▼
┌──────────────┐     ┌──────────────────┐
│ ¿Usuario     │ NO  │ Retornar error   │
│ existe?      │────▶│ GENÉRICO         │
└──────┬───────┘     │"Credenciales     │
       │ SÍ          │ inválidas"       │
       ▼             └──────────────────┘
┌──────────────┐            ▲
│ ¿Password    │ NO         │
│ correcto?    │────────────┘
└──────┬───────┘     + incrementar contador
       │ SÍ          + si contador >= 5 → bloquear
       ▼
┌──────────────┐
│ Resetear     │
│ contador     │
│ Generar JWT  │
│ Retornar     │
└──────────────┘
```

---


## 10. A08 — Software and Data Integrity Failures

### ¿Qué es?

> **Data Integrity Failures** = No puedes garantizar que el código o los datos
> no fueron modificados por un atacante entre que los creaste y los usaste.

### En el Contexto del Proyecto

| Riesgo | Control | Implementación |
|--------|---------|---------------|
| Dependencia alterada (supply chain) | Verificar hashes | `pip install --require-hashes` |
| Código modificado sin autorización | Commits firmados | `git commit -S` |
| JWT modificado | Firma criptográfica | `jwt.encode(..., SECRET_KEY)` |
| Config alterada | Validación al cargar | Pydantic strict mode |

### Ejemplo: JWT Integrity

```python
# El JWT tiene 3 partes: header.payload.SIGNATURE
# Si un atacante modifica el payload (ej: cambia user_id),
# la firma NO coincide y el token se RECHAZA.

# Verificación:
def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        # Si el token fue modificado → DecodeError
        # Si expiró → ExpiredSignatureError
        return payload
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
```

---

## 11. A09 — Security Logging and Monitoring Failures

### ¿Qué es?

> **Logging Failures** = No tienes forma de SABER que te están atacando,
> ni de reconstruir QUÉ pasó después de un incidente.

Es como una tienda SIN cámaras de seguridad: te roban y nunca sabes quién fue.

### Lo que TaskFlow Registra

```python
import logging
import structlog

# Configuración de logging estructurado
logger = structlog.get_logger()

class AuthService:
    def login(self, email, password):
        user = self._db.query(User).filter_by(email=email).first()

        if user is None or not self._verify_password(password, user.password_hash):
            # ✅ REGISTRAR intento fallido (OWASP A09)
            logger.warning(
                "login_failed",
                email=email,
                reason="invalid_credentials",
                ip=request.client.host,  # Quién intentó
                timestamp=datetime.now().isoformat(),
            )
            self._record_failed_attempt(user)
            raise AuthenticationError("Credenciales inválidas")

        # ✅ REGISTRAR login exitoso
        logger.info(
            "login_success",
            user_id=user.id,
            email=email,
            ip=request.client.host,
        )
        # ...
```

### Qué Debe Registrarse (y qué NO)

| ✅ REGISTRAR | ❌ NUNCA REGISTRAR |
|-------------|-------------------|
| Intentos de login fallidos | Contraseñas (ni correctas ni incorrectas) |
| Accesos denegados (403) | Tokens JWT completos |
| Cambios de rol/permisos | Datos personales sensibles |
| Errores de validación sospechosos | Números de tarjeta de crédito |
| IPs con múltiples fallos | Respuestas de APIs externas completas |

---

## 12. A10 — Server-Side Request Forgery (SSRF)

### ¿Qué es?

> **SSRF** = Engañar a tu servidor para que haga requests a lugares
> donde NO debería — como tu red interna o servicios privados.

### Relevancia para TaskFlow (API Validation)

Nuestro sistema llama a APIs externas (LLMs, servicios). Sin control:

```python
# ❌ VULNERABLE — El usuario controla la URL
@app.post("/fetch-data")
def fetch_external(url: str):
    response = requests.get(url)  # ← ¡El usuario puede pedir CUALQUIER URL!
    return response.json()

# Ataque: POST /fetch-data {"url": "http://169.254.169.254/metadata"}
# ← Accede a metadatos de AWS/GCP (credenciales del servidor)
```

```python
# ✅ SEGURO — Allowlist de URLs permitidas
ALLOWED_DOMAINS = {"api.openai.com", "api.taskflow.local"}

@app.post("/fetch-data")
def fetch_external(url: str):
    from urllib.parse import urlparse
    parsed = urlparse(url)

    if parsed.hostname not in ALLOWED_DOMAINS:
        raise HTTPException(400, "Dominio no permitido")

    if parsed.scheme != "https":
        raise HTTPException(400, "Solo HTTPS permitido")

    # Verificar que no es IP privada
    import ipaddress
    try:
        ip = ipaddress.ip_address(parsed.hostname)
        if ip.is_private:
            raise HTTPException(400, "IPs privadas no permitidas")
    except ValueError:
        pass  # Es un dominio, no IP — ok

    response = requests.get(url, timeout=5)  # ← Timeout obligatorio
    return response.json()
```

---


## 13. Seguridad con IA Asistida

### ¿Por qué la IA Necesita Guía de Seguridad?

| Sin guía OWASP | Con guía OWASP |
|----------------|----------------|
| La IA genera código funcional pero inseguro | La IA genera código funcional Y seguro |
| `f"SELECT * FROM users WHERE id={user_id}"` | `db.query(User).filter(User.id == user_id)` |
| `password = request.form["password"]` | `password_hash = bcrypt.hash(password)` |
| Sin rate limiting | Con circuit breaker + token bucket |

### Prompts Efectivos para Seguridad

```markdown
## Para revisar seguridad:
"Revisa este código buscando vulnerabilidades OWASP Top 10.
Para cada una encontrada:
1. Identifica la categoría OWASP (A01-A10)
2. Muestra cómo un atacante lo explotaría
3. Propón la corrección"

## Para generar código seguro:
"Implementa un endpoint de login con estas protecciones OWASP:
- A02: Password hasheado con bcrypt
- A07: Bloqueo después de 5 intentos fallidos
- A09: Log de todos los intentos (sin loggear el password)
- Mensajes de error genéricos (no revelar info)"

## Para crear tests de seguridad:
"Genera tests que verifiquen estas protecciones:
- SQL injection no funciona (A03)
- Un usuario no puede ver datos de otro (A01)
- Passwords no se guardan en texto plano (A02)
- La cuenta se bloquea tras fuerza bruta (A07)"
```

---

## 14. Ejercicios Prácticos

### Ejercicio 1: Identifica la Vulnerabilidad (15 min) 🔍

**Nivel**: Principiante

Identifica qué categoría OWASP viola cada código:

```python
# Código A:
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return db.query(User).filter(User.id == user_id).first()
# Vulnerabilidad: ___ (pista: ¿cualquiera puede ver cualquier usuario?)

# Código B:
def register(email, password):
    user = User(email=email, password=password)
    db.add(user)
# Vulnerabilidad: ___ (pista: ¿cómo se guarda el password?)

# Código C:
@app.get("/search")
def search(q: str):
    results = db.execute(f"SELECT * FROM products WHERE name LIKE '%{q}%'")
    return results
# Vulnerabilidad: ___ (pista: ¿qué pasa si q = "' OR 1=1 --"?)

# Código D:
SECRET_KEY = "mi-clave-super-secreta-123"
# Vulnerabilidad: ___ (pista: ¿esto va al repositorio de código?)
```

**Respuestas**: A=A01, B=A02, C=A03, D=A05

---

### Ejercicio 2: Corrige la Vulnerabilidad (25 min) 🔧

**Nivel**: Intermedio

Toma el Código C del ejercicio anterior y:
1. Reescribe usando SQLAlchemy ORM (protección contra A03)
2. Agrega validación Pydantic del parámetro `q`
3. Agrega autenticación (protección contra A01)
4. Escribe 2 tests que verifiquen la protección

---

### Ejercicio 3: Diseño Seguro desde Cero (30 min) 🏗️

**Nivel**: Intermedio-Avanzado

Diseña un endpoint de "cambio de contraseña" que sea seguro:

**Requisitos**:
- El usuario debe estar autenticado (A01)
- Debe proporcionar la contraseña actual (verificar)
- La nueva contraseña debe cumplir requisitos (A02)
- Registrar el cambio en logs (A09)
- No revelar información en errores (A07)

**Entrega**: Código + test BDD + 2 tests unitarios

---

### Ejercicio 4: Pentest Básico de TaskFlow (30 min) 🕵️

**Nivel**: Avanzado

Intenta "atacar" los endpoints de TaskFlow:

1. **A01**: ¿Puedes ver tareas de otro usuario?
2. **A03**: ¿Puedes inyectar SQL en la búsqueda?
3. **A07**: ¿Puedes hacer fuerza bruta sin bloqueo?
4. **A05**: ¿Hay algún secret expuesto?

Documenta: qué intentaste, qué pasó, por qué la defensa funcionó.

---

### Ejercicio 5: BDD de Seguridad (30 min) 🛡️

**Nivel**: Todos

Escribe escenarios Gherkin de seguridad para tu profesión:

| Si eres... | Feature de seguridad |
|-----------|---------------------|
| Abogado | "Expedientes solo visibles por el abogado asignado" |
| Economista | "Reportes financieros requieren doble autenticación" |
| Gastrónomo | "Recetas secretas no son accesibles por staff temporal" |
| Empresario | "Datos de clientes aislados entre franquicias" |

Escribe: Feature + 3 escenarios (happy path, acceso denegado, auditoría)

---

## 15. Referencias

### Recursos Oficiales OWASP

| Recurso | URL | Uso |
|---------|-----|-----|
| OWASP Top 10 (2021) | owasp.org/Top10/ | Referencia principal |
| OWASP ASVS 4.0 | owasp.org/asvs/ | Verificación detallada |
| OWASP Cheat Sheets | cheatsheetseries.owasp.org | Guías rápidas por tema |
| OWASP Testing Guide | owasp.org/testing-guide/ | Cómo testear seguridad |

### Herramientas Usadas en el Proyecto

| Herramienta | Propósito | Categoría OWASP |
|-------------|-----------|----------------|
| `bandit` | Análisis estático de seguridad (Python) | A03, A05 |
| `pip-audit` | Vulnerabilidades en dependencias | A06 |
| `safety` | Verificación de CVEs | A06 |
| `semgrep` | Detección de patrones inseguros | A01-A10 |
| `pytest` | Tests de seguridad automatizados | Todos |

### Conexión con Otros Módulos del Taller

| Módulo | Conexión con OWASP |
|--------|-------------------|
| **BDD** | Los escenarios de seguridad se escriben en Gherkin |
| **TDD** | Los controles se verifican con tests unitarios |
| **SOLID** | SRP en validación previene A03 (Injection) |
| **ISO 25010** | Seguridad es una de las 8 características de calidad |
| **API Validation** | Rate limiting previene A07 (Auth Failures) |

---

## Control de Cambios

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0.0 | 2026-08-03 | Versión inicial completa del recurso formativo |

---

> **Este documento es un recurso académico para el taller de Desarrollo Asistido por IA.**
> Cada vulnerabilidad se presenta con:
> 1. Explicación simple (para no-técnicos)
> 2. Código vulnerable (❌) vs seguro (✅) (para técnicos)
> 3. Tests que verifican la protección (para validar)
> 4. Escenarios BDD (para especificar)
>
> Flujo del taller:
> BDD → TDD → SOLID → **OWASP** → ISO 25010 → Stress → UX → APIs
