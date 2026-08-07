# language: es

Característica: Protección contra Saturación de API
  Como sistema que consume APIs externas
  Quiero controlar la tasa de requests
  Para no ser bloqueado ni generar costos excesivos

  Escenario: Rate limiting permite requests dentro del límite
    Dado que el límite configurado es 60 requests por minuto
    Y he realizado 50 requests en el último minuto
    Cuando realizo 1 request más
    Entonces el request se procesa normalmente
    Y recibo la respuesta esperada

  Escenario: Rate limiting encolda requests que exceden el límite
    Dado que el límite configurado es 60 requests por minuto
    Y he realizado 60 requests en el último minuto
    Cuando intento realizar 1 request más
    Entonces el request se pone en cola de espera
    Y recibo la respuesta después de esperar
    Y NO recibo un error

  Escenario: Circuit breaker se activa tras fallos consecutivos
    Dado que el umbral de fallos es 5
    Y la API externa ha fallado 5 veces consecutivas
    Cuando intento hacer un request
    Entonces el sistema NO contacta la API
    Y recibo un mensaje "Servicio temporalmente no disponible"
    Y el sistema reintentará automáticamente en 30 segundos

  Escenario: Circuit breaker se recupera cuando la API vuelve
    Dado que el circuit breaker está en estado "OPEN"
    Y han pasado 30 segundos desde la apertura
    Cuando el sistema prueba la API
    Y la API responde exitosamente
    Entonces el circuit breaker vuelve a estado "CLOSED"
    Y los requests se procesan normalmente

  Escenario: Presupuesto diario previene gastos excesivos
    Dado que el presupuesto diario es 10 dólares
    Y el gasto acumulado hoy es 9.50 dólares
    Cuando realizo un request que cuesta 0.60 dólares
    Entonces el request se rechaza
    Y recibo una alerta "Presupuesto diario alcanzado"
    Y el sistema sugiere "Continúa mañana o aumenta el límite"
