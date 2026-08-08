<!-- Página 1 -->

## Uso de la IA en técnicas de experiencia de usuario “Si tomamos las decisiones equivocadas y se escapa de nuestro control, la IA puede llevarnos al fin del Homo Sapiens, al fin de nuestra especie” Yuval Noah Harari Lucas Melgares Carmona UPC CITM (Centro de la Imagen y Tecnología Multimedia) Profesora: Eva Villegas Portero

---

<!-- Página 2 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## AGRADECIMIENTOS

No podría empezar estos agradecimientos sin hacer una mención a mi madre, desde pequeño me dio las alas para comerme el mundo, la única persona que sé con certeza que me seguirá apoyando toda la vida. Gracias mamá por ser todo en mi vida, has sido madre y padre. Por cada sacrificio que has hecho para que nunca nos falte nada, y todas las lecciones que nos has enseñado. Eres mi referente en la vida, te he admirado, te admiro y te admiraré siempre. Este logro también es tuyo, todo lo bueno que hay en mí nace de ti.

A mis abuelos maternos, gracias por ser mis segundos padres, por cuidarme como si fuera vuestro propio hijo y por darme un hogar lleno de cariño, raíces y valores. Os quiero con locura y me siento afortunado de haberos tenido y teneros tan cerca cada día. Habéis sido y sois el claro ejemplo de amor, generosidad y ternura.

A mi hermano pequeño. Siempre intento protegerte, llenarte los vacíos y estar ahí como un hermano y como ese padre que nunca tuvimos. Gracias por hacerme sentir responsable, fuerte y, sobre todo, querido. Eres parte esencial de mi vida.

A mi padrastro, muchísimas gracias por entrar en nuestras vidas con respeto y con cariño. Gracias por acompañarnos desde tan pequeños siendo una figura de apoyo, equilibrio y seguridad. Te agradezco tu forma de estar, sin exigir, simplemente cuidándonos a los tres.

A mi profesora del TFG, Eva Villegas Portero, por acompañarme con paciencia y dedicación, por tus consejos y enseñanzas y por guiarme. Tu seguimiento ha sido clave para dar forma a esta investigación y ayudarme a llegar hasta el final.

Por último, pero no menos importante, gracias a mí mismo. Por todo lo pasado y porque he seguido adelante cuando era más fácil parar. Por no rendirme cuando las dudas eran más grandes que las certezas. Por convertirme en alguien del que, por fin, he empezado a estar orgulloso. Este trabajo no solo cierra una etapa universitaria. Es también el reflejo de todo lo que he vivido, sentido y superado. Y, por encima de todo, es una carta de amor a quienes han caminado conmigo, incluso cuando el camino ha sido cuesta arriba.

A todos vosotros: gracias, con todo mi corazón.

---

<!-- Página 3 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## RESUMEN

Este Trabajo de Final de Grado explora el impacto del uso de la inteligencia artificial (IA) en las técnicas de experiencia de usuario (UX), con especial atención en el ámbito del comercio electrónico. Se cuestiona si la IA es una herramienta transformadora capaz de mejorar la personalización, eficiencia y adaptabilidad de las interfaces digitales, permitiendo experiencias más relevantes, fluidas y centradas en el usuario. A través de la generación de prototipos con herramientas de IA como Visily, Uizard, Mockflow y Websim.ai, se han creado y evaluado distintas pantallas de una tienda online (inicio, login, detalles de producto, seguimiento de pedido y ayuda), todas diseñadas a partir de prompts específicos.

El estudio se ha basado en metodologías de evaluación heurística reconocidas, como las de Jakob Nielsen y Hassan Montero y Yusef, para comparar objetivamente la calidad UX de los resultados obtenidos. Además, se destaca especialmente el rendimiento de la herramienta Visily, cuyos prototipos fueron los más fieles al prompt, consistentes visualmente y claros funcionalmente, lo que ha permitido que posteriormente en conclusiones y análisis, se pueda justificar si la IA puede actuar como un aliado valioso en el proceso de diseño, reduciendo tiempos y potenciando la exploración visual.

Este trabajo no solo ofrece resultados prácticos sobre la implementación de IA en diseño UX, sino que también abre reflexiones sobre sus implicaciones éticas, su impacto en la profesión del diseñador y su potencial para la creación de experiencias digitales más inclusivas y accesibles.

## PALABRAS CLAVE

Inteligencia artificial, Experiencia de usuario (UX), Interfaz de usuario (UI), Prototipado con IA, Evaluación heurística, E-commerce, Personalización, Usabilidad y Diseño centrado en el usuario.

---

<!-- Página 4 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## ÍNDICE ÍNDICE DE FIGURAS ........................................................................................................... 1 1. Introducción ................................................................................................................. 3

- 1.1. Justificación del proyecto ..................................................................................... 3

- 1.2. Objetivos generales y específicos ....................................................................... 5 2. Metodología de trabajo ................................................................................................... 6

3. Planificación .................................................................................................................... 8 - 3.1. Herramienta de planificación y su justificación ..................................................... 8

- 3.2. Planificación en base a la metodología exploratoria y experimental. ................. 11 3.2.1. Diagrama de Gantt ............................................................................................. 13

- 3.3. Seguimiento de la Planificación en base a la metodología exploratoria y experimental. ................................................................................................................... 13

- 3.4. Análisis DAFO ................................................................................................... 16 - 3.5. Análisis Inicial de Costes ................................................................................... 17

- 3.6. Impacto ambiental y responsabilidad social ....................................................... 20

4. Marco Teórico ............................................................................................................... 25 - 4.1. Conceptos básicos de la Inteligencia Artificial (IA) ...................................... 25

4.1.1. Definición y evolución de la IA............................................................................ 25 - 4.2. Experiencia de usuario ................................................................................... 28

4.2.1. Tipos de IA más utilizados hoy día en la UX ...................................................... 30 4.2.2. Tecnologías emergentes similares en el campo de la IA. ................................... 31

- 4.3. Funcionamiento de la IA en la experiencia de usuario (UX) ......................... 33 4.3.1. Funcionamiento general de los algoritmos de IA ................................................ 35

4.3.2. Impacto de la IA en el diseño de experiencia de usuario .................................... 38

4.3.3. Diferencias entre UX tradicional y UX impulsado por IA ..................................... 41 - 4.4. Ética y retos en la implementación de la IA a UX .......................................... 43

5. Estado del Arte .............................................................................................................. 44 - 5.1. Estudio de casos y aplicaciones actuales ..................................................... 44

5.1.1. IA en la industria de los videojuegos .................................................................. 45 5.1.2. IA en el marketing digital .................................................................................... 51

5.1.3. IA en otros sectores: e-commerce, salud, educación ......................................... 57 - 5.2. Comparativa de herramientas y tecnologías disponibles ............................ 64

5.2.1. Herramientas de IA de código abierto ................................................................ 65 5.2.2. Plataformas comerciales para la IA a UX ........................................................... 69

5.2.3. Evaluación de su impacto en la industria ........................................................... 74

6. Proyecto ........................................................................................................................ 77

---

<!-- Página 5 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- 6.1. Desarrollo de prototipos con IA ..................................................................... 77 6.1.1. Herramientas / softwares de prototipado ............................................................ 77

6.1.2. Definición de perfiles de usuario ........................................................................ 82 6.1.3. Implementación de prompts de personalización y análisis ................................. 87

6.1.4. Diseño de un prototipo de UI impulsado por IA .................................................. 97 - 6.2. Evaluación del impacto de la IA en UX ........................................................ 110

6.2.1. Evaluación Heurística utilizando heurísticas de Hassan Montero y Yusef ........ 112

6.2.1.1 Uizard ......................................................................................................... 112 6.2.1.2 Visily ........................................................................................................... 115

6.2.1.3 Mockflow .................................................................................................... 117 6.2.1.4 Websim.ai ................................................................................................... 120

6.2.2. Evaluación Heurística utilizando heurísticas de Jacob Nielsen......................... 122 6.2.2.1 Uizard ......................................................................................................... 122

6.2.2.2 Visily ........................................................................................................... 125 6.2.2.3 Mockflow .................................................................................................... 127

6.2.2.4 Websim.ai ................................................................................................... 129

6.2.3. Mejor herramienta / software de prototipado .................................................... 132 - 6.3. Desarrollo de prototipos con IA mediante Visily ......................................... 135

6.3.1. Página de Login ............................................................................................... 135 6.3.2. Página de Detalles de un producto .................................................................. 138

6.3.3. Página de Seguimiento .................................................................................... 142 6.3.4. Página de Ayuda .............................................................................................. 145

7. Conclusiones .............................................................................................................. 149 8. Referencias.................................................................................................................. 152

---

<!-- Página 6 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## ÍNDICE DE FIGURAS

“Fig 1 Promp que se le ha proporcionado" ............................................................................ 9 “Fig 2 Planificación del Proyecto” ........................................................................................ 10 “Fig 3 Planificación del Proyecto" ........................................................................................ 10 “Fig 4 Planificación del Proyecto” ........................................................................................ 11 “Fig 5 Diagrama de Gantt”.................................................................................................. 13 “Fig 6 Cronograma de la Planificación actualizado" ............................................................ 16 “Fig 7 Cronograma02 de la Planificación actualizado" ........................................................ 16 “Fig 8 Análisis DAFO” ......................................................................................................... 17 “Fig 9 Emisiones generadas en 2024” ................................................................................. 22 “Fig 10 Portada de La Tierra Media: Sombras de Mordor y el Sistema Némesis” ............... 47 “Fig 11 Portada No Man's Sky y la generación procedimental del universo” ....................... 48 “Fig 12 Portada Alien: Isolation" .......................................................................................... 49 “Fig 13 Portada Dota 2"....................................................................................................... 50 “Fig 14 Coca-Cola recrea su anuncio navideño más icónico con la IA como total protagonista” ....................................................................................................................... 52 “Fig 15 La netflixización de los contenidos en marketing digital” ......................................... 53 “Fig 16 Sephora y ejemplo de implementación de su chatbots” .......................................... 54 “Fig 17 Amazon está introduciendo anuncios en Rufus, su asistente de IA para la compra” 55 “Fig 18 Spotify usa la IA para crear anuncios en los podcasts entre otros sectores” ........... 56 “Fig 19 Amazon tiene un nuevo aliado, la IA" ...................................................................... 58 “Fig 20 Volumen bruto de mercancías de Alibaba durante el Singles’ Day en China” ......... 59 “Fig 21 Zalando y su probador virtual” ................................................................................. 60 “Fig 22 IBM Watson Health logo” ........................................................................................ 60 “Fig 23 PathAI logo” ............................................................................................................ 61 “Fig 24 DeepMind logo”....................................................................................................... 61 “Fig 25 Duolingo y su nueva herramienta Stories”............................................................... 62 “Fig 26 Squirrel logo startup china” ..................................................................................... 62 “Fig 27 Khan Academy logo” ............................................................................................... 63 “Fig 28 TensorFlow y sus sistemas de recomendación” ...................................................... 66 “Fig 29 PyTorch logo”.......................................................................................................... 67 “Fig 30 Hugging Face logo” ................................................................................................. 68 “Fig 31 OpenCV logo” ......................................................................................................... 69 “Fig 32 Adobe Sensei logo” ................................................................................................. 70 “Fig 33 Salesforce Einstein logo” ........................................................................................ 72 “Fig 34 Amazon Personalize logo” ...................................................................................... 73 “Fig 35 User Persona - El comprador impulsivo” ................................................................. 84 “Fig 36 User Persona - El buscador informado” .................................................................. 85 “Fig 37 User Persona - El usuario leal o recurrente” ........................................................... 85 “Fig 38 User Persona - El comprador ocasional” ................................................................. 86 “Fig 39 User Persona - El usuario indeciso” ........................................................................ 86 “Fig 40 Página Home Amazon" ........................................................................................... 90 “Fig 41 Página de Login Amazon" ....................................................................................... 91 “Fig 42 Página de Producto específico de Amazon"............................................................ 91 “Fig 43 Página de Seguimiento de Amazon" ....................................................................... 92

LUCAS MELGARES CARMONA 1

---

<!-- Página 7 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 44 Página de Ayuda de Amazon"................................................................................. 92 “Fig 45 Planes de Uizard" ................................................................................................... 98 “Fig 46 Interfaz Uizard" ....................................................................................................... 99 “Fig 47 Chat con la IA" ...................................................................................................... 100 “Fig 48 Prototipo de Uizard" .............................................................................................. 101 “Fig 49 Opciones para empezar un proyecto" ................................................................... 102 “Fig 50 Espacio de trabajo Visily" ...................................................................................... 103 “Fig 51 Consola de Prompts de Visily" .............................................................................. 103 “Fig 52 Prototipo 01 Visily" ................................................................................................ 104 “Fig 53 Prototipo 02 Visily" ................................................................................................ 105 “Fig 54 Espacio de trabajo de MockFlow" ......................................................................... 106 “Fig 55 Consola de prompts MockFlow" ............................................................................ 106 “Fig 56 Prototipo 01 MockFlow" ........................................................................................ 107 “Fig 57 Prototipo 02 MockFlow" ........................................................................................ 107 “Fig 58 Interfaz Websim.ai" ............................................................................................... 108 “Fig 59 Consola de Prompts de Websim.ai" ...................................................................... 108 “Fig 60 Prototipo 01 Websim.ai" ........................................................................................ 109 “Fig 61 Prototipo 02 Websim.ai" ........................................................................................ 109 “Fig 62 Prototipo 03 Websim.ai" ........................................................................................ 109 “Fig 63 Prototipo 04 Websim.ai" ........................................................................................ 109 “Fig 64 Resultado Final Login" .......................................................................................... 136 “Fig 65 Resultado Final Detalles Producto 01" .................................................................. 139 “Fig 66 Resultado Final Detalles Producto 02" .................................................................. 139 “Fig 67 Resultado Final Detalles Producto 03" .................................................................. 140 “Fig 68 Resultado Final Seguimiento" ............................................................................... 143 “Fig 69 Resultado Final Ayuda01" ..................................................................................... 146 “Fig 70 Resultado Final Ayuda02" ..................................................................................... 146 “Fig 71 Resultado Final Ayuda02" ..................................................................................... 147

LUCAS MELGARES CARMONA 2

---

<!-- Página 8 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## 1. Introducción

- 1.1. Justificación del proyecto

Se ha elegido el tema "Uso de la IA en técnicas de experiencia de usuario" para el Trabajo de Final de Grado porque se trata de un área de gran relevancia en la actualidad, con un impacto significativo tanto presente como futuro. La inteligencia artificial (IA) está revolucionando múltiples aspectos de nuestras vidas, y la experiencia de usuario (UX) no es una excepción. Se quiere explorar cómo la IA puede mejorar la eficiencia de las técnicas UX, en la manera en que interactuamos con productos y servicios digitales, personalizando y mejorando experiencias y sensaciones de los usuarios, de forma que antes eran impensables. En este caso la IA, se utiliza como una herramienta muy potente que trabaja junto un consultor UX.

En mi opinión, en la actualidad, la personalización es clave para captar y retener a los usuarios. Plataformas como Netflix, Amazon y Spotify utilizan IA para ofrecer recomendaciones ajustadas a los gustos individuales, demostrando que la personalización no solo mejora la satisfacción del usuario, sino también su compromiso y lealtad (El papel de la inteligencia artificial en el diseño UX/UI, 2025). En este proyecto, se quiere investigar cómo se puede mejorar la eficiencia de los procesos UX (User Experience) y UI (User Interface) gracias a la IA.

Tradicionalmente, la UX se ha basado en datos recogidos de estudios de usuarios para diseñar productos centrados en sus necesidades. Sin embargo, la IA permite ajustar y personalizar las experiencias en tiempo real, algo que se considera esencial, en un mundo donde las expectativas de los usuarios están en constante cambio.

Otro punto importante es el impacto de la IA en diversas industrias. Es interesante explorar cómo la IA puede aplicarse no solo en el sector de los videojuegos o el marketing digital, sino también en campos como la educación, la salud y el comercio electrónico. Cada uno de estos sectores puede beneficiarse enormemente de una experiencia de usuario mejorada mediante IA, y llama la atención investigar estos casos para demostrar la versatilidad de esta tecnología.

LUCAS MELGARES CARMONA 3

---

<!-- Página 9 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Mirando hacia el futuro, el uso de la IA en UX no solo impactará en los productos y servicios que se usa, sino también en el mercado laboral y en la educación. La creciente demanda de profesionales con habilidades en IA y UX hace que este tema no solo sea relevante desde un punto de vista técnico, sino también estratégico para mi desarrollo profesional. (Habilidades de IA que todo

diseñador UX/UI necesita, 2025). Considero que, trabajar en este proyecto me posicionará como un pionero en una disciplina que está en constante evolución y que es clave para el futuro de la interacción digital.

Además, llama la atención la capacidad de la IA para fomentar la innovación y la mejora continua. Los algoritmos de IA no solo pueden aprender de los datos actuales, sino que también pueden predecir tendencias futuras, permitiendo que las experiencias de usuario se adapten a las necesidades emergentes. Este potencial para la innovación es algo que se quiere explorar a fondo en el proyecto.

Asimismo, hay desafíos éticos asociados con el uso de la IA, como los sesgos algorítmicos y las preocupaciones sobre la privacidad. En el trabajo, se incluye un apartado en el que se aborda estos retos, para asegurar que las soluciones que se proponen sean justas y respetuosas con los derechos de los usuarios. Es esencial desarrollar sistemas de IA que sean no solo eficientes, sino también éticos y transparentes, que es un tema que hoy día también se está empezando a asentar.

Por último, hay un gran potencial en la IA para mejorar la inclusividad en las interfaces digitales. Es importante tener en cuenta, la idea de explorar cómo la IA puede diseñar experiencias accesibles para personas con discapacidades o necesidades especiales, contribuyendo así a una tecnología más inclusiva y equitativa.

En resumen, el tema del TFG no sólo es relevante por su aplicación actual, sino por su capacidad de moldear el futuro de la interacción con sistemas, webs, servicios, ... A través de este proyecto, se espera aportar conocimientos valiosos sobre cómo la IA puede integrarse de manera efectiva y ética en la experiencia de usuario, demostrando sus beneficios y anticipando sus desafíos. Esta investigación no solo contribuirá al campo de la UX, sino que también proporcionará una base sólida para seguir explorando este apasionante y dinámico campo en el futuro.

LUCAS MELGARES CARMONA 4

---

<!-- Página 10 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- 1.2. Objetivos generales y específicos

El objetivo principal en este proyecto es explorar cómo la inteligencia artificial (IA) puede mejorar las técnicas de experiencia de usuario (UX) en diferentes ámbitos e industrias para así, poder valorar su efectividad. Se realizará

1 mediante la creación de prototipos y pruebas con “prompts”de IA en para diferentes técnicas de UI. A través de estas pruebas, se buscará identificar las ventajas de implementar IA en la personalización de experiencias digitales, así como su impacto en la interacción del usuario en diferentes sectores.

Actualmente, se ha decidido centrar las pruebas en el ámbito del comercio electrónico, tomando como referencia Amazon, una de las plataformas más avanzadas y optimizadas en términos de experiencia de usuario (UX). Amazon es un referente en el uso de inteligencia artificial aplicada a la personalización de contenidos, la recomendación de productos y la optimización de la navegación, lo que la convierte en un caso de estudio ideal para evaluar el impacto de la IA en UX. A través del análisis de sus algoritmos y el desarrollo de pruebas específicas, se pretende explorar cómo la inteligencia artificial contribuye a mejorar la interacción del usuario y la eficiencia de la plataforma. Así, el objetivo principal consiste en analizar el impacto de la inteligencia artificial en la personalización y la mejora de la eficiencia en el diseño de interfaces de plataformas de comercio electrónico, mediante la implementación y evaluación de prototipos basados en prompts de IA.

Como objetivos más específicos, tal y como he mencionado anteriormente, se implementarán “prompts” que servirán para diseñar y analizar resultados de técnicas, además de probar y evaluar el rendimiento de la IA en términos de la interacción con el usuario en diversas interfaces.

Una vez hecho este proceso también resulta interesante y relevante poder extraer ciertas conclusiones basadas en los resultados de las pruebas iniciales e identificar en qué sectores la implementación de IA ofrece los mayores

beneficios en términos de personalización y satisfacción del usuario.

1 Un modelo de difusión capaz de generar imágenes, audios, textos, páginas de ventas… permitirán evaluar la capacidad de la IA para personalizar la experiencia del usuario de manera dinámica y en tiempo real, ajustando los contenidos y las interacciones según las preferencias y comportamientos del usuario.

LUCAS MELGARES CARMONA 5

---

<!-- Página 11 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## 2. Metodología de trabajo

Se utilizará una metodología exploratoria y experimental, ya que permite investigar de manera flexible y abierta cómo la inteligencia artificial (IA) puede mejorar la experiencia de usuario (UX) en diferentes sectores. La naturaleza exploratoria es ideal porque el ámbito de aplicación aún no está definido con precisión, lo que permite examinar múltiples sectores, como videojuegos, marketing digital y comercio electrónico sin limitaciones. Esta metodología se complementa con un enfoque experimental, donde se generarán prototipos mediante diferentes tipos de IA y se pondrá a prueba su eficacia. Al implementar esta metodología, se busca generar conocimiento práctico sobre la interacción entre IA y UX, lo que se considera fundamental debido a la falta de investigaciones concluyentes en este campo específico. Considero que este enfoque es el más adecuado para el trabajo, ya que proporciona la flexibilidad necesaria para adaptar el estudio según los hallazgos que surjan y permite obtener resultados que validen las hipótesis planteadas o que hayan podido surgir realizando el estudio.

- FASE 1: Estado actual de la IA aplicada a la UX En primer lugar, se llevará a cabo una revisión exhaustiva para comprender el estado actual de la IA aplicada a la UX. Se examinarán las técnicas de IA más relevantes, además, se explorarán casos de estudio en los ámbitos mencionados para identificar tendencias y mejores prácticas en la implementación de IA en interfaces de usuario, siempre y cuando esto sea posible.

- FASE 2: Caso práctico En segundo lugar, se va a proceder a medir esta mejora de la eficacia de los procesos de UX y UI implementando IA. Definiendo que tipos de pruebas se elaborarán, donde y como se implementarán, mediante el uso de prompts y prototipos generados por diferentes tipos de IA, siguiendo la estructura de pasos de un proceso UX: Análisis e investigación, Ideación y concepto, Wireframes o Prototipado, y Documentación final.

- FASE 3: Implementación y recopilación de datos En tercer lugar, tenemos el desarrollo y la implementación de estas pruebas, en el comercio electónico. Se recogerán datos cualitativos y cuantitativos,

LUCAS MELGARES CARMONA 6

---

<!-- Página 12 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

evaluando tanto el rendimiento técnico de la IA como el grado de personalización y satisfacción del usuario. Se utilizarán métricas específicas para medir el impacto en la UX, tales como el tiempo de interacción, la facilidad de uso y el nivel de personalización percibido.

- FASE 4: Análisis Finalmente, tras analizar los resultados de las pruebas, se elaborarán conclusiones sobre la viabilidad y efectividad del uso de IA en la personalización de UX en los diferentes ámbitos probados. Se identificarán los sectores donde la IA ha mostrado mayor potencial y se harán recomendaciones para futuras implementaciones y mejoras en el diseño de experiencias personalizadas.

LUCAS MELGARES CARMONA 7

---

<!-- Página 13 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## 3. Planificación

- 3.1. Herramienta de planificación y su justificación

MyMap.AI es una aplicación que ofrece diagramas interactivos y desarrollo de mapas conceptuales de diagramas Pert, líneas de tiempo y otros materiales visuales requeridos por los profesionales en el diseño de los proyectos complicados. Está completamente equipado con algoritmos de inteligencia artificial robustos que traducen los datos de texto proporcionados en consecuencia, esta función los convierte en esquemas completos y significativos. Es decir, el usuario mediante una especie de chatbox le va proporcionar diferentes datos con fechas o etapas del proyecto al que se refiere y él, lo plasmará de manera visual. MyMap.AI es una herramienta inteligente que trabaja con algoritmos avanzados de inteligencia artificial, interpretando la información de texto proporcionada en diagramas claros, fáciles de entender y comprensibles. Se encargan y ahorran tiempo a niveles funcionales al ser altamente instructivos en su visualización sobre cualquier proyecto que se presente para su visualización. MyMap.AI se diferencia en el manejo intuitivo incluso de los datos más complejos; el desarrollo rápido permite una iteración rápida y ajustes sobre la marcha.

Entre varios escenarios, MyMap.AI puede volverse aplicable a la parte de "Planificación" en el marco de TFG debido a varias razones: en primer lugar, el TFG trata el “Uso de la IA en técnicas de experiencia de usuario” y sus resultados particulares que causa para distintas esferas; por lo tanto, el objetivo se transforma en evaluar la experiencia, nivel de satisfacción, comodidad… con dispositivos basados en IA. Así, la aplicación de la solución basada en inteligencia artificial se mantiene en perfecta armonía con el tema que se está analizando durante el proceso de trabajo.

Es cierto que antes se pensó e incluso se empezó a organizar con herramientas más convencionales como puede ser Trello, pero a diferencia de Trello y los sistemas más clásicos tienen en cuenta el espacio según listas lineales y líneas de tiempo, en cambio, MyMap.AI tiene una visión más interesante y comprende la complejidad y las interconexiones entre las diferentes etapas del trabajo, mejorando la integridad de dicho trabajo a lo largo de múltiples fases, desde los análisis teóricos hasta la implementación

LUCAS MELGARES CARMONA 8

---

<!-- Página 14 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

práctica. Además, MyMap.AI permite realizar valiosos desarrollos gráficos avanzados útiles no solo en la gestión interna sino también para la elaboración de información visual que se agregará al TFG final, mejorando la presentación y haciendo que el lector comprenda de manera más clara y atractiva cómo se realizó la planificación y la organización del trabajo.

En este sentido, la elección de esta herramienta subraya la atención a la innovación que ha caracterizado, hasta hoy, el desarrollo del TFG; de hecho, la IA no es solo el objeto del estudio sino, de manera efectiva y concreta, un instrumento para su realización.

“Fig 1 Promp que se le ha proporcionado"

LUCAS MELGARES CARMONA 9

---

<!-- Página 15 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 2 Planificación del Proyecto”

“Fig 3 Planificación del Proyecto"

LUCAS MELGARES CARMONA 10

---

<!-- Página 16 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 4 Planificación del Proyecto”

- 3.2. Planificación en base a la metodología exploratoria y experimental.

Como el trabajo se realiza en una metodología exploratoria y experimental, se ha estructurado el trabajo en varias fases, para poder tener más flexibilidad para adaptarse a nuevos descubrimientos que puedan surgir durante la investigación. Además, tal y como se ha comentado y se ha visto antes, se ha elaborado un cronograma detallado utilizando MyMap.AI. Esta herramienta permite una visualización clara y adaptable de la planificación, asegurando la flexibilidad necesaria a medida que avanza la investigación.

El cronograma se ha organizado en fases clave para optimizar la gestión del tiempo y los recursos:

Inicio del TFG (Agosto - Octubre 2024)

- Definición del alcance del estudio.

- Revisión de la literatura y estado del arte sobre IA y UX. - Creación del esquema general del trabajo y selección de herramientas.

LUCAS MELGARES CARMONA 11

---

<!-- Página 17 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Reuniones estratégicas con la tutora

- Primera reunión (Octubre 2024): Validación del índice y estructura preliminar. - Segunda reunión (Noviembre 2024): Confirmación de la metodología y marco teórico. - Tercera reunión (Diciembre 2024): Revisión del enfoque experimental y selección de casos de estudio.

- Cuarta reunión (Enero 2025): Revisión global y ajustes metodológicos.

Implementación experimental (Diciembre 2024 - Febrero 2025)

- Desarrollo de los prototipos en Amazon, analizando su enfoque en UX. - Aplicación de técnicas de IA para analizar la experiencia del usuario. - Recopilación y procesamiento de datos para evaluar el impacto de la IA en UX.

Evaluación y análisis de resultados (Enero - Febrero 2025)

- Interpretación de los datos obtenidos en las pruebas. - Comparación con estudios previos y formulación de conclusiones. - Ajustes finales en función de los hallazgos obtenidos.

Entrega de la primera parte (Marzo 2025)

- Presentación de avances iniciales a la tutora. - Evaluación del progreso y posibles mejoras.

Revisión y feedback (Febrero - Abril 2025)

- Ajustes finales en el documento. - Corrección y refinamiento del análisis de resultados. - Integración de gráficos y diagramas generados con IA para mejorar la visualización de la información.

Finalización del TFG y entrega definitiva (Mayo 2025)

- Revisión final del documento y ajustes de formato. - Entrega oficial del trabajo final.

LUCAS MELGARES CARMONA 12

---

<!-- Página 18 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Preparación de la defensa y presentación de los hallazgos principales.

Este esquema garantiza un enfoque estructurado y adaptable, asegurando que cada etapa del TFG se desarrolla con la profundidad y el análisis necesarios.

3.2.1. Diagrama de Gantt

Además, a continuación, también se incluye un diagrama de Gantt. Una herramienta muy útil de planificación y gestión de proyectos que ayuda a visualizar las tareas y los principales hitos de una forma clara y práctica. Se puede visualizar las diferentes fases del proyecto o la programación que se ha llevado a cabo. Se representa mediante barras horizontales, en la que cada una representa una de estas fases o etapas del proceso, indicando su longitud y la duración de la tarea.

“Fig 5 Diagrama de Gantt”

- 3.3. Seguimiento de la Planificación en base a la metodología exploratoria y experimental.

A continuación, se volverá a detallar cual es la Planificación que se ha seguido después de la primera entrega, especificando cuales son las fases más importantes y que las compone, tal y como se especifica en el apartado anterior. Al igual que en el anterior punto, el cronograma se ha organizado en fases clave para optimizar la gestión del tiempo y los recursos:

Inicio del TFG (Agosto - Octubre 2024)

LUCAS MELGARES CARMONA 13

---

<!-- Página 19 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Definición inicial del alcance del estudio. - Revisión de literatura y estado del arte sobre IA y UX. - Creación del esquema general del trabajo y selección de herramientas.

Reuniones estratégicas con la tutora

- Primera reunión (Octubre 2024): Validación del índice y estructura preliminar. - Segunda reunión (Noviembre 2024): Confirmación de metodología y marco teórico. - Tercera reunión (Diciembre 2024): Revisión del enfoque experimental y selección de casos de estudio. - Cuarta reunión (Enero 2025): Revisión global y ajustes metodológicos.

Implementación experimental (Diciembre 2024 - Febrero 2025)

- Desarrollo de los prototipos en los entornos seleccionados (Amazon u otras plataformas UX relevantes). - Aplicación de técnicas de análisis de la experiencia del usuario mediante IA. - Recopilación y procesamiento de datos para evaluar el impacto de la

IA en UX.

Evaluación y análisis de resultados (Enero - Febrero 2025)

- Interpretación de datos obtenidos en las pruebas. - Comparación con estudios previos y extracción de conclusiones. - Ajustes finales en función de los hallazgos.

Entrega de la primera parte (Marzo 23, 2025)

- Presentación de avances iniciales a la tutora. - Evaluación del progreso y posibles mejoras.

Nuevas reuniones y avances tras la primera entrega

- Reunión final de marzo (Marzo 2025): Reunión de feedback con la tutora sobre la primera entrega. - Reunión de abril (principios): Inicio oficial de la parte práctica del proyecto.

LUCAS MELGARES CARMONA 14

---

<!-- Página 20 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Reunión de abril (mediados): Resolución de dudas y enfoque para la fase final. - Reunión de mayo (principios): Última reunión previa a la entrega final.

Entrega de la segunda parte (Mayo 11, 2025)

- Segunda entrega formal del trabajo: planificación, metodología, desarrollo y escritura.

Feedback de la segunda parte (Mayo 2025)

- Meeting para evaluar posibles mejoras y maneras de encarar la parte final del trabajo.

Revisión y cierre (Mayo - Junio 2025)

- Revisión final del documento y formato de presentación. - Preparación de la defensa y presentación de los hallazgos principales. - Meeting final para la revisión antes de la entrega.

Entrega final TFG (Junio 30, 2025)

- Tercera y última entrega formal del trabajo: Deposito final de TFG.

En este esquema actualizado, queda reflejado cual ha sido la planificación que se ha llevado a cabo y nuevas reuniones, y al igual que el anterior asegurando que cada etapa del TFG se desarrolla con la profundidad y el análisis necesarios.

A continuación, también se mostrará la imagen actualizada de la línea de tiempo actualizada con los nuevos hitos que se acaban de describir. La plataforma Mymap.ai ofrece un plan gratuito que he utilizado para crear la primera versión de mi cronograma del TFG, que incluye los hitos iniciales hasta la entrega de la primera parte del proyecto. Sin embargo, al intentar añadir los nuevos hitos posteriores al 23 de marzo de 2025, la herramienta me solicita ingresar una tarjeta de crédito para continuar. Por esta razón, he optado por replicar la línea de tiempo que tenía hecha hasta ahora, incluyendo los nuevos eventos, en una herramienta alternativa llamada: draw.io. Esta es una aplicación en línea para la creación de diagramas, muy versátil, que permite generar diagramas de flujo, UML, esquemas de bases de datos, redes,

LUCAS MELGARES CARMONA 15

---

<!-- Página 21 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

maquetas y más. Como novedad, actualmente incorpora una sección de inteligencia artificial llamada "Generate", a la cual le voy a pedir que recree mi cronograma completo, incluyendo los nuevos hitos que he definido, de forma automatizada y visualmente clara. Una vez probada esta nueva opción de IA se ha comprobado que no sirve para poder generar cronogramas, simplemente

es una ayuda muy limitada que se ofrece dentro de un proyecto ya empezado.

“Fig 6 Cronograma de la Planificación actualizado"

“Fig 7 Cronograma02 de la Planificación actualizado"

- 3.4. Análisis DAFO

Este análisis, permite poder evaluar de una manera estratégica las Debilidades, Amenazas, Fortalezas y Oportunidades del estudio sobre la implementación de la IA en la experiencia de usuario. Justificando decisiones metodológicas, identificando riesgos, proponiendo soluciones y optimizando el desarrollo del proyecto. También, fortalece la argumentación al demostrar la planificación estructurada y ofreciendo una visión crítica, reforzando la solidez del trabajo ante el tribunal evaluador. Al detectar oportunidades y desafíos, este análisis, permite maximizar el impacto del TFG y mejorar la organización

LUCAS MELGARES CARMONA 16

---

<!-- Página 22 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

del proceso de investigación. En general sirve para poder tener una idea de que es a lo se enfrentará en el proceso de la elaboración del trabajo.

En el caso de este TFG, el análisis DAFO se ha centrado en evaluar cómo la inteligencia artificial aplicada a la experiencia de usuario puede representar

una ventaja competitiva, los desafíos que puede implicar su implementación, y los riesgos asociados a la dependencia de herramientas emergentes. Se han analizado aspectos como la innovación del enfoque, la falta de estudios previos concluyentes en el área, la necesidad de validación experimental y la accesibilidad a herramientas de IA avanzadas. Además, se han incorporado Riesgos y Plan de Contingencias para mitigar posibles problemas en el desarrollo del proyecto y un Análisis Inicial de Costes, considerando recursos tecnológicos y el tiempo de investigación requerido. Este planteamiento permite estructurar de manera más efectiva la planificación y ejecución del TFG, asegurando una visión estratégica clara y fundamentada.

“Fig 8 Análisis DAFO”

- 3.5. Análisis Inicial de Costes

El siguiente apartado detalla de manera exhaustiva el análisis de costes asociados al desarrollo del Trabajo de Fin de Grado (TFG), desglosando los

LUCAS MELGARES CARMONA 17

---

<!-- Página 23 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

gastos directos e indirectos involucrados. Se ha tenido en cuenta tanto el uso de recursos tecnológicos y software específico, como los costes asociados al tiempo de dedicación y otros gastos operativos. Este análisis tiene como objetivo proporcionar una visión clara y transparente de los recursos necesarios para llevar a cabo el proyecto, así como justificar la inversión en

cada uno de los apartados contemplados.

La tabla que se muestra a continuación recoge los principales conceptos económicos, estructurados en categorías: Salario, Hardware, Software y Otros. Dentro de cada categoría, se detalla la amortización mensual y anual de los recursos, así como el importe total estimado. Se ha incluido la cuota de autónomo, ya que el proyecto es realizado de manera independiente, utilizando principalmente medios propios como el ordenador personal MSI GF63 Thin 9SC y servicios en la nube para almacenar y gestionar diferentes tipos de datos.

En cuanto al software, se han considerado herramientas esenciales para el desarrollo del TFG, como Figma Pro para prototipado, Adobe Creative Cloud para edición y diseño, y ChatGPT Plus. También se incluye el uso de MyMap.AI, una herramienta clave en la planificación del proyecto, y otros programas de inteligencia artificial para el desarrollo de prototipos y automatización de tareas. Por otra parte, se han contemplado los costes indirectos derivados del consumo de electricidad, telefonía y desplazamientos, así como una partida para imprevistos que cubre posibles gastos adicionales no previstos inicialmente.

Esta estructura permite reflejar no solo los costes económicos directos, sino también el valor del tiempo invertido, estimado en un total de 160 horas dedicadas al proyecto, con una dedicación total aproximada de 8 meses. El precio/hora resultante es de 25 €/hora, lo que ofrece una referencia clara del esfuerzo económico y temporal involucrado en el TFG.

AmortizaciónImporteImporte Gastos Cantidad TOTAL (€) (meses)ANUALMENSUAL SALARIO

LUCAS MELGARES CARMONA 18

---

<!-- Página 24 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Salario (sin incluir 12 30000 2500 1 20000 autónomo) Cuota de 8 720 90 1 720 Autónomo HARDWARE MSI GF63 Thin 36 900 25 1 200 9SC Periféricos y 24 480 20 1 160 mantenimiento SOFTWARE Figma Pro 8 96 12 1 96 Google Drive 8 66,64 8,33 1 66,64 (Almacenamiento) Adobe Creative 8 552 69 1 552 Cloud ChatGPT Plus 8 160 20 1 160 Otros programas 8 80 10 1 80 (MyMap.AI) Otros programas de IA para prototipos8 400 50 1 400 (Runway ML, Midjourney) OTROS Electricidad 8 400 50 1 400 Telefonía 8 400 50 1 400 Material de oficina 8 160 20 1 160 Desplazamientos 8 1000 125 1 1000 Imprevistos 8 200 25 1 200 TOTAL 30671,64

- Dedicación total: 8 meses

- Total de horas dedicadas: 160 horas

- Precio/Hora: 25 €/hora

- Fórmula del cálculo del importe total de las horas de dedicación:

El importe total de las horas de dedicación se calcula utilizando la siguiente fórmula:

Importe Total = Precio/Hora × Total de Horas Dedicadas

LUCAS MELGARES CARMONA 19

---

<!-- Página 25 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Aplicando esta fórmula obtenemos:

Importe Total = 25 €/hora × 160 horas = 4000 €

- Fórmula del cálculo del importe total de la tabla:

El importe total de la tabla se calcula sumando el coste de cada elemento listado:

Importe Total = Σ (Coste de cada elemento)

Aplicando esta fórmula al presente caso:

Importe Total = 20000 + 720 + 200 + 160 + 96 + 66,64 + 552 + 160 + 80 + 400 + 400 + 400 + 160 + 1000 + 200 = 30671,64 €

Horas de dedicación Importe TOTAL (€)

80 horas 2000,00

100 horas 2500,00

160 horas 4000,00

- 3.6. Impacto ambiental y responsabilidad social

El desarrollo y aplicación de la inteligencia artificial (IA) en la experiencia de usuario (UX) conlleva implicaciones tanto ambientales como sociales. Este apartado analiza el impacto de la investigación en estos ámbitos y las medidas para minimizar efectos negativos, promoviendo una implementación ética,

eficiente y sostenible.

1. Uso del hardware

PC de desarrollo, portátiles, etc.

- Consumo de energía: El consumo de energía del hardware se mide en vatios (W), lo que indica la potencia utilizada en un momento dado. Para calcular el consumo total de energía a lo largo del tiempo, utilizamos kilovatios-

LUCAS MELGARES CARMONA 20

---

<!-- Página 26 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

hora (kWh). El MSI GF63 Thin 9SC tiene un consumo aproximado de 135 W. - Fórmula del consumo de energía: KWh = (Vatios x Horas de uso) / 1000 - Cálculo del consumo para 8 horas de uso diario durante 8

meses: KWh = (135 W x 8 h x 240 días) / 1000 = 259,2 kWh - Factor de emisión: El factor de emisión en España se estima en 0,231 kg CO2/kWh. - Cálculo de CO2 equivalente: Emisiones de CO2 (kg) = 259,2 kWh x 0,231 kg CO2/kWh = 59,38 kg CO2 - Amortización del hardware: La principal fuente de gases de efecto invernadero es la producción de portátiles, ya que alrededor del 80% del impacto se deriva de esta etapa. Un estudio de 230 portátiles específicos sugiere una huella de carbono promedio de 331 kilogramos de CO2 equivalente (CO2e) para un portátil nuevo durante su producción. Sin embargo, el portátil también se utiliza para otras cosas, por lo que debe indicarse aquí la parte proporcional a su vida útil.

Suponiendo 4 años de uso y 8 h/día, cada hora de uso es: 1 h = (331 kg de CO2 / (4 x 365 x 8)) = 0,028 kg de CO2

Total por 8 meses de uso: 331 kg CO2 / 6 años = 55,17 kg de CO2

- Impacto total del hardware (Uso + Producción por 8 meses): 59,38 kg CO2 + 55,17 kg CO2 = 114,55 kg CO2

2. Entorno de oficina o doméstico

Iluminación, calefacción, aire acondicionado, etc.

- Consumo de energía y emisiones de CO2: Supongamos que se utilizan 100 W en iluminación y dispositivos periféricos durante 8 h/día.

LUCAS MELGARES CARMONA 21

---

<!-- Página 27 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Cálculo del consumo durante 8 meses: KWh = (100 W x 8 h x 240 días) / 1000 = 192 kWh - Emisiones de CO2 (kg): 192 kWh x 0,231 kg CO2/kWh = 44,35 kg CO2

“Fig 9 Emisiones generadas en 2024”

https://www.nowtricity.com/country/spain/ 3. Servicios de red y nube

El uso de plataformas en la nube y servicios en línea representa un componente significativo del impacto ambiental del proyecto. Entre los servicios utilizados destacan:

- Google Drive: Almacenamiento de documentos y recursos. - Aplicaciones de inteligencia artificial mencionadas en el presupuesto. - Consumo estimado: Según informes de sostenibilidad, los servicios en la nube pueden consumir aproximadamente 7 kWh por 100 GB de datos almacenados al año. Estimando un uso de 200 GB, el consumo sería:

KWh = (7 kWh/100 GB) x 200 GB = 14 kWh

- Emisiones de CO2 (kg): 14 kWh x 0,231 kg CO2/kWh = 3,23 kg CO2

4. Componentes físicos utilizados

Durante el desarrollo del TFG, también se pueden utilizar componentes físicos que contribuyen al impacto ambiental, como:

LUCAS MELGARES CARMONA 22

---

<!-- Página 28 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Libreta para notas y apuntes a mano

5. Otros

Cualquier otro aspecto que pueda influir en el impacto ambiental y la responsabilidad social del proyecto se incluirá en esta categoría. Esto podría abarcar:

- Desplazamientos: Para reuniones o eventos relacionados con el proyecto. Por ejemplo, un trayecto de 20 km en coche (0,2 kg CO2/km) supondría: 20 km x 0,2 kg CO2/km = 4 kg CO2 - Uso de papel y otros materiales de oficina: Evaluando la sostenibilidad de su origen y el volumen consumido. - Gestión de residuos: Asegurando el correcto reciclaje de todo el material en la medida de lo posible y la minimización de desechos innecesarios.

El análisis del impacto ambiental y la responsabilidad social del proyecto ha permitido identificar cuáles son los principales puntos donde se generan emisiones de CO2 y otros efectos medioambientales. El uso del hardware y los servicios en la nube representan una parte significativa del impacto, destacando la importancia de optimizar el tiempo de uso y considerar opciones energéticamente eficientes. Asimismo, la producción de hardware tiene un peso considerable, por lo que alargar su vida útil puede reducir el impacto total, por eso también se ha incluido el cálculo del impacto del hardware durante cuatro años, que es el tiempo que de momento se tiene el dispositivo.

Adicionalmente, factores como el entorno de trabajo, los desplazamientos y el uso de materiales físicos también contribuyen al impacto global. La gestión sostenible de estos elementos, incluyendo el reciclaje y el uso de fuentes de energía renovables, puede ayudar a minimizar el impacto ambiental del proyecto. Como lo son el uso de bombillas leds, aprovechar la luz natural, utilizar las propias herramientas que ahorra de energía que te proporciona el hardware en su sistema operativo…

LUCAS MELGARES CARMONA 23

---

<!-- Página 29 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

En conclusión, el proyecto adopta un enfoque sostenible y responsable en el uso de IA, equilibrando el avance tecnológico con la reducción de su impacto ambiental y la promoción de un desarrollo ético centrado en el usuario.

LUCAS MELGARES CARMONA 24

---

<!-- Página 30 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## 4. Marco Teórico

- 4.1. Conceptos básicos de la Inteligencia Artificial (IA)

La inteligencia artificial es la capacidad de las máquinas y sistemas informáticos para realizar tareas que por lo general necesitan de la inteligencia humana, como el reconocimiento de patrones, la toma de decisiones, la solución de problemas y el aprendizaje. Mediante algoritmos y modelos matemáticos, la IA puede tratar grandes cantidades de datos, detectar relaciones y patrones y realizar decisiones basadas en dichos datos.

La IA se divide en varios subcampos, como el aprendizaje automático, que hace que los sistemas se vuelvan más efectivos con el tiempo al darles la opción de aprender mediante el análisis de datos, el procesamiento del lenguaje natural, que trata de la interacción entre humanos y máquina en un lenguaje natural hablado o escrito.

Hoy en día, la IA se está implementando en una abrumadora cantidad de aplicaciones, desde asistentes virtuales y sistemas de recomendación, hasta vehículos autónomos, y tiene un papel vital en la mejora y personalización de

la Experiencia del Usuario.

A continuación, se hace una explicación más exhaustiva en la que se detalla los conocimientos necesarios sobre la IA, desde su definición hasta la explicación de sus diferentes tipos y tecnologías similares emergentes hoy día.

4.1.1. Definición y evolución de la IA

Se empezará definiendo el concepto de IA o que es lo que entendemos por hoy día. En internet hay muchísimas definiciones que nos explican cómo podemos definir la IA, y para ello se han seleccionado tres definiciones principales de tres páginas de empresas o compañías muy importantes y reconocidas. La primera de todas es la que encontramos en la web “Plan de recuperación, Transformación y Resiliencia” del Gobierno de España, en la que se define que “La Comisión Europea la define como sistemas de software (y posiblemente también de hardware) diseñados por humanos que, ante un objetivo complejo, actúan en la dimensión física o digital. Percibiendo su entorno, a través

LUCAS MELGARES CARMONA 25

---

<!-- Página 31 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

de la adquisición e interpretación de datos estructurados o no estructurados. Razonando sobre el conocimiento, procesando la información derivada de estos datos y decidiendo las mejores acciones para lograr el objetivo dado. Los sistemas de IA pueden usar reglas simbólicas o aprender un modelo numérico. También pueden adaptar

su comportamiento al analizar cómo el medio ambiente se ve afectado por sus acciones previas.” (Qué es la Inteligencia Artificial, 2023) La segunda definición, la encontramos en la página web de Google Cloud, de la empresa de Google pionera en la inteligencia artificial, en la que se afirma que “La inteligencia artificial (IA) es un conjunto de tecnologías que permiten que las computadoras realicen una variedad de funciones avanzadas, incluida la capacidad de ver, comprender y traducir lenguaje hablado y escrito, analizar datos, hacer recomendaciones y mucho más.” (¿Qué es la inteligencia artificial o IA?, 2024) Por último, tal y como afirma la empresa IBM “La inteligencia artificial, o IA, es tecnología que permite que las computadoras simulen la inteligencia humana y las capacidades humanas de resolución de problemas.” (¿Qué es la Inteligencia Artificial (IA)?, 2024)

Una vez vistas estas tres definiciones, que nos dan estas tres grandes empresas, se ha podido concluir que todas ellas parecen coincidir en la idea de que la IA es una tecnología diseñada a semejanza de las capacidades humanas (o al menos para imitarlas), lo que permite que las máquinas puedan realizar tareas de alto nivel, como el procesamiento de datos y la toma de decisiones. Todas ellas destacan su capacidad para analizar y razonar la información de modo de ejecutar acciones o recomendaciones que, de otro modo, habrían sido derechos exclusivos de los humanos. Además, señalan su flexibilidad:

la IA se puede aplicar a contextos muy diferentes para adaptarse a diversas situaciones y objetivos. Estas definiciones conjuntas reflejan la esencia de la IA: flexible y autónoma, simulando la inteligencia y el comportamiento humanos para resolver problemas complejos.

LUCAS MELGARES CARMONA 26

---

<!-- Página 32 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Una vez hecha esta pequeña indagación y analizadas todas ellas, como definición más acertada se podría decir que la inteligencia artificial, es una subdisciplina de la informática cuyo trabajo se proyecta hacia el desarrollo de sistemas capaces de realizar actividades, hasta ahora exclusivas de los humanos, relacionadas con el razonamiento,

el aprendizaje, la percepción y la toma de decisiones. Algunos de los principales objetivos de la IA son la simulación de la inteligencia humana mediante algoritmos y modelos matemáticos, que permitan a las propias máquinas realizar operaciones muy complicadas sin intervención externa. Con el tiempo, la IA moderna encontró su ancla en la forma en que puede procesar enormes volúmenes de datos, identificar patrones, hacer predicciones y lograr resultados óptimos. Su implementación ha sido altamente revolucionaria en la medicina, los negocios, el transporte, la educación y el entretenimiento.

Desde sus inicios conceptuales y sus hitos clave hasta las aplicaciones actuales, el proceso de evolución ha sido gradual y multifacético. Los primeros intentos de dotar de inteligencia a las máquinas se remontan a mediados del siglo XX, ya que tal y como segura la página web (Inteligencia artificial : definición, historia, usos, peligros, 2024) la historia de la IA comenzó en el 1943 con la publicación del artículo “A Logical Calculus of Ideas Immanent in Nervous Activity” de Warren McCullough y Walter Pitts, en el que se presenta el primer modelo matemático par a la creación de una red neuronal. En 1950 se creó Snarc, el primer ordenador de red neuronal que, a su vez en ese mismo

2 año, Alan Turing publica el famoso “Test de Turing”que hoy día se sigue utilizando para valorar las IA. Otra figura importante, fue Arthur Samuel, que en 1952 creó un software capaz de aprender a jugar al ajedrez de forma autónoma, que a su vez fue él mismo, en el que, en el año 1959 apodó el término de “Machine Learning”. Hasta 1956, la "IA" se estableció oficialmente como tema predominante durante la conferencia de Dartmouth, donde investigadores como John McCarthy y Marvin Minsky promovieron la idea de que las máquinas debían ser

2 La prueba de Turing se utiliza como un estándar para medir la inteligencia artificial y la capacidad de una máquina para realizar tareas que requieren inteligencia humana, como el procesamiento de lenguaje natural, la toma de decisiones, el razonamiento y la creatividad.

LUCAS MELGARES CARMONA 27

---

<!-- Página 33 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

entrenadas para imitar ciertas habilidades de los seres humanos, como el razonamiento a través de la lógica y las matemáticas.

En esas décadas iniciales, la IA se limitaba a algoritmos explícitos basados en reglas o sistemas expertos que dependían completamente

de conocimientos programados previamente.

Se trataba de sistemas útiles para aplicaciones en medicina y demás, pero su capacidad de generalización era limitada, ya que no podían aprender de la experiencia ni adaptarse a situaciones que los programadores no habían previsto. La introducción del aprendizaje automático en la década de 1980 se convirtió así en un punto de inflexión. Este nuevo enfoque significó que las máquinas podían aprender de los datos y mejorar con el tiempo sin reglas de funcionamiento predefinidas. El aprendizaje profundo (redes neuronales artificiales) es otra rama del aprendizaje automático que ha supuesto nuevas revoluciones en este campo en la última década. Se trata de inspiraciones funcionales del cerebro humano, capaz de aprender y reconocer patrones complejos en grandes conjuntos de datos. La funcionalidad de las redes neuronales para aprender y reconocer patrones complejos a partir de grandes volúmenes de datos ha sido uno de los principales facilitadores de aplicaciones como el reconocimiento de imágenes, el procesamiento del lenguaje natural y la conducción autónoma.

(Evolución de la IA a través de la Historia, 2024), (Historia de la inteligencia artificial: del origen al futuro de la tecnología, 2024), (Inteligencia artificial : definición, historia, usos, peligros, 2024)

- 4.2. Experiencia de usuario

Es importante, tener claro el concepto de “Experiencia de Usuario” y

sobre todo a que hace referencia. Una vez se tenga clara su definición y conceptos generales, se definirá UX que es el concepto que junto la IA, se trata en este trabajo de final de grado.

LUCAS MELGARES CARMONA 28

---

<!-- Página 34 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

La experiencia de usuario se refiere al conjunto de percepciones y sensaciones del usuario en el uso de un determinado producto, servicio o sistema (UX, 2025). El objetivo de la experiencia de usuario es la satisfacción del usuario; debe hacer que la interacción sea intuitiva, efectiva y agradable ya que hay una mayor facilidad de uso y

accesibilidad. No se trata solo de la facilidad con la que se puede utilizar el sistema sino también de cómo el sistema responde para satisfacer las expectativas de los usuarios. Esto significa que el sistema tiene que reducir las barreras de interacción con el usuario para obtener lo que necesita lo más rápido posible y sin complicaciones. Ejemplos de buenas empresas de diseño UX que se utilizan mucho en nuestra vida diaria y de diferentes ámbitos son: plataformas online como Amazon o AirBnB, desde las que cualquier usuario no tendría ningún problema para operar y comprar algo de una manera muy sencilla. De esta manera, influiría en la UX de forma positiva en las percepciones sobre el producto y en la lealtad del cliente hacia la marca. Es importante remarcar, que en este caso se ha mencionado dos empresas, negocios o plataformas muy conocidos en concreto, ja que, en su momento, la disciplina del UX nació para hacer más atractivas y sencillas de usar cualquier tipo de página web, para así poder conseguir mayor tiempo de navegación y respectivamente, alcanzar más objetivos de venta. Pero la experiencia de usuario lo encontramos en todos lados que nos podamos imaginar, desde un producto en específico hasta una aplicación de móvil… Todos los productos que tenemos a nuestro alrededor han pasado antes por una fase de diseño en la que se ha tenido muy en cuenta la experiencia de usuario, buscando que el producto sea lo más fácil de usar posible.

Cuando hablamos de UX, hablamos del proceso de diseño que busca la intuición, accesibilidad y disfrute en la interacción con cualquier producto o servicio digital. Permite imaginar lo que el usuario puede

necesitar y esperar, y disminuir las situaciones que le resultan incómodas a la hora de utilizar una plataforma o aplicación para navegar fácilmente, acceder a la información y entender las funciones, es decir su función principal es anticiparse a cualquier problema que el usuario se pueda encontrar en una plataforma. Esto significaría que una tienda online bien optimizada permite a sus usuarios encontrar

LUCAS MELGARES CARMONA 29

---

<!-- Página 35 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

determinados productos con facilidad y simplemente comprarlos sin complicaciones innecesarias en los pasos de pago o navegación, como es el caso de sitios web de Amazon mencionado anteriormente, que incluso han hecho más fácil la compra con un solo clic. Este enfoque considera el diseño tanto desde la perspectiva técnica

como emocional, empezando por la usabilidad hasta la accesibilidad para personas con discapacidad. Son las pruebas continuas, por

3 ejemplo, las pruebas A/Bo las pruebas de resultados funcionales las que harán que el diseño sea atractivo, al igual que ocurre con plataformas muy exitosas como Airbnb, creando una experiencia desde la entrada hasta la reserva de un alojamiento que se ajuste a las expectativas de sus usuarios.

(La experiencia de usuario (UX): qué es, disciplinas y ejemplos, 2024),

(HubSpot, s.f.), (¿Qué es UX o User Experience? Ejemplos para valorar la experiencia del usuario, 2024)

4.2.1. Tipos de IA más utilizados hoy día en la UX

Para saber y explicar que tipos de IA son los más utilizados actualmente en la UX, es fundamental entender cómo cada uno de estos tipos, contribuye a mejorar la interacción entre el usuario y la interfaz. Los tipos más comunes incluyen:

- Una IA de personalización que emplea técnicas de aprendizaje automático para adaptar la interacción del usuario alineándose con las preferencias y acciones elegidas. En las plataformas de comercio electrónico, siguiendo con el ejemplo de Amazon, la IA propone artículos de acuerdo con patrones de compra, facilitando una experiencia de navegación más intuitiva y personalizada para cada usuario.

- Mecanismos de sugerencias personalizados: estos marcos analizan los datos del usuario para formular orientación individualizada y personalizada, presente en servicios de

3 Las pruebas A/B (también denominadas pruebas de división o pruebas de cubos) comparan el rendimiento de dos versiones de contenido para ver cuál atrae más a los visitantes/la audiencia.

LUCAS MELGARES CARMONA 30

---

<!-- Página 36 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

transmisión como Netflix y Spotify. Al examinar tendencias y su actividad, estos sistemas aumentan el placer del usuario final al simplificar el acceso a materiales que cautivan su interés.

- Chatbots y ayudas virtuales: utilizan tecnología de análisis lingüístico, estos ayudantes automatizados facilitan la comunicación ininterrumpida, respondiendo consultas y resolviendo problemas sin participación humana. Esto mejora enormemente la interacción y la asistencia al cliente, proporcionando retroalimentación instantánea y personalizada a la situación del usuario.

- Reconocimiento de voz e imagen: esta función de IA ayuda a las personas con discapacidades a acceder a la tecnología permitiéndoles hablar con aplicaciones o describiéndoles imágenes. Estos instrumentos son esenciales para garantizar una interfaz fácil de usar y sin barreras.

- El análisis predictivo emplea comportamientos pasados del usuario y datos históricos para pronosticar preferencias futuras, lo que resulta invaluable para el comercio electrónico y la publicidad personalizada al anticipar el interés del usuario en productos o servicios específicos.

Estas variedades de inteligencia artificial han transformado la UX al

brindar una participación más personalizada, accesible y que ahorra tiempo, lo que permite a las personas sentirse contentas y complacidas en sus actividades y navegación digital.

(Tipos de IA más utilizados en la experiencia de usuario, 2024), (Aplicaciones de la inteligencia artificial para mejorar la experiencia de usuario, 2024), (Tipos de Inteligencia Artificial —ejemplos en atención al cliente, 2024), (HubSpot, s.f.)

4.2.2. Tecnologías emergentes similares en el campo de la IA.

LUCAS MELGARES CARMONA 31

---

<!-- Página 37 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Entre las tecnologías de vanguardia de la inteligencia artificial actual y que sirguen surgiendo cada día, varias tecnologías emergentes están dejando su huella. Si bien no son IA en sí, tienen un impacto tremendo en el desarrollo y las aplicaciones de la IA. Importante recalcar que son tecnologías emergentes que trabajan con IA o que ayudan al propio

desarrollo de la inteligencia artificial. Algunas de las más destacadas son las siguientes:

- Computación cuántica: esta tecnología promete cambiar el campo de juego en el procesamiento de datos basado en los principios de la mecánica cuántica. Aunque todavía se encuentra en sus inicios, ya se ha propuesto su uso para la criptografía poscuántica y las redes cuánticas, que transformarán la seguridad informática y la transferencia de datos.

- Internet de las cosas (IoT): se logran más extensiones hacia hogares inteligentes, ciudades conectadas y automatización industrial al integrarlas con sistemas de IA. IoT permite recopilar datos en tiempo real para optimizar procesos mediante IA.

- PLN o procesamiento del lenguaje natural (Natural Language Processing): si bien eso también es parte del dominio de la IA, evoluciona cada vez más con derivaciones de modelos más avanzados como ChatGPT, Gemini, Copilot, Claude y otros para redefinir literalmente cómo interactuarán los humanos y las máquinas. Algunos usos actuales incluyen servicio al cliente, traducción automática e incluso en algunos casos análisis de sentimientos, se definen como “IA Assistants”.

- Blockchain e IA: con la fusión de blockchain con IA, el rastreo se ha vuelto más sencillo, transparente y seguro en las industrias de la cadena de suministro, los servicios financieros y la atención médica. Este dúo tecnológico garantiza un análisis de datos más seguro y confiable.

LUCAS MELGARES CARMONA 32

---

<!-- Página 38 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Los sistemas autónomos incluyen drones, vehículos autónomos y robots, que están mejorando gracias a la integración de sensores progresivos de IA con algoritmos de control en vivo. Las implementaciones adicionales en logística, vigilancia y exploración son cada vez mayores. BCI: un grupo de tecnologías emergentes,

entre ellas Neuralink, conectan el cerebro humano directamente con dispositivos digitales. Es un amplio campo de oportunidades, desde la rehabilitación médica hasta el control de dispositivos.

Estas tecnologías también respaldan el desarrollo adicional de la IA y abren un horizonte completamente diferente para nuevas aplicaciones en la vida diaria, la industria y la investigación.

(Tipos de IA más utilizados en la experiencia de usuario, 2024),

(Aplicaciones de la inteligencia artificial para mejorar la experiencia de usuario, 2024), (Tipos de Inteligencia Artificial —ejemplos en atención al cliente, 2024), (HubSpot, s.f.) (Tecnologías emergentes similares IA, 2024) (Cómo afectarán al mundo las 10 tecnologías emergentes más importantes de 2024, 2024), (Las 10 Tecnologías Emergentes, 2024), (Las 10 tendencias tecnológicas estratégicas para 2024 según Gartner, 2024), (Principales tendencias tecnológicas para 2024: IA, computación cuántica y sostenibilidad, 2024), (19 Tecnologías emergentes más importantes del 2025 ¡Top ejemplos!, 2024)

- 4.3. Funcionamiento de la IA en la experiencia de usuario (UX)

La IA también está trastornando fundamentalmente la UX, mientras que el aprendizaje automático, los datos y el análisis y la automatización son modos superiores en los cuales se hacen de manera explotadora en la arquitectura de interfaz y la interacción. Su comportamiento principal en este campo implica examinar la actividad del usuario, personalizar las interacciones y ajustar reiteradas de manera innata las interfaces de usuario conforme a los requerimientos particulares.

El primer ejemplo es el análisis predictivo y la formación única. La IA beneficia los protocolos de adiestramiento automático para inspeccionar grandes bases de detalles de información del usuario, y de sus orientaciones. Se puede

LUCAS MELGARES CARMONA 33

---

<!-- Página 39 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

percibir los requerimientos y la alteración subsiguiente en los datos y hechos. Las OTT (Over The Top), tales como Netflix y Amazon, adaptan sus proposiciones y entorno a sugerencias instantáneamente en respuesta a la actividad en línea y los registros de compras de los espectadores. Modifican su interfaz y contenido a raíz de las necesidades de los usuarios.

El segundo ejemplo, es la automatización y eficiencia. La IA automatiza tareas monótonas, como responder consultas utilizando chatbots o asistentes virtuales (definidos anteriormente) como Alexa de Amazon o Siri de Apple. Estos sistemas no sólo mejoran la rapidez del tratamiento, sino que también recopilan estadísticas para proporcionar remedios más precisos y adecuados a lo largo del tiempo.

El tercer ejemplo es la interacción natural e intuitiva. "Técnicas innovadoras como el análisis lingüístico (LA) y la comprensión verbal facilitan intercambios fluidos basados en el diálogo". Esto simplifica los detalles complejos y mejora la comprensión al fomentar la interacción entre las personas y los sistemas automatizados. Un ejemplo que seguro que muchas personas utilizan hoy día es, por ejemplo, preguntar a nuestro asistente ya sea Google Assistant, Alexa, Siri... "Que tiempo hará hoy?" y mediante estos sistemas se procesa el lenguaje, se contextualiza y se responde de manera adecuada.

Como cuarto ejemplo, encontramos la optimización del diseño UX. La IA evalúa constantemente la interacción del usuario con una plataforma, detectando problemas de usabilidad y proponiendo mejoras. Las evaluaciones algorítmicas pueden identificar regiones de descontento de los usuarios y sugerir modificaciones instantáneamente.

En quinto lugar, tenemos la accesibilidad digital. Las aplicaciones impulsadas por IA mejoran la accesibilidad digital, incluido el software de ayuda visual para personas ciegas o los subtítulos generados por máquinas para material de vídeo. Esto amplía el alcance y garantiza que cada usuario pueda participar de una experiencia ejemplar.

Por último, en sexto lugar tenemos las pruebas y evolución continuas. La IA le permite realizar pruebas y análisis comparativos de forma rápida y eficaz,

LUCAS MELGARES CARMONA 34

---

<!-- Página 40 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

determinando qué diseños o atributos producen resultados superiores. Esta capacidad repetitiva garantiza que las interfaces se adapten de acuerdo con las cambiantes demandas de los usuarios.

La IA en UX tiene como objetivo crear experiencias personalizadas, fáciles de usar y accesibles, mejorando la interacción y la satisfacción del cliente. A medida que avancen los avances, la influencia de la IA en este ámbito seguirá expandiéndose, facilitando un encuentro digital más mejorado y flexible.

(Cómo funciona la IA en la experiencia de usuario UX, 2024), (El UX (Experiencia de Usuario) en los Tiempos de la Inteligencia Artificial, 2024), (La revolución del diseño: cómo la IA transforma la experiencia de usuario, 2024), (IA y UX: Cómo la IA está mejorando la experiencia del usuario, 2024), (El uso de la inteligencia artificial en UX/UI, 2024), (Uso de la inteligencia artificial en la personalización de la experiencia del usuario en plataformas digitales, 2025), (Análisis de la interacción entre la inteligencia artificial y la experiencia del usuario: Aplicación a un caso práctico, 2025)

4.3.1. Funcionamiento general de los algoritmos de IA

Un algoritmo de inteligencia artificial es un sistema que opera con el conocimiento sobre el procesamiento de datos, el aprendizaje de patrones y la realización de predicciones o decisiones basadas en ese análisis, generalizando este tipo de conocimiento a nuevas situaciones nunca antes vistas. El proceso de cómo funciona típicamente un sistema de IA se puede dividir en varias fases:

- Recopilación y preprocesamiento de datos: la inteligencia artificial requiere enormes cantidades de datos estructurados y no estructurados. Los datos recopilados se limpian y normalizan para que el modelo pueda procesarlos con precisión.

- Construcción del modelo: en esta etapa, los algoritmos aprenden a encontrar el patrón dentro de los datos o entre dichas variables en un conjunto de datos. En función de si un modelo es supervisado, no supervisado o de aprendizaje

LUCAS MELGARES CARMONA 35

---

<!-- Página 41 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

por refuerzo, actualiza sus parámetros internos para obtener un error mínimo y resultados óptimos.

- Validación y evaluación: un modelo que no se ha probado previamente se valida con datos que nunca se han visto antes, para verificar su precisión y solidez mientras se generalizan los datos de entrenamiento.

- Implementación y uso: el modelo final obtenido del proceso de validación se aplicará a sistemas reales, como UX, asistentes virtuales o motores de recomendación. Esto también incluye los errores monitoreados a lo largo del tiempo, la adaptación a nuevas condiciones o datos que puedan aparecer, y más.

- Mejora continua: la mayoría de los modelos de IA son iterativos. Debido a que pueden aprender de la información continuamente actualizada que se les puede suministrar, se pueden mejorar continuamente para mantener su efectividad a lo largo del tiempo.

En la experiencia de usuario de un producto, los algoritmos de IA están diseñados para personalizar las experiencias de los usuarios, analizar el comportamiento de los clientes y automatizar otros mecanismos, como la recomendación de productos o el diseño de interfaces dinámicas. Por ejemplo, las redes neuronales profundas permiten que los algoritmos de IA detecten patrones complicados en los datos visuales, que son útiles para ajustar las interfaces gráficas a las preferencias de los usuarios. Además, con el aprendizaje supervisado, ya se puede predecir el comportamiento de los usuarios en los sitios web, mientras que el aprendizaje no supervisado encuentra tendencias que pueden ser de interés para un usuario.

Habiendo visto y entendido el funcionamiento general de los algoritmos de IA, vamos a ver qué pasos, o como en el ejemplo anterior, fases que sigue la IA para comprender cómo estas tecnologías procesan y

LUCAS MELGARES CARMONA 36

---

<!-- Página 42 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

optimizan las interacciones de los usuarios con los productos digitales. Los algoritmos de IA juegan un papel clave en la personalización y las ganancias en eficiencia, así que pasan por algunas etapas clave específicas para la UX.

- Recopilación y procesamiento de datos: la inteligencia artificial comienza a trabajar recopilando grandes conjuntos de datos, ya sea en forma de clics, tiempo de pantalla, historial de navegación o algo relacionado con las preferencias de un usuario. Los algoritmos involucrados en esto, a través de técnicas de aprendizaje automático, procesan dicha información para identificar patrones relevantes.

- Análisis predictivo: la IA se puede utilizar para predecir lo que las personas van a hacer a través del análisis predictivo. Por ejemplo, un modelo podría predecir qué productos podría querer comprar un usuario en función de su historial de compras, o sugerir el contenido más relevante, teniendo en cuenta el comportamiento anterior.

- Automatización de procesos creativos: por ejemplo, creación automática de prototipos de interfaz por parte de sistemas de diseño de IA a partir de preferencias de diseño anteriores y comportamientos de los usuarios. Optimiza el trabajo realizado por los diseñadores y proporciona una experiencia personal a los usuarios a cambio.

- Adaptabilidad en tiempo real: como los algoritmos de IA se alimentan continuamente con procesamiento de datos en tiempo real, las interfaces se pueden hacer más interactivas para realizar cambios oportunos según las influencias en el comportamiento del usuario. Como, por ejemplo, los colores, el diseño o incluso los textos de las aplicaciones móviles se pueden cambiar automáticamente con los cambios de contexto.

LUCAS MELGARES CARMONA 37

---

<!-- Página 43 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Interacción multimodal: la IA también integrará modos como la detección de voz, texto y gestos, lo que hará que las interfaces sean aún más naturales. Los usuarios estarán en mejores condiciones de decidir en cualquier momento cómo interactuar con los sistemas: lo que mejor se adapte a sus

necesidades o preferencias en cada momento.

Estas características contribuyen a la fluidez y la interacción, pero lo más importante es que generan una ventaja en el desarrollo de interfaces intuitivas.

(Cómo funcionan los algoritmos de inteligencia artificial explicación, 2024), (Qué Son y Cómo Funcionan los Algoritmos de Inteligencia Artificial, 2024), (Inteligencia Artificial: ¿Qué es y Cómo Funciona?, 2024), (Algoritmos de inteligencia artificial: qué son, qué tipos hay y cómo funcionan, 2024), (¿Cuáles son los algoritmos de inteligencia artificial?, 2024), (Cómo los algoritmos de IA funcionan en UX personalización análisis comportamiento diseño interfaces, 2024), (¿Cómo usar la iteligencia artificial en UX/UI?, 2024), (La IA en el Diseño de Experiencia de Usuario (UX): Mejorando la Interfaz del Usuario, 2024), (IA UX/UI: La revolución de la inteligencia artificial en el diseño de Apps, 2024)

4.3.2. Impacto de la IA en el diseño de experiencia de usuario

La Inteligencia Artificial ha crecido hasta convertirse en un factor transformador en el diseño UX, el verdadero punto de inflexión en el que los diseñadores abordarían la creación de interfaces y productos digitales. En este sentido, la IA proporciona la capacidad de hacer que las experiencias de usuario sean más personalizadas y optimizadas a través del análisis, la automatización de procesos y la capacidad de aprendizaje continuo. Es fundamental situar al lector en el contexto de este impacto al comienzo de este TFG, tal y como se ha hecho, explorando cuáles son las aplicaciones actuales de la IA en UX y abriendo la puerta al análisis de sus posibilidades en el futuro.

LUCAS MELGARES CARMONA 38

---

<!-- Página 44 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

La IA permitirá recopilar y procesar grandes volúmenes de datos sobre el comportamiento y las preferencias y necesidades de los usuarios, lo que permite un nivel de personalización que hasta ahora no se ha alcanzado por otros medios. Por ejemplo, y, por último, pero no menos importante, algoritmos sofisticados como los que utilizan plataformas

en línea como Netflix o Amazon actualizan el contenido y las recomendaciones de productos en función de los patrones de cada usuario individual, lo que aumenta aún más la satisfacción y la lealtad del cliente. Como tal, el enfoque predictivo anticiparía las necesidades de los usuarios al eliminar la fricción en su recorrido mediante sugerencias de soluciones más pertinentes y específicas para esos usuarios en tiempo real.

Por otro lado, el trabajo de los diseñadores se ha visto muy revolucionado por herramientas que automatizan procesos complejos

4 de forma repetida, como Adobe Sensei. Desde la generación de prototipos interactivos hasta el cambio dinámico de colores o formas, estas tecnologías ahorran un tiempo precioso a los diseñadores para crear e innovar. Igualmente, importante es que la IA respalda la optimización continua mediante las pruebas A/B automatizadas en las que identifica las versiones de las interfaces que mejor se adaptan a las expectativas de los usuarios.

Pero estos cambios introducidos por la IA no están exentos de desafíos para la experiencia de usuario y una serie de dilemas éticos. De ellos,

uno de los más importantes es cómo garantizar que las decisiones automatizadas respeten los valores humanos y reflejen las expectativas de los usuarios. Por ejemplo, si bien es realmente interesante que la IA pueda predecir patrones de comportamiento, un malentendido o una comprensión sesgada de los datos podría conducir a experiencias deshumanizadas o discriminatorias. Por lo tanto, debe utilizarse de tal manera que el uso de la IA se combine con la supervisión y el juicio humanos, con la garantía de incluir interfaces diversificadas para que las interfaces satisfagan a todos los usuarios.

4 Adobe Sensei es una herramienta basada en inteligencia artificial que potencia las aplicaciones de Adobe, proporcionando funciones avanzadas que mejoran la eficiencia y la experiencia del diseño.

LUCAS MELGARES CARMONA 39

---

<!-- Página 45 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Más allá de las ventajas mencionadas anteriormente, el desarrollo de la IA también está restableciendo las expectativas de los usuarios. El desarrollo continuo de interfaces conversacionales cada vez más sofisticadas, incluidos tanto chatbots como asistentes virtuales, continúa elevando el estándar de interacciones naturales y fluidas; servicio al cliente eficiente y personalizado.

De manera similar, un diseño basado en IA en interfaces dinámicas hace posible que dos usuarios distintos de la misma aplicación tengan interacciones completamente diferentes con ella, adaptadas a sus diferentes hábitos y gustos.

Debido a este hecho, la implementación de IA en UX también plantea preguntas sobre el futuro del diseño en primer lugar. Lo único que se esperaría de los profesionales es una formación constante, ya que las tecnologías se desarrollan muy rápido y las herramientas y tendencias emergentes son difíciles de seguir. No es solo un desafío técnico, sino que requiere cambiar la mentalidad ante esta tecnología de tendencia, dando la bienvenida a la IA como un aliado y no temiendo que sea un reemplazo.

Este TFG profundizará en los usos actuales de la IA en UX y explorará su impacto práctico mediante una serie de experimentos y estudios de casos. En esta parte experimental, se busca una evaluación de cómo se pueden integrar estas tecnologías en el proceso de diseño y cuáles son sus limitaciones. Una vez finalizada esta fase práctica se presentarán unas conclusiones que nos permitirán profundizar en el impacto real de la IA en el diseño UX, y cuál puede ser su potencial futuro.

(Impacto de la inteligencia artificial en el diseño de experiencia de usuario UX 2024, 2024), (La revolución del diseño: cómo la IA

transforma la experiencia de usuario, s.f.), (El UX (Experiencia de Usuario) en los Tiempos de la Inteligencia Artificial, 2024), (Inteligencia Artificial en el Diseño y UX: Innovaciones para 2024, 2024), (Impacto

LUCAS MELGARES CARMONA 40

---

<!-- Página 46 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

de la inteligencia artificial en UX UI en la transformación digital en España, 2024), (El Impacto de la IA en el Diseño UX este 2024, 2024)

4.3.3. Diferencias entre UX tradicional y UX impulsado por IA

El diseño UX tradicional es muy diferente del diseño de IA en cuanto a enfoque, herramientas y resultados. Reconocer estos contrastes será muy importante para entender muchas formas en que la IA está cambiando la forma en que se diseñan y optimizan las experiencias digitales.

El diseño UX tradicional se basa en gran medida en datos cualitativos y cuantitativos, generalmente recopilados manualmente. Normalmente se realiza a través de entrevistas personales, cuestionarios y pruebas de usuario para sacar conclusiones sobre cuáles son las necesidades y preferencias de los usuarios. Si bien esto es efectivo, puede ser un proceso terriblemente lento; debido a que el análisis humano debe realizarse con grandes volúmenes de datos para procesar, puede ser muy propenso a limitaciones o incluso en algunos casos a errores. El diseño UX tradicional se basa en la intuición, la creatividad y la experiencia de los diseñadores, por lo que la UX tradicional, es menos automatizada y más artesanal. Por un lado, la UX impulsada por IA emplea algoritmos elaborados de recopilación y procesamiento de datos a gran escala que podrían permitir una mirada al interior del comportamiento del usuario más profunda y precisa que nunca. Equipadas con el poder de la IA, las herramientas podrán predecir patrones de interacción, permitir la personalización de contenido y dominar tareas rutinarias como la creación de prototipos o el análisis de pruebas de usuarios. Además, la IA permitirá obtener información (hasta ahora oculta en los datos) que permitirá a los diseñadores tomar mejores decisiones y crear experiencias mejor adaptadas a las necesidades de cada usuario.

Por ejemplo, en un diseño de UX impulsado por IA, a diferencia de un diseño que usa la UX tradicional los perfiles de usuario se creaban mediante entrevistas y suposiciones, esto se crearía automáticamente

LUCAS MELGARES CARMONA 41

---

<!-- Página 47 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

a partir de datos internos en vivo, como la interacción en las redes sociales, las visitas a la página y los comportamientos en general. En ese sentido, se podrían crear personajes mucho más apropiados y precisos, y serían dinámicos.

Pero, además, todas esas UX impulsadas por IA aportan dimensiones completamente nuevas, como la personalización en tiempo real y la automatización de los flujos de trabajo. Si bien las herramientas impulsadas por IA solo pueden recomendar cambios en las interfaces para mejorar las acciones del usuario, ajustan automáticamente los elementos visuales y funcionales creando una experiencia óptima. La eficiencia se mejora aún más gracias a la intuición y el nivel de participación generados para la experiencia del usuario final.

Permítanme enfatizar, sin embargo, que la IA no reemplaza las capacidades humanas. Está en el dominio del diseñador humano ver e interpretar emociones y contextos complejos, áreas en las que la IA no puede ingresar. La IA propone sólo una complementariedad capaz de mejorar las capacidades humanas al reducir varias de las limitaciones inherentes a los enfoques tradicionales. Una transformación está en pleno apogeo, desde el diseño UX tradicional al diseño UX impulsado por IA, marcando el comienzo de una era de diseño ágil, eficiente y personalizado. Sea como sea, con todo, se requiere una estrecha colaboración entre las personas con la tecnología para mantener las necesidades humanas y las expectativas de los resultados finales. Además, será más atractivo notar cómo estas transformaciones dentro de las tecnologías de IA han provocado prácticas de diseño en los últimos tiempos.

(Diferencias entre UX tradicional y UX impulsado por IA, 2024), (Cómo el Diseño UX Está Evolucionando con la IA y Aumenta las Conversiones, 2024), (El UX (Experiencia de Usuario) en los Tiempos de la Inteligencia Artificial, 2024), (La revolución del diseño: cómo la IA transforma la experiencia de usuario, s.f.), (Diseño UX y AI: una relación de confianza y reciprocidad, 2024), (7 ventajas que nos puede aportar la IA a los diseñadores UI/UX Sí, existen, 2024)

LUCAS MELGARES CARMONA 42

---

<!-- Página 48 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- 4.4. Ética y retos en la implementación de la IA a UX

La implementación de la inteligencia artificial enfrenta muchos desafíos éticos y técnicos. Ofrecer herramientas poderosas para mejorar y personalizar las experiencias digitales, por un lado, implica una responsabilidad significativa en materia de privacidad, equidad y transparencia.

Estas consideraciones no solo tendrán un impacto en la percepción del usuario, sino también en la confianza general en los sistemas y las empresas que los utilizan. Por eso, la consideración de las consecuencias éticas en el diseño y desarrollo de sistemas de IA se vuelve muy importante.

Entre estos, uno de los problemas éticos más importantes que se deben abordar es la gestión del sesgo algorítmico, que, si no se regula, puede conducir a experiencias injustas, erróneas y discriminatorias o perpetuarlas.

Ciertamente, existe una tendencia a que los algoritmos de IA reflejan sesgos en los datos con los que fueron entrenados y, a veces, fomentan estereotipos o resultados desiguales basados en garantías. Por ejemplo, las aplicaciones basadas en IA que personalizan el contenido tienden a favorecer a un tipo de usuario sobre otro en perjuicio de la inclusión en las experiencias digitales. Es solo entonces cuando se necesitan metodologías de desarrollo ético como auditorías de sesgo y controles de calidad en los datos de entrenamiento para reducir el problema.

Otro aspecto importante es el tratamiento de los datos personales. La IA en la experiencia del usuario depende en gran medida de los datos recopilados de los usuarios, lo que conlleva riesgos de privacidad y seguridad.

Un posible ejemplo es que las interfaces que requieren personalización pueden solicitar información sensible, como el patrón de navegación o las preferencias personales. Si esta información no se trata adecuadamente, puede hacer que los usuarios se sientan vulnerables y, por lo tanto, reducir su confianza en el sistema. Las empresas deben cumplir con regulaciones como el “Reglamento General de Protección de Datos”, asegurando al mismo tiempo que los usuarios tengan control sobre el uso de los datos recopilados de ellos.

LUCAS MELGARES CARMONA 43

---

<!-- Página 49 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

La cuestión de dónde trazar el límite en el uso de la IA para influir en el comportamiento del usuario plantea un dilema ético en la personalización. La interfaz personalizada está destinada a aumentar la conversión y la satisfacción, pero también manipula las decisiones y plantea preguntas sobre la autonomía del usuario.

Estos dilemas surgen en el caso de las recomendaciones de productos, donde los algoritmos pueden priorizar los intereses comerciales sobre las necesidades reales del usuario. Finalmente, la operacionalización de estos desafíos requiere no solo estrategias técnicas, sino también una gobernanza ética. Se trata de establecer los principios para crear sistemas de IA: explicabilidad de las decisiones algorítmicas, imparcialidad de los resultados y prevención de daños.

Aun así, es necesario fomentar un diálogo continuo entre empresas, reguladores y usuarios para definir con claridad estándares que fomenten un uso responsable de la IA en UX. Estos últimos desafíos se desarrollarán más adelante, explicando casos prácticos y soluciones emergentes que garanticen el uso ético y justo de la IA en UX y reforzando las mismas conclusiones que se presentarán al final de este trabajo.

(Ética y retos en la implementación de la IA en UX, 2024), (Ética en IA: Los

Desafíos Morales de la Inteligencia Artificial, 2024), (La Ética en la Inteligencia Artificial: Consideraciones y Debates Actuales, 2024), (¿Qué es la ética de la IA?, 2024), (Ética en la Inteligencia Artificial Empresarial, 2024), (De los sesgos

a la manipulación, la cuestión ética es ineludible en el desarrollo de la inteligencia artificial, 2025),

## 5. Estado del Arte

- 5.1. Estudio de casos y aplicaciones actuales

En el siguiente apartado se explica a través de casos prácticos con ejemplos reales, cómo se está incorporando la IA a la UX. A continuación, se describirán las aplicaciones más concretas de cómo los algoritmos y la IA en general están cambiando las interfaces digitales para ofrecer, de forma más personal, cómo ser más eficientes y ricos en innovación.

LUCAS MELGARES CARMONA 44

---

<!-- Página 50 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Entre los ejemplos excelentes se encuentran el comercio electrónico, que hace uso de la misma en el desarrollo de sistemas de sugerencias y potentes chatbots, mejorando las experiencias de los clientes; también se abordará cómo las plataformas de streaming han utilizado de forma ideal la IA para presentar contenidos al usuario en función de las preferencias de este. Y, por último, las herramientas de diseño que utilizan esta potente tecnología para automatizar todo tipo de procesos creativos ayudarán a acelerar la creación de interfaces altamente intuitivas.

En este apartado se expondrán tanto los logros actuales como, con el apoyo de un análisis crítico, las limitaciones y los retos: desde los sesgos algorítmicos hasta las preocupaciones éticas sobre el tratamiento de los datos. El lector, al final de esta revisión, entenderá cómo la IA está redefiniendo la UX y cuáles podrían ser los desarrollos futuros que ya están marcando sus tendencias. Cada ejemplo en particular se desarrolla más a fondo, con elementos posteriores que brindan datos precisos, un diagrama que explica cosas muy simples y pone cada comparación una al lado de la otra mientras sienta las bases para su comprensión básica del impacto que hoy en día la IA tiene en la experiencia del cliente final.

5.1.1. IA en la industria de los videojuegos

La inteligencia artificial en los videojuegos significa el desarrollo e implementación de algoritmos y sistemas que otorgan la capacidad a los NPC y otros objetos del juego para actuar de manera inteligente,

similar a los seres humanos. El objetivo principal es diseñar experiencias de juego más realistas, dinámicas y desafiantes en las que los personajes no jugadores reaccionen al jugador de manera realista, se adapten dinámicamente a las circunstancias e incluso tomen decisiones en tiempo real. Tradicionalmente, la IA dentro de los videojuegos ha estado allí para controlar los movimientos de enemigos, aliados y otros personajes con respecto a la estrategia y la respuesta dentro de un entorno virtual. Técnicas como el uso de máquinas de estados finitos, árboles de decisión y algoritmos de búsqueda de rutas son algunos de los medios por los que los NPC pueden moverse a

LUCAS MELGARES CARMONA 45

---

<!-- Página 51 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

través de un juego y responder a los sucesos que ocurren a su alrededor.

La IA generativa se ha convertido recientemente en una herramienta revolucionaria para el desarrollo de videojuegos. Esta área de la IA se

ocupa de la creación de contenido nuevo a partir de datos previamente existentes, como niveles, personajes, historias y diálogos.

La generación procedimental es una de las técnicas de IA generativa que permite la creación automática de mundos y escenarios, permitiendo así experiencias diferentes en cada juego y reduciendo tiempos y recursos durante el proceso de desarrollo. Como se acaba de mencionar, en la actualidad, se está abriendo paso y cada vez se está dando a conocer más la “inteligencia artificial generativa”. Este tipo de IA hace la idea que se ha explicado anteriormente, es decir, utiliza técnicas avanzadas como las redes neuronales para generar contenido nuevo y único. Esto lo hace mediante la idea de poder tener un juego que crea sus propias misiones, historias y personajes dinámicamente en respuesta a las acciones del jugador, lo que conlleva un nivel de personalización e inmersión increíble, proporcionando una experiencia de juego en constante evolución y adaptada a cada jugador, a parte de que ayuda a reducir el tiempo y los recursos necesarios para crear contenido nuevo.

Algunos ejemplos so, “Nvidia Instant Nerf”, que usa la IA para generar de forma automática modelos 3D de alta calidad y fidelidad, o como “Nvidia Ace”, que también usa la IA para generar personajes NPC, más realistas y conseguidos, con una capacidad de respuesta mucho más natural.

A continuación, se presentan algunos de los casos más relevantes en la realización de aplicaciones de IA dentro de la industria de los videojuegos, junto con los resultados obtenidos y las conclusiones derivadas de dichas experiencias.

1. La Tierra Media: Sombras de Mordor y el Sistema Némesis

LUCAS MELGARES CARMONA 46

---

<!-- Página 52 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

La Tierra Media: Sombras de Mordor, de Monolith Productions, introdujo por primera vez en 2014 el Sistema Némesis, una aplicación avanzada de IA mediante la cual los enemigos podían recordar interacciones previas con jugadores y cambiar su estrategia en consecuencia. Se trata de un sistema de generación dinámica de

enemigos únicos en jerarquías con características, fortalezas y debilidades, que evolucionan en función de la interacción con el jugador. Algunos ejemplos son la capacidad de un enemigo que sobrevive a una batalla con el jugador, de recordar dicho encuentro, comentarlo en futuros encuentros y ascender en la jerarquía de enemigos para volverse más poderoso. Esto proporciona juegos personalizados que son dinámicos y en los que las acciones del jugador tienen un efecto inmediato en los eventos que ocurren dentro del mundo virtual. Eso fue lo que hizo que el Sistema Némesis fuera un éxito, ya que cada jugador tenía su experiencia, aumentando así la rejugabilidad y la inmersión, aunque es cierto que, en su uso, se notaron algunas limitaciones, como ciertos comportamientos repetidos para los enemigos y una falta de profundidad en la interacción a largo plazo. Esto ha establecido el estándar en la industria en cuanto a cómo la IA puede enriquecer la narrativa emergente en los videojuegos.

“Fig 10 Portada de La Tierra Media: Sombras de Mordor y el Sistema Némesis”

https://generacionxbox.com/la-tierra-media-sombras-de-mordor-nos-muestra-el-sistema- nemesis/

2. No Man's Sky y la generación procedimental del universo. No Man's Sky es un videojuego desarrollado y publicado de forma independiente lanzado en 2016 que resulta ser probablemente uno de

LUCAS MELGARES CARMONA 47

---

<!-- Página 53 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

los ejemplos más famosos de aplicación de todo este mecanismo y patrón de creación procedimental impulsada por IA de un universo virtualmente infinito, desde planetas y ecosistemas, flora y fauna, cada uno a partir de un algoritmo automático. Se dice que los usuarios están explorando al menos más de 18 billones de planetas singulares.

Esto permite que cada jugador tenga su forma de descubrimiento en la exploración, creando así una sensación de gran aventura y descubrimiento. Aunque en su momento de lanzamiento, el juego había atraído críticas por contener contenidos sin sentido y generar una experiencia que era altamente repetitiva al revelar sus propias limitaciones de usar la generación procedimental de contenidos sin ninguna función curativa propia, con el tiempo, las actualizaciones equilibraron la generación automática con contenido diseñado manualmente, y tanto la profundidad como la calidad comenzaron a mejorar en las partidas. Este caso pone de relieve cómo la IA generativa debe combinarse con la intervención humana para crear mundos de juego ricos y satisfactorios.

“Fig 11 Portada No Man's Sky y la generación procedimental del universo”

https://store.steampowered.com/app/275850/No_Mans_Sky/?l=spanish&cc=fr

3. Alien: Isolation y la IA del Xenomorfo En Alien: Isolation, desarrollado por Creative Assembly y publicado en 2014, la IA del antagonista principal debía ser una experiencia insoportablemente intensa en el género survival horror. El comportamiento del Xenomorfo se basa en un sistema de IA que combina varios patrones predefinidos con aprendizaje adaptativo; por ello, reacciona de forma impredecible a las acciones del jugador. El

LUCAS MELGARES CARMONA 48

---

<!-- Página 54 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Xenomorfo no sigue caminos fijos, sino que patrulla dinámicamente mientras escucha ruidos y observa movimientos. Incluso aprende de las tácticas del jugador, como utilizar siempre los escondites o las distracciones. Crea una atmósfera de tensión constante porque en ningún momento se puede estar seguro de lo que el enemigo podría

hacer realmente a cambio. La introducción de esta IA en el videojuego fue aclamada porque la creación de una intensa atmósfera de terror estuvo muy presente durante todo el transcurso del juego. Algunos de ellos sí dieron señales hacia una jugabilidad frustrante en dificultad, basándose en el hecho de que un Xenomorfo es una criatura adaptable. Nuevamente, este sería un ejemplo perfecto de una IA excelente y adecuada, inmersión dentro de un videojuego y un estímulo para muchas de sus respuestas emocionales.

“Fig 12 Portada Alien: Isolation"

https://www.nintendo.com/es-es/Juegos/Programas-descargables-Nintendo-Switch/Alien- Isolation-1575873.html

4. Dota 2 y los bots de OpenAI Durante 2018, OpenAI tenía listo un equipo de bots que podrían competir en el videojuego Dota 2, que es una estrategia en tiempo real con alta complejidad debido a su gran cantidad de variables y decisiones tomadas dentro de una partida. Mientras entrenaban a estos bots de OpenAI, los métodos de aprendizaje por refuerzo han permitido que los agentes de IA jueguen entre sí muchos millones de veces, aprendiendo así en ese proceso cómo hacer uso de estrategias óptimas. Esos eventuales bots salieron adelante para ganar varios juegos uno contra uno, después de lo cual incluso pudieron ganar

LUCAS MELGARES CARMONA 49

---

<!-- Página 55 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

juegos completos en equipo, de hecho, una visión bastante profunda de la jugabilidad y de hacer las coordinaciones necesarias en el trabajo en equipo. Sería un testimonio interesante de la importancia que tiene la capacidad actual de la IA para dominar juegos complejos, que exigen una gran capacidad para gestionar planes estratégicos, adaptación y,

sobre todo, coordinación de varios procesos prácticamente en tiempo de ejecución. Si bien las técnicas presentadas en este contexto limitado son prometedoras, los resultados muestran que las discusiones sobre su implementación en contextos más amplios se deben a la enorme potencia computacional necesaria para el entrenamiento de los robots.

Todos estos ejemplos que se acaban de mencionar usan IA generativa, una tecnología que hoy día se sigue usando en múltiples casos y con muchos más ejemplos, simplemente se han mencionado cuatro que han sido estudiados al completo y que se han implementado. Esta IA generativa también se puede usar como herramienta de apoyo en todas las áreas del desarrollo, es decir, en el diseño de la historia, personajes o niveles hasta la programación, traducción en diferentes idiomas, su música o efectos de sonido… Lo que está impulsado la creatividad e innovación en los equipos, democratizando el acceso al desarrollo y producción de videojuegos.

“Fig 13 Portada Dota 2"

https://www.vidaextra.com/esports/dota-2-para-dummies-iniciacion-a-la-defensa-de-los- ancestros

LUCAS MELGARES CARMONA 50

---

<!-- Página 56 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

(Qué es la inteligencia artificial en videojuegos, 2024), (La IA ya está ocupando puestos de trabajo en la industria de los videojuegos, 2024), (Inteligencia artificial (videojuegos), 2024), (Inteligencia artificial reemplazó estos trabajos en la industria de los videojuegos, 2024), (Cómo se aplica la Inteligencia Artificial en los videojuegos, 2024), (El

papel de la inteligencia artificial en los videojuegos, 2024), (¿Qué papel tiene la inteligencia artificial en los videojuegos?, 2024), (IA en la industria de los videojuegos, 2024), (Aplicaciones de la inteligencia artificial en el sector gaming, 2024), (La inteligencia artificial en videojuegos, 2024), (Innovación y creatividad en el diseño de videojuegos: el uso de la IA, 2024), (IA en Gaming, 2024), (La IA en los videojuegos: dando forma al futuro de los videojuegos, 2024), (PARENTE, 2024), (Inteligencia artificial en videojuegos: una mirada al pasado y futuro de la industria, 2024), (La industria del gaming tiene un amor-odio por la IA, 2024)

5.1.2. IA en el marketing digital

La IA ha revolucionado por completo el marketing digital. Ha ayudado a su empresa a procesar grandes cantidades de datos, personalizar la experiencia de los consumidores y obtener una estrategia optimizada. En este sentido, la IA trabaja en la velocidad y precisión del procesamiento de la información, al tiempo que identifica patrones de comportamiento y predice tendencias dentro de este contexto, mientras que en el marketing digital se inculcan algoritmos avanzados, que incluyen, entre otros, la segregación de audiencias, la generación de contenido, la gestión de campañas publicitarias y la generación de recomendaciones.

Tal vez lo más relevante para el marketing sea que la IA generativa crea contenido automáticamente, desde textos y diseños hasta videos y anuncios. Reduce el tiempo y el costo de la producción creativa al tiempo que desarrolla materiales relevantes y atractivos para una audiencia objetivo. A continuación, se muestran algunos ejemplos sorprendentes de cómo se ha aplicado la IA al marketing digital, como se ha dicho en el caso anterior, han sido ejemplos ya usados hoy en día con un estudio completo.

LUCAS MELGARES CARMONA 51

---

<!-- Página 57 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

1. Coca-Cola y la IA para la creación de contenidos Recientemente, Coca-Cola ha adoptado la IA generativa para crear campañas publicitarias innovadoras dirigidas a públicos específicos. Un buen ejemplo es el uso de herramientas como OpenAI y DALL·E

para crear imágenes personalizadas y textos atractivos para sus anuncios. Con la IA, cada pieza de contenido puede alinearse con las preferencias individuales de los consumidores, desde los colores y los estilos visuales hasta el tono de los mensajes, ajustándose a las normas y manual de marca

Además, Coca-Cola utiliza algoritmos de aprendizaje automático sobre datos de redes sociales para reflejar las tendencias y opiniones sobre la marca en tiempo real. Este enfoque les permite realizar ajustes proactivos en las campañas para mejorar el compromiso con su audiencia. Las conclusiones obtenidas han demostrado que las campañas personalizadas generan un mayor compromiso y lealtad hacia la marca.

“Fig 14 Coca-Cola recrea su anuncio navideño más icónico con la IA como total protagonista”

https://www.marketingdirecto.com/campanas-navidenas/coca-cola-recrea-anuncio-navideno- iconico-ia-total-protagonista

2. Netflix y la personalización del marketing Netflix es uno de los principales ejemplos de aplicación de la IA a la personalización. Si bien para la mayoría de las personas esto significa la recomendación de contenido, también utiliza la IA en sus estrategias

LUCAS MELGARES CARMONA 52

---

<!-- Página 58 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

de marketing digital. Guiándose por los datos de comportamiento, Netflix crea correos electrónicos, anuncios y redes sociales de una manera que capte la atención de los usuarios y muestre nuevas series o películas que se ajusten mejor a sus gustos.

Por ejemplo, con cada nuevo lanzamiento de producción, Netflix hace varias variantes de tráiler y carteles promocionales en relación con los intereses pasados de los usuarios. Si a uno le gustan las novelas románticas, obtendrá un tráiler que subrayará solo la parte romántica de esa serie, mientras que un amante de la acción obtendrá un tráiler con las escenas más emocionantes. Este enfoque ha resultado en un aumento significativo en las tasas de conversión y retención de usuarios. Además, las pruebas A/B continuas han podido agudizar las estrategias basadas en IA de la empresa.

“Fig 15 La netflixización de los contenidos en marketing digital”

https://www.cyberclick.es/numerical-blog/la-netflixizacion-de-los-contenidos-en-marketing-digital

3. Sephora y los chatbots inteligentes Sephora, una marca de cosméticos, ha integrado chatbots impulsados por IA en sus estrategias de marketing digital y atención al cliente. Los chatbots de Sephora, como "Sephora Virtual Artist", no solo responden a las consultas, sino que también hacen el trabajo de sugerir una gama

LUCAS MELGARES CARMONA 53

---

<!-- Página 59 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

de opciones basadas en las preferencias anteriores y el historial de compras, junto con el análisis de tendencias.

Además, los beneficios de la IA generativa son que los chatbots pueden crear contenido educativo (por ejemplo, tutoriales de maquillaje o guías de cuidado de la piel) que se proporcionarían específicamente para cada usuario. En este sentido, la experiencia del cliente mejorará y podría mantener un mayor compromiso con la marca.

Estas métricas recopiladas muestran que ha habido un aumento en las ventas y una reducción en los tiempos de respuesta, lo que refuerza la eficacia de la IA como herramienta de marketing y soporte.

“Fig 16 Sephora y ejemplo de implementación de su chatbots”

https://reads.alibaba.com/es/10-ways-chatbot-implementation-enhances-your-ecommerce-web- store/

4. Amazon y la publicidad programática basada en IA Amazon ha revolucionado el espacio de la publicidad digital con sus campañas programáticas administradas por IA. Sus algoritmos analizan la información del usuario sobre el historial de compras, las búsquedas y las preferencias para utilizarla para una segmentación precisa de la audiencia y mostrar anuncios relevantes exactamente en el momento adecuado.

Además, Amazon implementa IA en la optimización en tiempo real de las ofertas para garantizar que los anunciantes obtengan el mejor

LUCAS MELGARES CARMONA 54

---

<!-- Página 60 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

retorno de la inversión. Por ejemplo, durante la promoción de un nuevo producto, la IA evalúa qué formato de anuncio, plataforma y franja horaria son más eficientes para llegar a la audiencia objetivo.

El uso de la IA también permite a Amazon contabilizar el resultado de sus campañas con un grado de precisión hasta ahora impensable, suele definir qué estrategias funcionan mejor y realizar cambios rápidos en ellas. Fue precisamente este enfoque el que le ayudó a mantener el liderazgo en el comercio electrónico.

“Fig 17 Amazon está introduciendo anuncios en Rufus, su asistente de IA para la compra”

https://www.reasonwhy.es/actualidad/amazon-introduce-anuncios-rufus-asistente-inteligencia- artificial

5. Spotify y la personalización de anuncios Spotify utiliza la IA para rastrear el comportamiento de sus usuarios en lo que escuchan y utiliza los resultados para crear anuncios personalizados para ellos. Mezclará datos demográficos, geográficos y de preferencias musicales para diseñar una campaña dirigida a este grupo. La segmentación a través de Spotify, por ejemplo, se puede hacer en función del estado de ánimo o la hora del día. Si uno escucha música relajada al final, los anuncios promocionados pueden estar orientados a productos de descanso o bienestar. Este nivel de personalización no solo mejora la experiencia del usuario, sino que también aumenta la efectividad de las campañas publicitarias. Spotify también ha recurrido a la IA generativa para crear jingles únicos y

LUCAS MELGARES CARMONA 55

---

<!-- Página 61 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

mensajes sonoros personalizados para cada oyente para mejorar el engagement de los anuncios.

Después de analizar y describir estos casos, se puede ver como la IA está transformando el marketing digital, ofreciendo una experiencia más personalizada y efectiva para cada usuario según sus gustos. Esto es solo el principio, lo más probable es que surjan muchas más aplicaciones que amplíen aún más las posibilidades de la IA.

“Fig 18 Spotify usa la IA para crear anuncios en los podcasts entre otros sectores”

https://es.linkedin.com/pulse/spotify-usa-la-ia-para-crear-anuncios-en-los-podcast-juan-merodio

(Coca-Cola y la IA para Predecir Tendencias y Conquistar al Mundo, 2024), (Cinco formas en que Coca-Cola utiliza la IA para mejorar su marketing, 2024), (Lecciones de personalización: lo que Netflix puede enseñar a los equipos de marketing y ventas, 2024), (¿Cómo funciona la personalización de Amazon y Netflix?, 2024), (Chatbot Sephora, 2024), (Implementación de Chatbots con GPT-4 en Atención al Cliente, 2024), (Cómo la publicidad basada en IA generativa puede ayudar a las marcas a contar su historia e interactuar con los clientes, 2024), (Publicidad programática, 2024), (Personalized Marketing: Spotify y su estrategia de personalización, 2024), (Spotify trabaja en una herramienta para crear anuncios personalizados con IA generativa, 2024), (Diez formas en que la implementación de Chatbot mejora su tienda web de comercio electrónico, 1025)

LUCAS MELGARES CARMONA 56

---

<!-- Página 62 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

5.1.3. IA en otros sectores: e-commerce, salud, educación

La Inteligencia Artificial se ha convertido en un elemento importante en sectores clave como el comercio electrónico, la salud y la educación. En todos estos campos, la IA transforma por completo las dinámicas tradicionales, dando paso a niveles de personalización, automatización y eficiencia nunca antes vistos. En cada una de estas áreas, la IA juega un papel diferente: permite una mayor eficiencia, personalización y accesibilidad. Antes de considerar ejemplos específicos, primero debe buscarse una comprensión de cómo se aplica la IA en cada uno de estos sectores.

La IA para el comercio electrónico no termina con las recomendaciones personalizadas de productos, se extiende a la mejora de las experiencias de los clientes con la anticipación de las necesidades y la optimización de la logística. Ya sean chatbots, asistentes virtuales o algoritmos de aprendizaje automático, todos utilizan big data para predecir las tendencias de compra que permitirán cambios en tiempo real en las estrategias de marketing.

La IA médica sirve para mejorar el diagnóstico, predecir el momento de aparición de la enfermedad, ofrecer un tratamiento personalizado y optimizar todos los procesos dentro de un hospital. En otras palabras, los algoritmos procesan una gran cantidad de datos médicos utilizando modelos predictivos para delinear los riesgos y ofrecer soluciones de manera proactiva.

Por último, tenemos la IA que se está adoptando en la educación para adaptar fácilmente los programas educativos a las necesidades de los estudiantes. Está cambiando el paradigma de la forma en que los estudiantes adquieren conocimientos, desde plataformas de aprendizaje personalizadas hasta asistentes virtuales, para hacer que la educación sea accesible para los grupos desfavorecidos.

A continuación, se mencionarán y se explicarán casos en específicos de empresas que usan la IA en estos sectores, explicando como la usan y unas pequeñas conclusiones.

LUCAS MELGARES CARMONA 57

---

<!-- Página 63 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

1. La IA en el comercio electrónico: Amazon, Alibaba y Zalando Amazon ha desarrollado uno de los sistemas de recomendación más sofisticados del mundo, con IA que procesa datos sobre el historial de

compras, el tiempo de navegación y las preferencias de los usuarios. Este sistema ofrece sugerencias muy específicas sobre los productos exactos que un consumidor podría querer comprar y representa el 35% de las ventas totales de la compañía. Además, la compañía ha utilizado la IA en su cadena de suministro para optimizar los inventarios y predecir la demanda con el objetivo de reducir los costes en logística.

“Fig 19 Amazon tiene un nuevo aliado, la IA"

https://www.programaticaly.com/otras-noticias/amazon-refuerza-inversion-anthropic-impulsar-ia- generativa

Alibaba ha ido un paso más allá con la implementación de la IA a través de su evento de ventas "Single's Day", donde los algoritmos generan anuncios personalizados y procesan millones de transacciones al mismo tiempo. También han desarrollado "City Brain", un sistema que aplica la IA para optimizar la logística urbana en tiempo real,

LUCAS MELGARES CARMONA 58

---

<!-- Página 64 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

asegurando que los productos lleguen a los clientes de forma más rápida y eficiente.

“Fig 20 Volumen bruto de mercancías de Alibaba durante el Singles’ Day en China”

https://www.statista.com/chart/16063/gmv-for-alibaba-on-singles-day/

La empresa de moda europea Zalando utiliza la IA para predecir las preferencias de estilo de los usuarios. Su herramienta "Zalando Algorithmic Fashion Companion" analiza las tendencias de moda globales y combina estos datos con las preferencias personales de los clientes para sugerir conjuntos personalizados.

LUCAS MELGARES CARMONA 59

---

<!-- Página 65 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 21 Zalando y su probador virtual”

https://es.fashionnetwork.com/news/Zalando-lanza-un-probador-virtual-en-sus-25- mercados,1509974.html

Estos ejemplos también muestran cómo la IA puede optimizar los procesos internos y cambiar totalmente la cara de las compras haciéndolas más personalizadas y efectivas.

2. Inteligencia artificial en medicina: IBM-Watson-Health, PathAI y DeepMind IBM Watson Health ha cambiado por completo el mundo de la oncología al procesar datos clínicos y publicaciones científicas para proponer tratamientos personalizados. En un estudio en colaboración con centros médicos estadounidenses, Watson pudo identificar planes de tratamiento en el 90% de los casos de cáncer analizados, lo que es comparable a los expertos humanos.

“Fig 22 IBM Watson Health logo”

LUCAS MELGARES CARMONA 60

---

<!-- Página 66 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

PathAI se especializa en el análisis de biopsias mediante IA. Sus algoritmos analizan patrones en muestras de tejido para realizar diagnósticos, como el cáncer, con mucha más precisión y velocidad en comparación con los métodos tradicionales. Esto aumenta no sólo la

precisión del diagnóstico, sino que también reduce significativamente los tiempos de espera.

“Fig 23 PathAI logo”

DeepMind ha desarrollado herramientas para predecir enfermedades renales agudas con hasta 48 horas de antelación. Este modelo se ha puesto en práctica en hospitales del Reino Unido y ha conseguido evitar complicaciones graves en pacientes críticos.

“Fig 24 DeepMind logo”

La IA en salud aumenta la velocidad y precisión de los diagnósticos y abre nuevas perspectivas para tratamientos más personalizados, mejorando la calidad de vida de los pacientes.

3. La IA en educación: Duolingo, Squirrel AI y Khan Academy La plataforma de aprendizaje de idiomas online Duolingo aplica la IA para personalizar las lecciones según las necesidades individuales.

LUCAS MELGARES CARMONA 61

---

<!-- Página 67 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Los algoritmos de deep learning comprueban el progreso de cada usuario y ajustan las actividades según su nivel de dificultad. Además, su herramienta “Stories” utiliza la IA generativa para crear historias personalizadas que mantengan el interés de los usuarios.

“Fig 25 Duolingo y su nueva herramienta Stories”

https://blog.duolingo.com/es/como-duolingo-usa-la-ia-para-crear-lecciones-mas-rapido/

Squirrel AI es una startup china que ofrece tutorías personalizadas mediante IA. Los algoritmos calculan el nivel de conocimientos de cada alumno y ofrecen ajustes en tiempo real en sus contenidos para asegurar el máximo aprendizaje. Se ha demostrado en estudios realizados en escuelas piloto que los estudiantes que utilizan Squirrel AI mejoran notablemente sus notas en comparación con los métodos tradicionales.

“Fig 26 Squirrel logo startup china”

LUCAS MELGARES CARMONA 62

---

<!-- Página 68 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Khan Academy utiliza la IA para identificar las lagunas en el conocimiento de los estudiantes y recomendar los materiales específicos que ayudarán a llenar esas lagunas. Su plataforma, utilizada en más de 190 países, también incorpora análisis en tiempo real para que los profesores puedan supervisar el progreso de sus

estudiantes.

“Fig 27 Khan Academy logo”

La IA en la educación puede permitir además un mejor aprendizaje, una mejor accesibilidad y un uso más eficiente, ayudando así a los estudiantes y profesores a adaptar el contenido a sus necesidades y optimizar los recursos.

El uso de la IA en el comercio electrónico, la salud y la educación muestra la nueva tendencia en la que se está sumergiendo esta tecnología debido a las importantes demandas de la sociedad. Desde la personalización de las compras hasta los diagnósticos médicos para optimizar el aprendizaje, la IA muestra un inmenso potencial para

convertirse en una de las herramientas más potentes que ayudan a encontrar soluciones a problemas grandes y complejos. Al mismo tiempo, también plantean algunas cuestiones éticas y técnicas cuyas respuestas definitivamente se encontrarán al ampliar esta tecnología.

(La Inteligencia Artificial en el E-commerce, 2024), (Alibaba actualiza su modelo de IA para competir con Amazon y Microsoft, 2024),

LUCAS MELGARES CARMONA 63

---

<!-- Página 69 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

(Zalando lanza su asistente de IA en España: ofrece recomendaciones personalizadas y aprende de los usuarios, 2024), (IBM Watson Health vs Google DeepMind Health: Soluciones de IA para diagnóstico médico, 2024), (Big Data e IA en la salud: la medicina del futuro, 2024), (Cómo Duolingo usa la IA para crear lecciones más rápido, 2024), (Esta

startup china de Inteligencia Artificial quiere revolucionar la manera en la que se estudia en los colegios, pero sin sustituir profesores, 2024)

- 5.2. Comparativa de herramientas y tecnologías disponibles En este apartado se analizan, con más detalle y en términos más comparativos que nunca, las principales herramientas y tecnologías de IA disponibles en la actualidad, centrándose en su aplicabilidad en relación con el diseño y desarrollo de la experiencia de usuario. Se ofrece una visión general que abarca desde soluciones de código abierto hasta plataformas comerciales para que se puedan entender las posibilidades y limitaciones de cada tipo de herramienta. El siguiente análisis intenta poner en contexto las condiciones en las que realmente sería posible entender cuáles son las implicaciones prácticas de las tecnologías analizadas y qué consecuencias podrían tener en la industria.

En primer lugar, en el primer subapartado analizaremos la IA de código abierto, que es un conjunto de tecnologías innovadoras creadas por comunidades vibrantes de desarrolladores activos en todo el mundo. Algunos ejemplos, entre otros, incluyen TensorFlow, que según Wiquipèdia “es una biblioteca de software de código abierto en el ámbito del aprendizaje profundo y automático.” (TensorFlow, 2025), PyTorch que según IBM “es un marco de deep learning de código abierto basado en software que se utiliza para crear redes neuronales, combinando la biblioteca de machine learning (ML) de Torch con una API de alto nivel basada en Python.” (¿Qué es PyTorch?, 2025) o Hugging Face, que según Keepgoing es “una empresa de tecnología que se dedica al desarrollo de herramientas y plataformas de procesamiento de lenguaje natural o NLP basadas en inteligencia artificial.” (¿Qué es Hugging Face?, 2025). Estas empresas, han demostrado ser fundamentales para investigadores y empresas al ofrecer flexibilidad, escalabilidad y transparencia.

En el segundo subapartado de Plataformas comerciales para IA en UX, el lector conocerá con mayor detalle las soluciones más populares para IA en UX

LUCAS MELGARES CARMONA 64

---

<!-- Página 70 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

desarrolladas por grandes empresas tecnológicas: Adobe Sensei, Google Cloud AI y Microsoft Azure AI. La mayoría de ellas cuentan con interfaces muy fáciles de usar y soporte técnico, que son irremplazables para las empresas que desean implementar IA en el menor tiempo posible y con el mínimo esfuerzo. Se discutirán los modelos de negocio basados en suscripciones, la

profundidad de las capacidades técnicas proporcionadas y las limitaciones en cuanto a personalización y acceso a datos en bruto. Todo esto se reflejará en el tercer subapartado. De hecho, es más crítico desde la perspectiva de la crítica sobre lo que esto realmente significa para la industria al considerar las influencias que las herramientas y tecnologías antes mencionadas tienen tanto en los procesos creativos como técnicos dentro del diseño de UX. Esta parte revisará los cambios que las tecnologías emergentes traen a las interacciones que los usuarios tienen con los productos, y lo que todos esos cambios significan desde un punto de vista ético, pero también práctico. La comparación de rendimiento será cuantitativa y cualitativa, sobre la facilidad de integración y la adaptabilidad en diferentes escenarios de uso; los casos concretos mostrarán tanto la eficacia como los desafíos introducidos. Por lo tanto, se convierte en la guía clave para todo profesional, estudiante o investigador que quiera profundizar en la aplicación práctica de la IA en el campo de la UX. Al reflexionar sobre el impacto de las plataformas tanto de código abierto como comerciales, esto le dará una visión equilibrada para elegir las más adecuadas para usar en los proyectos futuros. De hecho, sobre esta base, las decisiones sobre la implementación de la IA se pueden tomar con plena conciencia, teniendo en cuenta no sólo el contexto técnico sino también los contextos económicos, éticos y creativos en los que operan estas herramientas.

5.2.1. Herramientas de IA de código abierto

El desarrollo de herramientas de IA de código abierto ha convertido el

panorama tecnológico en uno de recursos fáciles, flexibles y transparentes para investigadores, desarrolladores y diseñadores de UX. Estas herramientas permitirán a las organizaciones aprovechar el poder de la IA con menores costos asociados con las plataformas comerciales. También pueden brindar la capacidad de personalizar algoritmos según las necesidades de cada proyecto. A continuación,

LUCAS MELGARES CARMONA 65

---

<!-- Página 71 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

se presentan algunas de las herramientas de código abierto más destacadas, los casos de uso existentes actualmente y las lecciones aprendidas durante su implementación.

TensorFlow

Una de las bibliotecas de IA más populares y versátiles es TensorFlow, desarrollada por Google. Está diseñada para crear y entrenar modelos de ML y DL, es decir, modelos de aprendizaje automático (ML) y aprendizaje profundo (DL) que describen el uso de algoritmos y técnicas de gran complejidad para procesar y analizar datos con el fin de producir predicciones o decisiones en tiempo real. Su capacidad para funcionar en múltiples plataformas, desde dispositivos móviles hasta supercomputadoras, la hace adecuada para una amplia gama de proyectos.

Caso de uso en UX: Un ejemplo destacado es su uso en el sistema de recomendaciones de YouTube, donde TensorFlow analiza los patrones de comportamiento de los usuarios para sugerir videos que les resulten de interés. Debido a su capacidad para procesar grandes volúmenes de datos en tiempo real, la plataforma ha mejorado considerablemente la retención y satisfacción de los usuarios.

“Fig 28 TensorFlow y sus sistemas de recomendación”

https://www.tensorflow.org/resources/recommendation-systems?hl=es-419

En resumen, TensorFlow ha demostrado ser muy útil para escalar soluciones de personalización de UX al optimizar tanto el rendimiento técnico como la experiencia del usuario.

LUCAS MELGARES CARMONA 66

---

<!-- Página 72 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

PyTorch PyTorch es otra biblioteca de código abierto extremadamente popular proporcionada por Facebook. Ha ganado una gran cantidad de seguidores debido a su simplicidad y facilidad de uso. En la investigación de redes neuronales profundas y la implementación de

visión artificial, realmente reemplaza a la corona.

Caso de uso en UX: PyTorch se ha utilizado para el desarrollo de interfaces adaptativas en aplicaciones móviles. Por ejemplo, empresas como Shopify querían integrar esta herramienta para predecir y ajustar el diseño de sus plataformas en función de los patrones de uso. La IA analiza el tiempo que uno pasa en cada sección y reorganiza dinámicamente los elementos para priorizar los más relevantes.

“Fig 29 PyTorch logo”

En resumen, PyTorch tiene un valor especial para la UX adaptativa porque permite a las empresas responder rápidamente a las necesidades cambiantes de los usuarios, mejorando la retención y la conversión.

Hugging Face Hugging Face es una empresa que se dedica al procesamiento del lenguaje natural y al aprendizaje automático. El uso de modelos preentrenados como GPT y BERT a través de su biblioteca

LUCAS MELGARES CARMONA 67

---

<!-- Página 73 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

'Transformers' para cosas como la generación de texto, la traducción y el análisis de sentimientos es mucho más fácil hoy en día.

Caso de uso en UX: Hugging Face se ha utilizado en plataformas como Duolingo

para personalizar las recomendaciones de lecciones en función del progreso percibido y la dificultad de cada usuario. Esto también hizo posible, con la integración de modelos de procesamiento del lenguaje natural, una retroalimentación más detallada que podría ser motivadora.

“Fig 30 Hugging Face logo”

En resumen, Hugging Face ha sido eficaz para generar mejoras en la personalización y el compromiso en las plataformas educativas, aumentando la satisfacción y las tasas de finalización de los cursos.

OpenCV OpenCV es una biblioteca de código abierto, utilizada básicamente para visión artificial. Se ha utilizado para ejecutar algoritmos de detección de objetos, detección de rostros e incluso para procesar imágenes.

Caso de uso de UX: OpenCV se ha implementado en el sector minorista para analizar transmisiones de video de la tienda física, encontrar áreas de alto tráfico y reajustar la disposición de los productos

LUCAS MELGARES CARMONA 68

---

<!-- Página 74 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

en sus tiendas en tiempo real. Esto optimiza la experiencia de compra al facilitar la búsqueda de productos populares.

“Fig 31 OpenCV logo”

En resumen, OpenCV ha sido sobresaliente en el arte de desarrollar una conexión de IA con datos del mundo físico, mejorando la interacción entre los usuarios y los espacios minoristas.

En conclusión, las herramientas de código abierto como TensorFlow, PyTorch, Hugging Face y OpenCV están reescribiendo las reglas sobre cómo las empresas abordan el diseño y la iteración de las experiencias de usuario. Debido a su flexibilidad, accesibilidad y capacidad de personalización, son las soluciones a las que recurren todos, desde las empresas emergentes hasta las grandes corporaciones. Además de democratizar el acceso a la IA, estas herramientas también permiten la experimentación y la innovación en el desarrollo de interfaces más dinámicas y personalizadas, pero lo más importante es que benefician al usuario final.

(Introducción a TensorFlow, 2025), (¿Qué es PyTorch?, 2025), (La importancia de Hugging Face, 2025), (¿Qué es OpenCV?, 2025)

5.2.2. Plataformas comerciales para la IA a UX

Las plataformas comerciales de IA ya han cambiado las reglas del juego en el diseño y la optimización de la experiencia del usuario. A diferencia de las herramientas de código abierto, las plataformas comerciales ofrecen soluciones completas y altamente integradas para las necesidades particulares de las empresas. Estas suelen incluir

LUCAS MELGARES CARMONA 69

---

<!-- Página 75 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

soporte técnico, interfaces fáciles de usar, actualizaciones periódicas y capacidades avanzadas que hacen que la implementación de la IA en proyectos de experiencia del usuario sea bastante sencilla. A continuación, se presentan algunas de las plataformas comerciales más destacadas, sus casos de uso y los efectos que tienen en la

industria.

Adobe Sensei Adobe Sensei es una plataforma de IA dentro del ecosistema de Adobe. Creada desde cero para impulsar herramientas creativas como Photoshop, Illustrator y Experience Manager, hasta otras más analíticas como Analytics, Sensei facilita el trabajo de los creativos, simplifica el análisis de datos y hace que las experiencias sean más personales.

Caso de uso de UX: La razón es que, en términos generales, la personalización de las experiencias de sitios web y aplicaciones con Sensei es importante funcionan mejor. Por ejemplo, en Adidas, Sensei ha estado analizando los comportamientos de los usuarios en línea con una precisión de hasta microsegundos para brindar recomendaciones de productos en tiempo real y mejorar la navegación del sitio y el diseño visual personalizado desde la perspectiva del cliente. Automatiza la creación de banners responsivos y contenido visual en función de la segmentación de la audiencia.

“Fig 32 Adobe Sensei logo”

LUCAS MELGARES CARMONA 70

---

<!-- Página 76 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

En resumen, las empresas que han implementado Adobe Sensei informaron una mejora muy significativa en la participación de los usuarios, incluida una mayor conversión y retención de clientes.

IBM Watson IBM Watson probablemente sirva como la solución de IA más avanzada y multivariante hasta la fecha que podría comprender, deducir, aprender, casi hasta tal punto con capacidades UX mientras predice, sugiere, procesa lenguaje natural, personaliza contenido, entre otros.

Caso de uso de UX: IBM Watson se ha instalado en KLM para construir un sistema de servicio al cliente basado en inteligencia artificial. Watson analiza las preguntas más frecuentes y brinda respuestas personalizadas para los clientes en tiempo real, mejorando la experiencia del usuario con la marca por un amplio margen. También se está utilizando en Macy's, una cadena de tiendas, para ayudar a los clientes a navegar por establecimientos físicos con el uso de chatbots inteligentes.

En resumen, ha ayudado a las organizaciones a reducir los costos operativos y al mismo tiempo aumentar la satisfacción del cliente debido a interacciones más rápidas y precisas.

Salesforce Einstein Einstein es la IA de Salesforce diseñada para permear cada rincón de su ecosistema CRM. Proporciona la capacidad de analizar datos de los clientes y automatizar las interacciones para las empresas, lo que les permite ajustar las estrategias de UX en tiempo real.

Caso de uso de UX: Por ejemplo, en Coca-Cola, Salesforce Einstein se utiliza para entender el comportamiento de sus clientes a través del análisis de datos de consumo y ventas, enviando así comunicaciones de marketing dirigidas, y para sugerir productos mediante máquinas expendedoras inteligentes. También da pronósticos

LUCAS MELGARES CARMONA 71

---

<!-- Página 77 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

sobre el comportamiento de compra de los usuarios para poder cambiar la comunicación con ellos.

“Fig 33 Salesforce Einstein logo”

En resumen, Salesforce Einstein ha demostrado ser muy eficiente para impulsar las ventas, además de asegurar la lealtad del cliente a través de interacciones más relevantes y personalizadas.

Amazon Web Services-AI Trabaja sobre una variedad de servicios vanguardistas basados en IA ofrecidos por AWS que incluyen, pero no se limitan a, Amazon Personalize, Amazon Recognition y Amazon Lex. Estas herramientas ayudan a brindar experiencias personalizadas a través del análisis de imágenes y textos, con un enfoque en la creación de asistentes virtuales inteligentes.

Caso de uso de UX: Dominos Pizza utiliza Amazon Personalize para mejorar la aplicación de pedidos de la cadena para sugerir automáticamente combinaciones de productos y personalizar ofertas de acuerdo con el historial de compras de cada cliente. Para Snapchat, Amazon Rekognition ejecuta filtros de realidad aumentada en tiempo real, gracias al reconocimiento facial.

LUCAS MELGARES CARMONA 72

---

<!-- Página 78 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 34 Amazon Personalize logo”

En resumen, AWS AI ha permitido a las empresas ofrecer experiencias más interactivas e intuitivas para los usuarios, aumentando la satisfacción y el compromiso.

En conclusión, sabemos que las soluciones de las principales herramientas de IA comercial (Adobe Sensei, IBM Watson, Salesforce Einstein y AWS AI) garantizan que las empresas tengan medios integrales para implementar transformaciones en su estrategia de UX. Las tecnologías avanzadas combinadas con una facilidad intuitiva para aplicar la IA en un dominio específico: todo lo que se necesita es incorporar tecnologías y aplicarlas fácilmente. Si bien estas herramientas implican una inversión importante, los efectos positivos de esta inversión se producen en muchos aspectos: la personalización, la eficiencia operativa y la satisfacción del cliente son solo algunos de ellos. Estas son las plataformas futuras en el diseño de experiencias, y la interacción será mucho más dinámica y efectiva entre las marcas y sus usuarios.

(Te presentamos la generación IA, 2025), (¿Qué es Adobe Sensei y Cómo Aprender a Usarlo?, 2025), (Soluciones de tejido de datos, 2025), (De IBM Watson a watsonx, 2025), (Inteligencia artificial de Salesforce, 2025), (El impacto de la inteligencia artificial en los negocios: Caso de estudio de Coca-Cola, 2025), (Explorador de casos de uso de IA, 2025), (Domino’s Pizza Enterprises entrega en tiempo récord utilizando AWS para pedidos predictivos, 2025).

LUCAS MELGARES CARMONA 73

---

<!-- Página 79 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

5.2.3. Evaluación de su impacto en la industria

La integración de herramientas y plataformas de inteligencia artificial en la UX ha marcado una diferencia fundamental para muchas industrias. Se trata de un nuevo capítulo o etapa en la forma en que los consumidores y las marcas interactúan. En esta sección se evalúa cómo las herramientas de código abierto y el empleo de plataformas comerciales y tecnologías emergentes explicadas anteriormente, por parte de la industria para la eficiencia, la personalización y la capacidad de innovación se han aplicado desde diferentes dimensiones.

Impacto en la eficiencia operativa Una de las mayores contribuciones de la IA en la UX tiene que ver con la mejora de la eficiencia operativa. Con herramientas como TensorFlow y PyTorch, los desarrolladores pudieron aprovechar los modelos de aprendizaje automático para optimizar los procesos de diseño y análisis. Las plataformas de código abierto reducen el tiempo de creación de prototipos y validación de nuevas ideas, mientras que las plataformas comerciales como Salesforce Einstein y Adobe Sensei ofrecen soluciones listas para usar que abstraen la mayor parte de la complejidad técnica. Por ejemplo, la automatización de tareas repetitivas, como el análisis de datos o la creación de contenido visual, libera recursos que las empresas pueden utilizar para impulsar la innovación. De hecho, un informe de Deloitte muestra que las empresas que adoptan la IA en su estrategia de UX han visto una mejora del 25% en la eficiencia operativa.

Impacto en la personalización Otros logros brillantes de la IA en UX son la personalización. IBM Watson, Amazon Personalize, ejemplos de una plataforma que analiza grandes volúmenes para entender los gustos y el comportamiento de los clientes. Las experiencias han dado como resultado una “hiperpersonalización” para un mejor vínculo entre las marcas y los consumidores.

LUCAS MELGARES CARMONA 74

---

<!-- Página 80 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

En el caso de Netflix, por ejemplo, la recomendación impulsada por IA contribuyó al alto porcentaje de sus suscriptores retenidos. Un artículo de McKinsey afirmó que el 75% de todo el contenido que se ve en Netflix se basa en recomendaciones algorítmicas. Aquí es donde la personalización impulsada por IA demuestra lo efectiva que es.

Impacto en la innovación y la creatividad La IA también ha sido un motor de innovación y creatividad dentro de la industria, permitiendo la creación de experiencias de usuario nunca antes vistas. Por ejemplo, herramientas como Runway ML se están utilizando para generar contenido visual y audiovisual de alta calidad utilizando inteligencia artificial generativa. Esto abre nuevas posibilidades en sectores donde la creatividad juega un papel importante, como en el entretenimiento y la publicidad. Empresas como Airbnb han utilizado la IA en el análisis de patrones de comportamiento de los usuarios para desarrollar interfaces más intuitivas y atractivas en el diseño de productos. Esto permitirá mejorar la experiencia del usuario y, al mismo tiempo, aumentar la ventaja competitiva de la empresa.

Impacto ético y social Además de todos los beneficios, existen importantes desafíos éticos y sociales relacionados con el uso de la IA en la experiencia del usuario. El uso de algoritmos sesgados, la falta de transparencia y las preocupaciones sobre la privacidad de los datos son cuestiones que las empresas que desean evitar daños a largo plazo deberían tener en cuenta. De hecho, un estudio de MIT Technology Review descubrió que el 78 % de los consumidores temen que sus datos personales se utilicen indebidamente al interactuar con plataformas impulsadas por IA.

Estas herramientas y plataformas están influyendo en la industria UX a muchos niveles: primero, ofreciendo eficiencias mucho mayores en la creación de experiencias “hiperpersonalizadas”, permitiendo la innovación y muchos otros. Por supuesto, estos desarrollos no están exentos de desafíos, más aún éticos y relacionados con la privacidad,

LUCAS MELGARES CARMONA 75

---

<!-- Página 81 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

pero para los cuales las empresas deben ser siempre proactivas si quieren conservar la confianza del cliente. Se refiere al análisis necesario para el establecimiento de dichas herramientas y tecnologías, centrándose en cómo esto podría llevarse a cabo en la práctica con vistas a maximizar los beneficios y minimizar

los riesgos, asegurando que será sostenible y ético. Algunos casos reales que muestran el impacto de estas tecnologías se comentarán más adelante con el apoyo de la parte práctica de este TFG, obteniendo conclusiones más concretas que podrían aplicarse en el ámbito profesional.

(Tech Trends 2025, 2025), (Optimización de modelos de TensorFlow, 2024), (Mejora continua – logrando que la buena gestión se convierta en un hábito para los líderes, 2024), (Amazon Personalize, 2025), (Perfil de la empresa Runway ML: Líder en conversión de texto en vídeo, 2025), (Ejemplo de rediseño de un sitio web o aplicación: El caso de AirBnB, 2025), (Ética | MIT Technology Review, 2025).

LUCAS MELGARES CARMONA 76

---

<!-- Página 82 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## 6. Proyecto - 6.1. Desarrollo de prototipos con IA

Una vez contextualizado el proyecto, justificados sus objetivos, el enfoque metodológico, la planificación temporal y los recursos necesarios, llega el momento de adentrarse en la parte práctica del trabajo. En esta sección, se materializan las ideas previamente planteadas y se concreta su aplicación a través de herramientas, técnicas y procesos reales.

En este bloque se detallará paso a paso cómo se ha llevado a cabo el desarrollo práctico del trabajo de fin de grado, desde la definición del usuario hasta la creación de los prototipos, wireframes y soluciones funcionales. Se mostrarán las decisiones de diseño tomadas, el uso de inteligencia artificial en el flujo de trabajo y cómo cada parte contribuye a la experiencia del usuario, eje central del proyecto.

Además, se incluirán capturas, enlaces y recursos visuales que permitan al lector comprender no solo los resultados, sino también el razonamiento detrás de cada elección. Esta parte no solo busca exponer un producto final, sino evidenciar el proceso de creación, iteración y validación que lo sustenta, destacando tanto los logros como las posibles limitaciones encontradas durante su ejecución.

La finalidad de esta sección es ofrecer una visión completa y transparente del desarrollo del proyecto, poniendo en valor el trabajo práctico realizado a lo largo de varios meses y aportando una perspectiva aplicada al uso de la inteligencia artificial en el diseño de experiencias de usuario.

6.1.1. Herramientas / softwares de prototipado

Se ha realizado una investigación exhaustiva para saber que apps/plataformas están en funcionamiento hoy día en las que se

5 permita crear prototipos en sus diferentes fases wireframes,

6 mockups… para así poder tener un herramienta eficiente y eficaz, en

5 Un wireframe es un diagrama visual que esboza el esqueleto de un proyecto o pieza tecnológica. 6 Un mockup es una representación visual similar a un prototipo que simula el aspecto final de un diseño. Va más allá de los wireframes y los diseños, ya que muestra los elementos de diseño reales, como los colores, tipografía y las imágenes.

LUCAS MELGARES CARMONA 77

---

<!-- Página 83 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

las exigencias que se piden para poder llevar a cabo esta parte del trabajo. A continuación, se detallan cinco de las mejores herramientas que se han podido encontrar en funcionamiento, en el que se explica en que consiste cada una, el uso de la IA, su plan de uso, sus funcionalidades principales, ventajas y e inconvenientes.

Uizard

Uizard es una plataforma de diseño de interfaces de usuario que aprovecha la inteligencia artificial para facilitar la creación rápida de wireframes y prototipos interactivos. Su característica destacada es "Autodesigner", que permite generar interfaces completas a partir de descripciones textuales, como "Página de inicio de comercio electrónico". Esto es especialmente útil para cualquier persona que busca transformar ideas en prototipos funcionales sin necesidad de habilidades avanzadas en diseño o incluso programación.

- Uso de IA: Utiliza IA para convertir descripciones textuales en wireframes y para transformar bocetos en interfaces digitales. - Disponibilidad gratuita: Consta un plan gratuito con funcionalidades limitadas. - Funcionalidades principales: Creación rápida de wireframes y prototipos interactivos, transformación de texto o bocetos en interfaces digitales, y una amplia biblioteca de componentes prediseñados. - Ventajas: Es muy intuitivo y fácil de usar, ideal para prototipos rápidos con estilos predefinidos, y permite la colaboración en tiempo real. - Inconvenientes: Las funcionalidades avanzadas requieren una suscripción de pago, y la personalización puede ser limitada en comparación con herramientas más complejas.

Visily

Visily es una herramienta de diseño de interfaces de usuario potenciada por IA, diseñada para facilitar la creación de prototipos y wireframes de alta fidelidad. Permite a los usuarios generar diseños a partir de texto, imágenes o incluso URLs de sitios existentes, lo que la

LUCAS MELGARES CARMONA 78

---

<!-- Página 84 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

convierte en una opción versátil para proyectos de comercio electrónico, como es nuestro caso.

- Uso de IA: Incorpora el uso de la IA para generar diseños desde descripciones textuales, imágenes o URLs. - Disponibilidad gratuita: Ofrece un plan gratuito con características generosas. - Funcionalidades principales: Permite la creación de prototipos interactivos, importación de diseños desde sitios web existentes, uso de plantillas específicas para comercio electrónico y colaboración en tiempo real. - Ventajas: Consta de una interfaz visual y fácil de usar, ideal para equipos que buscan colaborar en el diseño, y ofrece una amplia gama de plantillas y componentes. - Inconvenientes: Al ser relativamente nueva en el mercado, puede carecer de algunas integraciones o funcionalidades presentes en herramientas más establecidas.

Penpot

Penpot es una herramienta de diseño y prototipado de código abierto que facilita la colaboración entre diseñadores y desarrolladores. Al estar basada en estándares abiertos como SVG y CSS, permite una integración fluida entre el diseño y el código, lo que es beneficioso para proyectos que requieren una estrecha colaboración técnica.

- Uso de IA: No incorpora funcionalidades de inteligencia artificial, lo que en nuestro caso juega bastante en contra. - Disponibilidad gratuita: Es completamente gratuita y de código abierto. - Funcionalidades principales: Ofrece el diseño de interfaces, creación de prototipos interactivos, colaboración en tiempo real y exportación de código en formatos estándar. - Ventajas: Totalmente gratuita y de código abierto, favorece la colaboración entre equipos de diseño y desarrollo, y es altamente personalizable. - Inconvenientes: Al ser una herramienta emergente, puede no contar con una comunidad tan amplia o con tantas

LUCAS MELGARES CARMONA 79

---

<!-- Página 85 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

integraciones como otras herramientas más consolidadas, que en este caso se hace referencia a que carece del uso de la IA.

Figma con Plugins de IA (como Magician, Wireframe Plugin, etc.)

Figma es una plataforma de diseño colaborativo ampliamente utilizada que, mediante la incorporación de plugins de inteligencia artificial como Magician o Wireframe, amplía sus capacidades para facilitar la creación de prototipos y wireframes de manera más eficiente.

- Uso de IA: Utiliza la IA a través de plugins específicos que añaden funcionalidades basadas en IA. - Disponibilidad gratuita: Ofrece un plan gratuito que permite hasta 3 proyectos activos. - Funcionalidades principales: Diseño de interfaces, creación de prototipos interactivos, colaboración en tiempo real y una amplia biblioteca de plugins para extender funcionalidades. - Ventajas: Comunidad extensa con numerosos recursos y plugins, facilita la colaboración en equipos distribuidos, y es altamente personalizable mediante plugins. Además, en este caso, ya se ha usado esta plataforma varias veces en otros proyectos, lo que podría ser un punto muy a favor conocer la plataforma previamente a su uso. - Inconvenientes: Algunas funcionalidades avanzadas requieren suscripciones de pago, y el rendimiento puede verse afectado en proyectos muy grandes o complejos.

MockFlow

MockFlow es una herramienta enfocada en la creación rápida de wireframes y planificación de interfaces de usuario. Ofrece una variedad de componentes y plantillas que facilitan el proceso de diseño inicial de proyectos de comercio electrónico.

- Uso de IA: Cuenta con una funcionalidad llamada "Genius AI" que ayuda en la generación automática de interfaces de usuario.

LUCAS MELGARES CARMONA 80

---

<!-- Página 86 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Disponibilidad gratuita: Ofrece un plan básico gratuito con acceso a todos los paquetes de UI y plantillas. - Funcionalidades principales: Creación de wireframes, colaboración en tiempo real, acceso a una amplia biblioteca de componentes y plantillas, y generación automática de interfaces

mediante IA. - Ventajas: Ideal para las etapas iniciales de planificación de UX, interfaz intuitiva y facilita la colaboración en equipo. - Inconvenientes: Consta de limitaciones en su plan gratuito y por lo general, ofrece una menor proyección profesional, es decir, ofrece una interfaz algo básica para un diseño visual avanzado en comparación de otras herramientas o plataformas.

Websim.ai

Websim.ai es una herramienta de generación de páginas web mediante inteligencia artificial. Está especialmente, orientada a diseñadores, emprendedores y desarrolladores que deseen obtener un prototipo web funcional a partir de simples descripciones en lenguaje natural, sin tener conocimientos previos sobre ningún tipo de lenguaje de programación, destacando la rapidez y simplicidad para visualizar ideas en cuestión de segundos.

- Uso de IA: Utiliza inteligencia artificial generativa para interpretar descripciones textuales (prompts) y transformarlas automáticamente en interfaces web completas. - Disponibilidad gratuita: Ofrece un plan gratuito con un número limitado de generaciones y sin necesidad de registro en un primer uso. Sin embargo, para acceder a más funcionalidades (como edición avanzada o exportación completa del código), se requiere registro y en algunos casos, una suscripción de pago. - Funcionalidades principales: Generación automática de sitios web completos desde texto descriptivo, vista previa instantánea de páginas funcionales (no solo mockups), exportación del código HTML/CSS generado, posibilidad de editar contenido directamente sobre el resultado, diseño

LUCAS MELGARES CARMONA 81

---

<!-- Página 87 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

responsivo por defecto (adaptado a móvil y escritorio), y opción de guardar y compartir el diseño generado. - Ventajas: Tiene un interfaz minimalista y sencilla, su uso no requiere de conocimientos previos, ofrece el código de programación para continuar con el desarrollo web y ahorra mucho tiempo en las primeras fases de un proyecto. - Inconvenientes: Alta dependencia del nivel de detalle y claridad del prompt, no permite tanto nivel de control de los elementos estéticos, los diseños generados pueden ser simples o poco personalizados, y algunas opciones más avanzadas pueden estar limitadas al plan de pago.

(¿Qué es un wireframe?, 2025), (Qué es un mockup, 2025), (Uizard Review: AI Features, Use Cases, And Alternatives, 2025), (Turn product ideas into concepts instantly with GenAI, 2025), (UI design software for everyone, 2025), (Design and code beautiful products. Together., 2025), (Penpot: The open-source design tool for design and code collaboration, 2025), (Two Figma AI Plugins Every Designer Should Know, 2025), (Plans for any business size, 2025), (Websim.ai que es, 2025).

6.1.2. Definición de perfiles de usuario

En el diseño de experiencias de usuario (UX) para sitios web de comercio electrónico, la definición de perfiles de usuario es una fase fundamental. Estos perfiles nos permiten poder comprender las motivaciones, necesidades, comportamientos y expectativas de los distintos tipos de usuarios que interactúan con una plataforma como Amazon. La identificación de estos perfiles no solo facilita una mejor personalización del contenido y de las funcionalidades, sino que también permite optimizar la arquitectura de la información, el diseño visual y los flujos de navegación.

A continuación, se definen algunos de los perfiles más comunes y representativos dentro del ámbito del e-commerce, especialmente relevantes para la fase práctica del presente TFG, donde se desarrollará un prototipo basado en inteligencia artificial.

LUCAS MELGARES CARMONA 82

---

<!-- Página 88 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Para poder llevar a cabo estas user personas, se ha consultado y analizado exhaustivamente varias fuentes en las que se le proporciona al usuario ciertas “Estadísticas de mercado” sobre diferentes tipos de vendedores y compradores en Amazon, ofreciendo a la empresa todo tipo de información útil para masificar su presencia, mediante

diferentes estrategias de marketing. Las páginas que han reforzado y proporcionado este tipo de información han sido (Estadísticas del mercado de Amazon 2024, 2025) página en la que podemos encontrar estadísticas de mercado de Amazon del 2024 a nivel global, y (El 64% de los consumidores españoles de Amazon lo compra casi todo en el propio marketplace, 2025) donde podemos encontrar mayoritariamente información sobre estadísticas de mercado de Amazon en el 2022 en España.

Una vez vistas y analizadas estas páginas, se han creado cinco User

7 personasdistintas. Tres son mujeres y dos son hombres ya que como asegura la página (Estadísticas del mercado de Amazon 2024, 2025) “El 60% de los clientes de Amazon son mujeres, lo que muestra una división relativamente equitativa entre los géneros que compran en el gigante del comercio electrónico.”. También se incluyen tres perfiles de personas jóvenes debido a que tal y como asegura (El 64% de los consumidores españoles de Amazon lo compra casi todo en el propio marketplace, 2025) “Descubrimos que las personas de entre 25 y 34 años son las que compran con mayor frecuencia en Amazon.” , además de ser los perfiles que compran con más volumen por lo que estos compradores visitan Amazon en busca de inspiración, lo que significa que no tienen un producto en mente cuando realizan sus compras en línea, teniendo un perfil claro de User Persona, el comprador impulsivo y el comprador indeciso.

(Estadísticas del mercado de Amazon 2024, 2025), nos asegura que “El 62% de los compradores de marcas de Amazon afirman que el precio de los productos es la principal motivación para comprar en Amazon frente a otros minoristas.”, “El 82% de los compradores afirma

7 Personaje ficticio basado en tu cliente actual o ideal, el cual es creado con base en una investigación para identificar a los diferentes tipos de clientes que podrían usar tu servicio, producto, sitio o marca de manera similar.

LUCAS MELGARES CARMONA 83

---

<!-- Página 89 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

que el precio es un factor importante para ellos a la hora de comprar en la plataforma. La mayoría de los productos de Amazon se encuentran en el rango de precios más accesible.” y “El 41% de los usuarios en Amazon siempre lee las reseñas antes de comprar un producto en la plataforma.” Por eso se ha creado el buscador

informado.

Por último, según (Estadísticas del mercado de Amazon 2024, 2025) “Casi 9 de cada 10 compradores eligen comprar en Amazon en lugar de en otras tiendas de comercio electrónico en línea debido a las opciones de envío gratuito.” a raíz de este dato se ha creado el comprador leal para representar esa gran mayoría de usuarios recurrentes y un comprador ocasional para representar esa pequeña minoría.

User Persona - El comprador impulsivo

“Fig 35 User Persona - El comprador impulsivo”

https://www.canva.com/design/DAGktiE44As/18bMOc1g3E-sNYNIs1DJ5Q/edit

LUCAS MELGARES CARMONA 84

---

<!-- Página 90 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

User Persona - El buscador informado

“Fig 36 User Persona - El buscador informado”

https://this-person-does-not-exist.com/ca

User Persona - El usuario leal o recurrente

“Fig 37 User Persona - El usuario leal o recurrente”

https://this-person-does-not-exist.com/ca

LUCAS MELGARES CARMONA 85

---

<!-- Página 91 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

User Persona - El comprador ocasional

“Fig 38 User Persona - El comprador ocasional”

https://this-person-does-not-exist.com/ca

User Persona - El usuario indeciso

“Fig 39 User Persona - El usuario indeciso”

https://this-person-does-not-exist.com/ca

A continuación, se citan ciertos datos de estadísticas de mercado que pueden considerarse relevantes o de especial interés, en esta segunda parte práctica del trabajo. Todos estos datos y más se pueden encontrar en (Estadísticas del mercado de Amazon 2024, 2025):

- “El 33% de los compradores en Amazon afirmaron que la rapidez con la que Amazon responde a sus consultas es la mejor parte de

LUCAS MELGARES CARMONA 86

---

<!-- Página 92 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

comprar en el gigante del comercio electrónico. Esta estadística resalta la enorme importancia de utilizar chat en vivo u otras integraciones para ofrecer una experiencia de atención al cliente inigualable.”

- “Los millennials compran en Amazon el doble de veces que los baby boomers, una estadística que vale la pena tener en cuenta al definir tu público objetivo y estrategias de marketing.”

- “El 80% de los compradores de Amazon son propietarios de viviendas, lo que explica en parte la popularidad de los artículos para el hogar y los muebles en la plataforma.”

- “El 65% de los compradores en línea en Amazon prefieren utilizar la plataforma a través de su ordenador o portátil. Sin embargo, un tercio significativo de los compradores utiliza la plataforma desde el móvil, por lo que sigue siendo importante que su sitio sea apto para móviles.”

Además, es importante mencionar que todas y cada una de las características de cada User persona han sido creadas y escogidas con todos estos datos.

6.1.3. Implementación de prompts de personalización y análisis

En esta sección, junto con la del prototipado, una de las más importantes del trabajo, se abordará una de las fases más prácticas y experimentales del proyecto: la creación e implementación de prompts personalizados mediante inteligencia artificial para el diseño de interfaces de usuario en plataformas de prototipado. Esta etapa tiene como objetivo adaptar las propuestas de diseño a perfiles de usuario reales definidos en el apartado anterior, utilizando herramientas que integran IA para generar de forma rápida y visual maquetas, interfaces y experiencias adaptadas a diferentes necesidades dentro del ámbito del e-commerce y a continuación se detallarán cuáles son los prompts que se usarán o se implementarán para poder llevar a cabo el prototipado.

LUCAS MELGARES CARMONA 87

---

<!-- Página 93 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Una vez hecho el análisis de las posibles herramientas o plataformas con la que se trabajará para poder llevar a cabo esta segunda fase del TFG, explicado detalladamente en el apartado “6.1.1”, se ha decidido trabajar con tres plataformas que destacan por su accesibilidad,

funcionalidades inteligentes y enfoque visual: Uizard, Visily, MockFlow y Websim.ai. ¿Por qué vernos obligados a escoger una de ellas?, cada una ofrece distintas maneras de interactuar con la inteligencia artificial: Uizard permite transformar texto en wireframes, Visily destaca por generar interfaces desde URLs o imágenes, MockFlow integra un sistema de IA para proponer estructuras de diseño según la intención del usuario y Websim.ai se especializa en la generación automática de sitios web completos desde texto descriptivo ofreciendo un plan gratuito muy amplio. Estas herramientas permiten introducir instrucciones en lenguaje natural, es decir, los “prompts”, que se traducen automáticamente en estructuras visuales como páginas de inicio, flujos de compra, fichas de producto o páginas de usuario.

Además, para realizar de manera más efectiva esta parte práctica del trabajo, se ha hecho una búsqueda exhaustiva en diferentes páginas especializadas sobre como generar un buen prompt y poder extraer los mejores resultados posible en cada plataforma.

Para generar un prompt efectivo en herramientas de inteligencia artificial, es fundamental estructurar la solicitud de manera clara y detallada. Un buen prompt se compone de varios elementos clave que guían al modelo para producir respuestas precisas y útiles.

En primer lugar, hemos de proporcionar una instrucción clara. Se puede empezar con un verbo que indique la acción deseada, como "escribe", "genera" o "explica". Esto establece de inmediato la tarea que se espera del modelo.

En segundo lugar, hemos de proporcionar un contexto detallado. Es importante detallar información relevante que sitúe al modelo en el escenario adecuado. Por ejemplo, si se solicita una descripción de

LUCAS MELGARES CARMONA 88

---

<!-- Página 94 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

producto, hay que especificar el tipo de producto, su uso y características principales.

En tercer lugar, indicar el rol asignado. Hemos de indicar al modelo que asuma un rol específico, como "actúa como un experto en marketing digital", esto puede mejorar la relevancia y profundidad de la

respuesta.

En cuarto lugar, hemos de indicar el formato deseado. Hemos de especificar cómo deseamos que se presente la respuesta: en forma de lista, párrafo, tabla, etc. Esto ayuda a obtener resultados más alineados con nuestras necesidades.

En quinto lugar, tenemos el tono y el estilo. Hemos de proporcionarle el tono que debe adoptar la respuesta, ya sea formal, informal, técnico o amigable. Esto asegura que el contenido generado se adecúe al público objetivo.

Por último, es recomendable utilizar ejemplos o referencias. Se puede incluir ejemplos concretos o referencias puede orientar al modelo y mejorar la calidad de la respuesta.

Estas recomendaciones se basan en diversas fuentes especializadas en la creación de prompts efectivos, como IEBS School, PorContar y AcademiaSeo. Además, expertos en ingeniería de prompts han desarrollado estructuras como la fórmula REDICE (Rol, Ejemplo, Detalle, Instrucción, Contexto, Estilo) para optimizar la interacción con modelos de lenguaje.

En resumen, un prompt bien construido debe ser específico, contextualizado y estructurado, lo que facilita que la inteligencia artificial comprenda y responda de manera adecuada a las solicitudes del usuario.

(¿Cómo escribir mejores Prompts en ChatGPT?, 2025), (¿Cómo hacer Prompts para ChatGPT?, 2025), (Como escribir los mejores prompts en ChatGPT usando R.E.D.I.C.E, 2025).

LUCAS MELGARES CARMONA 89

---

<!-- Página 95 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

A continuación, se han generado distintos prompts diseñados específicamente para responder a los perfiles de usuario descritos en el apartado anterior. Cada prompt busca adaptar la experiencia de compra online a los hábitos, preferencias y comportamientos de estos perfiles, explorando cómo la IA puede facilitar la personalización visual

desde el momento mismo del diseño. En vez de generar distintos prompts para cada plataforma, se han diseñado cinco, para replicar funcionalidades clave de una web de referencia en el sector del e- commerce, Amazon. De este modo, se busca analizar qué herramienta ofrece una mayor fidelidad en la generación de páginas esenciales para una tienda online. Las cinco páginas seleccionadas para el estudio son: página de inicio (Home), página de inicio de sesión (Login), página de producto doméstico específico (Detalles de un producto), página de seguimiento de pedido (Seguimiento), y página de ayuda o contacto (Ayuda).

Una vez se han decidido las páginas que se les pedirá a las anteriores plataformas, se tendrán en cuenta el modelo que usa Amazon en cada una de estas páginas, teniendo en cuenta su composición, disposición de elementos… Estas páginas servirán como “rúbrica” para posteriormente, tener en cuenta y evaluar que plataforma es más eficaz.

“Fig 40 Página Home Amazon"

https://www.amazon.es/?&tag=hydesnav- 21&ref=pd_sl_781oit2196_e&adgrpid=152290669839&hvpone=&hvptwo=&hvadid=6722913625 54&hvpos=&hvnetw=g&hvrand=2582204976868816026&hvqmt=e&hvdev=c&hvdvcmdl=&hvloci nt=&hvlocphy=9196034&hvtargid=kwd-10573980&hydadcr=4855_2227860

LUCAS MELGARES CARMONA 90

---

<!-- Página 96 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 41 Página de Login Amazon"

https://www.amazon.es/?&tag=hydesnav- 21&ref=pd_sl_781oit2196_e&adgrpid=152290669839&hvpone=&hvptwo=&hvadid=6722913625 54&hvpos=&hvnetw=g&hvrand=2582204976868816026&hvqmt=e&hvdev=c&hvdvcmdl=&hvloci nt=&hvlocphy=9196034&hvtargid=kwd-10573980&hydadcr=4855_2227860

“Fig 42 Página de Producto específico de Amazon"

https://www.amazon.es/?&tag=hydesnav- 21&ref=pd_sl_781oit2196_e&adgrpid=152290669839&hvpone=&hvptwo=&hvadid=6722913625 54&hvpos=&hvnetw=g&hvrand=2582204976868816026&hvqmt=e&hvdev=c&hvdvcmdl=&hvloci nt=&hvlocphy=9196034&hvtargid=kwd-10573980&hydadcr=4855_2227860

LUCAS MELGARES CARMONA 91

---

<!-- Página 97 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 43 Página de Seguimiento de Amazon"

https://www.youtube.com/watch?v=4bihZmwCYlc

“Fig 44 Página de Ayuda de Amazon"

https://www.amazon.es/?&tag=hydesnav- 21&ref=pd_sl_781oit2196_e&adgrpid=152290669839&hvpone=&hvptwo=&hvadid=6722913625 54&hvpos=&hvnetw=g&hvrand=2582204976868816026&hvqmt=e&hvdev=c&hvdvcmdl=&hvloci nt=&hvlocphy=9196034&hvtargid=kwd-10573980&hydadcr=4855_2227860

Antes de realizar estos cinco prompts, se han definido diferentes características básicas de estética común, establecidas en la web que se quiere obtener como resultado:

- Colores predominantes: fondo gris claro (#f4f4f4), textos en gris oscuro (#333333), elementos interactivos en azul profundo (#003366), botones de acción principales en naranja vibrante (#ff9900). - Tipografía: Sans-serif moderna, legible, como 'Inter' o 'Open Sans'.

LUCAS MELGARES CARMONA 92

---

<!-- Página 98 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Diseño: Espaciado amplio, secciones delimitadas, navegación accesible tanto en escritorio como móvil. - Menú superior común: Logo a la izquierda, barra de búsqueda centrada, iconos de cuenta, pedidos y carrito a la derecha. Menú desplegable con categorías generales.

Se ha utilizado una estética y sobre todo estructura similar a Amazon.

A continuación, se presentan los cinco prompts que serán utilizados de manera idéntica en las tres plataformas. Con una línea visual moderna, profesional, intuitiva, centrada en usabilidad, con una paleta de colores basada en azul oscuro, gris claro y toques de naranja para botones principales, tipografía sans-serif clara y una maquetación adaptable a escritorio y móvil.

Página Home (Inicio):

- “Diseña una página principal de un e-commerce profesional con una estructura visual clara y moderna. La cabecera debe incluir: logotipo alineado a la izquierda, barra de búsqueda centrada con lupa integrada, y a la derecha iconos de usuario (cuenta), lista de deseos, carrito de compras (con contador) y ayuda. Justo debajo, coloca un menú horizontal con las siguientes categorías: Tecnología, Hogar, Moda, Belleza, Infantil y Supermercado. A continuación, crea un banner promocional a ancho completo con imagen llamativa, texto principal y botón de llamada a la acción naranja (“Descúbrelo”). Después, incluye una sección de “Ofertas Flash” con productos en carrusel horizontal, cada uno con imagen, nombre, precio original tachado, descuento, y contador de tiempo. Continúa con un bloque de “Inspirado en tus búsquedas” en formato de grid de 4 columnas. Añade también una sección de “Categorías más populares” con íconos y enlaces visuales. El pie de página debe mostrar logos de métodos de pago, política de devoluciones, atención al cliente y sello de

LUCAS MELGARES CARMONA 93

---

<!-- Página 99 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

seguridad. Aplica una estética visual consistente con fondo gris claro (#f4f4f4), textos en gris oscuro (#333333), acentos azules (#003366) en títulos y navegación, y botones de acción en naranja brillante (#ff9900). Utiliza tipografía sans-serif

moderna y asegúrate de que la página sea adaptable a dispositivos móviles.”

Página Iniciar Sesión:

- “Crea una página de inicio de sesión para un e-commerce moderno. La cabecera debe mantener el mismo diseño que la página de inicio, incluyendo logotipo, barra de búsqueda y menú simplificado. Centra un formulario de acceso sobre fondo gris claro. El formulario debe incluir los siguientes campos: correo electrónico, contraseña, casilla “Recuérdame” y botón principal naranja con texto “Iniciar sesión”. Debajo, coloca dos enlaces en texto azul: “¿Olvidaste tu contraseña?” y “Crear cuenta nueva”. A la derecha (o debajo en versión móvil), añade un recuadro con beneficios de estar registrado: acceso a historial de pedidos, guardado de productos favoritos y soporte prioritario. Aplica una estética coherente con el resto de la web: fondo gris claro (#f4f4f4), contenedor blanco con sombra sutil, botones en naranja (#ff9900), y elementos interactivos en azul profundo (#003366). Usa tipografía sans-serif clara como 'Open Sans' o 'Inter'.”

Página Producto en específico (Producto doméstico):

- “Diseña una página de producto para una cafetera automática de gama media. Incluye una barra de navegación superior con logotipo, búsqueda, cuenta y carrito, igual al resto de páginas. Justo debajo, coloca una ruta de navegación tipo “Inicio > Hogar > Cocina > Cafeteras”. Divide la página en dos columnas: o Izquierda: galería con imagen principal grande y miniaturas clicables debajo.

LUCAS MELGARES CARMONA 94

---

<!-- Página 100 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

o Derecha: nombre del producto, marca, puntuación (estrellas y nº de valoraciones), precio original y final con descuento, selector de cantidad, botones “Añadir al carrito” (naranja) y “Comprar ahora” (azul).

o Debajo, añade secciones: Descripción del producto (expandible). Especificaciones técnicas (tabla detallada). Opiniones de clientes (con filtros y fotos de usuarios). Productos relacionados (carrusel

horizontal)

Mantén la estética uniforme: fondo gris claro (#f4f4f4), textos en gris oscuro (#333333), botones naranjas (#ff9900), títulos en azul profundo (#003366) y tipografía sans-serif. El diseño debe ser limpio, estructurado y accesible desde móvil.”

Página Seguimiento de Pedido:

- “Diseña una página de seguimiento de pedido para una tienda online con diseño visual y moderno. En la parte superior incluye logotipo, barra de búsqueda y menú como en las demás páginas. Muestra la información del pedido con número, producto adquirido, fecha y resumen de pago. En el centro de la pantalla, crea una línea de progreso horizontal con cinco estados: “Pedido recibido”, “Preparando”, “Enviado”, “En reparto”, “Entregado”. Cada paso debe estar marcado con íconos y cambiar de color según el estado (gris pendiente, verde completado, azul actual). A la derecha, incluye bloque con: dirección de envío, transportista, estimación de llegada, número de seguimiento (con opción de copiar). Debajo, añade botón azul “Contactar con soporte” y texto de ayuda útil (enlaces a política de devoluciones o preguntas frecuentes). Estética coherente: fondo gris claro (#f4f4f4), títulos en azul

LUCAS MELGARES CARMONA 95

---

<!-- Página 101 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

(#003366), textos grises, botones naranja (#ff9900) y tipografía sans-serif legible.”

Página Ayuda o Contacto:

- “Crea una página de ayuda/contacto para una tienda online. Muestra primero un buscador central con texto sugerido:

“¿En qué podemos ayudarte?”. Debajo, organiza una sección de preguntas frecuentes en bloques con iconos: “Pedidos y entregas”, “Devoluciones”, “Cuenta”, “Pagos y facturas”. Cada bloque debe ser clicable y desplegable. A continuación, añade un formulario de contacto con los campos: nombre, email, tipo de consulta (menú desplegable) y mensaje. Incluir botón naranja “Enviar”. Añade una sección con datos de contacto directo: número de teléfono, email, y acceso al chat en vivo (ícono visible). Al final, muestra estimación de tiempos de respuesta y frase tipo “Estamos aquí para ayudarte”. Diseño limpio, con fondo gris claro, secciones blancas con sombra suave, textos en gris oscuro, botones en naranja (#ff9900), acentos azules (#003366) y tipografía sin serifa.”

Estos prompts son el resultado de una reflexión estratégica que cruza las posibilidades de la inteligencia artificial en herramientas de prototipado con perfiles de usuarios reales y comunes en sitios como Amazon. En las siguientes secciones se detallará cómo han sido implementados estos prompts en cada plataforma, se analizarán los resultados visuales obtenidos, y se valorará cómo cada herramienta ha respondido a las necesidades específicas de los distintos tipos de usuarios definidos. Esta fase servirá para valorar la capacidad real de personalización de la IA en entornos de diseño UX y ofrecer conclusiones aplicables al desarrollo de productos digitales más adaptados a sus usuarios.

(Qué es una landing page, para qué sirve y qué tipos existen, 2025)

LUCAS MELGARES CARMONA 96

---

<!-- Página 102 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

6.1.4. Diseño de un prototipo de UI impulsado por IA

Para realizar esta prueba inicial de prototipado, se ha decidido utilizar la página de inicio (Home) como referencia común en las tres plataformas seleccionadas. La elección de la página de inicio (Home) se considera adecuada ya que representa el punto de entrada principal de cualquier aplicación o sitio web, tanto de e-commerce como de cualquier otro sector, y suele concentrar los elementos clave de navegación, jerarquía visual, mensaje principal de la marca y primeros puntos de interacción del usuario. Esto la convierte en una excelente base para analizar cómo cada herramienta de diseño con IA interpreta y genera soluciones a nivel visual y funcional. En todas las plataformas se utilizará el mismo prompt definido previamente para la Home, garantizando así una comparativa justa.

Una vez obtenidos los resultados generados por las tres herramientas, se realizará un análisis en términos de experiencia de usuario (UX) para valorar cuál de los diseños resulta más exitoso en cuanto a claridad, usabilidad, estética y efectividad comunicativa.

Uizard:

Una vez el usuario se ha registrado, se le ofrece los planes que ofrece la plataforma. En este caso, para realizar la parte práctica del proyecto, se intentará permanecer en las cuatro plataformas en el “Plan free” o versión gratuita y posteriormente, si es necesario, se ampliará asumiendo la tarifa que sea necesaria.

LUCAS MELGARES CARMONA 97

---

<!-- Página 103 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 45 Planes de Uizard"

A continuación, se realizan una serie de preguntas con unas respuestas predeterminadas por la plataforma al usuario, para saber qué tipo de rol ejercerá en la plataforma o cual es el objetivo al que se quiere llegar. Para el proyecto, se ha seleccionado el rol de consultor de UX/UI, con el fin de poder crear un nuevo proyecto web en desktop.

Una vez se crea el proyecto, se le pedirá que indique con que finalidad está creando ese proyecto, es decir, donde se visualizará: “Desktop”, “Tablet” o “Movile”. A continuación, se creará de forma automática el lienzo que se haya escogido para el proyecto y se le dará la bienvenida, junto con un pequeño tutorial con los pasos a seguir. Además, el usuario podrá encontrar situado centrado en la parte inferior, un chat

8 de IA con un placeholder: “¿Le puedo ayudar en algo?”.

8 Texto genérico que sirve para sustituir temporalmente un texto permanente u ocupar espacio en un elemento de contenido.

LUCAS MELGARES CARMONA 98

---

<!-- Página 104 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 46 Interfaz Uizard"

Una vez se incia el chat con la IA, se abre un pop-up o ventana emergente en el que se muestra: que tipo de motor de IA se está utilizando y diferentes funcionalidades (iniciar un nuevo chat, ver el historial…), además de mostrar la conversación que se va a tener. Utiliza una apariencia de colores oscuros, similar a cualquier plataformas o app de mensajes, con la que hoy día cualquier persona ya está familiarizada, como Whatsapp, Telegram, Messenger… dándo directamente la bienvenida con el siguiente mensaje: “¡Hola! ¿Qué acción te gustaría realizar?”, con cuatro opciones de respuestas predeterminadas, “Modificar selección”, “Generar pantallas”, “Generar Imágenes” y “Generar Temas”.

Una vez clara la respuesta, se mostrará un mensaje en el que se pedirá que se especifique cual es el objetivo a cumplir. En este caso, para poder realizar la parte práctica del trabajo, se ha seleccionado la opción de “Generar pantallas”, en la que se le enviará el prompt que define la página que se quiere generar.

En este caso se le pedirá que realice la página de inicio (Home), ja que como se ha justificado anteriormente, representa el punto de entrada inicial de cualquier aplicación.

LUCAS MELGARES CARMONA 99

---

<!-- Página 105 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 47 Chat con la IA"

Una vez el usuario ha contestado las preguntas pertinentes, se le va a describir todos los detalles del diseño de la página, o lo que es lo mismo, se le proporcionará el prompt en el que se describe todas las características principales: colores, funcionalidades, estética, organización de los banners… con todo lujo de detalles.

LUCAS MELGARES CARMONA 100

---

<!-- Página 106 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 48 Prototipo de Uizard"

A continuación, se realizará el mismo procedimiento para las otras tres plataformas, se evaluarán los resultados y se decidirá que cual de ellas se adecua mejor a los objetivos que se le han proporcionado.

Visily:

Una vez el usuario se ha registrado, al contrario que en la plataforma anterior, no se le proporcionará ningún tipo de plan, ni ninguna información sobre lo que tiene o no disponible. Al introducir el correo electrónico para hacer el proceso de registro, ofrece diferentes “workspaces” o espacios de trabajo de usuarios registrados, destacando su funcionalidad principal definida en el apartado 6.1.1, permitiendo la creación de prototipos interactivos y colaboración en tiempo real.

LUCAS MELGARES CARMONA 101

---

<!-- Página 107 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

De igual modo que la plataforma Uizard, en este caso, también se le harán ciertas preguntas al usuario cuando haya realizado el proceso de registro, preguntas como: ¿Qué rol desempeñará?, ¿Cómo ha conocido la herramienta? y ¿Qué uso le dará?

Una vez finalizado este proceso inicial, se crea un espacio de trabajo de manera automática en el que, se ofrece tres opciones para empezar el proyecto. La primera opción es crear Wireframes a partir de templates ya creadas o disponibles en la plataforma, usar una plantilla de un diagrama para esa primera fase de todo proyecto en la que se generan múltiples ideas (brainstorming), o empezar desde cero.

“Fig 49 Opciones para empezar un proyecto"

Una vez el usuario ha seleccionado cuál de las opciones es la que mejor se adecua a él, se le proporciona un espacio de trabajo en blanco, con todas las herramientas disponibles para poder desarrollar el proyecto. Para poder realizar la parte práctica de este trabajo, la opción que se ha seleccionado ha sido “Start from scratch” o empezar desde cero, y así poder ver que prototipado o wireframe es capaz de desarrollar de manera más eficiente en términos de UX la página de inicio (Home).

LUCAS MELGARES CARMONA 102

---

<!-- Página 108 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 50 Espacio de trabajo Visily"

A continuación, una vez se haya familiarizado con la interfaz, se accederá a la consola de prompts o al chat con la IA, situado en la parte inferior derecha. Una vez dentro, se proporcionará diferentes maneras de empezar, ya sea a través a de una imagen, texto, modificar un diseño ya existente, generar un diagrama… y a partir de la opción escogida la plataforma empezará a elaborar el proyecto.

“Fig 51 Consola de Prompts de Visily"

Antes de poder pasar cualquier parámetro, la plataforma, al igual que en el caso anterior de Uizard, realiza diferentes preguntas para saber cómo es el prototipado que tiene que llevar a cabo, para que dispositivo

LUCAS MELGARES CARMONA 103

---

<!-- Página 109 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

será o si se quiere generar toda una página web de e-commerce o una pantalla en específico. Una vez escogidas estas opciones, se le proporciona nuestro prompt de página de inicio (Home) y posteriormente se evaluará junto con los demás resultados de las diferentes plataformas.

“Fig 52 Prototipo 01 Visily"

LUCAS MELGARES CARMONA 104

---

<!-- Página 110 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 53 Prototipo 02 Visily"

MockFlow:

En esta plataforma, al entrar, al igual que en el caso de Uizard se proporciona información sobre los diferentes planes que ofrece y que es lo que permite cada uno de ellos. Una vez el usuario se haya registrado, entra dentro de la interfaz en la que se le ofrecen dos opciones.

La primera es crear un wireframe, a partir de plantillas, imágenes, IA… y la segunda es un ideaboard o un muro de ideas. Como en los anteriores casos, para poder desarrollar la parte práctica del proyecto, se seleccionará la opción de crear un prototipo a partir de IA, en el que se le proporcionará el prompt de la página de inicio (Home).

LUCAS MELGARES CARMONA 105

---

<!-- Página 111 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 54 Espacio de trabajo de MockFlow"

A partir de la opción de generar un wireframe con IA, se abre la consola de prompts en la que se le proporciona la descripción de la página de inicio. Además, el usuario puede encontrar diferentes posibles prompts que pueden encajar con su objetivo.

“Fig 55 Consola de prompts MockFlow"

Como resultado de prototipado se ha obtenido el siguiente:

LUCAS MELGARES CARMONA 106

---

<!-- Página 112 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 56 Prototipo 01 MockFlow"

“Fig 57 Prototipo 02 MockFlow"

Websim.ai:

Por último, también se realizará este mismo proceso para Websim.ai. Una web con una estética centrada en la productividad y la simplicidad, ideal para el desarrollo rápido de prototipos funcionales sin sobrecargar

LUCAS MELGARES CARMONA 107

---

<!-- Página 113 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

al usuario con configuraciones visuales. Llama la atención su estética, simulando una especie de buscador como Google o Chrome, en el que predomina la consola de prompts anclada en la parte superior y mostrando diferentes proyectos que la plataforma ofrece para el usuario.

“Fig 58 Interfaz Websim.ai"

Una vez el usuario se ha registrado y tiene acceso total a la plataforma, en la consola de prompts, se le proporciona la opción de escoger el tipo

de motor de IA que quiere para llevar a cabo su petición. Para llevar a acabo el prototipo, se ha seleccionado el motor de IA “GPT-4.1”, un motor de IA creado por la empresa OpenAI con múltiples mejoras respecto a sus modelos anteriores u otros motores, ofreciendo mejoras de comprensión de contextos extensos, entre otras muchas otras características.

“Fig 59 Consola de Prompts de Websim.ai"

A continuación, se muestra cual ha sido el resultado obtenido:

LUCAS MELGARES CARMONA 108

---

<!-- Página 114 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 60 Prototipo 01 Websim.ai"

“Fig 61 Prototipo 02 Websim.ai"

“Fig 62 Prototipo 03 Websim.ai"

“Fig 63 Prototipo 04 Websim.ai"

LUCAS MELGARES CARMONA 109

---

<!-- Página 115 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- 6.2. Evaluación del impacto de la IA en UX

En este apartado, se encuentra el análisis de los resultados obtenidos en el apartado anterior mediante las diferentes plataformas. El análisis se realiza siguiendo la “Guía de Evaluación Heurística de Sitios Web" de Hassan Montero Yusef y Martín Fernández Francisco J. Una guía centrada en evaluar la usabilidad y experiencia de usuario (UX), a través de diez principios heurísticos específicos que se detallan en la siguiente página, (Guía de Evaluación Heurística de Sitios Web, 2025), y que se definen a continuación.

1. Visibilidad del estado del sistema: En este criterio, el usuario debe estar siempre informado de lo que está ocurriendo en la página web.

2. Correspondencia entre el sistema y el mundo real: Se centra en enfatizar que el sistema debe hablar el lenguaje del usuario. 3. Control y libertad del usuario: El usuario debe poder deshacer o rehacer acciones. 4. Consistencia y estándares: Debe mantener uniformidad en los elementos y comportamientos. 5. Prevención de errores: Se debe minimizar la ocurrencia de errores y ayudar a corregirlos de la forma más eficiente posible. 6. Reconocimiento mejor que recuerdo: Los elementos deben ser visibles y fáciles de identificar. 7. Flexibilidad y eficiencia de uso: Debe permitir atajos para usuarios expertos. 8. Estética y diseño minimalista: Se ha de evitar información innecesaria. 9. Ayudar a los usuarios a reconocer, diagnosticar y recuperarse de errores: Debe proporcionar mensajes claros y soluciones propuestas. 10. Ayuda y documentación: Se ha de proveer asistencia cuando sea necesario.

Al realizar la búsqueda exhaustiva que criterios, se han de tener en cuenta a la hora de hacer una evaluación heurística de sitios webs, también se ha encontrado otra guía muy reconocida en el ámbito de usabilidad web, la de Jacob Nielsen. Una guía ideal para proyectos que buscan apegarse a estándares globales de usabilidad o cuando se necesita una evaluación rápida pero efectiva. En el caso de Hassan Montero y Martín Fernández, se centra en

LUCAS MELGARES CARMONA 110

---

<!-- Página 116 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

una guía heurística adaptada más detallada y contextualizada, con criterios más actuales, perfectas para auditorías completas, académicas o profesionales, donde se requiere mayor profundidad y una visión integral del sitio web.

A continuación, también se incluye un análisis hecho bajo los criterios de Jacob Nielsen detallados en las siguientes páginas, (Análisis Heurístico para UX: evalua la usabilidad de tu web, 2025) y (10 reglas heurísticas de Nielsen y cómo aplicarlas, 2025), y que se definen a continuación.

1. Visibilidad del estado del sistema: Este principio establece que el usuario siempre debe estar informado sobre lo que está ocurriendo. 2. Correspondencia entre el sistema y el mundo real: El sistema debe hablar el lenguaje del usuario, utilizando palabras y conceptos familiares, o con los que el usuario ya esté familiarizado. 3. Control y libertad del usuario: Los usuarios necesitan opciones para deshacer o rehacer acciones. 4. Consistencia y estándares: Los elementos deben mantenerse uniformes y seguir las convenciones del entorno. 5. Prevención de errores: El sistema debe ayudar a los usuarios a evitar errores. 6. Reconocimiento mejor que recuerdo: Los elementos deben ser visibles y fácilmente reconocibles. 7. Flexibilidad y eficiencia de uso: Se deben proporcionar atajos y opciones avanzadas para usuarios experimentados. 8. Estética y diseño minimalista: El diseño debe ser claro y sin información innecesaria. 9. Ayudar a reconocer, diagnosticar y recuperarse de errores: Los mensajes de error deben ser claros y ofrecer soluciones.

10. Ayuda y documentación: Se debe proveer asistencia siempre que sea necesario.

Al realizar estos dos análisis se obtendrá un estudio contrastado con numerosos resultados para ver si se coincide en la conclusión final sobre cuál es la plataforma que proporciona el mejor prototipado hecho con IA, respetando los criterios de UX.

LUCAS MELGARES CARMONA 111

---

<!-- Página 117 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

6.2.1. Evaluación Heurística utilizando heurísticas de Hassan Montero y Yusef

6.2.1.1 Uizard

Visibilidad del Estado del Sistema:

- Encabezado: o Elementos: Logo, barra de búsqueda, menú de categorías (Tecnología, Hogar, Moda, Belleza, Infantil, Supermercado). o Análisis: El encabezado está fijo en la parte superior, proporcionando un acceso constante a las secciones principales, lo cual es positivo en términos de visibilidad. o Botones: El icono de búsqueda es reconocible y fácilmente accesible. Sin embargo, podría beneficiarse de un “Placeholder” o pequeño texto que indique "Buscar" para mayor claridad. - Banner de Promoción Especial: o Botón "Descúbrelo": Tamaño adecuado, color naranja vibrante que contrasta con el fondo oscuro. Al ser el elemento central, cumple su función de captar la atención. o Análisis: La oferta especial es visible de inmediato al cargar la página, lo cual es coherente con el objetivo de resaltar promociones. - Ofertas Destello: o Botones en cada tarjeta: No hay botones explícitos en las tarjetas de productos. Esto puede ser confuso para usuarios menos familiarizados con interfaces de e- commerce. En este caso, es recomendable, proporcionar un prompt específico para incluir un botón claro como "Comprar ahora" o "Ver detalles" en cada una de estas tarjetas. - Pie de Página: o Elementos: Acceso a políticas de devoluciones, métodos de pago, contacto.

LUCAS MELGARES CARMONA 112

---

<!-- Página 118 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

o Análisis: Buena visibilidad, aunque los íconos de categorías podrían beneficiarse de etiquetas adicionales para mejorar el reconocimiento.

Correspondencia entre el Sistema y el Mundo Real:

- Lenguaje Natural: o Uso de términos como "Ofertas Destello" y "Inspirado en tus búsquedas" es adecuado y cercano al usuario. - Iconografía: o El uso de iconos en las categorías facilita la identificación. Sin embargo, algunos iconos pueden ser ambiguos, como es el caso de “Belleza” o el icono de "Moda" que podría ser más específico.

Control y Libertad del Usuario:

- Navegación Fija: o El menú superior siempre visible permite cambiar de sección fácilmente. - Falta de Opciones para Deshacer: o No hay botones para eliminar productos del carrito o deshacer acciones, lo cual limita el control del usuario.

Consistencia y Estándares:

- Diseño de Tarjetas: o Los productos en "Ofertas Destello" tienen un diseño homogéneo. Esto ayuda a mantener una estética uniforme. - Botones: o El botón "Descúbrelo" sigue un estilo común en la interfaz, pero se podría mejorar la consistencia añadiendo botones similares en otras secciones, como en la sección de “Ofertas destello” o “Inspirado en tus búsquedas”, reforzando el estilo común de la interfaz.

Prevención de Errores:

- Mensajes de Advertencia:

LUCAS MELGARES CARMONA 113

---

<!-- Página 119 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

o No hay confirmación al realizar acciones importantes (como agregar al carrito), lo que podría generar errores indeseados.

Reconocimiento Mejor que Recuerdo:

- Iconos Claros: o Las categorías están bien representadas, pero algunas como "Belleza" pueden ser interpretadas de manera ambigua. - Productos Inspirados: o Al estar ubicados bajo las ofertas, el usuario reconoce el patrón de navegación rápidamente.

Flexibilidad y Eficiencia de Uso:

- Accesos Rápidos: o El pie de página ofrece accesos rápidos a secciones clave, pero la falta de botones de acción rápida en productos limita la eficiencia.

Estética y Diseño Minimalista:

- Colores: o El uso de tonos oscuros con acentos naranjas crea un contraste visual atractivo. - Tipografía: o Clara y legible, con tamaños adecuados para cada sección. - Distribución: o El diseño modular permite identificar secciones de forma rápida, evitando la saturación.

Ayuda a Reconocer y Corregir Errores:

- Mensajes de Error: o No hay mensajes claros cuando el usuario realiza una acción errónea, por ejemplo: Si un producto ya está en el carrito, no hay advertencia de duplicación.

Ayuda y Documentación:

LUCAS MELGARES CARMONA 114

---

<!-- Página 120 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Asistencia:

o No hay tutoriales o guías para nuevos usuarios, lo que podría ser útil para compradores ocasionales.

En definitiva, en el caso de Uizard, el diseño cumple parcialmente con el prompt de inicio definido. Las promociones están bien destacadas, pero la falta de botones claros en las tarjetas limita la interacción. Además, la ausencia de opciones de deshacer resta, puntos de usabilidad.

6.2.1.2 Visily

Visibilidad del Estado del Sistema:

- Encabezado: o El logo y el menú superior permanecen visibles durante la navegación. o Botón "Shop Now" está claramente destacado en el banner, invita a la acción inmediata. - Productos Destacados: o Cada tarjeta tiene un botón de acción "Comprar Ahora", que está claramente identificado con un color naranja que resalta.

Correspondencia entre el Sistema y el Mundo Real:

- Lenguaje Amigable: o Usa términos comunes en e-commerce ("Save Big Today!", "Ofertas Flash"), lo cual facilita el entendimiento. - Imágenes Atractivas: o Los productos muestran imágenes de calidad que aumentan el reconocimiento visual.

Control y Libertad del Usuario:

- Deshacer y Rehacer: o No hay una clara opción para deshacer acciones, lo que puede frustrar al usuario.

LUCAS MELGARES CARMONA 115

---

<!-- Página 121 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Consistencia y Estándares:

- Botones: o El diseño uniforme de los botones facilita la identificación. - Estilo Visual: o El uso de colores consistentes en toda la interfaz mantiene una experiencia unificada.

Prevención de Errores:

- Alertas: o No hay mensajes para evitar duplicados al agregar productos al carrito.

Reconocimiento Mejor que Recuerdo:

- Íconos Claros: o Las categorías están bien diferenciadas con íconos intuitivos. - Acceso Directo: o Los botones de compra están claramente visibles en cada producto.

Flexibilidad y Eficiencia de Uso:

- Atajos Visuales: o El menú fijo y los botones rápidos facilitan el uso frecuente.

Estética y Diseño Minimalista:

- Limpieza Visual: o La interfaz es moderna y clara, con suficiente espacio en blanco para evitar saturación.

Ayuda a Reconocer y Corregir Errores:

- Mensajes de Confirmación: o Faltan avisos antes de completar acciones importantes.

Ayuda y Documentación:

LUCAS MELGARES CARMONA 116

---

<!-- Página 122 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Ausencia de Guías:

o No hay tutoriales o indicaciones rápidas.

En definitiva, en el caso de Visily el diseño cumple en gran medida con el prompt de página de inicio definido previamente, destacando especialmente en su estructura clara y organizada, promociones visibles bien ubicadas, botones de acción intuitivos a la par que llamativos, personalización mediante recomendaciones y una

navegación eficiente gracias al menú fijo.

6.2.1.3 Mockflow

Visibilidad del Estado del Sistema:

- Encabezado: o Elementos: Logo, barra de búsqueda, menú de categorías (Ofertas Flash, Recomendaciones, Inspirado en tus búsquedas). o Botón de búsqueda: El botón es pequeño y algo oscuro, lo que lo hace menos llamativo. Un icono más grande y en color contrastante mejoraría su visibilidad. o Menú Fijo: Se mantiene fijo al desplazarse, lo que permite acceder siempre a las categorías principales, pero aun así, la falta de resaltado en la categoría activa reduce la percepción de contexto. - Sección de Ofertas Flash: o Tarjetas de Producto: Cada tarjeta incluye una imagen, el nombre del producto y el precio, pero carece de un botón de acción directo como "Comprar" o "Ver detalles", generando dudas sobre cómo proceder para interactuar con los productos. - Pie de Página: o Contenido: Información de contacto y accesos rápidos a categorías. o Visibilidad: Es claro, pero el tamaño de la fuente es pequeño, lo que puede dificultar su lectura.

Correspondencia entre el Sistema y el Mundo Real:

LUCAS MELGARES CARMONA 117

---

<!-- Página 123 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Lenguaje Amigable: o Utiliza términos habituales como "Ofertas Flash" y "Inspirado en tus búsquedas", lo que resulta familiar para el usuario. - Inconsistencia Visual:

o Algunas categorías no están acompañadas de iconos, lo que rompe con la lógica visual de otros elementos.

Control y Libertad del Usuario:

- Navegación: o El menú fijo permite moverse entre secciones, pero el diseño compacto puede dificultar el acceso rápido. - Falta de Opciones para Deshacer: o No hay botones para deshacer acciones, como eliminar productos del carrito o cancelar una compra.

Consistencia y Estándares:

- Estilo de Tarjetas: o Aunque las tarjetas de productos mantienen un formato uniforme, los botones y textos varían en estilo según la sección. - Botones: o No hay botones específicos para añadir productos al carrito desde la vista principal, lo que contradice las prácticas comunes de e-commerce.

Prevención de Errores:

- Sin Confirmación: o Al agregar productos al carrito, no se muestra un mensaje de éxito o advertencia, lo que podría generar confusión.

Reconocimiento Mejor que Recuerdo:

- Iconos en el Menú:

LUCAS MELGARES CARMONA 118

---

<!-- Página 124 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

o La falta de iconos hace que el usuario dependa exclusivamente del texto, lo que puede aumentar la carga cognitiva. - Ofertas Flash: o No hay indicadores visuales claros que muestren la

duración o el estado de la oferta.

Flexibilidad y Eficiencia de Uso:

- Navegación entre Secciones: o El usuario debe desplazarse bastante para llegar a ciertas categorías, lo que reduce la eficiencia. - Atajos: o No hay atajos visibles o accesos rápidos a ofertas destacadas.

Estética y Diseño Minimalista:

- Colores: o El uso de tonos oscuros hace que el diseño se vea algo anticuado. - Tipografía: o Los textos son pequeños y el interlineado es reducido, lo que da una impresión de compresión visual. - Distribución: o Los elementos están muy agrupados, lo que genera una sensación de saturación.

Ayudar a Reconocer y Corregir Errores:

- Mensajes de Error: o No se observan mensajes que guíen al usuario en caso de acciones erróneas o repetitivas.

Ayuda y Documentación:

- Ausencia de Ayuda: o No se encuentran secciones de ayuda o guías integradas en la interfaz.

LUCAS MELGARES CARMONA 119

---

<!-- Página 125 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

El diseño de Mockflow, por ahora, es el que menos sigue de manera efectiva el prompt definido. La falta de botones claros en las tarjetas y la organización visual rígida dificultan la experiencia de navegación. Además, el aspecto visual es poco atractivo en comparación con otros diseños.

6.2.1.4 Websim.ai

Visibilidad del Estado del Sistema:

- Encabezado: o Elementos: Logo, menú principal con categorías (Ofertas, Nuevos Productos, Recomendados). o Botones de Acción: El botón de "Ver Más" es pequeño y poco destacado, sería necesario mediante un prompt específico, cambiarlo a un tamaño mayor y con un color más llamativo mejoraría la visibilidad. o Menú Fijo: No se mantiene fijo al desplazarse, lo que obliga al usuario a volver arriba para cambiar de sección. - Sección de Ofertas: o Tarjetas: Cada tarjeta tiene un botón de "Comprar" claramente identificado con un color azul. El contraste es adecuado y facilita la interacción. o Descripciones: El nombre del producto está en negrita, lo cual es útil, pero el precio en un tono más claro reduce su impacto visual. - Pie de Página: o Contenido: Enlaces a políticas, métodos de pago y redes sociales. o Visibilidad: La disposición clara y el uso de íconos son adecuados.

Correspondencia entre el Sistema y el Mundo Real:

- Lenguaje Comercial: o Utiliza términos comerciales estándar, como "Grandes Ofertas" y "Recomendados para Ti" con los que el usuario ya está familiarizado.

LUCAS MELGARES CARMONA 120

---

<!-- Página 126 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Iconografía: o Los íconos de redes sociales en el pie de página son reconocibles y están bien integrados.

Control y Libertad del Usuario:

- Botón de Regreso: o No hay un botón de "Inicio" visible en la navegación. Esto puede confundir al usuario al explorar diferentes secciones. - Eliminar Productos: o No se encuentran opciones para eliminar productos desde la pantalla principal.

Consistencia y Estándares:

- Estilo de Botones: o Los botones "Comprar" tienen el mismo estilo en todas las tarjetas, lo que facilita la identificación. - Fuentes: o El tamaño de la fuente varía según la sección, lo que puede generar inconsistencia.

Prevención de Errores:

- Sin Confirmación: o No hay mensajes de advertencia al agregar un producto al carrito.

Reconocimiento Mejor que Recuerdo:

- Iconos del Menú: o La falta de íconos en el menú principal puede hacer que el usuario tenga que memorizar las categorías.

Flexibilidad y Eficiencia de Uso:

- Navegación Larga: o El usuario necesita desplazarse bastante para encontrar productos específicos. - Atajos:

LUCAS MELGARES CARMONA 121

---

<!-- Página 127 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

o No hay enlaces rápidos a ofertas destacadas.

Estética y Diseño Minimalista:

- Colores: o Uso adecuado de tonos azules y blancos, que dan un aspecto limpio. - Tipografía: o Claridad en los títulos, pero los textos secundarios pueden ser difíciles de leer debido al contraste bajo.

Ayudar a Reconocer y Corregir Errores:

- Mensajes de Error: o No hay mensajes que guíen al usuario ante problemas comunes.

Ayuda y Documentación:

- Ausencia de Guía: o No se incluye ninguna documentación o tutorial interactivo.

En definitiva, en el caso de Websim.ai, aunque el prototipo cumple parcialmente con el prompt al mostrar productos destacados, la falta de navegación fija y los botones pequeños afectan negativamente a la experiencia del usuario.

6.2.2. Evaluación Heurística utilizando heurísticas de Jacob Nielsen

6.2.2.1 Uizard

Visibilidad del Estado del Sistema:

- Encabezado Fijo: o El logo, el menú de categorías y la barra de búsqueda permanecen visibles durante el desplazamiento. - Indicador de Ofertas: o El banner promocional con el botón "Descúbrelo" es claramente visible al cargar la página.

LUCAS MELGARES CARMONA 122

---

<!-- Página 128 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Mejora: o Sería necesario proporcionar un prompt para añadir un indicador visual para mostrar el estado de acciones como "Producto añadido al carrito".

Correspondencia entre el Sistema y el Mundo Real:

- Lenguaje Natural: o El uso de palabras como "Promoción Especial" y "Ofertas Destello" coincide con el lenguaje común

del comercio electrónico o de las páginas de e- commerce. - Íconos de Categorías: o Los iconos son reconocibles, aunque algunos pueden ser más específicos, por ejemplo, el icono de moda podría ser más claro.

Control y Libertad del Usuario:

- Falta de Botones de Deshacer: o No hay opciones para cancelar o revertir la acción de añadir productos al carrito, o por lo menos de forma visible en la página de inicio (Home). - Navegación Fija: o El menú superior permanece accesible en todo momento.

Consistencia y Estándares:

- Diseño Homogéneo: o El uso de colores naranjas y azules mantiene una coherencia visual. - Botones de Acción: o El botón "Descúbrelo" y otros botones siguen el mismo estilo, lo que facilita el reconocimiento.

Prevención de Errores:

- Falta de Confirmación:

LUCAS MELGARES CARMONA 123

---

<!-- Página 129 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

o No hay mensajes al añadir productos al carrito, lo que podría generar duplicados.

Reconocimiento Mejor que Recuerdo:

- Menú Superior Fijo: o El usuario siempre tiene acceso a las categorías, lo que facilita el reconocimiento. - Tarjetas de Productos: o Cada tarjeta sigue el mismo formato, lo que refuerza

el reconocimiento visual.

Flexibilidad y Eficiencia de Uso:

- Búsqueda Rápida: o La barra de búsqueda accesible permite encontrar productos de forma eficiente. - Falta de Atajos: o No hay accesos rápidos para ir directamente a las ofertas destacadas.

Estética y Diseño Minimalista:

- Uso de Espacios en Blanco: o El diseño no está saturado y las secciones están bien delimitadas. - Colores Vibrantes: o El contraste entre el fondo oscuro y los botones naranjas destaca sin ser agresivo.

Ayudar a Reconocer y Recuperarse de Errores:

- Mensajes de Error: o No hay mensajes claros al realizar acciones incorrectas o duplicadas.

Ayuda y Documentación:

- Ausencia de Tutoriales:

LUCAS MELGARES CARMONA 124

---

<!-- Página 130 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

o No hay guías rápidas o documentación visible.

En definitiva, en el caso de Uizard, el diseño cumple parcialmente con el prompt de inicio definido. En él, encontramos promociones destacadas, pero se hace notable la falta de botones de acceso directo en las tarjetas, además de la

ausencia de opciones de deshacer acciones, como en el carrito, resta puntos de usabilidad.

6.2.2.2 Visily

Visibilidad del Estado del Sistema:

- Encabezado y Menú Fijo: o Encontramos el menú siempre visible, lo que mantiene al usuario orientado. - Banner Promocional: o El botón "Shop Now" es grande y de color naranja, lo que garantiza visibilidad.

Correspondencia entre el Sistema y el Mundo Real:

- Lenguaje Familiar: o Se usan términos como "Ofertas Flash" y "Recomendado para Ti", términos claros y relevantes. - Íconos de Categorías: o Los iconos son claros y están bien distribuidos.

Control y Libertad del Usuario:

- Botones Claros: o Cada producto tiene un botón de compra directo. - Falta de Deshacer: o No hay forma de eliminar productos del carrito directamente desde la vista principal.

Consistencia y Estándares:

- Diseño Uniforme:

LUCAS MELGARES CARMONA 125

---

<!-- Página 131 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

o Los botones de acción y las tarjetas mantienen el mismo formato visual. - Estilo de Tipografía: o Tipografía clara y consistente en todo el diseño.

Prevención de Errores:

- Sin Mensajes de Confirmación: o No hay mensajes de éxito al añadir productos.

Reconocimiento Mejor que Recuerdo:

- Botones Consistentes: o El uso repetido de botones "Comprar ahora" refuerza el reconocimiento. - Íconos Identificables: o El menú superior tiene iconos que facilitan el acceso.

Flexibilidad y Eficiencia de Uso:

- Atajos Visuales: o Las secciones de productos destacados están accesibles de inmediato.

Estética y Diseño Minimalista:

- Diseño Limpio: o El uso de colores claros y contrastes suaves garantiza un aspecto moderno. - Tipografía Clara: o Se usa un tamaño adecuado y jerarquía bien marcada.

Ayudar a Reconocer y Recuperarse de Errores:

- Sin Mensajes de Error: o No hay indicaciones cuando una acción no se completa correctamente.

Ayuda y Documentación:

LUCAS MELGARES CARMONA 126

---

<!-- Página 132 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Falta de Guías:

o No hay asistencia integrada en la página o alguna especie de tutorial inicial.

Por ahora, es el prototipo que mejor se adapta al prompt proporcionado que define la página de inicio (Home), sin

embargo, existen fallos de en la gestión de errores y en proporcionar tutoriales o documentación de uso de la interfaz.

6.2.2.3 Mockflow

Visibilidad del Estado del Sistema:

- Encabezado: o Encontramos un encabezado fijo que permanece visible al desplazarse, facilitando la orientación. o Las categorías se muestran en forma de texto sin íconos, lo que reduce la visibilidad. o No hay un indicador visual que muestre la sección activa, lo que puede causar desorientación, por lo que hay una falta de resaltado. - Sección de Ofertas Flash: o Las ofertas están agrupadas en bloques rígidos, lo que dificulta identificar qué productos están en oferta a simple vista. - Pie de Página: o El tamaño pequeño de la fuente reduce su impacto y accesibilidad, por lo que dificulta la visibilidad.

Correspondencia entre el Sistema y el Mundo Real:

- Lenguaje Formal: o Uso de términos estándar como "Ofertas Flash" y "Recomendaciones" en el mundo del e-commerce. - Iconografía: o La ausencia de iconos en el menú hace que el usuario dependa exclusivamente del texto, lo que

reduce la familiaridad visual.

LUCAS MELGARES CARMONA 127

---

<!-- Página 133 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Control y Libertad del Usuario:

- Falta de Opciones de Deshacer: o No hay manera de cancelar acciones ni de volver atrás fácilmente. - Navegación Rígida:

o El usuario debe volver al menú superior para cambiar de sección, lo que reduce la libertad.

Consistencia y Estándares:

- Formato Homogéneo: o El diseño mantiene una consistencia en el uso de colores oscuros y fuentes de tamaño similar. - Inconsistencia en las Tarjetas: o Algunas tarjetas tienen botones, otras solo muestran el nombre del producto, lo que genera confusión.

Prevención de Errores:

- Falta de Confirmación: o No hay mensajes que adviertan al usuario al añadir productos repetidos al carrito. - Sin Mensajes de Confirmación: o No hay mensajes de éxito al añadir productos.

Reconocimiento Mejor que Recuerdo:

- Menú Compacto: o El menú superior sin iconos requiere que el usuario recuerde qué representa cada categoría. - Tarjetas de Productos: o La disposición uniforme ayuda a reconocer productos, pero la falta de botones claros resta usabilidad.

Flexibilidad y Eficiencia de Uso:

- Falta de Atajos:

LUCAS MELGARES CARMONA 128

---

<!-- Página 134 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

o El diseño obliga a desplazarse bastante para acceder a los productos más buscados. - Barra de Búsqueda: o Aunque visible, su ubicación en el extremo derecho puede pasar desapercibida.

Estética y Diseño Minimalista:

- Diseño Anticuado: o La paleta de colores oscuros y el estilo plano

generan una percepción de rigidez. - Falta de Dinamismo: o Las ofertas no destacan visualmente, lo que puede hacer que pasen desapercibidas.

Ayudar a Reconocer y Recuperarse de Errores:

- Sin Mensajes de Error: o No se observan mensajes que orienten al usuario al cometer errores.

Ayuda y Documentación:

- Ausencia de Guías: o No hay asistencia visual ni documentación sobre cómo usar la página.

En definitiva, el diseño de Mockflow, por ahora al igual que en el análisis anterior, es el que menos sigue el prompt proporcionado. La falta de contrastes, botones claros, atajos y la organización visual rígida, dificultan la experiencia de usuario.

6.2.2.4 Websim.ai

Visibilidad del Estado del Sistema:

- Encabezado: o El menú no permanece fijo, lo que genera pérdida de contexto al navegar.

LUCAS MELGARES CARMONA 129

---

<!-- Página 135 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

o No hay resaltado visual o contraste que indique en qué sección se encuentra el usuario. - Productos Destacados: o Los botones de "Descúbrelo" están visibles, pero el tamaño pequeño los hace menos atractivos.

o La ausencia de botones en cada tarjeta de producto para poder comprarlo, resta la ausencia de experiencia de usuario. o La oferta diaria se muestra en un banner estático, lo que reduce la sensación de dinamismo.

Correspondencia entre el Sistema y el Mundo Real:

- Lenguaje Comercial: o Utiliza frases comunes en e-commerce como "Grandes Ofertas", lo que facilita el entendimiento. - Iconografía: o Los iconos del pie de página de redes sociales son claros y reconocibles.

Control y Libertad del Usuario:

- Sin Opciones de Deshacer: o No hay botones para eliminar productos del carrito desde la vista principal. - Navegación Inflexible: o Cambiar de categoría implica volver al menú principal, lo que limita la libertad.

Consistencia y Estándares:

- Botones Homogéneos: o El botón de "Descúbrelo" tiene un diseño uniforme en todas las tarjetas. - Cambio de Tipografía: o Algunas secciones tienen fuentes más grandes que otras, lo que puede romper la coherencia visual.

Prevención de Errores:

LUCAS MELGARES CARMONA 130

---

<!-- Página 136 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Sin Confirmación de Acciones: o No hay mensajes al añadir un producto, lo que puede llevar a compras duplicadas.

Reconocimiento Mejor que Recuerdo:

- Barra de Navegación: o La ausencia de iconos en el menú hace que el usuario tenga que recordar qué sección corresponde a cada nombre.

- Botones Consistentes: o El mismo diseño en todos los botones de compra facilita el reconocimiento.

Flexibilidad y Eficiencia de Uso:

- Navegación Larga: o El usuario debe desplazarse extensamente para llegar a ofertas destacadas. - Falta de Atajos: o No hay botones rápidos para acceder a las secciones más visitadas.

Estética y Diseño Minimalista:

- Colores Modernos: o El uso de tonos azules y blancos crea un diseño más limpio que Mockflow. - Espacios Ajustados: o Algunas secciones están muy juntas, lo que provoca una sensación de saturación.

Ayudar a Reconocer y Recuperarse de Errores:

- Sin Retroalimentación de Errores: o No hay avisos cuando una acción no se completa correctamente.

Ayuda y Documentación:

LUCAS MELGARES CARMONA 131

---

<!-- Página 137 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- Sin Soporte: o No hay documentación o tutoriales integrados.

En definitiva, en el caso de Websim.ai, el prototipo cumple parcialmente con el prompt al mostrar productos destacados, aun así, la falta de navegación fija y la ausencia de botones afectan

negativamente a la experiencia del usuario.

6.2.3. Mejor herramienta / software de prototipado

En este apartado se decide cuál ha sido la herramienta o plataforma que ha proporcionado el mejor wireframe en términos de UX, y para ello, se han realizado dos tablas en modo resumen que contienen todos los puntos descritos y discutidos de los dos casos de análisis anteriores, para así

poder tener una respuesta clara y contrastada.

Tabla Resumen Análisis Heurístico de Hassan Montero y Yusef

Página de inicio (Home) Uizard Visily Mockflow Websim Visibilidad del estado del sistema SÍ SÍ SÍ SÍ Correspondencia entre el sistema y el mundo real SÍ SÍ SÍ SÍ Control y libertad del usuario NO NO NO NO Consistencia y estándares SÍ SÍ NO SÍ Prevención de errores NO NO NO NO Reconocimiento mejor que recuerdo SÍ SÍ NO SÍ Flexibilidad y eficiencia de uso SÍ SÍ NO SÍ Estética y diseño minimalista SÍ SÍ NO SÍ Ayudar a reconocer y corregir errores NO NO NO NO Ayuda y documentación NO NO NO NO

Tabla Resumen: Análisis Heurístico de Jakob Nielsen

Página de inicio (Home) Uizard Visily Mockflow Websim Visibilidad del estado del sistema SÍ SÍ SÍ SÍ

Correspondencia entre el sistema y el mundo real SÍ SÍ SÍ SÍ

Control y libertad del usuario NO NO NO NO Consistencia y estándares SÍ SÍ NO SÍ Prevención de errores NO NO NO NO Reconocimiento mejor que recuerdo SÍ SÍ NO SÍ

LUCAS MELGARES CARMONA 132

---

<!-- Página 138 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Página de inicio (Home) Uizard Visily Mockflow Websim Flexibilidad y eficiencia de uso SÍ SÍ NO SÍ Estética y diseño minimalista SÍ SÍ NO SÍ Ayudar a reconocer, diagnosticar y recuperarse de NO NO NO NO errores Ayuda y documentación NO NO NO NO

Como se ha mencionado anteriormente, para asegurar una evaluación exhaustiva y precisa de los prototipos creados para la página de inicio (Home) del e-commerce, se han realizado dos evaluaciones heurísticas basadas en diferentes enfoques en el campo de la experiencia de usuario (UX): la evaluación heurística del sitio web de Montero y Yusef y los principios de usabilidad de Nielsen. Ambos enfoques, aunque se ocupan de identificar problemas relacionados con las interacciones y la usabilidad, tienen algunos elementos de diferentes permitiendo evaluar de manera aún más exigente los prototipos, conduciendo a una comprensión holística y precisa de cuál de los prototipos tiene un mejor rendimiento en UX.

El enfoque de Montero y Yusef enfatiza particularmente la acomodación de la visibilidad, la claridad y la representación del mundo real del sistema para que los usuarios puedan sentirse como en casa con la interfaz desde la primera interacción. Además, este análisis enfatiza la coherencia y evitar sobrecargar al usuario con información innecesaria y una estética agradable en el diseño en sí. Por otro lado, el enfoque de Jakob Nielsen proporciona una visión más holística al incorporar factores como el control y la libertad del usuario, la auto prevención de errores y la capacidad del sistema para proporcionar mensajes claros para fallos o situaciones imprevistas. Esto permite un control más directo sobre la interfaz y la recuperación de errores potenciales.

Después de realizar ambos estudios, hubo una coincidencia notable en todos los resultados, lo que otorga mayor consistencia y validez a las conclusiones que se obtuvieron. En ambos casos, el prototipo que se destacó con el mejor rendimiento en UX fue el de Visily. Esto se debe a que Visily se ha destacado de manera explícita en factores como la visibilidad del estado del sistema, la cobertura de la realidad, la consistencia y unidad del texto y gráficos, así como la modernidad y

LUCAS MELGARES CARMONA 133

---

<!-- Página 139 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

minimalismo del diseño. Además, el hecho de que el elemento del menú que queda fijo al desplazarse garantiza intuición y eficiencia en la navegación, lo cual es crucial para la retención del sentido de posicionamiento por parte del usuario en la exploración de la página.

Otro de los puntos que sobresale en Visily fue la ejecución correcta de botones de acción decisivos y que llaman la atención, como el “Shop Now” del banner promocional, cumpliendo con el principio de ofrecer llamadas a la acción evidentes y accesibles. Asimismo, el diseño atractivo y organizado de las tarjetas de productos, con botones de compra uniformes, refuerza la coherencia visual en toda la interfaz, lo que genera una experiencia positiva y evita la carga cognitiva innecesaria.

Si bien Visily ha identificado puntos de mejora, como la falta de un reiniciar, la falta de mensajes de errores no elaborados, estos hallazgos son comunes a los cuatro prototipos testeados y no suponen una vulnerabilidad para su competitividad global, además, para la parte práctica de este trabajo, no se espera crear una página web funcional en términos de programación o similar, lo que implica que estos hallazgos erróneos encontrados, tal vez se vean resueltos al realizar diferentes acciones o accediendo a otras páginas diferentes a las escogidas. Por esta razón, tras haber considerado ambos enfoques heurísticos y tras una reflexión crítica y comparativa de los resultados, se ha concluido que el prototipo de Visily es el que mejor resuelve en cuanto a experiencia de usuario. Un resultado que es sinónimo de una interfaz clara, actualizada y fácil de usar, que conviene al perfil del usuario final y con la que también se puede seguir una navegación clara e intuitiva en todo momento.

Es por esto que, con base en los resultados ilustrados en este test, se procederá a la elaboración del resto de páginas que compondrán el sitio web de este proyecto de la misma forma que Visily se ha construido, recogiendo los puntos fuertes que este tiene en su haber para mantener la coherencia y el uso amigable en todo el sitio web. Con lo que no solo se garantiza una experiencia de usuario inmejorable, sino que también se pone en bandeja la creación de una identidad visual homogénea y seductora para toda la tienda online a través de la IA.

LUCAS MELGARES CARMONA 134

---

<!-- Página 140 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

- 6.3. Desarrollo de prototipos con IA mediante Visily

A continuación, tras realizar una comparativa visual y funcional entre las distintas herramientas de prototipado utilizadas y aplicar dos análisis heurísticos en base a los perfiles de usuario definidos, y de acuerdo con el apartado “6.2.3”, a continuación, se ha decidido seguir el desarrollo práctico del TFG utilizando esta herramienta como base para el resto de las páginas definidas. En este apartado, el lector encontrará el proceso de diseño y generación de las interfaces correspondientes a las siguientes secciones clave de un e-commerce: la página de inicio de sesión (Login), la página de detalle de producto doméstico (Detalles de un producto), la página de seguimiento de pedido (Seguimiento) y la página de ayuda o contacto (Ayuda). Cada

prototipo ha sido construido con prompts cuidadosamente redactados y alineados con los principios de UX establecidos, buscando mantener una coherencia visual y funcional respecto al diseño inicial de la página de inicio y adaptándose a los distintos perfiles de usuario contemplados en el proyecto.

6.3.1. Página de Login

Para comprobar la fidelidad del diseño creado por la herramienta Visily en relación con el prompt de la pantalla de inicio de sesión, se ha llevado a cabo un análisis detallado que compara todos los elementos solicitados con el resultado final.

El prompt incluía varios requisitos específicos, tanto visuales como funcionales: debía mantener una cabecera idéntica a la de la página de inicio, incorporar un formulario centrado sobre un fondo gris claro con campos para el correo electrónico, la contraseña, una casilla de “Recuérdame” y un botón naranja destacado. También se requería incluir enlaces en azul para la recuperación de contraseña y el registro. Además, a la derecha (o debajo, dependiendo del dispositivo), debía integrarse un bloque informativo que resaltara los beneficios del registro, como el historial de pedidos, favoritos y soporte prioritario, todo manteniendo una estética coherente con la página principal: fondo gris claro (#f4f4f4), contenedores blancos con sombras suaves, botones naranja (#ff9900) y elementos interactivos en azul profundo (#003366), utilizando una tipografía sans-serif clara como Open Sans o Inter.

LUCAS MELGARES CARMONA 135

---

<!-- Página 141 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 64 Resultado Final Login"

El resultado que se obtuvo con Visily cumple con una precisión sorprendente cada uno de estos requisitos. La cabecera es exactamente la misma que en la pantalla de inicio, tanto en disposición como en estilo, aunque en este caso la encontramos más simplificada y con diferentes botones como el de “Iniciar Sesión” y secciones más genéricas para posteriormente poder navegar en la web.

El fondo gris claro se aplica correctamente, y el formulario de acceso está centrado con un diseño limpio y bien estructurado. Todos los campos solicitados están presentes: correo electrónico, contraseña, la casilla de “Recuérdame” y un botón de “Iniciar sesión” en un vibrante naranja (#ff9900), perfectamente ubicado y con un alto contraste visual. Justo debajo, se encuentran los enlaces de “¿Olvidaste tu contraseña?” y “Crear cuenta nueva”, en un tono azul profundo que coincide con la guía de estilo proporcionada. A la derecha del formulario, Visily ha implementado un bloque muy bien diseñado que destaca los beneficios de estar registrado, incluyendo íconos identificativos y descripciones claras. En conjunto y con la combinación de estos estos elementos, Visily ha desarrollado una interfaz visualmente coherente, clara y fucnional.

LUCAS MELGARES CARMONA 136

---

<!-- Página 142 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Además, al observar la pantalla de Home y contrastarla con las páginas de Login elaboradas por Visily, se aprecia una conexión evidente en el estilo y la disposición. Ambas pantallas comparten la navegación, colores (gris claro, blanco, naranja y azul oscuro), tipografía y

estructura de forma coherente. Aún los diminutos aspectos, tales como los espacios en blanco, las formas de los botones y las sutiles luces y sombras en los cuadros, son reproducidos con extrema minuciosidad, evidenciando una cohesión visual excepcional en el conjunto del sitio. Esta consistencia es esencial para la interacción del usuario, ya que comunica una identidad fuerte, simplifica la exploración y disminuye la dificultad al cambiar entre áreas.

Es cierto, que se ha podido observar dos factores que, en este caso, si se llevase a cabo la elaboración de la página web se cambiarían de inmediato. El primero de todos es que, a pesar de seguir el estilo y disposición del encabezado igual que en la página de Home, es cierto que el nombre y logo de la web no es el mismo, además de la foto de perfil del usuario registrado. Además, en este caso nos encontramos con secciones más genéricas en las que algunas coinciden con el header de la página de inicio y otras no. Por último, al hacer esta comparación de resultados, se ha podido observar que el footer tampoco coincidía con el que se generó en la página de Home, en este caso, encontramos uno mucho más simplificado, lo cual es un acierto. Esto es debido a que, si echamos un vistazo a nuestra página de referencia "Amazon", podemos observar cómo directamente en la página de Login, no aparece ningún header limitando las opciones de navegación, pero lo que sí que se puede observar, es un footer mucho más resumido y simplificado, tal y como podemos ver en la “Fig 40 Página de Login Amazon".

En conclusión, podemos afirmar con plena certeza que Visily ha cumplido de manera excelente con la solicitud de la página de Login, tanto en su diseño como en su aspecto visual. Además, se ha mantenido una coherencia estética con la pantalla principal, lo que garantiza una experiencia del usuario fluida, consistente y experta. Este hallazgo fortalece la decisión de elegir a Visily como la

LUCAS MELGARES CARMONA 137

---

<!-- Página 143 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

herramienta más sólida y segura para crear las otras pantallas del sitio web. A partir de ahora, se continuará con el diseño de las vistas restantes del comercio electrónico, como la página de detalles de productos, seguimiento y asistencia, manteniendo la misma estética y los mismos conceptos de facilidad de uso, asegurando de este modo

la consistencia general del plan.

6.3.2. Página de Detalles de un producto

Para analizar la calidad del diseño de la pantalla de "Detalles de un artículo" hecha por Visily, se ha llevado a cabo una comparación entre las imágenes resultantes (Detalles_producto01, 02 y 03) y las

instrucciones detalladas previas, que se le ha pedido a la plataforma mediante el prompt que ya se ha definido anteriormente, como en los demás casos. Se buscaba confirmar si se mantenían los componentes prácticos y el estilo visual coherente definido para todo el proyecto.

La solicitud pedía una disposición específica que incluyera, en la parte superior, una sección coherente con el resto de páginas con un logo, búsqueda, cuenta y carrito, seguida de una guía de navegación estilo migas de pan. El contenido principal debía dividirse en dos secciones: una izquierda con una galería de imágenes (imagen principal grande y miniaturas clicables), y una derecha con información del producto, marca, valoración (estrellas y cantidad de opiniones), precio original y rebajado, selector de cantidad y dos botones: "Agregar al carrito" en color naranja y "Comprar ahora" en azul. También, era necesario agregar secciones desplegables que contengan información detallada, una tabla con especificaciones técnicas, reseñas de usuarios con opciones de filtrado, valoración con estrellas e imágenes, y una galería de productos relacionados. Todo esto debía mantener la estética del proyecto: un fondo gris claro (#f4f4f4), texto en tonos oscuros, títulos en azul intenso, botones en color naranja (#ff9900), fuente sans-serif clara, un diseño pulcro y adaptable a dispositivos móviles.

LUCAS MELGARES CARMONA 138

---

<!-- Página 144 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 65 Resultado Final Detalles Producto 01"

“Fig 66 Resultado Final Detalles Producto 02"

LUCAS MELGARES CARMONA 139

---

<!-- Página 145 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 67 Resultado Final Detalles Producto 03"

Al igual que en las dos páginas anteriores, el desempeño de Visily es super bueno, al satisfacer completamente los requisitos del prompt. Para empezar, la cabecera se conserva igual que en la página principal y la de inicio de sesión, incluyendo logotipo, menú en la parte superior, barra de búsqueda, enlace a la cuenta y al carrito. Como única pega que se podría tener en cuenta es que, al igual que en el caso anterior de la página de Login, no se mantiene el mismo logo y nombre de la web o e-commerce, pero sí que se mantiene la misma estructura y disposición de los elementos y misma foto de perfil. Esto fortalece la consistencia y facilita la navegación sin interrupciones. El camino de

9 navegación breadcrumbse muestra debajo, fácil de seguir para ayudar al usuario a moverse por el sitio.

9 El concepto de bradcrumb o “migas de pan”, hace referencia a una navegación secundaria que se encuentra dentro de un web, ofreciendo enlaces internos a los usuarios para navegar en los diferentes niveles de la web, ya sea volver a la página principal o a otro nivel.

LUCAS MELGARES CARMONA 140

---

<!-- Página 146 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

La disposición de dos columnas se mantiene intacta: en la columna izquierda, destaca una imagen amplia del producto con miniaturas clicables debajo, y en la columna derecha, se detalla toda la información importante sobre el producto. Se presentan el título, la firma, una puntuación con estrellas y la cantidad total de reseñas, el

valor original tachado con el costo definitivo en color azul mostrando un descuento resaltado en verde, lo que realza la apariencia llamativa de la oferta. Además, se agrega un menú desplegable de selección práctico y dos botones de acción claramente distintos, aunque con los colores intercambiados en comparación con lo que se le pedía en el prompt, "Añadir al carro" es azul y debería ser naranja.

Respecto a las partes de abajo, las secciones están bien hechas en su totalidad. La explicación del artículo está presentada de forma desplegable, después viene una tabla técnica, tal como se solicitaba. Aunque es cierto que estas dos secciones aparecen en forma de despegable, no se ha generado como tal el contenido que el usuario encontraría dentro de estos apartados. La sección de comentarios de clientes sobresale por su excelencia: muestra una calificación general con números, filtros por estrellas y reseñas visibles en grande y con imágenes auténticas de los usuarios, mejorando la experiencia y fortaleciendo la confianza del comprador. A continuación, se exhibe una fila de productos relacionados con detalles de precios previos y posteriores a rebajas, junto con opciones para "Agregar al carrito". Se ha incluido una sección de preguntas frecuentes adicional que no fue pedida específicamente en el prompt, pero que resulta muy beneficiosa para los usuarios, mejorando la funcionalidad del sitio web sin afectar su diseño limpio.

Al contrastar este apartado de producto con las otras secciones del proyecto ya revisadas, la página de inicio (Home) y la de inicio de sesión, se puede afirmar claramente que se conserva una uniformidad visual en todo el sitio. El fondo gris claro (#f4f4f4) se mantiene, los textos en gris oscuro (#333333), los títulos siguen siendo azul profundo (#003366), y los botones mantienen la apariencia reconocible con naranja y azul como colores principales. La tipografía es coherente, posiblemente Open Sans o Inter, lo que asegura una lectura clara y una

LUCAS MELGARES CARMONA 141

---

<!-- Página 147 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

identidad uniforme. Igualmente, la disposición de los márgenes, contenedores, sombras suaves y organización general sigue el patrón visual ya establecido en las demás páginas, lo que comunica una coherencia evidente, experta y muy bien organizada. Es cierto que, al comparar todos los elementos de forma más detallada, en el caso de

nuestra web de referencia "Amazon", se utiliza el mismo footer tanto en la página principal o "Home" como en la de "Detalles de un producto", cosa que Visily no ha respetado.

Para concluir, es seguro decir que la pantalla de descripción del producto creada por Visily conserva fielmente todos los elementos funcionales y visuales del diseño original. No solo replica lo requerido, sino que también sigue una estética consistente con las pantallas previas del proyecto, asegurando así una experiencia de usuario fluida, visualmente sólida y sumamente profesional. La herramienta comprende de manera exacta lo que se necesita en términos de funcionalidad y diseño, siguiendo los criterios establecidos desde el principio del proyecto.

6.3.3. Página de Seguimiento

Al diseñar la nueva pantalla para seguir pedidos, se pidió un estilo limpio y moderno que encaje con el estilo del resto del sitio. La cabecera tuvo que seguir llevando el logotipo, la barra de búsqueda y el menú que ya aparecen en las otras páginas. En el centro, se incluye un cuadro donde se lean el número de pedido, el producto, la fecha y el resumen del pago. Debe ir también una barra de progreso horizontal dividida en cinco pasos: Pedido recibido, Preparando, Enviado, En reparto y Entregado. Cada paso lleva su icono y color gris para pendiente, verde para terminado y azul para el que se sigue. A la derecha hay que añadir otro recuadro con los datos del envío: dirección, empresa de transporte, fecha estimada y número de seguimiento que el cliente pueda copiar. Por último, debajo debe aparecer un botón azul que diga Contactar con soporte y, junto a él, los enlaces directos a la política de devoluciones y a las preguntas frecuentes. Además, se requería que todo se presentara con un diseño moderno: un fondo de color gris claro (#f4f4f4), encabezados en azul

LUCAS MELGARES CARMONA 142

---

<!-- Página 148 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

intenso (#003366), texto en tono gris oscuro, botones en naranja brillante (#ff9900) y una fuente sin remates.

“Fig 68 Resultado Final Seguimiento"

El nuevo diseño se ajusta a las pautas del proyecto y lo hace de forma brillante. La cabecera, por ejemplo, queda alineada con las páginas de inicio, de inicio de sesión y de detalles del producto. En ella, el logotipo aparece a la izquierda, la barra de búsqueda se sitúa en el centro y los enlaces de cuenta y carrito ocupan su lugar sin desorden. Todo esto consigue que la navegación sea uniforme en todo el sitio, a pesar de que, como ha sucedido en proyectos anteriores, el header conserva la misma composición, pero alterna el logotipo y el nombre de la empresa, incluso la foto de perfil. Justo debajo, en el centro, hay un bloque claro que muestra los detalles del pedido-número de orden, nombre del producto, fecha de compra, total pagado y método de pago- dentro de una caja blanca con sombra suave y jerarquía visual sencilla.

LUCAS MELGARES CARMONA 143

---

<!-- Página 149 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Centrando la mirada en la pantalla principal, lo primero que salta es la barra de progreso, amplia y clara. Cada fase del pedido viene marcada por un icono y una breve explicación que sigue un esquema de colores concreto: los pasos ya cumplidos y el que está en marcha-aparecen en azul; los que quedan, en gris. Curiosamente, aquí no se ha empleado

el verde habitual para los logros pasados. Esta elección cromática permite ver de un vistazo dónde está el pedido, algo muy útil en pantallas pequeñas. Resulta vital en una interfaz que busca rapidez en la lectura. Generalmente, la disposición horizontal se comporta bien y no desdibuja el texto ni en teléfonos. A la derecha, un cuadro reúne todos los datos de envío. Dentro aparecen la dirección completa, la empresa transportista, la fecha de entrega prevista y el número de seguimiento. También hay un botón que copia esa información al portapapeles con un solo toque. En resumen, cada solicitud se ha reflejado aquí de forma precisa y sin errores. Just debajo, se ha añadido de manera adicional, el historial del pedido detallando la fecha y hora de cada cambio, lo cual no se había solicitado específicamente, pero resulta muy útil para el usuario al brindar más información, lo que a su vez aumenta la confianza y transparencia del proceso.

En la parte más baja de la pantalla se encuentra un botón azul que da acceso inmediato al equipo de soporte, tal como se pide. Justo al lado aparecen dos enlaces prácticos: uno lleva a la política de devoluciones y el otro a las preguntas frecuentes. La forma en que se organizan estos elementos es sencilla y permite al usuario encontrar ayuda rápida si surge cualquier duda. También, al igual que en tiendas en línea reconocidas como Amazon, se ha añadido un pie de página o footer que responde a las necesidades específicas de esta sección. La estética general sigue siendo uniforme: el fondo gris claro, el texto en tonos oscuros y los encabezados como Seguimiento de pedido o Información de envío resaltan en ese azul (#003366). La tipografía sans-serif, limpia y fácil de leer, se alinea con las fuentes de otras pantallas del sistema. Aunque el botón principal es azul y no naranja como suele aconsejarse para las acciones decisivas, el contraste sigue siendo fuerte y la jerarquía visual está bien marcada, por lo que su funcionalidad queda intacta.

LUCAS MELGARES CARMONA 144

---

<!-- Página 150 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

En resumen, la pantalla de seguimiento de pedidos creada por Visily sigue fielmente el diseño original y se integra perfectamente con el estilo visual general de la tienda. La forma en que se presenta la información es muy clara, se ha manejado bien la paleta de colores y se han incluido todas las funciones necesarias, junto con algunos

extras útiles como un historial detallado de pedidos. Esta coherencia tanto en el aspecto visual como en el funcionamiento mejora la experiencia del usuario, haciéndola más sólida y fluida.

6.3.4. Página de Ayuda

El nuevo prototipo para la sección de Ayuda se ajusta fielmente a lo

pedido en el prompt, tanto en funciones como en apariencia. Encontramos un header con componentes ordenados de forma coherente, pero con un nuevo nombre y logo de empresa y sin foto de perfil. En este caso no tenemos en buscador incrustado en el header, debido a que en la parte superior la página arranca con un buscador grande y centrado que lleva la pista ¿En qué podemos ayudarte?, tal como se pidió. Esa línea incita al visitante a escribir su duda y da una sensación de orden y acceso inmediato. El elemento está alineado, rodeado de un limpio icono de lupa y contrasta bien sobre el fondo, así que da una buena primera impresión.

LUCAS MELGARES CARMONA 145

---

<!-- Página 151 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 69 Resultado Final Ayuda01"

“Fig 70 Resultado Final Ayuda02"

LUCAS MELGARES CARMONA 146

---

<!-- Página 152 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

“Fig 71 Resultado Final Ayuda02"

Bajo el buscador aparece un bloque de preguntas frecuentes que se despliega en secciones colapsables, otra idea del prompt original. Las temáticas “Pedidos y entregas”, “Devoluciones”, “Cuenta”, “Pagos y

facturas” y “General”, están agrupadas de forma lógica. A cada ítem se le suma un icono claro y un pequeño botón que abre el texto asociado en un clic. Así, el visitante puede encontrar respuestas rápidas y evita tener que llamar o escribir al equipo de soporte. Por lo general, se cuida la jerarquía con títulos en negrita, gráficos sencillos y alineación uniforme sobre un fondo blanco que lleva una leve sombra.

A continuación, se muestra un formulario de contacto completo, que sigue al pie de la letra lo pedido en el prompt. Lleva nombre, dirección de e-mail, tipo de consulta en un menú desplegable, mensaje y un campo para subir archivos, lo que mejora lo solicitado. El botón de envío es naranja (#ff9900), dice “Enviar” mensaje y está en un lugar claro, con suficiente contraste. La zona mantiene orden visual, buen espaciado y estructura vertical lógica, de modo que resulta fácil de usar en ordenador y móvil.

A la derecha se añade un bloque de contacto directo que muestra teléfono, dirección de correo y un botón grande para abrir el chat en vivo, con ícono azul muy visible. Por debajo aparece un aviso que explica los tiempos de respuesta y la frase “Estamos aquí para ayudarte”, tal como se pidió, que refuerza la cercanía y confianza del soporte del e-commerce.

LUCAS MELGARES CARMONA 147

---

<!-- Página 153 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Más abajo aparece una sección que nunca se pidió, pero que añade mucho: una rejilla de artículos de ayuda recientes, con imágenes llamativas, títulos breves y enlaces que dicen "Leer más". Estas secciones extras dejan al usuario manejarse solo, aprender a su ritmo

y quitarse dudas antes de llamar. Más abajo se puede ver un bloque titulado “Nuestras Historias de Éxito”, donde cuelga comentarios positivos de clientes; queda claro que aquí la atención es rápida y humana. Desde el punto de vista visual, la estética general es completamente coherente con el resto de las páginas del sistema. El fondo principal es gris claro, los bloques se presentan sobre tarjetas blancas con bordes redondeados y sombras sutiles, los textos están en gris oscuro, y los títulos emplean un azul profundo (#003366). La tipografía empleada es sin serifa, clara y legible, y se mantiene el uso de acentos cromáticos definidos en el sistema de diseño (botones naranjas para acciones principales y azules para acciones secundarias o informativas). Todo ello en una disposición bien aireada, con márgenes generosos, jerarquía visual clara y excelente adaptación a dispositivos móviles, de manera que el contenido respira, se lee sin esfuerzo y se ve igual de nítido en un teléfono que en un monitor grande.

En pocas palabras, la nueva pantalla de ayuda que generó la herramienta Visily cumple al pie de la letra con lo que se le pidió, pero, además, incluye guías extras que la hacen mucho más útil. Su arreglo ordenado, aspecto limpio y la forma en que se integra con el resto de la tienda online refuerzan una experiencia contundente, comprensiva y profesional. Con este panel no solo se ofrecen respuestas prácticas, sino que se transmite calma y claridad al cliente, ratificando, una vez más, que Visily es el aliado perfecto para dar forma al diseño de este proyecto.

LUCAS MELGARES CARMONA 148

---

<!-- Página 154 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## 7. Conclusiones

El trabajo final de grado se ha ocupado de analizar a fondo cómo la inteligencia artificial influye hoy en día en las prácticas de experiencia de usuario, un campo joven, como quien dice, que no solo marca otro salto tecnológico, sino que también cambia la manera en que se piensa y se construye cualquier producto o servicio digital. En la introducción se explicó por qué esta cuestión es relevante tanto en el presente como en el futuro, y por eso se decidió abordarla y entrar a fondo. En un entorno en el que la personalización ya se da por hecha si se quiere captar y mantener a los usuarios, la IA brinda herramientas que ajustan la interacción al instante, pulen recorridos, eliminan obstáculos y elevan la satisfacción a límites que antes parecían lejanos. Este modelo de trabajo ya lo practican multinacionales titanes como Amazon, Netflix o Spotify, y ahora salta con rapidez a ámbitos como la educación, la salud o el comercio electrónico.

Como objetivo principal, se propuso estudiar de manera directa cómo la inteligencia artificial puede hacer más ágiles los procesos de experiencia de usuario, centrándose en la creación de prototipos e incorporando prompts generativos para diseñar pantallas que pongan al usuario en el centro. Se adoptó un enfoque práctico, eligiendo el comercio electrónico como ámbito real y tomando como referente el modelo de personalización que utiliza Amazon. Para llevarlo a cabo, se recurrió a herramientas de prototipado impulsadas por IA, como Visily, Uizard, Mockflow y Websim.ai, que permiten generar varias versiones de una misma interfaz a partir de un único prompt, con el fin de comprobar cuál ofrece una experiencia superior, tanto según las reglas heurísticas de Jakob Nielsen como por la lista de evaluación propuesta por Hassan Montero y Yusef.

Los resultados, sin duda, han sido muy relevantes. Tras revisar a fondo todas las pantallas generadas (Inicio, Login, Detalle del producto, Seguimiento del pedido y Ayuda), quedó claro que Visily generó piezas mucho más cercanas a lo pedido: la coherencia visual, la jerarquía de la información y la fluidez de la interacción eran superiores a lo que se esperaba. Las evaluaciones heurísticas, hechas de forma cruzada con ambos métodos, permiten afirmar que los prototipos creados por IA no solo son válidos, sino que rivalizan con los que elabora a mano un experto en UX, siempre que el prompt esté bien

LUCAS MELGARES CARMONA 149

---

<!-- Página 155 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

definido y un ojo profesional valide el resultado. Esta conclusión es clave: la IA no sustituye al diseñador, sino que funciona como un asistente estratégico y operativo que amplifica su velocidad, su rigor y su momento de exploración creativa.

Los resultados de este proyecto coinciden con estudios recientes, como El papel de la inteligencia artificial en el diseño UX/UI (2025), que destacan la importancia de la IA para crear experiencias adaptativas y personalizadas. No obstante, aquí se ofrece un enfoque más práctico, al confrontar directamente los resultados producidos por algoritmos con evaluaciones hechas según pautas clásicas de usabilidad. Así, en lugar de seguir una línea meramente teórica, este TFG presenta pruebas empíricas que demuestran que la IA puede incorporarse, de forma útil y tangible, a cada paso del trabajo diario en diseño UX.

Aun así, es cierto que se han encontrado diferentes obstáculos. Por un lado, las herramientas de IA empleadas todavía son rígidas y no permiten diseños completamente libres, ajustes minuciosos de cada pieza ni conexión directa con bases de datos reales. Además, aunque se redactaron arquetipos de usuarios y se simularon revisiones heurísticas, nunca se llevaron a cabo test reales que aportaran datos cualitativos y cuantitativos sobre el uso, de modo que el análisis de la interacción sigue siendo superficial. Por último, los dilemas éticos que podrían profundizarse mediante experimentos prácticos que midan la transparencia de los algoritmos, la protección de los datos y una accesibilidad automática realmente inclusiva.

Aunque todavía hay cosas por pulir, los logros hasta hoy ya son notables. Se ha creado un método claro para diseñar y evaluar las interfaces de usuario que genera la IA, se ha montado un sistema visual coherente alrededor de una tienda online completa y se han documentado, desde una mirada académica, técnica y ética, las ventajas y los riesgos de usar IA en ese proceso. Todo esto me ha permitido posicionarme como un perfil multidisciplinar que, además de manejar herramientas de IA, sigue dominando los fundamentos clásicos del diseño UX, una combinación clave para su futuro profesional.

De cara al futuro, el proyecto plantea varias ideas. Por un lado, convendría hacer pruebas con usuarios reales, los test A/B, mapas de calor con

LUCAS MELGARES CARMONA 150

---

<!-- Página 156 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

eyetracking o breves encuestas, para comprobar si lo que creó la IA funciona mejor, igual o peor que lo hecho a mano. También sería práctico usar IA generativa en fases tardías, por ejemplo, al escribir microtextos, generar imágenes a medida o prototipar gestos avanzados. Otra vía importante es investigar cómo la IA puede ayudar al diseño inclusivo, creando versiones

automáticas que se adapten a personas con discapacidades visuales, cognitivas o motrices. Por último, sería valioso construir un sistema híbrido IA- UX en el que el diseñador no solo ajuste resultados, sino que entrene al modelo según su estilo personal o el tono de una marca determinada, proporcionándole plantillas ajustadas a su historial y flujo de trabajo.

En resumen, este trabajo de fin de grado ha mostrado que la inteligencia artificial puede cambiar de verdad la forma en que entendemos y construimos experiencias de usuario. Al mezclar teoría, experimentos prácticos y una evaluación crítica honesta, la investigación aporta ideas útiles tanto a académicos como a profesionales, y abre caminos hacia diseños digitales más efectivos, ajustados a cada persona, éticos e inclusivos. Así, en lugar de reemplazar al diseñador, la IA se perfila como un compañero indispensable que dará forma a la UX del mañana.

Por último, como complemento visual, se ha generado un vídeo en el que se muestra de forma dinámica, gráfica y realista los resultados de los wireframes generados mediante inteligencia artificial para las diferentes pantallas del e- commerce. Este tráiler permite visualizar con mayor claridad los resultados obtenidos y cómo la IA ha sido capaz de transformar los prompts en propuestas de diseño funcionales y coherentes. Puede consultarse a través del siguiente enlace: UX con IA: Wireframes de un e-commerce diseñado con inteligencia artificial - Lucas Melgares Carmona [Vídeo]. YouTube. https://youtu.be/XOefb8A6G60?si=Mwzr-wYPI7CkejEw

LUCAS MELGARES CARMONA 151

---

<!-- Página 157 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

## 8. Referencias

¿Cómo escribir mejores Prompts en ChatGPT? (30 de 04 de 2025). Obtenido de IEBS: https://www.iebschool.com/hub/como-escribir-mejores-prompts-en- chatgpt-tecnologia/?utm_source= ¿Cómo funciona la personalización de Amazon y Netflix? (18 de 12 de 2024). Obtenido de VWO: https://vwo.com/blog/es/personalizacion-de-amazon-y- netflix/ ¿Cómo hacer Prompts para ChatGPT? (30 de 04 de 2025). Obtenido de POR CONTAR: https://porcontar.com/blog/como-hacer-un-prompt-para-para- chatgpt/?utm_source

¿Cómo usar la iteligencia artificial en UX/UI? (19 de 10 de 2024). Obtenido de KEEPGOING: https://keepcoding.io/blog/inteligencia-artificial-en-ux-ui/ ¿Cuáles son los algoritmos de inteligencia artificial? (18 de 10 de 2024). Obtenido de TEKDI: https://tekdi.education/blog/algoritmos-inteligencia-artificial/ ¿Qué es Adobe Sensei y Cómo Aprender a Usarlo? (20 de 1 de 2025). Obtenido de IMAGINA: https://imaginaformacion.com/tutoriales/que-es-adobe-sensei-y- como-aprender-a-usarlo ¿Qué es Hugging Face? (3 de 1 de 2025). Obtenido de BOOTCAMPS: https://keepcoding.io/blog/que-es-hugging- face/#%C2%BFQue_es_Hugging_Face ¿Qué es la ética de la IA? (13 de 11 de 2024). Obtenido de IBM: https://www.ibm.com/mx-es/topics/ai-ethics ¿Qué es la Inteligencia Artificial (IA)? (12 de Octubre de 2024). Obtenido de IBM: https://www.ibm.com/mx-es/topics/artificial-intelligence ¿Qué es la inteligencia artificial o IA? (12 de Octubre de 2024). Obtenido de Google Cloud: https://cloud.google.com/learn/what-is-artificial-intelligence?hl=es-419 ¿Qué es OpenCV? (20 de 1 de 2025). Obtenido de CREHANA: https://www.crehana.com/blog/transformacion-digital/que-es-opencv/ ¿Qué es PyTorch? (3 de 1 de 2025). Obtenido de IBM: https://www.ibm.com/es- es/topics/pytorch ¿Qué es PyTorch? (20 de 1 de 2025). Obtenido de IBM: https://www.ibm.com/es- es/topics/pytorch ¿Qué es un wireframe? (14 de 04 de 2025). Obtenido de Miro: https://miro.com/es/wireframe/que-es-wireframe/

LUCAS MELGARES CARMONA 152

---

<!-- Página 158 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

¿Qué es UX o User Experience? Ejemplos para valorar la experiencia del usuario. (6 de 10 de 2024). Obtenido de HOTMART BLOG: https://hotmart.com/es/blog/que-es-ux-user-experience-ejemplos ¿Qué papel tiene la inteligencia artificial en los videojuegos? (20 de 12 de 2024). Obtenido de OBICEX: https://www.obicex.es/blog/aprende-con-

obicex/inteligencia-artificial-y-videojuegos 10 reglas heurísticas de Nielsen y cómo aplicarlas. (10 de 05 de 2025). Obtenido de uifrommars: https://www.uifrommars.com/10-reglas-heuristicas-como- aplicarlas/ 19 Tecnologías emergentes más importantes del 2025 ¡Top ejemplos! (5 de 10 de 2024). Obtenido de OVACEN: https://ovacen.com/tecnologias-emergentes/ 7 ventajas que nos puede aportar la IA a los diseñadores UI/UX Sí, existen. (5 de 11 de 2024). Obtenido de CODITRAMUNTANA: https://coditramuntana.com/es/blog/ventajas-ia-para-dise%C3%B1o Algoritmos de inteligencia artificial: qué son, qué tipos hay y cómo funcionan. (13 de 11 de 2024). Obtenido de BGAN: https://bgan.es/blog-marketing- digital/algoritmos-de-inteligencia-artificial-que-son-que-tipos-hay-y-como- funcionan/ Alibaba actualiza su modelo de IA para competir con Amazon y Microsoft. (19 de 12 de 2024). Obtenido de ECOMMERCE NEWS: https://ecommerce- news.es/alibaba-actualiza-su-modelo-de-ia-para-competir-con-amazon-y- microsoft/ Amazon Personalize. (6 de 1 de 2025). Obtenido de AWS: https://aws.amazon.com/es/personalize/ Análisis de la interacción entre la inteligencia artificial y la experiencia del usuario: Aplicación a un caso práctico. (12 de 03 de 2025). Obtenido de Google Scholar: https://ruc.udc.es/dspace/handle/2183/39531 Análisis Heurístico para UX: evalua la usabilidad de tu web. (10 de 05 de 2025). Obtenido de hiberusblog: https://www.hiberus.com/crecemos-contigo/analisis- heuristico-para-ux-evalua-la-usabilidad-de-tu-web/ Aplicaciones de la inteligencia artificial en el sector gaming. (16 de 12 de 2024). Obtenido de INESDI: https://www.inesdi.com/blog/la-IA-en-videojuegos/ Aplicaciones de la inteligencia artificial para mejorar la experiencia de usuario. (8 de 10 de 2024). Obtenido de ENIUN: https://www.eniun.com/aplicaciones- inteligencia-artificial-mejorar-experiencia-de-usuario/

LUCAS MELGARES CARMONA 153

---

<!-- Página 159 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Big Data e IA en la salud: la medicina del futuro. (3 de 12 de 2024). Obtenido de KALIA: https://kaila.eu/es/blog/big-data-e-ia-en-la-salud-la-medicina-del- futuro/ Chatbot Sephora. (6 de 12 de 2024). Obtenido de FASTERCAPITAL: https://fastercapital.com/es/palabra-clave/chatbot-sephora.html

Cinco formas en que Coca-Cola utiliza la IA para mejorar su marketing. (7 de 12 de 2024). Obtenido de ADLATINA: https://www.adlatina.com/marketing/cinco- formas-en-que-coca-cola-utiliza-la-ia-para-mejorar-su-marketing Coca-Cola y la IA para Predecir Tendencias y Conquistar al Mundo. (9 de 12 de 2024). Obtenido de ICAPVAL: https://icapval.com/sas/coca-cola-un-caso-de- exito-en-la-aplicacion-de-ia/ Cómo afectarán al mundo las 10 tecnologías emergentes más importantes de 2024. (9 de 10 de 2024). Obtenido de WORLD ECONOMIC FORUM: https://es.weforum.org/stories/2024/07/como-afectaran-al-mundo-las-10- tecnologias-emergentes-mas-importantes-de-2024/ Cómo Duolingo usa la IA para crear lecciones más rápido. (17 de 12 de 2024). Obtenido de BLOG DUOLINGO: https://blog.duolingo.com/es/como-duolingo- usa-la-ia-para-crear-lecciones-mas-rapido/ Cómo el Diseño UX Está Evolucionando con la IA y Aumenta las Conversiones. (15 de 11 de 2024). Obtenido de +MERCA: https://publicidadymercados.com/como-el-diseno-ux-esta-evolucionando-con- la-ia-y-aumenta-las-conversiones/ Como escribir los mejores prompts en ChatGPT usando R.E.D.I.C.E. (30 de 04 de 2025). Obtenido de AcademiaSeo: https://academiaseo.net/como-escribir- mejores-prompts-en-chatgpt-usando-redice/ Cómo funciona la IA en la experiencia de usuario UX. (16 de 10 de 2024). Obtenido de MICROSOFT BING: https://www.bing.com/search?pc=OA1&q=c%C3%B3mo%20funciona%20la% 20IA%20en%20la%20experiencia%20de%20usuario%20UX Cómo funcionan los algoritmos de inteligencia artificial explicación. (5 de 10 de 2024). Obtenido de MICROSOFT BING: https://www.bing.com/search?pc=OA1&q=c%C3%B3mo%20funcionan%20lo s%20algoritmos%20de%20inteligencia%20artificial%20explicaci%C3%B3n Cómo la publicidad basada en IA generativa puede ayudar a las marcas a contar su historia e interactuar con los clientes. (15 de 12 de 2024). Obtenido de AMAZON ADS: https://advertising.amazon.com/es-es/blog/generative-ai- advertising

LUCAS MELGARES CARMONA 154

---

<!-- Página 160 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Cómo los algoritmos de IA funcionan en UX personalización análisis comportamiento diseño interfaces. (7 de 10 de 2024). Obtenido de MICROSOFT BING: https://www.bing.com/search?pc=OA1&q=c%C3%B3mo%20los%20algoritmo s%20de%20IA%20funcionan%20en%20UX%20personalizaci%C3%B3n%20 an%C3%A1lisis%20comportamiento%20dise%C3%B1o%20interfaces

Cómo se aplica la Inteligencia Artificial en los videojuegos. (6 de 12 de 2024). Obtenido de INSTITUTO DE INGENIERIA DEL CONOCIMIENTO: https://www.iic.uam.es/noticias/como-aplica-inteligencia-artificial-en- videojuegos/ De IBM Watson a watsonx. (15 de 1 de 2025). Obtenido de IBM WATSON: https://www.ibm.com/es-es/watson De los sesgos a la manipulación, la cuestión ética es ineludible en el desarrollo de la inteligencia artificial. (6 de 11 de 2025). Obtenido de REASONWHY: https://www.reasonwhy.es/actualidad/desafios-etica-moral-inteligencia- artificial-desarrollo-tecnologia Design and code beautiful products. Together. (14 de 04 de 2025). Obtenido de Penpot: https://penpot.app/ Diez formas en que la implementación de Chatbot mejora su tienda web de comercio electrónico. (18 de 2 de 1025). Obtenido de Alibaba.com READS: https://reads.alibaba.com/es/10-ways-chatbot-implementation-enhances- your-ecommerce-web-store/ Diferencias entre UX tradicional y UX impulsado por IA. (6 de 11 de 2024). Obtenido de MICROSOFT BING: https://www.bing.com/search?pc=OA1&q=Diferencias%20entre%20UX%20tr adicional%20y%20UX%20impulsado%20por%20IA Diseño UX y AI: una relación de confianza y reciprocidad. (2 de 11 de 2024). Obtenido de ASESOFTWARE: https://asesoftware.com/inteligencia-artificial- diseno-ux-y-ai/ Domino’s Pizza Enterprises entrega en tiempo récord utilizando AWS para pedidos predictivos. (7 de 1 de 2025). Obtenido de AWS: https://aws.amazon.com/es/solutions/case-studies/dominos-case-study/ Ejemplo de rediseño de un sitio web o aplicación: El caso de AirBnB. (8 de 1 de 2025). Obtenido de KEEPCODING: https://keepcoding.io/blog/rediseno-de- un-sitio-web-o-aplicacion-ejemplo/ El 64% de los consumidores españoles de Amazon lo compra casi todo en el propio marketplace. (26 de 04 de 2025). Obtenido de Marketing4;eCommerce:

LUCAS MELGARES CARMONA 155

---

<!-- Página 161 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

https://marketing4ecommerce.net/el-64-de-los-consumidores-espanoles-de- amazon-lo-compra-casi-todo-en-el-propio-marketplace/ El Impacto de la IA en el Diseño UX este 2024. (8 de 11 de 2024). Obtenido de ANDREA SANZ: https://andreasanzsanchez.es/el-impacto-de-la-ia-en-el- diseno-ux-este-2024/

El impacto de la inteligencia artificial en los negocios: Caso de estudio de Coca-Cola. (7 de 1 de 2025). Obtenido de TOOLIFY.AI: https://www.toolify.ai/es/ai-news- es/el-impacto-de-la-inteligencia-artificial-en-los-negocios-caso-de-estudio-de- cocacola-2086694 El papel de la inteligencia artificial en el diseño UX/UI. (7 de 2 de 2025). Obtenido de IRONHACK: https://www.ironhack.com/es/blog/el-papel-de-la-inteligencia- artificial-en-el-diseno-ux-ui El papel de la inteligencia artificial en los videojuegos. (8 de 12 de 2024). Obtenido de THE GOOD GAMER: https://thegoodgamer.es/el-papel-de-la-inteligencia- artificial-en-los-videojuegos/ El uso de la inteligencia artificial en UX/UI. (7 de 10 de 2024). Obtenido de KEEPCODING: https://keepcoding.io/blog/inteligencia-artificial-en-ux-ui/ El UX (Experiencia de Usuario) en los Tiempos de la Inteligencia Artificial. (8 de 10 de 2024). Obtenido de UX EN ESPAÑOL: https://uxenespanol.com/articulo/el-ux-experiencia-de-usuario-en-los- tiempos-de-la-inteligencia-artificial El UX (Experiencia de Usuario) en los Tiempos de la Inteligencia Artificial. (18 de 11 de 2024). Obtenido de UX EN ESPAÑOL: https://uxenespanol.com/articulo/el-ux-experiencia-de-usuario-en-los- tiempos-de-la-inteligencia-artificial Esta startup china de Inteligencia Artificial quiere revolucionar la manera en la que se estudia en los colegios, pero sin sustituir profesores. (7 de 12 de 2024). Obtenido de BUSINESS INSIDER: https://www.businessinsider.es/squirrel-ai- inteligencia-artificial-revolucionar-colegios-472481 Estadísticas del mercado de Amazon 2024. (26 de 04 de 2025). Obtenido de eDesk: https://www.edesk.com/es/blog/estadisticas-amazon/ Ética | MIT Technology Review. (9 de 1 de 2025). Obtenido de MIT Technology Review: https://www.technologyreview.es/c/etica Ética en IA: Los Desafíos Morales de la Inteligencia Artificial. (28 de 11 de 2024). Obtenido de LOVETECHNOLOGY: http://lovtechnology.com/etica-en-ia-los- desafios-morales-de-la-inteligencia-artificial/

LUCAS MELGARES CARMONA 156

---

<!-- Página 162 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Ética en la Inteligencia Artificial Empresarial. (29 de 11 de 2024). Obtenido de ADEN: https://www.aden.org/business-magazine/etica-en-la-inteligencia-artificial- empresarial/ Ética y retos en la implementación de la IA en UX. (30 de 11 de 2024). Obtenido de MICROSOFT BING:

https://www.bing.com/search?pc=OA1&q=%C3%89tica%20y%20retos%20en %20la%20implementaci%C3%B3n%20de%20la%20IA%20en%20UX Evolución de la IA a través de la Historia. (7 de 10 de 2024). Obtenido de TADIA : https://www.tadia.ai/evolucion-de-la-ia-a-traves-de-la-historia-cronologia/ Explorador de casos de uso de IA. (29 de 1 de 2025). Obtenido de AWS: https://aws.amazon.com/es/ai/use-cases/?use-cases.sort- by=item.additionalFields.priority&use-cases.sort-order=asc&awsf.use-case- area=*all&awsf.industry=*all&awsf.business-function=*all&awsf.business- outcome=*all&awsf.type=*all Guía de Evaluación Heurística de Sitios Web. (10 de 05 de 2025). Obtenido de NSU (No Solo Usabilidad): https://www.nosolousabilidad.com/articulos/heuristica.htm Habilidades de IA que todo diseñador UX/UI necesita. (13 de 2 de 2025). Obtenido de IRONHACK: https://www.ironhack.com/es/blog/habilidades-de-ia-que- todo-disenador-ux-ui-necesita Historia de la inteligencia artificial: del origen al futuro de la tecnología. (6 de 10 de 2024). Obtenido de PARETO: https://blog.pareto.io/es/historia-de-la- inteligencia-artificial/ HubSpot. (s.f.). Obtenido de UX: guía completa sobre la experiencia de usuario: https://blog.hubspot.es/website/experiencia-de-usuario-ux#que-es IA en Gaming. (6 de 12 de 2024). Obtenido de GLOBANT: https://www.globant.com/es/tech-terms/ia-en-gaming IA en la industria de los videojuegos. (8 de 12 de 2024). Obtenido de IBERTECH: https://www.ibertech.org/ia-en-la-industria-de-los-videojuegos/ IA UX/UI: La revolución de la inteligencia artificial en el diseño de Apps. (3 de 10 de 2024). Obtenido de DOONAMIS: https://www.doonamis.com/ia-uxui-diseno- apps/ IA y UX: Cómo la IA está mejorando la experiencia del usuario. (4 de 10 de 2024). Obtenido de UXICANS: https://uxicans.com/influencia-y-persuasion/ia-y-ux- como-la-ia-esta-mejorando-la-experiencia-del-usuario/

LUCAS MELGARES CARMONA 157

---

<!-- Página 163 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

IBM Watson Health vs Google DeepMind Health: Soluciones de IA para diagnóstico médico. (6 de 12 de 2024). Obtenido de HERRAMIENTAS-IA: https://herramientas-ia.com/ibm-watson-health-vs-google-deepmind-health/ Impacto de la inteligencia artificial en el diseño de experiencia de usuario UX 2024. (8 de 11 de 2024). Obtenido de BING:

https://www.bing.com/search?pc=OA1&q=impacto%20de%20la%20inteligenc ia%20artificial%20en%20el%20dise%C3%B1o%20de%20experiencia%20de %20usuario%20UX%202024 Impacto de la inteligencia artificial en UX UI en la transformación digital en España. (8 de 11 de 2024). Obtenido de DINOBRAIN ARTIFICIAL INTELLIGENCE: https://blog.dinobrain.ai/inteligencia-artificial-ux-ui/ Implementación de Chatbots con GPT-4 en Atención al Cliente. (18 de 12 de 2024). Obtenido de ICEMD ESIC: https://icemd.esic.edu/knowledge/articulos/implementacion-de-chatbots-con- gpt-4-en-atencion-al-cliente/ Innovación y creatividad en el diseño de videojuegos: el uso de la IA. (7 de 12 de 2024). Obtenido de UNIVERSIDAD DE DISEÑO, INNOVACIÓN Y TECNOLOGÍA: https://udit.es/actualidad/innovacion-y-creatividad-en-el- diseno-de-videojuegos-el-uso-de-la-ia/ Inteligencia artificial (videojuegos). (6 de 12 de 2024). Obtenido de WIKIPEDIA: https://es.wikipedia.org/wiki/Inteligencia_artificial_%28videojuegos%29 Inteligencia artificial : definición, historia, usos, peligros. (7 de 10 de 2024). Obtenido de DataScientest: https://datascientest.com/es/inteligencia-artificial-definicion Inteligencia artificial de Salesforce. (30 de 1 de 2025). Obtenido de SALESFORCE: https://www.salesforce.com/mx/artificial-intelligence/ Inteligencia Artificial en el Diseño y UX: Innovaciones para 2024. (6 de 11 de 2024). Obtenido de MAXINET: https://maxinext.com/desarrollo-web/inteligencia- artificial/ Inteligencia artificial en videojuegos: una mirada al pasado y futuro de la industria. (1 de 12 de 2024). Obtenido de IAT: https://iat.es/tecnologias/inteligencia- artificial/videojuegos/ Inteligencia artificial reemplazó estos trabajos en la industria de los videojuegos. (2 de 12 de 2024). Obtenido de INFOBASE: https://www.infobae.com/tecno/2024/03/19/inteligencia-artificial-reemplazo- estos-trabajos-en-la-industria-de-los-videojuegos/

LUCAS MELGARES CARMONA 158

---

<!-- Página 164 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Inteligencia Artificial: ¿Qué es y Cómo Funciona? (2 de 10 de 2024). Obtenido de CULTURAAI: https://culturaai.com/inteligencia-artificial-que-es-y-como- funciona/ Introducción a TensorFlow. (1 de 1 de 2025). Obtenido de TENSORFLOW: https://www.tensorflow.org/learn?hl=es-419

La Ética en la Inteligencia Artificial: Consideraciones y Debates Actuales. (1 de 11 de 2024). Obtenido de LOVETECHNOLOGY: https://lovtechnology.com/la-etica- en-la-inteligencia-artificial-consideraciones-y-debates-actuales/ La experiencia de usuario (UX): qué es, disciplinas y ejemplos. (3 de 9 de 2024). Obtenido de POCION DIGITAL: https://pociondigital.com/blog/experiencia-de- usuario-ux/ La IA en el Diseño de Experiencia de Usuario (UX): Mejorando la Interfaz del Usuario. (2 de 10 de 2024). Obtenido de Q2B STUDIO: https://www.q2bstudio.com/nuestro-blog/299/ia-en-diseno-ux-mejorando- interfaz-usuario La IA en los videojuegos: dando forma al futuro de los videojuegos. (3 de 12 de 2024). Obtenido de ULTRALYTICS: https://www.ultralytics.com/es/blog/ai-in- video-games-shaping-the-future-of-gaming La IA ya está ocupando puestos de trabajo en la industria de los videojuegos. (4 de 12 de 2024). Obtenido de WIRED: https://es.wired.com/articulos/ia-ya-esta- ocupando-puestos-de-trabajo-en-la-industria-de-los-videojuegos La importancia de Hugging Face. (6 de 1 de 2025). Obtenido de ATHOS CAPITAL: https://www.athos-cap.com/post-12-la-importancia-de-hugging-face/ La industria del gaming tiene un amor-odio por la IA. (15 de 12 de 2024). Obtenido de EXPANSIÓN: https://expansion.mx/tecnologia/2024/07/24/claroscuros- inteligencia-artificial-en-industria-videojuegos La Inteligencia Artificial en el E-commerce. (5 de 12 de 2024). Obtenido de GBITCORP: https://gbitcorp.com/blog/posts/la-inteligencia-artificial-en-el-e- commerce/ La inteligencia artificial en videojuegos. (6 de 12 de 2024). Obtenido de TOKIO: https://www.tokioschool.com/noticias/inteligencia-artificial-videojuegos/ La revolución del diseño: cómo la IA transforma la experiencia de usuario. (s.f.). Obtenido de NOVICELL: https://www.novicell.es/es/blog/ia-experiencia-de- usuario La revolución del diseño: cómo la IA transforma la experiencia de usuario. (s.f.). Obtenido de NOVICELL: https://www.novicell.es/es/blog/ia-experiencia-de- usuario

LUCAS MELGARES CARMONA 159

---

<!-- Página 165 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

La revolución del diseño: cómo la IA transforma la experiencia de usuario. (7 de 10 de 2024). Obtenido de NOVICELL: https://www.novicell.es/es/blog/ia- experiencia-de-usuario Las 10 Tecnologías Emergentes. (7 de 10 de 2024). Obtenido de MIT Technology Review: https://www.technologyreview.es/listas/tecnologias-emergentes/2024

Las 10 tendencias tecnológicas estratégicas para 2024 según Gartner. (5 de 10 de 2024). Obtenido de BISMART: https://blog.bismart.com/10-tendencias- tecnologia-2024 Lecciones de personalización: lo que Netflix puede enseñar a los equipos de marketing y ventas. (8 de 12 de 2024). Obtenido de ENTREPRENEUR: https://www.entrepreneur.com/es/marketing/lecciones-de-personalizacion-lo- que-netflix-puede/425566 Mejora continua – logrando que la buena gestión se convierta en un hábito para los líderes. (9 de 1 de 2024). Obtenido de McKinsey & Company: https://www.mckinsey.com/capabilities/operations/our-insights/continuous- improvement-make-good-management-every-leaders-daily-habit/es-ES Optimización de modelos de TensorFlow. (4 de 1 de 2024). Obtenido de TENSORFLOW: https://www.tensorflow.org/model_optimization/guide?hl=es- 419 PARENTE, D. (18 de 12 de 2024). El Impacto de la Inteligencia Artificial en la Industria de los Videojuegos en 2024. Obtenido de DANIEL PARENTE: https://www.danielparente.net/es/2024/05/25/el-impacto-de-la-inteligencia- artificial-en-la-industria-de-los-videojuegos-en-2024/ Penpot: The open-source design tool for design and code collaboration. (14 de 04 de 2025). Obtenido de GitHub: https://github.com/penpot/penpot?utm_source= Perfil de la empresa Runway ML: Líder en conversión de texto en vídeo. (7 de 1 de 2025). Obtenido de SKIM AI: https://skimai.com/es/runway-ml-perfil-de- empresa-lider-en-conversion-de-texto-en-video/ Personalized Marketing: Spotify y su estrategia de personalización. (27 de 12 de 2024). Obtenido de MOKA: https://mokaletstalk.com/personalized-marketing- spotify/ Plans for any business size. (14 de 04 de 2025). Obtenido de MockFlow: https://mockflow.com/pricing/?utm_source= Principales tendencias tecnológicas para 2024: IA, computación cuántica y sostenibilidad. (5 de 10 de 2024). Obtenido de REVISTA C-LEVEL: https://revistaclevel.com/principales-tendencias-tecnologicas-para-2024-ia- computacion-cuantica-y-sostenibilidad

LUCAS MELGARES CARMONA 160

---

<!-- Página 166 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Publicidad programática. (6 de 12 de 2024). Obtenido de AMAZON ADS: https://advertising.amazon.com/es-es/blog/programmatic-advertising Qué es la Inteligencia Artificial. (19 de Abirl de 2023). Obtenido de Plan de Recuperación, Transformación y Resiliencia: https://planderecuperacion.gob.es/noticias/que-es-inteligencia-artificial-ia-prtr

Qué es la inteligencia artificial en videojuegos. (28 de 12 de 2024). Obtenido de UNIVERSIDAD EUROPEA: https://creativecampus.universidadeuropea.com/blog/inteligencia-artificial- videojuegos/ Qué es un mockup. (14 de 04 de 2025). Obtenido de Miro: https://miro.com/es/mockup/que-es-mockup/ Qué es una landing page, para qué sirve y qué tipos existen. (16 de 04 de 2025). Obtenido de HubSpot: https://blog.hubspot.es/website/landing-page Qué Son y Cómo Funcionan los Algoritmos de Inteligencia Artificial. (26 de 10 de 2024). Obtenido de INTELIGEN ARTIFICIAL: https://inteligenartificial.com/inteligencia-artificial/que-son-y-como-funcionan- los-algoritmos-de-inteligencia-artificial/ Soluciones de tejido de datos. (6 de 1 de 2025). Obtenido de IBM: https://www.ibm.com/es-es/data- fabric?utm_content=SRCWW&p1=Search&p4=43700081258914859&p5=p& p9=58700008826344331&gad_source=1&gclid=EAIaIQobChMI48zmjs- qiwMV2mlBAh0h6goUEAAYASAAEgLqTfD_BwE&gclsrc=aw.ds Spotify trabaja en una herramienta para crear anuncios personalizados con IA generativa. (6 de 12 de 2024). Obtenido de PORTALTIC: https://www.europapress.es/portaltic/internet/noticia-spotify-trabaja- herramienta-crear-anuncios-personalizados-ia-generativa- 20240614114843.html Te presentamos la generación IA. (7 de 1 de 2025). Obtenido de ADOBE: https://www.adobe.com/es/sensei/generative-ai.html Tech Trends 2025. (17 de 1 de 2025). Obtenido de DELOITTE INSIGHTS: https://www2.deloitte.com/us/en/insights/focus/tech-trends.html Tecnologías emergentes similares IA. (8 de 10 de 2024). Obtenido de MICROSOFT BING: https://www.bing.com/search?pc=OA1&q=tecnolog%C3%ADas%20emergent es%20similares%20IA%202024 TensorFlow. (3 de 1 de 2025). Obtenido de WIKIPEDIA: https://ca.wikipedia.org/wiki/TensorFlow

LUCAS MELGARES CARMONA 161

---

<!-- Página 167 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

Tipos de IA más utilizados en la experiencia de usuario. (18 de 10 de 2024). Obtenido de MICROSOFT BING: https://www.bing.com/search?pc=OA1&q=tipos%20de%20IA%20m%C3%A1 s%20utilizados%20en%20la%20experiencia%20de%20usuario Tipos de Inteligencia Artificial —ejemplos en atención al cliente. (8 de 10 de 2024).

Obtenido de ZENDESK: https://www.zendesk.es/blog/tipos-de-sistemas-de- inteligencia-artificial/ Turn product ideas into concepts instantly with GenAI. (14 de 04 de 2025). Obtenido de Uizard.io: https://uizard.io/ Two Figma AI Plugins Every Designer Should Know. (14 de 04 de 2025). Obtenido de Medium: https://uxplanet.org/figma-ai-plugins-39a48a181f6 UI design software for everyone. (14 de 04 de 2025). Obtenido de Visily.ai: https://www.visily.ai/ Uizard Review: AI Features, Use Cases, And Alternatives. (14 de 04 de 2025). Obtenido de Banani: https://www.banani.co/blog/uizard-ai- review?utm_source= Uso de la inteligencia artificial en la personalización de la experiencia del usuario en plataformas digitales. (12 de 03 de 2025). Obtenido de Google Scholar: https://www.polodelconocimiento.com/ojs/index.php/es/article/view/5738 UX. (12 de 2 de 2025). Obtenido de Google: https://www.google.com/search?q=La+experiencia+de+usuario+se+refiere+al +conjunto+de+percepciones+y+sensaciones+del+usuario+en+el+uso+de+un +determinado+producto%2C+servicio+o+sistema&oq=La+experiencia+de+us uario+se+refiere+al+conjunto+de+percepciones+y+sen Websim.ai que es. (7 de 05 de 2025). Obtenido de GOOGLE: https://www.google.com/search?q=websim+.ai+que+es&oq=websim+.ai+que +es&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yBwgCEAAY7 wUyCggDEAAYgAQYogQyCggEEAAYgAQYogQyCggFEAAYgAQYogTSAQ g0MTA1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8 Zalando lanza su asistente de IA en España: ofrece recomendaciones personalizadas y aprende de los usuarios. (8 de 12 de 2024). Obtenido de MARKETING ECOMMERCE: https://marketing4ecommerce.net/zalando- asistente-ia-espana/

LUCAS MELGARES CARMONA 162

---

<!-- Página 168 -->

Lucas Melgares Carmona Uso de la IA en técnicas de experiència de usuario

LUCAS MELGARES CARMONA 163