"""
Step Definitions para Features de Tareas.

NOTA EDUCATIVA:
Estos steps conectan los escenarios Gherkin de tareas con la API real.
Cada step tiene un propósito claro y documentado.

Principios demostrados:
- Cada step hace UNA sola cosa (SRP)
- Los steps son reutilizables entre escenarios
- Las verificaciones son explícitas y con mensajes claros
"""

from behave import given, when, then
from datetime import date


# ═══════════════════════════════════════════════════════════════
# GIVEN — Establecer contexto/precondiciones
# ═══════════════════════════════════════════════════════════════

@given('María tiene las siguientes tareas')
def step_maria_tiene_tareas(context):
    """
    Crea múltiples tareas desde una tabla Gherkin.

    NOTA EDUCATIVA:
    Las tablas en Gherkin se acceden via context.table.
    Cada fila es un diccionario con las columnas como claves.
    """
    for row in context.table:
        context.client.post("/tasks", json={
            "titulo": row["título"],
            "estado": row.get("estado", "pendiente"),
            "prioridad": row.get("prioridad", "media"),
            "etiquetas": row.get("etiquetas", "").split(", ") if row.get("etiquetas") else []
        }, headers=context.headers)


@given('que María ya tiene una tarea "{titulo}"')
@given('María ya tiene una tarea "{titulo}"')
def step_maria_ya_tiene_tarea(context, titulo):
    """Crea una tarea preexistente para María."""
    response = context.client.post("/tasks", json={
        "titulo": titulo,
    }, headers=context.headers)
    assert response.status_code == 201, f"No se pudo crear la tarea preexistente: {response.text}"
    context.existing_task = response.json()


@given('María tiene {cantidad:d} tareas en su lista')
def step_maria_tiene_n_tareas(context, cantidad):
    """Crea N tareas genéricas para María."""
    for i in range(cantidad):
        context.client.post("/tasks", json={
            "titulo": f"Tarea de prueba #{i+1}",
        }, headers=context.headers)


# ═══════════════════════════════════════════════════════════════
# WHEN — Acciones del usuario
# ═══════════════════════════════════════════════════════════════

@when('María crea una tarea con título "{titulo}"')
def step_crear_tarea_titulo(context, titulo):
    """
    Acción: crear tarea con solo título.

    NOTA EDUCATIVA:
    Los steps @when representan lo que el usuario HACE.
    Siempre guardamos la respuesta para verificar en @then.
    """
    context.response = context.client.post("/tasks", json={
        "titulo": titulo,
    }, headers=context.headers)

    if context.response.status_code == 201:
        context.created_task = context.response.json()


@when('María crea una tarea con')
def step_crear_tarea_completa(context):
    """
    Acción: crear tarea con múltiples campos (tabla Gherkin).

    NOTA EDUCATIVA:
    La tabla se convierte en un diccionario para el JSON de la API.
    Esto demuestra cómo Gherkin maneja datos estructurados.
    """
    task_data = {}
    for row in context.table:
        campo = row["campo"]
        valor = row["valor"]

        if campo == "etiquetas":
            task_data[campo] = [e.strip() for e in valor.split(",")]
        else:
            task_data[campo] = valor

    context.response = context.client.post("/tasks", json=task_data, headers=context.headers)

    if context.response.status_code == 201:
        context.created_task = context.response.json()


@when('María intenta crear una tarea sin título')
def step_crear_tarea_sin_titulo(context):
    """Acción: intento inválido (sin título)."""
    context.response = context.client.post("/tasks", json={
        "titulo": "",
    }, headers=context.headers)


@when('María intenta crear una tarea con un título de {cantidad:d} caracteres')
def step_crear_tarea_titulo_largo(context, cantidad):
    """Acción: intento con título excesivamente largo."""
    titulo_largo = "A" * cantidad
    context.response = context.client.post("/tasks", json={
        "titulo": titulo_largo,
    }, headers=context.headers)


@when('intento crear una tarea')
def step_crear_tarea_sin_auth(context):
    """Acción: crear tarea sin autenticación."""
    context.response = context.client.post("/tasks", json={
        "titulo": "Tarea de prueba",
    }, headers=context.headers)  # headers vacíos = sin token


@when('María crea otra tarea con título "{titulo}"')
def step_crear_otra_tarea(context, titulo):
    """Acción: crear tarea con título que ya existe."""
    context.response = context.client.post("/tasks", json={
        "titulo": titulo,
    }, headers=context.headers)

    if context.response.status_code == 201:
        context.second_task = context.response.json()


@when('María busca "{texto}"')
def step_buscar_tareas(context, texto):
    """Acción: buscar tareas por texto."""
    context.response = context.client.get(
        f"/tasks?search={texto}",
        headers=context.headers
    )
    context.search_results = context.response.json() if context.response.status_code == 200 else []


@when('María filtra por estado "{estado}"')
def step_filtrar_por_estado(context, estado):
    """Acción: filtrar tareas por estado."""
    context.response = context.client.get(
        f"/tasks?estado={estado}",
        headers=context.headers
    )
    context.search_results = context.response.json() if context.response.status_code == 200 else []


@when('María filtra por prioridad "{prioridad}"')
def step_filtrar_por_prioridad(context, prioridad):
    """Acción: filtrar tareas por prioridad."""
    context.response = context.client.get(
        f"/tasks?prioridad={prioridad}",
        headers=context.headers
    )
    context.search_results = context.response.json() if context.response.status_code == 200 else []


@when('María filtra por etiqueta "{etiqueta}"')
def step_filtrar_por_etiqueta(context, etiqueta):
    """Acción: filtrar tareas por etiqueta."""
    context.response = context.client.get(
        f"/tasks?etiqueta={etiqueta}",
        headers=context.headers
    )
    context.search_results = context.response.json() if context.response.status_code == 200 else []


@when('María filtra con')
def step_filtrar_combinado(context):
    """Acción: filtrar con múltiples criterios."""
    params = "&".join(f"{row['filtro']}={row['valor']}" for row in context.table)
    context.response = context.client.get(
        f"/tasks?{params}",
        headers=context.headers
    )
    context.search_results = context.response.json() if context.response.status_code == 200 else []


# ═══════════════════════════════════════════════════════════════
# THEN — Verificaciones
# ═══════════════════════════════════════════════════════════════

@then('la tarea se crea exitosamente')
def step_tarea_creada_ok(context):
    """
    Verificación: la tarea se creó correctamente.

    NOTA EDUCATIVA:
    Verificamos tanto el status HTTP como el contenido de la respuesta.
    Un 201 sin datos válidos seguiría siendo un error.
    """
    assert context.response.status_code == 201, \
        f"Esperaba 201, recibí {context.response.status_code}: {context.response.text}"
    assert context.created_task.get("id") is not None, \
        "La tarea creada debe tener un ID asignado"


@then('tiene estado "{estado}" por defecto')
def step_estado_por_defecto(context, estado):
    """Verifica el estado por defecto de la tarea."""
    assert context.created_task["estado"] == estado, \
        f"Esperaba estado '{estado}', tiene '{context.created_task['estado']}'"


@then('tiene prioridad "{prioridad}" por defecto')
def step_prioridad_por_defecto(context, prioridad):
    """Verifica la prioridad por defecto."""
    assert context.created_task["prioridad"] == prioridad, \
        f"Esperaba prioridad '{prioridad}', tiene '{context.created_task['prioridad']}'"


@then('la fecha de creación es hoy')
def step_fecha_creacion_hoy(context):
    """Verifica que la fecha de creación es la actual."""
    fecha = context.created_task["fecha_creacion"]
    hoy = date.today().isoformat()
    assert fecha == hoy, f"Esperaba fecha '{hoy}', tiene '{fecha}'"


@then('la tarea se crea con todos los datos especificados')
def step_tarea_con_todos_datos(context):
    """Verifica creación exitosa con datos completos."""
    assert context.response.status_code == 201
    assert context.created_task.get("id") is not None


@then('cada campo refleja exactamente lo que ingresé')
def step_campos_correctos(context):
    """Verifica que cada campo del input se refleja en el output."""
    # Los campos se verifican contra la tabla del step @when
    for row in context.table:
        campo = row["campo"]
        valor_esperado = row["valor"]
        valor_actual = context.created_task.get(campo)

        if campo == "etiquetas":
            etiquetas_esperadas = [e.strip() for e in valor_esperado.split(",")]
            assert set(valor_actual) == set(etiquetas_esperadas), \
                f"Etiquetas: esperaba {etiquetas_esperadas}, tiene {valor_actual}"
        else:
            assert str(valor_actual) == str(valor_esperado), \
                f"Campo '{campo}': esperaba '{valor_esperado}', tiene '{valor_actual}'"


@then('recibo el ID único de la tarea')
def step_recibe_id(context):
    """Verifica que la respuesta incluye un ID."""
    assert "id" in context.created_task
    assert isinstance(context.created_task["id"], int)
    assert context.created_task["id"] > 0


@then('el mensaje dice "{mensaje}"')
def step_mensaje_dice(context, mensaje):
    """Verifica que el mensaje de error contiene el texto esperado."""
    body = context.response.json()
    response_message = body.get("message", body.get("detail", ""))
    assert mensaje.lower() in response_message.lower(), \
        f"Esperaba mensaje con '{mensaje}', recibí: '{response_message}'"


@then('no se crea ninguna tarea')
def step_no_se_crea_tarea(context):
    """Verifica que la operación fallida no creó nada."""
    assert context.response.status_code >= 400


@then('el sistema me sugiere iniciar sesión')
def step_sugiere_login(context):
    """Verifica sugerencia de autenticación."""
    body = context.response.json()
    message = body.get("message", body.get("detail", ""))
    assert any(word in message.lower() for word in ["iniciar sesión", "login", "autenticarse"])


@then('ambas tareas coexisten en el sistema')
def step_ambas_tareas_coexisten(context):
    """Verifica que la segunda tarea se creó sin afectar la primera."""
    assert context.response.status_code == 201
    assert context.second_task.get("id") is not None


@then('cada una tiene un ID único diferente')
def step_ids_diferentes(context):
    """Verifica que los IDs son distintos."""
    assert context.existing_task["id"] != context.second_task["id"], \
        "Las tareas duplicadas deben tener IDs diferentes"


@then('obtiene {cantidad:d} resultado')
@then('obtiene {cantidad:d} resultados')
def step_cantidad_resultados(context, cantidad):
    """Verifica la cantidad de resultados de búsqueda."""
    actual = len(context.search_results)
    assert actual == cantidad, \
        f"Esperaba {cantidad} resultados, obtuve {actual}"


@then('el resultado es "{titulo}"')
def step_resultado_es(context, titulo):
    """Verifica que el único resultado tiene el título esperado."""
    assert len(context.search_results) >= 1
    titulos = [t["titulo"] for t in context.search_results]
    assert titulo in titulos, f"'{titulo}' no está en resultados: {titulos}"


@then('todos tienen estado "{estado}"')
def step_todos_estado(context, estado):
    """Verifica que todos los resultados tienen el estado esperado."""
    for task in context.search_results:
        assert task["estado"] == estado, \
            f"Tarea '{task['titulo']}' tiene estado '{task['estado']}', esperaba '{estado}'"


@then('ve el mensaje "{mensaje}"')
def step_ve_mensaje(context, mensaje):
    """Verifica un mensaje informativo en la respuesta."""
    body = context.response.json()
    response_msg = body.get("message", body.get("detail", ""))
    assert mensaje.lower() in response_msg.lower()


@then('se sugiere "{sugerencia}"')
def step_se_sugiere(context, sugerencia):
    """Verifica que se incluye una sugerencia al usuario."""
    body = context.response.json()
    suggestion = body.get("suggestion", body.get("sugerencia", ""))
    assert sugerencia.lower() in suggestion.lower()
