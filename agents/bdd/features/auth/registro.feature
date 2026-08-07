# language: es

Característica: Registro de Usuarios
  Como persona interesada en usar TaskFlow
  Quiero poder crear una cuenta
  Para gestionar mis tareas de forma segura

  Escenario: Registro exitoso con datos válidos
    Dado que soy un visitante nuevo del sistema
    Cuando me registro con:
      | campo    | valor                |
      | nombre   | María García         |
      | email    | maria@ejemplo.com    |
      | password | MiClave$egura2026    |
    Entonces mi cuenta se crea exitosamente
    Y recibo un mensaje de bienvenida
    Y puedo iniciar sesión inmediatamente

  Escenario: No puedo registrarme con email ya existente
    Dado que ya existe un usuario con email "maria@ejemplo.com"
    Cuando intento registrarme con email "maria@ejemplo.com"
    Entonces recibo un error indicando "Este email ya está registrado"
    Y no se crea una cuenta duplicada

  Escenario: La contraseña debe cumplir requisitos de seguridad
    Dado que soy un visitante nuevo del sistema
    Cuando intento registrarme con contraseña "123"
    Entonces recibo un error de validación
    Y el mensaje indica los requisitos:
      | requisito                          |
      | Mínimo 8 caracteres               |
      | Al menos una mayúscula            |
      | Al menos un número                |
      | Al menos un carácter especial     |

  Esquema del escenario: Validación de formato de email
    Dado que soy un visitante nuevo del sistema
    Cuando intento registrarme con email "<email>"
    Entonces recibo un error indicando "Formato de email inválido"

    Ejemplos:
      | email              |
      | sin-arroba.com     |
      | @sin-usuario.com   |
      | espacios @mail.com |
      |                    |
