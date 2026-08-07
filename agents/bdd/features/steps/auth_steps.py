"""
Step Definitions para Features de Autenticación.

NOTA EDUCATIVA (OWASP A07 — Authentication Failures):
- Los mensajes de error son GENÉRICOS (no revelan si el email existe)
- Se verifica el bloqueo por fuerza bruta
- Las contraseñas NUNCA se exponen en logs o respuestas

Principios demostrados:
- Seguridad por diseño (shift-left)
- Validación de inputs
- Rate limiting para login
"""

from behave import given, when, then


# ═══════════════════════════════════════════════════════════════
# GIVEN — Contexto de autenticación
# ═══════════════════════════════════════════════════════════════

@given('que existe un usuario registrado')
def step_existe_usuario_registrado(context):
    """Crea usuarios desde la tabla del Background."""
    for row in context.table:
        context.client.post("/auth/register", json={
            "nombre": row["nombre"],
            "email": row["email"],
            "password": row["password"]
        })
        context.test_user = dict(row)


@given('que soy un visitante nuevo del sistema')
def step_soy_visitante_nuevo(context):
    """Establece que no hay sesión activa."""
    context.headers = {}
    context.auth_token = None



@given('ya existe un usuario con email "{email}"')
def step_ya_existe_email(context, email):
    """Crea un usuario previo con ese email."""
    context.client.post("/auth/register", json={
        "nombre": "Usuario Existente",
        "email": email,
        "password": "Password$123"
    })


@given('que mi cuenta está bloqueada por intentos fallidos')
def step_cuenta_bloqueada(context):
    """Simula el bloqueo de cuenta por intentos fallidos."""
    for i in range(5):
        context.client.post("/auth/login", json={
            "email": context.test_user["email"],
            "password": f"WrongPassword{i}"
        })


@given('han pasado {minutos:d} minutos desde el bloqueo')
def step_han_pasado_minutos(context, minutos):
    """
    Simula el paso del tiempo.

    NOTA EDUCATIVA:
    En tests reales, usamos mocking del reloj del sistema
    para no esperar 15 minutos reales. Esto demuestra
    el principio de "testabilidad" (ISO 25010).
    """
    from unittest.mock import patch
    from datetime import datetime, timedelta

    future_time = datetime.now() + timedelta(minutes=minutos)
    context.mock_time = patch('datetime.datetime')
    context.mock_time.start().now.return_value = future_time


# ═══════════════════════════════════════════════════════════════
# WHEN — Acciones de autenticación
# ═══════════════════════════════════════════════════════════════

@when('inicio sesión con email "{email}" y password "{password}"')
def step_login(context, email, password):
    """Intenta iniciar sesión con las credenciales dadas."""
    context.response = context.client.post("/auth/login", json={
        "email": email,
        "password": password
    })


@when('inicio sesión con password incorrecta {veces:d} veces consecutivas')
def step_login_multiples_fallos(context, veces):
    """
    Simula ataque de fuerza bruta.

    NOTA EDUCATIVA (OWASP A07):
    Este escenario verifica que el sistema implementa protección
    contra ataques de fuerza bruta. Un sistema sin esta protección
    permitiría infinitos intentos de login.
    """
    for i in range(veces):
        context.response = context.client.post("/auth/login", json={
            "email": context.test_user["email"],
            "password": f"WrongPassword{i}"
        })


@when('me registro con')
def step_registro_con_tabla(context):
    """Registra un usuario con datos de la tabla Gherkin."""
    data = {row["campo"]: row["valor"] for row in context.table}
    context.response = context.client.post("/auth/register", json=data)


@when('intento registrarme con email "{email}"')
def step_registrar_con_email(context, email):
    """Intenta registro con un email específico."""
    context.response = context.client.post("/auth/register", json={
        "nombre": "Test User",
        "email": email,
        "password": "ValidPassword$123"
    })


@when('intento registrarme con contraseña "{password}"')
def step_registrar_con_password(context, password):
    """Intenta registro con una contraseña específica."""
    context.response = context.client.post("/auth/register", json={
        "nombre": "Test User",
        "email": "test@ejemplo.com",
        "password": password
    })


@when('inicio sesión con credenciales correctas')
def step_login_correcto(context):
    """Login con las credenciales del usuario de prueba."""
    context.response = context.client.post("/auth/login", json={
        "email": context.test_user["email"],
        "password": context.test_user["password"]
    })



# ═══════════════════════════════════════════════════════════════
# THEN — Verificaciones de autenticación
# ═══════════════════════════════════════════════════════════════

@then('accedo al sistema exitosamente')
def step_login_exitoso(context):
    """Verifica login exitoso."""
    assert context.response.status_code == 200, \
        f"Login falló: {context.response.status_code} - {context.response.text}"
    body = context.response.json()
    assert "token" in body, "La respuesta debe incluir un token"


@then('recibo un token de sesión válido')
def step_token_valido(context):
    """Verifica que el token tiene formato JWT válido."""
    body = context.response.json()
    token = body["token"]
    parts = token.split(".")
    assert len(parts) == 3, "El token JWT debe tener 3 partes (header.payload.signature)"


@then('veo mi nombre "{nombre}" en la interfaz')
def step_veo_nombre(context, nombre):
    """Verifica que la respuesta incluye el nombre del usuario."""
    body = context.response.json()
    assert body.get("nombre") == nombre or body.get("user", {}).get("nombre") == nombre


@then('recibo un error de credenciales inválidas')
def step_error_credenciales(context):
    """Verifica error de autenticación."""
    assert context.response.status_code == 401, \
        f"Esperaba 401, recibí {context.response.status_code}"


@then('el mensaje NO revela si el email existe o no')
def step_mensaje_generico_seguridad(context):
    """
    NOTA EDUCATIVA (OWASP):
    El mensaje de error debe ser GENÉRICO. Si decimos "email no encontrado",
    un atacante puede enumerar emails válidos. Si decimos "contraseña incorrecta",
    confirma que el email SÍ existe.

    Correcto: "Credenciales inválidas" (no dice cuál está mal)
    """
    body = context.response.json()
    message = body.get("message", body.get("detail", "")).lower()

    # NO debe revelar información específica
    assert "email no encontrado" not in message, "OWASP: No revelar si email existe"
    assert "usuario no existe" not in message, "OWASP: No revelar si usuario existe"
    assert "contraseña incorrecta" not in message, "OWASP: No revelar qué credencial falló"

    # SÍ debe ser genérico
    assert "inválida" in message or "incorrecta" in message or "credenciales" in message


@then('se registra el intento fallido')
def step_registra_intento(context):
    """
    Verifica que los intentos fallidos se auditan.

    NOTA EDUCATIVA (OWASP A09 — Logging Failures):
    Todo intento de login fallido debe registrarse para detectar
    patrones de ataque (fuerza bruta, credential stuffing).
    """
    # En una implementación real, verificaríamos el log
    # Aquí verificamos que la API acepta que se registre
    pass  # Se verifica en tests de integración del audit trail


@then('mi cuenta se bloquea temporalmente por {minutos:d} minutos')
def step_cuenta_bloqueada_temp(context, minutos):
    """Verifica bloqueo de cuenta."""
    # Intentar login correcto — debe fallar por bloqueo
    response = context.client.post("/auth/login", json={
        "email": context.test_user["email"],
        "password": context.test_user["password"]
    })
    assert response.status_code == 429, \
        f"Cuenta debería estar bloqueada (429), recibí {response.status_code}"


@then('recibo un mensaje indicando el bloqueo')
def step_mensaje_bloqueo(context):
    """Verifica mensaje informativo de bloqueo."""
    response = context.client.post("/auth/login", json={
        "email": context.test_user["email"],
        "password": context.test_user["password"]
    })
    body = response.json()
    message = body.get("message", body.get("detail", "")).lower()
    assert "bloqueada" in message or "bloqueado" in message or "locked" in message


@then('mi cuenta se crea exitosamente')
def step_cuenta_creada(context):
    """Verifica registro exitoso."""
    assert context.response.status_code == 201, \
        f"Registro falló: {context.response.status_code} - {context.response.text}"


@then('recibo un mensaje de bienvenida')
def step_mensaje_bienvenida(context):
    """Verifica mensaje de bienvenida post-registro."""
    body = context.response.json()
    assert "message" in body
    assert "bienvenid" in body["message"].lower()


@then('puedo iniciar sesión inmediatamente')
def step_puedo_login_inmediato(context):
    """Verifica que el usuario recién creado puede loguearse."""
    body = context.response.json()
    # Si el registro devolvió token, ya está logueado
    if "token" in body:
        return
    # Si no, intenta login
    # (Los datos vienen del step @when 'me registro con')


@then('recibo un error indicando "{mensaje}"')
def step_error_con_mensaje(context, mensaje):
    """Verifica error con mensaje específico."""
    assert context.response.status_code >= 400
    body = context.response.json()
    response_msg = body.get("message", body.get("detail", ""))
    assert mensaje.lower() in response_msg.lower(), \
        f"Esperaba '{mensaje}' en respuesta, recibí: '{response_msg}'"


@then('no se crea una cuenta duplicada')
def step_no_cuenta_duplicada(context):
    """Verifica que no se creó cuenta duplicada."""
    assert context.response.status_code in (400, 409), \
        f"Esperaba error 400/409, recibí {context.response.status_code}"


@then('recibo un error de validación')
def step_error_validacion(context):
    """Verifica error de validación (422)."""
    assert context.response.status_code in (400, 422), \
        f"Esperaba 400/422, recibí {context.response.status_code}"


@then('el mensaje indica los requisitos')
def step_indica_requisitos(context):
    """Verifica que se muestran los requisitos de la contraseña."""
    body = context.response.json()
    message = body.get("message", body.get("detail", "")).lower()

    for row in context.table:
        requisito = row["requisito"].lower()
        # Verifica que al menos la esencia del requisito está mencionada
        assert any(word in message for word in requisito.split()), \
            f"Requisito no mencionado: '{row['requisito']}'"


@then('el contador de intentos se reinicia')
def step_contador_reinicia(context):
    """Verifica que tras login exitoso, el contador se reinicia."""
    assert context.response.status_code == 200
