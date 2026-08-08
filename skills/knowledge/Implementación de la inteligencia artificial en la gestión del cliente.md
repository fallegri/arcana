<!-- Página 1 -->

Implementación de la Inteligencia Artificial en la gestión del cliente

Isabela González Vargas, Andrés Felipe Ruiz Henao

Asesora: Manuela Escobar Sierra

Facultad de ciencias económicas y administrativas

Universidad de Medellín

2025

---

<!-- Página 2 -->

Contenido

Resumen.......................................................................................................................................... 4 Abstract ........................................................................................................................................... 4 Introducción .................................................................................................................................... 5 Planteamiento del problema ............................................................................................................ 6 Justificación .................................................................................................................................... 7 Conceptualización ........................................................................................................................... 8 Inteligencia Artificial .................................................................................................................. 8 Machine learning ........................................................................................................................ 9 Big data ..................................................................................................................................... 10 Marco teórico ................................................................................................................................ 11 Análisis Bibliométrico: Relaciones entre Conceptos Gestión de Clientes e Inteligencia Artificial .................................................................................................................................... 11 1. PROTOCOLO DE BÚSQUEDA: BÚSQUEDA Y EXTRACCIÓN DE DOCUMENTOS 12 2. ANÁLISIS DE CO-OCURRENCIA ................................................................................ 13 2.1. MAPA DE CO-OCURRENCIA DE CONCEPTOS ...................................................... 14 2.2. FAMILIA DE TÉRMINOS ............................................................................................ 14 3. CLASIFICACIÓN NARRATIVA DE ARTÍCULOS POR CLUSTERS PRINCIPALES 15 3.1. ANÁLISIS DE EVOLUCIÓN TEMPORAL ................................................................. 24 Objetivos ....................................................................................................................................... 27 Objetivo General: ...................................................................................................................... 27 Objetivos Específicos: ............................................................................................................... 27 Metodología .................................................................................................................................. 27 Tipo de información .................................................................................................................. 27 Reconocimiento entidad nombrada............................................................................... 28 Detección de emociones ............................................................................................... 30 Algoritmo LDA ............................................................................................................. 31 Resultados ..................................................................................................................................... 33 Interpretación exhaustiva de términos destacados en la minería de texto................................. 33 1. AI (Inteligencia Artificial) ................................................................................................. 33

---

<!-- Página 3 -->

2. Generative (Generativa) .................................................................................................... 34 3. Customer/Customers (Cliente/Clientes) ............................................................................ 34 4. Data (Datos) ....................................................................................................................... 35 5. Service (Servicio) .............................................................................................................. 35 6. Agents (Agentes) ............................................................................................................... 36 7. Marketing........................................................................................................................... 36 8. Content (Contenido) .......................................................................................................... 36 9. Experience (Experiencia) .................................................................................................. 37 10. Conversational (Conversacional) .................................................................................... 37 11. Using/Use (Usando/Uso) ................................................................................................. 38 12. Tools (Herramientas) ....................................................................................................... 38 13. Help (Ayuda) ................................................................................................................... 39 14. Think/Really/Right (Pensar/Realmente/Correcto) .......................................................... 39 15. Well (Bien) ...................................................................................................................... 39 16. Tech/Technology (Tecnología) ....................................................................................... 40 17. Super ................................................................................................................................ 40 18. User (Usuario) ................................................................................................................. 40 19. People (Personas) ............................................................................................................ 41 20. Look (Mirar) .................................................................................................................... 41 21. Celeste/Carol/Scooter ...................................................................................................... 42 22. Yeah (Sí) .......................................................................................................................... 42 23. Actually (Realmente) ....................................................................................................... 42 Conclusiones ................................................................................................................................. 43 Impacto de la IA en la Gestión de Clientes ............................................................................... 44 Tecnologías Emergentes y su Adopción ................................................................................... 44 Desafíos y Barreras de Implementación.................................................................................... 45 Recomendaciones para la Implementación ............................................................................... 45 Futuras Líneas de Investigación ................................................................................................ 46 Bibliografía ................................................................................................................................... 47

---

<!-- Página 4 -->

Resumen

El acelerado desarrollo de las tecnologías de inteligencia artificial (IA) está transformando la manera en que las organizaciones interactúan con sus clientes. Según Davenport y Ronanki (2018), el 84% de las empresas considera que la IA les proporcionará una ventaja competitiva significativa. Sin embargo, su aplicación estratégica y sostenible en la gestión de relaciones con los clientes (CRM) permanece subestimada. Este estudio tiene como objetivo general determinar el impacto de la implementación de tecnologías de IA en la gestión de relaciones con clientes y estrategias de marketing empresarial. El marco teórico se fundamenta en los conceptos de automatización inteligente, toma de decisiones basada en datos y estrategias centradas en el cliente. La metodología incluye un análisis bibliométrico para mapear las tendencias más relevantes en la literatura científica sobre IA y CRM, seguido de un análisis de contenido de 197 artículos científicos. Para la búsqueda narrativa se profundizó en artículos de selección selectiva que muestran operaciones de procesamiento de lenguaje natural (PLN), segmentación latente de Dirichlet (LDA) y detección de emociones para extraer y evaluar las tendencias emergentes, patrones de implementación y resultados obtenidos. Las principales variables vinculadas a cinco categorías: automatización, personalización, predicción, comprensión emocional y mejoramiento de la experiencia del cliente, las cuales han sido claves en la mejora del potencial de revitalización de la gestión de clientes para permitir experiencias anticipadas, adaptativas y emocionalmente inteligentes.

Abstract

The accelerated development of artificial intelligence (AI) technologies is transforming the way organizations interact with their customers. However, its strategic and sustainable application in customer relationship management (CRM) remains underexplored. This study aims to characterize how AI contributes to the evolution of customer management processes through an integrative approach. The theoretical framework is based on intelligent automation, data-driven decision-making, and customer-centric strategies. The methodology included a bibliometric analysis to map the most relevant trends in the scientific literature on AI and CRM, followed by text mining and content analysis of a corpus of 197 academic articles. For the in-depth narrative

---

<!-- Página 5 -->

analysis, a representative sample of 25 key articles was selected, allowing for the identification of core topics and emotional clusters. Natural language processing (NLP), latent Dirichlet allocation (LDA), and emotion detection models were applied to extract and interpret thematic and affective patterns. The results validated five key categories: automation, personalization, prediction, emotional understanding, and ethical concerns. The study concludes that AI has the potential to revolutionize CRM by enabling anticipatory, adaptive, and emotionally intelligent customer experiences. Future research should focus on evaluating implementation models by sector and assessing the performance impact of AI-driven CRM strategies.

Palabras clave: Inteligencia Artificial (IA) · Machine learning (aprendizaje automático) · Big Data (macrodatos) · Procesamiento del Lenguaje Natural (NLP) · Analítica de Datos · Automatización

Introducción

La cuarta revolución industrial, a menudo denominada Industria 4.0, describe la integración de las tecnologías emergentes y las herramientas digitales en toda la cadena de valor de la fabricación, basándose en los sistemas ciberfísicos (SCF). Sin embargo, la cuarta revolución industrial no debe concebirse únicamente en términos de fábricas basadas en IoT (Internet de las cosas). Debido a que es necesario reconocer el uso revolucionario de la inteligencia artificial (IA) como motor principal, y tener en cuenta que las interacciones más naturales entre humanos y máquinas representan una nueva forma de trabajar, más allá de los límites de la empresa a lo largo del ciclo de vida del producto (Meindl & Mendonça, 2021). Esto causa que la llegada de la IA transforme profundamente el panorama de las interacciones entre las empresas y sus clientes. De esta forma, en el centro de dicha transformación se encuentra la gestión de clientes y la personalización de la experiencia del mismo, un ámbito en el que la IA está desempeñando un papel cada vez más destacado (Timimi et al., 2025).

Igualmente, la IA se ha integrado en áreas clave como la administración y el marketing principalmente, gracias a herramientas como el aprendizaje automático y el procesamiento del lenguaje natural (NLP) que permiten el análisis de grandes volúmenes de datos en tiempo real,

---

<!-- Página 6 -->

mejorando la segmentación y la optimización de campañas publicitarias (Henostroza Diaz & Marquez Yauri, 2025). Este hecho ha despertado cierto interés académico y profesional, por las implicaciones que trae consigo en la relación entre consumidores y marcas, puesto que interviene en gran medida la satisfacción del cliente. Es en este punto en donde la implementación de la IA en herramientas como la gestión de relaciones con el cliente (CMR), cobra tanta relevancia, porque es posible automatizar procesos repetitivos y aportar información valiosa y oculta para llevar la gestión de clientes al siguiente nivel (Alladi, 2024).

Además, comprender la forma en la que se están aplicando estas tecnologías en temas relacionados, qué cambios están generando y su respectivo impacto se ha vuelto una necesidad latente para quienes estudian el comportamiento del consumidor, la gestión de clientes, el marketing y la innovación. Ahora bien, para que sea posible obtener un entendimiento de lo anterior, en este proyecto se podrá encontrar una revisión de literatura, un análisis bibliométrico y técnicas de minera de texto con el objetivo de proporcionar una visión completa que pueda capturar las principales tecnologías involucradas, tendencias emergentes, sus ventajas, desafíos, y el valor estratégico de la analítica de datos en la toma de decisiones dentro de las empresas que utilizan IA en sus procesos.

Planteamiento del problema

A lo largo de los últimos años, la gestión de clientes ha sido una de las áreas más beneficiadas por la transformación digital. Según Kumar y Reinartz (2016), las empresas que implementan estrategias de CRM basadas en datos experimentan un incremento promedio del 41% en sus ingresos por cliente. Los avances en robótica e inteligencia artificial han permitido a las máquinas realizar tareas cada vez más complejas (Russell y Norvig, 2020). Por tanto, muchas organizaciones están optando por aprovechar algunas herramientas proporcionadas por la IA en sus estrategias relacionadas a la experiencia del cliente. Dado que la IA permite recopilar y analizar datos de clientes de manera predictiva, segmentación, CRM, chatbots, análisis de sentimientos y automatización de procesos (Syam & Sharma, 2018)

De acuerdo con el informe de Salesforce (2023), el 67% de los líderes de marketing ya utilizan IA, y este porcentaje se espera que aumente al 84% en los próximos dos años. Sin embargo,

---

<!-- Página 7 -->

McKinsey & Company (2023) reporta que solo el 23% de las empresas ha escalado exitosamente las iniciativas de IA más allá de las fases piloto.

A pesar del gran avance que supone la Inteligencia Artificial en términos empresariales para la mejora de los procesos, aún persisten desafíos significativos en cuanto a su evaluación profunda y sistemática de su impacto real en la gestión del cliente. Específicamente en países latinoamericanos como el caso de Colombia, donde los recursos, capacidades tecnológicas y propiedades estratégicas pueden diferir considerablemente respecto a contextos globales. Por ello, es pertinente conocer cómo contribuyen las tecnologías de Inteligencia Artificial a la transformación de la gestión del cliente en el contexto actual de la digitalización empresarial.

En este sentido, surge la necesidad de examinar cómo se están integrando las tecnologías basadas en IA dentro de las prácticas empresariales orientadas al cliente, y cuál es su verdadero impacto en este campo. A partir de lo anterior, se formula la siguiente pregunta problema:

¿Cómo contribuyen las tecnologías de Inteligencia Artificial a la transformación de la gestión del cliente en el contexto actual de la digitalización empresarial?

Justificación

En un contexto empresarial cada vez más digitalizado, la gestión de clientes ha experimentado una evolución dirigida hacia modelos más proactivos, inteligentes y personalizados. Según Verhoef et al. (2021), la llegada de tecnologías como la Inteligencia Artificial, el aprendizaje automático, el procesamiento de lenguaje natural y el análisis de Big Data ha transformado fundamentalmente la forma en que las organizaciones realizan sus procesos de comprensión, interacciones y fidelización con sus clientes.

La relevancia de esta investigación se sustenta en la creciente adopción de estas tecnologías y su impacto demostrable en el desempeño empresarial. De acuerdo con PwC (2023), las empresas que implementan IA en sus procesos de marketing experimentan un incremento promedio del 37% en sus tasas de conversión, mientras que el mercado global de IA en marketing se valoró en $27.4 mil millones en 2023 y se proyecta alcanzar $78.8 mil millones para 2030 según Grand View Research (2024). En el contexto colombiano, MinTIC (2023) reporta que el 45% de las empresas

---

<!-- Página 8 -->

medianas y grandes han iniciado proyectos de transformación digital que incluyen componentes de IA, evidenciando la urgencia de comprender mejor estos fenómenos en el ámbito nacional.

Sin embargo, a pesar de esta creciente adopción, existe una brecha significativa en la comprensión sistemática del impacto real de estas tecnologías en la gestión de relaciones con clientes. Davenport y Ronanki (2018) señalan que mientras muchas organizaciones invierten en IA, pocas han logrado escalar exitosamente estas implementaciones más allá de proyectos piloto. Esta situación genera la necesidad de investigación que analice cómo estas tecnologías emergentes de gran impacto están transformando efectivamente la experiencia del cliente, desde los procesos de automatización de servicios hasta la predicción y análisis de comportamientos y emociones.

La justificación teórica de este estudio radica en la necesidad de consolidar el conocimiento disperso sobre la aplicación de IA en marketing y CRM, proporcionando un marco comprensivo que permita a las organizaciones tomar decisiones informadas sobre la implementación de estas tecnologías. Desde una perspectiva práctica, los resultados de esta investigación pueden orientar a empresas colombianas en la optimización de sus estrategias de gestión de clientes, contribuyendo al desarrollo de ventajas competitivas sostenibles en un entorno empresarial cada vez más digitalizado.

Conceptualización

Inteligencia Artificial

Para comprender el concepto de inteligencia artificial (IA), se debe recurrir a lo sugerido por uno de los padres fundadores de este campo. John McCarthy, fue el primero en mencionar el término en el año 1956. Su idea se centraba en la rama de la informática dedicada al diseño de máquinas, con el fin de que estas tuvieran la capacidad de emular algunas conductas humanas, etiquetadas como inteligentes (Benhamou, 2022). Sin embargo, no se tiene una definición estándar para el término. Aun así, es posible encontrar diferentes autores que se refieren a la inteligencia artificial, como sistemas que pueden imitar la operación del razonamiento humano; mientras que otros se centran principalmente en la utilización de estas herramientas, como apoyo para la

---

<!-- Página 9 -->

resolución de problemas (Del Carmen Sosa Sierra, 2007). Mediante la capacidad de pensar, usando la lógica. Por otro lado, la inteligencia artificial es esencial dentro del proceso productivo de una gran parte de dispositivos tecnológicos. Debido a que colabora a la búsqueda e implementación de materiales capaces de satisfacer las necesidades de los seres humanos de una forma más eficaz y al mismo tiempo eficiente. No obstante, su uso no se limita al sector industrial enfocado en la parte manufacturera, dado que su presencia es relevante en sectores sociales como el de la salud, seguridad y educación para ayudar al análisis e identificación de oportunidades de mejora en los programas ofrecidos al público (Aparecido Claudio, 2024).

Machine learning

A pesar de que los principios de la IA sean de larga data, hay un paso significativo que se ha dado en los últimos años: una de las ramas de la IA, denominada Machine learning o aprendizaje automático. Este enfoque se centra procedimientos basados en patrones de datos, que permiten a las computadoras la creación de algoritmos a partir de dichos datos, de manera automática (Benhamou, 2022).

Además, el machine learning hace referencia a una técnica destinada a optimizar el rendimiento de un sistema. Mediante la adquisición de experiencia, materializada en forma de datos. Allí el aprendizaje automático, desarrolla un papel importante debido a que su tarea principal se basa en la construcción de algoritmos, que generen modelos a partir de datos. Para que posteriormente se puedan realizar predicciones (Zhou, 2021). En la actualidad, se han llevado a cabo diversos modelos que implementan esta técnica, logrando superar la precisión humana en algunas tareas específicas como lo es el reconocimiento de objetos en imágenes. El desarrollo de modelos de machine learning exige adecuaciones específicas que dependen de la problemática abordada y del origen de la información. Adicionalmente, existe una rama perteneciente al machine learning denominada Procesamiento del Lenguaje Natural (Natural Language Processing (NLP)). La cual actúa como una herramienta enfocada en el análisis e interpretación de textos (Omar et al., 2022).

---

<!-- Página 10 -->

Big data

El Big Data o macrodatos, son datos masivos que surgen a partir de la interacción producida con otros dispositivos que se encuentran interconectadas. Estos datos se procesan mediante métodos computacionales y algunos numéricos. Se caracterizan por su gran volumen, su velocidad al ser generados prácticamente en tiempo real, por su variedad en cuanto a tipos de datos y fuentes (Gontero & Menéndez, 2021). Actualmente, este término ha dejado de ser un tema netamente relacionado a una gran cantidad de datos. Dado que ha tenido grandes avances, hasta el punto de convertirse en un objeto presente en los medios de comunicación diarios. Además, el Big Data es un factor de interés para diversos sectores económicos y organizaciones (Ortiz Morales et al., 2015).

El Big Data es importante para la sociedad actual. Puesto que se ha convertido en un modelo que se caracteriza por los constantes procesos de digitalización, automatización y gestión del conocimiento dentro de todo tipo de ámbito perteneciente a la sociedad. Además, el Big data representa un ecosistema donde se facilita la generación y obtención de datos, especialmente no estructurados, y se promueve la interacción horizontal, vertical y la generación de inteligencia procesable. (Vargas Pérez & Peñalosa Figueroa, 2019). Por otro lado, el Big Data adquiere importancia en la producción de datos masivos resultantes de redes de sensores y dispositivos, como lo es la actividad diaria de los usuarios vía internet. Por esta razón, dichos datos generan un aporte significativo de información sobre una gran variedad de procesos. Desde la movilidad de la población mediante el registro de teléfonos móviles, o el consumo como tal, a través de las transacciones de tarjetas de crédito, hasta procesos ambientales como la contaminación del aire detectada por sensores localizados en las diferentes ciudades (Puebla, 2018).

Finalmente, es claro mencionar un concepto conocido y necesario en el campo del Big Data, llamado Analítica de Datos. Alude al proceso de estudio y procesamiento de datos masivos mediante funciones tecnológicas como la gestión de datos, minería de textos, programación de código abierto, análisis estadísticos, análisis de sentimientos, análisis de series temporales, entre otros (Dos Santos & Carvalho, 2023). La utilización de esta herramienta ayuda a identificar y

---

<!-- Página 11 -->

comprender patrones, posibles correlaciones entre variables y tendencias. Para realizar un proceso de toma de decisiones asertivo basado en información precisa. Adicionalmente, el Big Data es clave para que se pueda llevar a cabo el proceso de Machine Learning para que este pueda aprender de los diferentes conjuntos de datos y a su vez mejorar las predicciones y modelos conforme pasa el tiempo (Moodley, 2024).

Marco teórico

Análisis Bibliométrico: Relaciones entre Conceptos Gestión de Clientes e Inteligencia Artificial

El análisis bibliométrico constituye una herramienta crucial en la exploración del creciente campo de la Inteligencia Artificial (IA) aplicada a la gestión de clientes. Esta metodología nos permite examinar de manera sistemática y cuantitativa la evolución y el estado actual de la investigación en esta intersección tecnológica y empresarial.

En el contexto de la IA y la gestión de clientes, el análisis bibliométrico ofrece varias ventajas significativas como el mapeo de tendencias para identificar las áreas emergentes y las tecnologías de IA más prometedoras en la gestión de relaciones con clientes. Asimismo, la evolución temporal, que permite trazar la progresión histórica de conceptos clave, desde los primeros sistemas CRM hasta las actuales soluciones basadas en aprendizaje automático y procesamiento del lenguaje natural (PLN). También hace posible visualizar las conexiones entre diferentes disciplinas, como informática, marketing y psicología del consumidor. Todo esto permite evaluar la influencia y contribución del avance de la IA en la gestión de clientes.

Este análisis nos proporciona una base sólida para comprender el panorama actual de la investigación, identificar brechas de conocimiento y prever futuras direcciones en la aplicación de IA para mejorar la gestión y experiencia del cliente.

---

<!-- Página 12 -->

1. PROTOCOLO DE BÚSQUEDA: BÚSQUEDA Y EXTRACCIÓN DE DOCUMENTOS

Para llevar a cabo el análisis bibliométrico sobre la relación entre la Inteligencia Artificial y la gestión de clientes, se estableció un protocolo de búsqueda riguroso en la base de datos Scopus. Este protocolo se diseñó para identificar de manera sistemática y exhaustiva artículos relevantes que abordan la intersección de estos dos campos. A través de una serie de ecuaciones de búsqueda específicas, se buscó no solo recopilar publicaciones recientes, sino también trazar la evolución de los conceptos clave a lo largo del tiempo. A continuación, se detallan las estrategias de búsqueda implementadas y los resultados obtenidos.

ECUACIÓN DE BÚSQUEDA PRINCIPAL: (“Artificial intelligence” OR “IA”) AND (“customer” OR “clients”) AND (“management” OR “administration”)

Luego, realizamos ajustes con los filtros de exclusiones e inclusiones en la búsqueda obteniendo como resultado los siguientes grupos de artículos, observando su distribución en la Tabla 1.

N° DocumentosFecha Ecuación de Búsqueda Encontrados

(“Artificial intelligence” OR “IA”) AND 145.445 2010-2024(“customer” OR “clients”) AND (“management” OR “administration”)

( TITLE-ABS-KEY ( emerging AND technologies ) 2016, 2021, 2022,OR TITLE-ABS-KEY ( machine AND learning ) 9 2023AND TITLE-ABS-KEY ( predictive AND analysis ) AND TITLE-ABS-KEY ( automatization ) )

---

<!-- Página 13 -->

( TITLE-ABS-KEY ( data AND mining ) OR TITLE-ABS-KEY ( data AND analysis ) AND 2013,2014,2019, 13 TITLE-ABS-KEY ( resources AND optimization ) 2021,2022 AND TITLE-ABS-KEY ( algorithms ) AND TITLE-ABS-KEY ( intelligent AND robotics ) )

2003, 2004, 2005, 2006 2007, 2008, ( TITLE-ABS-KEY ( sentiment AND analysis ) 2009,2010,2011, 9.888AND TITLE-ABS-KEY ( natural AND language 2012, 2013, 2014, AND processing ) ) 2015, 2016, 2017,2018, 2023,2024

Tabla 1: Distribución de Documentos Encontrados por Ecuaciones de Búsqueda. Elaboración Propia.

Luego de aplicar los filtros pertinentes de inclusión y exclusión, junto con la ecuación de búsqueda principal, la ecuación de búsqueda número 1 fue la más utilizada debido a su amplia gama de resultados y artículos útiles para el análisis a desarrollar, los cuales serán clasificados a continuación de acuerdo a su contenido.

2. ANÁLISIS DE CO-OCURRENCIA

En este apartado, se presenta la familia de términos identificados a través del análisis de co-ocurrencia realizado con VOSviewer. Este mapa ilustra las relaciones entre las palabras clave más frecuentemente utilizadas en los documentos seleccionados sobre la aplicación de la Inteligencia Artificial en la gestión de clientes. La visualización de estos términos permite identificar clusters conceptuales y áreas de enfoque en la literatura existente de la mano con la ecuación de búsqueda (“Artificial intelligence” OR “IA”) AND (“customer” OR “clients”) AND (“management” OR “administration”), facilitando una comprensión más profunda de las tendencias emergentes y las interconexiones temáticas en este campo.

---

<!-- Página 14 -->

2.1. MAPA DE CO-OCURRENCIA DE CONCEPTOS

Figura 1 : Mapa de Co-ocurrencia de Conceptos. Elaboración propia.

2.2. FAMILIA DE TÉRMINOS

Pueden destacarse los siguientes términos según el mapa de co-ocurrencia y el tema a relacionar en el presente estudio:

2.2.1. Predicción y análisis (azul)

- Análisis de sentimientos, estimación, memoria, estracción, técnicas, procedimiento, bosque aleatorio, NLP (procesamiento del lenguaje natural), estudios comparativos, conversación.

2.2.2. Redes y arquitectura (verde)

---

<!-- Página 15 -->

- Agente, precio, servidor, centro de datos, informática, qos (calidad del servicio), sumistro, ruta, distribuidor, dss (sistema soporte de toma de decisiones), nodo, automatización.

2.2.3. Gestión de relaciones con clientes (rojo)

- Revelaciones (insight), servicio al cliente, transformación digital, ventaja competitiva, desempeño financiero, originalidad, valor, mercadeo digital, adopción, lugar de trabajo.

2.2.4. Cadena de suministro (verde limón)

- Cliente, demanda, planeación de producción, SCM (gestión de la cadena de sumistro), consumidor final, materia prima, tiempos de entrega, bodega, estimación de demanda.

- Automatización - Minería de datos - Machine learning - Análisis de datos - Optimización de recursos - Algoritmos - Tecnologías emergentes - Robótica inteligente - Análisis de sentimientos - Procesamiento del lenguaje natural (PLN) - Análisis predictivo

3. CLASIFICACIÓN NARRATIVA DE ARTÍCULOS POR CLUSTERS PRINCIPALES

---

<!-- Página 16 -->

El análisis bibliométrico realizado revela una compleja red de interrelaciones entre diversos campos de investigación en tecnología, gestión y análisis de datos. El mapa de co-ocurrencia de conceptos (Figura 1) destaca cuatro clusters principales: redes y arquitectura, gestión de relaciones con clientes, predicción y análisis, y cadena de suministro. Estos clusters no sólo representan áreas de investigación distintas, sino que también ilustran la naturaleza interdisciplinaria del panorama tecnológico actual. La prominencia de temas como el análisis de sentimientos, la transformación digital y las tecnologías emergentes como blockchain y fintech, subraya la evolución constante y la convergencia de estas disciplinas.

Esta visión holística proporciona un marco sólido para comprender cómo las diferentes áreas de estudio se entrelazan y se influencian mutuamente, reflejando la complejidad de los desafíos y soluciones en la era digital. A continuación, se presentará un análisis de artículos clave, ofreciendo insights valiosos sobre las tendencias actuales y futuras en cada uno de los clusters mencionados, junto con su ocurrencia y relacionamiento en los 25 artículos seleccionados para contrastar las diferentes áreas del tema de estudio.

Año Título del Artículo Cluster Principal Subgrupo

A formal study of classificationAnálisis de Predicción y 2010techniques on entity discovery and theirSentimientos y Minería Análisis (P&A) application to opinion miningde Opiniones

Techniques and applications for sentiment analysis: The mainAnálisis de Predicción y 2013applications and challenges of one of theSentimientos y Minería Análisis (P&A) hottest research areas in computerde Opiniones science

Aspect-based opinion mining fromAnálisis de Predicción y 2015product reviews using conditionalSentimientos y Minería Análisis (P&A) random fieldsde Opiniones

---

<!-- Página 17 -->

Redes yProcesamiento del Natural Language Processing for the 2017 ArquitecturaLenguaje Natural y Semantic Web (R&A)Web Semántica

Gestión de Fuzzy formal concept analysis based Clientes (CRM)Análisis de Opiniones 2017opinion mining for CRM in financial y Servicio alpara CRM services Cliente

Gestión de Professional chat application based onClientes (CRM)Experiencia del Cliente 2018 natural language processingy Servicio aly Personalización Cliente

Análisis de Opinion Knowledge Injection NetworkPredicción y 2019 Sentimientos y Minería for Aspect ExtractionAnálisis (P&A) de Opiniones

Aprendizaje Forecasting of Customer BehaviorPredicción y 2020 Automático y Análisis Using Time Series AnalysisAnálisis (P&A) Predictivo

Self attentive product recommender - AAprendizaje Predicción y 2020hybrid approach with machine learningAutomático y Análisis Análisis (P&A) and neural networkPredictivo

Aprendizaje An approach to integrating sentimentPredicción y 2021 Automático y Análisis analysis into recommender systemsAnálisis (P&A) Predictivo

Análisis de Sector-level sentiment analysis withPredicción y 2022 Sentimientos y Minería deep learningAnálisis (P&A) de Opiniones

---

<!-- Página 18 -->

Supporting Argumentation Dialogues inRedes y Sistemas de Soporte a 2022Group Decision Support Systems: AnArquitectura la Decisión Approach Based on Dynamic Clustering(R&A)

Gestión de Classification of Product Review Clientes (CRM)Análisis de Opiniones 2022Sentiment by NLP and Machine y Servicio alpara CRM Learning Cliente

Análisis de A survey on sentiment analysisPredicción y 2022 Sentimientos y Minería methods, applications, and challengesAnálisis (P&A) de Opiniones

Cadena de A dynamic customer requirement Suministro yAnálisis de Requisitos 2022mining method for continuous product Gestión dedel Cliente improvement Operaciones

A conditional random field frameworkAnálisis de Predicción y 2023for language process in product reviewSentimientos y Minería Análisis (P&A) miningde Opiniones

Integrating NLP in the BusinessRedes y Sistemas de Soporte a 2023Decision Support System to PromoteArquitectura la Decisión Customer Loyalty(R&A)

Análisis de Sentiment analysis using a deepPredicción y 2024 Sentimientos y Minería ensemble learning modelAnálisis (P&A) de Opiniones

AI-driven service marketing:Aprendizaje Predicción y 2024Transforming customer experience andAutomático y Análisis Análisis (P&A) operational efficiencyPredictivo

---

<!-- Página 19 -->

Use of explainable AI to interpret theAnálisis de Predicción y 2024results of NLP models for sentimentalSentimientos y Minería Análisis (P&A) analysisde Opiniones

Análisis de Objective and neutral summarization ofPredicción y 2024 Sentimientos y Minería customer reviewsAnálisis (P&A) de Opiniones

Aprendizaje Data science in healthcare: techniques,Predicción y 2024 Automático y Análisis challenges and opportunitiesAnálisis (P&A) Predictivo

Adaptive Evolutionary ComputingAnálisis de Predicción y 2024Ensemble Learning Model forSentimientos y Minería Análisis (P&A) Sentiment Analysisde Opiniones

Using machine learning to developAprendizaje Predicción y 2024customer insights from user-generatedAutomático y Análisis Análisis (P&A) contentPredictivo

Tell me what you Like: introducing Redes yProcesamiento del natural language preference elicitation 2024ArquitecturaLenguaje Natural y strategies in a virtual assistant for the (R&A)Web Semántica movie domain

Tabla 2: Clasificación de los Artículos Seleccionados. Elaboración Propia.

De acuerdo a la clasificación anterior, puede realizarse un análisis de cada clúster principal considerando el relacionamiento de conceptos dentro de los artículos seleccionados:

Predicción y Análisis (P&A): Este cluster muestra una fuerte tendencia hacia la aplicación de técnicas avanzadas de aprendizaje profundo y análisis de sentimientos en diversos sectores. Se observa un énfasis particular en el procesamiento de grandes volúmenes de datos, especialmente en contextos de redes sociales y revisiones de productos. La presencia de estudios en el sector

---

<!-- Página 20 -->

salud indica la creciente importancia del análisis de datos en áreas críticas más allá del comercio electrónico. Este se conecta con el cluster de Redes y Arquitectura, a través de términos como "prediction" y "computing", indicando la integración de técnicas de análisis en la infraestructura de red.

El cluster de Predicción y Análisis (P&A) se enfoca en el uso de técnicas avanzadas de análisis de datos y aprendizaje automático para prever el comportamiento del cliente y mejorar la toma de decisiones en marketing así como Berry y Singh (2024) destacan cómo el marketing impulsado por IA está transformando la experiencia del cliente y la eficiencia operativa mediante recomendaciones personalizadas y una entrega de servicios fluida. Reforzando la misma idea, Abbasimehr y Shabani (2020) proponen una metodología para crear segmentos de clientes basados en datos pasados, crear pronósticos por segmento y luego descubrir el comportamiento futuro de cada segmento. Este enfoque ilustra cómo las técnicas de análisis de series temporales se pueden aplicar para predecir el comportamiento del cliente con mayor precisión.

Por otro lado, Zhang et al. (2019) hacen referencia a la extracción de aspectos mediante la inyección de conocimiento de opinión, lo cual también se alinea con este cluster. Dado que proporciona una técnica avanzada para analizar y predecir las opiniones de los clientes sobre aspectos específicos de los productos o servicios. De la misma forma, Liu et al. (2024) aportan al cluster con su modelo de aprendizaje integrado computacional evolutivo adaptativo (AdaECELM), diseñado específicamente para superar los desafíos del análisis de sentimientos en textos cortos, lo cual es particularmente relevante en el contexto de las redes sociales y las reseñas de productos en línea. Manteniendo la misma línea, Carichon et al. (2024) contribuyen con su enfoque en la minería de opiniones para detectar y extraer información relevante de una gran cantidad de reseñas de clientes, proponiendo un modelo de aprendizaje multitarea que permite una summarización más objetiva y neutral de las opiniones de los clientes. Asimismo, Feldman (2013) proporciona una visión general de las principales aplicaciones y desafíos del análisis de sentimientos, estableciendo una base teórica para muchas de las aplicaciones prácticas desarrolladas en los años siguientes, como corresponde al trabajo de Mustak et al. (2024) y Dang et al. (2021), los cuales amplían el alcance del cluster al explorar, respectivamente, el uso del

---

<!-- Página 21 -->

aprendizaje automático para desarrollar insights de clientes a partir de contenido generado por usuarios y la integración del análisis de sentimientos en los sistemas de recomendación.

Estos estudios demuestran cómo el cluster P&A se centra en utilizar técnicas avanzadas de análisis de datos y aprendizaje automático para predecir el comportamiento del cliente y mejorar la toma de decisiones en marketing.

Redes y Arquitectura: Este cluster representa la importancia de las tecnologías de procesamiento de lenguaje natural en la arquitectura de sistemas web y en la toma de decisiones grupales. La aplicación de NLP en la web semántica sugiere un movimiento hacia una internet más inteligente y capaz de comprender el contexto. Se conecta con el cluster Cadena de Suministro mediante conceptos como "supply" y "demand", sugiriendo la importancia de la infraestructura de red en la gestión de la cadena de suministro.

El cluster de Redes y Arquitectura (R&A) se centra en las tecnologías y estructuras subyacentes que permiten el procesamiento y análisis avanzado de datos, particularmente en el contexto del procesamiento del lenguaje natural (NLP) y la web semántica. Maynard et al.( 2017) presentan en su libro una introducción exhaustiva al procesamiento del lenguaje natural para la web semántica. Este trabajo es fundamental para el cluster R&A, ya que explora cómo las tecnologías de NLP y la web semántica se pueden integrar para permitir que los datos estructurados y no estructurados se fusionen sin problemas. Los autores discuten arquitecturas clave como la anotación semántica, la vinculación de ontologías y la población, que son esenciales para construir sistemas de procesamiento de lenguaje natural efectivos.

Musto et al. (2024) contribuyen a este cluster con su trabajo sobre una estrategia que permite a los usuarios expresar sus preferencias y necesidades a través de declaraciones en lenguaje natural. Este estudio demuestra cómo las arquitecturas de sistemas de NLP pueden aplicarse para mejorar la interacción con los clientes y la personalización de servicios. SSherif et al. (2023) amplían el alcance del cluster al explorar la integración del procesamiento del lenguaje natural en el sistema de soporte a la decisión empresarial. Su trabajo destaca cómo las arquitecturas de NLP

---

<!-- Página 22 -->

pueden incorporarse en sistemas más amplios de toma de decisiones, mejorando la capacidad de las empresas para comprender y responder a las necesidades de los clientes.

Los artículos seleccionados demuestran cómo el cluster R&A se enfoca en las estructuras y tecnologías fundamentales que permiten el procesamiento avanzado del lenguaje natural y la integración de datos estructurados y no estructurados, elementos cruciales para las aplicaciones modernas de análisis de clientes y marketing basado en datos.

Cadena de suministro y Gestión de Operaciones: El cluster de Cadena de Suministro y Gestión de Operaciones, aunque es el menos prominente en los artículos analizados, destaca la importancia de integrar el análisis de requisitos del cliente en la mejora continua de productos y la gestión de la cadena de suministro. Zhao et al. (2022) proponen un método novedoso de minería de requisitos de clientes dinámicos para analizar los cambios dinámicos de la satisfacción del cliente con los atributos del producto. Este enfoque es crucial para la gestión de operaciones y la mejora continua del producto, ya que permite a las empresas adaptar rápidamente sus ofertas en respuesta a las cambiantes preferencias de los clientes. Esto sugiere una tendencia hacia la personalización y adaptación rápida en la gestión de operaciones y cadena de suministro. Se conecta con el cluster verde (Redes y Arquitectura) a través de "logistics" y "distribution", mostrando la dependencia de la cadena de suministro en la infraestructura de red. Asimismo, se vincula con el cluster rojo (Gestión de relaciones con clientes) mediante "customer demand", resaltando la importancia de la orientación al cliente en la gestión de la cadena de suministro. El trabajo de Zhao et al. (2022) ilustra cómo las técnicas avanzadas de análisis de datos pueden aplicarse no solo para comprender las necesidades actuales de los clientes, sino también para prever cambios futuros en sus preferencias. Esto es particularmente valioso en el contexto de la gestión de la cadena de suministro, donde la capacidad de anticipar y responder a los cambios en la demanda del cliente es fundamental para la eficiencia operativa y la satisfacción del cliente. Este estudio demuestra cómo el cluster de Cadena de Suministro y Gestión de Operaciones se enfoca en utilizar el análisis avanzado de datos para mejorar la toma de decisiones en la gestión de operaciones y la cadena de suministro, con un énfasis particular en la adaptación rápida a las cambiantes necesidades y preferencias de los clientes.

---

<!-- Página 23 -->

Gestión de relaciones con clientes (CRM) y servicio al cliente: Este cluster refleja un enfoque significativo en la mejora de la experiencia del cliente a través de tecnologías de procesamiento de lenguaje natural y aprendizaje automático. Se destaca la importancia de analizar el contenido generado por usuarios para obtener insights valiosos. La presencia de estudios en servicios financieros y entretenimiento subraya la versatilidad de estas técnicas en diferentes industrias de servicios. Se conecta con el cluster de Predicción y Análisis a través de "sentiment analysis" y "text", indicando el uso de técnicas de análisis de datos para mejorar la experiencia del cliente y se vincula con el cluster de Cadena de Suministro mediante "customer demand", mostrando la importancia de entender las necesidades del cliente en la gestión de la cadena de suministro. Ravi et al. (2017) presentan un modelo de análisis de opinión basado en el análisis de conceptos formales difusos para CRM en servicios financieros. Este estudio es crucial para el cluster, ya que demuestra cómo las técnicas avanzadas de análisis de datos pueden utilizarse para analizar las quejas/reclamos y resumir las quejas largas y verbosas de forma concisa, lo que permite a las empresas financieras comprender mejor las necesidades y problemas de sus clientes.

Al siguiente año, Karthick et al. (2018) contribuyen al cluster con su desarrollo de una aplicación de chat profesional basada en procesamiento del lenguaje natural. Este trabajo ilustra cómo las tecnologías de NLP pueden aplicarse directamente para mejorar la comunicación con los clientes y el servicio al cliente en tiempo real. Unos años después de esto, Das et al. (2022) proponen un sistema que utiliza el procesamiento del lenguaje natural para evaluar los comentarios de los clientes de las compras en línea y proporcionar una proporción de comentarios positivos y negativos. Este enfoque es particularmente relevante para la gestión de clientes en el contexto del comercio electrónico, donde la comprensión rápida y precisa de los sentimientos de los clientes es crucial. Estos estudios demuestran cómo el cluster de CRM y Servicio al Cliente se enfoca en utilizar tecnologías avanzadas de procesamiento de lenguaje natural y análisis de datos para mejorar la comprensión de las necesidades y opiniones de los clientes, optimizar los servicios y, en última instancia, fomentar la lealtad del cliente.

La interconexión de estos clusters subraya la evolución de las estrategias empresariales basadas en datos, donde el análisis avanzado y la infraestructura tecnológica juegan un papel

---

<!-- Página 24 -->

central en la optimización de procesos. Predicción y Análisis (P&A) impulsa la toma de decisiones en marketing y experiencia del cliente, mientras que Redes y Arquitectura proporciona la base tecnológica que permite la implementación de estas estrategias en entornos digitales cada vez más complejos. En paralelo, la Gestión de Relaciones con Clientes (CRM) transforma estos datos en insights accionables para mejorar la interacción con los consumidores, y la Cadena de Suministro y Gestión de Operaciones capitaliza este conocimiento para anticipar la demanda y optimizar la logística. La sinergia entre estos clusters demuestra que la transformación digital no solo es un desafío técnico, sino una oportunidad estratégica para mejorar la eficiencia y competitividad en mercados dinámicos.

3.1. ANÁLISIS DE EVOLUCIÓN TEMPORAL

En la última década, la intersección entre la inteligencia artificial (IA) y la gestión de relaciones con clientes ha experimentado un crecimiento significativo, impulsado por la búsqueda de las organizaciones de métodos más efectivos para comprender y responder a las necesidades de sus clientes. Esta evolución se refleja claramente en la literatura académica y las aplicaciones prácticas del campo.

El análisis de sentimientos y la minería de opiniones se han convertido en herramientas fundamentales en este proceso. Feldman (2013) estableció las bases al discutir las principales aplicaciones y desafíos de una de las áreas de investigación más candentes en ciencias de la computación, refiriéndose al análisis de sentimientos. Este trabajo seminal destacó la importancia de comprender las opiniones de los clientes en el proceso de toma de decisiones, sentando las bases para futuras investigaciones y aplicaciones en el campo. A medida que avanzaba la década, se observó un refinamiento en las técnicas y aplicaciones. Ravi et al. (2017) presentaron un modelo innovador de análisis de opinión basado en el análisis de conceptos formales difusos para CRM en servicios financieros. Este estudio demostró cómo el análisis de sentimientos podía utilizarse para mejorar la comprensión de las quejas y necesidades de los clientes en la industria financiera. Así, el trabajo de Maynard et al. (2017) sobre Procesamiento del Lenguaje Natural para la Web Semántica amplió el alcance de estas tecnologías, explorando cómo el NLP y las tecnologías de la

---

<!-- Página 25 -->

Web Semántica podían integrarse para mejorar la gestión de datos estructurados y no estructurados. Esta investigación fue crucial para el desarrollo de sistemas más sofisticados capaces de procesar y comprender el lenguaje natural en contextos empresariales.

A medida que nos acercamos a la década de 2020, la investigación se volvió más especializada y orientada a aplicaciones específicas. Zhang et al. (2019) introdujeron la Red de Inyección de Conocimiento de Opinión para la Extracción de Aspectos, una técnica avanzada para analizar opiniones de clientes con mayor precisión. Este trabajo representó un avance significativo en la capacidad de las empresas para extraer información detallada y relevante de las opiniones de los clientes. El período 2020-2024 ha sido testigo de una explosión de investigaciones que aplican técnicas de IA cada vez más sofisticadas a la gestión de clientes. Abbasimehr y Shabani (2020) propusieron metodologías para la Previsión del Comportamiento del Cliente Utilizando Análisis de Series Temporales, demostrando cómo las técnicas avanzadas de análisis de datos podían aplicarse para predecir el comportamiento futuro de los clientes con mayor precisión.

En los años más recientes, hemos visto un enfoque creciente en la integración de múltiples tecnologías de IA para abordar desafíos complejos en la gestión de clientes. Berry y Singh (2024) exploraron cómo el marketing impulsado por IA está transformando la experiencia del cliente y la eficiencia operativa, destacando cómo las técnicas de IA están revolucionando no solo la comprensión del cliente, sino también la forma en que las empresas interactúan con ellos.

Liu et al. (2024) presentaron un Modelo de Aprendizaje Conjunto Computacional Evolutivo Adaptativo para el Análisis de Sentimientos, demostrando cómo las técnicas de IA más avanzadas pueden aplicarse para superar los desafíos en el análisis de sentimientos, especialmente en contextos de redes sociales y reseñas en línea.

Esta evolución temporal refleja un campo en rápido desarrollo, con un enfoque creciente en soluciones más sofisticadas, personalizadas y explicables para la gestión de relaciones con clientes. Desde los primeros trabajos que establecieron las bases conceptuales, hasta las aplicaciones más recientes que integran múltiples tecnologías de IA, la trayectoria muestra una tendencia clara hacia sistemas más inteligentes y adaptativos capaces de comprender y responder a las necesidades de los clientes de manera más efectiva y personalizada.

---

<!-- Página 26 -->

Figura 2: Línea de tiempo análisis de evolución temporal. Elaboración propia

---

<!-- Página 27 -->

Objetivos

Objetivo General: Determinar el impacto de la implementación de tecnologías de Inteligencia Artificial en la gestión de relaciones con clientes y estrategias de marketing en el contexto empresarial actual.

Objetivos Específicos: 1. Identificar las tecnologías de Inteligencia Artificial más utilizadas en la gestión de clientes mediante análisis bibliométrico de literatura científica reciente. 2. Analizar el impacto de la IA en los indicadores de satisfacción, retención y experiencia del cliente a través de estudios de caso documentados. 3. Evaluar la efectividad de las herramientas de IA en la personalización de estrategias de marketing y segmentación de clientes. 4. Proponer recomendaciones para la implementación exitosa de tecnologías de IA en la gestión de clientes, considerando las particularidades del contexto empresarial.

Metodología

La presente investigación adopta un enfoque metodológico mixto que combina técnicas de análisis bibliométrico y revisión sistemática de literatura para abordar de manera integral el fenómeno de la implementación de tecnologías de Inteligencia Artificial en la gestión de clientes. Esta aproximación metodológica permite tanto la identificación de patrones cuantitativos en la producción científica como el análisis cualitativo profundo del contenido de las investigaciones más relevantes. La selección de esta metodología se fundamenta en la necesidad de proporcionar una visión comprehensiva y actualizada del estado del arte en IA aplicada al marketing y CRM, considerando tanto la evolución temporal de las publicaciones como la calidad y relevancia del contenido científico analizado.

Tipo de información

La investigación se basa en información secundaria obtenida de fuentes académicas especializadas, incluyendo artículos científicos, estudios de caso y reportes técnicos publicados en revistas indexadas y bases de datos reconocidas internacionalmente.

---

<!-- Página 28 -->

- Reconocimiento entidad nombrada

El Reconocimiento de Entidades Nombradas (NER) es una tarea fundamental y constituye el núcleo de los sistemas de procesamiento del lenguaje natural (PLN). Además, NER pertenece a una clase general de problemas en NLP conocida como etiquetado de secuencias (Erdogan, 2010).El reconocimiento de Entidades Nombradas (NER) consiste en procesar estructurados y no estructurados e identificar expresiones que se refieren a personas, lugares, organizaciones y empresas. De esta forma se identifican nombres propios en texto, y luego se clasifican en categorías de interés predefinidas (Mansouri et al., 2008). En este caso las categorías resultantes del proceso ejecutado de la mano de NER fueron verbos, sustantivos y adjetivos.

Figura 3: Nube de palabras verbos. Elaboración propia

---

<!-- Página 29 -->

Figura 4: Nube de palabras sustantivos. Elaboración propia

Figura 5: Nube de palabras adjetivos. Elaboración propia

---

<!-- Página 30 -->

- Detección de emociones

La detección de emociones consiste en la identificación y el análisis del estado emocional de un individuo a través de diversas metodologías y herramientas tecnológicas. En el ámbito del marketing, las investigaciones han documentado de manera extensa la influencia que ejercen las emociones sobre el comportamiento del consumidor.

Además, Ramos Torres & Duque Holguín (2023) subrayan que las emociones pueden predecir el comportamiento del consumidor en diferentes contextos, siendo esenciales para la toma de decisiones de compra. Este fenómeno es respaldado por Gallego (2023) , quien enfatiza que las emociones influyen en las decisiones de compra y en la percepción de una marca, permitiendo la creación de conexiones auténticas y significativas entre las marcas y los consumidores.

Desde el ámbito técnico, la detección de emociones utiliza el procesamiento del lenguaje natural (PLN), una rama de la inteligencia artificial que mejora la interacción entre humanos y sistemas computacionales. Este campo, que ha evolucionado desde el siglo XX, basado inicialmente en básicas de traducción hasta llegar a modelos avanzados de aprendizaje automático implementado actual. Ahora, este modelo combina análisis de sentimientos y algoritmos predictivos, permitiendo identificar patrones emocionales en grandes volúmenes de datos, como redes sociales o reseñas.

Este tipo de tecnología es esencial en la gestión de clientes, debido permiten identificar emociones en tiempo real y ofrecer respuestas personalizadas, mejorando la experiencia del consumidor y fortaleciendo su vínculo con las marcas.

---

<!-- Página 31 -->

Figura 6: Gráfico emociones detectadas en las transcripciones. Elaboración propia

- Algoritmo LDA

El algoritmo LDA o la asignación de Dirichlet latente, es un modelo probabilístico generativo de un corpus. La idea es que los documentos se representen como mezclas aleatorias sobre temas latentes, donde cada tema se caracteriza por una distribución sobre palabras (Blei et al., 2003). Además, se utiliza a menudo para el modelado de temas basado en contenido, lo que, básicamente, significa el aprendizaje de categorías de texto sin clasificar. En el modelado de temas basado en contenido, un tema es una distribución de palabras (Gayhardt et al., 2024).

Según Murel Ph.D & Kavlakoglu (2024) la LDA es una técnica de modelización de temas que aplica el aprendizaje no supervisado en conjuntos de datos de texto grandes para producir un conjunto resumido de términos derivados de esos documentos. Esta técnica es un enfoque bayesiano de modelado de temas que asume que los documentos se han generado a través de un muestreo aleatorio de temas previos al documento, e intenta aplicar ingeniería inversa a este muestreo.

---

<!-- Página 32 -->

El LDA genera temas clasificando palabras y documentos entre estos diferentes temas de acuerdo con distribuciones de probabilidad. El proceso de generación de texto de LDA comienza con temas previos al documento, y para crear un documento de texto, se genera aleatoriamente una distribución sobre temas y se emite de manera aleatoria una palabra de ese tema (Murel Ph.D & Kavlakoglu, 2024). Esta técnica permite descubrir los temas latentes que caracterizan a una colección de documentos (Gonzalez Avella, 2017).

En este orden de ideasal ser una técnica de modelización de temas, el algoritmo permite descubrir los temas centrales y sus distribuciones en un conjunto de documentos. En este caso, es una herramienta útil para convertir el texto resultando de la recolección de la información sobre el tema de interés, en una representación más compacta al reducir el espacio de características (palabras) a un espacio de temas latentes.

- Temas encontrados: - Tema 0: 0.022*"ai" + 0.012*"data" + 0.011*"use" + 0.010*"agents" + 0.010*"tools" + 0.009*"using" - Tema 1: 0.018*"celeste" + 0.016*"crm" + 0.011*"carol" + 0.011*"scooter" + 0.009*"customers" + 0.007*"customer" - Tema 2: 0.037*"ai" + 0.022*"generative" + 0.014*"customer" + 0.010*"conversational" + 0.009*"experience" + 0.009*"using" - Tema 3: 0.011*"well" + 0.010*"think" + 0.009*"tech" + 0.008*"really" + 0.008*"yeah" + 0.007*"technology" - Tema 4: 0.000*"ai" + 0.000*"customer" + 0.000*"think" + 0.000*"actually" + 0.000*"data" + 0.000*"right" - Tema 5: 0.021*"marketing" + 0.013*"content" + 0.011*"data" + 0.011*"well" + 0.011*"super" + 0.009*"ai" - Tema 6: 0.028*"ai" + 0.023*"customer" + 0.015*"service" + 0.012*"customers" + 0.010*"agents" + 0.009*"generative"

---

<!-- Página 33 -->

- Tema 7: 0.008*"customers" + 0.008*"data" + 0.006*"ai" + 0.006*"help" + 0.003*"customer" + 0.003*"experience" - Tema 8: 0.012*"ai" + 0.012*"service" + 0.011*"user" + 0.010*"customer" + 0.008*"people" + 0.008*"look" - Tema 9: 0.025*"ai" + 0.019*"customer" + 0.018*"right" + 0.014*"really" + 0.014*"think" + 0.011*"service"

Resultados

Interpretación exhaustiva de términos destacados en la minería de texto

1. AI (Inteligencia Artificial) La prominencia del término "AI" en todos los temas analizados (especialmente en los temas 0, 2, 6, 8 y 9 con frecuencias de 0.022, 0.037, 0.028, 0.012 y 0.025 respectivamente) refleja su rol fundamental como concepto vertebrador en la gestión del cliente moderno. Su alta frecuencia valida lo establecido por John McCarthy, quien acuñó el término en 1956, y lo descrito por Benhamou (2022) quien señaló que, aunque los principios de la IA son de larga data, en los últimos años se ha experimentado un avance significativo. La aparición consistente de "AI" junto a "customer", "service" y "experience" confirma la tendencia identificada en el análisis bibliométrico hacia aplicaciones prácticas de la IA en entornos de atención al cliente. Como destacan Berry y Singh (2024), el marketing impulsado por IA está transformando tanto la experiencia del cliente como la eficiencia operativa, lo que explica esta alta correlación en los datos analizados. Además, la asociación de "AI" con "tools" (herramientas) en el tema 0 refleja lo señalado por Aparecido (2024) sobre cómo la IA forma parte de la cadena de producción de prácticamente todos los aparatos tecnológicos, ayudando a encontrar medios capaces de satisfacer las necesidades humanas con eficiencia.

---

<!-- Página 34 -->

2. Generative (Generativa) La recurrencia del término "generative" junto a "AI" y "customer" (con frecuencias destacadas de 0.022 en el tema 2 y 0.009 en el tema 6) señala la relevancia creciente de la IA generativa en el contexto de la gestión de clientes. Esta tendencia se alinea con la evolución temporal identificada en el análisis bibliométrico, donde las investigaciones entre 2020-2024 muestran un enfoque en tecnologías más sofisticadas y adaptativas. La IA generativa representa una evolución desde el análisis predictivo hacia sistemas capaces no solo de analizar datos existentes sino de crear nuevos contenidos y soluciones personalizadas. Esta evolución se corresponde con lo que Zhou (2021) describió como la capacidad del machine learning para desarrollar algoritmos que construyen modelos a partir de datos y realizan predicciones cada vez más precisas. La presencia repetida de este término junto a "conversational" en el tema 2 refleja específicamente la tendencia hacia asistentes virtuales y chatbots generativos que pueden mantener conversaciones naturales con los clientes, transformando fundamentalmente la experiencia de servicio.

3. Customer/Customers (Cliente/Clientes) La alta frecuencia de los términos "customer" y "customers" en varios de los temas analizados (con valores de 0.014, 0.023 en los temas 2 y 6 para "customer", y 0.009, 0.012, 0.008 en los temas 1, 6 y 7 para "customers") confirma el enfoque centrado en el cliente de las aplicaciones de IA. Esto coincide con lo identificado en el cluster de Gestión de Relaciones con Clientes del análisis bibliométrico, donde Ravi et al. (2017)demostraron la importancia del análisis de opiniones para comprender mejor las necesidades de los clientes en servicios financieros. La co-ocurrencia de estos términos con "experience", "service" y "agents" revela una preocupación fundamental por mejorar la experiencia del cliente, validando la tendencia hacia sistemas más inteligentes capaces de responder a las necesidades individuales. Esta orientación coincide con lo señalado por Das et al. (2022) sobre la clasificación de sentimientos en reseñas de productos para proporcionar análisis de comentarios positivos y negativos, herramienta crucial para comprender la percepción del cliente en entornos de comercio electrónico.

---

<!-- Página 35 -->

4. Data (Datos) La presencia constante del término "data" en varios temas (con frecuencias de 0.012 en el tema 0, 0.011 en el tema 5 y 0.008 en el tema 7) confirma el papel fundamental de los datos como materia prima para las aplicaciones de IA en la gestión de clientes. Esto corrobora lo establecido por Gontero y Menéndez (2021) sobre la caracterización de los macrodatos por su volumen, velocidad y variedad, las llamadas "3V". La co-ocurrencia con "use" y "using" sugiere un enfoque práctico en la utilización de estos datos, alineándose con lo que Moodley (2024) señaló sobre la importancia del Big Data para el aprendizaje automático. Además, la aparición de "data" junto a "marketing" en el tema 5 refleja el vínculo creciente entre el análisis de datos y las estrategias de marketing, donde el procesamiento de grandes volúmenes de información permite personalizar campañas y mejorar la segmentación de clientes, como se observa en el trabajo de Mustak et al. 2024) sobre el uso del aprendizaje automático para desarrollar insights de clientes a partir de contenido generado por usuarios.

5. Service (Servicio) La alta frecuencia del término "service" en asociación con "AI" y "customer" (con valores de 0.015 en el tema 6 y 0.012 en el tema 8) refleja la aplicación práctica de la IA en entornos de servicio al cliente. Esto se alinea con lo identificado en el cluster de Gestión de Clientes (CRM) y Servicio al Cliente del análisis bibliométrico, donde Karthick et al. (2018) demostraron cómo las tecnologías de NLP pueden aplicarse directamente para mejorar la comunicación con los clientes y el servicio en tiempo real. La presencia repetida de este término junto a "AI" y "agents" en el tema 6 refleja la tendencia creciente hacia la automatización inteligente del servicio al cliente mediante agentes virtuales, coincidiendo con lo que Sherif et al. (2023) describieron sobre la integración del procesamiento del lenguaje natural en los sistemas de soporte a la decisión empresarial para promover la lealtad del cliente. Este enfoque en el servicio potenciado por IA representa una evolución natural desde los sistemas CRM tradicionales hacia plataformas más adaptativas y centradas en la experiencia del usuario.

---

<!-- Página 36 -->

6. Agents (Agentes) La recurrencia del término "agents" en conjunción con "AI", "customer" y "service" (con frecuencias de 0.010 en el tema 0 y 0.010 en el tema 6) sugiere un enfoque en la implementación de agentes inteligentes o virtuales en la gestión de clientes. Esto coincide con la evolución temporal identificada en el análisis bibliométrico, donde las investigaciones más recientes muestran un interés creciente en soluciones automatizadas y sistemas de soporte a la decisión. La presencia de "agents" junto a "tools" en el tema 0 refleja el papel instrumental de estos agentes como herramientas que aumentan las capacidades humanas en la gestión de clientes, mientras que su co- ocurrencia con "service" en el tema 6 subraya su aplicación específica en la mejora del servicio al cliente. Esta tendencia se alinea con los hallazgos Musto et al. (2024) sobre la introducción de estrategias de elicitación de preferencias en lenguaje natural en asistentes virtuales, demostrando cómo estos agentes pueden facilitar interacciones más naturales y eficaces con los usuarios.

7. Marketing La presencia destacada del término "marketing" (0.021 en el tema 5) junto a "content", "data" y "ai" refleja la integración de tecnologías de IA en estrategias de marketing basadas en datos. Esto valida los hallazgos de Berry y Singh (2024) sobre cómo el marketing impulsado por IA está transformando la experiencia del cliente. La co-ocurrencia con "content" (0.013) sugiere un enfoque particular en la generación y optimización de contenido utilizando IA, una tendencia creciente identificada en los estudios más recientes. Además, la presencia de "super" (0.011) junto a "marketing" puede indicar la percepción de que estas nuevas capacidades potenciadas por IA representan una evolución significativa o "super-capacidades" en comparación con el marketing tradicional. Esta transformación del marketing mediante IA coincide con la literatura revisada sobre cómo la inteligencia artificial está cambiando fundamentalmente las operaciones empresariales en diversos sectores, como señalaron Aparecido (2024) y Benhamou (2022).

8. Content (Contenido) La recurrencia del término "content" (0.013 en el tema 5) junto a "marketing" y "ai" indica la importancia creciente del contenido generado o optimizado por IA en estrategias de marketing

---

<!-- Página 37 -->

y gestión de clientes. Esto se alinea con la evolución temporal identificada en el análisis bibliométrico, especialmente con los desarrollos más recientes en procesamiento del lenguaje natural y análisis de sentimientos. La presencia de este término refleja la tendencia hacia un marketing de contenido más sofisticado y personalizado utilizando tecnologías de IA, coincidiendo con lo que (Carichon et al., 2024) describieron sobre la sumarización objetiva y neutral de reseñas de clientes mediante modelos de aprendizaje multitarea. Esta tendencia muestra cómo la IA está transformando no solo la forma en que las empresas analizan la información de los clientes, sino también cómo generan y adaptan el contenido para interactuar con ellos de manera más efectiva.

9. Experience (Experiencia) La presencia del término "experience" (0.009 en el tema 2 y aparición significativa en el tema 7) junto a "customer" y "ai" confirma el enfoque en la mejora de la experiencia del cliente mediante la aplicación de tecnologías de IA. Esto coincide con lo identificado en el cluster de Gestión de Clientes (CRM) del análisis bibliométrico, donde diversos estudios destacan la importancia de comprender y mejorar la experiencia del cliente. La co-ocurrencia con "generative" y "conversational" sugiere una tendencia hacia experiencias de cliente más interactivas y personalizadas utilizando tecnologías avanzadas de IA. Esta tendencia refleja la evolución desde los primeros sistemas CRM, centrados principalmente en la gestión de datos, hacia plataformas más sofisticadas que priorizan la calidad de la experiencia del usuario, como se observa en el trabajo de Berry y Singh (2024) sobre cómo el marketing impulsado por IA está transformando tanto la experiencia del cliente como la eficiencia operativa.

10. Conversational (Conversacional) La presencia del término "conversational" (0.010 en el tema 2) junto a "ai", "customer" y "generative" refleja el creciente interés en interfaces conversacionales y chatbots en la gestión de clientes. Esto se alinea perfectamente con lo encontrado por Karthick et al. (2018) sobre aplicaciones de chat profesional basadas en procesamiento del lenguaje natural, y se relaciona con el trabajo de Omar et al. (2022) sobre el papel del procesamiento del lenguaje natural como proveedor relevante de herramientas de análisis e interpretación de textos. La recurrencia de este

---

<!-- Página 38 -->

término confirma la tendencia hacia interacciones más naturales y fluidas con los clientes, facilitando una comunicación bidireccional que mejora tanto la satisfacción del cliente como la capacidad de las empresas para recopilar información valiosa de estas interacciones.

11. Using/Use (Usando/Uso) La alta frecuencia de los términos "using" (0.009 en los temas 0 y 2) y "use" (0.011 en el tema 0) junto a "ai", "data" y "tools" sugiere un enfoque práctico y aplicado en la implementación de tecnologías de IA en la gestión de clientes. Esto refleja la madurez creciente del campo, evolucionando desde conceptos teóricos hacia aplicaciones concretas, como se observa en la evolución temporal identificada en el análisis bibliométrico. La presencia de estos términos indica que las organizaciones están pasando de la fase de exploración a la implementación activa de soluciones de IA, alineándose con lo que Zhao et al. (2022) describieron sobre métodos dinámicos de minería de requisitos de clientes para la mejora continua de productos. Esta tendencia hacia la aplicación práctica marca una etapa importante en la adopción de tecnologías de IA en entornos empresariales.

12. Tools (Herramientas) La presencia del término "tools" (0.010 en el tema 0) junto a "ai", "data", "using" y "agents" indica la importancia de las herramientas específicas en la implementación de soluciones de IA para la gestión de clientes. Esto coincide con la evolución del campo identificada en el análisis bibliométrico, donde las tecnologías de IA han pasado de ser conceptos teóricos a herramientas prácticas. La co-ocurrencia con "agents" sugiere que estas herramientas a menudo toman la forma de agentes virtuales o sistemas automatizados, alineándose con lo que Sherif et al. (2023) describieron sobre la integración del NLP en sistemas de soporte a la decisión empresarial. Esta concepción de la IA como conjunto de herramientas prácticas refleja una comprensión más madura del campo, donde el foco está en la utilidad y aplicabilidad práctica más que en los aspectos puramente conceptuales.

---

<!-- Página 39 -->

13. Help (Ayuda) La aparición del término "help" (0.006 en el tema 7) junto a "customers", "data" y "experience" refleja el propósito fundamental de las tecnologías de IA en la gestión de clientes: proporcionar asistencia y mejorar el servicio. Esta orientación hacia la ayuda se alinea con lo que Aparecido (2024) describió sobre cómo la IA ayuda a analizar las causas prioritarias en programas sociales como la salud, la seguridad y la educación, extendiendo este concepto al ámbito de la atención al cliente. La presencia de este término en asociación con "experience" sugiere que esta ayuda está orientada principalmente a mejorar la experiencia del cliente, coincidiendo con la tendencia general identificada en el análisis bibliométrico hacia sistemas más centrados en el usuario.

14. Think/Really/Right (Pensar/Realmente/Correcto) La presencia de términos como "think" (0.010 en el tema 3 y 0.014 en el tema 9), "really" (0.008 en el tema 3 y 0.014 en el tema 9) y "right" (0.018 en el tema 9) sugiere un componente reflexivo y evaluativo en las discusiones sobre IA y gestión de clientes. Estos términos reflejan la necesidad de evaluación crítica y juicio en la implementación de soluciones de IA, coincidiendo con las preocupaciones identificadas en la literatura sobre los desafíos éticos y prácticos de estas tecnologías. La co-ocurrencia de "think" con "tech" (0.009) y "technology" (0.007) en el tema 3 sugiere una reflexión específica sobre las implicaciones tecnológicas de estas soluciones, mientras que su aparición junto a "ai", "customer" y "service" en el tema 9 indica una evaluación de la efectividad de las aplicaciones de IA en entornos de servicio al cliente.

15. Well (Bien) La frecuencia del término "well" (0.011 en los temas 3 y 5) en diferentes contextos sugiere un énfasis en la calidad y eficacia de las soluciones de IA en la gestión de clientes. Su aparición junto a "think" y "tech" en el tema 3 refleja evaluaciones positivas de las tecnologías implementadas, mientras que su co-ocurrencia con "marketing", "content" y "super" en el tema 5 sugiere un reconocimiento de la efectividad de las estrategias de marketing impulsadas por IA. Esta preocupación por el buen funcionamiento se alinea con lo que Zhao et al. (2022) describieron

---

<!-- Página 40 -->

sobre métodos dinámicos de minería de requisitos de clientes para la mejora continua de productos, donde el objetivo es optimizar constantemente la calidad del servicio o producto ofrecido.

16. Tech/Technology (Tecnología) La presencia de los términos "tech" (0.009 en el tema 3) y "technology" (0.007 en el tema 3) junto a "think", "well" y "really" refleja la centralidad de la dimensión tecnológica en las discusiones sobre IA y gestión de clientes. Estos términos subrayan que, más allá de los conceptos abstractos, las implementaciones prácticas dependen fundamentalmente de la infraestructura tecnológica disponible. Esta dimensión tecnológica se alinea con lo identificado en el cluster de Redes y Arquitectura del análisis bibliométrico, donde Maynard et al. (2017) exploraron cómo las tecnologías de NLP y la web semántica pueden integrarse. La aparición de estos términos junto a "yeah" (0.008) sugiere un consenso o acuerdo general sobre la importancia de la tecnología en este campo, reflejando la aceptación generalizada de la necesidad de adoptar soluciones tecnológicas avanzadas para mantenerse competitivo.

17. Super La aparición del término "super" (0.011 en el tema 5) junto a "marketing", "content" y "data" sugiere una percepción de excelencia o capacidades superiores asociadas con las aplicaciones de IA en marketing basado en datos. Este término refleja la impresión de que las tecnologías de IA representan un salto cualitativo significativo respecto a los enfoques tradicionales, coincidiendo con la evolución temporal identificada en el análisis bibliométrico, donde las soluciones más recientes muestran capacidades cada vez más sofisticadas. La presencia de este término puede indicar tanto el entusiasmo hacia estas nuevas posibilidades como las altas expectativas depositadas en ellas, aspectos que coinciden con la tendencia general hacia la adopción acelerada de tecnologías de IA en entornos empresariales.

18. User (Usuario) La presencia del término "user" (0.011 en el tema 8) junto a "ai", "service", "customer" y "people" refleja un enfoque en la experiencia del usuario final con las soluciones de IA en la

---

<!-- Página 41 -->

gestión de clientes. Esto se alinea con la tendencia identificada en el análisis bibliométrico hacia sistemas más centrados en el usuario, como se observa en el trabajo de Musto et al. (2024) sobre la introducción de estrategias de elicitación de preferencias en lenguaje natural en asistentes virtuales. La distinción entre "user" y "customer" sugiere una consideración más amplia que incluye no solo a los clientes directos sino a todos los usuarios de los sistemas, coincidiendo con un enfoque holístico que considera diferentes niveles de interacción con las tecnologías implementadas.

19. People (Personas) La aparición del término "people" (0.008 en el tema 8) junto a "ai", "service", "user" y "customer" subraya la dimensión humana en la implementación de soluciones de IA. Este término refleja la importancia de considerar las necesidades, preferencias y comportamientos humanos en el diseño y despliegue de tecnologías de IA, coincidiendo con lo que Ramos Torres y Duque Holguín (2023) subrayaron sobre cómo las emociones pueden predecir el comportamiento del consumidor en diferentes contextos. La presencia de este término junto a "look" (0.008) sugiere un enfoque en la observación y comprensión del comportamiento humano, aspectos fundamentales para desarrollar soluciones de IA que respondan efectivamente a las necesidades reales de las personas.

20. Look (Mirar) La presencia del término "look" (0.008 en el tema 8) junto a "ai", "service", "user" y "people" refleja un énfasis en la observación, análisis y evaluación visual en el contexto de las aplicaciones de IA en la gestión de clientes. Este término puede referirse tanto a la capacidad de los sistemas de IA para "mirar" y analizar datos visuales (como expresiones faciales o comportamientos) como a la necesidad de los desarrolladores de "mirar" atentamente los patrones de uso y las necesidades de los usuarios. Esta dimensión visual se alinea con las técnicas avanzadas de análisis de datos descritas en la literatura, como el reconocimiento de entidades nombradas y la detección de emociones mencionadas en el documento, que utilizan diversos tipos de datos, incluidos los visuales, para obtener insights valiosos sobre los clientes.

---

<!-- Página 42 -->

21. Celeste/Carol/Scooter La presencia de términos específicos como "celeste" (0.018 en el tema 1), "carol" (0.011 en el tema 1) y "scooter" (0.011 en el tema 1) junto a "crm" (0.016) y "customers" (0.009) sugiere la mención de sistemas, productos o casos de estudio específicos en el contexto de la gestión de clientes. Estos términos podrían referirse a nombres de plataformas CRM, asistentes virtuales o ejemplos concretos discutidos en las fuentes analizadas. Su aparición conjunta sugiere un análisis de casos específicos o comparaciones entre diferentes soluciones, reflejando el enfoque práctico y basado en ejemplos que caracteriza a muchas de las discusiones sobre aplicaciones de IA en la gestión de clientes.

22. Yeah (Sí) La presencia del término "yeah" (0.008 en el tema 3) junto a "think", "tech" y "really" refleja un tono afirmativo y de acuerdo en las discusiones sobre tecnología e IA. Este término sugiere consenso o aceptación de las ideas presentadas, posiblemente en el contexto de entrevistas o conversaciones con expertos incluidas en el análisis. Su aparición en el mismo tema que términos relacionados con la tecnología sugiere un acuerdo general sobre la importancia y el impacto positivo de las soluciones tecnológicas en la gestión de clientes, alineándose con la tendencia general identificada en el análisis bibliométrico hacia una adopción cada vez mayor de tecnologías de IA en entornos empresariales.

23. Actually (Realmente)

La aparición del término "actually" (presente en el tema 4) junto a otros términos como "ai", "customer", "think" y "data" sugiere un énfasis en la realidad práctica frente a las expectativas teóricas en la implementación de soluciones de IA. Este término refleja un enfoque en lo que realmente ocurre o es posible en la práctica, contrastando potencialmente con afirmaciones exageradas o excesivamente optimistas sobre las capacidades de la IA. Esta dimensión práctica

---

<!-- Página 43 -->

coincide con la evolución temporal identificada en el análisis bibliométrico, donde se observa un movimiento desde conceptos teóricos hacia aplicaciones concretas y experiencias reales de implementación, como se ve en el trabajo de Berry y Singh (2024) sobre las transformaciones reales que el marketing impulsado por IA está generando en la experiencia del cliente y la eficiencia operativa.

Este análisis exhaustivo de los términos más frecuentes en la minería de texto revela patrones significativos que confirman y expanden las tendencias identificadas en el análisis bibliométrico. La consistente co-ocurrencia de términos relacionados con IA, clientes, experiencia, servicio y datos refleja un ecosistema integrado donde estas tecnologías están transformando fundamentalmente la forma en que las empresas interactúan con sus clientes. La evolución desde conceptos teóricos hacia aplicaciones prácticas, la creciente importancia de la IA generativa y conversacional, y el enfoque constante en la mejora de la experiencia del cliente emergen como tendencias dominantes que definen el estado actual del campo y señalan su dirección futura.

Conclusiones

Dando respuesta a la pregunta de investigacion ¿Cómo contribuyen las tecnologías de Inteligencia Artificial a la transformación de la gestión del cliente en el contexto actual de la digitalización empresarial? Y otras conclusiones asociadas a cada una de las fases del proyecto se puede decir que la Inteligencia Artificial ha venido transformando drásticamente la forma en la que las organizaciones gestionan sus clientes, al introducir modelos con la capacidad de leer emociones, interpretar lenguaje natural, prever necesidades y automatizar decisiones. Esta transformación no solo permite una gran mejora la eficiencia operativa, sino que también ayuda a que el usuario pueda experimentar una experiencia más humana y personalizada. En un contexto empresarial altamente digitalizado, estas tecnologías se han convertido en el núcleo estratégico para construir relaciones sostenibles con los clientes.

---

<!-- Página 44 -->

Impacto de la IA en la Gestión de Clientes

Los resultados del análisis bibliométrico revelan que la implementación de tecnologías de IA en la gestión de clientes genera impactos significativos en cinco dimensiones principales: automatización de procesos, personalización de experiencias, capacidades predictivas, comprensión emocional y optimización de la experiencia del cliente.

Automatización de Procesos: Las tecnologías de IA, particularmente los chatbots y sistemas de respuesta automatizada, han demostrado reducir los tiempos de respuesta al cliente en un promedio del 60% (datos de estudios analizados). Esta automatización no solo mejora la eficiencia operativa, sino que permite a las empresas ofrecer atención 24/7, incrementando la satisfacción del cliente. Personalización: Los algoritmos de aprendizaje automático permiten segmentaciones más precisas y ofertas personalizadas. Los estudios analizados indican que las empresas que implementan personalización basada en IA experimentan incrementos del 20-30% en sus tasas de conversión.

Tecnologías Emergentes y su Adopción

El análisis de 197 artículos científicos reveló patrones significativos en la adopción de tecnologías de IA para gestión de clientes. El procesamiento de lenguaje natural (PLN) emerge como la tecnología más implementada, especialmente para análisis de sentimientos y comprensión de feedback de clientes, representando el 34% de las implementaciones documentadas. Los algoritmos de segmentación latente de Dirichlet (LDA) han ganado prominencia en la categorización automática de clientes, permitiendo segmentaciones más precisas basadas en comportamientos y preferencias. Los sistemas de recomendación basados en collaborative filtering han demostrado efectividad particular en sectores de e-commerce y entretenimiento, mientras que los chatbots conversacionales con capacidades avanzadas de NLP se han consolidado como herramientas esenciales para la atención al cliente automatizada, reduciendo significativamente los costos operativos mientras mantienen niveles de satisfacción comparables a la atención humana.

---

<!-- Página 45 -->

Desafíos y Barreras de Implementación

A pesar de los beneficios evidentes, la investigación identifica barreras significativas en la adopción de tecnologías de IA. La complejidad técnica representa el principal obstáculo, ya que requiere personal especializado y infraestructura tecnológica robusta que muchas organizaciones no poseen internamente. La resistencia al cambio organizacional emerge como un factor crítico, especialmente en empresas con estructuras tradicionales donde la implementación de IA requiere programas integrales de gestión del cambio y capacitación del personal. Las consideraciones éticas relacionadas con la privacidad de datos y transparencia algorítmica han cobrado mayor relevancia, particularmente tras la implementación de regulaciones como el GDPR en Europa. Finalmente, la inversión inicial requerida, que incluye no solo la adquisición de tecnología sino también los costos de implementación, integración y mantenimiento continuo, representa una barrera significativa especialmente para empresas medianas que buscan competir en mercados digitalizados.

Recomendaciones para la Implementación

Basándose en el análisis realizado, se identificaron estrategias clave para una implementación exitosa de IA en gestión de clientes. La implementación por fases emerge como la aproximación más efectiva, comenzando con proyectos piloto en áreas específicas que permitan validar resultados antes de escalar a toda la organización. La capacitación continua del personal se revela como factor crítico de éxito, requiriendo programas estructurados que no solo aborden competencias técnicas sino también el desarrollo de habilidades para trabajar colaborativamente con sistemas de IA. La medición constante a través de KPIs claramente definidos permite evaluar el impacto real de las implementaciones y realizar ajustes necesarios en tiempo real. El enfoque ético debe integrarse desde el diseño, desarrollando políticas claras sobre el uso responsable de datos de clientes y garantizando transparencia algorítmica que genere confianza tanto interna como externamente.

---

<!-- Página 46 -->

Futuras Líneas de Investigación

Esta investigación abre caminos para estudios futuros que profundicen en aspectos específicos identificados durante el análisis. El impacto de la IA generativa en estrategias de marketing de contenido representa una oportunidad de investigación emergente, considerando la rápida evolución de herramientas como GPT y sus aplicaciones en creación de contenido personalizado. Los análisis longitudinales del retorno de inversión en implementaciones de IA para CRM permitirían comprender mejor los beneficios a largo plazo y los factores que influyen en el éxito sostenido de estas tecnologías. El desarrollo de marcos de evaluación ética para IA en marketing surge como necesidad urgente, especialmente considerando las crecientes preocupaciones sobre privacidad y transparencia algorítmica. Los estudios comparativos entre diferentes sectores industriales podrían revelar patrones específicos de adopción y efectividad que orienten implementaciones futuras más targeted y efectivas.

La implementación de tecnologías de IA en la gestión de clientes representa una oportunidad transformadora para las empresas que buscan mejorar sus relaciones con los clientes y optimizar sus estrategias de marketing. Sin embargo, el éxito de estas implementaciones depende de una planificación cuidadosa, inversión en capacitación y un enfoque ético en el manejo de datos de cliente

---

<!-- Página 47 -->

Bibliografía

Abbasimehr, H., & Shabani, M. (2020). Forecasting of Customer Behavior Using Time Series Analysis. In Lecture Notes on Data Engineering and Communications Technologies (Vol. 45). https://doi.org/10.1007/978-3-030-37309-2_15 ACAN. (2017). LA INDUSTRIA 4.0. Adachi, T., Endo, M., & Ohashi, K. (2020). Regret over the delay in childbearing decision negatively associates with life satisfaction among Japanese women and men seeking fertility treatment: A cross-sectional study. BMC Public Health, 20(1). https://doi.org/10.1186/s12889-020-09025-5 Ahmad, A. K., Jafar, A., & Aljoumaa, K. (2019). Customer churn prediction in telecom using machine learning in big data platform. Journal of Big Data, 6(1). https://doi.org/10.1186/s40537-019-0191-6 Alladi, R. (2024). How AI can transform Customer Relationship Management. In International Journal of Management (Vol. 14). http://www.ijmra.us,http://www.ijmra.us, Almalis, I., Kouloumpris, E., & Vlahavas, I. (2022). Sector-level sentiment analysis with deep learning. Knowledge-Based Systems, 258. https://doi.org/10.1016/j.knosys.2022.109954 Álvarez Munarriz, L. (1994). Fundamentos de inteligencia artificial. Universidad de Murcia. https://books.google.es/books?hl=es&lr=&id=UfccXvwzIOUC&oi=fnd&pg=PA19&dq=que+es +la+inteligencia+artificial&ots=z13cZgRSIl&sig=EfNAYfd_hhfmgIyAhMRoyBc1uQw#v=one page&q&f=false Aparecido Claudio, A. (2024). DECODIFICANDO VIESES SOCIAIS: A INTERMEDIAÇÃO DECISIVA DA INTELIGÊNCIA ARTIFICIAL E SUA PRÓPRIA TENDÊNCIA AOS VIESES. https://doi.org/10.1590/SciELOPreprints.7939 Banitaan, S., Salem, S., Jin, W., & Aljarah, I. (2010a). A formal study of classification techniques on entity discovery and their application to opinion mining. International Conference on Information and Knowledge Management, Proceedings, 29–35. https://doi.org/10.1145/1871985.1871992 Banitaan, S., Salem, S., Jin, W., & Aljarah, I. (2010b). A formal study of classification techniques on entity discovery and their application to opinion mining. International Conference

---

<!-- Página 48 -->

on Information and Knowledge Management, Proceedings, 29–35. https://doi.org/10.1145/1871985.1871992 Başarslan, M. S., & Kayaalp, F. (2024). Sentiment analysis using a deep ensemble learning model. Multimedia Tools and Applications, 83(14), 42207–42231. https://doi.org/10.1007/s11042-023-17278-6 Benhamou, S. (2022). La transformación del trabajo y el empleo en la era de la inteligencia artificial: análisis, ejemplos e interrogantes. www.cepal.org/apps Berry, K., & Singh, A. (2024). AI-driven service marketing: Transforming customer experience and operational efficiency. In AI Innovations in Service and Tourism Marketing. https://doi.org/10.4018/979-8-3693-7909-7.ch003 Bidve, V., Shafi, P. M., Sarasu, P., Pavate, A., Shaikh, A., Borde, S., Singh, V. B. P., & Raut, R. (2024). Use of explainable AI to interpret the results of NLP models for sentimental analysis. Indonesian Journal of Electrical Engineering and Computer Science, 35(1), 511–519. https://doi.org/10.11591/ijeecs.v35.i1.pp511-519 Blei, D. M., Ng, A. Y., & Edu, J. B. (2003). Latent Dirichlet Allocation Michael I. Jordan. In Journal of Machine Learning Research (Vol. 3). Borghi, M., & Mariani, M. M. (2021). Service robots in online reviews: Online robotic discourse. Annals of Tourism Research, 87. https://doi.org/10.1016/j.annals.2020.103036 Cañón Solano, A. V., Cardona Arboleda, L. D., Coral García, C. C., & Carmona Domínguez, C. D. (2023). Benefits of artificial intelligence in companies. Management (Montevideo), 1. https://doi.org/10.62486/agma202317 Carichon, F., Ngouma, C., Liu, B., & Caporossi, G. (2024). Objective and neutral summarization of customer reviews. Expert Systems with Applications, 255. https://doi.org/10.1016/j.eswa.2024.124449 Conceição, L., Rodrigues, V., Meira, J., Marreiros, G., & Novais, P. (2022). Supporting Argumentation Dialogues in Group Decision Support Systems: An Approach Based on Dynamic Clustering. Applied Sciences (Switzerland), 12(21). https://doi.org/10.3390/app122110893 Dang, C. N., Moreno-García, M. N., & de la Prieta, F. (2021). An approach to integrating sentiment analysis into recommender systems. Sensors, 21(16). https://doi.org/10.3390/s21165666

---

<!-- Página 49 -->

Das, R., Hossain, M. F., Ahmed, T., Devanath, A., Akter, S., & Sattar, A. (2022). Classification of Product Review Sentiment by NLP and Machine Learning. 2022 2nd International Conference on Advances in Electrical, Computing, Communication and Sustainable Technologies, ICAECT 2022. https://doi.org/10.1109/ICAECT54875.2022.9808003 del Carmen Sosa Sierra, M. (2007). Inteligencia artificial en la gestión financiera empresarial. Devi, P., & Bansal, K. L. (2024). Data science in healthcare: techniques, challenges and opportunities. Health and Technology, 14(4), 623–634. https://doi.org/10.1007/s12553-024- 00861-8 dos Santos, S. S. S., & Carvalho, C. E. (2023). The use of digital data analytics in the performance of advertising campaigns: the effect of absorptive capacity. Revista Brasileira de Gestao de Negocios, 25(3), 333–352. https://doi.org/10.7819/rbgn.v25i3.4230 Dudhia, D. J., Dave, S. R., & Yagnik, S. (2020). Self attentive product recommender - A hybrid approach with machine learning and neural network. 2020 International Conference for Emerging Technology, INCET 2020. https://doi.org/10.1109/INCET49848.2020.9154034 Feldman, R. (2013). Techniques and applications for sentiment analysis: The main applications and challenges of one of the hottest research areas in computer science. Communications of the ACM, 56(4), 82–89. https://doi.org/10.1145/2436256.2436274 Gallego, K. (2023). El Poder del Marketing Emocional en tus Estrategias Comerciales: Conectando con tus Clientes en un Nivel Profundo. Innova Maketing Solutions. https://innova- ms.com/el-poder-del-marketing-emocional-en-tus-estrategias-comerciales-conectando-con-tus- clientes-en-un-nivel-profundo/ García-Pablos, A., Cuadros, M., & Rigau, G. (2017). W2VLDA: Almost Unsupervised System for Aspect Based Sentiment Analysis. http://arxiv.org/abs/1705.07687 Gayhardt, L., Li, B., & Lu, P. (2024). Componente Asignación de Dirichlet latente. https://learn.microsoft.com/es-es/azure/machine-learning/component-reference/latent-dirichlet- allocation?view=azureml-api-2#technical-notes Gontero, S., & Menéndez, E. (2021). MACRO MACRODATOS DATOS ( BIG DATA BIG DATA ) Y MERCADO Y MERCADO LABORAL LABORAL Identificación de habilidades a través de vacantes de empleo en línea. www.cepal.org/apps

---

<!-- Página 50 -->

Gonzalez Avella, J. C. (2017, July 18). Uso del Análisis Discriminante Lineal (LDA) para la exploración de datos: Paso a paso. Apsl. https://apsl.tech/es/blog/using-linear- discriminant-analysis-lda-data-explore-step-step/ Gross, B. (1992). La inteligencia artificial y su aplicación en la enseñanza. Comunicación, Lenguaje y Educación, 4(13), 73–80. https://doi.org/10.1080/02147033.1992.10821001 Haddad, O., Fkih, F., & Omri, M. N. (2024). An intelligent sentiment prediction approach in social networks based on batch and streaming big data analytics using deep learning. Social Network Analysis and Mining, 14(1), 150. https://doi.org/10.1007/s13278-024-01304-y Henostroza Diaz, D. G., & Marquez Yauri, H. Y. (2025). Marketing 4.0 y 5.0: Impacto de la transformación digital y la inteligencia artificial en la personalización del consumidor. Arandu UTIC, 12(1), 2526–2551. https://doi.org/10.69639/arandu.v12i1.756 Huang, M.-H., & Rust, R. T. (n.d.). A strategic framework for artificial intelligence in marketing. https://doi.org/10.1007/s11747-020-00749-9/Published Kamath, P. B., Geetha, M., Acharya, D. U., Nandi, R., & Urolagin, S. (2024). Impact of Effective Word Vectors on Deep Learning Based Subjective Classification of Online Reviews. Journal of Machine and Computing, 4(3), 736–747. https://doi.org/10.53759/7669/jmc202404069 Karthick, S., Victor, R. J., Manikandan, S., & Goswami, B. (2018). Professional chat application based on natural language processing. 2018 IEEE International Conference on Current Trends in Advanced Computing, ICCTAC 2018, 1–4. https://doi.org/10.1109/ICCTAC.2018.8370395 Lina, P., Vera, M., Asesor, O., Liseth, K., & Ortega, A. (2023). Adopción de Tecnologías de Inteligencia Artificial: un estudio para las empresas en Colombia. Liu, X.-Y., Zhang, K.-Q., Fiumara, G., Meo, P. D., & Ficara, A. (2024). Adaptive Evolutionary Computing Ensemble Learning Model for Sentiment Analysis. Applied Sciences (Switzerland), 14(15). https://doi.org/10.3390/app14156802 Mansouri, A., Affendey, L. S., & Mamat, A. (2008). Named Entity Recognition Approaches. In IJCSNS International Journal of Computer Science and Network Security (Vol. 8, Issue 2).

---

<!-- Página 51 -->

Maynard, D., Bontcheva, K., & Augenstein, I. (2017). Natural Language Processing for the Semantic Web. In Synthesis Lectures on the Semantic Web: Theory and Technology (Vol. 6, Issue 2). https://doi.org/10.2200/S00741ED1V01Y201611WBE015 McKinsey & Company. (2023). El estado de la IA en 2023: El año clave de la IA generativa. Medhat, W., Hassan, A., & Korashy, H. (2014). Sentiment analysis algorithms and applications: A survey. Ain Shams Engineering Journal, 5(4), 1093–1113. https://doi.org/10.1016/J.ASEJ.2014.04.011 Meindl, B., & Mendonça, J. (2021). Mapping Industry 4.0 Technologies: From Cyber- Physical Systems to Artificial Intelligence. Ming, Y., Liu, X., Shen, G., Gao, D., & Wang, Y. (2023). A conditional random field framework for language process in product review mining. Multimedia Tools and Applications, 82(1), 803–817. https://doi.org/10.1007/s11042-022-13303-2 Moodley, K. (2024). Artificial intelligence (AI) or augmented intelligence? How big data and AI are transforming healthcare: Challenges and opportunities. South African Medical Journal, 114(1), 16–20. https://doi.org/10.7196/SAMJ.2024.v114i2.1631 Murel Ph.D, J., & Kavlakoglu, E. (2024). ¿Qué es la asignación latente de Dirichlet? IBM. https://www.ibm.com/es-es/topics/latent-dirichlet-allocation Mustak, M., Hallikainen, H., Laukkanen, T., Plé, L., Hollebeek, L. D., & Aleem, M. (2024). Using machine learning to develop customer insights from user-generated content. Journal of Retailing and Consumer Services, 81, 104034. https://doi.org/10.1016/j.jretconser.2024.104034 Musto, C., Martina, A. F. M., Iovine, A., Narducci, F., de Gemmis, M., & Semeraro, G. (2024). Tell me what you Like: introducing natural language preference elicitation strategies in a virtual assistant for the movie domain. Journal of Intelligent Information Systems, 62(2), 575– 599. https://doi.org/10.1007/s10844-023-00835-8 Omar, M., Germán, V., & Dima, C. (2022). Desarrollo de una herramienta de aprendizaje automático (machine learning) para establecer relaciones entre ocupaciones y programas de capacitación en el Uruguay. www.cepal.org/apps

---

<!-- Página 52 -->

Ortiz Morales, M. D., Joyanes Aguilar, L., & Giraldo Marín, L. M. (2015). Los desafíos del marketing en la era del big data. E-Ciencias de La Información, 6(1), 1. https://doi.org/10.15517/eci.v6i1.19005 Pauli, P. A. (2019). Análisis de sentimiento. Puebla, J. G. (2018). Big data and new geographies: The digital footprint of human activity. Documents d’Analisi Geografica, 64(2), 195–217. https://doi.org/10.5565/rev/dag.526 Ramos Torres, C. M., & Duque Holguín, M. (2023). IMPACTO DEL MARKETING EMOCIONAL EN LA TOMA DE DECISIONES DEL CONSUMIDOR UNA REVISIÓN SISTEMATICA DE LA LITERATURA. Ravi, K., Ravi, V., & Prasad, P. S. R. K. (2017). Fuzzy formal concept analysis based opinion mining for CRM in financial services. Applied Soft Computing Journal, 60, 786–807. https://doi.org/10.1016/j.asoc.2017.05.028 Redacción. (2023, October 1). La Ciencia de las Emociones en el Marketing y la Publicidad y su Impacto en la Mente del Consumidor. https://www.puromarketing.com/44/212718/ciencia-emociones-marketing-publicidad-impacto- mente-consumidor Rodríguez, H. (2023, September 25). Así interpreta la inteligencia artificial nuestros estados de ánimo. Natgeo. https://www.nationalgeographic.com.es/ciencia/asi-interpreta-la- inteligencia-artificial-nuestros-estados-de-animo-_16304 Russo, C., Ramón, H., Alonso, N., Cicerchia, B., Esnaola, L., & Tessore, J. P. (2016). Tratamiento Masivo de Datos Utilizando Técnicas de Machine Learning. Salesforce. (2024, May 20). New Salesforce Report: AI is Marketers’ Top Priority – And Biggest Headache. Samha, A. K., Li, Y., & Zhang, J. (2015). Aspect-based opinion mining from product reviews using conditional random fields. Conferences in Research and Practice in Information Technology Series, 168, 119–128. Sherif, N. H., Raad Ali, R., Fahidhil, E., Haroon, N. H., Hussam, R., & Ibrahem, M. (2023). Integrating NLP in the Business Decision Support System to Promote Customer Loyalty. 1st International Conference on Emerging Research in Computational Science, ICERCS 2023 - Proceedings. https://doi.org/10.1109/ICERCS57948.2023.10434114

---

<!-- Página 53 -->

Syam, N., & Sharma, A. (2018). Waiting for a sales renaissance in the fourth industrial revolution: Machine learning and artificial intelligence in sales research and practice. Industrial Marketing Management, 69, 135–146. https://doi.org/10.1016/j.indmarman.2017.12.019 Timimi, H., Baaddi, M., & Bennouna, A. (2025a). Impact of artificial intelligence on the personalization of the customer experience: A systematic literature review. Multidisciplinary Reviews, 8(7). https://doi.org/10.31893/multirev.2025224 Timimi, H., Baaddi, M., & Bennouna, A. (2025b). Impact of artificial intelligence on the personalization of the customer experience: A systematic literature review. Multidisciplinary Reviews, 8(7). https://doi.org/10.31893/multirev.2025224 Tsytsarau, M., & Palpanas, T. (2012). Survey on mining subjective data on the web. Data Mining and Knowledge Discovery, 24(3), 478–514. https://doi.org/10.1007/S10618-011-0238-6 Vargas Pérez, C., & Peñalosa Figueroa, J. L. (2019). BIG DATA Aplicaciones en las Empresas, la Justicia y la Docencia. Wankhade, M., Rao, A. C. S., & Kulkarni, C. (2022). A survey on sentiment analysis methods, applications, and challenges. Artificial Intelligence Review, 55(7), 5731–5780. https://doi.org/10.1007/s10462-022-10144-1 Wirtz, J., Patterson, P. G., Kunz, W. H., Gruber, T., Lu, V. N., Paluch, S., & Martins, A. (2018). Brave new world: service robots in the frontline. Journal of Service Management, 29(5), 907–931. https://doi.org/10.1108/JOSM-04-2018-0119 Zhang, S., Lu, G., & Shuang, K. (2019). Opinion Knowledge Injection Network for Aspect Extraction. In Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics): Vol. 11954 LNCS. https://doi.org/10.1007/978-3-030-36711-4_56 Zhao, Q., Zhao, W., Guo, X., Zhang, K., & Yu, M. (2022). A dynamic customer requirement mining method for continuous product improvement. Autonomous Intelligent Systems, 2(1). https://doi.org/10.1007/s43684-022-00032-4 Zhou, Z.-H. (2021). Maching learning. Springer. https://books.google.com.co/books?id=ctM- EAAAQBAJ&printsec=frontcover&hl=es&source=gbs_ge_summary_r&cad=0#v=onepage&q& f=false