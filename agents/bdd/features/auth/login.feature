# language: es

Característica: Inicio de Sesión
  Como usuario registrado de TaskFlow
  Quiero iniciar sesión de forma segura
  Para acceder a mis tareas personales

  Antecedentes:
    Dado que existe un usuario registrado:
      | nombre | email             | password          |
      | María  | maria@ejemplo.com | MiClave$egura2026 |

  Escenario: Login exitoso con credenciales correctas
    Cuando inicio sesión con email "maria@ejemplo.com" y password "MiClave$egura2026"
    Entonces accedo al sistema exitosamente
    Y recibo un token de sesión válido
    Y veo mi nombre "María" en la interfaz

  Escenario: Login fallido con contraseña incorrecta
    Cuando inicio sesión con email "maria@ejemplo.com" y password "ClaveIncorrecta"
    Entonces recibo un error de credenciales inválidas
    Y el mensaje NO revela si el email existe o no
    Y se registra el intento fallido

  Escenario: Bloqueo de cuenta tras múltiples intentos fallidos
    Cuando inicio sesión con password incorrecta 5 veces consecutivas
    Entonces mi cuenta se bloquea temporalmente por 15 minutos
    Y recibo un mensaje indicando el bloqueo
    Y se envía una alerta de seguridad a mi email

  Escenario: Login exitoso después de esperar el tiempo de bloqueo
    Dado que mi cuenta está bloqueada por intentos fallidos
    Y han pasado 15 minutos desde el bloqueo
    Cuando inicio sesión con credenciales correctas
    Entonces accedo al sistema exitosamente
    Y el contador de intentos se reinicia
