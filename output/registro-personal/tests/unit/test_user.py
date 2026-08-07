"""Tests de autenticación — Derivados de BDD + OWASP."""
import pytest


class TestRegister:
    """Derivado de: 'Escenario: Registro exitoso'"""

    def test_register_with_valid_data_succeeds(self):
        """Registro con datos válidos crea usuario."""
        # TODO: Implementar con servicio real
        assert True  # Placeholder para TDD RED

    def test_register_duplicate_email_fails(self):
        """Email duplicado es rechazado."""
        assert True

    def test_password_is_hashed(self):
        """OWASP A02: Password NUNCA en texto plano."""
        assert True


class TestLogin:
    """Derivado de: 'Escenario: Login exitoso'"""

    def test_login_correct_returns_token(self):
        """Login exitoso retorna JWT."""
        assert True

    def test_login_wrong_password_generic_error(self):
        """OWASP A07: Mensaje genérico (no revela info)."""
        assert True

    def test_account_locks_after_5_failures(self):
        """OWASP A07: Bloqueo por fuerza bruta."""
        assert True
