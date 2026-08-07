import os
"""
🚨 CÓDIGO INTENCIONALMENTE MALO — Para demostración educativa.

Este archivo viola TODOS los estándares que Arcana enseña:
- SOLID: God Object con múltiples responsabilidades
- OWASP: SQL Injection, secrets hardcoded, debug mode
- TDD: Sin tests
- BDD: Sin especificación de comportamiento

NUNCA uses código como este en producción.
Arcana lo va a DESTROZAR. 😈
"""

import sqlite3
import smtplib

# OWASP A05: Secret hardcoded en código fuente
SECRET_KEY = os.environ.get("SECRET_KEY", "CHANGE-ME-IN-ENV")
API_KEY = os.environ.get("API_KEY", "CHANGE-ME-IN-ENV")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "")

# OWASP A05: Debug mode en producción
debug = False


# ARCANA-FIX [SRP]: Nombre 'AppManager' sugiere múltiples responsabilidades
# SUGERENCIA: Renombra para ser más específico o divide la clase.
# ARCANA-FIX [SRP]: Nombre 'AppManager' sugiere múltiples responsabilidades
# SUGERENCIA: Renombra para ser más específico o divide la clase.
class AppManager:
    """
    GOD OBJECT — Viola SRP, OCP, DIP, ISP.

    Esta clase hace TODO:
    - Autenticación
    - Gestión de usuarios
    - Gestión de tareas
    - Envío de emails
    - Reportes
    - Conexión a base de datos
    - Validación
    - Logging
    """

    def __init__(self):
        # OWASP A05 + SOLID DIP: Crea sus propias dependencias
        self.db = sqlite3.connect("production.db")
        self.email_server = smtplib.SMTP("mail.company.com")
        self.users = {}
        self.tasks = {}
        self.logs = []

    def register_user(self, name, email, password):
        """
        Viola:
        - OWASP A02: Password en texto plano
        - OWASP A03: SQL Injection
        - OWASP A07: Sin validación de password
        - OWASP A09: Sin logging
        - SOLID SRP: Hace registro + validación + email + DB
        """
        # Sin validación de email
        # Sin validación de password
        # Sin verificar si email ya existe

        # OWASP A03: SQL Injection — concatenación directa
        sql = f"INSERT INTO users (name, email, password) VALUES ('{name}', '{email}', '{password}')"
        self.db.execute(sql)
        self.db.commit()

        # OWASP A02: Password guardado en texto plano
        self.users[email] = {"name": name, "password": password}

        # Envío de email dentro del mismo método (SRP violation)
        try:
            self.email_server.sendmail(
                "noreply@app.com",
                email,
                f"Bienvenido {name}! Tu password es: {password}"
                # ↑ OWASP A02: ¡Envía el password por email en texto plano!
            )
        except Exception:
            pass  # Silencia errores (OWASP A09: sin logging)

    def login(self, email, password):
        """
        Viola:
        - OWASP A07: Sin rate limiting, sin bloqueo
        - OWASP A07: Mensajes que revelan información
        - SOLID SRP: Login + token + logging en un método
        """
        user = self.users.get(email)

        if user is None:
            # OWASP A07: Revela que el email NO existe
            return {"error": "Email no encontrado en el sistema"}

        if user["password"] != password:
            # OWASP A07: Revela que el PASSWORD es incorrecto (vs email)
            return {"error": "Contraseña incorrecta para este usuario"}

        # Token predecible (OWASP A02)
        token = f"token-{email}-{password}"
        return {"token": token, "message": "Login exitoso"}

    def get_task(self, task_id):
        """
        Viola:
        - OWASP A01: No verifica propiedad (cualquiera ve cualquier tarea)
        - OWASP A03: SQL Injection
        """
        # SQL Injection — el task_id podría ser "1 OR 1=1"
        sql = f"SELECT * FROM tasks WHERE id = {task_id}"
        result = self.db.execute(sql)
        return result.fetchone()

    def search_tasks(self, query):
        """
        Viola:
        - OWASP A03: SQL Injection masiva
        - OWASP A01: Sin filtro por usuario
        """
        # SUPER VULNERABLE: query podría ser "'; DROP TABLE tasks; --"
        sql = f"SELECT * FROM tasks WHERE title LIKE '%{query}%'"
        result = self.db.execute(sql)
        return result.fetchall()

    def delete_user(self, user_id):
        """
        Viola:
        - OWASP A01: Sin verificar permisos
        - Sin confirmación
        - Hard delete (no recuperable)
        - Sin auditoría
        """
        sql = f"DELETE FROM users WHERE id = {user_id}"
        self.db.execute(sql)
        self.db.commit()
        # No verifica si el solicitante tiene permisos
        # No registra quién borró a quién
        # No hay soft delete

    # ARCANA-FIX [SRP]: Método con 31 líneas (máx recomendado: 30)
    # SUGERENCIA: Extrae lógica a métodos privados o clases helper.
    # ARCANA-FIX [OCP]: Método con 7 condicionales — difícil de extender
    # SUGERENCIA: Reemplazar if/elif con Strategy Pattern o Registry
    # ARCANA-FIX [SRP]: Método con 31 líneas (máx recomendado: 30)
    # SUGERENCIA: Extrae lógica a métodos privados o clases helper.
    # ARCANA-FIX [OCP]: Método con 7 condicionales — difícil de extender
    # SUGERENCIA: Reemplazar if/elif con Strategy Pattern o Registry
    def generate_report(self, user_id, format, send_email=False):
        """
        Viola:
        - SOLID SRP: Genera + formatea + envía en un método
        - SOLID OCP: if/elif para cada formato (no extensible)
        """
        # Obtener datos (sin verificar permisos)
        data = self.db.execute(  # FIXME: SQL Injection — usar queries parametrizadas  # FIXME: SQL Injection — usar queries parametrizadas
            f"SELECT * FROM tasks WHERE user_id = {user_id}"
        ).fetchall()

        # OCP violation: if/elif infinito
        if format == "pdf":
            report = self._make_pdf(data)
        elif format == "html":
            report = self._make_html(data)
        elif format == "csv":
            report = self._make_csv(data)
        elif format == "json":
            report = self._make_json(data)
        elif format == "xml":
            report = self._make_xml(data)
        elif format == "xlsx":
            report = self._make_xlsx(data)
        else:
            report = str(data)

        if send_email:
            # Más responsabilidades mezcladas
            self.email_server.sendmail("reports@app.com", "user@mail.com", report)

        return report

    def _make_pdf(self, data):
        return f"PDF: {data}"

    def _make_html(self, data):
        return f"<html>{data}</html>"

    def _make_csv(self, data):
        return f"csv,{data}"

    def _make_json(self, data):
        return f'{{"data": "{data}"}}'

    def _make_xml(self, data):
        return f"<data>{data}</data>"

    def _make_xlsx(self, data):
        return f"xlsx:{data}"

    def fetch_external_data(self, url):
        """
        Viola:
        - OWASP A10: SSRF — URL sin validar
        - Sin timeout
        - Sin rate limiting
        """
        import requests
        # El usuario controla la URL — puede pedir recursos internos
        # FIXME: Validar URL contra allowlist antes de hacer request
        # FIXME: Validar URL contra allowlist antes de hacer request
        response = requests.get(url)
        return response.json()

    def validate_and_save_config(self, config_dict):
        """
        Viola:
        - SOLID SRP: Valida + guarda + notifica
        - SOLID DIP: Crea dependencias internamente
        - Sin validación real
        """
        # "Validación" que no valida nada
        if config_dict:
            # Guarda directamente sin sanitizar
            import json
            with open("config.json", "w") as f:
                json.dump(config_dict, f)
            # Notifica (otra responsabilidad)
            print(f"Config saved: {config_dict}")
