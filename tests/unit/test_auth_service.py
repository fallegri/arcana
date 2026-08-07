"""
Tests Unitarios — AuthService (Autenticación)

DERIVADO DE: agents/bdd/features/auth/login.feature
CICLO TDD: Tests escritos ANTES de la implementación

OWASP A07 — Authentication Failures:
- Mensajes genéricos (no revelan información)
- Bloqueo por fuerza bruta
- Hash seguro de contraseñas
"""

import pytest


class TestRegister:
    """Tests de registro de usuarios."""

    def test_register_creates_user(self, auth_service):
        """Registro exitoso retorna datos del usuario."""
        result = auth_service.register(
            nombre="Ana López",
            email="ana@test.com",
            password="MiClave$123"
        )

        assert result["nombre"] == "Ana López"
        assert result["email"] == "ana@test.com"
        assert "id" in result

    def test_register_returns_welcome_message(self, auth_service):
        """Registro exitoso incluye mensaje de bienvenida."""
        result = auth_service.register(
            nombre="Ana", email="ana@test.com", password="Valid$123"
        )

        assert "bienvenid" in result["message"].lower()

    def test_register_duplicate_email_raises_error(self, auth_service):
        """Email duplicado es rechazado."""
        auth_service.register(
            nombre="Ana", email="ana@test.com", password="Valid$123"
        )

        with pytest.raises(ValueError, match="ya está registrado"):
            auth_service.register(
                nombre="Otra Ana", email="ana@test.com", password="OtraClave$1"
            )

    def test_register_weak_password_raises_error(self, auth_service):
        """Contraseña débil es rechazada."""
        with pytest.raises(ValueError, match="requisitos"):
            auth_service.register(
                nombre="Ana", email="ana@test.com", password="123"
            )


class TestLogin:
    """Tests de login — derivados del escenario BDD."""

    def test_login_correct_credentials_returns_token(
        self, auth_service, registered_user
    ):
        """Login exitoso retorna token."""
        result = auth_service.login(
            email=registered_user["email"],
            password=registered_user["password"]
        )

        assert "token" in result
        assert len(result["token"]) > 0

    def test_login_returns_user_name(self, auth_service, registered_user):
        """Login exitoso incluye nombre del usuario."""
        result = auth_service.login(
            email=registered_user["email"],
            password=registered_user["password"]
        )

        assert result["nombre"] == registered_user["nombre"]


class TestLoginSecurity:
    """
    Tests de seguridad OWASP — mensajes genéricos.

    NOTA EDUCATIVA:
    Estos tests verifican que el sistema NO da pistas a un atacante.
    """

    def test_wrong_password_generic_error(self, auth_service, registered_user):
        """Contraseña incorrecta → error genérico."""
        from examples.taskflow.api.services.auth_service import AuthenticationError

        with pytest.raises(AuthenticationError) as exc_info:
            auth_service.login(
                email=registered_user["email"],
                password="PasswordIncorrecta$1"
            )

        # OWASP: No dice "contraseña incorrecta"
        assert "credenciales inválidas" in str(exc_info.value).lower()

    def test_nonexistent_email_same_error(self, auth_service):
        """Email inexistente → MISMO error que password incorrecta."""
        from examples.taskflow.api.services.auth_service import AuthenticationError

        with pytest.raises(AuthenticationError) as exc_info:
            auth_service.login(
                email="noexiste@test.com",
                password="Cualquiera$1"
            )

        # MISMO mensaje (no revela que el email no existe)
        assert "credenciales inválidas" in str(exc_info.value).lower()

    def test_password_not_stored_plain_text(self, auth_service, test_db):
        """La contraseña NUNCA se guarda en texto plano (OWASP A02)."""
        from examples.taskflow.api.models import User

        auth_service.register(
            nombre="Ana", email="ana@test.com", password="MiClave$123"
        )

        user = test_db.query(User).filter_by(email="ana@test.com").first()
        assert user.password_hash != "MiClave$123"
        assert len(user.password_hash) > 20


class TestBruteForceProtection:
    """
    Tests de protección contra fuerza bruta (OWASP A07).

    Derivado de: 'Scenario: Bloqueo de cuenta tras múltiples intentos'
    """

    def test_account_locks_after_5_failures(self, auth_service, registered_user):
        """5 intentos fallidos → cuenta bloqueada."""
        from examples.taskflow.api.services.auth_service import (
            AccountLockedError,
            AuthenticationError,
        )

        # 5 intentos fallidos
        for i in range(5):
            with pytest.raises(AuthenticationError):
                auth_service.login(
                    email=registered_user["email"],
                    password=f"Wrong{i}$Pass"
                )

        # El 6to intento → AccountLockedError (incluso con password correcta)
        with pytest.raises(AccountLockedError, match="bloqueada"):
            auth_service.login(
                email=registered_user["email"],
                password=registered_user["password"]
            )

    def test_successful_login_resets_counter(self, auth_service, registered_user):
        """Login exitoso reinicia el contador de intentos."""
        from examples.taskflow.api.services.auth_service import AuthenticationError

        # 3 intentos fallidos
        for i in range(3):
            with pytest.raises(AuthenticationError):
                auth_service.login(
                    email=registered_user["email"],
                    password=f"Wrong{i}$Pass"
                )

        # Login exitoso (reinicia contador)
        result = auth_service.login(
            email=registered_user["email"],
            password=registered_user["password"]
        )
        assert "token" in result

        # Otros 4 intentos fallidos (NO bloquea porque se reinició)
        for i in range(4):
            with pytest.raises(AuthenticationError):
                auth_service.login(
                    email=registered_user["email"],
                    password=f"Wrong{i}$Pass"
                )

        # Aún NO está bloqueada (4 < 5)
        result = auth_service.login(
            email=registered_user["email"],
            password=registered_user["password"]
        )
        assert "token" in result
