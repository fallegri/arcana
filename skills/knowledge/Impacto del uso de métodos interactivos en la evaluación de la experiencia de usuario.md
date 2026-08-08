<!-- Página 1 -->

UNIVERSIDAD DE COSTA RICA SISTEMA DE ESTUDIOS DE POSGRADO

IMPACTO DEL USO DE MÉTODOS INTERACTIVOS EN LA EVALUACIÓN DE LA EXPERIENCIA DE USUARIO

Trabajo final de investigación aplicada sometido a la consideración de la Comisión del Programa de Posgrado en Computación e Informática para optar al grado y título de Maestría Profesional en Computación e Informática

DEIVERT GUILTRICHS CORDERO

Ciudad Universitaria Rodrigo Facio, Costa Rica

2024

---

<!-- Página 2 -->

DEDICATORIA

A mi hijo Ryan Guiltrichs. La sonrisa con la que escribo esta dedicatoria y la misma que he tenido los últimos 11 años, la has dibujado con la felicidad que me das cada día. Te amo Rayo.

ii

---

<!-- Página 3 -->

AGRADECIMIENTO

A don Gustavo López, don Ignacio Díaz y doña Kryscia Ramírez quienes me entregaron todas las herramientas, impulso y motivación para el desarrollo de esta investigación. Y en general a la UCR. A don Georges Alfaro, gracias a usted aprendí una de las cosas que más me gustan en la vida, programar. Hay un antes y un después de aquella primera clase de Programación I en la UNA. A mi madre, Estrella Cordero y a mi tía, que es como otra madre, Miriam Cordero que me han dado tanto amor, cada día. A mi tío, Jesús Cordero que, siempre me ha cubierto las espaldas y nunca me ha dejado caer (aunque a veces me saque de quicio). A la Universidad Fidélitas, por dejarme hacer lo que más me gusta en la vida, educar. Al MOPT, en especial a Orlando, Byron, Alonso y don Carlos Olivas, gracias a ustedes soy hoy el profesional que siempre soñé ser. A Panji, Pepe, Padawan y Negrito, es un honor ser el líder de su manada. A Danny Mora y Pablo Morales, Jean Carlo y Alexander Saénz mis hermanos de otra madre. Y finalmente al Manchester United, amor eterno desde el 26 de mayo de 1999, que me permitió conocer a Chris, Beto, Mario, Masco, los Calis, Shoshua, Elias, Randy, Carlos, Tony, Joel, Ale, Adrián, Javi, Cedeño, Daniel, Sando, Ronald, Piña y en especial a Edu. Gracias por tanto amor y por darme el espacio para ser yo mismo.

iii

---

<!-- Página 4 -->

Este trabajo final de investigación aplicada fue aceptado por la Comisión del Programa de Posgrado en Computación e Informática de la Universidad de Costa Rica, como requisito parcial para optar al grado y título de Maestría Profesional en Computación e Informática.

______________________________________ Dr. Luis Quesada Quirós Representante de la Decana Sistema de Estudios de Posgrado

______________________________________ Dr. Gustavo López Herrera Profesor Guía

________________________________________ Dr. Ignacio Díaz Oreiro Lector

________________________________________ Dra. Kryscia Ramírez Benavides Lectora

________________________________________ Dr. Adrián Lara Petitdemange Representante Programa de Posgrado en Computación e Informática

________________________________________ Deivert Guiltrichs Cordero Sustentante

iv

---

<!-- Página 5 -->

TABLA DE CONTENIDO

DEDICATORIA .....................................................................................................................ii

AGRADECIMIENTO .......................................................................................................... iii

TABLA DE CONTENIDO .................................................................................................... v

RESUMEN ......................................................................................................................... viii

ABSTRACT...........................................................................................................................ix

LISTA DE TABLAS .............................................................................................................. x

LISTA DE FIGURAS ............................................................................................................xi

CAPÍTULO I. INTRODUCCIÓN .......................................................................................... 1

Justificación ....................................................................................................................... 3

Objetivos ............................................................................................................................ 5

Objetivo general ................................................................................................................ 5

Objetivos específicos ......................................................................................................... 5

CAPÍTULO II. ESTADO DEL ARTE ................................................................................... 7

Objetivo de la revisión de literatura ............................................................................... 8

Metodología aplicada para la revisión de literatura...................................................... 8

Criterios de elegibilidad ............................................................................................... 9

Descripción del proceso de búsqueda .......................................................................... 9

Resultados de la revisión de literatura .......................................................................... 10

Distribución de las técnicas de evaluación utilizadas .............................................. 10

Elementos de experiencia de usuario evaluados ...................................................... 11

Objetivos de la evaluación de experiencia de usuario ............................................. 13

Utilización de técnicas gamificadas ........................................................................... 15

Evaluación de hallazgos.................................................................................................. 16

v

---

<!-- Página 6 -->

CAPÍTULO III. MARCO CONCEPTUAL.......................................................................... 17

CAPÍTULO IV. METODOLOGÍA ...................................................................................... 20

Contexto ........................................................................................................................... 21

Procedimiento.................................................................................................................. 22

Plan piloto .................................................................................................................... 22

Primera etapa .............................................................................................................. 24

Segunda etapa ............................................................................................................. 25

Tercera etapa............................................................................................................... 25

Instrumentos .................................................................................................................... 26

Cuestionario estandarizado meCUE ......................................................................... 27

Cuestionario gamificado meCUE .............................................................................. 28

UEQ (User Experience Questionnaire) ..................................................................... 32

CAPÍTULO V. RESULTADOS. .......................................................................................... 34

Hallazgos del plan piloto ................................................................................................ 34

Características demográficas de la investigación ........................................................ 35

Evaluación meCUE estandarizada de Chat GPT ........................................................ 36

Evaluación meCUE gamificada de Chat GPT ............................................................. 37

Resultados sobre la comparación de meCUE estandarizado y meCUE gamificado 37

Resultados de Evaluación UEQ de meCUE Estandarizado y meCUE Gamificado . 39

CAPÍTULO VI. CONCLUSIONES ..................................................................................... 42

REFERENCIAS.................................................................................................................... 46

ANEXO 1 ............................................................................................................................. 51

Cuestionario estandarizado meCUE ............................................................................. 51

ANEXO 2 ............................................................................................................................. 56

Cuestionario gamificado meCUE .................................................................................. 56

vi

---

<!-- Página 7 -->

ANEXO 3 ............................................................................................................................. 62

Cuestionario UEQ utilizado para la evaluación de las herramientas meCUE (tanto gamificada como estandarizada) ................................................................................... 62

ANEXO 4 ............................................................................................................................. 65

Artículo presentado en las Jornadas Costarricenses de Investigación en Computación e Informática (JOCICI), del año 2023. ................................................. 65

vii

---

<!-- Página 8 -->

RESUMEN

La evaluación de la experiencia del usuario (UX) es esencial para las organizaciones, ya que les permite generar ventajas competitivas. Existen varias herramientas de evaluación de UX para sistemas de información, entre las cuales las más utilizadas son los cuestionarios estandarizados. Sin embargo, en los últimos años, han comenzado a ganar protagonismo técnicas más interactivas, como las metodologías gamificadas que buscan incorporar técnicas de juegos para atraer un mayor interés de los evaluadores. Esta investigación tiene como objetivo evaluar el posible impacto en la evaluación de la experiencia de usuario, con la incorporación de mecanismos gamificados en el uso de cuestionarios estandarizados, tanto en la propia evaluación de aplicaciones de software como en la aplicación de las propias evaluaciones.

En su aplicación final el trabajo incluyó la realización de un caso de estudio en el que participaron 60 personas mayores de 18 años, quienes utilizaron dos tipos de cuestionarios basados en la herramienta meCUE (un cuestionario para evaluación de experiencia de usuario modularizado), una gamificada y otra estandarizada, la primera utilizada por 26 evaluadores y la segunda por 34 de ellos. Adicionalmente, todos los participantes completaron un cuestionario final (UEQ) que permitió evaluar ambas versiones del cuestionario meCUE.

Se seleccionó el software Chat GPT para ser evaluado en ambas versiones del cuestionario meCUE, con resultados que no determinan diferencias significativas en ninguna de las diez escalas de evaluación dispuestas, lo que sugiere que ambas implementaciones son igualmente efectivas en la evaluación de la experiencia del usuario mediante herramienta seleccionada. Sin embargo, en la evaluación de experiencia de usuario, utilizando la herramienta UEQ (un cuestionario para evaluación de experiencia de usuario, aplicado a ambas versiones de meCUE), se observó una evaluación generalmente mejor para la versión gamificada, siendo significativa en la escala de Novedad.

viii

---

<!-- Página 9 -->

ABSTRACT

User Experience (UX) evaluation is essential for organizations, as it enables them to gain a competitive advantage. There are various UX evaluation tools for information systems, with standardized questionnaires being the most commonly used. However, in recent years, more interactive techniques, such as gamified methodologies that aim to incorporate gaming elements to capture greater interest from evaluators, have been gaining prominence. This research aims to assess the potential impact on user experience when using standardized questionnaires by integrating gamification elements, both in the evaluation of software applications and the evaluation process itself.

In the final application of the study, a case study was conducted involving 60 participants aged 18 and above. They used two types of questionnaires based on the meCUE tool, one gamified and the other standardized. The gamified version was used by 26 evaluators, while the standardized version was used by 34. Additionally, all participants completed a final questionnaire (UEQ) that allowed the evaluation of both versions of the meCUE questionnaire.

The software Chat GPT was selected to be evaluated in both versions of the meCUE questionnaire, with results indicating no significant differences in any of the ten evaluation scales. This suggests that both implementations are equally effective in evaluating the user experience of the selected tool. However, in the User Experience Questionnaire (UEQ), a generally better evaluation was observed for the gamified version, particularly in the novelty scale.

ix

---

<!-- Página 10 -->

LISTA DE TABLAS

Tabla 1. Escalas de UEQ y sus enfoques de evaluación. ...................................................... 32

Tabla 2. Resumen de características demográficas .............................................................. 35

Tabla 3. Prueba de valores Wilcoxon para muestras independientes en la aplicación del

meCUE estandarizado y gamificado..................................................................................... 39

x

---

<!-- Página 11 -->

LISTA DE FIGURAS

Figura 1. Preguntas de investigación para la revisión de literatura. ....................................... 8

Figura 2. Artículos según el tipo de técnica utilizada por los autores. ................................. 11

Figura 3. Combinaciones de elementos de experiencia de usuario utilizados por los usuarios

según el tipo de técnica aplicada........................................................................................... 13

Figura 4. Distribución de los objetivos de evaluación de experiencia de usuario. ............... 14

Figura 5. Estrategia metodológica en relación con los objetivos de la investigación........... 21

Figura 6. Versión estandarizada de meCUE utilizada en el plan piloto de la presente

investigación. ........................................................................................................................ 23

Figura 7. Versión gamificada meCUE utilizada en el plan piloto de la presente

investigación. ........................................................................................................................ 24

Figura 8. Cuestionario estandarizado meCUE en línea que imita la evaluación original..... 28

Figura 9. Cuestionario meCUE gamificado en línea, que muestra el aspecto básico de su

implementación incluyendo los potenciadores, a Mario y su rival en el Módulo I. ............. 30

Figura 10. Potenciadores asignados de forma aleatoria al hacer clic en las cajas relacionadas

a la escala likert de cada enunciado de meCUE. .................................................................. 31

Figura 11. Perspectiva del movimiento de Mario en diferentes escenarios contra diferentes

rivales (muestra del Módulo I, en donde el jugador compite contra Luigi). ........................ 31

Figura 12. Estructura de la evaluación global del cuestionario meCUE gamificado,

utilizando elementos del juego "Mario Kart". ...................................................................... 31

Figura 13. Cuestionario UEQ utilizado por los participantes para evaluar la herramienta

meCUE (gamificada o estandarizada según correspondiese). .............................................. 33

xi

---

<!-- Página 12 -->

Figura 14. Espacio para comentarios adicionales dentro del cuestionario UEQ aplicado a

los participantes. ................................................................................................................... 33

Figura 15. Comparación general entre los cuestionarios meCUE estandarizados y

gamificados. .......................................................................................................................... 38

Figura 16. Resultados de las evaluaciones gamificadas y estandarizadas de meCUE basadas

en su comparación con el cuestionario UEQ. ....................................................................... 40

Figura 17. Percepción de los participantes, descrita en una sola palabra, para ambas

herramientas meCUE. ........................................................................................................... 41

xii

---

<!-- Página 13 -->

1

CAPÍTULO I. INTRODUCCIÓN

Actualmente, en relación con la experiencia de usuario, definida en el estándar ISO 9241- 210 como las percepciones y respuestas de una persona que resultan del uso, o un anticipado uso de un producto sistema o servicio [1], tanto los desarrolladores como los usuarios de tecnologías de información, comprenden, en la mayoría de los casos que, su evaluación certera y a conciencia, puede derivar en mejores resultados en la construcción, mejora y gestión de sistemas de información.

A partir de lo anterior, en años recientes se han desarrollado técnicas para la evaluación de experiencia de usuario sumamente específicas y dedicadas a facilitar la obtención de retroalimentación por parte de los usuarios finales relacionados a tecnologías de información [2].

Según un estudio realizado en el año 2016, por Loiola et al. [3], la gran mayoría de evaluaciones de experiencia de usuario son ejecutadas a través de cuestionarios estandarizados (84%), las cuales son aplicadas de forma individual o en combinación con otras técnicas, mientras tanto, para el año 2018 [4] y 2019 (como se detallará en el Capítulo de Estado del Arte del presente documento) se puede observar que, se comienzan a utilizar con más frecuencia, otro tipo de evaluaciones orientadas principalmente a la aplicación de herramientas interactivas de evaluación.

Es por esto que, resulta atractivo determinar si la tendencia descrita en el párrafo anterior sobre la utilización de técnicas de evaluación interactivas, podría estar relacionada a que estas impactan de alguna forma la recolección de resultados, que difiera de lo que hasta el momento se puede lograr mediante el uso de cuestionarios estandarizados.

Las herramientas de evaluación interactivas de experiencia de usuario son aplicaciones, sistemas o metodologías que permiten a los diseñadores, desarrolladores y equipos de UX (Experiencia de Usuario, por sus siglas en idioma inglés) analizar y medir la calidad de la

---

<!-- Página 14 -->

2

experiencia del usuario en sus productos, ya sean sitios web, aplicaciones móviles, software o cualquier otro tipo de interfaz, a través de espacios que permiten al usuario interactuar con dichas herramientas de forma más dinámica, mediante la integración de elementos externos al entorno laboral o educativo, como puede ser el uso de realidad virtual, juegos, “storytelling”, mapas de empatía, entre otras. Estas herramientas buscan generar una mejora de la usabilidad y la satisfacción del usuario, así como en la optimización de las evaluaciones de productos y servicios [5].

Ejemplo de estas técnicas de evaluación interactivas son aquellas que se ejecutan mediante la aplicación de técnicas gamificadas (aplicación de elementos de juego a contextos educativos-profesionales) de evaluación de experiencia de usuario, que nacen con el objetivo de reducir factores de presión y fuentes de estrés, a través de la aplicación de procedimientos de evaluación guiados por procesos de juegos e interacciones lúdicas (relativas a juegos) entre los usuarios y las herramientas a utilizar [6].

Sin embargo, no existe referencia de investigación alguna (ver Capítulo de Estado del Arte) hasta el momento que realice una comparación entre el uso de cuestionarios estandarizados y técnicas gamificadas en evaluación de experiencia de usuario. Por lo que, resulta motivante verificar si el comportamiento señalado anteriormente, sobre la aplicación más frecuente de técnicas interactivas en la evaluación de experiencia de usuario, podría deberse a que su utilización, específicamente en lo que respecta a metodologías gamificadas, se da como resultado de que estas generen algún impacto específico y notable en el proceso de evaluación de experiencia de usuario en contraste con los cuestionarios estandarizados, lo cual constituye el principal objetivo de la investigación a realizar.

En general, a partir de la presente investigación se pretende que, tanto investigadores como evaluadores, dispongan de información concreta sobre metodologías alternativas para la evaluación de experiencia de usuario, principalmente en el campo de la gamificación. Esto, poniendo a disposición no solo los resultados específicos de este trabajo, sino también, las herramientas a adaptar y construir, para que puedan ser aplicadas en procesos de evaluación de experiencia de usuario como tal o como parte investigaciones adicionales.

---

<!-- Página 15 -->

3

A continuación, se presenta un apartado que se centra en describir la justificación del presente estudio, en donde se describe a mayor profundidad la motivación del trabajo realizado y se delimitan los alcances de este.

Justificación

La evaluación de la experiencia de usuario es vital en el desarrollo de sistemas de información ya que, mediante su uso es posible generar ventaja competitiva al incrementar las ganancias y reducir los costos, esto porque permite diagnosticar, identificar y solucionar posibles errores en las aplicaciones de software que se entregarán a sus usuarios finales [7].

Dado lo anterior, se torna indispensable obtener de los usuarios la mejor retroalimentación posible al implementar sistemas de información por lo que, resulta interesante definir si la metodología y contexto de aplicación de herramientas específicas para evaluación de experiencia de usuario, podrían impactar los resultados obtenidos.

Las técnicas interactivas, en específico las gamificadas (en las que se concentra la presente investigación) de evaluación de experiencia de usuario buscan adicionalmente, aplicar una metodología más dinámica en comparación con aquellas que se implementan a través de cuestionarios estandarizados. Estos métodos, a partir de juegos, pretenden: eliminar presiones, evitar sesgos al recibir respuestas memorizadas o monótonas y principalmente obtener resultados más certeros apostando a la empatía de los usuarios que evalúan los sistemas de información [8].

De forma concreta, al aplicar gamificación en evaluación de experiencia de usuario, lo que se pretende es sustituir total o parcialmente el uso de cuestionarios estandarizados, por elementos interactivos que permitan obtener retroalimentación de los usuarios, aplicando conceptos y estructuras de juego [9].

---

<!-- Página 16 -->

4

La mejoría en la obtención de los resultados de evaluación de experiencia de usuario, beneficia no solo a quienes utilizarán los sistemas, sino también a los desarrolladores de estos y a aquellos quienes requieren el sistema para automatizar o mejorar alguno de sus procesos de negocio. Por lo que, el impacto de obtener mejores resultados, en caso de presentarse, sería de altísimo provecho en el contexto de aplicación de un determinado software.

Actualmente, un conjunto importante de evaluaciones de experiencia de usuario se aplica a través de encuestas y cuestionarios estandarizados que, si bien es cierto generan muy buenos resultados, con el tiempo pueden tender a volverse rutinarios para los usuarios [10]. Es por esto que, recientemente se comienzan a proponer técnicas interactivas en la evaluación de experiencia de usuario para sistemas de información [11].

El presente estudio plantea precisamente, contrastar la aplicación de este tipo de técnicas (interactivas, gamificadas) dentro de cuestionarios estandarizados en relación con las herramientas tradicionales utilizadas para aplicarlos, para evaluar si efectivamente, las guiadas por elementos interactivos, juegos específicamente, pueden impactar de alguna forma significativa la retroalimentación de los usuarios en la recolección de resultados de evaluación de experiencia de usuario.

A partir de lo anterior, en la sección a continuación se describirán los objetivos del presente estudio en donde, se establecen las principales acciones a realizar para precisamente contrastar resultados obtenidos en evaluaciones de experiencia de usuario utilizando técnicas interactivas, en específico gamificadas, y las herramientas tradicionales de captura de respuestas de los cuestionarios estandarizados, con el fin de diagnosticar el impacto estas técnicas en los ámbitos de evaluadores, investigadores y propietarios de los sistemas de información.

---

<!-- Página 17 -->

5

Objetivos

Objetivo general

Determinar el impacto de la utilización de métodos interactivos en los resultados de la evaluación de experiencia de usuario, en aplicaciones de software, medida a través de cuestionarios estandarizados.

Objetivos específicos

1. Incorporar elementos (interactivos) dinámicos de apoyo visual para la captura de respuestas de un cuestionario estandarizado. 2. Comparar los resultados de la ejecución de evaluación de experiencia de usuario de la versión interactiva y la versión del cuestionario estandarizado. 3. Determinar el nivel de satisfacción de los usuarios a partir de la utilización de metodologías de evaluación de experiencia de usuario interactivas en relación al uso de cuestionarios estandarizados.

Teniendo en contexto lo anterior, se dispone el presente documento inicialmente con un capítulo que describe el Estado del Arte, en donde se desglosan los aspectos principales de las herramientas a considerar para el presente estudio, relacionando la situación actual de las mismas en contextos científicos probados. Más adelante, en el capítulo de Marco Conceptual, se definirá el contexto del estudio, describiendo en detalle los principales conceptos que se tomaron en cuenta y los enlaces que estos establecieron con los objetivos planteados.

Adicionalmente, se presenta un capítulo de Metodología, en donde se describen los procedimientos, participantes, contexto e instrumentos utilizados para el alcance de los objetivos planteados. Y, finalmente, se presentan dos capítulos de cierre que permiten

---

<!-- Página 18 -->

6

analizar los Resultados de la investigación, junto con las Conclusiones obtenidas a partir del trabajo realizado.

---

<!-- Página 19 -->

7

CAPÍTULO II. ESTADO DEL ARTE

Para la presente investigación se realizó una revisión bibliográfica que, nace de la necesidad de determinar si existe ya alguna referencia de investigación que permita determinar si se ha evidenciado previamente, algún tipo de impacto en la obtención de resultados en la evaluación de experiencia de usuario, en aplicaciones de software, con la utilización de metodologías gamificadas, en comparación con las técnicas estandarizadas.

En el caso específico de la experiencia de usuario, Brito C. [12], realiza una revisión de literatura relacionada a su evaluación en donde, pretende determinar aspectos como: el momento de la evaluación, las técnicas que se utilizaron, los elementos de experiencia que se tomaron en consideración y los objetivos de la evaluación. Si bien detecta dentro de sus resultados el uso de algunas técnicas interactivas, con algunas pocas de estas gamificadas, no realiza una comparación de los resultados obtenidos a través de ellas con ninguna otra técnica.

Por otro lado, al realizar una búsqueda de revisiones de literatura relacionada a la aplicación de técnicas gamificadas a la evaluación de experiencia de usuario, los resultados son prácticamente nulos, ya que la mayoría de documentos relacionados a este tema están dedicados a etapas previas del desarrollo de software, por ejemplo, en la toma de requerimientos de usuario, generación de prototipos e historias de usuario, diseño de interfaces, entre otras; [7, 13] y no en la evaluación de experiencia de usuario como tal. Adicionalmente, dentro de la misma revisión se pudo identificar un grupo de investigaciones que utilizan el concepto de gamificación, sin embargo, este se utiliza en entornos ajenos a tecnologías de información y evaluación de experiencia de usuario [14, 15].

En el siguiente apartado, se describirán los objetivos de investigación que se plantearon para la revisión de literatura aplicada, mismos que están relacionados a los propios del presente estudio.

---

<!-- Página 20 -->

8

Objetivo de la revisión de literatura

El objetivo general de esta revisión bibliográfica fue identificar si es posible obtener mejores resultados en la evaluación de experiencia de usuario, en aplicaciones de software, con la utilización de metodologías gamificadas, en comparación con las técnicas estandarizadas.

De forma más específica, se buscaba evaluar: las técnicas de evaluación aplicadas por los autores, los elementos de experiencia de usuario que son evaluados, los objetivos de la evaluación y la utilización de técnicas gamificadas.

A continuación, se describirá en detalle la metodología aplicada para la revisión de literatura planteada como parte de la presente investigación.

Metodología aplicada para la revisión de literatura

Como parte inicial de la metodología aplicada y en aras de alcanzar el objetivo de esta revisión bibliográfica, se formularon las preguntas que se muestran en la Figura 1.

Q2. ¿Cuáles elementos de Q1. ¿Cuáles técnicas de evaluación experiencia de usuario son de experiencia de usuario fueron considerados cuando se evaluó utilizadas por los autores? experiencia de usuario?

Preguntas de investigación

Q4. ¿Consideraron los autores el Q3. ¿Cuáles objetivos se definieron uso de técnicas gamificadas para la cuando se evaluó experiencia de evaluación de experiencia de usuario? usuario?

Figura 1. Preguntas de investigación para la revisión de literatura.

---

<!-- Página 21 -->

9

A continuación, se describen los criterios de elegibilidad a aplicar para los resultados obtenidos a partir de las preguntas de investigación planteadas.

Criterios de elegibilidad

Se realizó un análisis de artículos publicados en los últimos 12 años (2011 a la fecha) en: conferencias o journals, cuyos permisos de lectura fuesen libres (acceso sin costo) y que estuviesen escritos en idioma inglés. Además, los artículos que se seleccionaron están asociados a la evaluación de experiencia de usuario para herramientas de software.

En el apartado siguiente, se realiza una descripción, a mayor profundidad, del proceso de búsqueda aplicado para la revisión de literatura realizada.

Descripción del proceso de búsqueda

Este proceso se implementó mediante la aplicación de tres fases, a saber:

1. La primera fase consistió en la aplicación de los criterios de elegibilidad definidos a través del análisis de los títulos y resúmenes de los estudios, para determinar que artículos son realmente útiles para esta investigación. 2. Para la segunda fase, se realizó en una revisión más detallada del contenido de los artículos obtenidos en la fase inicial, incluyendo un análisis de la introducción de los mismos, el detalle de la propuesta y sus conclusiones; buscando nuevamente continuar con el análisis de aquellos artículos cuyo contenido sea relevante para la presente revisión bibliográfica. 3. Finalmente, se realizó un análisis completo de los artículos resultantes en las fases anteriores y a partir de estos se generaron las respuestas a las preguntas de investigación y la evaluación de los resultados relevantes a partir de la información recabada.

---

<!-- Página 22 -->

10

A partir de los procesos descritos en la presente metodología para la revisión de literatura, fue posible concretar hallazgos de importancia concreta para la investigación propuesta. Estos se describen a profundidad, como resultados, en la sección siguiente.

Resultados de la revisión de literatura

En esta sección, se presentan los resultados de la revisión sistemática de literatura implementada, exponiendo los hallazgos de mayor relevancia identificados en los documentos analizados.

Inicialmente se identificaron 541 documentos que podrían ser analizados para la presente revisión, sin embargo, al aplicar los criterios de elegibilidad y al realizar un análisis detallado de sus contenidos, se terminaron seleccionando un total de 47 documentos cuya finalidad se ajustaba a los objetivos planteados.

A continuación, se detalla la distribución de las técnicas de evaluación establecidas en los documentos seleccionados.

Distribución de las técnicas de evaluación utilizadas

En cuanto a los tipos de técnicas utilizadas en la literatura analizada, resultó sencillo observar que la gran mayoría (53%) de los autores utiliza técnicas estandarizadas (cuestionarios) para la evaluación de experiencia de usuario.

Adicionalmente, en aquellos artículos donde se utilizó una combinación de técnicas (100% de los artículos de este tipo), siempre los estandarizados fueron utilizados como referencia base. Cabe destacar que la combinación de técnicas consiste en construir un procedimiento de evaluación de experiencia de usuario experimental, a partir de la unión de enunciados de varias herramientas estandarizadas. Si se toman en conjunto las técnicas estandarizadas y combinadas, estas alcanzan un 63% de uso entre los documentos analizados.

---

<!-- Página 23 -->

11

Por otro lado, las técnicas gamificadas, tanto comunes (en físico) como digitales, sólo se utilizaron en el 12% de las aplicaciones de evaluación de experiencia de usuario. Un porcentaje tan bajo como el de aquellos artículos en donde no se utilizó algún tipo de técnica estandarizada o gamificada, para los que se registraron técnicas experimentales en entornos muy específicos (ej. Realidad virtual).

En la Figura 2 se puede observar el detalle de la distribución de las técnicas de evaluación utilizadas por los autores en la evaluación de experiencia de usuario.

Figura 2. Artículos según el tipo de técnica utilizada por los autores.

Continuando con la descripción de resultados de la revisión de literatura, en la sección a continuación, se detallan los principales elementos de experiencia de usuario evaluados en los documentos seleccionados para análisis.

Elementos de experiencia de usuario evaluados

En el caso de los elementos de experiencia de usuario evaluados por los autores, es notorio que: la utilidad (76%), Percepción (72%), análisis de sentimiento y facilidad de uso de uso (63% en ambos casos), consecuencias de uso e intención de uso (53% cada uno); son los que más consideran los usuarios en sus evaluaciones.

---

<!-- Página 24 -->

12

Mientras tanto, el alcance de uso (34%) y los elementos visuales (50%) son los aspectos que menos toman en cuenta para evaluar experiencia de usuario en sistemas de información.

Caso particular se da cuando los autores evalúan elementos adicionales (otros) a los mencionados anteriormente, ya que, aunque a nivel cuantitativo parecen de mucho peso en las evaluaciones, ya que son tomados en consideración en el 82% de las aplicaciones de herramientas de evaluación de UX, es necesario destacar que se detectaron pocas repeticiones de elementos específicos entre los artículos analizados. Estos elementos adicionales se utilizan para evaluar situaciones, contextos y necesidades específicas tanto de los evaluadores como de los investigadores (ej. Utilización de medición optométrica en ambientes de realidad virtual para un laboratorio de evaluación de experiencia de usuario en juegos tridimensionales).

Adicional a lo anterior es necesario indicar, que en todos aquellos casos en donde los autores consideraron técnicas gamificadas, se puede establecer que: el análisis de sentimiento (90%), la facilidad de uso y utilidad (80%), la percepción (70%) y la intención de uso (60%) son los elementos que se evalúan con mayor frecuencia. Mientras que para los demás elementos se consideran en menos de la mitad de los documentos. Si tomamos en consideración esta medición específica con la medición total de todos los documentos revisados, es claro que en las técnicas gamificadas el análisis de sentimiento toma mucha más importancia en las evaluaciones de UX.

En la Figura 3 se puede encontrar un desglose que permite identificar las distintas combinaciones de elementos de experiencia de usuario evaluados y en cuantas ocasiones se repitió el uso de dichos elementos. Cabe destacar que se detectaron 189 combinaciones distintas de elementos de evaluación de experiencia de usuario mediante cuestionarios estandarizados mientras que, para las gamificadas se detectaron 52.

---

<!-- Página 25 -->

13

Figura 3. Combinaciones de elementos de experiencia de usuario utilizados por los usuarios según el tipo de técnica aplicada.

En el apartado a continuación se describen, para los documentos seleccionados, los objetivos de la evaluación de experiencia de usuario que se establecieron en sus contenidos.

Objetivos de la evaluación de experiencia de usuario

Es necesario resaltar que, solamente una de las técnicas seleccionadas por los autores se aplicó en la migración de sistemas de información y que sólo en el 10% de los casos se aplicaron técnicas (estandarizadas solamente) a un sistema nuevo.

En el caso de las aplicaciones de software en producción (es decir aplicación de evaluaciones de UX posteriores al uso inicial de la liberación del producto de software), su uso es frecuente para gamificadas y estandarizadas (tanto individualizadas como combinadas), siendo evaluados en un 51% de los casos.

---

<!-- Página 26 -->

14

De los demás objetivos de evaluación de experiencia de usuario planteados para la presente revisión de literatura, se puede notar, para todas las técnicas, un uso mucho más frecuente de experimentos de evaluación (en el 76% de los casos), esto sucede principalmente al evaluar tecnologías, ambientes o usuarios específicos (ej. Realidad virtual al servicio adultos mayores que visitan museos en línea).

Adicionalmente, un porcentaje considerable (34%) de la literatura analizada consiste en evidenciar la generación de nuevas técnicas de evaluación de experiencia de usuario, de las cuales el 80% son técnicas gamificadas.

Finalmente, se puede observar que solamente en el 27% de los casos, se consideraron objetivos de evaluación adicionales, ninguno con suficiente peso para la generación de una categoría adicional a las establecidas inicialmente y que se implementan en ambientes específicos como realidad virtual o dispositivos móviles.

En la Figura 4 se pueden observar los resultados obtenidos, descritos en los párrafos anteriores de esta sección, al analizar los objetivos de evaluación de experiencia de usuario planteados en los artículos revisados.

Figura 4. Distribución de los objetivos de evaluación de experiencia de usuario.

---

<!-- Página 27 -->

15

De la Figura 4, es necesario destacar que la categoría denominada “Otros” se relaciona a aquellos resultados en donde no se identifica una metodología específica de aplicación. Para estos resultados se analizó el proceso de evaluación de forma general ya que, no se establecían objetivos específicos para evaluación de UX.

El siguiente apartado describe, para los documentos seleccionados, aquellos que se concentran específicamente en la utilización de técnicas gamificadas.

Utilización de técnicas gamificadas

En cuanto a la utilización de técnicas gamificadas, de los documentos seleccionados, se registraron en el 12% de los casos, de las cuales una mitad se aplicó en medios físicos (papel) y la otra mitad en medios digitales.

Al aplicar este tipo de técnicas se puede observar que la metodología principal de aplicación se da a través de tarjetas de descripción de emociones (EmoCards), cuya aplicación se da en un 60% de los casos evaluados. El restante 40% consiste de metodologías dispersas, individuales y para situaciones muy específicas (ej. Simulador de conducción de un vehículo para medición de experiencia de usuario).

Un dato que atrae la atención, obtenido en el análisis de la aplicación de las técnicas gamificadas es que, en el 100% de los casos en que fueron utilizadas, los usuarios, tanto expertos como principiantes, tuvieron una reacción positiva en el uso de las herramientas indicando que: se sintieron más seguros (80%), se divirtieron (90%) y tuvieron mayor motivación para responder adecuadamente la evaluación de experiencia de usuario (70%) al utilizar este tipo de metodologías.

Finalmente, como parte de los resultados obtenidos, a continuación, se describe una serie de hallazgos adicionales que, si bien no se relacionan a los objetivos planteados en la revisión de literatura, resultan interesantes de exponer.

---

<!-- Página 28 -->

16

Evaluación de hallazgos

Cabe destacar que, solamente en el 14% de los artículos analizados fue posible identificar una comparación concreta entre diferentes técnicas de evaluación de experiencia de usuario, las cuales en la mayoría de los casos consistían en contrastar los resultados obtenidos por cada herramienta sin realizar una evaluación adicional del porqué una u otra registraban una valoración más positiva o negativa en sus resultados.

A partir de los hallazgos obtenidos es posible vislumbrar que los cuestionarios estandarizados son las técnicas preferidas por los investigadores en la evaluación de experiencia de usuario. Sin embargo, se puede notar una tendencia a utilizar estos cuestionarios en combinación con otras herramientas o bien a sustituirlos por técnicas más dinámicas, en ambientes específicos y con grupos de usuarios diversos.

Dentro de estas técnicas dinamizadas se pueden identificar claramente las metodologías gamificadas que, si bien no tienen un papel protagónico en la evaluación de experiencia de usuario, se ha podido identificar que en el 100% de sus aplicaciones tienen, una valoración positiva de parte de los evaluadores, quienes indican sentir confianza, motivación y principalmente diversión en el uso de estos procedimientos.

De forma concreta, dada la baja cantidad de evaluaciones sobre metodologías gamificadas que fueron identificadas (12%) y el hecho de que no se comparan directamente en ninguno de los artículos analizados, resulta interesante proceder con una investigación que permita determinar si se puede establecer algún impacto en los resultados en la evaluación de experiencia de usuario al utilizar herramientas gamificadas.

En el siguiente capítulo, de Marco Conceptual, se describen los conceptos más importantes a conocer para el alcance de los presentes objetivos y que servirán de insumo primordial para la correcta definición de la metodología a aplicar para la investigación propuesta.

---

<!-- Página 29 -->

17

CAPÍTULO III. MARCO CONCEPTUAL.

La experiencia de usuario (UX) como tal, es el conjunto de factores y elementos relativos a la interacción del usuario con un entorno concreto, en donde puede obtener una percepción negativa o positiva de dicho entorno, a partir de las formas y métodos por los cuales se enfrenta al mismo [16].

La evaluación de experiencia de usuario, en sistemas de información, es vital para los desarrolladores ya que, todos aquellos productos que brinden una adecuada experiencia a quienes los utilizan, eventualmente permitirán, a través de recomendaciones, satisfacción y sensaciones positivas, generar potencialmente, ventaja competitiva para las soluciones construidas [17].

De forma más general, comúnmente la recolección de datos de evaluación de experiencia de usuario se realiza a partir de diferentes cuestionarios estandarizados (que siguen una norma, modelo o patrón) buscando capturar diferentes elementos de UX. Algunas de estas herramientas buscan medir aspectos como la percepción del producto en diversas dimensiones que abordan cualidades pragmáticas (referido a cómo el contexto de la aplicación de la evaluación influye en su comprensión y significado) y hedónicas (que tan placentera o satisfactoria es la aplicación de la evaluación) [18].

Existen diversos cuestionarios estandarizados para la evaluación de experiencia de usuario, tales como: AttrakDiff, UEQ, meCUE, entre otros [19]. De los cuales, para la presente investigación, se eligió la herramienta denominada meCUE que, permite evaluar la experiencia de usuario de una manera modular y se basa en el modelo Component of User Experience (CUE) de Thuring y Mahlke [20] ya que este, presenta dentro de sus categorías, elementos de evaluación que en principio son adaptables para el uso de metodologías interactivas y en específico gamificadas [21], cuestión que se describirá a profundidad en la sección de metodología del presente documento.

---

<!-- Página 30 -->

18

Este cuestionario comprende cinco módulos, los primeros cuatro contienen enunciados en forma de preguntas que se evalúan utilizando una escala Likert de 7 puntos, los cuales van del 1 (totalmente en desacuerdo) a 7 (totalmente de acuerdo), mientras que el quinto módulo contiene solamente una pregunta que engloba la evaluación del sistema como un todo utilizando valores en una escala entre -5 (malo) y 5 (bueno). Los módulos de meCUE y los elementos que evalúan se describen a continuación:

1. Módulo I: Percepción de las cualidades instrumentales del producto a. Utilidad b. Usabilidad 2. Módulo II: Percepción de las cualidades no instrumentales del producto a. Estética visual b. Estado c. Compromiso 3. Módulo III: Emociones a. Positivas b. Negativas 4. Modulo IV: Consecuencias a. Intención de uso b. Lealtad al producto 5. Módulo V: Evaluación Global

Por otro lado, dado que existen diversas técnicas interactivas que pueden ajustarse a la evaluación de experiencia de usuario, para la presente evaluación se aplicó la llamada técnica de gamificación que, es conocida como la aplicación de estrategias de juego en ambientes no lúdicos, buscando incrementar el compromiso, la atención a los detalles y en mayor escala, el comportamiento emocional de los usuarios [22].

Más específicamente, según la definición dada por Deterding, S., Dixon, D., Khaled, R. y Nacke, L. [23], gamificación se refiere al uso de elementos diseñados a partir de características de juegos en contextos no enfocados a ámbitos de diversión o esparcimiento.

---

<!-- Página 31 -->

19

Lo anterior buscando, dadas las características interactivas de este tipo de herramientas que, en su unión con actividades profesionales o académicas (o cualquier otra no lúdica), logren un mayor enganche entre las herramientas y sus usuarios finales [24].

Además, acerca del diseño de herramientas gamificadas, es importante recalcar que, esta comúnmente se ha apoyado en el uso de tecnologías de información (aplicaciones web, móviles, redes sociales, plataformas educativas en línea, entre otras) principalmente porque desde sus inicios en ambientes no lúdicos, se presentó con una relación cercana a los video juegos, utilizando algunos elementos de estos, pero sin dejar de lado el objetivo académico o profesional deseado [25].

Dado lo anterior y en referencia a que, en la actualidad existe un uso extendido, para la evaluación de experiencia de usuario, a partir de cuestionarios estandarizados [26], en la presente investigación se adaptó la misma herramienta meCUE, aplicándole a esta, mecánicas de juego y controles interactivos que aplican los contenidos del cuestionario estandarizado, con su misma definición de preguntas y escala de respuestas. Esto, teniendo como objetivo evaluar las mismas categorías y conceptos, solamente que, con la aplicación de distintos mecanismos de ejecución.

A continuación, en la descripción de la Metodología de la presente investigación, se utilizarán los conceptos centrales de este capítulo, para describir la forma en que se procedió con las actividades de investigación de este trabajo.

---

<!-- Página 32 -->

20

CAPÍTULO IV. METODOLOGÍA

El trabajo de investigación realizado tuvo su origen en parte de los contenidos del curso "Usabilidad y Accesibilidad de Aplicaciones y Sitio Web" de la Maestría Profesional en Ciencias de la Computación e Informática de la Universidad de Costa Rica, del cual se obtuvo el conocimiento base para el desarrollo de la propuesta, misma que fue objeto de análisis por parte de un grupo de profesionales expertos (Grupo de investigación USING de la Universidad de Costa Rica) con amplia experiencia en el campo de estudio aplicado, como lo es la evaluación de experiencia de usuario.

La metodología de la investigación planteada, se desarrolló tomando como base la propuesta de Saunders, M. y Tosey, P. [27], realizando un diseño con tres capas exteriores, a saber:

1. Primera capa, filosofía de investigación: el diseño de los instrumentos (que se abordarán en detalle más adelante en esta sección del documento) están ligados al marco de trabajo de ciencias del diseño [28], en donde, sus características se asocian al contexto de aplicación.

2. Segunda capa, elección metodológica: se planteó para la presente investigación la aplicación de métodos cuantitativos como lo son los cuestionarios estandarizados y gamificados, en asociación con un método mixto (cuantitativo y cualitativo) para la evaluación de los niveles de satisfacción de quienes aplicaron el proceso de medición experiencia de usuario (cuestionario estandarizado y cuestionario gamificado), en el cual se definieron espacios de retroalimentación más abiertos.

3. Tercera capa, línea estratégica: se planteó un diseño de metodología centrada en el usuario, ya que los participantes asociados a la presente investigación aplicarían las herramientas base (cuestionario estandarizado y cuestionario gamificado) para,

---

<!-- Página 33 -->

21

posteriormente, evaluarlas a través de una encuesta específica del ámbito de medición de niveles de satisfacción, propuesta para la presente investigación. En el siguiente apartado, se describirá el contexto de la presente metodología, en donde se hará una especial referencia a la estrategia metodológica aplicada.

Contexto

De forma general, cada uno de los objetivos planteados en la presente investigación, se asociaron a un marco metodológico específico, en aras de obtener distintos artefactos que permitieran establecer, analizar y constatar resultados tangibles de estudio.

Esta relación de objetivos, marco metodológico y artefactos, se describe a continuación en la Figura 5.

Objetivo Marco metodológico Artefactos

Incorporación deConstrucción del cuestionarioCuestionario meCUE elementos gamificado basado engamificado interactivosmeCUE

Comparación deAplicación de ambosResultados de evaluación de resultados (meCUEtipos de evaluaciones experiencia de gamificado vsde experiencia de usuario con ambas usuario estandarizado)herramientas

Evaluación de laAplicación de encuesta adicionalExperiencia de los experiencia de (UEQ) para evaluar lausuarios al utilizar usuario según la experiencia deambas herramientas herramienta meCUEusuario al usar lasde evaluación meCUE utilizadaherramientas meCUE

Figura 5. Estrategia metodológica en relación con los objetivos de la investigación.

---

<!-- Página 34 -->

22

A partir de este contexto, se describirá en la sección siguiente, el procedimiento específico aplicado para alcanzar los objetivos propuestos.

Procedimiento

A continuación, se detalla cómo la presente investigación fue desarrollada, esto a partir de la implementación de un plan piloto y un conjunto de etapas específicas de implementación que, como un todo definieron la base para el alcance de los objetivos propuestos.

Plan piloto

Para el presente estudio, se llevó a cabo un plan piloto de evaluación de experiencia de usuario en el que se contrastaron las dos metodologías propuestas: una utilizando el cuestionario meCUE de manera estándar y la otra implementando una versión gamificada. En este proceso, participaron 20 evaluadores de distintos perfiles y niveles de experiencia en la utilización de sistemas de información.

El objetivo de este plan piloto, era principalmente, evaluar la herramienta gamificada a aplicar de forma definitiva en la investigación, para determinar posibles mejoras, formas de aplicación y principalmente analizar la percepción de los participantes al aplicar esta metodología.

En cuestiones de desarrollo, se debe indicar que el cuestionario estandarizado se implementó en una versión en línea, fiel a la estructura, enunciados y escalas de la herramienta meCUE tradicional. Mientras que, en el caso de la herramienta gamificada, se implementó el mismo cuestionario, también apegado a su estructura original, pero añadiendo algunos elementos visuales de apoyo a la recepción de respuestas, utilizando imágenes de video juegos clásicos (como Donkey Kong, Megaman, Sonic, entre otros), en donde al hacer clic sobre algún elemento básicos de estos (barril, tubería, aro, entre otros) se presentaba la imagen del personaje relacionado al video juego. El proceso que debía

---

<!-- Página 35 -->

23

completar el usuario era arrastrar el personaje a algún elemento relacionado, para así dar respuesta a los enunciados del cuestionario.

En este proceso, todos los evaluadores recibieron ambos cuestionarios y evaluaron dos sitios web diferentes para cada uno. En el caso de la herramienta estandarizada se evaluó la página de Federación Internacional de Fútbol Asociado (FIFA), en donde se les pidió a los usuarios simular la compra de entradas para un partido de fútbol oficial. Mientras tanto para la aplicación de la herramienta gamificada, se solicitó a los usuarios evaluar la página del Manchester United Football Club, en donde se les pidió que simularan la compra de una camiseta en la tienda en línea oficial del equipo.

En la Figura 6 se puede observar la versión preliminar de la herramienta estandarizada y en la Figura 7, la versión preliminar de la herramienta gamificada. Nótese que inicialmente ambas herramientas se aplicaron a los participantes en idioma inglés.

Figura 6. Versión estandarizada de meCUE utilizada en el plan piloto de la presente investigación.

---

<!-- Página 36 -->

24

Figura 7. Versión gamificada meCUE utilizada en el plan piloto de la presente investigación.

Una vez finalizado el plan piloto, se procedió a realizar las modificaciones pertinentes en las herramientas, para iniciar con las etapas específicas de la investigación propuesta. La primera etapa de este proceso, se describe a continuación.

Primera etapa

Inicialmente se construyó el cuestionario gamificado que, como se estableció previamente en la sección de Marco Conceptual, consistió en una adaptación de la herramienta meCUE estandarizada, añadiéndole elementos de mecánica de juegos, conservando la estructura modular base del cuestionario original.

Además, en esta etapa se implementó una solución en línea para el cuestionario estandarizado, para que este pudiese ser accedido y completado a través de medios digitales, asegurando que este mantenga el mismo contexto de aplicación que se dispuso para el cuestionario gamificado.

Posteriormente, se procedió con la aplicación de la segunda etapa, misma que se describe en el apartado siguiente.

---

<!-- Página 37 -->

25

Segunda etapa

Para la aplicación de ambas metodologías de evaluación, se facilitó a los participantes, un enlace electrónico o dirección web (URL), en donde ubicarían la herramienta a aplicar.

Dentro de dicho enlace, los participantes encontraron instrucciones adecuadas y detalladas sobre cómo utilizar cada herramienta y dentro de la misma, se les indicó el software o sistema de información que debían evaluar, con un enlace que pueda dirigirlos a su dirección web. En aras de realizar esta evaluación se eligió la herramienta Chat GPT [29].

Para la aplicación de ambas herramientas de evaluación (gamificada y estandarizada) se planificó contar con una población de al menos 20 usuarios, tomando como base lo indicado por Díaz-Oreiro, I. [30] en sus hallazgos sobre la media de participantes en estudios de evaluación de UX), seleccionados de forma aleatoria. A cada uno de ellos, vía correo electrónico se le facilitó la dirección web en donde podían encontrar la herramienta (también seleccionada de forma aleatoria) que deberían aplicar para evaluar la experiencia de usuario de Chat GPT. Estos participantes fueron estudiantes de la carrera de Bachillerato en Ingeniería de Sistemas de la Universidad Fidélitas.

Por último, una vez finalizada la aplicación de las evaluaciones de los usuarios, se realizó un análisis de los resultados de cada una de las herramientas más una comparación de las mismas para cada uno de los módulos que se establecen en el cuestionario meCUE, en aras de identificar si era posible obtener algún resultado significativo en contraste con la otra.

Al finalizar esta segunda etapa, se procedió con la aplicación de la tercera y última fase de la presente metodología, misma que se describe en el apartado siguiente.

Tercera etapa

---

<!-- Página 38 -->

26

En esta etapa, independientemente de la herramienta aplicada por el participante, a este se le aplicó una segunda encuesta que, estuvo centrada ya no en la evaluación de la herramienta de software, si no, en la evaluación de la herramienta que utilizó para realizar dicha evaluación. Esto con el fin de medir su nivel de satisfacción al momento de aplicar la evaluación de experiencia de usuario y mediante la utilización de una herramienta adicional de evaluación de experiencia de usuario (UEQ, que se describe más adelante en la sección de Instrumentos).

A continuación, se realizará una descripción detallada de los instrumentos que se utilizaron como parte de la metodología de la presente investigación.

Instrumentos

Para la presente investigación, se decidió seleccionar la herramienta meCUE en su versión original y la misma en una adaptación gamificada (de creación propia), cuyas características fueron descritas en la sección de Marco Conceptual del presente documento. Esto se definió dado que, aunque representan metodologías distintas (la primera es un cuestionario estandarizado y la segunda una herramienta interactiva) ambas evaluarían los mismos elementos de experiencia de usuario permitiendo principalmente, contrastar de mejor manera los resultados obtenidos.

Adicionalmente, la principal razón para esta decisión es que la herramienta meCUE toma como uno de sus principales aspectos de medición el análisis de emoción del usuario, cuestión que, tal como se describió en los hallazgos del Estado del Arte en el presente documento, representa para el 60% de los investigadores, el principal objetivo de estudio en el uso de técnicas gamificadas. Si bien otras herramientas, como UEQ [31], evalúan de cierto modo el tema de emoción, no delimitan una sección específica al respecto como sí lo define meCUE.

---

<!-- Página 39 -->

27

Además, es necesario recalcar que el cuestionario meCUE, seleccionado como base para la presente investigación, ha sido probado y validado ya en diferentes contextos [32], por lo que representa una metodología válida a aplicar para la recolección de resultados de evaluación de experiencia de usuario.

A continuación, se describirá en detalle la herramienta seleccionada, en el contexto del cuestionario estandarizado utilizado.

Cuestionario estandarizado meCUE

Los contenidos, escalas, orden y demás elementos originales de la herramienta meCUE se mantuvieron sin ninguna variación durante la ejecución de la presente investigación. Sin embargo, para facilitar su aplicación y el acceso a la misma de los participantes, se realizó una modificación concreta, a saber:

- La herramienta, de forma general, se aplica en físico (papel). No obstante, para el presente trabajo se construyó una versión digital, para que los participantes pudiesen completarla en línea. Esto, para mantener un contexto estable entre ambas metodologías, ya que, la gamificada al aplicar elementos interactivos, requiere de un ambiente que permita facilitar la adición de mecanismos de juego, como lo son los medios digitales (ver Anexo 1).

En la Figura 8 se presenta la estructura base de la herramienta meCUE estandarizada que se aplicó a los participantes, en donde, se mantienen los mismos enunciados y elementos de su versión general (en papel).

---

<!-- Página 40 -->

28

Figura 8. Cuestionario estandarizado meCUE en línea que imita la evaluación original

En la siguiente sección se describirá, para esta misma herramienta, la versión gamificada que se implementó.

Cuestionario gamificado meCUE

Para la aplicación de la metodología gamificada, se mantuvo los contenidos, escalas, orden y demás elementos originales del cuestionario original meCUE, añadiendo mecanismos de juego al cuestionario para que este fuese interactivo (ver Anexo 2).

En general, se construyó una versión digital del cuestionario, que fue dividida en 5 secciones o “niveles” (similares a los que se tienen que superar en los video juegos comunes), uno por cada módulo de la herramienta original. Añadiendo en cada una de estas, mecanismos de juego, que permiten al participante interactuar de forma dinámica con el cuestionario.

---

<!-- Página 41 -->

29

En esta versión gamificada, se utilizaron personajes del videojuego "Mario Kart" [33], los cuales tenían diferentes objetivos en cada uno de los niveles del cuestionario, y su progreso dependía de que el participante contestara a las preguntas del cuestionario, por lo que en síntesis, para terminar el juego, los evaluadores debían responder a todos los enunciados proporcionados.

El personaje principal asignado a los usuarios fue Mario, quien avanza en la pantalla cada vez que el usuario hace clic en una caja de potenciadores (llamados “power-ups” en la versión original del juego). Cada uno de estos potenciadores (revelados al azar) son los mismos que se utilizan en el juego (tortugas, bombas, hongos, entre otros). La gamificación se aplica con el objetivo ayudar a Mario a alcanzar y vencer a su rival en cada nivel-carrera (módulo del cuestionario) respondiendo a los enunciados de evaluación de meCUE. Una vez que el usuario completa un módulo (nivel), Mario cruza la línea de meta y se revela otra carrera con un nuevo rival.

En la Figura 9, se muestra la implementación del cuestionario gamificado meCUE que fue utilizado por los participantes.

---

<!-- Página 42 -->

30

Figura 9. Cuestionario meCUE gamificado en línea, que muestra el aspecto básico de su implementación incluyendo los potenciadores, a Mario y su rival en el Módulo I.

Por otro lado, la Figura 10 muestra cómo se revelan los potenciadores una vez que el usuario selecciona una caja y en la Figura 11 se muestra cómo Mario avanza en la carrera contra diferentes rivales y en diferentes escenarios de juego según las respuestas de los usuarios a los enunciados del cuestionario.

---

<!-- Página 43 -->

31

Figura 10. Potenciadores asignados de forma aleatoria al hacer clic en las cajas relacionadas a la escala likert de cada enunciado de meCUE.

Figura 11. Perspectiva del movimiento de Mario en diferentes escenarios contra diferentes rivales (muestra del Módulo I, en donde el jugador compite contra Luigi).

De forma adicional, para el Módulo V de este cuestionario gamificado, sobre la evaluación global del producto, se incluyó una escala con elementos del juego seleccionado, para que el usuario pudiese expresar su valoración general de Chat GPT. Esto se muestra en la Figura 12.

Figura 12. Estructura de la evaluación global del cuestionario meCUE gamificado, utilizando elementos del juego "Mario Kart".

---

<!-- Página 44 -->

32

En el apartado a continuación se describirá, la herramienta UEQ, que fue utilizada en esta investigación para realizar la evaluación sobre las herramientas tanto gamificada como estandarizada de meCUE.

UEQ (User Experience Questionnaire)

Este cuestionario permitió a los participantes valorar la herramienta de evaluación de la experiencia de usuario previamente aplicada (ya sea la versión estándar o la gamificada de meCUE). De igual forma que ambas versiones de meCUE, esta herramienta UEQ se implementó a través de una solución en línea (sitio web), manteniendo su estructura original, con una variante al final de la evaluación donde se solicitaba a los participantes que describieran la herramienta meCUE recibida usando tres palabras (ver Anexo 3).

El UEQ es un cuestionario estandarizado, que se aplica a través de un control de Likert de 7 puntos, para la evaluación de la experiencia de usuario que puede aplicarse a diferentes productos. Esta herramienta contiene seis escalas: Atractivo (seis ítems), Transparencia, Controlabilidad, Eficiencia, Novedad y Estimulación (cuatro ítems cada una). Busca llevar a cabo evaluaciones rápidas y considera aspectos centrales de la calidad y percepción de los productos [31]. Sus escalas y enfoque de evaluación se detallan en la Tabla 1.

Tabla 1. Escalas de UEQ y sus enfoques de evaluación.

Escala Enfoque Impresión obtenida al utilizar el producto. Atracción Transparencia Facilidad para familiarizarse con el producto. Cantidad de esfuerzo que se debe realizar al utilizar el producto. Eficiencia Controlabilidad Control que se tiene al interactuar con el producto. Motivación en el uso del producto. Estimulación Novedad Innovación y creatividad en el producto.

Adicionalmente en la Figura 13, se puede observar una parte el cuestionario UEQ aplicado en línea a los participantes. Mientras que en la Figura 14, se muestra el apartado adicional

---

<!-- Página 45 -->

33

que se le agregó al cuestionario, en donde se insta a que los participantes describan la herramienta en tres palabras.

Figura 13. Cuestionario UEQ utilizado por los participantes para evaluar la herramienta meCUE (gamificada o estandarizada según correspondiese).

Figura 14. Espacio para comentarios adicionales dentro del cuestionario UEQ aplicado a los participantes.

A continuación, se presenta el capítulo de Resultados, en donde se detallan los principales hallazgos de la esta investigación, a partir de la aplicación de lo descrito en la presente sección de Metodología.

---

<!-- Página 46 -->

34

CAPÍTULO V. RESULTADOS.

Hallazgos del plan piloto

En total, durante la aplicación del plan piloto propuesto para la presente investigación, participaron 20 personas, todas mayores de 18 años, siendo 12 personas hombres y 8 mujeres. Cabe destacar que todos los participantes completaron ambas versiones del cuestionario, tanto el gamificado como el estandarizado.

Durante este proceso, no se realizaron evaluaciones adicionales para evaluar las herramientas dadas a los usuarios, si no que, se hicieron análisis directos sobre los resultados de ambas aplicaciones. Sin embargo, sí se les solicitó a los usuarios una breve retroalimentación (un texto corto de opinión) sobre su experiencia en el uso de cada herramienta, prestando especial atención a los comentarios sobre el cuestionario gamificada, ya que, era esta la que se quería evaluar a fondo para generar un producto final adecuado para las necesidades, contexto y objetivos de la investigación.

Los resultados generales de esta aplicación indicaron que, para la herramienta estándar los usuarios proporcionaron comentarios centrados en la usabilidad y la funcionalidad de la interfaz. Por otro lado, para la metodología gamificada ofrecieron comentarios relacionados con la experiencia de juego, indicando en su mayoría (60%) que, aunque se tienen imágenes de video juegos clásicos, la interfaz como tal, no ofrecía una secuencia que pudiese ser relacionada a un juego como tal (no se superan niveles, los personajes no tienen una recompensa, no existe ningún tipo de competencia u obstáculos que se deban superar).

A partir de estos resultados, se tomaron decisiones puntuales para modificar la herramienta gamificada, agregando elementos de juego puntuales a su estructura, a saber: división de módulos de meCUE en niveles, inclusión de competencias entre el personaje principal y personajes secundarios, adición de recompensas para los personajes y en general

---

<!-- Página 47 -->

35

animaciones básicas que simularan el comportamiento de un video juego dentro del cuestionario. En la sección a continuación, se describen los resultados de la investigación principal, una vez analizados los hallazgos dados en el plan piloto realizado, iniciando por las características demográficas de los participantes de la investigación.

Características demográficas de la investigación

En total, 60 personas, todas mayores de 18 años, respondieron a los cuestionarios meCUE propuestos. De estos, 26 utilizaron la herramienta gamificada y 34 utilizaron la estandarizada. Es necesario destacar que el 100% de estos participantes respondieron al cuestionario UEQ final que evaluó ambas herramientas meCUE.

Entre los que completaron el cuestionario estandarizado, el 79% eran hombres, y un alto número de los participantes totales tenían entre 18 y 29 años de edad (85%). De estos, la mayoría ya conocía (97%) y había utilizado (85%) Chat GPT.

Por otro lado, quienes completaron el cuestionario gamificado también eran en su mayoría jóvenes de entre 18 y 29 años (96%), con el mayor número (76%) de evaluadores siendo hombres. En esta versión del cuestionario meCUE, la mayoría de los participantes ya conocía (92%) y había utilizado (88%) Chat GPT. La Tabla 2 muestra el resumen demográfico completo.

Tabla 2. Resumen de características demográficas

Distribución Herramienta Variable n % 27 79 Hombres 18-29 años 23 85 27 100 Conocían Chat GPT Estandarizada (34) Habían utilizado Chat GPT 23 85 7 21 Mujeres 18-29 años 6 85

---

<!-- Página 48 -->

36

Distribución Herramienta Variable n % 6 85 Conocían Chat GPT 6 85 Habían utilizado Chat GPT 20 76 Hombres 19 95 18-29 años 19 95 Conocían Chat GPT Gamificada (26) 19 95 Habían utilizado Chat GPT 6 24 Mujeres 6 100 18-29 años Gamificada (26) 5 83 Conocían Chat GPT 4 66 Habían utilizado Chat GPT

Continuando con la exposición de resultados, en el apartado siguiente se detalla la información obtenida de la evaluación de Chat GPT, utilizando el cuestionario estandarizado meCUE.

Evaluación meCUE estandarizada de Chat GPT

En términos generales, después del análisis de datos del cuestionario meCUE estandarizado, la evaluación de Chat GPT por parte de los 34 participantes que lo utilizaron fue positiva para todos los módulos evaluados, incluida la evaluación global.

En cada uno de los cuatro módulos iniciales, los participantes indicaron en mayor medida que el producto parece útil y con buena usabilidad. Además, tiene una estética visual adecuada y genera más emociones positivas que negativas. Además, en el módulo V de evaluación global, los participantes dieron una calificación positiva al producto, evaluándolo con un 3.32 en una escala máxima de 5.

Seguidamente, se detallan los resultados de la evaluación de experiencia de usuario para Chat GPT, utilizando la evaluación gamificada meCUE.

---

<!-- Página 49 -->

37

Evaluación meCUE gamificada de Chat GPT

Los 26 participantes que utilizaron el cuestionario gamificado también dieron una evaluación positiva para todos los módulos evaluados en relación con Chat GPT.

En los primeros cuatro módulos, se indicó que el producto es útil y tiene buena usabilidad. Además, su estética visual y estado fueron calificados positivamente. En cuanto a las emociones, los participantes indicaron tener más emociones positivas que negativas. En consecuencia, en cuanto a la evaluación global, evaluada en el módulo V, los participantes calificaron positivamente el producto, con un promedio de 3.31 en una escala máxima de 5.

A partir de los resultados expuestos en las dos secciones anteriores, se realizó una comparación sobre los resultados de ambas herramientas, lo cual, se describe en el siguiente apartado.

Resultados sobre la comparación de meCUE estandarizado y meCUE gamificado

En general, al comparar los cuestionarios meCUE con sus resultados básicos, se puede notar que los usuarios evalúan la herramienta gamificada de manera más positiva en todos los aspectos evaluados, e incluso en su evaluación global. La Figura 15 muestra esta comparación general entre los cuestionarios meCUE estandarizados y gamificados para sus cuatro primeros módulos.

---

<!-- Página 50 -->

38

Figura 15. Comparación general entre los cuestionarios meCUE estandarizados y gamificados.

Sin embargo, esta comparación general es insuficiente para determinar si existen diferencias significativas en la evaluación de los participantes de ambos cuestionarios. Por lo tanto, con las evaluaciones realizadas utilizando las dos versiones del cuestionario meCUE (gamificado y estandarizado), se realizó una comparación general de sus resultados mediante una Prueba de Rango Wilcoxon [34] para muestras independientes, ya que las respuestas de las subescalas no presentaron una distribución normal; por lo tanto, se utiliza una prueba no paramétrica.

Dado que la estimación de diferencias para las diez escalas meCUE se considera como múltiples pruebas simultáneas de hipótesis, se aplicó la corrección Holm-Bonferroni al nivel alfa de 0.05, para compararlo con los valores de p obtenidos en la prueba Wilcoxon y, así, reducir los errores de Tipo I (falsos positivos). A partir de esta comparación, se establece que las hipótesis nulas no pueden ser rechazadas en las nueve subescalas, por lo que se concluye que no existen diferencias significativas en los resultados de ambas implementaciones.

---

<!-- Página 51 -->

39

Basándose en lo anterior, resulta que no hay diferencia significativa en ninguna de las nueve subescalas evaluadas en los cuestionarios meCUE, ni en su evaluación general. La Tabla 3 describe los resultados de la Prueba de Rango Wilcoxon, al comparar los datos generales de ambas herramientas, según sus subescalas. Es necesario destacar que todos los valores de p son mayores que el valor "alfa" o valor de significancia establecido en 0.05.

Tabla 3. Prueba de valores Wilcoxon para muestras independientes en la aplicación del meCUE estandarizado y gamificado.

MediaMedia Valor- p de la cuestionariocuestionarioDiferencia Subescalaprueba gamificadoestandarizadosignificativa Wilcoxon (N = 26)(N=34) 5.42 0.8747 No Utilidad 5.63 5.75 0.4815 No Usabilidad 6.04 4.71 0.7531 No Estética visual 4.65 3.63 0.1871 No Estado 4.10 2.58 0.3557 No Compromiso 3.04 3.66 0.3018 No Emociones positivas 4.04 2.52 0.6268 No Emociones negativas 2.76 3.33 0.9224 No Intención de uso 3.45 3.75 0.1535 No Lealtad al producto 4.18 3.32 0.4403 No Evaluación global 3.31

Finalmente, en la siguiente sección se detallan los resultados de la evaluación de ambas metodologías (gamificada y estandarizada) a partir de la retroalimentación dada por los participantes al completar el cuestionario UEQ.

Resultados de Evaluación UEQ de meCUE Estandarizado y meCUE Gamificado

Los participantes también realizaron una evaluación de experiencia de usuario (UEQ) en las dos implementaciones de meCUE utilizando el cuestionario UEQ. En este caso, los resultados muestran que el cuestionario gamificado presentó una mejor evaluación en todas las escalas UEQ.

---

<!-- Página 52 -->

40

Sin embargo, la herramienta de análisis de datos UEQ identificó inconsistencias [33] en ambas evaluaciones meCUE. A partir de esto, se determinó que sería necesario analizar los datos evitando estas variaciones. Como resultado, las respuestas inconsistentes se eliminaron de las evaluaciones meCUE, dejando 27 evaluaciones estandarizadas y 24 evaluaciones gamificadas, lo que resultó en una mejor percepción de los usuarios que utilizaron la herramienta gamificada en todas las escalas, pero solo hubo una diferencia significativa en la escala de Novedad, como se muestra en la Figura 16.

Figura 16. Resultados de las evaluaciones gamificadas y estandarizadas de meCUE basadas en su comparación con el cuestionario UEQ.

Además, los valores obtenidos en las evaluaciones UEQ de ambas herramientas meCUE se compararon utilizando una prueba Wilcoxon para muestras independientes. Se estableció un Alfa de 0.05 como el nivel de significación de la hipótesis de que no hay diferencia significativa en las evaluaciones de las seis escalas UEQ. También se aplicó la corrección Holm-Bonferroni para pruebas simultáneas, y se identificó que solo en la escala de Novedad se puede rechazar la hipótesis nula. Por lo tanto, se puede concluir que, en la escala de Novedad, los participantes consideran mejor la versión gamificada y que en las otras cinco escalas no hay diferencias significativas.

Finalmente, con respecto a la solicitud de que los participantes describieran la herramienta meCUE recibida usando tres palabras, los datos muestran que para la versión gamificada se

---

<!-- Página 53 -->

41

considera Creativa (41%), Interesante (27%), Original - Atractiva (18%) y Divertida - Fácil (13%). Por otro lado, la versión estandarizada se considera Fácil (33%), Rápida (22%), Ordenada - Clara (18%) y Simple - Interesante (14%). Estos resultados se ilustran en la Figura 17.

Figura 17. Percepción de los participantes, descrita en una sola palabra, para ambas herramientas meCUE.

Cabe destacar que los resultados descritos en este Capítulo fueron expuestos, mediante la publicación de un artículo científico (Ver Anexo 4), en las VI Jornadas Costarricenses en Investigación en Computación e Informática (JOCICI) del año 2023, cuya sesión magna se llevó a cabo el 20 de setiembre de ese mismo año en la Universidad Técnica Nacional, campus Alajuela, Costa Rica; cuyas memorias se publicarán en el sitio web del evento [35] y se enlazarán a la plataforma IEEE.

Seguidamente, se desarrolla el Capítulo de Conclusiones en donde se discuten y sintetizan precisamente los resultados descritos en la presente sección, además de tomar un espacio para el análisis de posibles extensiones de la investigación realizada.

---

<!-- Página 54 -->

42

CAPÍTULO VI. CONCLUSIONES

Durante la presente investigación se planteó determinar si, cabe la posibilidad de que exista algún tipo de impacto, para los usuarios, en la utilización de métodos interactivos, en específico gamificados, en contraste con la aplicación de cuestionarios tradicionales estandarizados.

Para cumplir con dicho planteamiento, se generaron, a partir del cuestionario meCUE, dos herramientas de evaluación de experiencia de usuario, una gamificada y otra tradicional estandarizado, ambos accesibles en línea y respetando la estructura, enunciados y formato general de la aplicación original.

Uno de los hallazgos más importantes que resultan de esta investigación, es el hecho de que, en los resultados de la aplicación de ambas herramientas meCUE, se puede determinar que, para ninguna de las dos versiones, existen diferencias significativas en las evaluaciones realizadas por los usuarios.

Este descubrimiento permite demostrar que, independientemente de la técnica de evaluación utilizada, los participantes no generarán desviaciones en los datos recopilados debido a distracciones, motivación, estimulación visual u cualquier otro aspecto que las herramientas interactivas puedan ofrecer en comparación con la estructura general y formato de caputra de un cuestionario estandarizado.

Más específicamente, para ambas metodologías, el uso del cuestionario estandarizado o gamificado, es posible evaluar un producto dado de la misma manera sin que los resultados de la evaluación de la experiencia del usuario se vean afectados en ninguna de las escalas de meCUE.

Además, de acuerdo con los resultados recopilados en la aplicación de ambos cuestionarios meCUE, se puede observar que la experiencia de usuario al utilizar la herramienta

---

<!-- Página 55 -->

43

gamificada es mejor evaluada por los participantes en todas las escalas, en comparación con la herramienta estandarizada. Sin embargo, una vez analizados los datos finales, solo se observa un impacto significativo en la escala de "Novedad".

De forma más concreta, al utilizar UEQ para evaluar la experiencia de usuario de las dos versiones del cuestionario (gamificado o tradicional), se logró determinar, dentro de sus resultados, únicamente un impacto significativo en la subescala de "Novedad" al utilizar la herramienta de evaluación de UX gamificada en comparación con la estandarizada, lo cual indica que los usuarios consideran a esta evaluación innovadora y creativa, siendo capaz de atraer su interés durante la generación de las respuestas a cada uno de los enunciados propuestos por meCUE.

Esto último, plantea una un espacio atractivo adicional de investigación, que sería el determinar si efectivamente los usuarios, con el paso del tiempo logran mantener el interés en la evaluación mientras estén utilizando este tipo de herramientas interactivas, o bien si con el tiempo, esta percepción de “Novedad” puede disminuir con el uso constante de estas metodologías.

Relacionado a lo anterior, es necesario tomar en cuenta que, cuando se les pidió a los participantes que describieran la herramienta meCUE utilizada en tres palabras, se observó que, para la gamificada, los términos más frecuentemente utilizados también estaban relacionados con los evaluados en la escala de "Novedad" del cuestionario (creativo, original, novedoso, etc). Esto, permite visualizar varias oportunidades de mejora, utilizando no solo la gamificación, sino también el uso de ayudas visuales que puedan motivar y atraer la atención de los participantes en la aplicación de este tipo de cuestionarios.

Por otro lado, para la versión estandarizada, se observó que los participantes evaluaban con mayor frecuencia términos relacionados con el esfuerzo y el tiempo invertido. Lo cual podría ser un aspecto llamativo de evaluar y analizar en futuros trabajos como comparación

---

<!-- Página 56 -->

44

entre ambas herramientas, tratando de determinar si una u otra herramienta presume un mayor esfuerzo o inversión de tiempo para los evaluadores durante su aplicación. Adicional a los hallazgos determinados anteriormente, en donde incluso es posible determinar posibles trabajos futuros sobre el hallazgo de una diferencia significativa en la escala de “Novedad”, para la herramienta gamificada, podría también resultar atractivo llevar a cabo una evaluación de este tipo en herramientas de software más controladas y de contextos específicos (software industrial), en donde el ambiente de aplicación podría variar los hallazgos sobre la satisfacción de los participantes respecto a la interacción ofrecida por la metodología gamificada.

Es necesario destacar que, tanto para los investigadores de UX como para los evaluadores, es importante contar con herramientas que les permitan mejorar la motivación y la concentración en la evaluación de productos, ya que esto puede generar eventualmente una ventaja competitiva para las soluciones construidas, generando mejoras a través de los resultados de las evaluaciones en aspectos como la intención de uso, la satisfacción percibida y las emociones.

A partir de los resultados obtenidos y con la premisa descrita anteriormente, la presente investigación implementa y establece una herramienta novedosa y original que se puede utilizar, tanto por los investigadores como por los evaluadores, como un enfoque totalmente válido en la aplicación de evaluaciones interactivas de UX, a partir del uso de técnicas de gamificación para lograr un mayor interés por parte de los participantes en la evaluación de productos de software.

Lo anterior resulta especialmente relevante, dado que, la puesta a disposición de una nueva herramienta para la evaluación de UX permite, aparte de explorar enfoques novedosos de estudio, contar con una metodología ya probada para la recopilación de datos, sin ningún impacto significativo, en las percepciones de los usuarios y principalmente sin modificar la estructura original de herramientas validadas y de uso continuo en la evaluación de experiencia de usuario.

---

<!-- Página 57 -->

45

Por otro lado, aunque los resultados obtenidos con el cuestionario estandarizado no son significativamente mejor evaluados que los obtenidos con el gamificado, esto no significa que este tipo de evaluación tenga una valoración negativa, por lo que no se pretende indicar que su uso deba ser interrumpido o alterado, ya que, aunque para los usuarios no representen una metodología novedosa o estimulante, finalmente permiten obtener resultados precisos y concretos en su objetivo principal de evaluar productos.

En resumen, la investigación demuestra que ambas metodologías son efectivas en la evaluación de la experiencia de usuario, pero la gamificación genera un impacto específico en las evaluaciones, mediante el cual puede aportar un elemento de novedad y atractivo adicional. Esto plantea oportunidades para futuras investigaciones y la posibilidad de utilizar la gamificación como enfoque para mejorar la motivación y la concentración de los evaluadores en la evaluación de productos de software. La nueva herramienta gamificada se considera una opción válida y efectiva en la evaluación de UX, sin un impacto significativo en las percepciones de los usuarios.

---

<!-- Página 58 -->

46

REFERENCIAS

[1] Wallach, D., Conrad, J., Steimle, T. The UX Metrics Table: A Missing Artifact, In International Conference of Design, User Experience, and Usability DUXU 2017: Design, User Experience, and Usability: Theory, Methodology, and Management pp 507-517, 2017.

[2] Tähti, M. Arhippainen, L. A Proposal of collecting Emotions and Experiences, In Interactive Experiences in HCI, Volume 2, pp. 195–198, 2004.

[3] Loiola, C. A Systematic Review About User Experience Evaluation. "International Conference of Design, User Experience, and Usability. DUXU 2016: Design, User Experience, and Usability: Design Thinking and Methods pp 445-455.

[4] Darin, T., Coelho B., Borges, B. Which Instrument Should I Use? Supporting Decision- Making About the Evaluation of User Experience. International Conference on Human- Computer Interaction HCII 2019: Design, User Experience, and Usability. Practice and Case Studies pp 49-67, 2019.

[5] Vermeeren, A., Lai-Chong, E., Roto, V., Obrist, M., Hoonhout, J. & Väänänen-Vainio- Mattila, K. User experience evaluation methods: current state and development needs. In Proceedings of the 6th Nordic Conference on Human-Computer Interaction: Extending Boundaries (NordiCHI '10). Association for Computing Machinery, New York, NY, USA, pp 521–530, 2010.

[6] Mora, A. Gamification: a systematic review of design frameworks. Journal of Computing in Higher Education. December 2017, Volume 29, Issue 3, pp 516–548.

[7] Bang K., Kanstrup M.A., Kjems A., Stage J. Adoption of UX Evaluation in Practice: An Action Research Study in a Software Organization. In: Bernhaupt R., Dalvi G., Joshi A., K. Balkrishan D., O’Neill J., Winckler M. (eds) Human-Computer Interaction –

---

<!-- Página 59 -->

47

INTERACT 2017. INTERACT 2017. Lecture Notes in Computer Science, vol 10516. Springer, Cham. 2017.

[8] Matthews, P., Jucá, I., Teixeira, J. Game for Heuristic Evaluation (G4H): A Serious Game for Collaborative Evaluation of Systems. "International Conference on Human- Computer Interaction HCI 2017: Human-Computer Interaction. User Interface Design, Development and Multimodality pp 341-352. 2017.

[9] Walther, B., Juel Larsen, L. Gamification and Beyond: The Case of Ludification. Games and Learning Alliance, pp. 125-135. 2020.

[10] Sonderegger A., Uebelbacher A., Sauer J. The UX Construct – Does the Usage Context Influence the Outcome of User Experience Evaluations?. In: Lamas D., Loizides F., Nacke L., Petrie H., Winckler M., Zaphiris P. (eds) Human-Computer Interaction – INTERACT 2019. INTERACT 2019. Lecture Notes in Computer Science, vol 11749. Springer, Cham. 2019.

[11] Villega, E., S., Labrador, E., Fonseca, D., Fernández-Guinea, S.: Improvement of user experience methodologies through the application of gamification: I'm in methodology. 13th Iberian Conference on Information Systems and Technologies (CISTI), 2018; Spain; 2018.

[12] Brito, C. A Systematic Review About User Experience Evaluation. International Conference of Design, User Experience, and Usability. 2016.

[13] Rivero, L., Conte, T. A Systematic Mapping Study on Research Contributions on UX Evaluation Technologies. IHC 2017 Proceedings of the XVI Brazilian Symposium on Human Factors in Computing Systems. Article No. 5. Brazil; 2017.

[14] Marcus, A., Abromowitz, S. The Driving Machine: Mobile UX Design That Combines Information Design with Persuasion Design. International Conference of Design, User

---

<!-- Página 60 -->

48

Experience, and Usability DUXU 2013: Design, User Experience, and Usability. User Experience in Novel Technological Environments pp 140-149. United States; 2013.

[15] Harms, J., Biegler, S., Wimmer, C. et al. Gamification of Online Surveys: Design Process, Case Study, and Evaluation. IFIP Conference on Human-Computer Interaction INTERACT 2015: Human-Computer Interaction – INTERACT 2015 pp 219-236. Austria; 2015.

[16] Kujala, S., Roto, V., Vaananen-Vainio-Mattila, K., Karapanos, E., Sinnela, A.: UX Curve: a method for evaluating long-term user experience. Interact. Comput. 23(5), 473– 483 (2011).

[17] A. Fernandez, E. Insfran and S. Abrahao, “Usability evaluation methods for the Web: A systematic mapping study”, Information and Software Technology, 53(8), pp. 789-817, 2011.

[18] “Tina” Lee S., Ivory M. What Makes a Good UX Questionnaire? User-Centered Scorecard Development. In: Chung W., Shin C. (eds) Advances in Affective and Pleasurable Design. Advances in Intelligent Systems and Computing, vol 483. Springer, Cham. 2017.

[19] Lallemand, C., Koenig, V. (2017). How Could an Intranet be Like a Friend to Me? - Why Standardized UX Scales Don’t Always Fit. 2017.

[20] Minge, M., Thüring, M. The MeCUE Questionnaire (2.0): Meeting Five Basic Requirements for Lean and Standardized UX Assessment. International Conference of Design, User Experience, and Usability DUXU 2018: Design, User Experience, and Usability: Theory and Practice pp 451-469, 2018.

[21] Zagel, C., Piazza, A., Petrov, Y. et al. SciencOmat: A Gamified Research Platform for Evaluating Visual Attractiveness. International Conference on Applied Human Factors and

---

<!-- Página 61 -->

49

Ergonomics AHFE 2017: Advances in The Human Side of Service Engineering pp 50-60. 2017. [22] Villegas, E., Labrador, E., Fonseca, D. et al. Methodology I’M IN applied to workshop: successful educational practice for consultants in user experience with gamification fields. Universal Access in the Information Society. August 2019, Volume 18, Issue 3, pp 507–521. 2019.

[23] Deterding, S., Dixon, D., Khaled, R., Nacke, L. From Game Design Elements to Gamefulness: Defining Gamification. Proceedings of the 15th International Academic MindTrek Conference: Envisioning Future Media Environments, MindTrek 2011.

[24] Huotari, K., Hamari, J. Defining Gamification - A Service Marketing Perspective. 2012.

[25] Domínguez, A., Saenz-de-Navarrete, J., de-Marcos, L., Fernández-Sanz, L., Pagés, C., Martínez-Herráiz, J. Gamifying learning experiences: Practical implications and outcomes, Computers & Education. Volume 63, 2013, pp. 380-392.

[26] Zaraza, V., Rusu, C., Rusu, P. et al. On User eXperience Evaluation: Combining User Tests and Psychometrics. International Conference on Intelligent Human Systems Integration IHSI 2018: Intelligent Human Systems Integration, pp 626-632. 2018.

[27] Saunders, M., Tosey, P. The Layers of Research Design. 2013.

[28] Vaishnavi, V., Kuechler JR., W. Design science research methods and patterns: Innovating Information and Communication Technology 2nd ed., Florida, UAS: CRC. 2015.

[29] “Chat GPT”. openai.com. https://chat.openai.com (consultado el 10 de julio de 2023).

---

<!-- Página 62 -->

50

[30] Díaz-Oreiro, I., López, G., Quesada, L., Guerrero, L. Standardized Questionnaires for User Experience Evaluation: A Systematic Literature Review. 13th International Conference on Ubiquitous Computing and Ambient Intelligence UCAmI 2019; Toledo, Spain; December 2 to 5th, 2019.

[31] Lallemand, C., Koenig, V. (2017). How Could an Intranet be Like a Friend to Me? - Why Standardized UX Scales Don’t Always Fit. 2017.

[32] Filippi, S., Barattin, D. Exploiting the meCUE Questionnaire to Enhance an Existing UX Evaluation Method Based on Mental Models. International Conference on Human- Computer Interaction HCII 2019: Design, User Experience, and Usability. Practice and Case Studies pp 117-133, 2019.

[33] “Manual de Mario Kart 8 para Nintendo WiiU”. nintendo.com. https://www.nintendo.com/consumer/downloads/manual-WiiU-Mario_Kart_8.pdf (consultado el 10 de julio de 2023).

[34] M. Schrepp. “User Experience Questionnaire Handbook. Procedia Comput. Sci. Hockenheim, Germany, 2019.

[35] “JOCICI 2023”. citic.ucr.ac.cr. https://citic.ucr.ac.cr/eventos/vi-jornadas- costarricenses-investigacion-computacion-e-informatica-jocici (consultado el 18 de octubre de 2023).

---

<!-- Página 63 -->

51

ANEXO 1

Cuestionario estandarizado meCUE

---

<!-- Página 64 -->

52

---

<!-- Página 65 -->

53

---

<!-- Página 66 -->

54

---

<!-- Página 67 -->

55

---

<!-- Página 68 -->

56

ANEXO 2 Cuestionario gamificado meCUE

---

<!-- Página 69 -->

57

---

<!-- Página 70 -->

58

---

<!-- Página 71 -->

59

---

<!-- Página 72 -->

60

---

<!-- Página 73 -->

61

---

<!-- Página 74 -->

62

ANEXO 3 Cuestionario UEQ utilizado para la evaluación de las herramientas meCUE (tanto gamificada como estandarizada)

---

<!-- Página 75 -->

63

---

<!-- Página 76 -->

64

---

<!-- Página 77 -->

65

ANEXO 4 Artículo presentado en las Jornadas Costarricenses de Investigación en Computación e Informática (JOCICI), del año 2023.

---

<!-- Página 78 -->

66

---

<!-- Página 79 -->

67

---

<!-- Página 80 -->

68

---

<!-- Página 81 -->

69

---

<!-- Página 82 -->

70

---

<!-- Página 83 -->

71