"""
Planner — Genera el Plan de Desarrollo completo.

Recibe requerimientos en lenguaje natural y produce un plan
de N pasos que la IA debe ejecutar secuencialmente.

Cada paso incluye:
- Instrucciones EXACTAS de qué implementar
- Archivos que debe crear/modificar
- Criterios de verificación (qué valida Arcana)
- Estándares que debe cumplir (SOLID, OWASP, etc.)
"""

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class Requirement:
    """Un requerimiento del usuario."""
    id: str
    description: str
    type: str  # "functional", "security", "ux", "performance"
    priority: str  # "must", "should", "could"


@dataclass
class Step:
    """Un paso del plan de desarrollo."""
    number: int
    phase: str  # "setup", "models", "services", "routers", "auth", "frontend", "tests", "deploy"
    title: str
    instructions: str  # Instrucciones detalladas para la IA
    files_to_create: List[str]
    files_to_modify: List[str] = field(default_factory=list)
    verification_criteria: List[str] = field(default_factory=list)
    standards: List[str] = field(default_factory=list)  # ["SOLID-SRP", "OWASP-A03"]
    depends_on: List[int] = field(default_factory=list)
    status: str = "pending"  # pending, in_progress, completed, failed


@dataclass
class DevelopmentPlan:
    """Plan completo de desarrollo generado por el Orchestrator."""
    id: str
    project_name: str
    created_at: str
    requirements: List[Requirement]
    steps: List[Step]
    entities: List[Dict]
    business_rules: List[str]
    current_step: int = 0
    total_steps: int = 0

    @property
    def progress_percentage(self) -> float:
        completed = sum(1 for s in self.steps if s.status == "completed")
        return (completed / len(self.steps) * 100) if self.steps else 0

    @property
    def current_step_obj(self) -> Optional[Step]:
        if 0 <= self.current_step < len(self.steps):
            return self.steps[self.current_step]
        return None

    def advance(self):
        if self.current_step < len(self.steps):
            self.steps[self.current_step].status = "completed"
            self.current_step += 1

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "project_name": self.project_name,
            "created_at": self.created_at,
            "progress": f"{self.progress_percentage:.0f}%",
            "current_step": self.current_step + 1,
            "total_steps": len(self.steps),
            "steps": [
                {"number": s.number, "phase": s.phase, "title": s.title, "status": s.status}
                for s in self.steps
            ],
        }


class Planner:
    """
    Genera planes de desarrollo desde requerimientos.

    El plan es una secuencia ORDENADA de pasos que,
    ejecutados en orden, producen un sistema completo.
    """

    def create_plan(
        self,
        project_name: str,
        requirements_text: str,
        output_path: Path,
    ) -> DevelopmentPlan:
        """
        Genera un plan completo desde texto de requerimientos.

        El plan sigue la filosofía Arcana:
        BDD → Modelos → Servicios (SOLID) → Routers → Auth (OWASP) → Tests → Frontend → Deploy
        """
        # Parsear requerimientos
        requirements = self._parse_requirements(requirements_text)
        entities = self._extract_entities(requirements_text)
        business_rules = self._extract_rules(requirements_text)

        # Generar pasos
        steps = self._generate_steps(project_name, entities, business_rules, output_path)

        plan = DevelopmentPlan(
            id=f"PLAN-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            project_name=project_name,
            created_at=datetime.now().isoformat(),
            requirements=requirements,
            steps=steps,
            entities=entities,
            business_rules=business_rules,
            total_steps=len(steps),
        )

        return plan

    def _parse_requirements(self, text: str) -> List[Requirement]:
        """Extrae requerimientos individuales del texto."""
        reqs = []
        lines = [l.strip() for l in text.split("\n") if l.strip()]

        for i, line in enumerate(lines, 1):
            # Detectar tipo
            line_lower = line.lower()
            if any(w in line_lower for w in ["segur", "password", "auth", "permiso", "owasp"]):
                req_type = "security"
            elif any(w in line_lower for w in ["rápid", "rendimiento", "carga"]):
                req_type = "performance"
            elif any(w in line_lower for w in ["interfaz", "pantalla", "botón", "formulario"]):
                req_type = "ux"
            else:
                req_type = "functional"

            # Detectar prioridad
            if any(w in line_lower for w in ["debe", "obligatori", "siempre", "nunca"]):
                priority = "must"
            elif any(w in line_lower for w in ["debería", "important"]):
                priority = "should"
            else:
                priority = "could"

            reqs.append(Requirement(
                id=f"REQ-{i:03d}",
                description=line.lstrip("- •*"),
                type=req_type,
                priority=priority,
            ))

        return reqs

    def _extract_entities(self, text: str) -> List[Dict]:
        """Extrae entidades del dominio."""
        text_lower = text.lower()
        entities = []

        entity_map = {
            "reserva": {"name": "Reservation", "fields": ["fecha", "hora", "personas", "nombre_cliente", "estado", "mesa_id"]},
            "mesa": {"name": "Table", "fields": ["numero", "capacidad", "ubicacion", "estado"]},
            "cliente": {"name": "Client", "fields": ["nombre", "email", "telefono"]},
            "pedido": {"name": "Order", "fields": ["items", "total", "estado", "fecha", "cliente_id"]},
            "producto": {"name": "Product", "fields": ["nombre", "precio", "stock", "categoria"]},
            "usuario": {"name": "User", "fields": ["nombre", "email", "password_hash", "rol", "activo"]},
            "expediente": {"name": "Case", "fields": ["numero", "titulo", "estado", "cliente_id", "fecha_apertura"]},
            "tarea": {"name": "Task", "fields": ["titulo", "descripcion", "estado", "prioridad", "fecha_limite"]},
            "receta": {"name": "Recipe", "fields": ["nombre", "ingredientes", "porciones", "tiempo_minutos"]},
            "factura": {"name": "Invoice", "fields": ["numero", "monto", "estado", "fecha", "cliente_id"]},
        }

        # Siempre incluir User
        entities.append(entity_map["usuario"])

        for keyword, entity in entity_map.items():
            if keyword in text_lower and entity not in entities:
                entities.append(entity)

        if len(entities) == 1:
            entities.append({"name": "Item", "fields": ["nombre", "descripcion", "estado"]})

        return entities

    def _extract_rules(self, text: str) -> List[str]:
        """Extrae reglas de negocio del texto."""
        rules = []
        lines = text.split("\n")

        for line in lines:
            line_stripped = line.strip().lstrip("- •*")
            if not line_stripped:
                continue
            # Detectar reglas (contienen restricciones)
            if any(w in line_stripped.lower() for w in [
                "máximo", "mínimo", "no puede", "debe", "solo",
                "antes de", "después de", "si ", "cuando",
                "no se permite", "obligatorio", "horario"
            ]):
                rules.append(line_stripped)

        return rules if rules else ["Sin reglas de negocio específicas detectadas"]

    def _generate_steps(
        self, name: str, entities: List[Dict], rules: List[str], output: Path
    ) -> List[Step]:
        """Genera la secuencia de pasos del plan."""
        steps = []
        step_num = 1
        entity_names = [e["name"] for e in entities if e["name"] != "User"]
        entities_str = ", ".join(entity_names)
        rules_str = "\n".join(f"  - {r}" for r in rules)
        fields_detail = "\n".join(
            f"  {e['name']}: {', '.join(e['fields'])}"
            for e in entities
        )

        # ═══ PASO 1: Setup del proyecto ═══
        steps.append(Step(
            number=step_num,
            phase="setup",
            title="Crear estructura del proyecto",
            instructions=f"""Crea la estructura de directorios del proyecto '{name}':

```
{name}/
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   └── routers/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── unit/
├── features/
├── pyproject.toml
└── README.md
```

El pyproject.toml debe usar setuptools con dependencias:
fastapi, uvicorn, sqlalchemy, pydantic, python-jose, bcrypt, pytest, httpx

database.py debe configurar SQLAlchemy con SQLite y proveer get_db() como dependency.""",
            files_to_create=["pyproject.toml", "api/__init__.py", "api/main.py", "api/database.py", "tests/__init__.py", "tests/conftest.py"],
            verification_criteria=["pyproject.toml existe", "api/database.py tiene get_db()", "estructura de directorios completa"],
            standards=["SOLID-DIP: database como dependencia inyectable", "OWASP-A05: sin secrets hardcoded"],
        ))
        step_num += 1

        # ═══ PASO 2: Modelos ═══
        steps.append(Step(
            number=step_num,
            phase="models",
            title="Implementar modelos de datos",
            instructions=f"""Crea api/models.py con los siguientes modelos SQLAlchemy:

Entidades:
{fields_detail}

Requisitos:
- Cada modelo hereda de Base (declarative_base)
- Todos tienen campo 'id' (Integer, primary_key, autoincrement)
- Todos tienen campo 'eliminado' (Boolean, default=False) para soft delete
- User.password_hash es String(255) — NUNCA guardar password en texto plano (OWASP A02)
- Usar tipos correctos: String(255), Integer, Float, Boolean, Text, JSON
- Agregar relaciones ForeignKey donde corresponda""",
            files_to_create=["api/models.py"],
            verification_criteria=["Todos los modelos tienen campo 'id'", "Todos tienen 'eliminado'", "User tiene 'password_hash' no 'password'"],
            standards=["OWASP-A02: password hasheado", "SOLID-SRP: solo definición de datos"],
            depends_on=[1],
        ))
        step_num += 1

        # ═══ PASO 3: Schemas ═══
        steps.append(Step(
            number=step_num,
            phase="schemas",
            title="Crear schemas Pydantic (contratos de datos)",
            instructions=f"""Crea schemas Pydantic para cada entidad en api/schemas/:

Para cada entidad ({entities_str}) crea:
- {{Entity}}Create: campos para CREAR (sin id, sin eliminado)
- {{Entity}}Response: campos que se RETORNAN (con id, sin password_hash)
- {{Entity}}Update: campos OPCIONALES para modificar

Requisitos (SOLID ISP — Interface Segregation):
- Un schema por operación (no un "God Schema" que sirve para todo)
- Usar model_config = ConfigDict(from_attributes=True) en Response
- Validaciones Pydantic: min_length, max_length donde corresponda
- NUNCA exponer password_hash en Response (OWASP A02)""",
            files_to_create=[f"api/schemas/{e['name'].lower()}.py" for e in entities],
            verification_criteria=["Create no tiene campo 'id'", "Response no tiene 'password_hash'", "Update tiene campos Optional"],
            standards=["SOLID-ISP: interfaces separadas por operación", "OWASP-A02: no exponer datos sensibles"],
            depends_on=[2],
        ))
        step_num += 1

        # ═══ PASO 4: Repositories ═══
        steps.append(Step(
            number=step_num,
            phase="repositories",
            title="Implementar repositorios (acceso a datos)",
            instructions=f"""Crea un repository por entidad en api/repositories/:

Cada repository ({entities_str}) debe tener:
- __init__(self, db: Session) — recibe sesión inyectada (DIP)
- create(**kwargs) → Entity — persiste nuevo registro
- get_by_id(id: int) → Optional[Entity] — busca por ID (excluye eliminados)
- list_all() → List[Entity] — lista activos
- update(item, **kwargs) → Entity — actualiza campos
- soft_delete(item) → Entity — marca eliminado=True (NO borra físicamente)

Requisitos:
- SOLID DIP: recibe db como parámetro, no la crea
- SOLID SRP: solo acceso a datos, NO lógica de negocio
- Filtrar siempre por eliminado==False (soft delete)
- Usar SQLAlchemy ORM (NUNCA SQL crudo — OWASP A03)""",
            files_to_create=[f"api/repositories/{e['name'].lower()}_repository.py" for e in entities if e['name'] != 'User'],
            verification_criteria=["Recibe db en __init__", "Filtra por eliminado==False", "No usa SQL crudo"],
            standards=["SOLID-DIP: dependencia inyectada", "SOLID-SRP: solo persistencia", "OWASP-A03: ORM anti-injection"],
            depends_on=[2],
        ))
        step_num += 1

        # ═══ PASO 5: Services con lógica de negocio ═══
        steps.append(Step(
            number=step_num,
            phase="services",
            title="Implementar servicios con LÓGICA DE NEGOCIO",
            instructions=f"""Crea un service por entidad en api/services/:

Cada service coordina la lógica de negocio. Aquí van las REGLAS:

Reglas de negocio a implementar:
{rules_str}

Estructura de cada service:
- __init__(self, db: Session) — crea internamente el Repository
- create(data: EntityCreate) → EntityResponse
- get_by_id(id) → Optional[EntityResponse]
- list_all() → List[EntityResponse]
- update(id, data: EntityUpdate) → Optional[EntityResponse]
- delete(id) → bool

Requisitos:
- SOLID SRP: coordina lógica, NO accede a DB directamente (usa repository)
- Validar reglas de negocio ANTES de persistir
- Lanzar ValueError con mensaje CLARO si una regla no se cumple
- Lanzar HTTPException(404) si no encuentra el recurso""",
            files_to_create=[f"api/services/{e['name'].lower()}_service.py" for e in entities if e['name'] != 'User'],
            verification_criteria=["Usa Repository internamente", "Valida reglas de negocio", "Mensajes de error claros"],
            standards=["SOLID-SRP: lógica separada de persistencia", "UX: mensajes de error comprensibles"],
            depends_on=[3, 4],
        ))
        step_num += 1

        # ═══ PASO 6: Auth Service ═══
        steps.append(Step(
            number=step_num,
            phase="auth",
            title="Implementar autenticación segura (OWASP)",
            instructions=f"""Crea api/services/auth_service.py con autenticación COMPLETA:

Funcionalidades:
- register(nombre, email, password) → hashea con bcrypt, retorna user + token
- login(email, password) → verifica hash, retorna token JWT
- get_current_user(token) → decodifica JWT, retorna user

Seguridad OWASP obligatoria:
- A02: Password SIEMPRE hasheado con bcrypt (import bcrypt; bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
- A07: Mensaje GENÉRICO en login fallido ("Credenciales inválidas" — no revelar qué falló)
- A07: Bloqueo después de 5 intentos fallidos (campo intentos_fallidos en User)
- A05: SECRET_KEY desde os.environ (NUNCA hardcoded)
- JWT con expiración (24h)

Crea también api/routers/auth_router.py con:
- POST /auth/register
- POST /auth/login

Y una función get_current_user() que sirva como Depends() en los otros routers.""",
            files_to_create=["api/services/auth_service.py", "api/routers/auth_router.py"],
            verification_criteria=["Password hasheado con bcrypt", "Mensaje genérico en error", "JWT con expiración", "SECRET_KEY desde environ"],
            standards=["OWASP-A02: crypto", "OWASP-A07: auth failures", "OWASP-A05: no secrets hardcoded"],
            depends_on=[2],
        ))
        step_num += 1

        # ═══ PASO 7: Routers ═══
        steps.append(Step(
            number=step_num,
            phase="routers",
            title="Implementar endpoints REST con protección",
            instructions=f"""Crea un router por entidad en api/routers/:

Cada router ({entities_str}) debe tener:
- GET    /{{entidad}}s/        → Listar (requiere auth)
- POST   /{{entidad}}s/        → Crear (requiere auth)
- GET    /{{entidad}}s/{{id}}   → Obtener por ID (requiere auth)
- PATCH  /{{entidad}}s/{{id}}   → Actualizar (requiere auth)
- DELETE /{{entidad}}s/{{id}}   → Soft delete (requiere auth)

Requisitos:
- TODOS los endpoints requieren autenticación: current_user = Depends(get_current_user)
- Usar Service internamente (no Repository directo)
- Retornar 404 si no existe, 201 en creación, 204 en delete
- Manejar errores con HTTPException y mensajes claros

Actualiza api/main.py para registrar TODOS los routers con app.include_router().""",
            files_to_create=[f"api/routers/{e['name'].lower()}_router.py" for e in entities if e['name'] != 'User'],
            files_to_modify=["api/main.py"],
            verification_criteria=["Todos los endpoints requieren auth", "Usa Service no Repository", "404/201/204 correctos"],
            standards=["OWASP-A01: access control en cada endpoint", "REST: status codes correctos"],
            depends_on=[5, 6],
        ))
        step_num += 1

        # ═══ PASO 8: Tests ═══
        steps.append(Step(
            number=step_num,
            phase="tests",
            title="Implementar tests completos (TDD verification)",
            instructions=f"""Crea tests REALES que verifiquen todo el sistema:

tests/conftest.py:
- Fixture 'client': TestClient con DB en memoria (StaticPool)
- Fixture 'auth_headers': registra usuario + login + retorna headers con JWT

tests/unit/test_auth.py:
- test_register_success
- test_register_duplicate_email_fails
- test_login_success_returns_token
- test_login_wrong_password_generic_error
- test_password_not_stored_plain_text

tests/unit/test_{{entidad}}.py (para cada entidad):
- test_create_returns_201
- test_create_returns_id
- test_list_empty_returns_empty
- test_list_after_create_has_items
- test_get_existing_returns_200
- test_get_nonexistent_returns_404
- test_delete_returns_204
- test_deleted_not_in_list
- test_create_without_auth_returns_401
- Tests de reglas de negocio específicas

Requisitos:
- TODOS los tests deben PASAR (no placeholders)
- Usar fixtures para evitar duplicación
- Tests de auth verifican OWASP (mensajes genéricos, hash)
- Tests de CRUD verifican reglas de negocio""",
            files_to_create=["tests/conftest.py", "tests/unit/test_auth.py"] + [f"tests/unit/test_{e['name'].lower()}.py" for e in entities if e['name'] != 'User'],
            verification_criteria=["Todos los tests PASAN", "Auth tests verifican OWASP", "CRUD tests verifican reglas de negocio"],
            standards=["TDD: tests verifican comportamiento", "OWASP: tests de seguridad incluidos"],
            depends_on=[7],
        ))
        step_num += 1

        # ═══ PASO 9: BDD Features ═══
        steps.append(Step(
            number=step_num,
            phase="bdd",
            title="Generar escenarios BDD (documentación ejecutable)",
            instructions=f"""Crea archivos .feature en Gherkin (español) para cada funcionalidad:

features/auth.feature:
- Registro exitoso, registro con email duplicado, login exitoso, login fallido, bloqueo

features/{{entidad}}.feature (para cada entidad):
- Crear exitosamente, crear sin datos falla, listar, buscar, eliminar, permisos

Reglas de negocio como escenarios:
{rules_str}

Requisitos:
- Lenguaje de NEGOCIO (no técnico)
- Cada escenario es independiente
- Cubrir: happy path + error + seguridad
- Background con "usuario autenticado" donde corresponda""",
            files_to_create=["features/auth.feature"] + [f"features/{e['name'].lower()}.feature" for e in entities if e['name'] != 'User'],
            verification_criteria=["Escenarios en español", "Cubren happy + error + seguridad", "Reglas de negocio incluidas"],
            standards=["BDD: especificación ejecutable", "ISO 9241: lenguaje comprensible"],
            depends_on=[7],
        ))
        step_num += 1

        # ═══ PASO 10: Dockerfile + Deploy ═══
        steps.append(Step(
            number=step_num,
            phase="deploy",
            title="Preparar para despliegue (Docker + config)",
            instructions=f"""Genera los archivos de deployment:

Dockerfile:
- Base: python:3.12-slim
- Instala dependencias desde pyproject.toml
- Expone puerto 8000
- CMD: uvicorn api.main:app --host 0.0.0.0 --port 8000

docker-compose.yml:
- Service: app (build desde Dockerfile)
- Ports: 8000:8000
- Environment: SECRET_KEY, DATABASE_URL

.env.example:
- SECRET_KEY=change-me-in-production
- DATABASE_URL=sqlite:///./app.db

README.md actualizado con:
- Descripción del proyecto
- Cómo instalar y correr
- Cómo correr tests
- Cómo desplegar con Docker
- Endpoints disponibles
- Estándares aplicados (SOLID, OWASP, BDD, TDD)""",
            files_to_create=["Dockerfile", "docker-compose.yml", ".env.example", "README.md"],
            verification_criteria=["Dockerfile construye", "docker-compose válido", "README completo"],
            standards=["OWASP-A05: secrets en .env no en código", "DevOps: reproducible"],
            depends_on=[8],
        ))

        return steps

    def get_step_instruction(self, plan: DevelopmentPlan) -> Optional[str]:
        """Retorna las instrucciones del paso actual formateadas para la IA."""
        step = plan.current_step_obj
        if step is None:
            return None

        standards_str = "\n".join(f"  - {s}" for s in step.standards) if step.standards else "  - Ninguno específico"
        criteria_str = "\n".join(f"  ✓ {c}" for c in step.verification_criteria)
        files_create = "\n".join(f"  + {f}" for f in step.files_to_create)
        files_modify = "\n".join(f"  ~ {f}" for f in step.files_to_modify) if step.files_to_modify else "  (ninguno)"

        return f"""
## 🔮 ARCANA ORCHESTRATOR — Paso {step.number}/{plan.total_steps}
### {step.title}
**Fase:** {step.phase} | **Progreso:** {plan.progress_percentage:.0f}%

---

### Instrucciones:

{step.instructions}

---

### Archivos a CREAR:
{files_create}

### Archivos a MODIFICAR:
{files_modify}

### Estándares que DEBE cumplir:
{standards_str}

### Criterios de verificación (Arcana validará esto):
{criteria_str}

---

⚠️ IMPORTANTE:
- Implementa EXACTAMENTE lo que se pide (ni más, ni menos)
- Cuando termines, llama a `orchestrator_verify` para que valide
- Si la verificación falla, recibirás instrucciones de corrección
"""
