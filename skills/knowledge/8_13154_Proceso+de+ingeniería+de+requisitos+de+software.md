<!-- Página 1 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

Tipo de artículo: Artículo original Temática: Ingeniería de Requisitos

Proceso de ingeniería de requisitos de software en la dirección de Tecnología y Sistemas del Ministerio del Interior

Software requirements engineering process in the Technology and Systems Directorate of the Ministry of the Interior

1* Yilian Rodríguez Gille https://orcid.org/0009-0009-9677-3828

2 Yoandy Lazo Alvarado https://orcid.org/0000-0002-8285-2180

1 Cuba. Universidad de Ciencias Informáticas.

2 Ministerio de Comunicaciones, avenida Independencia, No. 2, entre 19 de Mayo y Aranguren, Plaza de la Revolución, La Habana, Cuba

*Autor para la correspondencia. (yr.grille@gmail.com)

Editorial “Ediciones Futuro”142 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 2 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

RESUMEN

El desarrollo de software implica procesos que si no están bien definidos puede tener consecuencias negativas, el área de la ingeniería de requisitos es fundamental en el ciclo de vida de desarrollo del software, no realizarla correctamente implica riesgos que influyen en la calidad del producto. El Modelo de Calidad para el Desarrollo de Aplicaciones Informáticas cubano proporciona, al igual que otros modelos internacionales, buenas prácticas a seguir para mejorar los procesos de desarrollo, teniendo en cuenta las características nacionales. El Ministerio del Interior ha creado su propio marco de trabajo basándose en las mejores prácticas de modelos internacionales. La presente investigación tiene como objetivo desarrollar un proceso de Ingeniería de Requisitos de software que contribuya a disminuir las fallas que tengan como causa raíz los requisitos durante el ciclo de vida de desarrollo de soluciones informáticas en la Dirección de Tecnología y Sistemas del Ministerio del Interior. Se utilizaron métodos científicos teóricos y empíricos que permitieron conocer los conceptos y modelos relacionados con el tema, así como realizar un análisis de los documentos que rigen el desarrollo y gestión de proyectos en la institución. Como resultado se obtiene un proceso de Ingeniería de Requisitos de software en la Dirección de Tecnología y Sistemas del Ministerio del Interior que define los roles, responsabilidades, actividades, tareas y artefactos de entrada/salida que estarán involucrados en cada actividad del proceso, se incluya en las normas y se institucionalice en la institución, para la obtención de productos de calidad.

Palabras clave: ingeniería de requisitos; modelo de calidad; mejora de proceso; buenas prácticas

ABSTRACT

Software development involves processes that, if not well defined, can have negative consequences. The area of requirements engineering is fundamental in the software development life cycle. Not performing it correctly implies risks that influence the quality of the product. The Cuban Quality Model for the Development of Computer Applications provides, like other international models, good practices to follow to improve development processes, taking into account national characteristics. The Ministry of the Interior has created its own framework based on the best practices of international models. This research aims to

Editorial “Ediciones Futuro”143 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 3 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

develop a Software Requirements Engineering process that contributes to reduce failures that have as their root cause the requirements during the development life cycle of computer solutions in the Directorate of Technology and Systems of the Ministry of the Interior. Theoretical and empirical scientific methods were used to understand the concepts and models related to the topic, as well as to analyze the documents that govern the development and management of projects in the institution. As a result, a Software Requirements Engineering process is obtained in the Directorate of Technology and Systems of the Ministry of the Interior that defines the roles, responsibilities, activities, tasks and input/output artifacts that will be involved in each activity of the process, is included in the standards and is institutionalized in the institution, to obtain quality products.

Keywords: requirements engineering; quality model; process improvement; good practices

Recibido: 27/10/2025 Aceptado: 12/01/2026 Publicado: 12/01/2026

## Introducción

La competencia creciente entre empresas va a un ritmo acelerado provocado por el surgimiento de nuevas tecnologías que tienen como finalidad brindar un mejor servicio, que permita la satisfacción del cliente al ofrecerle rapidez, confianza, óptimas soluciones y bajo costo (García, 2018; Barragán, 2022; Trujillo & García 2012). Las empresas de software mundialmente centran su interés en obtener el producto en el menor tiempo posible y sin descuidar la calidad (Tomaselli, 2019). Para asegurar la calidad del proceso de desarrollo de los productos de software se han creado modelos de referencia de procesos como: el Modelo de Capacidad de Madurez Integrada para Desarrollo (CMMI-DEV), el Modelo de Procesos para la Industria de Software (MoProSoft) en México, la iniciativa Mejora de Procesos de Software Brasileño (MPS.Br), el

Editorial “Ediciones Futuro”144 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 4 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

proyecto de Mejora de Procesos para Fomentar la Competitividad de la Pequeña y Mediana Industria del Software de Iberoamérica (COMPETISOFT), el Modelo de Calidad de Desarrollo de Aplicaciones Informáticas (MCDAI) en Cuba, entre otros; colecciones de buenas prácticas que ayudan a las organizaciones a mejorar sus procesos, durante todo el ciclo de vida del producto en las distintas áreas del conocimiento (Coque, Jurado, Avendaño & Pizarro, 2017; Suarez & Leon, 2019; Machado, Mexas & de Oliveira, 2019; Ganvini, Martínez, & Soriano 2023). La Mejora de Procesos Software (MPS) es definida por Trujillo como un “proceso sistémico, con independencia del enfoque adoptado, requiere de cierto tiempo, recursos, medidas y las iteraciones para su aplicación efectiva y exitosa. Su objetivo es mejorar el rendimiento del proceso de desarrollo de software, a partir de desarrollar acciones que se manifiestan en modificaciones al proceso de desarrollo de software” (Trujillo, Febles, & León, 2015). Los esfuerzos para conseguir un mejor producto software han derivado en el desarrollo de varios modelos de mejora de procesos. Ejemplo de ello son los modelos de mejora continua como PDCA (acrónimo en inglés de Plan, Do, Chek, Act), Impact, IDEAL y Bootstrap que promueven una optimización cíclica y estructurada para conducir la mejora. El Modelo IDEAL fue desarrollado por el SEI como un modelo de ciclo de vida para la mejora de procesos, su objetivo es la adopción de las prácticas sustentadas por CMMI, y debe su nombre a las cinco fases de trabajo Iniciación, Diagnóstico, Establecer, Actuar y Aprender. El modelo está diseñado como un modelo cíclico, en el cual una vez se han terminado de ejecutar las diferentes actividades que este involucra, se debe volver a iniciar el ciclo de mejoramiento, llevando a cabo las mismas actividades, pero definiendo nuevos objetivos para el ciclo que comienza. IDEAL es ampliamente usado, su adaptación es la forma más utilizada para conducir la mejora. Es un modelo disponible públicamente, e implementa el modelo PDCA (McFeeley, 1996; Aguileta, Ancona, Leon & Ucan, 2015; Bayona, Chamilco & Perez, 2020). Luego de analizar los modelos de referencia de procesos mencionados anteriormente se identifica que las principales áreas del conocimiento que intervienen en el proceso de desarrollo de software son: Gestión del Conocimiento, Gestión de Adquisiciones, Ingeniería de Requisitos (IR), Implementación, Pruebas de Software, Gestión de Riesgos, Medición y Análisis, Aseguramiento a la Calidad, Gestión de Configuración, entre otros. La presente investigación se centra en la IR, que es una de las disciplinas fundamentales de la ingeniería de software.

Editorial “Ediciones Futuro”145 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 5 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

El espectro amplio de tareas y técnicas que llevan a entender los requisitos se denomina Ingeniería de Requisitos (IR) (Pressman, 2010). Karl Wiegers la divide en desarrollo de los requisitos y gestión de los requisitos (Wiegers & Beatty, 2013). En el glosario de términos de la IREB (del inglés Internacional Requirements Engineering Board) se define la IR como, un enfoque sistemático y disciplinado para la especificación y gestión de requisitos con el objetivo de comprender los deseos y necesidades de las partes interesadas y minimizar el riesgo de entregar un sistema que no satisfaga dichos deseos y necesidades (Glinz, 2020). En el SWEBOK (del inglés Software Engineering Body of Knowledge) un requisito de software es descrito como una propiedad que debe ser exhibida por el software desarrollado o adaptado para resolver algún problema particular (Bourque & Dupuis, 2014). Por su parte la Norma Cubana NC 1400-1:2021 define requisito como la necesidad o expectativa establecida, generalmente implícita u obligatoria, que expresa una condición o capacidad demandada por las partes interesadas o la organización, que debe cumplir o poseer un proceso, producto o componente de producto para solucionar un problema o lograr un objetivo y para satisfacer un contrato, norma, especificación u otros documentos impuestos formalmente (MINCOM, 2021). Se asume en esta investigación la brindada en esta norma, que reúne los elementos esenciales planteados por modelos y estándares internacionales. La IR proporciona el mecanismo apropiado para entender lo que desea el cliente. Incluye siete tareas diferentes: concepción, indagación, elaboración, negociación, especificación, validación y administración. Es importante notar que algunas de estas tareas ocurren en paralelo y que todas se adaptan a las necesidades del proyecto (Pressman, 2010). De forma similar, aunque más sintetizada, Sommerville identifica que los procesos de IR incluyen cuatro actividades de alto nivel. Éstas se enfocan en valorar si el sistema es útil para la empresa (estudio de factibilidad), descubrir requisitos (adquisición y análisis), convertir dichos requisitos en alguna forma estándar (especificación) y comprobar que los requisitos definan realmente el sistema que quiere el cliente (validación). La IR es un proceso iterativo donde las actividades están entrelazadas (Sommerville, 2011).

Karl Wiegers ofrece buenas prácticas para el desarrollo de requisitos, las que subdivide en Elicitación, Análisis, Especificación y Validación. Abarca todas las actividades involucradas en explorar, evaluar,

Editorial “Ediciones Futuro”146 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 6 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

documentar y confirmar los requisitos de un producto. Para la gestión de requisitos incluye actividades como, definir una línea base de requisitos, con los RF y RNF revisados y aprobados; evaluar el impacto de los cambios de requisitos, negociar nuevos compromisos en función del impacto estimado de los cambios de requisitos; rastrear los requisitos; hacer un seguimiento del estado de los requisitos entre otros, con el objetivo de anticipar y acomodar los cambios para minimizar su impacto disruptivo en el proyecto (Wiegers & Beatty, 2013). Requisitos de Software, es una de las áreas del conocimiento de SWEBOK. Se ocupa de la obtención, el análisis, la especificación y la validación de los requisitos de software. Es ampliamente reconocido dentro de la industria del software que los proyectos de ingeniería de software son extremadamente vulnerables cuando estas actividades se realizan de manera deficiente (Bourque & Dupuis, 2014). Una IR adecuada añade valor en el proceso de desarrollo y evolución de un sistema: reduciendo el riesgo de desarrollar un sistema incorrecto, mejorando la comprensión del problema, siendo la base para estimar el esfuerzo y el coste del desarrollo y siendo prerrequisito para probar el sistema. Las principales tareas de esta disciplina, según IREB son, la educción, documentación, validación y la gestión de los requisitos, realizadas mayormente por el rol ingeniero de requisitos (Glinz, Leonhoud, Staal, & Bühne, 2024). La aplicación de las buenas prácticas en IR permite la mejora de la calidad del software, optimiza el tiempo y recursos, fortalece la relación del equipo de trabajo con los implicados y minimiza los riesgos de fracaso del proyecto. La Industria Cubana de Programas y Aplicaciones Informáticas (InCuSoft) es un pilar fundamental en la transformación digital del país. Tiene como objetivo, contribuir a respaldar las prioridades de la informatización en beneficio de la economía, la sociedad y la Seguridad y Defensa Nacional, para alcanzar un crecimiento sustancial de su ejecución y servicios asociados. Está compuesto por empresas estatales y privadas que se relacionan con el desarrollo de programas y aplicaciones informáticas y la prestación de servicios informáticos, y que estén inscritos en el control administrativo del Ministerio de Comunicaciones (Decreto No. 359, 2019). El MCDAI fue creado para impulsar el desarrollo de InCuSoft (MINCOM, 2021), está compuesto por doce procesos bases, entre ellos el de Ingeniería de requisitos; permite a las organizaciones alcanzar los niveles de madurez básico, intermedio y avanzado, y a los procesos el nivel de capacidad con iguales nombres. Los niveles de capacidad se alcanzan luego de implementar los requisitos genéricos y específicos.

Editorial “Ediciones Futuro”147 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 7 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

El Ministerio del Interior de la República de Cuba cuenta con la Dirección de Tecnología y Sistemas (DTS) que tiene como misión la informatización en función del conocimiento, dicha dirección forma parte de InCuSoft y para asegurar el cumplimiento de su misión cuenta con un marco de trabajo basado en las mejores prácticas de COBIT (del inglés Control Objectives for Information Systems and related Technology), ITIL (del inglés Information Technology Infrastructure Library) y PMBOK (del inglés Project Management Body of Knowledge). Al realizar la revisión documental del marco de trabajo se identificó que: establece el modelo del ciclo de vida de proyectos; se enfoca en la Gestión de Proyectos, Gestión de Implantación, Gestión de Cambios y la certificación del producto final. También se pudo identificar que las actividades de IR se concentran en las etapas de Iniciación y Planificación por lo que se puede afirmar que no se profundiza en ella y las acciones que realizan los equipos de desarrollo se sustentan sobre la base de la experiencia acumulada (MININT, 2011; MININT, 2015; MININT, 2017; MININT, 2019). Se realizó una entrevista a cinco jefes de proyectos y cuatro analistas de la DTS con el objetivo de conocer que buenas prácticas se implementan en la institución. Como resultado de dicha entrevista se pudo conocer que durante el proceso de desarrollo de soluciones informáticas se realizan las actividades: levantamiento de requisitos funcionales y la identificación de prioridades y reglas de validación, como resultado se obtiene la especificación de requerimientos funcionales aprobado por el jefe y la tarea técnica donde se describen los procesos de negocio. La entrevista también permitió identificar que durante el desarrollo de la solución informática existe poco entendimiento de los requisitos funcionales lo que provoca omisiones y ambigüedad; escaso control de cambios ya que se implementan sin un análisis y aprobación formal y no se documentan lo que provoca retrasos y retrabajo. Además de conocer qué buenas prácticas se utilizan en la institución para el desarrollo y gestión de requisitos, siendo el análisis, la especificación, el control de cambio y la trazabilidad de requisitos las más ausentes. El intercambio con los entrevistados permitió afirmar la relación entre la no implementación de buenas prácticas en la IR en la DTS con la calidad de los productos de software finales e inconformidades de los clientes con estos. Basado en la problemática expresada anteriormente se define el objetivo general de la presente investigación: Desarrollar un proceso de IR de software que contribuya a disminuir las fallas que tengan como causa raíz los requisitos durante el ciclo de vida de desarrollo de soluciones informáticas en la DTS del Ministerio del Interior.

Editorial “Ediciones Futuro”148 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 8 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

## Métodos o Metodología Computacional

Para lograr el objetivo trazado se realiza una investigación utilizando métodos como la revisión bibliográfica, lo cual permitió conocer los modelos de calidad existentes en el mundo y en el país, así como las buenas prácticas relacionadas con el proceso de IR. Se realizó un análisis histórico-lógico para conocer la evolución del proceso de IR.

Las entrevistas a especialistas de la DTS y el análisis documental permitieron identificar las fortalezas y las debilidades para enfrentar la mejora de proceso basado en el modelo de referencia MCDAI. Para conducir la MPS se utilizó el modelo IDEAL con el objetivo de implementar el PB IR del MCDAI. Las acciones propuestas por cada una de las fases para lograr la mejora de procesos en un ciclo inicial de IDEAL se especifican en la siguiente tabla:

Tabla 1 - Acciones propuestas por cada fase de IDEAL.

Fases 1: I – Iniciar 2: D - Diagnosticar 3: E - Establecer 4: A - Actuar 5: L - Aprender

Propósito Sentar las basesDeterminar dóndeDiseñar el procesoImplementar elEvaluar para la mejora delse encuentra la DTSde IR según elprocesoresultados, proceso de IR.en el área de IR,MCDAI integradoen proyectosaprender de la Establecerdónde se quiereal ciclo de vida depiloto yexperiencia y compromiso yllegar y conocer lasproyectos de lacapacitar equipos.ajustar el proceso. planificacióndificultades delDTS. inicial.estado actual. Acciones 1.- Comprometer a1.- Caracterizar1.- Mapear1.- Escoger1.- Definir la dirección de laestado actual de laactividades delCuaexperimento.métricas DTS.DTS.MCDAI al ciclo de2.- Realizarde éxito. 2.- Definir alcance.2.- Analizarvida de la DTS.capacitación.2.- Identificar 3.- Establecerejecución del2.- Establecer3.- Supervisar elmejoras y infraestructura yproceso IR actual.artefactos para elproceso.retroalimentarse recursos necesarios3.- Priorizarproceso IR de la4.- Realizarde problemasDTS.revisioneslas lecciones detectados.3.- Integración conperiódicas deaprendidas 4.- Aplicar elprocesos existentes.avance.3.- Actualizar el método deproceso. evaluación de4.- Aplicar el

Editorial “Ediciones Futuro”149 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 9 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

MCDAI al PB IR método de evaluación de MCDAI al PB IR. ResultadosSe conoce de laProceso IR actualActividades,CuaexperimentoLecciones esperadosimportancia de laevaluado a travésroles,implementadoaprendidas para MPS y se proponedel Método deresponsabilidades,con elmejorar en el definir un Procesoevaluación delartefactosproceso IRpróximo ciclo de IR basado enMCDAI, se obtienenecesarios para eldefinido.IDEAL. MCDAI ynivel de capacidadproceso IR gestionadodel proceso.definidos. mediante IDEAL, para institucionalizar en la DTS.

Se utiliza el Método de evaluación del MCDAI para determinar el nivel de capacidad de un PB para lo cual se debe realizar una evaluación de la conformidad de los requisitos genéricos y específicos correspondientes a cada nivel (básico intermedio y avanzado). Para obtener el nivel de capacidad básico, todos los requisitos genéricos y específicos tienen que estar evaluados de Altamente Implementado (AI) o Completamente Implementado (CI). Para el nivel Intermedio, todos los requisitos genéricos y específicos básicos tienen que estar evaluados de CI y los intermedios de AI o CI. Y para el avanzado todos los requisitos genéricos y específicos básicos e intermedios tienen que estar evaluados de CI y los avanzados de AI o CI. Los requisitos también pueden ser evaluados como No Implementados (NI) o Parcialmente implementado (PI), cuando no hay, o hay poca evidencia de cumplimiento del requisito del PB, en la entidad (MINCOM, 2021).

## Resultados y discusión

Diagnóstico El proceso para el desarrollo de software en la institución se aplica teniendo en cuenta la Gestión de Proyectos que han definido para realizar la creación de nuevas soluciones informáticas. Las actividades que se tienen en cuenta en el área de IR se muestran principalmente en las dos primeras etapas que conforman el ciclo de vida de las soluciones informáticas definidas por la institución (Inicio, planificación) y enfocadas en la Gestión de Proyectos. Al diagnosticar el proceso de IR según

Editorial “Ediciones Futuro”150 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 10 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

el MCDAI en la institución para el nivel básico de capacidad, se identificó que de los trece requisitos evaluados (genéricos y específicos) solo 5 son Altamente Implementados (AI) o Completamente Implementado (CI) lo que representa el 38,46% del total, como se muestra en la figura 1.

5

0 Total AI o CI Fig. 1- Requisitos del PB IR AI o CI.

Fuente: Elaboración propia

En la figura 2 se muestran el resultado de la evaluación de los ocho requisitos genéricos y los cinco requisitos específicos necesarios para el nivel de capacidad básico del pro ceso, obteniéndose como resultado que el requisito genérico uno, que responde a la definición/conceptualización del proceso no está implementado, y los siete requisitos genéricos restantes están parcialmente implementados. De los requisitos específicos existen tres altamente implementados y dos completamente implementados, que responde a definir los requisitos de las partes interesadas y a priorizar requisitos. Esta evaluación reafirma que el proceso de IR no es un proceso definido en la institución, aunque se realizan actividades de forma empírica correspondientes a la obtención, análisis, priorización y validación de los requisitos, no se cumple con el cien por ciento de los requisitos relacionados para el nivel de capacidad básico con grado de implementación entre alto y completo; según lo establecido en la NC 1400 MCDAI Parte 3: Guía de evaluación.

Editorial “Ediciones Futuro”151 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 11 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

Fig. 2- Aplicación del método de evaluación MCDAI al proceso IR de la DTS. Fuente: Elaboración propia.

Diseño del proceso de IR en la DTS Se definen el propósito, los roles, las responsabilidades, los artefactos de entrada y salida necesarios, así como las actividades que guían el proceso correspondiente a los requisitos específicos del MCDAI para las etapas del ciclo de vida de desarrollo de aplicaciones informáticas en la DTS, para obtener el nivel de capacidad básico. Optar inicialmente por este nivel de capacidad permitirá realizar cambios organizacionales de forma continua, como parte de la estrategia a largo plazo que ofrece IDEAL. El nivel de capacidad básico como punto de partida inicial, es necesario para obtener la cultura organizacional requerida en el proceso y que permita ganar en madurez para alcanzar el próximo nivel de capacidad: Intermedio y luego el Avanzado.

Editorial “Ediciones Futuro”152 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 12 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

Proceso Ingeniería de Requisitos El proceso Ingeniería de Requisitos tiene como propósito identificar necesidades y expectativas de las partes interesadas, transformarlas en requisitos técnicos, desarrollar los requisitos técnicos, facilitar la comunicación y establecer consenso entre los involucrados para obtener la solución informática deseada. Los requisitos técnicos son aquellos requisitos que detallan técnicamente las necesidades de las partes interesadas, sirven para traducir esas necesidades al lenguaje de los desarrolladores y c omo entrada para el desarrollo posterior del diseño, construcción y pruebas del sistema (MINCOM, 2021).

Tabla 2 - Requisitos específicos del MCDAI en el ciclo de vida de desarrollo de la DTS.

Etapas del ciclo deActividades de IR Roles/responsabilidades Artefactos de entrada/ salida vida de la DTS Iniciación IR1: Definir los requisitos de las partesRol: Cliente - Analista de Entrada: Documento Solicitud de interesadas pertinentes.requisitosinicio del proyecto. - Enunciar los procesos que se desean Entrada: Acta informatizar y resultados que se pretendenResponsabilidades: Obtener losConstitución. alcanzar.requisitos de diversas fuentes - Identificar las fuentes y proveedores parautilizando buenas habilidades de  Salida: Listado de obtener los requisitos.comunicación y técnicas derequisitos de las partes recopilación de información.interesadas.  Salida: Listado de proveedores. Planificación IR2: Analizar y especificarRol: Analista de requisitosEntrada: Listado de requisitos los requisitos.de las partes interesadas. - Analizar qué requisitos son necesarios oResponsabilidades: suficientes para el producto.Analizar los requisitos ySalida: Documento de - Definir nuevos requisitos derivados oasegurarse de que sean claros,Especificación de Requisitos implícitos.consistentes, completos,(DER): Incluir requisitos - Especificar formalmente y con suficientefactibles y comprobables.funcionales, no funcionales, detalle los RF y RNF. - Revisar viabilidadpriorización y reglas de de los requisitos (si sonvalidación (IR2, IR4). Salida: completos, factibles,Documento Tarea Técnica. realizables y verificables). IR 2.2: Priorizar requisitos. - Priorizar requisitos acordes a necesidades de los interesados, o los objetivos de la entidad.

Editorial “Ediciones Futuro”153 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 13 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

Desarrollo IR 3: Lograr el entendimiento yRol: Cliente - Analista de Entrada: Documento de compromiso de los requisitos técnicos. -requisitos - Jefe ProyectoEspecificación de Requisitos Consensuar y resolver conflictos sobre los(DER). requisitos especificados entre el cliente, elResponsabilidades: Decidir Entrada: Documento analista y el jefe de proyecto.sobre los requisitosTarea Técnica. especificados y los cambios - Controlar los cambios necesarios sique sean necesarios. Llegar a un Salida: Documento evolucionan los requisitos.acuerdo común.Tarea Técnica.  Salida: Actas de reunión.  Salida: Solicitud de Cambios: Formulario estandarizado con análisis de impacto. Pilotaje IR4: Validar requisitos con el cliente. -Rol: Cliente-Analista de Entrada: Documento de Validar que los requisitos estánrequisitosEspecificación de Requisitos correctamente descritos, que sean(DER). verificables, completos, traceables y noResponsabilidades: Validar los Entrada: Documento ambiguos.requisitos y garantizar queSolicitud de Cambios cumplan con las expectativas y necesidades de las partes Salida: Documento de interesadas.Especificación de Requisitos (DER): firmado por las partes interesadas.  Salida: Acta de Aceptación por el Cliente.

Despliegue - - -

Validación Para realizar la validación del proceso propuesto se utilizó la técnica de grupo focal constituido por seis expertos con más de cinco años de experiencia en el análisis de IR en el desar rollo de software. Los encuestados pertenecen a la DTS (4), DATYS (1), MINCOM (1), y consideran que la propuesta es correcta y está acorde para la institución. Constituyó una satisfacción la idea de “Contar con un proceso de IR definido basado en el MCDAI”.

La definición del proceso de IR de software presentado en esta investigación brinda un aporte significativo en el desarrollo del ciclo de vida del producto, y robustez al marco de trabajo de la institución al sumarle un proceso basado en el MCDAI cubano; para ello es necesario incluirlo en las normas de la DTS e institucionalizarlo en el MININT para la obtención de productos de calidad. El

Editorial “Ediciones Futuro”154 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 14 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

seguimiento correcto de las actividades propuestas, teniendo en cuenta los roles, responsabilidades, artefactos de entrada y de salida especificados contribuirá a disminuir las fallas propiciadas por los requisitos.

## Conclusiones

La definición de un proceso de Ingeniería de Requisitos (IR) en la Dirección de Tecnología y Sistemas (DTS) del Ministerio del Interior es una estrategia efectiva para mitigar las fallas relacionadas con los requisitos durante el ciclo de vida del desarrollo de soluciones informáticas. Las buenas prácticas del PB IR que ofrece el Modelo de Calidad para el Desarrollo de Aplicaciones Informáticas (MCDAI), permitió desarrollar un proceso de IR alineado con el modelo de calidad cubano MCDAI, integrándolo en el ciclo de vida de los proyectos, con roles, responsabilidades y artefactos definidos.

La aplicación del modelo IDEAL para la mejora continua de procesos, junto con la adaptación del MCDAI, proporcionó un marco sistemático para diagnosticar, diseñar e implementar el proceso de IR. La evaluación mediante el método MCDAI confirmó que la institución presenta una implementación insuficiente de los requisitos necesarios para alcanzar el nivel básico de capacidad. Este trabajo sienta las bases para futuras investigaciones en la optimización del proceso de ingeniería de requisitos hasta alcanzar el nivel de capacidad Avanzado. Además, se recomienda extender el estudio a los dos procesos bases restantes asociados a la categoría Ingeniería y profundizar en la capacitación y en la automatización de herramientas para apoyar dichas actividades.

## Referencias

García Rodríguez, A. M. (2018). Modelo de Recomendación de Escenarios al iniciar la Mejora de Procesos de Software.

Editorial “Ediciones Futuro”155 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 15 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

Barragán Martínez, X. (2022). Posmodernidad, gestión pública y tecnologías de la información y comunicación en la Administración pública de Ecuador. Estado & comunes, revista de políticas y problemas públicos, 1(14), 113-131. Trujillo Armas, Y., & García Rodríguez, A. M. (2012). Proceso para Pronosticar el Resultado de Iniciativas de Mejora de Procesos de Software (Bachelor's thesis, Universidad de las Ciencias Informáticas). Tomaselli, G. P. (2019). Evaluación de calidad de procesos ágiles en PyMEs del Noreste Argentino (Doctoral dissertation, Universidad Nacional de La Plata). PRESSMAN, R. S. (2010). Ingeniería de software enfoque practico. Pressman. PDF. Ingeniería del software, un enfoque práctico. Sommerville, I. (2011). Ingeniería del software. Pearson educación. Wiegers, K., & Beatty, J. (2013). Software requirements. Pearson Education. de Ministros, C. Decreto No. 359/2019 Sobre el Desarrollo de la Industria Cubana de Programas y Aplicaciones Informáticas (GOC-2019-548-O45). Gaceta Oficial (45). La Habana. Cuba, 777-785. NC 1400 MINCOM, 2021. NC 1400-1 Parte 1: Guía General. 2021 S.L.: SN DTS, MININT. (2011). Anexos 3 Procedimiento gestión del ciclo vida soluciones informáticas 1.2. DTS, MININT. (2015). Proceso Gestión de Proyecto. DTS, MININT. (2017). Guía para la Gestión de Proyectos Informáticos en el MININT v2. Lineamientos para el Desarrollo de Soluciones informáticas en el MININT. v2.0.2. (2019). Glinz, M. (2024). Requirements Engineering Glossary. Certified Professional for Requirements Engineering (CPRE) Studies and Exam, Version, 2.1.0, 54. Bourque, P., & Dupuis, R. Guide to the Software Engineering Body of Knowledge Version 3.0 SWEBOK. IEEE, 2014. Glinz, M., van Leonhoud, H., Staal, S., & Bühne, S. (2024). Nivel Básico. Programa de estudios. Certified Professional for Requirements Engineering. Version, 3.2.0, 51 Trujillo Casañola, Y., Febles Estrada, A., & León Rodríguez, G. (2015). Modelo para valorar las organizaciones desarrolladoras de software al iniciar la mejora de procesos. McFeeley, B. (1996). IDEALSM: A user’s guide for software process improvement. Software Engineering Institute Handbook. Carnegie Mellon University. CMU/SEI-96-HB-001.

Editorial “Ediciones Futuro”156 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 16 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

Aguileta, A. A, Ancona, G.B., Leon, E. J., & Ucan, J. P. (2015) Una Revisioón Sistemática en los Marcos de Trabajo de Desarrollo Software en las MiPyMES Productoras de Software. Recibe. Revista electrónica de Computación, Informática, Biomédica y Electrónica, 3. Bayona-Oré, S., Chamilco, J., / Perez, D. (2020) CMMI and IDEAL in software process improvement. Coque-Villegas, S., Jurado-Vite, V., Avendaño-Sudario, A., & Pizarro, G. (2017). Análisis de experiencias de mejora de procesos de desarrollo de software en PYMEs.//Analysis of experiences of improvement of software development processes in SMEs. Ciencia Unemi, 10(25), 13-24. SUAREZ, D. R., & LEON, G. C. (2019). Las PyME de desarrollo de software. Modelos de mejora de sus procesos en Latinoamérica. Revista Espacios, 40(28). Machado, E. M. M., Mexas, M. P., & de Oliveira, S. B. (2021). Proposta para a implantação do CMMI- DEV v2. 0 ML3 em empresas de pequeno e médio porte de desenvolvimento de software. Revista Ibérica de Sistemas e Tecnologias de Informação, (E41), 83-97. Ganvini Montes, G. I., Martínez Saldaña, A. D., & Soriano Toyama, F. K. (2023). Propuesta para la mejora de la calidad del software en una consultora de tecnologías de la información aplicando las áreas prácticas del estándar CMMI DEV 2.0 Nivel 2. NC 1400 MINCOM, 2021. NC 1400-3 Parte 3: Método de Evaluación. 2021 S.L.: SN Decreto No. 359/2019 Sobre el Desarrollo de la Industria Cubana de Programas y Aplicaciones Informáticas (GOC-2019-548-O45).

Conflicto de interés El autor autoriza la distribución y uso de su artículo.

Contribuciones de los autores Conceptualización: Yilian Rodríguez Grille Curación de datos: Yoandy Lazo Alvarado Análisis formal: Yilian Rodríguez Grille Adquisición de fondos: Yoandy Lazo Alvarado Investigación: Yilian Rodríguez Grille

Editorial “Ediciones Futuro”157 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu

---

<!-- Página 17 -->

Revista Cubana de Ciencias Informáticas Vol. 20, No.1, Enero-Marzo, 2026 ISSN: 2227-1899 | RNPS: 2301 http://rcci.uci.cu Pág. 142-158

Metodología: Yilian Rodríguez Grille Administración del proyecto: Yoandy Lazo Alvarado Recursos: Yoandy Lazo Alvarado Software: Yoandy Lazo Alvarado Supervisión: Yoandy Lazo Alvarado Validación: Yilian Rodríguez Grille Visualización: Yilian Rodríguez Grille Redacción – borrador original: Yilian Rodríguez Grille Redacción – revisión y edición: Yilian Rodríguez Grille

Editorial “Ediciones Futuro”158 Universidad de las Ciencias Informáticas. La Habana, Cuba rcci@uci.cu