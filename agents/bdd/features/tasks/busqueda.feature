# language: es

Característica: Búsqueda y Filtrado de Tareas
  Como usuario con muchas tareas
  Quiero poder buscar y filtrar mi lista
  Para encontrar rápidamente lo que necesito

  Antecedentes:
    Dado un usuario autenticado "María García"
    Y María tiene las siguientes tareas:
      | título                    | estado     | prioridad | etiquetas        |
      | Revisar contrato legal    | pendiente  | alta      | legal, urgente   |
      | Preparar presentación     | en_proceso | media     | ventas           |
      | Comprar insumos oficina   | pendiente  | baja      | oficina          |
      | Informe financiero Q2     | completada | alta      | finanzas, Q2     |
      | Llamar al proveedor       | pendiente  | media     | compras          |

  Escenario: Buscar por texto en título
    Cuando María busca "contrato"
    Entonces obtiene 1 resultado
    Y el resultado es "Revisar contrato legal"

  Escenario: Filtrar por estado
    Cuando María filtra por estado "pendiente"
    Entonces obtiene 3 resultados
    Y todos tienen estado "pendiente"

  Escenario: Filtrar por prioridad
    Cuando María filtra por prioridad "alta"
    Entonces obtiene 2 resultados:
      | título                  |
      | Revisar contrato legal  |
      | Informe financiero Q2   |

  Escenario: Combinación de filtros
    Cuando María filtra con:
      | filtro    | valor     |
      | estado    | pendiente |
      | prioridad | alta      |
    Entonces obtiene 1 resultado
    Y el resultado es "Revisar contrato legal"

  Escenario: Búsqueda sin resultados muestra mensaje amigable
    Cuando María busca "vacaciones"
    Entonces obtiene 0 resultados
    Y ve el mensaje "No se encontraron tareas con ese criterio"
    Y se sugiere "Intenta con otros términos o revisa los filtros"

  Escenario: Filtrar por etiqueta
    Cuando María filtra por etiqueta "legal"
    Entonces obtiene 1 resultado
    Y el resultado es "Revisar contrato legal"
