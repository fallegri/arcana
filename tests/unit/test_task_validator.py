"""
Tests Unitarios — TaskValidator (Validación de Tareas)

NOTA EDUCATIVA:
Estos tests se ejecutan SIN base de datos.
Solo validan lógica de negocio pura.
Son los más RÁPIDOS (Fast de FIRST).

Demuestran que REFACTORIZAR la validación a su propia clase
permite testearla independientemente.
"""

import pytest


class TestValidateTitle:
    """Tests para validación de título."""

    def test_valid_title_returns_cleaned(self, task_validator):
        """Título válido se retorna limpio (sin espacios extra)."""
        result = task_validator.validate_title("  Mi tarea  ")
        assert result == "Mi tarea"

    def test_none_raises_error(self, task_validator):
        with pytest.raises(ValueError, match="obligatorio"):
            task_validator.validate_title(None)

    def test_empty_string_raises_error(self, task_validator):
        with pytest.raises(ValueError, match="obligatorio"):
            task_validator.validate_title("")

    def test_whitespace_only_raises_error(self, task_validator):
        with pytest.raises(ValueError, match="obligatorio"):
            task_validator.validate_title("   ")

    def test_too_short_raises_error(self, task_validator):
        with pytest.raises(ValueError, match="3"):
            task_validator.validate_title("AB")

    def test_too_long_raises_error(self, task_validator):
        with pytest.raises(ValueError, match="200"):
            task_validator.validate_title("X" * 201)

    def test_boundary_min_3_is_valid(self, task_validator):
        result = task_validator.validate_title("ABC")
        assert result == "ABC"

    def test_boundary_max_200_is_valid(self, task_validator):
        title = "Y" * 200
        result = task_validator.validate_title(title)
        assert result == title


class TestValidatePriority:
    """Tests para validación de prioridad."""

    @pytest.mark.parametrize("valid_priority", [
        "baja", "media", "alta", "urgente"
    ])
    def test_valid_priorities_pass(self, task_validator, valid_priority):
        result = task_validator.validate_priority(valid_priority)
        assert result == valid_priority

    def test_invalid_priority_raises_error(self, task_validator):
        with pytest.raises(ValueError, match="inválida"):
            task_validator.validate_priority("super_urgente")

    def test_empty_priority_raises_error(self, task_validator):
        with pytest.raises(ValueError):
            task_validator.validate_priority("")


class TestValidateState:
    """Tests para validación de estado."""

    @pytest.mark.parametrize("valid_state", [
        "pendiente", "en_proceso", "completada", "cancelada"
    ])
    def test_valid_states_pass(self, task_validator, valid_state):
        result = task_validator.validate_state(valid_state)
        assert result == valid_state

    def test_invalid_state_raises_error(self, task_validator):
        with pytest.raises(ValueError, match="inválido"):
            task_validator.validate_state("archivada")
