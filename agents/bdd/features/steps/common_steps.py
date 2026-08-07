"""
Step Definitions Comunes — Pasos reutilizables entre features.

NOTA EDUCATIVA:
Los steps comunes evitan duplicación (DRY - Don't Repeat Yourself).
Se colocan aquí para que cualquier feature pueda usarlos.

Ejemplo: "Given un usuario autenticado" se usa en TODAS las features
de tareas, así que vive aquí en vez de repetirse en cada archivo.
"""

from behave import given, then


@given('un usuario autenticado "{nombre}"')
def step_usuario_autenticado(context, nombre):
    """
    Crea y autentica un usuario de prueba.

    Este step:
    1. Registra al usuario (si no existe)
    2. Obtiene un token JWT
    3. Guarda el token en context para los steps siguientes

    NOTA EDUCATIVA:
    El 'context' de behave es como una mochila que llevas entre steps.
    Lo que guardas en un @given, lo puedes usar en @when y @then.
    """
    email = f"{nombre.lower().replace(' ', '.')}@test.com"

    # Registrar
    context.client.post("/auth/register", json={
        "nombre": nombre,
        "email": email,
        "password": "TestPassword$123"
    })

    # Login
    response = context.client.post("/auth/login", json={
        "email": email,
        "password": "TestPassword$123"
    })

    context.auth_token = response.json().get("token")
    context.user_name = nombre
    context.user_email = email
    context.headers = {"Authorization": f"Bearer {context.auth_token}"}


@given('el sistema está operativo')
def step_sistema_operativo(context):
    """
    Verifica que el sistema está respondiendo.

    NOTA EDUCATIVA:
    Este step parece trivial, pero es importante:
    - Documenta una precondición explícita
    - Si el sistema no está levantado, falla aquí (no en steps posteriores)
    - Facilita debugging: sabes EXACTAMENTE dónde falló
    """
    response = context.client.get("/health")
    assert response.status_code == 200, "El sistema no está operativo"


@given('que no estoy autenticada')
@given('que no estoy autenticado')
def step_no_autenticado(context):
    """Asegura que no hay token de autenticación."""
    context.auth_token = None
    context.headers = {}


@then('recibe un mensaje de error claro')
@then('recibo un mensaje de error claro')
def step_mensaje_error_claro(context):
    """
    Verifica que el error es comprensible por el usuario.

    NOTA EDUCATIVA (ISO 9241 — Auto-descriptividad):
    Los errores deben ser claros, específicos y orientados a la acción.
    No "Error 422" sino "El título es obligatorio".
    """
    assert context.response.status_code >= 400
    body = context.response.json()
    assert "message" in body or "detail" in body, \
        "El error debe incluir un mensaje descriptivo"


@then('recibo un error de acceso denegado')
def step_error_acceso_denegado(context):
    """Verifica error 401 (no autenticado) o 403 (sin permisos)."""
    assert context.response.status_code in (401, 403), \
        f"Esperaba 401/403, recibí {context.response.status_code}"
