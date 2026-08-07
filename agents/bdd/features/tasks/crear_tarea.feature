# language: es

Característica: Creación de Tareas
  Como usuario autenticado de TaskFlow
  Quiero crear tareas con diferentes niveles de detalle
  Para organizar mi trabajo de forma flexible

  Antecedentes:
    Dado un usuario autenticado "María García"
    Y el sistema está operativo

  Escenario: Crear tarea con solo título (mínimo)
    Cuando María crea una tarea con título "Comprar insumos"
    Entonces la tarea se crea exitosamente
    Y tiene estado "pendiente" por defecto
    Y tiene prioridad "media" por defecto
    Y la fecha de creación es hoy

  Escenario: Crear tarea completa con todos los campos
    Cuando María crea una tarea con:
      | campo            | valor                                |
      | título           | Preparar informe trimestral          |
      | descripción      | Incluir métricas de ventas Q2 2026   |
      | prioridad        | alta                                 |
      | fecha_limite     | 2026-08-15                           |
      | etiquetas        | informe, ventas, Q2                  |
    Entonces la tarea se crea con todos los datos especificados
    Y cada campo refleja exactamente lo que ingresé
    Y recibo el ID único de la tarea

  Escenario: No puedo crear tarea sin título
    Cuando María intenta crear una tarea sin título
    Entonces recibe un mensaje de error claro
    Y el mensaje dice "El título es obligatorio"
    Y no se crea ninguna tarea

  Escenario: El título tiene un límite de caracteres
    Cuando María intenta crear una tarea con un título de 250 caracteres
    Entonces recibe un mensaje de error
    Y el mensaje dice "El título no puede exceder 200 caracteres"

  Escenario: No puedo crear tareas sin estar autenticada
    Dado que no estoy autenticada
    Cuando intento crear una tarea
    Entonces recibo un error de acceso denegado
    Y el sistema me sugiere iniciar sesión

  Escenario: Título duplicado es permitido
    Dado que María ya tiene una tarea "Revisar contrato"
    Cuando María crea otra tarea con título "Revisar contrato"
    Entonces ambas tareas coexisten en el sistema
    Y cada una tiene un ID único diferente
