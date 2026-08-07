"""
AuthService — Servicio de autenticación.

NOTA EDUCATIVA:
Este servicio implementa autenticación SEGURA según OWASP:
- A02: Contraseñas hasheadas con bcrypt (nunca texto plano)
- A07: Bloqueo por intentos fallidos (anti fuerza bruta)
- Mensajes genéricos (no revelan si el email existe)

Principios SOLID:
- SRP: Solo maneja autenticación (no tareas, no permisos)
- DIP: Recibe db como dependencia inyectada
"""

from datetime import datetime, timedelta
from typing import Dict, Optional

from sqlalchemy.orm import Session

from examples.taskflow.api.models import User


class AuthenticationError(Exception):
    """Error de credenciales inválidas (mensaje genérico por OWASP)."""
    pass


class AccountLockedError(Exception):
    """Cuenta bloqueada por intentos fallidos."""
    pass


class AuthService:
    """
    Servicio de autenticación segura.

    Implementa:
    - Registro con hash de contraseña
    - Login con verificación de hash
    - Bloqueo por intentos fallidos (OWASP A07)
    - Mensajes genéricos para no revelar información (OWASP)
    """

    MAX_FAILED_ATTEMPTS: int = 5
    LOCKOUT_MINUTES: int = 15

    def __init__(self, db: Session):
        self._db = db

    def register(
        self,
        nombre: str,
        email: str,
        password: str,
    ) -> Dict:
        """
        Registra un nuevo usuario.

        Args:
            nombre: Nombre completo
            email: Email único
            password: Contraseña (se hashea antes de guardar)

        Returns:
            Dict con datos del usuario creado

        Raises:
            ValueError: Si el email ya existe o datos inválidos
        """
        # Verificar email único
        existing = self._db.query(User).filter(User.email == email).first()
        if existing:
            raise ValueError("Este email ya está registrado")

        # Validar contraseña
        self._validate_password(password)

        # Hashear contraseña (OWASP A02)
        password_hash = self._hash_password(password)

        # Crear usuario
        user = User(
            nombre=nombre,
            email=email,
            password_hash=password_hash,
        )
        self._db.add(user)
        self._db.commit()
        self._db.refresh(user)

        return {
            "id": user.id,
            "nombre": user.nombre,
            "email": user.email,
            "message": "¡Bienvenido/a! Tu cuenta se ha creado exitosamente.",
        }

    def login(self, email: str, password: str) -> Dict:
        """
        Inicia sesión con credenciales.

        NOTA EDUCATIVA (OWASP):
        - El mensaje de error es SIEMPRE el mismo, no importa qué falló
        - Se registran intentos fallidos para bloqueo
        - Después de N intentos, la cuenta se bloquea temporalmente

        Returns:
            Dict con token JWT y datos del usuario

        Raises:
            AuthenticationError: Credenciales inválidas (mensaje genérico)
            AccountLockedError: Cuenta bloqueada por intentos fallidos
        """
        user = self._db.query(User).filter(User.email == email).first()

        # Si el usuario no existe, lanzamos el MISMO error (OWASP)
        if user is None:
            raise AuthenticationError("Credenciales inválidas")

        # Verificar si está bloqueado
        if self._is_account_locked(user):
            raise AccountLockedError(
                f"Cuenta bloqueada temporalmente. "
                f"Intenta nuevamente en {self.LOCKOUT_MINUTES} minutos."
            )

        # Verificar contraseña
        if not self._verify_password(password, user.password_hash):
            self._record_failed_attempt(user)
            # MISMO error que usuario inexistente (OWASP)
            raise AuthenticationError("Credenciales inválidas")

        # Login exitoso — reiniciar contador
        self._reset_failed_attempts(user)

        # Generar token
        token = self._generate_token(user)

        return {
            "token": token,
            "nombre": user.nombre,
            "email": user.email,
        }

    def _validate_password(self, password: str) -> None:
        """Valida requisitos de contraseña."""
        errors = []
        if len(password) < 8:
            errors.append("Mínimo 8 caracteres")
        if not any(c.isupper() for c in password):
            errors.append("Al menos una mayúscula")
        if not any(c.isdigit() for c in password):
            errors.append("Al menos un número")
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            errors.append("Al menos un carácter especial")

        if errors:
            raise ValueError(
                "La contraseña no cumple los requisitos: " + "; ".join(errors)
            )

    def _hash_password(self, password: str) -> str:
        """
        Hashea la contraseña con bcrypt.

        NOTA EDUCATIVA:
        bcrypt genera un salt aleatorio automáticamente.
        El hash resultante incluye el salt, así que no necesitas
        guardarlo por separado.
        """
        import bcrypt
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def _verify_password(self, password: str, password_hash: str) -> bool:
        """Verifica una contraseña contra su hash."""
        import bcrypt
        try:
            return bcrypt.checkpw(password.encode(), password_hash.encode())
        except Exception:
            return False

    def _is_account_locked(self, user: User) -> bool:
        """Verifica si la cuenta está bloqueada."""
        if user.bloqueado_hasta is None:
            return False
        return datetime.now() < user.bloqueado_hasta

    def _record_failed_attempt(self, user: User) -> None:
        """Registra un intento fallido y bloquea si excede el límite."""
        user.intentos_fallidos += 1

        if user.intentos_fallidos >= self.MAX_FAILED_ATTEMPTS:
            user.bloqueado_hasta = datetime.now() + timedelta(
                minutes=self.LOCKOUT_MINUTES
            )

        self._db.commit()

    def _reset_failed_attempts(self, user: User) -> None:
        """Reinicia el contador de intentos fallidos tras login exitoso."""
        user.intentos_fallidos = 0
        user.bloqueado_hasta = None
        self._db.commit()

    def _generate_token(self, user: User) -> str:
        """
        Genera un token JWT.

        NOTA EDUCATIVA:
        En producción usarías RS256 (asimétrico) y claims estándar.
        Aquí simplificamos para el ejemplo.
        """
        try:
            from jose import jwt
            payload = {
                "sub": str(user.id),
                "name": user.nombre,
                "email": user.email,
                "exp": datetime.now() + timedelta(hours=24),
            }
            return jwt.encode(payload, "secret-key-change-in-production", algorithm="HS256")
        except ImportError:
            # Fallback educativo
            import base64
            import json
            payload = {"sub": str(user.id), "name": user.nombre}
            return base64.b64encode(json.dumps(payload).encode()).decode()
