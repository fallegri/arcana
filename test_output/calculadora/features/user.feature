# language: es
Característica: Autenticación de Usuarios
  Como usuario del sistema
  Quiero registrarme e iniciar sesión
  Para acceder a mis datos de forma segura

  Escenario: Registro exitoso
    Dado que soy un visitante nuevo
    Cuando me registro con datos válidos
    Entonces mi cuenta se crea exitosamente
    Y recibo un mensaje de bienvenida

  Escenario: Login exitoso
    Dado que soy un usuario registrado
    Cuando inicio sesión con credenciales correctas
    Entonces accedo al sistema
    Y recibo un token válido

  Escenario: Login fallido no revela información
    Dado que intento logearme con credenciales incorrectas
    Entonces recibo un error genérico
    Y el mensaje no revela si el email existe

  Escenario: Bloqueo por fuerza bruta
    Dado que fallo el login 5 veces consecutivas
    Entonces mi cuenta se bloquea temporalmente
