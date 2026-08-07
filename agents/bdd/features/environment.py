"""
Configuración Global de Behave — Setup y Teardown.

NOTA EDUCATIVA:
Este archivo es el "backstage" de los tests BDD.
Se ejecuta automáticamente:
- before_all: Una vez al inicio
- before_scenario: Antes de CADA escenario
- after_scenario: Después de CADA escenario
- after_all: Una vez al final

Esto garantiza que cada escenario empiece con un "lienzo limpio"
(principio de independencia de tests).
"""


def before_all(context):
    """
    Inicialización global.

    En un proyecto real aquí se levantaría:
    - La aplicación de test
    - La base de datos de test
    - El cliente HTTP
    """
    try:
        from fastapi.testclient import TestClient
        from examples.taskflow.api.main import create_app

        context.app = create_app(testing=True)
        context.client = TestClient(context.app)
    except ImportError:
        # Modo educativo: sin app real
        from unittest.mock import MagicMock
        context.client = MagicMock()
        context.app = None


def before_scenario(context, scenario):
    """
    Prepara estado limpio para cada escenario.

    NOTA EDUCATIVA:
    Cada escenario DEBE ser independiente. Si el Escenario A
    depende de que el Escenario B se ejecute primero, tienes
    un problema de diseño.

    Este hook garantiza independencia reiniciando el estado.
    """
    # Reset de estado
    context.auth_token = None
    context.headers = {}
    context.response = None
    context.created_task = None
    context.test_user = None
    context.search_results = []

    # Reset de base de datos (si aplica)
    try:
        from examples.taskflow.api.database import reset_test_db
        reset_test_db()
    except ImportError:
        pass


def after_scenario(context, scenario):
    """
    Limpieza post-escenario y logging de fallos.

    NOTA EDUCATIVA:
    Registrar detalles de escenarios fallidos es crucial para debugging.
    En producción esto iría a un sistema de logging estructurado.
    """
    if scenario.status == "failed":
        print(f"\n{'='*60}")
        print(f"❌ ESCENARIO FALLIDO: {scenario.name}")
        print(f"   Feature: {scenario.feature.name}")
        if context.response:
            print(f"   Último HTTP Status: {context.response.status_code}")
            try:
                print(f"   Response: {context.response.text[:300]}")
            except Exception:
                pass
        print(f"{'='*60}\n")


def after_all(context):
    """Limpieza final."""
    pass
