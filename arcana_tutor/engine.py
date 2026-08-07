"""
Tutor Engine — Motor de enseñanza interactiva.

Genera retos, evalúa soluciones, da pistas progresivas.

Personalidad: Profesor paciente.
"Casi lo tenés. Fijate en la línea 12..."
"""

import sys
import hashlib
from pathlib import Path
from typing import Dict, List, Optional

sys.path.insert(0, str(Path(__file__).parent.parent))


# ═══════════════════════════════════════════════════════════════
# BANCO DE RETOS
# ═══════════════════════════════════════════════════════════════

CHALLENGES = {
    # ─── OWASP ───
    "owasp_beginner_a02": {
        "id": "CH-OWASP-001",
        "topic": "owasp", "subtopic": "A02", "level": "beginner",
        "title": "El Password Desnudo",
        "description": (
            "Este código guarda la contraseña del usuario en TEXTO PLANO.\n"
            "  Un atacante que acceda a la base de datos vería todas las contraseñas.\n\n"
            "  Tu misión: Haz que el password se guarde como HASH (irreversible)."
        ),
        "bad_code": '''class UserService:
    def register(self, email, password):
        user = User(
            email=email,
            password=password  # ← ¡TEXTO PLANO!
        )
        self.db.add(user)
        self.db.commit()
        return user''',
        "good_code": '''import bcrypt

class UserService:
    def register(self, email, password):
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User(
            email=email,
            password_hash=password_hash  # ← HASH irreversible
        )
        self.db.add(user)
        self.db.commit()
        return user''',
        "hints": [
            "¿Qué pasa si alguien roba la base de datos? ¿Puede leer las contraseñas?",
            "Busca 'bcrypt' — es la librería para hashear passwords.",
            "El campo debería llamarse 'password_hash', no 'password'. Y su valor NO debe ser el password original.",
        ],
        "evaluation_criteria": [
            "password_no_plain",  # No guarda password en texto plano
            "uses_hashing",       # Usa alguna función de hash
            "field_renamed",      # Campo se llama password_hash (no password)
        ],
    },
    "owasp_beginner_a03": {
        "id": "CH-OWASP-002",
        "topic": "owasp", "subtopic": "A03", "level": "beginner",
        "title": "La Inyección Mortal",
        "description": (
            "Este código construye SQL concatenando el input del usuario.\n"
            "  Un atacante puede escribir SQL malicioso y BORRAR toda tu base de datos.\n\n"
            "  Tu misión: Reescribe usando SQLAlchemy ORM (queries seguras)."
        ),
        "bad_code": '''def search_users(self, query):
    sql = f"SELECT * FROM users WHERE name LIKE '%{query}%'"
    result = self.db.execute(sql)
    return result.fetchall()

# Un atacante puede enviar: query = "'; DROP TABLE users; --"
# Y tu SQL se convierte en:
# SELECT * FROM users WHERE name LIKE '%'; DROP TABLE users; --%'
# ← ¡BORRA LA TABLA!''',
        "good_code": '''def search_users(self, query):
    # SQLAlchemy NUNCA concatena strings en SQL
    # El input siempre se trata como DATO, nunca como instrucción
    return (
        self.db.query(User)
        .filter(User.name.contains(query))
        .all()
    )''',
        "hints": [
            "El problema es la f-string. El 'query' del usuario se MEZCLA con el SQL.",
            "SQLAlchemy ORM genera queries parametrizadas automáticamente. Usa .filter() en vez de SQL crudo.",
            "self.db.query(User).filter(User.name.contains(query)).all() — esto es seguro.",
        ],
        "evaluation_criteria": [
            "no_fstring_sql",    # No usa f-string para SQL
            "no_string_concat",  # No concatena strings en SQL
            "uses_orm",          # Usa ORM o queries parametrizadas
        ],
    },
    "owasp_beginner_a05": {
        "id": "CH-OWASP-003",
        "topic": "owasp", "subtopic": "A05", "level": "beginner",
        "title": "Los Secretos a la Vista",
        "description": (
            "Este código tiene secrets (API keys, passwords) hardcoded.\n"
            "  Si subes esto a GitHub, CUALQUIERA puede ver tus credenciales.\n\n"
            "  Tu misión: Mueve los secrets a variables de entorno."
        ),
        "bad_code": '''import requests

SECRET_KEY = "sk-proj-abc123456789"
DB_PASSWORD = "admin123"
API_URL = "https://api.openai.com/v1/chat"

def call_api(prompt):
    headers = {"Authorization": f"Bearer {SECRET_KEY}"}
    response = requests.post(API_URL, headers=headers, json={"prompt": prompt})
    return response.json()''',
        "good_code": '''import os
import requests

SECRET_KEY = os.environ.get("SECRET_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
API_URL = os.environ.get("API_URL", "https://api.openai.com/v1/chat")

def call_api(prompt):
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY not configured in environment")
    headers = {"Authorization": f"Bearer {SECRET_KEY}"}
    response = requests.post(API_URL, headers=headers, json={"prompt": prompt})
    return response.json()''',
        "hints": [
            "Los valores entre comillas que parecen credenciales NO deberían estar en el código.",
            "Usa os.environ.get('NOMBRE_VARIABLE') para leer del entorno.",
            "import os; SECRET_KEY = os.environ.get('SECRET_KEY') — y el valor real va en un archivo .env",
        ],
        "evaluation_criteria": [
            "no_hardcoded_secrets",  # No hay strings que parezcan secrets
            "uses_environ",          # Usa os.environ o similar
            "handles_missing",       # Maneja el caso de variable no definida
        ],
    },
    # ─── SOLID ───
    "solid_beginner_srp": {
        "id": "CH-SOLID-001",
        "topic": "solid", "subtopic": "SRP", "level": "beginner",
        "title": "El Dios Objeto",
        "description": (
            "Esta clase hace DEMASIADAS cosas: valida, guarda, envía email y genera reportes.\n"
            "  Si cambias la validación, arriesgas romper el envío de email.\n\n"
            "  Tu misión: Separa en al menos 2 clases, cada una con UNA responsabilidad."
        ),
        "bad_code": '''class OrderManager:
    def process_order(self, order):
        # Valida
        if order.total <= 0:
            raise ValueError("Total inválido")
        if not order.email:
            raise ValueError("Email requerido")

        # Guarda en DB
        self.db.add(order)
        self.db.commit()

        # Envía confirmación
        self.send_email(order.email, f"Pedido {order.id} confirmado")

        # Genera reporte
        self.generate_pdf(order)

    def send_email(self, to, message):
        # ... 20 líneas de lógica de email ...
        pass

    def generate_pdf(self, order):
        # ... 30 líneas de generación PDF ...
        pass''',
        "good_code": '''class OrderValidator:
    """SRP: Solo valida."""
    def validate(self, order):
        if order.total <= 0:
            raise ValueError("Total inválido")
        if not order.email:
            raise ValueError("Email requerido")

class OrderRepository:
    """SRP: Solo persiste."""
    def save(self, order):
        self.db.add(order)
        self.db.commit()

class OrderService:
    """SRP: Solo coordina."""
    def __init__(self, validator, repository):
        self.validator = validator
        self.repository = repository

    def process_order(self, order):
        self.validator.validate(order)
        self.repository.save(order)
        # Email y PDF serían otros servicios inyectados''',
        "hints": [
            "Cuenta cuántas 'razones para cambiar' tiene esta clase. Si son más de 1, viola SRP.",
            "Piensa: ¿qué pasa si cambias cómo se envían emails? ¿Tienes que tocar la lógica de pedidos?",
            "Crea una clase para validar, otra para guardar. El OrderManager solo COORDINA.",
        ],
        "evaluation_criteria": [
            "multiple_classes",     # Más de 1 clase
            "separated_concerns",   # Validación separada de persistencia
            "coordinator_pattern",  # Una clase coordina, las otras hacen el trabajo
        ],
    },
    "solid_intermediate_ocp": {
        "id": "CH-SOLID-002",
        "topic": "solid", "subtopic": "OCP", "level": "intermediate",
        "title": "El if/elif Infinito",
        "description": (
            "Este código usa if/elif para cada formato de reporte.\n"
            "  Si quieres agregar un formato nuevo, MODIFICAS esta función.\n\n"
            "  Tu misión: Rediseña para que agregar formatos NO requiera modificar código existente."
        ),
        "bad_code": '''def export_report(data, format):
    if format == "pdf":
        return generate_pdf(data)
    elif format == "html":
        return generate_html(data)
    elif format == "csv":
        return generate_csv(data)
    elif format == "json":
        return generate_json(data)
    elif format == "xml":
        return generate_xml(data)
    # ¿Quieres agregar Excel? Modificas AQUÍ (viola OCP)''',
        "good_code": '''# Registry pattern — abierto para extensión, cerrado para modificación
EXPORTERS = {}

def register_exporter(format_name):
    def decorator(func):
        EXPORTERS[format_name] = func
        return func
    return decorator

@register_exporter("pdf")
def export_pdf(data): ...

@register_exporter("html")
def export_html(data): ...

def export_report(data, format):
    exporter = EXPORTERS.get(format)
    if not exporter:
        raise ValueError(f"Formato no soportado: {format}")
    return exporter(data)

# Agregar Excel = solo agregar @register_exporter("xlsx") — SIN tocar export_report''',
        "hints": [
            "El problema es el if/elif: agregar un formato = modificar esta función.",
            "Piensa en un diccionario que mapee formato → función. Registras nuevos sin tocar el código.",
            "Patrón Registry: EXPORTERS = {'pdf': func_pdf, ...}; export_report usa EXPORTERS[format]",
        ],
        "evaluation_criteria": [
            "no_if_elif_chain",    # Eliminó la cadena de if/elif
            "extensible_design",   # Se puede agregar sin modificar
            "uses_mapping",        # Usa dict, registry o strategy
        ],
    },
}


class TutorEngine:
    """Motor del Tutor — Genera retos, evalúa, da pistas."""

    def generate_challenge(
        self,
        topic: str,
        level: str = "beginner",
        subtopic: Optional[str] = None,
        exercise_type: str = "fix_code",
        context: Optional[str] = None,
    ) -> Dict:
        """Genera un reto según los parámetros."""
        # Buscar reto que coincida
        key = f"{topic}_{level}_{subtopic}" if subtopic else f"{topic}_{level}"

        # Buscar match exacto o parcial
        challenge = None
        for k, v in CHALLENGES.items():
            if k.startswith(key) or (v["topic"] == topic and v["level"] == level):
                if subtopic is None or v.get("subtopic", "").lower() == subtopic.lower():
                    challenge = v
                    break

        if not challenge:
            # Fallback: primer reto del tema
            for k, v in CHALLENGES.items():
                if v["topic"] == topic:
                    challenge = v
                    break

        if not challenge:
            return {
                "id": "CH-000",
                "title": "Reto no disponible",
                "description": f"No hay retos para {topic}/{level}/{subtopic} aún.",
                "bad_code": "# No disponible",
                "hints_available": False,
            }

        return {
            "id": challenge["id"],
            "title": challenge["title"],
            "description": challenge["description"],
            "bad_code": challenge["bad_code"],
            "hints_available": len(challenge.get("hints", [])) > 0,
            "time_suggested": "15 minutos",
        }

    async def evaluate(self, challenge_id: str, student_code: str) -> Dict:
        """Evalúa la solución del alumno."""
        # Buscar el reto
        challenge = None
        for v in CHALLENGES.values():
            if v["id"] == challenge_id:
                challenge = v
                break

        if not challenge:
            return {"error": f"Challenge {challenge_id} not found", "score": 0, "max_score": 10}

        criteria = challenge.get("evaluation_criteria", [])
        good_code = challenge.get("good_code", "")
        score = 0
        feedback = []
        missing = []

        # Evaluar cada criterio
        code_lower = student_code.lower()

        for criterion in criteria:
            passed = self._check_criterion(criterion, student_code, challenge)
            if passed:
                score += 10 // len(criteria)
                feedback.append(self._criterion_feedback(criterion, True))
            else:
                missing.append(self._criterion_feedback(criterion, False))

        # Extra credit
        extra = []
        if "docstring" in student_code or '"""' in student_code:
            extra.append("Agregaste documentación — excelente práctica")
            score = min(10, score + 1)
        if "def test_" in student_code:
            extra.append("Incluiste tests — nivel profesional")
            score = min(10, score + 1)

        return {
            "score": min(10, score),
            "max_score": 10,
            "passed": score >= 7,
            "feedback": feedback,
            "missing": missing,
            "extra_credit": extra,
        }

    def get_hint(self, challenge_id: str, hint_level: int = 0) -> str:
        """Retorna una pista progresiva (sin resolver)."""
        for v in CHALLENGES.values():
            if v["id"] == challenge_id:
                hints = v.get("hints", [])
                if hints:
                    # Rotar pistas (la siguiente cada vez que pide)
                    idx = hint_level % len(hints)
                    return hints[idx]
                return "No hay pistas disponibles para este reto."
        return f"Reto {challenge_id} no encontrado."

    def get_solution(self, challenge_id: str) -> str:
        """Muestra la solución completa (solo cuando el alumno lo pide)."""
        for v in CHALLENGES.values():
            if v["id"] == challenge_id:
                return v.get("good_code", "Solución no disponible.")
        return f"Reto {challenge_id} no encontrado."

    def _check_criterion(self, criterion: str, code: str, challenge: Dict) -> bool:
        """Verifica un criterio de evaluación."""
        code_lower = code.lower()

        checks = {
            "password_no_plain": lambda: "password_hash" in code_lower or "hash" in code_lower,
            "uses_hashing": lambda: "bcrypt" in code_lower or "hash" in code_lower,
            "field_renamed": lambda: "password_hash" in code_lower and "password=" not in code.replace("password_hash", ""),
            "no_fstring_sql": lambda: 'f"select' not in code_lower and "f'select" not in code_lower,
            "no_string_concat": lambda: "execute(f" not in code and 'execute(f' not in code,
            "uses_orm": lambda: ".query(" in code or ".filter(" in code or "contains(" in code,
            "no_hardcoded_secrets": lambda: not any(s in code for s in ["sk-proj", "admin123", "abc123"]),
            "uses_environ": lambda: "os.environ" in code or "getenv" in code or "environ" in code,
            "handles_missing": lambda: "if not" in code or "raise" in code or "ValueError" in code,
            "multiple_classes": lambda: code.count("class ") >= 2,
            "separated_concerns": lambda: code.count("class ") >= 2 and ("Validator" in code or "Repository" in code or "Service" in code),
            "coordinator_pattern": lambda: "self.validator" in code or "self.repository" in code or "self._" in code,
            "no_if_elif_chain": lambda: code.count("elif") <= 1,
            "extensible_design": lambda: "dict" in code_lower or "registry" in code_lower or "register" in code_lower or "EXPORTERS" in code,
            "uses_mapping": lambda: "{" in code and "}" in code and ("format" in code_lower or "export" in code_lower),
        }

        checker = checks.get(criterion)
        if checker:
            return checker()
        return False

    def _criterion_feedback(self, criterion: str, passed: bool) -> str:
        """Genera feedback legible para un criterio."""
        messages = {
            "password_no_plain": ("Password hasheado correctamente", "Todavía guardas el password en texto plano"),
            "uses_hashing": ("Usas función de hash (bcrypt)", "No detecté uso de hashing — prueba con bcrypt.hashpw()"),
            "field_renamed": ("Campo renombrado a password_hash", "El campo aún se llama 'password' — renómbralo a 'password_hash'"),
            "no_fstring_sql": ("No hay f-strings en SQL — bien", "Aún tienes f-string construyendo SQL — es vulnerable"),
            "no_string_concat": ("No concatenas strings en SQL", "Detecté concatenación de strings en SQL — usa ORM"),
            "uses_orm": ("Usas ORM/queries parametrizadas", "No detecté uso de ORM — prueba con .query().filter()"),
            "no_hardcoded_secrets": ("No hay secrets hardcoded", "Aún hay valores que parecen credentials en el código"),
            "uses_environ": ("Usas variables de entorno", "No detecté os.environ — mueve secrets al entorno"),
            "handles_missing": ("Manejas el caso de variable ausente", "¿Qué pasa si la variable de entorno no existe? Agrega verificación"),
            "multiple_classes": ("Separaste en múltiples clases (SRP)", "Solo hay 1 clase — necesitas dividir responsabilidades"),
            "separated_concerns": ("Responsabilidades separadas correctamente", "Las responsabilidades aún están mezcladas — crea Validator/Repository"),
            "coordinator_pattern": ("Patrón coordinador aplicado", "La clase principal debería DELEGAR, no hacer todo"),
            "no_if_elif_chain": ("Eliminaste la cadena if/elif", "Aún tienes if/elif — piensa en un dict/registry"),
            "extensible_design": ("Diseño extensible sin modificar", "Para agregar un formato, ¿necesitas modificar código? Eso viola OCP"),
            "uses_mapping": ("Usas mapping/diccionario para dispatch", "Prueba con un diccionario que mapee formato→función"),
        }
        msg = messages.get(criterion, ("Criterio cumplido", "Criterio no cumplido"))
        return msg[0] if passed else msg[1]
