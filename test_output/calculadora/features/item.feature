# language: es
Característica: Gestión de Item
  Como usuario autenticado
  Quiero gestionar mis items
  Para organizar mi trabajo

  Escenario: Crear item exitosamente
    Dado un usuario autenticado
    Cuando crea un item con datos válidos
    Entonces el item se registra exitosamente
    Y recibe confirmación con el ID

  Escenario: Listar mis items
    Dado un usuario con items existentes
    Cuando consulta su lista
    Entonces ve solo sus propios items
    Y están ordenados por fecha

  Escenario: No puedo ver items de otro usuario
    Dado que otro usuario tiene items
    Cuando intento acceder a ellos
    Entonces recibo error 404
    Y no veo su contenido

  Escenario: Crear item sin datos obligatorios falla
    Dado un usuario autenticado
    Cuando intenta crear un item sin datos requeridos
    Entonces recibe un error de validación claro

  Escenario: Eliminar item requiere confirmación
    Dado un usuario con un item
    Cuando solicita eliminarlo
    Entonces el sistema realiza soft-delete
    Y el item es recuperable por 30 días
