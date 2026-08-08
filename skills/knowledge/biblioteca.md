<!-- Página 1 -->

# UNIVERSIDAD SANTO TOMÁS

## DESARROLLO DE UN SISTEMA DE BAJO COSTO PARA LA

## TENEDURÍA DE LIBROS EN LA PARROQUIA SANTUARIO

## SEÑOR DE LA SALUD UBICADA EN EL MUNICIPIO DE

## CHAGUANÍ

Realizado por

## Jhon Edilberto Rubio Carrillo

Proyecto de Grado presentado en cumplimiento del requisito para optar por el grado de Ingeniería Electrónica

Grupo de Investigación MEM (Modelado-Electrónica-Monitoreo) Facultad de Ingeniería Electrónica División de Ingenierías

## Julio de 2022

---

<!-- Página 2 -->

## DESARROLLO DE UN SISTEMA DE BAJO COSTO

## PARA LA TENEDURÍA DE LIBROS EN LA

## PARROQUIA SANTUARIO SEÑOR DE LA SALUD

## UBICADA EN EL MUNICIPIO DE CHAGUANÍ

Realizado por

## Jhon Edilberto Rubio Carrillo

Proyecto de Grado presentado en cumplimiento del requisito para optar por el grado de Ingeniería Electrónica

Dirigido por

## Darío Alejandro Segura Torres

Grupo de Investigación MEM (Modelado-Electrónica-Monitoreo) Facultad de Ingeniería Electrónica División de Ingenierías

## Julio de 2022

---

<!-- Página 3 -->

# Dedicatoria

Dedico este proyecto a mi madre, mis hermanas y mi sobrina, pues gracias a su apoyo hoy estoy a puertas de culminar mi carrera, asimismo se lo dedico a mi padre quien sé que desde el cielo también me ha brindado su apoyo y me ha guiado para salir adelante en todo lo que me he propuesto.

I

---

<!-- Página 4 -->

# Agradecimientos

Agradezco inmensamente a mis docentes, compañeros y demás personas que a lo largo de la carrera me brindarón su apoyo y ayuda, también quiero agradecer a mi director de tesis Darío Segura y al contador Juan Carlos Moreno por ayudarme a llevar a cabo este proyecto.

II

---

<!-- Página 5 -->

# Índice general

Dedicatoria I

Agradecimientos II

Resumen V

Introducción VI

1. Planteamiento del problema 1

2. Estado del arte 3

3. Justificación 5

4. Objetivos 6 4.1. Objetivo general . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6 4.2. Objetivos específicos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

5. Marco teórico 7 5.1. Sistemas de información . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 5.2. Pasos para la creación de un sistema de información . . . . . . . . . . . . . . . . . 8 5.3. Aplicación de los sistemas de información en la contabilidad . . . . . . . . . . . . 9 5.4. Software contable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 5.5. Características de un software contable . . . . . . . . . . . . . . . . . . . . . . . . 10 5.6. Marco legal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 5.7. Teneduría de libros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 5.8. Requerimientos del software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

6. Diseño 13 6.1. Descripción de la teneduría de libros . . . . . . . . . . . . . . . . . . . . . . . . . . 13 6.1.1. Libros principales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14 6.1.1.1. Libro diario . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14 6.1.1.2. Libro mayor y balance . . . . . . . . . . . . . . . . . . . . . . . . 14 6.1.2. Características de los libros . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 6.1.2.1. Características de los libros electrónicos . . . . . . . . . . . . . . 15 6.1.2.2. Prohibiciones en los libros físicos . . . . . . . . . . . . . . . . . . 16

III

---

<!-- Página 6 -->

IV

6.1.3. Paso a paso de la teneduría en el libro diario de la Parroquia . . . . . . . . 16 6.2. Levantamiento de requerimientos no funcionales . . . . . . . . . . . . . . . . . . . 17 6.2.1. Requerimientos no funcionales acordados para el sistema . . . . . . . . . 17 6.3. Diseño de la arquitectura del sistema . . . . . . . . . . . . . . . . . . . . . . . . . . 19 6.3.1. Diagrama estructural . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 6.3.2. Diagrama de despliegue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 6.3.3. Diagrama de casos de uso . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20 6.3.4. Diagrama relacional . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 6.3.5. Casos de uso . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

7. Resultados 26 7.1. Desarrollo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 7.2. Pruebas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 7.2.1. Pruebas realizadas por el desarrollador . . . . . . . . . . . . . . . . . . . . 37 7.2.2. Pruebas realizadas por el párroco . . . . . . . . . . . . . . . . . . . . . . . . 45 7.3. Implementación . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45 7.4. Características del software obtenido . . . . . . . . . . . . . . . . . . . . . . . . . . 48 7.4.1. Requisitos mínimos para la operación del sistema . . . . . . . . . . . . . . 48

8. Impacto social 50

9. Conclusiones 51

10. Trabajos futuros y recomendaciones 53

Anexos 54

Bibliografía 71

---

<!-- Página 7 -->

# Resumen

El presente proyecto se diseñó y desarrolló una aplicación de escritorio para llevar a cabo la teneduría de libros de una iglesia, el diseño se basó en el paradigma de programación orientado a objetos, en el cual se tuvo en cuenta cada una de las características o reglamentaciones que se tienen a la hora de llevar a cabo los libros contables, del mismo modo el desarrollo de la aplicación estuvo basado en el paradigma orientado a objetos. Posteriormente se verifico el correcto funcionamiento de la aplicación mediante las pruebas de usuario basadas en datos reales, obteniendo así una aplicación que cumple con las características necesarias para ser catalogada como una buena herramienta. Finalmente, la aplicación se deja a disposición del párroco para su uso o futuras mejoras.

V

---

<!-- Página 8 -->

# Introducción

Con el pasar de los años la organización de las entidades en el país ha tendido a ser más com- pleja, por lo que se ha requerido diseñar nuevas herramientas para ayudar a manejar esta acti- vidad. Es allí donde nacen los sistemas de información, los cuales son aplicables en cada una de las áreas de dichas entidades pues con estos se genera el crecimiento de las mismas, dicho creci- miento se realiza mediante la obtención de información relevante que es usada para la correcta toma de decisiones. Ahora bien, una de las áreas de aplicación de los sistemas de información es la contable, donde este simplifica las tareas de dicha área, pues su función es procesar las transacciones teniendo en cuenta la información suministrada.

En la Parroquia del municipio de Chaguaní se lleva a cabo la teneduría de libros de forma física, proceso que si bien no es del todo tedioso debe ser de cuidado ya que allí se almacena información muy importante para la Parroquia. Por otro lado, el párroco actual cuenta con conocimientos contables por lo que el proceso de teneduría de libros de forma física para él no es un problema, sin embargo, se debe tener en cuenta que este párroco no estará siempre al mando de la Parroquia.

Al evidenciar esto nació la idea de crear un sistema el cual fuera de fácil manejo tanto para personas con conocimientos contables como para las que no los tengan. Con la creación de dicho sistema se facilitó y agilizo la teneduría de libros, permitiendo así la mejora de los tiempos en este proceso, también se garantiza de que el proceso se ha realizado correctamente.

El proyecto se realizó bajo metodología RUP a la cual se le realizó una modificación para adap- tarla al proyecto, dicha adaptación se compuso de 6 etapas donde la primera de ellas fue la búsqueda de información para comprender el proceso de teneduría de libros, seguidamente se realizó el levantamiento de requerimientos no funcionales de acuerdo a las necesidades de la Parroquia. Teniendo claro el proceso de teneduría se pasó a la etapa de diseño en donde se rea- lizaron los diagramas de casos de uso, despliegue, relacional y estructural, además se realizó el proceso de levantamiento de requerimientos funcionales. Posteriormente se pasó al desarrollo

VI

---

<!-- Página 9 -->

VII

del sistema el cual se desarrolló bajo la arquitectura 3 capas con el fin de generar un sistema mucho más ordenado y que solo proporcionara la información que le es útil a los usuarios. Finalmente se realizaron las pruebas de usuario y entrega del sistema, etapas en las cuales se obtuvo la aprobación por parte del párroco encargado.

---

<!-- Página 10 -->

# Capítulo 1

# Planteamiento del problema

En el año 2012 el Gobierno Nacional permitió que la teneduría de libros pudiera llevarse a cabo mediante opciones tecnológicas, esto con el fin de agilizar y facilitar el proceso de contabilidad que deben llevar las entidades anualmente, como se expone en [1]. Teniendo en cuenta esto, toda persona natural o jurídica que esté en la obligación de llevar contabilidad es libre de ha- cerlo de forma física o electrónica, la forma física acarrea varias desventajas, pues al ser de este tipo la persona que lleve a cabo dicho proceso debe ser muy cuidadosa con las operaciones que realiza ya que un error en un cálculo puede dañar todo el proceso previamente hecho, además al realizar la debida verificación del error se gastará más tiempo en esta actividad. Por otro lado según lo expuesto en el artículo 1.6.1.17.3 del Decreto 1625 de 2016 las entidades están en la obligación de exhibir sus libros de contabilidad ante la DIAN si esta así lo requiere, dicha exhibición puede llegar a acarrear gastos para el paso del formato físico al electrónico teniendo en cuenta que dicho proceso se realiza a través medios digitales [2].

En la actualidad existen una gran cantidad de software contables, los cuales facilitan y simplifi- can la contabilidad de una entidad, a su vez dichos software son bastante completos por lo cual su principal aplicación se ha dado en las grandes empresas del país, de igual manera su costo juega un papel importante ya que este tiende a ser un poco elevado debido a su complejidad, este costo oscila entre el $1.200.000 y los $2.000.000 como es el caso de Softland Pyme [3] y Siigo [4], quienes ofrecen diferentes tipos de paquetes con una duración de un año. Además, estos software cuentan con bastantes herramientas las cuales en algunos casos tienden a no ser útiles para las pequeñas entidades obligándolas a pagar un costo elevado por un software que no será totalmente útil, o a seguir llevando su teneduría de forma física.

1

---

<!-- Página 11 -->

2

La Parroquia del municipio de Chaguaní maneja su contabilidad de forma física, pues a pesar de que el gobierno permitiera los libros contables de manera electrónica no se obligó a las en- tidades a pasarse a dicho formato, sino que estas están en la libertad de escoger con cuál de los dos formatos trabajarán, ahora bien, una de las exigencias de la Diócesis a la cual pertenece esta Parroquia es la aplicación de nuevas tecnologías para el manejo de su contabilidad, no obs- tante al ser una Parroquia pequeña esta no cuenta con muchos recursos para hacerlo, además se debe tener en cuenta la crisis económica que se ha dado en el país a causa de la pandemia lo que impide que esta Parroquia adquiera un software de tan elevado costo. Por otro lado, la Parroquia trabaja con un contador que no reside en el municipio, razón por lo cual el párroco se ve en la obligación de desplazarse hasta el municipio de La Dorada en Caldas con el fin de entregarle las copias del libro de contabilidad a su contador, a su vez con dicho desplazamiento se generan gastos de tiempo y dinero. Por lo anterior surge la siguiente pregunta, ¿Cuál es la posible solución que se ajusta a los requerimientos de la Parroquia Santuario Señor de La Salud del municipio de Chaguaní para mejorar su proceso de teneduría de libros contables?.

---

<!-- Página 12 -->

# Capítulo 2

# Estado del arte

En los últimos años los proyectos relacionados con sistemas de información han tenido un gran auge tanto a nivel nacional como internacional, pues estos sistemas son muy usados por las entidades para tener una mejor organización. Estos sistemas se encuentran enfocados a dife- rentes áreas como académica, financiera, salud, entre otras. Uno de los principales motivos por los que se han implementado estos sistemas es porque brindan información de forma oportuna mejorando así el desempeño del área donde se aplique.

Dentro del enfoque financiero se encuentran los software contables con los cuales se le ha dado un plus a las operaciones contables que se llevan en una entidad. En el ámbito internacional se han desarrollado muy buenos proyectos, en el año 2018 Douglas Iván Napa realizó el desarrollo de un software contable para mejorar los flujos de información financiera en la empresa Cachito S.A con el objetivo inicial de identificar la situación actual de la empresa en cuanto a gastos e ingresos, realizado el diagnostico Napa procedió a realizar el desarrollo del software contable basado en las necesidades vistas [5].

Para el año 2019 Santiago Chicaiza y Mauricio Diaz realizaron el diseño de un sistema contable en el centro de mecanización unión y trabajo, Cantón Salcedo Parroquia Mulalillo con el obje- tivo de dar un mejor manejo y control a los recursos económicos, permitiendo así mejorar la gestión administrativa y financiera de la organización [6].

Ahora bien, Colombia no ha sido la excepción en el desarrollo de software contables pues en el año 2017 los ingenieros Danilo Rodríguez y Zaida Salamanca realizaron la formulación del proyecto de desarrollo del software contable y financiero de la Compañía NOVALTEC S.A.S ba- sado en las Normas Internacionales de Información Financiera (NIIF) donde se buscaba saciar

3

---

<!-- Página 13 -->

4

las necesidades contables de esta y otras compañías jóvenes que requerían aprovechar correc- tamente sus recursos y tomar correctas decisiones financieras [7].

Posteriormente en el año 2018 Alexander Castellón y Rocío Vergara realizaron el diseño e imple- mentación de un software contable que apoye la gestión en las tiendas de barrio, de Cartagena de Indias con el fin de optimizar la gestión y control de cada una de las tiendas [8].

Para el año 2020 Astrid García, Alejandra Peña y Laura Prada realizarón el diseño e implemen- tación de una herramienta contable para la cafetería “típicas te da gusto”, el sistema se basó en Excel y estados financieros, mediante los cuales fue posible conocer la situación económica de la empresa [9].

Seguidamente en el año 2021 Jose Camargo realizo la implementación de software de factura- ción que consolide la contabilidad en el hotel 1525 de Santa Marta, con el objetivo de que este hotel pudiera seguir operando a pesar de la pandemia, además, el sistema le permitió generar reportes financieros y establecer las proyecciones de crecimiento [10].

En Colombia se siguen desarrollando software contables para todo tipo de entidades ya sea de carácter personalizado o general, algunos de estos desarrollos son de tipo ERP (Enterprise Resource Planning) con los cuales es posible manejar tanto la gestión interna como externa de la entidad, dichos sistemas son aplicados a grandes entidades pues son más completos y acarrean un mayor costo [11]. Algunos desarrolladores se encuentran enfocados en las pequeñas enti- dades pues estas requieren del software contable para poder crecer y llegar a ser competitivas, cabe resaltar que existen entidades que toman la opción de un software personalizado el cual “como su mismo nombre lo indica” se encuentra diseñado única y exclusivamente para una entidad, pues dicho diseño es realizado de acuerdo a las necesidades que esta tenga.

Del mismo modo los desarrolladores de estos software han buscado un mayor impacto en las entidades tanto a nivel nacional como internacional, como es el caso de Siigo e Ilimitada las cuales unieron fuerzas con el fin de mejorar las actividades contables de las micro, pequeñas y medianas empresas del país, además a mediano plazo se busca mejorar la incursión en el ámbito internacional, pues Siigo no solo cuenta con presencia en nuestro país sino que también lo hace en países como Ecuador y Perú [12].

---

<!-- Página 14 -->

# Capítulo 3

# Justificación

En Colombia se estableció la Ley 1314 de 2009 que en su artículo primero establece los objetivos de manejar la documentación contable de manera electrónica, además el Decreto 0019 de 2012 que en su artículo 173 modifica el artículo 56 estableciendo que los libros contables podrán lle- varse en archivos electrónicos que garanticen la confidencialidad, integridad y disponibilidad de la información que en estos se almacené [13], [14].

Un beneficio es la confiabilidad en los cálculos que requiere la teneduría pues el sistema los rea- liza evitando así errores humanos en estos, con lo cual se garantiza que no se tenga que realizar nuevamente el proceso, además el aporte de este sistema es mantener a salvo la información pues los libros de contabilidad no están exentos de pérdidas o daños.

Por otro lado con la implementación del sistema se evita el desplazamiento del párroco hasta el municipio de la Dorada ubicado en el departamento de Caldas, ya que la información del libro contable ahora se envía de manera electrónica, además se evitan los gastos monetarios y de tiempo que pueden ser usados en otras actividades.

5

---

<!-- Página 15 -->

# Capítulo 4

# Objetivos

## 4.1. Objetivo general

Diseñar e implementar un sistema informático para modernizar la teneduría de libros en la Parroquia del municipio de Chaguaní para cumplir con la exigencia impuesta por la Diócesis de la Dorada-Guaduas empleando una adaptación de la metodología RUP.

## 4.2. Objetivos específicos

Identificar las necesidades de la Parroquia para establecer los requerimientos no funcio- nales del sistema.

Determinar el proceso de teneduría de libros en la Parroquia para diseñar una aplicación que pueda sistematizar este proceso.

Diseñar la arquitectura del sistema para garantizar la seguridad de la información alma- cenada.

Desarrollar el sistema de acuerdo a las necesidades expuestas por la Parroquia.

Realizar pruebas de usuario para comprobar el correcto funcionamiento del sistema.

6

---

<!-- Página 16 -->

# Capítulo 5

# Marco teórico

## 5.1. Sistemas de información

Con el pasar de los años la organización de una entidad ha tendido a ser más compleja por ello se ha tenido que recurrir a la implementación de los sistemas de información que también han tomado una mayor relevancia en medida que se han desarrollado los equipos informáticos [15].

Según Rafael Andreu en su libro Estrategia y Sistemas de Información define a un sistema de información como un conjunto de procesos que operan sobre una colección de datos de acuerdo a las necesidades de una empresa, dicho sistema recopila, elabora y distribuye de manera selec- tiva la información para la operación de esta, además apoya los procesos de toma de decisiones que son necesarios para llevar a cabo funciones de negocio dentro de la entidad [16].

La implementación de estos sistemas han traído consigo bastantes beneficios como lo es la ob- tención de información en tiempo real, el cumplimiento de objetivos y el control en la informa- ción para un mejor análisis. La principal meta de cualquier entidad ya sea grande, mediana o pequeña es lograr ser competitiva y esto se logra con los tres beneficios expuestos anteriormen- te, con dicha competitividad una entidad puede llegar a incursionar fuertemente en el mercado logrando así hacer parte de la globalización [8] [17]. Otro beneficio importante consiste en que al aplicar un sistema de información para el tratamiento de datos se logra obtener información clara, precisa y confiable en la cual se basa la entidad para la toma de decisiones oportuna y acertada [18].

7

---

<!-- Página 17 -->

8

## 5.2. Pasos para la creación de un sistema de información

Según Alejandro Hernández el proceso de creación de un sistema de información está construi- do por una serie de pasos los cuales se describirán a continuación: [15]

Definición del proyecto: En esta etapa se identifican los problemas que presenta una entidad y como pueden solucionarse mediante la implementación de un sistema de información, además se establecen cuáles serán los objetivos del uso de dicho sistema.

Análisis de sistemas: Una vez identificados los problemas que presenta la entidad se procede a analizarlos más detenidamente identificando las causas que lo originan y dando diversas solu- ciones. En esta fase se genera un estudio de factibilidad con el fin de determinar si las soluciones planteadas son realizables basados en los recursos que posee la organización, a continuación se describirán tres tipos de factibilidad:

Factibilidad técnica: En este caso se debe analizar si la entidad cuenta con los medios informáticos adecuados para dar solución al problema o si se deben adquirir en el exterior.

Factibilidad económica: Se realiza un estudio económico a la solución con el fin de comprobar de que los beneficios económicos superen lo invertido.

Factibilidad operativa: Se debe valorar si la solución es deseable según la organización interna de la entidad.

Diseño de sistemas: Teniendo clara la solución se procede a detallar como el sistema de infor- mación satisface los requisitos planteados por la organización. También se debe indicar como se compone el sistema de información (hardware, software y tecnológica de las telecomunica- ciones) y como se relacionan estos entre sí para así establecer las especificaciones del sistema de información.

Programación: Se llevan a cabo las especificaciones del sistema en el área de programación y desarrollo de software.

Fase de pruebas: Con el fin de evaluar el correcto funcionamiento del sistema se lleva a cabo un análisis exhaustivo y profundo con el cual se comprueba el funcionamiento en diversas condiciones y si los resultados obtenidos son los esperados. Para llevar a cabo este proceso se deben llevar a cabo tres tipos de prueba las cuales se describen a continuación:

Pruebas de programas: Se deben probar los programas por separado con el fin de evidenciar que cada uno de estos se encuentra libre de errores.

---

<!-- Página 18 -->

9

Pruebas al sistema: Se probarán todos los programas en conjunto pues en ocasiones puede llegar a pasar que los programas por separado funcionan correctamente pero al momento de trabajar en conjunto no arrojan los resultados esperados.

Pruebas de aceptación: Pruebas realizadas por el personal que hará uso del sistema las cuales darán el visto bueno del correcto funcionamiento de este.

Conversión: Comprobado el correcto funcionamiento del sistema de información se procede a su implantación o a la sustitución del antiguo sistema por el nuevo. En esta conversión se pueden optar por diversas estrategias:

Estrategia paralelo: Esta estrategia se caracteriza porque ambos sistemas funcionan durante un periodo, siendo la estrategia más fiable y segura pero la más costosa con la cual se puede obte- ner información redundante.

Cambio directo: En este caso se cambia el antiguo sistema por el nuevo, siendo la menos cos- tosa pero con bastante riesgo pues en caso de llegarse a provocar algún error se puede dar la paralización de la actividad en la entidad.

Experiencia piloto: En este caso el nuevo sistema de información se utiliza solo en un área de la entidad y una vez comprobado su correcto funcionamiento se implementa en la totalidad de la compañía.

Producción y mantenimiento: Teniendo instalado el nuevo sistema de información se dice que este ya se encuentra en producción donde empieza un proceso de evolución del sistema por parte de los usuarios con el fin de identificar las actualizaciones que se requieren.

## 5.3. Aplicación de los sistemas de información en la contabilidad

Ahora bien uno de los campos de incursión de los sistemas de información es la contabilidad, pues con la aplicación de la teleinformática las entidades han podido suministrar información contable útil para la toma de decisiones por parte de los usuarios, también gracias al gran avance que se ha dado en estas ramas se ha conseguido llegar a la internacionalización de la contabilidad donde la información financiera puede llegar a ser comparada tanto a nivel nacional como internacional [7].

---

<!-- Página 19 -->

10

## 5.4. Software contable

En la contabilidad se entiende como sistema de información a un software contable que siste- matiza y simplifica las tareas de contabilidad, pues este se encarga de procesar las transacciones (compras, ventas) al cual solo se le ingresa la información requerida (ingresos, egresos) [19]. El software contable se caracteriza por ser el soporte para la toma de decisiones, a su vez dicho software es el modelo ideal para dar valor y crecimiento al área contable de una entidad [20].

## 5.5. Características de un software contable

Según Eduardo Pico y Sharon Núñez un software contable debe tener ciertas caracterizas para poder ser catalogado como una buena herramienta, a continuación se describirán algunas de esas características: [17]

Compatible: Debe funcionar a la par con otros programas para que pueda existir el intercambio de información.

Fácil uso: Su interfaz gráfica debe ser intuitiva de manera que el usuario pueda agregar de forma rápida y sencilla la información.

Automático: Cuando el usuario ingrese datos el programa debe generar información relevante.

Seguro: Debe contar con claves de acceso y diferentes tipos de usuario, para así proteger la información de la entidad.

Posibilidad de integrar: Un programa destacado es aquel que permite integrar documentos externos como adjuntar facturas, comprobantes entre otros.

Reportes básicos: Se debe contar con la opción para generar reportes con la información que se ha ingresado a lo largo del tiempo.

## 5.6. Marco legal

En Colombia se estableció la Ley 1314 de 2009 que en su artículo primero establece los permi- sos para poder manejar la documentación contable de manera electrónica [14], posteriormente se emitió el Decreto 0019 de 2012 que en su artículo 173 modifica el artículo 56 estableciendo lo siguiente: “Art. 173. Libros del comerciante. El artículo 56 de Código del Comercio quedará

---

<!-- Página 20 -->

11

así: Art. 56. Los libros podrán ser de hojas removibles o formarse por series continuas de tar- jetas, siempre que unas y otras estén numeradas, puedan conservarse archivadas en orden y aparezcan autenticadas conforme a la reglamentación del Gobierno. Los libros podrán llevarse en archivos electrónicos, que garanticen en forma ordenada la inalterabilidad, la integridad y seguridad de la información, así como su conservación. El registro de los libros electrónicos se adelantará de acuerdo con la reglamentación que expida el Gobierno Nacional” [13].

Ahora bien el artículo 175 del Decreto mencionado anteriormente tambien realiza una modi- ficación en el Código de Comercio, en dicha modificación se enuncia lo siguiente: “Art. 175. Registro de los libros de comercio. El numeral 7 del artículo 28 del Código de Comercio, que- dará así: 7. Los libros de registro de socios o accionistas, y los de actas de asamblea y juntas de socios” [13].

## 5.7. Teneduría de libros

Inicialmente en Colombia la teneduría de libros se realizaba de forma física, este tipo de tene- duría requería una condición especial la cual era el registro de todos los libros ante la Cámara de Comercio. Con las dos modificaciones mencionadas en la sección anterior se dio paso a los libros en archivos electrónicos, en los cuales el proceso de teneduría es similar al de los libros físicos, sin embargo para los libros de contabilidad oficiales (libro diario, mayor y balance y libro de inventarios) no se requiere el registro ante la Cámara de Comercio, sino que solo basta con la conservación del archivo electrónico dentro de la entidad [21].

Ahora bien el proceso de teneduría se trabaja así: La de teneduría de libros generalmente está a cargo por un contador público, el cual debe tomar las facturas en orden cronológico y pasarlas al libro de contabilidad garantizando que los saldos de debido y crédito sean iguales. Poste- riormente el contador y el representante legal de la entidad deben firmar el libro para que este sea válido [22].

## 5.8. Requerimientos del software

Ian Sommerville define los requerimientos para un sistema como la descripción de los servicios que este proporciona, así como sus restricciones operativas. En dichos requerimientos también se expresan las necesidades del cliente en cuanto a un sistema que ayude a resolver un proceso.

---

<!-- Página 21 -->

12

Los requerimientos de un sistema hacen parte de la ingeniería de requerimientos lo cual es el proceso de descubrir, analizar, documentar y verificar estos servicios y restricciones [23].

Los requerimientos de un sistema se clasifican en diversos tipos, sin embargo en este caso solo se tendrán en cuenta dos de ellos, a continuación se dará una breve descripción de cada uno de estos:

Requerimientos funcionales: Los requerimientos funcionales describen lo que un sistema debe hacer a partir de las acciones que realice un usuario, esto depende del tipo de software que se esté desarrollando, los tipos de usuarios y el enfoque que le de la organización al elaborarlos. Allí también se expresan las entradas, salidas, excepciones y condiciones con las cuales contara el sistema [23].

Requerimientos no funcionales: Los requerimientos no funcionales, como su mismo nombre lo dice no se refieren a las funciones específicas del sistema sino a la especificación o restricción de propiedades como la fiabilidad, tiempo de respuesta, capacidad de almacenamiento, entre otros. Dichos requerimientos surgen de las necesidades del usuario basadas en restricciones como el presupuesto, políticas de la entidad, necesidad de interoperabilidad con otros sistemas o campos como la seguridad de la información [23]

---

<!-- Página 22 -->

# Capítulo 6

# Diseño

El diseño de aplicaciones contables suele resultar algo tedioso para las personas que no tengan conocimientos en esta área, sin embargo, en este proyecto se realizó la debida investigación para poder realizar un diseño correcto. Ahora bien, una vez obtenidos los conocimientos ne- cesarios se pasó al diseño como tal, allí se realizaron los diagramas de despliegue, estructural y relacional, a su vez se realizaron los casos de uso y el levantamiento de requerimientos no funcionales. En este capítulo se desarrolla el proceso descrito anteriormente, el cual empieza con la investigación que se evidencia a continuación.

## 6.1. Descripción de la teneduría de libros

La teneduría de libros es el proceso de recopilación de información de los movimientos de di- nero (Ingresos y egresos) que se realizan en una entidad, dicha información se usa para clasifi- carla, sintetizarla y luego documentarla en registros especiales llamados libros de contabilidad. En algunas entidades los libros de contabilidad no existen como tal, pues estos se han venido llevando en CD, DVD, ordenadores o dispositivos similares, aun así mantienen su nombre ori- ginal de libros [22]. En dicha teneduría se manejan varios libros sin embargo los principales son el libro diario y el libro mayor y balance. A continuación se dará una descripción de cada uno de estos:

13

---

<!-- Página 23 -->

14

6.1.1. Libros principales

6.1.1.1. Libro diario

En este libro se realizan todas las operaciones que la entidad realiza día a día, dichas operacio- nes se denominan asientos contables los cuales se deben registrar de forma cronológica a partir de sus comprobantes (facturas). Cabe resaltar que el registro de las operaciones diarias en este libro se debe agrupar en periodos mensuales. En la figura 1 se puede evidenciar que este libro cuenta con diversas columnas dentro de las cuales se registran la fecha, el concepto del asiento contable, él debe, el haber y el saldo. Por otro lado cada una de las filas del libro será un asiento contable [24] [25].

FIGURA 1: Estructura del libro diario. Fuente: Autor

6.1.1.2. Libro mayor y balance

El libro mayor y balance se encuentra basado en el libro diario, pues allí se registran los valores por cuenta de los registros realizados en el libro diario. Ahora bien este libro parte de los saldos del periodo anterior, donde se muestran los valores del movimiento débito y crédito del perio- do respectivo para luego registrar los nuevos saldos que servirán como saldos anteriores para el periodo siguiente. En la figura 2 se observa cómo está compuesto el libro mayor en donde sus columnas corresponden al código de la cuenta, el nombre de esta, posteriormente se tienen el débito y crédito del periodo anterior, del periodo en curso y de los nuevos saldos que estos dos periodos produzcan [25].

---

<!-- Página 24 -->

15

FIGURA 2: Estructura del libro mayor y balance. Fuente: Autor

6.1.2. Características de los libros

Los libros de contabilidad físicos y electrónicos deben contar con algunas características para poder ser válidos, una de las principales características es la numeración consecutiva de cada una de sus páginas con lo cual se garantiza la calidad de la información contenida en ellos. Lo anterior se encuentra establecido en artículo 8 del anexo 6 del Decreto 2270 de 2019 donde se enuncia lo siguiente: “Art. 8. Libros. Los estados financieros deben ser elaborados con fun- damento en los libros en los cuales se hubieren asentado los comprobantes. Los libros deben conformarse y diligenciarse en forma tal que se garantice su autenticidad e integridad. Cada libro, de acuerdo con el uso a que se destina, debe llevar una numeración sucesiva y continúa. Las hojas y tarjetas deben ser codificadas por clase de libros (. . . )” [26]. Además de lo anterior los libros deben contar en su primera página con un encabezado donde se especifique qué libro es, el nombre de la entidad y su NIT.

Por otro lado el libro trabajado de forma electrónica debe contar con algunas características las cuales se explican a continuación:

6.1.2.1. Características de los libros electrónicos

Según [27] esta modalidad el archivo electrónico debe cumplir con lo siguiente:

Que la información que contengan sea accesible para su posterior consulta.

Que el mensaje de datos o el documento sea conservado en el formato en que se haya generado.

Que se pueda determinar el origen, la fecha y hora en que fue producido el documento.

Ahora bien los libros físicos no cuentan con unas características particulares, pero si con algunas prohibiciones. Según [28] dichas prohibiciones son:

---

<!-- Página 25 -->

16

6.1.2.2. Prohibiciones en los libros físicos

Alterar en los asientos el orden o la fecha de las operaciones.

Dejar espacios que permitan intercalaciones o adiciones en el texto.

Hacer raspaduras, tachones o correcciones en los asientos. Los errores se deben corregir con un nuevo registro.

Borrar, tachar en todo o en parte los registros.

Arrancar hojas, alterar el orden de las mismas o mutilarlas.

6.1.3. Paso a paso de la teneduría en el libro diario de la Parroquia

En el caso de la Parroquia de Chaguaní se trabaja solo con el libro diario, donde lo primero que se tiene en cuenta es cada una de las facturas que se emiten a diario, dichas facturas co- rresponden a conceptos de ingresos como misas, donaciones, alquiler de bóvedas entre otros. Ahora bien, como el libro diario se encuentra compuesto también por conceptos de egresos es- tos también se deben tener en cuenta con su respectivo respaldo, estos egresos se manejan en conceptos como el pago de servicios de la Parroquia, sostenimiento del párroco, arreglos flora- les entre otros. Seguidamente la información de estas facturas debe ser trasladada al libro diario de forma cronológica, este proceso lo realiza el párroco pues él tiene conocimientos en el área contable, sin embargo el sacerdote contrata a un contador para que este realice la verificación del proceso realizado y de fe con su firma de que el libro se ha llevado a cabo de una manera correcta. Ahora bien, el proceso anterior se puede representar gráficamente así:

FIGURA 3: Diagrama proceso de teneduría en la Parroquia. Fuente: Autor

---

<!-- Página 26 -->

17

## 6.2. Levantamiento de requerimientos no funcionales

Para levantar los requerimientos no funcionales inicialmente se buscó documentación guía de requerimientos para otros sistemas, a partir allí se tomaron algunos requerimientos que se veían necesarios para el sistema de la Parroquia. Seguido de esto se estableció una charla con el pá- rroco con el fin de exponerle los requerimientos planteados por el desarrollador y conocer su punto de vista acerca de estos, en dicha charla el párroco considero algunos requerimientos innecesarios por diversos motivos, sin embargo se le aconsejo que tomara algunos de los que él veía como innecesarios ya que como desarrollador se le debe ofrecer un buen sistema al cliente. Finalmente al concluir la charla se obtuvieron los requerimientos no funcionales para el sistema los cuales se evidencian en el anexo 17.

6.2.1. Requerimientos no funcionales acordados para el sistema

Los requerimientos no funcionales fueron divididos en varias categorías, a continuación se da la descripción de cada uno de ellos:

Roles

Inicialmente el párroco no consideraba necesario la creación de más de un rol, sin embargo después de aconsejarlo se estableció que existirán dos roles para los usuarios, el primero será un rol administrador al cual darán uso el y su secretaria, este rol contara con todos los permisos en el sistema (Lectura, escritura, modificación y creación de libros). El segundo rol será un rol invitado el cual solo tendrá acceso a la información contenida en el sistema, por lo tanto este no tendrá ningún otro permiso aparte del de lectura de libros.

Copias de seguridad

Las copias de seguridad se llevarán en el servicio de alojamiento de archivos en la nube conoci- do como Google Drive, ya que se desea tener un almacenamiento totalmente gratuito, además estas se llevarán a cabo de forma programada.

Facilidad de uso

El sistema permite al usuario el movimiento y modificación del tamaño de las ventanas, ade- más el sistema debe ser intuitivo y de fácil manejo para el usuario.

---

<!-- Página 27 -->

18

Interfaz

Al abrir la aplicación se debe mostrar la pantalla de ingreso, así como el nombre de la Parroquia en la parte superior, cabe resaltar que se definió no tener ninguna imagen como fondo. Por otro lado el color, el tamaño y tipo de letra vendrán predeterminados, sin embargo el usuario podrá modificarlos a su gusto.

Rendimiento

Al ejecutar una acción el sistema no se deberá bloquear para el usuario por más de 10 segundos.

Disponibilidad del sistema

Para esta categoría se acordó que el sistema debe realizar el cierre de la sesión después de 10 minutos de inactividad, esto con el fin de evitar que otras personas hagan uso del sistema sin previa autorización del párroco.

Arquitectura

El sistema debe estar diseñado para escritorio ya que se desea una aplicación totalmente gra- tuita, además, debido a que en el municipio la conectividad a internet en ocasiones suele ser intermitente es mejor una App de escritorio que una web, de igual manera el sistema debe estar diseñado para un PC que cuenta con un procesador Intel Celeron a 2.5 GHz, 2 GB de memoria RAM y un sistema operativo Windows 10 a 32 bits.

Seguridad

La longitud de las contraseñas debe ser entre ocho y nueve caracteres, además se debe controlar la complejidad de estas exigiendo una combinación de caracteres. De igual manera la cantidad máxima de intentos para el ingreso de la contraseña serán tres, una vez se llegue a este valor se pedirá restablecer la contraseña mediante el correo electrónico.

Otros

Finalmente el sistema debe mostrar el listado de los libros existentes por años, además de esto se debe permitir la modificación de datos antes de que se realice el cierre mensual. Por otro lado también se debe permitir la generación del documento en formato PDF con lo que se lleva trabajado hasta el momento, es decir que no es necesario realizar el cierre anual pero si el diario para su generación.

---

<!-- Página 28 -->

19

## 6.3. Diseño de la arquitectura del sistema

Para diseñar la arquitectura del sistema se realizaron los diagramas de despliegue, estructural, de casos de uso y relacional, dichos diagramas se evidencian y describen a continuación:

6.3.1. Diagrama estructural

El diagrama de la figura 4 representa la estructura del sistema, allí se evidencia el computador en el cual estará la aplicación junto a la base de datos, posteriormente se observa una relación con la nube la cual a su vez tiene una relación con drive, pues este será el servicio que se usará para almacenar las copias de seguridad.

FIGURA 4: Diagrama estructural. Fuente: Autor

6.3.2. Diagrama de despliegue

El diagrama de despliegue se encuentra compuesto por cuatro nodos que representan los ele- mentos de software y hardware del sistema, el primer nodo representa al servicio de drive, dentro de este nodo se encuentran las copias de seguridad las cuales son un componente de dicho nodo. Posteriormente en una asociación con el segundo nodo se tiene el computador que tendrá como componente un servicio de Windows para ejecutar las copias de seguridad, además este nodo contiene los nodos aplicación y base de datos, dentro del nodo aplicación se encuentran tres componentes asociados que son presentación, negocio y datos ya que se em- pleara una arquitectura clásica de tres capas. Finalmente el nodo base de datos se encuentra asociado a los componentes datos del nodo aplicación y al componente servicio de Windows, en la figura 5 se observa el diagrama anteriormente descrito.

---

<!-- Página 29 -->

20

FIGURA 5: Diagrama de despliegue. Fuente: Autor

6.3.3. Diagrama de casos de uso

En el diagrama de la figura 6 se representan los casos de uso, allí se tienen dos tipos de roles por lo cual es necesario que la aplicación permita gestionar todo lo referente a los usuarios, esto se hace necesario ya que todas las aplicaciones deben contar con este tipo de funcionalidad, es por ello que se decide colocar el caso de uso administrar usuarios. Debido a que el proceso de libros requiere la apertura y cierre de libros se hace necesario agregar los casos de uso crear libro y ce- rrar libro, los cuales solo podrán realizar los usuarios que cuenten con el rol de administrador. De igual manera la teneduría requiere que se agreguen asientos a los libros, además de poder modificarlos ante cualquier error, es por ello que se debe contar con funcionalidades que les permitan a los usuarios administradores realizar estas dos tareas, las cuales se ven representa- das en los casos de uso agregar asientos al libro y modificar asientos del libro. Además, ya que en distintos momentos se puede requerir la lectura de los libros así como su impresión se hace necesario implementar funcionalidades que lo permitan, es por ello que se crean los casos de uso leer libros e imprimir libro, a su vez estos dos casos de uso se encuentran relacionados con el caso de uso buscar libro ya que para leerlos e imprimirlos primero se debe buscar el libro que se desea.

Por otro lado, todas las aplicaciones sin importar su fin deben contar con funcionalidades de ingreso, cambio y recuperación de contraseñas es por ello que se hace necesario implementar los casos de uso ingresar, cambiar contraseña y recuperar contraseña. Con el fin de realizar

---

<!-- Página 30 -->

21

una aplicación cómoda y que se ajuste a los gustos de los usuarios se debe contar con una funcionalidad que permita la configuración de la aplicación lo cual se ve representado en el caso de uso configurar visualmente la aplicación. Finalmente con el fin de mantener la información segura y evitar su pérdida se debe contar con funcionalidades que permitan gestionar las copias de seguridad, es por ello que se implementan los casos de uso programar copias de seguridad y restaurar copia de seguridad.

FIGURA 6: Diagrama de casos de uso. Fuente: Autor

6.3.4. Diagrama relacional

Para el diagrama de la figura 7 se detectarón siete tablas las cuales son: Entidad, libro, asiento, tipoasiento, usuario, rol y cierre. Dichas tablas cuentan con diversos atributos, además estas se relacionan entre sí de la siguiente manera:

Un libro pertenece a una entidad, pero una entidad puede tener muchos libros.

Un asiento pertenece a un libro, pero un libro puede tener muchos asientos.

---

<!-- Página 31 -->

22

Un asiento pertenece a un tipoasiento, pero un tipoasiento puede tener muchos asientos.

Un asiento pertenece a un cierre, pero un cierre puede tener muchos asientos.

Un usuario pertenece a una entidad, pero una entidad puede tener muchos usuarios.

Un usuario pertenece a un rol, pero un rol puede tener muchos usuarios.

Por otro lado, se tomó la buena práctica de mantener el id independiente de los datos, el cual es un campo adicional en cada tabla y será auto numérico. Además, al momento de diseñar un modelo relacional es útil aplicar la normalización ya que con ella se garantiza la integridad de la información, este modelo cumple con la primera y segunda forma normal, las cuales exigen lo siguiente:

Primera forma normal: Una tabla se encuentra en primera forma normal si cada uno de los cam- pos contiene un único valor.

Segunda forma normal: La segunda forma normal se cumple si todos los campos dependen di- rectamente de la clave definida.

FIGURA 7: Diagrama relacional. Fuente: Autor

6.3.5. Casos de uso

Para generar los casos de uso se utilizó el formato de la figura 8, en la parte superior de este existen campos donde se debe colocar el nombre del proyecto, del caso de uso, de la persona que lo elabora, fecha de elaboración, actores que participaran en el caso de uso y un pequeño resumen de lo que hará el caso de uso. Posteriormente se tienen los campos de entrada que es la información que el usuario tendrá que digitar o seleccionar de listas en cada una de las pantallas de la aplicación.

---

<!-- Página 32 -->

23

Seguidamente, se tienen el campo para el flujo básico de eventos, en el cual se describirá a detalle cada uno de los pasos que realizará el actor y la respuesta que el sistema otorgará ante los pasos del actor, luego se tienen los flujos alternativos que al igual que el flujo básico son un paso a paso de interacciones del actor y el sistema, sin embargo los flujos alternativos solo se usan en casos excepcionales donde la aplicación toma otro camino. Además de esto, se tendrán campos para postcondiciones y requerimientos especiales.

Por otro lado, se tendrá el prototipo que se usará para el caso de uso, además de un control de versiones ante cambios que se realicen en este documento y finalmente la firma del cliente para su respectivo aval.

CASO DE USO

Código: Versión: 01 Emisión: Página 1 de 1

PROYECTO / APLICACIÓN: Identificador: CU- Nombre Caso de Uso:

Generado por: Fecha de creación: Resumen:

Actores:

Pre-Condición: Entradas Nombre de Ob Tipo Long Restricción Descripción campo

Flujo básico de eventos – Actor Sistema 1. 2. 3. 4. Flujo Alternativo 1 – Actor Sistema

Post- Condiciones:

Requerimientos especiales:

Prototipo

Control de versiones Versión Cambio Responsable Fecha

Aprobación y aceptación

_____________________________ Fecha:

FIGURA 8: Plantilla casos de uso. Fuente: Anónimo

---

<!-- Página 33 -->

24

A continuación, se dará una breve descripción de cada caso de uso, en caso de desear conocer- los más a detalle estos se pueden encontrar en los anexos del 1 al 15, donde se presentan los documentos firmados por el párroco aceptando las definiciones descritas en estos.

Crear libro

En este caso de uso se podrá realizar la creación de un nuevo libro, al cual se le deberá asignar un nombre de acuerdo al año en el que se esté creando.

Agregar asientos al libro

Allí se podrán agregar los asientos al libro, donde se solicitara fecha, valor, el tipo de asiento y la descripción. Teniendo en cuenta el asiento que se agrega se debe realizar la actualización del crédito, débito y saldo del libro correspondiente.

Modificar asientos del libro

Con este caso de uso se podrán realizar modificaciones a los asientos, esto con el fin de permitir corregir cualquier error en la información ingresada inicialmente.

Cerrar libro

Este caso de uso sirve para poder dar por terminada la contabilidad del mes y del año.

Ingresar

El caso de uso ingresar sirve para poder tener acceso a la aplicación, allí el usuario digitará su identificación y su contraseña.

Cambiar contraseña

Cambiar contraseña sirve para poder realizar la modificación de la contraseña, donde este cam- bio tendrá algunos requisitos para cumplir con un nivel de seguridad adecuado.

Configurar visualmente la aplicación

Este caso de uso sirve para modificar a gusto del usuario la presentación de la aplicación, estos cambios pueden ser en cuanto a letra y colores.

Programar copias de seguridad

Con el fin de dar seguridad a la información almacenada se tiene este caso de uso, en el cual se indica cada cuanto tiempo se debe realizar la copia de seguridad.

---

<!-- Página 34 -->

25

Restablecer contraseña

En ocasiones los usuarios suelen olvidar su contraseña por lo cual se tiene este caso de uso, el cual se encarga de enviar una nueva contraseña generada aleatoriamente al correo registrado por el usuario.

Administrar usuarios

Administrar usuarios se usa para crear, modificar y eliminar usuarios dentro del sistema. Para crear un usuario se debe otorgar a la aplicación información como el número de documento, correo electrónico y el rol que este nuevo usuario tendrá, para la modificación se podrán realizar cambios en la información mencionada anteriormente y finalmente para la eliminación solo se tendrá que seleccionar el usuario que se quiere eliminar.

Buscar libro

Como su mismo nombre lo indica el caso de uso buscar libro sirve para buscar un libro en específico. Este caso de uso abre los casos de uso leer libro e imprimir libro.

Leer libro

Para observar un libro de algún periodo anterior o en curso se tendrá este caso de uso, el cual se encargara de mostrar dentro de la aplicación un documento pdf con el libro solicitado.

Imprimir libro

Este caso de uso permite al usuario descargar de la aplicación el documento de un libro, esto para su respectiva impresión.

Restaurar copia de seguridad

En caso de pérdida o daño en la información este caso de uso será el encargado de recuperar en un punto anterior la información y no tener la pérdida total de esta.

---

<!-- Página 35 -->

# Capítulo 7

# Resultados

Todo desarrollo debe contar con una selección de herramientas que garanticen la correcta eje- cución del mismo, en este caso se debían tener herramientas como un gestor de base de datos, un IDE de desarrollo, un ORM, un lenguaje de programación y una plataforma de desarrollo para interfaces gráficas. Las herramientas seleccionadas fueron:

Microsoft SQL Server Management Studio.

Visual Studio.

Entity Framework.

C#.

Windows Forms.

Estas herramientas fueron seleccionadas ya que se posee un buen dominio sobre ellas por parte del autor, además son de fácil manejo y se tenía el apoyo del director en casos donde no se tuviera conocimiento. Cabe aclarar que la herramienta de Windows Forms fue seleccionada ya que dentro de los requerimientos se estableció una aplicación de escritorio.

## 7.1. Desarrollo

Para la etapa de desarrollo se tuvo en cuenta el diseño realizado previamente, en donde se tienen 3 capas llamadas datos, negocio y presentación, las cuales fueron creadas con el fin de

26

---

<!-- Página 36 -->

27

ocultar la complejidad de la base de datos en 3 niveles y así dar un mayor orden. Cada una de las capas tiene su función pues la capa de datos se encarga de almacenar la información, la de negocio de procesarla y la de presentación de mostrarla de una manera más amigable con el usuario.

En la figura 9 se puede observar la capa de datos, la cual establece la conexión la conexión con el motor de base de datos mediante el uso de la herramienta Entity Framework por lo cual esta capa no posee ninguna clase o formulario, ahora bien, en la figura 10 se puede observar la capa de negocio en la cual se crearon las clases identificadas para la aplicación, finalmente en la figura 11 se observa la capa de presentación en la cual fueron creados cada uno de los formularios de usuario que corresponden a los prototipos de los casos de uso levantados.

FIGURA 9: Capa de datos. Fuente: Autor

FIGURA 10: Capa de negocio. Fuente: Autor

---

<!-- Página 37 -->

28

FIGURA 11: Capa de presentación. Fuente: Autor

Ahora bien, dentro de las clases creadas en la capa de negocio se encuentran las funcionalidades planteadas mediante los casos de uso, por lo cual se puede decir que en esta capa es donde se ejecuta principalmente la aplicación, a continuación, se expondrán dichas funcionalidades.

Ingresar

Esta funcionalidad es la primera que usaran los usuarios al abrir la aplicación, además con ella se garantiza que personas inescrupulosas no puedan acceder al sistema. Para esta funcionali- dad fueron diseñadas dos pantallas, la primera de ellas se evidencia en la figura 12 y la segunda en la figura 13 que se habilitará una vez el usuario ingrese correctamente sus credenciales. Es de aclarar que la figura 13 cuenta con una modificación en su diseño pues en la planteada inicial- mente no se aprovechaba totalmente el espacio haciendo que el libro que se presentaba como PDF se observara muy pequeño.

---

<!-- Página 38 -->

29

FIGURA 12: Pantalla ingresar. Fuente: Autor

FIGURA 13: Pantalla principal. Fuente: Autor

Crear libro

El libro es el objeto principal dentro de la aplicación pues sin este no se puede realizar nada respecto a la teneduría, es por ello que esta funcionalidad se encarga de crear un libro dentro del sistema. Sin embargo, en caso de que exista un libro que no se encuentre cerrado no se permitirá la creación de uno nuevo. En la figura 14 se evidencia la pantalla que se creó para esta funcionalidad.

FIGURA 14: Pantalla crear libro. Fuente: Autor

---

<!-- Página 39 -->

30

Agregar asientos al libro

Para agregar asientos al libro se hace uso de la pantalla expuesta en la figura 15, la cual verá el usuario al hacer clic en el botón de agregar asientos que se encuentra en la pantalla principal. Esta funcionalidad se usa para realizar el registro en el sistema de cada una de las facturas que se tienen.

FIGURA 15: Pantalla agregar asiento. Fuente: Autor

Modificar asientos del libro

La modificación de asientos permite al usuario la corrección de estos ante cualquier error en el ingreso previo, para ello se desarrollaron dos pantallas, las cuales se observan en la figura 16 y 17. La pantalla de la figura 16 se encarga de mostrar a los usuarios los asientos que se pueden modificar, en cambio la pantalla de la figura 17 muestra la información del asiento a modificar.

FIGURA 16: Primera pantalla modificar asiento. Fuente: Autor

---

<!-- Página 40 -->

31

FIGURA 17: Segunda pantalla modificar asiento. Fuente: Autor

Cerrar libro

El cierre de asientos y libros es bastante importante dentro de la aplicación, ya que con esto se garantiza una mayor protección de los datos, pues allí se realiza el bloqueo de las modifica- ciones en los asientos que se tienen creados en el mes. Ahora bien, esta funcionalidad no tiene una pantalla como tal pues solo arroja un mensaje solicitando la confirmación para realizar el cierre, dicho mensaje se evidencia en la figura 18.

FIGURA 18: Mensaje cerrar libro. Fuente: Autor

Cambiar contraseña

El cambio de la contraseña puede ayudar a mantener la aplicación más segura pues como re- comendación esta se debe cambiar cada cierto periodo de tiempo con el fin de que personas ajenas no la conozcan. Ahora bien, para esta funcionalidad se diseñó la pantalla de la figura 19.

---

<!-- Página 41 -->

32

FIGURA 19: Pantalla cambiar contraseña. Fuente: Autor

Configurar visualmente la aplicación

La configuración visual es usada para que el usuario tenga una interfaz que pueda configurar en cuanto a letra y colores a su gusto, para ello se diseñó la pantalla de la figura 20.

FIGURA 20: Pantalla configuración visual Fuente: Autor

Programar copias de seguridad

La programación de las copias de seguridad permite al usuario establecer cada cuanto tiempo desea realizarlas, además si este desea hacerla en un momento diferente contará con un botón

---

<!-- Página 42 -->

33

para esto. Para llevar a cabo el procedimiento descrito anteriormente se diseñó la pantalla de la figura 21.

FIGURA 21: Pantalla programar copias de seguridad Fuente: Autor

Restablecer contraseña

En algunas ocasiones las contraseñas suelen ser olvidadas por los usuarios por lo que se deben tener métodos de recuperación para estas, en esta aplicación se establece el método mediante el correo electrónico al cual será enviada una contraseña generada aleatoriamente. En la figura 22 se observa la pantalla que se diseñó para esta funcionalidad en la cual el usuario solo tendrá que digitar su identificación.

FIGURA 22: Pantalla restaurar contraseña Fuente: Autor

Administrar usuarios

En la administración de usuarios se permite crear, modificar y eliminar usuarios lo cual se implementó debido a que son funciones fundamentales al momento de desarrollar una aplica- ción, con ellas se permite controlar el acceso de las personas a la aplicación, además del tipo de acceso que esta tendrá. Para estas funcionalidades se diseñaron tres pantallas, en donde en la primera se tendrá acceso a las acciones que se pueden realizar a los usuarios como se observa en la figura 23, la segunda será para crear y modificar la información de los usuarios, la pantalla diseñada para este caso se observa en la figura 24 y finalmente la tercera se observa en la figura

---

<!-- Página 43 -->

34

25, la cual no estaba contemplada en los casos de uso pero se agregó con el fin de verificar que el correo digitado al momento de crear el usuario realmente exista.

FIGURA 23: Pantalla principal administrar usuarios Fuente: Autor

FIGURA 24: Pantalla para crear y modificar usuarios Fuente: Autor

FIGURA 25: Pantalla para verificar correo de usuario Fuente: Autor

---

<!-- Página 44 -->

35

Restaurar copia de seguridad

La restauración de una copia de seguridad se usa para retomar la información que se tenía hasta cierto punto, pues un equipo no está exento de un daño en su sistema operativo u otro elemento que pueda provocar la pérdida de la información que se tenga en el equipo. Con esta copia de seguridad se garantiza la seguridad de la información ante perdidas pues esta se encontrara almacenada en el equipo y en el drive. La pantalla que se diseñó para esta funcionalidad se puede observar en la figura 26.

FIGURA 26: Pantalla restaurar copia de seguridad Fuente: Autor

Buscar libro

La búsqueda de libros permite al usuario conocer que libros existen o que han sido creados con anterioridad, la pantalla diseñada para esta funcionalidad se observa en la figura 27.

FIGURA 27: Pantalla buscar libro Fuente: Autor

---

<!-- Página 45 -->

36

Leer libro

La lectura del libro permite conocer a detalle la información que se encuentra almacenada en este, para ello se diseñó la pantalla de la figura 28.

FIGURA 28: Pantalla leer libro Fuente: Autor

Imprimir libro

La impresión del libro permite al usuario descargar en formato PDF un libro en específico, lo cual le permitirá suministrar este documento a personal que lo requiera. Si bien esta funciona- lidad no tiene una pantalla como tal en la figura 29 se presenta la imagen de la pantalla que se desplegará al querer generar el documento.

FIGURA 29: Pantalla imprimir libro Fuente: Autor

---

<!-- Página 46 -->

37

## 7.2. Pruebas

Al momento de desarrollar una aplicación es fundamental realizar pruebas para comprobar que esta funciona correctamente, dichas pruebas se deben ejecutar tanto por el desarrollador como por el cliente. El autor ejecutó las pruebas a la par del desarrollo de la aplicación, pues a medida que se desarrollaba una funcionalidad esta se contrastaba con el caso de uso respectivo, además en dichas pruebas se usaron diferentes datos que fueron proporcionados por el autor a la base de datos. A continuación, se expondrá más a detalle cada una de las pruebas realizadas por parte del autor de acuerdo a cada funcionalidad.

7.2.1. Pruebas realizadas por el desarrollador

Ingresar

Al abrir la aplicación se tendrá la pantalla de la figura 12 la cual servirá para acceder al sistema como tal, en esta pantalla el usuario ingresará su usuario y contraseña para que el sistema consulte si este se encuentra registrado y en caso de ser así el sistema le dará acceso a la pantalla principal como se evidencia en la figura 13.

Crear libro

Para crear un libro se da clic en el botón “crear libro” lo cual muestra la pantalla de la figura 14, posteriormente el usuario asigna el nombre deseado y da clic en aceptar, a lo cual el sistema crea el libro en la base de datos como se puede observar en la figura 30.

FIGURA 30: Prueba crear libro Fuente: Autor

Agregar asientos al libro

En esta funcionalidad lo primero que se debe hacer es dar clic sobre el botón de agregar asiento lo cual muestra la pantalla de la figura 15, posteriormente el usuario llena los campos requeri- dos y da clic en guardar lo cual hace que se muestre un mensaje de que la acción se ha realizado exitosamente. La comprobación de esto se puede observar en la figura 31 en donde se ha creado el registro dentro de la tabla asiento.

---

<!-- Página 47 -->

38

FIGURA 31: Prueba agregar asiento Fuente: Autor

Modificar asientos del libro

Para hacer uso de esta funcionalidad se debe dar clic sobre el botón modificar asiento que abre la pantalla de la figura 16, allí el usuario selecciona el asiento que desea modificar y da clic en modificar para abrir la pantalla de la figura 17, posteriormente modifica los datos que desea y da clic en guardar. El resultado de la modificación se observa en la figura 32 en donde se ha modificado el asiento creado en la funcionalidad anterior.

FIGURA 32: Prueba modificar asiento Fuente: Autor

Cerrar libro

Si se quiere realizar el cierre del mes se debe ir al botón cierre mensual el cual mostrará el men- saje de la figura 18, allí el usuario realizara la confirmación de la acción y el resultado de esta se ve reflejado en la figura 33, en donde el atributo cerrado del penúltimo mes se encuentra con el valor de 1. Ahora bien, para el cierre del libro los pasos son los mismos con la diferencia de que el sistema identificara cuando se esté en el mes de diciembre y una vez se cierre este mes también se realizará el cierre del libro. La comprobación de este segundo caso se ve reflejada en la figura 34 y al igual que para el mes el atributo cerrado se encuentra con el valor de 1.

FIGURA 33: Prueba cerrar mes Fuente: Autor

FIGURA 34: Prueba cerrar libro Fuente: Autor

---

<!-- Página 48 -->

39

Cambiar contraseña

El cambio de contraseña se puede realizar dando clic en el botón cambiar contraseña de la figura 13, esta acción hace que se muestre la pantalla de la figura 19 en donde el usuario digitará su nueva contraseña la cual debe cumplir con los requisitos que allí se muestran, cumplidos estos requisitos se habilita el botón guardar que será oprimido por el usuario. Finalmente, el cambio se puede observar en la figura 35 en donde el atributo contraseña del primer usuario corresponde a Prueba123, pero en formato varbinary.

FIGURA 35: Prueba cambiar contraseña Fuente: Autor

Configurar visualmente la aplicación

La configuración visual se realiza dando clic en el botón configurar app lo que hará que se muestre la pantalla de la figura 20, allí el usuario seleccionará la configuración deseada y dará clic en guarda, automáticamente el sistema toma esta configuración como se muestra en la figura 36, además esta configuración se guardar para este usuario mediante un archivo de texto plano que es nombrado con la identificación del usuario y se almacena en la carpeta donde se encuentra la aplicación como se observa en la figura 37.

FIGURA 36: Prueba configuración visual Fuente: Autor

---

<!-- Página 49 -->

40

FIGURA 37: Prueba archivo almacenado configuración visual Fuente: Autor

Restablecer contraseña

Cuando se quiere restablecer la contraseña se debe pulsar sobre “¿Olvido su contraseña?” el cual se observa en la figura 12, esto hará que se muestre la pantalla de la figura 22 donde el usuario digitará su usuario y el sistema enviará un correo electrónico con una contraseña generada aleatoriamente a la dirección asociada a este usuario como se observa en la figura 38, además el cambio también se puede observar en la base de datos en donde el primer usuario se le ha modificado la contraseña la cual corresponde a la enviada por correo, esto se puede observar en la figura 39. Cabe aclarar que la contraseña enviada por correo estará asignada para el usuario hasta que este desee cambiarla.

FIGURA 38: Prueba correo restablecimiento contraseña Fuente: Autor

FIGURA 39: Prueba base de datos restablecimiento contraseña Fuente: Autor

Programar copias de seguridad

Para programar las copias de seguridad se da clic en el botón programar copias de seguridad que se encuentra en la pantalla de la figura 13, posteriormente el sistema mostrará la pantalla de

---

<!-- Página 50 -->

41

la figura 21, allí el usuario seleccionará en el listado la opción que desea y dará clic en aceptar. Lo anterior hará que se cree un bloc de notas que contendrá el dato del tiempo en el que se hara la copia de seguridad como se observa en la figura 21. Ahora bien, con el uso de un servicio de Windows la copia se realiza sin necesidad de que la aplicación se encuentre en uso, dicho servicio almacena la copia en el equipo y en el drive como se observa en las figuras 41 y 42 respectivamente.

FIGURA 40: Prueba archivo almacenado configuración copia de seguridad Fuen- te: Autor

FIGURA 41: Prueba archivo almacenado en PC Fuente: Autor

FIGURA 42: Prueba archivo almacenado en Drive Fuente: Autor

---

<!-- Página 51 -->

42

Administrar usuarios

En la administración de usuarios se tienen 3 casos como lo son la creación, modificación y eliminación de usuarios, para poder hacer uso de estas funcionalidades se debe acceder a la pantalla de la figura 23, a continuación, se describirá el proceso para cada una de ellas:

Crear: A esta funcionalidad se accede dando clic en el botón crear lo cual hace que se muestre la pantalla de la figura 24 en donde el usuario digitará la información en los campos y dará clic en el botón confirmar, seguidamente el sistema mostrará la pantalla de la figura 25 en donde el usuario deberá ingresar la contraseña enviada a su correo con el fin de verificarlo, una vez ingresado el código el usuario dará clic en confirmar y el sistema mostrará un mensaje confirmando la creación del usuario. Lo anterior se puede evidenciar en la figura 43 en donde se puede observar que se ha agregado el usuario con idUsuario de 19.

Modificar: Para modificar un usuario primero se debe seleccionar uno dentro del listado y dar clic en el botón modificar lo cual hará que se muestre la pantalla de la figura 24, allí el usuario realizará los cambios necesarios y dará clic en confirmar a lo que el sistema responderá con un mensaje confirmando que el proceso se realizó correctamente. La comprobación del proceso anterior se puede observar en la figura 43 en comparación con la figura 23 en donde al usuario con identificación 857948 se le ha modificado el correo y rol pues ahora es invitado.

Eliminar: La eliminación de un usuario se realiza seleccionándolo y dando clic en el botón eli- minar, seguidamente el sistema solicitará la confirmación de la acción mediante un mensaje. El resultado de esta acción se puede observar en la figura 43 donde se muestran los diferentes usuarios que existen en la base de datos, allí se puede evidenciar que el usuario con identifica- ción 5678912 mostrado en la figura 23 ya no aparece en la tabla.

FIGURA 43: Prueba crear, modificar y eliminar usuario Fuente: Autor

Buscar libro

Para buscar libros basta con dar clic sobre el botón buscar libro que se encuentra en la figura 12, esta acción hará que se muestre la pantalla de la figura 27 en donde en el recuadro se observan los diferentes libros que se tienen.

---

<!-- Página 52 -->

43

Leer libro

Cuando se quiere leer un libro se debe estar en la pantalla de la figura 27, allí el usuario selec- cionará el libro que desea y presionará el botón leer para que así el sistema muestre la pantalla de la figura 28 la cual demuestra el correcto funcionamiento de esta funcionalidad pues en ella se puede observar el libro seleccionado en formato PDF.

Imprimir libro

Al igual que el caso anterior para esta funcionalidad se debe tener abierta la pantalla de la figura 27 para que así el usuario pueda seleccionar el libro que desea y posteriormente presionar el botón imprimir, esto hará que se despliegue la figura de la pantalla 29, en donde el usuario asignará un nombre, seleccionará la carpeta donde desea guardar el documento y finalmente dará clic en guardar. Con lo anterior se obtiene como resultado el documento PDF almacenado en la carpeta seleccionada como se observa en la figura 44.

FIGURA 44: Prueba imprimir libro Fuente: Autor

Restaurar copia de seguridad

Para evidenciar la restauración de la copia de seguridad primero se tiene la imagen de la figura 45 la cual pertenece al SQL Sever Management Studio, en donde la base de datos se encuentra totalmente vacía, pues previamente se ha obtenido una copia de seguridad con el fin de recu- perarla. Ahora bien, el proceso inicia al presionar el botón restaurar copia lo que hará que se muestre la pantalla de la figura 26, allí el usuario presionara el botón agregar en donde se le mostrara la pantalla de la figura 46, de esta manera podrá seleccionar el archivo que desea res- tablecer, una vez seleccionado el archivo el usuario presionara el botón cargar donde el sistema mostrara un mensaje preguntando si se desea realmente restablecer la copia de seguridad a lo que el usuario presionara el botón si, finalmente el sistema mostrara un mensaje confirmando que la copia se restauró satisfactoriamente. Para comprobar este proceso se revisa la base de

---

<!-- Página 53 -->

44

datos en donde esta se encuentra nuevamente con información en las tablas como se observa en la figura 47.

FIGURA 45: Tablas de la base de datos vacias Fuente: Autor

FIGURA 46: Prueba selección copia de seguridad Fuente: Autor

FIGURA 47: Tablas de la base de datos nuevamente con información Fuente: Au- tor

---

<!-- Página 54 -->

45

7.2.2. Pruebas realizadas por el párroco

La ejecución de las pruebas por parte del párroco se realizó inicialmente en el equipo que se desarrolló la aplicación, posteriormente se ejecutó una prueba final en el equipo del usuario. En el proceso de pruebas el párroco uso un libro real y verifico cada una de las funcionalidades contrastándolas con los documentos de los casos de uso, en caso de encontrar un error este procedía a reportarlo y el desarrollador verificaba si era de desarrollo o era un requerimiento nuevo, en caso de que fuera un error de desarrollo se corregía y se realizaba nuevamente la prueba hasta que se obtuviera la aprobación. La aprobación final se puede observar en el anexo 16, además, en la figura 48 se observa el diagrama del proceso descrito anteriormente.

FIGURA 48: Proceso de pruebas realizadas por el párroco Fuente: Autor

## 7.3. Implementación

El proceso de implementación inicio con la instalación del SQL SERVER y el Management Stu- dio, esto con el fin de poder tener la base de datos dentro del computador del usuario, además, con esta instalación fue posible conocer el nombre del servidor como se observa en la figura 49, luego de esto se procedió a configurar en el Visual Studio el archivo App.Config que esta- blece la conexión de la aplicación con la base de datos, de esta manera fue posible generar el instalador de la aplicación como se observa en la figura 50.

---

<!-- Página 55 -->

46

FIGURA 49: Pantalla de ingreso a SQL SERVER Fuente: Autor

FIGURA 50: Instalador y carpeta con librerías de la aplicación generada Fuente: Autor

Seguidamente, se procedió a instalar la aplicación y el servicio de Windows como se observa en las figuras 51 y 52, lo cual arrojo como resultado las figuras 53 y 54, en donde se puede observar que ambas herramientas se encuentran instaladas y listas para su uso.

FIGURA 51: Pantalla instalando la aplicación Fuente: Autor

---

<!-- Página 56 -->

47

FIGURA 52: Pantalla instalando el servicio Fuente: Autor

FIGURA 53: Comprobación de aplicación instalada Fuente: Autor

FIGURA 54: Comprobación de servicio instalado Fuente: Autor

---

<!-- Página 57 -->

48

## 7.4. Características del software obtenido

Finalmente, según los expuesto en la sección 5.5 del capitulo 5 un software debe contar con ciertas características para ser catalogado como una buena herramienta, es por ello que a conti- nuación se expondrán las características con las que cuenta el software obtenido, además de la funcionalidad que se encarga de dar cumplimiento a cada característica.

Fácil uso: Esta característica se asocia a su interfaz gráfica pues esta es sencilla e intuitiva lo que hace que el software sea de fácil manejo.

Automático: Al realizar el ingreso de información se generará información relevante lo cual se cumple con la funcionalidad agregar asientos, además la información generada se ve reflejada en cada uno de los cálculos que realiza el software y así llevar a cabo el libro.

Seguro: La seguridad del software se garantiza mediante la administración de usuarios pues se cuenta con dos roles (Administrador e invitado) que servirán para limitar el acceso de los usuarios invitados a ciertas funcionalidades, además cada uno de estos usuarios contará con su respectiva clave lo cual garantiza aún más la seguridad de los datos en el sistema.

Reportes básicos: Los reportes se generan el formato PDF y se pueden observar dentro del software o fuera de él, esta característica se cumple con las funcionalidades leer libro e imprimir libro.

7.4.1. Requisitos mínimos para la operación del sistema

Para obtener los requerimientos mínimos de operación del sistema se tuvo en cuenta los reque- rimientos para el Windows 7 los cuales se evidencian en el cuadro 2, además, se tienen los del motor de base de datos que se evidencian en el cuadro 1 y los de la aplicación que se observan en el cuadro 3.

SQL SERVER 2014 Componente Requerimientos minimos Procesador Velocidad 1GHz Memoria RAM 512MB Disco duro 4.2GB

CUADRO 1: Requerimientos minimos SQL SERVER 2014

---

<!-- Página 58 -->

49

Windows 7 Componente Requerimientos minimos Procesador Velocidad 1GHz Memoria RAM 1GB Disco duro 16GB

CUADRO 2: Requerimientos minimos Windows 7

Aplicación de teneduria Componente Requerimientos minimos Procesador Velocidad 2.5GHz Memoria RAM 80MB Disco duro 17MB .NET Framework 4.7.2 Sistema operativo Windows 7 Motor de base de datos SQL SERVER 2014

CUADRO 3: Requerimientos minimos de la aplicación

Analizando cada una de las tablas se pueden obtener los requerimientos totales de la aplicación los cuales se observan en el cuadro 4.

Requerimientos totales Componente Requerimientos minimos Procesador Velocidad 2.5GHz Memoria RAM 2GB Disco duro 17GB .NET Framework 4.7.2 Sistema operativo Windows 7 Motor de base de datos SQL SERVER 2014

CUADRO 4: Requerimientos minimos de totales la aplicación

---

<!-- Página 59 -->

# Capítulo 8

# Impacto social

Chaguaní es un municipio que cuenta aproximadamente con 3.845 habitantes, de los cuales se estima que el 75 % de esta población es católica [29]. Teniendo en cuenta que el impacto principal lo tendrá el párroco no se puede dejar a un lado a sus creyentes quienes también se verán involucrados, pues este podrá tener la información contable más ordenada con lo cual dará un mejor manejo a los recursos que son aplicados a sus fieles, además estos podrán tener acceso a la información y así conocer a donde han sido dirigidos los ingresos.

Ahora bien, también se deja abierta la posibilidad de impactar a futuro a una mayor parte de la comunidad que trabaja con la Parroquia, a la cual se le facilitará su trabajo con la aplicación de nuevos módulos en el sistema.

50

---

<!-- Página 60 -->

# Capítulo 9

# Conclusiones

Al realizar las pruebas se obtiene la validación del párroco, lo cual implica que las fun- cionalidades de la aplicación cumplen las expectativas de un sistema para reemplazar el método tradicional de teneduría de libros en papel al método electrónico, además garan- tiza a la aplicación como una posible solución a las necesidades de teneduría de libros en la Parroquia Santuario Señor de La Salud de Chaguaní.

El levantamiento de requerimientos no funcionales permitió identificar las restricciones con las cuales se debía desarrollar el sistema, dichas restricciones se asociaron a las espe- cificaciones del equipo, no cobro de la aplicación, entre otros.

Al realizar la investigación para determinar el proceso de teneduría se identificó la exis- tencia de más libros, sin embargo, estos no son usados en la Parroquia por lo que no fue necesaria su implementación.

Gracias al desarrollo de la aplicación en tres capas se facilitó responder adecuadamen- te y con un mínimo impacto en tiempo adicional a los requerimientos no definidos en un inicio como fueron: Verificación de la existencia del correo electrónico y cierre anual mediante el cierre mensual en el mes de diciembre.

La aplicación diseñada cumple con los tres pilares de la seguridad de la información, pues la integridad de los datos se garantizó mediante un diseño relacional en la base de datos donde además los procesos y cálculos se realizan correctamente, ahora bien, la confiden- cialidad se garantizó ya que se realizó una aplicación de escritorio a la cual solo podrán tener acceso las personas que puedan usar el computador, otro factor que garantiza este pilar es la implementación de la contraseña para ingresar al sistema y roles ya que de- pendiendo de este se tiene acceso a ciertas funcionalidades, finalmente la disponibilidad

51

---

<!-- Página 61 -->

52

no se garantiza al 100 % pues se requería una aplicación de escritorio, sin embargo esto se cubre en cierta parte ya que la información estará disponible y segura mediante las copias de seguridad que se almacenaran en la nube.

---

<!-- Página 62 -->

# Capítulo 10

# Trabajos futuros y recomendaciones

Finalizado el desarrollo se abre la posibilidad de trabajar a futuro con más módulos como in- ventario, facturación y libro mayor, esto con el fin de que la aplicación no sea solamente imple- mentada en la Parroquia, sino que se pueda expandir a mas entidades.

53

---

<!-- Página 63 -->

# Anexos

ANEXO 1: Caso de uso crear libro

54

---

<!-- Página 64 -->

55

ANEXO 2: Caso de uso agregar asientos al libro

---

<!-- Página 65 -->

56

ANEXO 3: Caso de uso modificar asientos del libro

---

<!-- Página 66 -->

57

ANEXO 4: Caso de uso cerrar libro

---

<!-- Página 67 -->

58

ANEXO 5: Caso de uso ingresar

---

<!-- Página 68 -->

59

ANEXO 6: Caso de uso cambiar contraseña

---

<!-- Página 69 -->

60

ANEXO 7: Caso de uso configuración visual

---

<!-- Página 70 -->

61

ANEXO 8: Caso de uso programar copias de seguridad

---

<!-- Página 71 -->

62

ANEXO 9: Caso de uso restablecer contraseña

---

<!-- Página 72 -->

63

ANEXO 10: Parte 1 caso de uso administrar usuarios

---

<!-- Página 73 -->

64

ANEXO 11: Parte 2 caso de uso administrar usuarios

---

<!-- Página 74 -->

65

ANEXO 12: Caso de uso buscar libro

---

<!-- Página 75 -->

66

ANEXO 13: Caso de uso leer libro

---

<!-- Página 76 -->

67

ANEXO 14: Caso de uso imprimir libro

---

<!-- Página 77 -->

68

ANEXO 15: Caso de uso restaurar copia de seguridad

---

<!-- Página 78 -->

69

ANEXO 16: Aceptación de funcionalidades

---

<!-- Página 79 -->

70

Requerimientos no funcionales Se tendrá un rol administrador que contara con todos los permi- Roles sos. Se tendrá un segundo rol que será un rol invitado el cual solo podrá visualizar los archivos mas no modificar ni ningún otro permiso. Las copias de seguridad se almacenarán en el drive, además, se Copias de seguridad realizarán de forma programada. Permita al usuario el movimiento y modificación del tamaño de Facilidad de uso las ventanas. El sistema debe ser intuitivo y de fácil manejo para el usuario. Interfaz Se podrán modificar los colores y el tamaño de la letra. Se debe mostrar el nombre de la Parroquia al abrir la aplicación, además de la pantalla de ingreso. El sistema no se debe bloquear para el usuario más de 10 segun- Rendimiento dos. Disponibilidad del sistema La sesión se debe cerrar después de 10 minutos de inactividad. Arquitectura El diseño debe ser para una aplicación de escritorio. El sistema debe estar diseñado un computador que cuenta un procesador Intel Celeron 2.50 GHz y 2 GB de memoria RAM y un sistema operativo Windows 10 a 32 bits. El sistema debe controlar la complejidad de la contraseña. (Com- Seguridadbinación de caracteres numéricos, alfabéticos (Mayúsculas y mi- núsculas) y signos o caracteres especiales). El sistema debe controlar la longitud mínima y máxima de las contraseñas, la cual debe ser de ocho a nueve caracteres. No se debe permitir guardar las contraseñas. Se tendrán tres intentos para el ingreso de la contraseña, una vez superada esta cantidad el sistema debe solicitar a este usuario restablecer la contraseña mediante correo electrónico. Otros Se debe mostrar el listado de los libros que existen. Permite la modificación de datos si no se ha hecho el cierre diario. Se debe permitir generar el documento (PDF) con la información que se haya trabajado hasta el momento. La aplicación debe ser totalmente gratuita.

ANEXO 17: Requerimientos no funcionales

---

<!-- Página 80 -->

# Bibliografía

[1] K. Garrido. Contrapartida 722. 2013. URL: https://incp.org.co/Site/news/red/ contrapartida/722.pdf.

[2] Decreto 1625 de 2016. Oct. de 2016. URL: http : / / www . suin - juriscol . gov . co / viewDocument.asp?ruta=Decretos/30030361 (visitado 03-06-2021).

[3] Compra de Licencia Softland Pyme. 2021. URL: https://softland.com.co/cotizador- pyme/compra-de-licencia/ (visitado 02-06-2021).

[4] Precios Software Siigo: Software administrativo y contable en la nube. 2021. URL: https:// www.siigo.com/precios-siigo/ (visitado 02-06-2021).

[5] D. Napa. «Desarrollo de un Software Contable para mejorar los Flujos de Información Financiera en la Empresa Cachito S.A». Tesis doct. Instituto Superior Tecnológico Boli- variano de Tecnologia, 2018, pág. 112. URL: https://repositorio.itb.edu.ec/ handle/123456789/1564.

[6] S. Chicaiza y E. Diaz. «Diseño de un sistema contable en el centro de mecanización unión y trabajo, Cantón Salcedo Parroquia Mulalillo». Tesis doct. Universidad Técnica de Co- topaxi, 2019, pág. 60. URL: http://repositorio.utc.edu.ec/handle/27000/ 7591.

[7] Ing. Z. Salamanca e Ing. D. Rodríguez. «Formulación del proyecto de desarrollo del soft- ware contable y financiero de la Compañía NOVALTEC S . A . S . basado en las Normas Internacionales de Información(NIIF)». Tesis doct. Universidad Distrital Francisco José de Caldas, 2017, pág. 180.

[8] A. Castellón y R. Vergara. «Diseño e implementación de un software contable que apoye la gestión en las tiendas de barrio, de Cartagena de Indias». En: Sostenibilidad, Tecnología y Humanismo 10.1 (2019), pág. 7. ISSN: 2216-1864. DOI: 10.25213/2216-1872.1.

71

---

<!-- Página 81 -->

72

[9] A. García, A. Peña y L. Prada. «Diseño e implementación de una herramienta contable pa- ra la cafetería típicas te da gusto». Tesis doct. Unidades Tecnológicas de Santander, 2020. URL: http://repositorio.uts.edu.co:8080/xmlui/handle/123456789/ 4077.

[10] J. Camargo. «Implementación de software de facturación que consolide la contabilidad en el hotel1525 de Santa Marta». Tesis doct. Universidad del Magdalena, 2021, pág. 24. URL: https://repositorio.unimagdalena.edu.co/items/43b4c68c-c569- 426e-bada-ab1d45375b51.

[11] R. Oltra. Evolución histórica de los Sistemas de información : Del software contable al ERP. Inf. téc. Universitat Politècnica de València, 2015, pág. 10.

[12] EL ESPECTADOR. Grandes líderes de software contable se unen en Colombia. 2019. URL: https : / / www . elespectador . com / tecnologia / grandes - lideres - de - software-contable-se-unen-en-colombia-articulo-839195.

[13] Decreto 0019 de 2012. Ene. de 2012. URL: http : / / www . suin - juriscol . gov . co / viewDocument.asp?id=1004430 (visitado 03-06-2021).

[14] Ley 1314 de 2009. Jul. de 2009. URL: http://www.suin-juriscol.gov.co/viewDocument. asp?id=1677255 (visitado 03-06-2021).

[15] A. Hernández. Los sistemas de información: evolución y desarrollo. Inf. téc. 10. Universidad de Zaragoza, 2003, pág. 15.

[16] R. Andreu y col. Estrategia y sistemas de información. Management (McGraw-Hill). McGraw- Hill, 1996. ISBN: 9788448105082. URL: https://books.google.com.ec/books?id= Dvb6OwAACAAJ.

[17] E. Pico y S. Núñez. «El software contable como herramienta técnica en las microempresas de la provincia de Santa Elena, Ecuador». En: Killkana Social 2.1 (2018), pág. 6. ISSN: 2528- 8008. DOI: 10.26871/killkana_social.v2i1.242.

[18] A. Lozano y L. Lozano. «Desarrollo e implementación del módulo de contabilidad, car- tera en el sistema de administración electrónica (SAEL) basado en el framework JBoss Seam para la empresa Provar Colombia S.A». Tesis doct. Universidad Francisco de Paula Santander Ocaña, 2015, pág. 118.

[19] J. Regalado. «Diseño E Implementación De Un Software Contable Y Su Influencia En La Gestión De La Información Empresarial, Caso: Empresa Distribuidora Comercial Delga- do S.R.L., Octubre-2014». Tesis doct. Universidad Católica Santo Toribio de Mogrovejo, 2016, pág. 95. URL: http://tesis.usat.edu.pe/xmlui/handle/20.500.12423/ 717.

---

<!-- Página 82 -->

73

[20] Y. Mora. «Los sistemas de información contable y su relación con las herramientas tec- nológicas». Tesis doct. Universidad de Bogotá Jorge Tadeo Lozano, 2017, pág. 29. ISBN: 9788578110796. arXiv: arXiv:1011.1669v3.

[21] Dr. G. Vásquez. ¿Libros de contabilidad físicos o electrónicos? Jun. de 2017. URL: https:// cijuf.org.co/documentos-de-interes/2017/libros-de-contabilidad- fisicos-o-electronicos (visitado 22-09-2021).

a [22] W. Label, J. Ledesma y R. Ramos. Contabilidad para no contadores. 2.ed. 2016. ISBN: 9789587712988. URL: https : / / www . ecoeediciones . com / wp - content / uploads / 2016 / 08 / Contabilidad-para-no-contadores-2ed.pdf.

[23] I. Sommerville. Ingeniería de software. Séptima edición. 2005. ISBN: 8478290745. URL: http: //zeus.inf.ucv.cl/~bcrawford/AULA_ICI_3242/Ingenieria%5C%20del% 5C%20Software%5C%207ma.%5C%20Ed.%5C%20-%5C%20Ian%5C%20Sommerville. pdf.

[24] Siigo. ¿Qué son los registros contabales? 2021. URL: https://www.siigo.com/blog/ contador/que-son-los-registros-contables/ (visitado 18-08-2021).

[25] R. García. Los libros oficiales de la contabilidad. Ago. de 2016. URL: https://occidente. co / area - legal / los - libros - oficiales - de - la - contabilidad/ (visitado 18-08-2021).

[26] Anexos Técnicos del Decreto 2270 de 2019. Dic. de 2019. URL: https : / / www . suin - juriscol . gov . co / imagenes / /18 / 12 / 2019 / 1576700747867 _ Anexos % 5C % 20Tecnicos%5C%20Compilatorios%5C%20- Incluidos%5C%20en%5C%20el% 5C%20Diario%5C%20Oficial%5C%2051166.pdf (visitado 17-09-2021).

[27] Ley 527 de 1999. Ago. de 1999. URL: http : / / www . suin - juriscol . gov . co / viewDocument.asp?id=1662013 (visitado 22-09-2021).

[28] O. Ureña. Contabilidad básica. 2010. ISBN: 9789589860069. URL: https://www.sanmateo. edu.co/documentos/publicacion-contabilidad-basica.pdf.

[29] DANE. Proyecciones de población hasta el 2020 del DANE. Inf. téc. DANE. URL: http:// www.dane.gov.co/files/investigaciones/poblacion/proyepobla06_20/ ProyeccionMunicipios2005_2020.xls.

——————————————————————–