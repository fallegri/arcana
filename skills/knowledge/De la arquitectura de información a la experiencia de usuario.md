<!-- Página 1 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1, Ene-Jun 2017 e-Ciencias de la Información

Los hipervínculos son señalados con esta clave

## De la arquitectura de información a la experiencia de usuario:

## Su interrelación en el desarrollo de software de la Universidad de

## las Ciencias Informáticas

## Liuris Rodríguez Castilla

## Delly Lien González Hernández

## Yudeisy Pérez González Publicado 01 de enero, 2017 / Informe técnico 1

Revista electrónica semestral ISSN-1659-4142

Escuela de Bibliotecología y Ciencias de la Información Universidad de Costa Rica

Visite el sitio web de e-Ciencias de la Información

ISSN 1659-4142http://revistaebci.ucr.ac.crrevista.ebci@ucr.ac.cr

---

<!-- Página 2 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

## De la arquitectura de información a la experiencia de usuario:

## Su interrelación en el desarrollo de software de la

## Universidad de las Ciencias Informáticas

From Architecture of Information to user experience: Their interaction in the development of software at the University of Computer Science

1 Liuris Rodríguez Castilla

2 Delly Lien González Hernández

3 Yudeisy Pérez González

RESUMEN

Se presenta un informe técnico sobre la aplicación de actividades y técnicas de arquitectura de información (AI) y experiencia de usuario UX) a partir de las buenas prácticas obtenidas en el proceso de desarrollo de software de la Universidad de las Ciencias Informáticas. Para ello, se identificaron las definiciones más citadas de AI y su evolución hacia el término de UX, como punto de partida para analizar la estrecha relación que existe entre estos dos conceptos durante el desarrollo de software. El trabajo permite reconocer el rol protagónico del usuario en el resultado de su interacción con el producto y con el proveedor o desarrollador. Se describen actividades y técnicas para la obtención de información y requisitos en las etapas de desarrollo del software, que tributen a una buena arquitectura de información, centrado en la experiencia del usuario.

ABSTRACT

A technical report on the application of activities and techniques of information architecture (AI) and UX user experience is presented based on the good practices obtained in the software development process of the University of Computer Science. For this, the most cited definitions of AI and their evolution towards the UX term were identified as a starting point to analyze the close relationship between these two concepts during software development. The work allows to recognize the protagonist role of the user in the result of their interaction with the product and the supplier or developer. It describes activities and techniques to obtain information and requirements in the stages of software development, which support good information architecture, focused on the user experience.

Palabras clave Keywords

Arquitectura de la información; experiencia delInformation architecture; user experience; usuario; productos interactivos; usabilidad;interactive products; usability; user-centered diseño centrado en el usuario; desarrollo dedesign; software development; University of software; Universidad de las CienciasComputer Science; Cuba. Informáticas; Cuba.

1 Universidad Tecnológica de La Habana “José Antonio Echeverría”. Centro de Referencia para la Investigación de Avanzada (CREA). Cujae, La Habana, CUBA.Orcid: orcid.org/0000-0002-9788-0686. liuris@crea.cujae.edu.cu. Autor de correspondencia 2 Universidad de las Ciencias Informáticas (UCI). Boyeros, La Habana, CUBA. delly@uci.cu 3 Universidad de las Ciencias Informáticas (UCI). Boyeros, La Habana, CUBA. Orcid: orcid.org/0000-0002-5948- 3321. yudeisy200731@gmail.com

Recibido: 20 de jun, 2016 Corregido: 21 de nov, 2016 Aprobado: 28 de nov, 2016 Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 1 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 3 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

1. Introducción

Desde mediados del siglo pasado, la interacción entre las personas y las computadoras (HCI, Human-Computer Interaction) se ha convertido en

un área de estudio centrada en el fenómeno de interacción entre usuarios y sistemas informáticos, cuyo objetivo es proporcionar bases teóricas, metodológicas y prácticas para el diseño y evaluación de productos interactivos que puedan ser usados de forma eficiente, eficaz, segura y satisfactoria. (Hassan Montero & Martín Fernández, 2005, “HCI y Usabilidad”, párr. 1)

El incremento tecnológico revolucionó las formas de desarrollar sistemas informáticos, lo que dio lugar al surgimiento de la arquitectura de información (en adelante AI). El objetivo de esta área del conocimiento dentro del desarrollo de software se centró (entre el 60 y 200) en determinar la funcionalidad del producto y especificar cómo los usuarios iban a encontrar la información a través de interfaces interactivas. Por ello, sus principales características son: la organización de la información, las formas de navegación, el sistema de etiquetado (nombres de categorías o clases generales y específicas que agrupan contenidos de información) y la funcionalidad de sistemas de búsqueda.

A partir del 2010, la tendencia en el desarrollo de software no solo debe ser fácil de usar, sino que también debe ser innovadora y enfocada a crear experiencias únicas. Las limitaciones de los enfoques tradicionales para el diseño de interfaces interactivas radican principalmente en el hecho de hacerle al usuario las interfaces fáciles de usar, obviando variables tan importantes como puede ser el comportamiento emocional.

En la actualidad, el desarrollo y uso de las tecnologías es cada vez más variado y generalizado, creciendo a un ritmo acelerado y alcanzando niveles extraordinarios. Esto ha dado lugar a la expansión de disímiles proyectos para la informatización de la sociedad, facilitando con ello la realización de las tareas cotidianas de los ciudadanos. Desde este punto de vista, el elemento principal en el desarrollo y la aceptación de las nuevas tecnologías, será la adecuación de ellas a la forma de pensar de los usuarios. Por ello, el objetivo final, que persiguen las grandes industrias dedicadas al desarrollo de software, es diseñar productos interactivos más simples, más centrados en las necesidades humanas y que ayuden a aumentar la efectividad y satisfacción de las personas (Aveleira, 2012).

Un programa interactivo es aquel que necesita un intercambio continuo con el usuario para poder ejecutarse. En este artículo, nos referimos a productos de software interactivos, los cuales facilitan la interacción social a través de la aplicación de interfaces amigables y fáciles de usar. Esta interactividad y su impacto en la sociedad se estudian a través de la disciplina interacción hombre-máquina, cuyo objetivo principal está en utilizar las computadoras para responder a las necesidades de las personas de forma interactiva. Es un término que se aplica ampliamente en las ciencias de la comunicación, en informática, en diseño multimedia y en diseño industrial (Dix, Finlay, Beale, y Abowd, 2008).

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 2 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 4 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

Esto hace que el intercambio con el usuario sea uno de los elementos más significativos de cualquier software y es básicamente la interfaz, la que proporciona este diálogo para permitir que el usuario acceda a los recursos del ordenador. La interfaz de usuario determinará en gran medida, la percepción e impresión que este posea de la aplicación. Las personas no utilizan sistemas interactivos, sino que utilizan las interfaces que les proporcionan, por tanto, una parte muy importante del éxito o fracaso de una aplicación interactiva depende de dicha interfaz (Granollers, 2004; Hassan, 2009).

Muchas instituciones y expertos que producen software conceden más importancia a las funcionalidades y muy poco en la forma en que interactúan los usuarios. Ignoran el interés por aquellos usuarios que experimentan con los procesos de interacción del software. Esto trae consigo que a menudo un producto sea poco usable a pesar de su calidad funcional debido a las dificultades en su explotación.

En la indagación de soluciones generalizables, en los últimos años, se ha difundido el concepto de experiencia de usuario (UX) o diseño de experiencias de usuario (DUX), un concepto paragua bajo el que se integran diferentes disciplinas y roles profesionales (Montero, 2009) para conseguir que los usuarios experimenten emociones al interactuar con los productos.

En el desarrollo de software, se reconoce la usabilidad como atributo de calidad en el éxito de un producto, para asegurar empíricamente los niveles de usabilidad requeridos. No obstante, son pocos los procesos y los profesionales que aplican o tienen en cuenta técnicas y procedimientos para lograr este atributo y menos los que se enfocan en DUX de sus sistemas interactivos.

La experiencia del usuario representa un cambio del propio concepto de usabilidad, pues el objetivo no se reduce a mejorar el rendimiento del usuario en la interacción entre eficacia, eficiencia y facilidad de aprendizaje, sino que trata de resolver el problema estratégico de la utilidad del producto y el problema psicológico del placer y diversión de su uso (D'Hertefelt, 2000).

Para entender mejor los aspectos de la AI y el DUX, en el proceso de desarrollo de software, se presenta este informe técnico con el objetivo de conocer estos conceptos clave y su estrecha relación con las etapas de desarrollo de un producto de software. A partir de la diversidad de autores que tratan el tema de la AI y el DXU, se identificaron de las definiciones más citadas y su relación con el término de experiencia de usuario.

Se explican también las actividades que se pueden realizar en cada fase de desarrollo del producto. Identificar la mayor cantidad de requisitos y necesidades del usuario a través de estas técnicas, hace que los usuarios se sientan involucrados directamente y obtener así más información. Estas actividades y técnicas constituyen un instrumento de trabajo para el arquitecto de información, máximo responsable de identificar y organizar la información y satisfacer las necesidades de interacción que el usuario espera encontrar en el producto.

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 3 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 5 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

2. Revisión de la Literatura

2.1. Arquitectura de información. Definiciones

El término arquitectura de la información fue acuñado por Wurman (1975) en el segundo lustro de los 70 y definido como “el estudio de la organización de la información con el objetivo de permitir al usuario encontrar su vía de navegación hacia el conocimiento y la comprensión de la información”, citado por Resmini y Rosati (2012, p. 2)

En la evolución de la definición de AI, Rosenfeld y Morville (2006, p. 26) extrapolaron el concepto al ámbito del desarrollo de aplicaciones web, enunciando la disciplina como

The art and science of shaping information products and experiences to support usability and findability [el arte y la ciencia de estructurar y clasificar sitios web e intranets con el fin de ayudar a los usuarios a encontrar y manejar la 4 información].

El concepto AI no solo abarca la organización de la información, sino también el resultado de dicha actividad. En el caso de un sitio web, como resultado de la actividad, comprende los sistemas de organización y estructuración de los contenidos, los sistemas de rotulado o etiquetado de dichos contenidos, y los sistemas de recuperación de información y navegación que provea el sitio web.

Abunda la apreciación de los usuarios de que "la interfaz es la aplicación" porque que es la parte que ven y a través de la cual interactúan, sin embargo, se debe entender que la usabilidad de la aplicación depende no sólo del diseño de la interfaz, sino también de su arquitectura, estructura y organización, o sea, del componente no visible del diseño.

Montes de Oca (2004) indica que la arquitectura de información es la disciplina encargada de disponer los elementos formales y de contenido que integran un sitio web. Comenta que el contenido informativo y el diseño deben tener la calidad requerida para, de ese modo, lograr la plena satisfacción de los usuarios. La implementación de una arquitectura de información coherente no puede lograrse sin incorporar los elementos que determinan el mejor uso del sitio. En este punto, la usabilidad adquiere relevancia particular.

Por su parte, Tramullas (2002) coincide con la definición dada por Rosenfeld y Morville (2006) considera que la arquitectura de la información no es el único componente del diseño de espacios de información digital. Debe trabajar también con técnicas de visualización de información, de evaluación, de usabilidad, de interacción hombre-máquina y de programación avanzada, todos ellos de manera integrada y altamente interrelacionados bajo el término “diseño de información”. Además, plantea que resulta casi imposible separar los aspectos de diseño, arquitectura y usabilidad en un sistema de documentos digitales.

4 Traducción realizada por las autoras.

Volumen 4, número 2, Artículo 1 4 Julio - Diciembre, 2014 Publicado 1 de julio, 2014

---

<!-- Página 6 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

En aplicaciones de software, Folmer y Bosch (2004) estudian este hecho y concluyen que el diseño a nivel de arquitectura tiene una gran influencia en la usabilidad del sistema. Desde la misma línea de investigación práctica trabajan Rodrigues de Albuquerque y Lima-Marques (2011), Paz, Hernández, y Manso (2015) y Santana (2011), quienes coinciden que el diseño de interfaz gráfica de un producto es un elemento de importancia para los usuarios en su primera interacción con alguna aplicación informática, pero también su usabilidad depende de la estructuración y organización del contenido mostrado. Concuerdan, además, en que la visualidad es una de las características fundamentales para los resultados de la AI, por lo tanto, están estrechamente complementadas. En muchos equipos de desarrollo de software, la realización de las actividades de un diseñador comienza básicamente después de haber sido aprobada la arquitectura de información.

Para Toub (2000, p. 2), la arquitectura de la información también es definida como

is the art and science of structuring and organizing information environments to help people effectively fulfill their information needs [el arte y la ciencia de organizar espacios de información con el fin de ayudar a los usuarios a satisfacer 5 sus necesidades de información].

En la AI, hay dos aspectos importantes a tener en cuenta, primero, la recuperación de la información, cuyo objetivo principal es facilitar al usuario llegar el contenido que indica las categorías estructuradas. Esto se logra, por una parte, posibilitando que el usuario pueda encontrar información, diseño y definición de índices, clasificaciones, taxonomías y sistemas de recuperación de información o sistemas de búsqueda en el sitio web. Por otra parte, posibilitando que cada elemento de información pueda ser encontrado (descripción a través de metadatos y optimización del sitio para buscadores). Este segundo caso se conoce como "findability", encontrabilidad o visibilidad. El segundo aspecto es el diseño a nivel conceptual, las técnicas propias de la AI, dentro del ciclo de vida del desarrollo de un sitio web, se ubican en fases de diseño conceptual. Las fases de diseño visual están, se caracterizan por técnicas de Ingeniería de la Usabilidad, Diseño de Interfaces y Diseño de Información.

Resaltando también la importancia del arquitecto de información, Montes de Oca (2004) refiere que un arquitecto de información no necesariamente tiene que ser un especialista en ciencias de la información o en otras disciplinas relacionadas con el desarrollo de software. Sin embargo, la tarea del arquitecto de información incluye también la revisión constante de los flujos vinculados al proceso de trabajo del equipo de desarrollo, así como la coordinación entre las distintas disciplinas que integran el equipo (analistas de sistemas, diseñadores, comunicadores, programadores, entre otros).

En las últimas dos décadas, con la llegada de internet, se ha extendido rápidamente el uso de la AI, que se considera una materia multidisciplinaria y relativamente joven. Asimismo, ha existido una explosión de arquitectos de información que en su trabajo mezclan tres grandes campos: tecnología, diseño gráfico y periodismo/redacción. No obstante, el arquitecto de información, además, debe tener conocimientos básicos de Ciencias de la Información, Ciencias de la Comunicación, Ingeniería en usabilidad, Marketing, Informática, Psicología y Sociología.

5 Traducción realizada por las autoras.

Volumen 4, número 2, Artículo 1 5 Julio - Diciembre, 2014 Publicado 1 de julio, 2014

---

<!-- Página 7 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

Tras el aporte de Wurman (1975), otros tomaron sus definiciones y comenzaron a ampliar el horizonte de la AI, haciendo más certera la definición sobre su ámbito de acción. Morville (2004) asume las ideas de este autor en sus definiciones y plantea que la AI se define a través de tres frases:

 La combinación de esquemas de organización, etiquetado y navegación, dentro de un sistema de información.

 El diseño estructural de un espacio de información para facilitar la terminación de tareas y el acceso intuitivo al contenido.

 El arte y la ciencia de estructurar y clasificar sitios web e intranets, para ayudar a las personas a encontrar y administrar información.

A partir de esta definición, Wurman (1975) y Morville (2004) establecen las tareas concretas que realiza un arquitecto de información:

 Aclarar la misión y la visión del sitio, haciendo un balance entre las necesidades de la organización que lo impulsa y las necesidades de sus audiencias.

 Determinar qué contenidos y funcionalidades deberá contener el sitio.

 Especificar cómo buscarán información en el sitio los usuarios, mediante la definición de sus sistemas de organización, navegación, etiquetado y búsqueda.

 Proyectar cómo se acomodará el sitio al cambio y el crecimiento a lo largo del tiempo.

Tradicionalmente, en el desarrollo de productos de software se aplicaba la arquitectura de información para organizar contenidos, encontrar y administrar información que satisface las necesidades básicas de conocimiento de los usuarios. El avance acelerado de las tecnologías ha propiciado la evolución este concepto a través del desarrollo de productos interactivos entre el hombre y las computadoras. Esta interactividad permite identificar el comportamiento racional del usuario en sus habilidades y conocimientos, pero aún no se consideraba con amplitud su comportamiento emocional.

Desde un enfoque social, el comportamiento emocional del usuario es un elemento clave en la aceptación y uso de los productos. Ya no solamente las aplicaciones informáticas requieren de organización de los contenidos y satisfacen demandas cognoscitivas, sino que también influyen en la formación del usuario, su experticia para asimilar y trabajar con las tecnologías de la información, sus gustos, preferencias, educación, ambiente o entorno social y laboral en el que se desarrolla, valores, sentimientos, idiosincrasia, cultura, entre otros. Este nuevo enfoque del desarrollo de productos interactivos, principalmente utilizado para encontrar soluciones de diseño más integradoras e inclusivas, en el entorno profesional del desarrollo web, se conoce como la experiencia del usuario (en adelante UX).

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 6 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 8 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

2.2. Experincia de usuario. Génesis y definiciones

La UX es un concepto que se enfoca directamente en las emociones que experimente el usuario al interactuar con los productos de software. Al respecto, Hassan Montero & Martín Fernández (2005, p. 6) explican que el comportamiento emocional del usuario es resultado de tres factores diferentes: “las emociones evocadas por el producto durante la interacción, el estado de humor del usuario y los sentimientos pre-asociados por el usuario al producto”. En tal sentido, es necesario reconocer que el enfoque tradicional para el diseño de productos interactivos en la web tiene limitaciones porque su visión del fenómeno es sesgada para el lado de los medios, las herramientas y las tecnologías empleadas.

Además, Hassan Montero & Martín Fernández (2005) continúan diciendo que uno de los aportes de la UX es su función de concepto para integrar las diferentes disciplinas y roles profesionales implicados en el diseño de productos interactivos como ingeniería de la usabilidad, arquitectura de la información, diseño gráfico, diseño de interacción, diseño de información, entre otros.

La UX representa un cambio del propio concepto de usabilidad, pues el objetivo no se reduce a mejorar el rendimiento del usuario en la interacción entre eficacia, eficiencia y facilidad de aprendizaje, sino que trata de resolver el problema estratégico de la utilidad del producto y el problema psicológico del placer y diversión de su uso (D'Hertefelt, 2000).

La génesis de este concepto se halla en el campo del Marketing, así lo considera Kankainen (2002). Esto se debe a su vínculo con el concepto de experiencia de marca “pretensión de establecer una relación familiar y consistente entre consumidor y marca” (Hassan Montero y Martín Fernández, “Origen”, párr. 4). En el contexto del marketing, un enfoque centrado en la UX conllevaría no sólo analizar los factores que influyen en la adquisición o elección de un determinado producto, sino también analizar cómo los consumidores usan el producto y la experiencia resultante de su uso. Por ser un concepto de reciente aplicación en el campo del diseño, es necesario apreciar diferentes definiciones y modelos propuestos, que permitan un acercamiento a lo que se entiende por la UX. Integrado desde tres niveles, Dillon (2001) define la UX: acción, qué hace el usuario; resultado, qué obtiene el usuario; y emoción, qué siente el usuario. Este planteamiento descompone el fenómeno causante (interacción) en dos niveles, acción y resultado; y solo le interesa el comportamiento emocional del usuario en la experiencia resultante.

Arhippainen y Tähti (2003) de la Linköping University en Suecia definen la UX como la experiencia que obtiene el usuario cuando interactúa con un producto en condiciones particulares. También destacan las emociones y expectativas del usuario y su relación con otras personas y el contexto de uso.

Por su parte, FatDUX Group (2013) define la experiencia del usuario como la suma de una serie de interacciones. Es un término para el nivel de satisfacción total de usuarios cuando utiliza tu producto o sistema. Representa la percepción dejada en la mente de alguien después de una serie interacción entre la gente, dispositivos y eventos- o una combinación de interacciones.

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 7 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 9 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

Desde una visión emocional, Clarenc (2011) también lo enfoca planteando que la experiencia del usuario abarca el conjunto de factores y elementos que determinan la interacción satisfactoria del usuario con un entorno o dispositivo y son capaces de generar en él un conjunto de emociones positivas sobre el sitio y su uso.

Para Hassan Montero & Martín Fernández (2005, p. 23), la UX “es la sensación, sentimiento, respuesta emocional, valoración y satisfacción del usuario respecto a un producto, resultado del fenómeno de interacción con el producto y la interacción con su proveedor”. Desde un enfoque “paragua”, Hassan (2009) describe la UX, bajo el que se integran diferentes disciplinas y roles profesionales implicados en el diseño de productos interactivos, ingeniería de la usabilidad, arquitectura de la información, diseño gráfico, diseño de interacción, diseño de información, etc.

Nielsen Norman Group (2003, p.1-2) define la UX como: “Concepto integrador de todos los aspectos de la interacción entre el usuario final y la compañía, sus servicios y productos". En ella sobresale el análisis de la experiencia de interacción no solo como fenómeno interactivo entre usuario y producto, sino también entre usuario y proveedor.

Asimismo, el primer requisito para una UX ejemplar es encontrar las necesidades exactas del cliente. Después vienen la sencillez y la elegancia que generan los productos fáciles de usar. La verdadera experiencia del usuario va mucho más allá de dar a los clientes lo que ellos dicen que quieren o proporcionar una lista de verificación. A fin de alcanzar la UX de alta calidad en la oferta de una empresa, debe haber una fusión sin fisuras de los servicios de múltiples disciplinas, incluyendo la ingeniería, el marketing, el diseño gráfico e industrial y el diseño de interfaz (Nielsen Norman Group, 2003).

Morville (2004) presenta “las facetas de la UX”, las cuales son representadas con un hexágono cuyo conjunto da origen a un diagrama al que popularmente se le ha llamado “El panel de Morville”. La conclusión más importante de dicho planteamiento es la UX vista como la integración de varias disciplinas y cualidades. La UX está compuesta de seis elementos:

A. Útil: se puede entender como la utilidad que tiene el sitio para el usuario, la capacidad de responder a sus necesidades. B. Usable: relacionada con la facilidad de uso, depende estrechamente de la aplicación de los conceptos de la ciencia de la interacción persona ordenador. C. Deseable: relacionada estrechamente con el diseño emocional. Un software es deseable como producto de la eficiencia en armonía con la imagen, lo gráfico y el manejo de marca. D. Encontrable: se refiere a la capacidad de un sitio de ser navegable. Los usuarios deben poder encontrar los elementos que responderán a su necesidad. E. Accesible: para un sitio será importante tratar de garantizar el acceso a la mayor cantidad de personas en la mayor cantidad de contextos. F. Creíble: indica la necesidad de mostrar los elementos que expongan un portal creíble y confiable ante los usuarios.

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 8 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 10 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

Garrett (2011) divide las decisiones en cuatro planos, a tomar en el DX. Además, se usa estrategias, que consiste en la etapa en la que se especifica el fundamento del proyecto. Se trata de establecer claramente qué esperan obtener del sitio sus gestores y sus usuarios.

 Alcance: comprende las funciones y características del sitio.  Estructura: se trata de los llamados blueprints o los planos del sitio que definen la relación entre las diversas páginas web, las estructuras de navegación, los y sus flujos,etc.  Esqueleto: son los denominados wireframes o esquemas donde se ubican los diversos elementos que componen la interfaz y la relación entre estos: menús, botones, imágenes, párrafos, etc.  Superficie: es el diseño visual de los elementos que comprenden las páginas del sitio.

Aveleira (2012) coincide con el enfoque que plantean Hassan (2009) y Morville (2004) y considera que el diseño de UX va más allá de perseguir la facilidad de uso en los productos para lograr propuestas innovadoras y enfocadas a crear experiencias únicas. No constituye una disciplina cerrada y definida, sino un enfoque de trabajo abierto y multidisciplinar. Las proyecciones deben enfocarse para que los usuarios experimenten placer al interactuar con los sistemas, enmarcarse en que ya los criterios funcionales (que son obvios) no bastan, por lo que debe lograrse una dimensión emocional del uso y el disfrute de una aplicación interactiva, por medio de un enfoque sobre el diseño emocional.

2.3 Análisis conceptual entre Arquitectura de Información y Experiencia de Usuario

A partir de las definiciones antes expuestas de estos dos términos, se realizó un análisis de significado y sintaxis en los contenidos de las definiciones descritas. Para ambos análisis, se introdujeron en un gestor bibliográfico (endnote) todas las definiciones en el campo: abstract. Luego, se extrajeron las palabras clave, que encierren un significado lógico, descritas en el contenido de los conceptos en el campo: keywords. Posteriormente, con la propia herramienta, se realiza un filtro para contar atributos, que son las características descritas en las definiciones a través de las palabras clave), con la opción subjet bibliographic por el indicador keywords. El sistema devuelve aquellas palabras encontradas y escritas de igual forma-sintaxis y la cantidad de veces que coinciden. Posteriormente, se realiza un análisis en el contenido de las definiciones por el significado que encierran, buscando aquellos términos que expliquen una misma idea- semántica.

Para las definiciones correspondientes al concepto de AI, se destacan como términos principales: navegación web, estructura de información, organización de información y clasificación de información, como puede apreciarse en la figura 1. Todos los autores coinciden en que la arquitectura de información está más enfocada a la organización de contenidos y clasificación de información para productos con interfaz web, buscando la interactividad del usuario. Utiliza también actividades/técnicas enfocadas al usuario para satisfacer sus necesidades de información y organizar los contenidos en base a ello.

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 9 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 11 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

Entre los atributos con coincidencia semántica sobresalen: estructura de información, estructura de contenidos; manejar información, gestionar información, administrar información; diseño de espacios, organización de espacios, diseño de información; visualización, calidad visual, visibilidad; taxonomías, índices, metadatos.

FIGURA 1 Número de coincidencia de atributos en los conceptos de arquitectura de información

Estructura de información, estructura de contenidos

Navegación web, encontrar información

Productos web

Organización de información

Clasificación de información, etiquetas

Diseño de espacios, organización de espacios, diseño de información

Usabilidad

Manejar información, gestionar información, administrar información

Atributos Taxonomías, índices, metadatos

Visualización, calidad visual, visibilidad

Recuperación de información

Ciencia

Arte

Software

Satisfacción de necesidades

Interacción persona-ordenador

Compresión de información

0 2 4 6 8 Número

Fuente: Elaboración propia.

Por su parte, en las definiciones de UX, los términos que más coinciden en estructura sintáctica son: placer, interacción, usabilidad, software, usuario. Se relacionan, además, otros atributos que describen con la organización de los contenidos de información, la satisfacción, emociones, entre otros, como se muestra en la figura 2. Con ideas de significados similares las palabras: placer, agradable, felicidad, deseable, sensaciones, sentimiento; interacción, interactividad, diseño de interacción; estructura, diseño de información, esqueleto, superficie, arquitectura de información, diseño gráfico; emoción, comportamiento emocional, respuesta emocional.

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 10 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 12 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

FIGURA 2 Número de coincidencia de atributos en los conceptos de experiencia de usuario

10Placer, agradable, felicidad, deseable, sensaciones, sentimiento

8Interacción, interactividad, diseño de interacción

7Usuarios

7Usabilidad

6Productos de sofware, servicios

5SatisfacciónAtributos

5Emoción, comportamiento emocional, respuesta emocional

Estructura, diseño de información, esqueleto, superficie, 5 arquitectura de información, diseño gráfico

4Productos web, utilidad del producto

2Valoraciones

1Eficacia

0 5 10 15 Número Fuente: Elaboración propia.

2.4 Usabilidad

Entre los autores más reconocidos y citados en este tema se encuentran Nielsen (2001) y Krug (2006), quienes abordan la definición de usabilidad en estrecho vínculo con la AI. De ahí que consideren que la usabilidad aparece como una conclusión natural del proceso de arquitectura de información. Estas ideas se sustentan en que el usuario de un sitio web no quiere pensar en cómo emplear una interface, sino solo utilizarla para los fines que lo llevaron a visitarlo. Por ello, se debe generar todo lo que se presenta en pantalla, con esa idea en mente.

Nielsen (1999) plantea que la usabilidad es un atributo de calidad que determina cuán fáciles son de usar las interfaces, mientras que Krug (2013) indica que las pantallas deben evitar hacer pensar al usuario. Esto significa que tanto como sea humanamente posible, cuando mire una página web debería ser auto evidente, obvia y auto explicativa. Debería ser posible “entenderla”, de qué se trata y cómo se usa, sin hacer esfuerzos en pensar al respecto.

Se reconoce, entonces, la calidad de uso de un producto interactivo como usabilidad. El término es realmente un anglicismo que significa facilidad de uso y se refiere al grado de eficacia, eficiencia y satisfacción con la que usuarios específicos pueden lograr objetivos específicos, en contextos de uso específicos (International Standard Organization, 1994).

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 11 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 13 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

3. Análisis de la Literatura

Experiencia del usuario y arquitectura de información en el proceso de desarrollo 3.1 de software

A partir de la revisión bibliográfica realizada en los acápites anteriores, en este artículo se coincide con la especialista Aveleira (2012), seguidora de las ideas de Montero (2009), quienes afirman que la experiencia de usuario es un término sombrilla bajo el que se incluye la arquitectura de información (ver figura 3). Está estrechamente vinculada con diferentes disciplinas en las que se desarrollan diversos roles profesionales (arquitectos de información, diseñadores, analistas de sistemas, informáticos, comunicadores, psicólogos, entre otros).

El punto común en ambos conceptos es el usuario como el elemento más importante durante el desarrollo de software. Los dos términos tienen como objetivo fundamental satisfacer las necesidades del usuario, uno de forma organizada a través de los contenidos de información y el otro a partir de las emociones que estos experimentan al interactuar con el software. Integran a su vez, otros componentes esenciales en lograr la realización final del software y la satisfacción del usuario al interactuar con estos, como se muestran en la figura 3.

FIGURA 3 Interrelación entre arquitectura de información y experiencia de usuario

EXPERIENCIA DE USUARIO Necesidades del usuario Diseño de interacción Especificaciones funcionales Dimensión emocional

ARQUITECTURA DE INFORMACIÓN

Objetivos del sitio Organización de contenidos Diseño de navegación Facilidad de uso

USUARIO

Fuente: Elaboración propia. Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 12 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 14 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

Además, se concuerda con los criterios de Nielsen Norman Group (2003), cuando plantean que para asegurar empíricamente que un software cumpla con los niveles de usabilidad requeridos, el diseñador necesita de una metodología, de técnicas y procedimientos ideados para tal fin. En este sentido, existen propuestas que guían este proceso como marco metodológico conocido como diseño centrado en el usuario (User-Centered Design), adaptándolo a las características propias del desarrollo de software.

El diseño centrado en el usuario se caracteriza por asumir que todo el proceso de desarrollo de un producto de software esté dirigido al usuario, a sus necesidades, características y objetivos. Centrar el diseño en sus usuarios, contrario a centrarlo en las posibilidades tecnológicas o en los propios diseñadores, implica involucrarlos desde el comienzo en el proceso de desarrollo del producto; conocer cómo son, qué necesitan, para qué los usan; probar el software con los usuarios finales; investigar cómo reaccionan ante el diseño, cómo es su experiencia de uso; e innovar siempre con el propósito de mejorar la experiencia del usuario.

No obstante, la integración del usuario, como elemento principal en el desarrollo de un software, va más allá de satisfacer sus emociones a través de la interpretación de otros, implica también permitir que él mismo sea quien manifieste, directamente en la interacción con el producto, sus gustos y utilidad. El diseño centrado en el usuario también incluye que él mismo sea co- diseñador, esto se manifiesta desde la identificación de sus necesidades hasta la implementación del producto.

Al realizar pruebas en los prototipos no funcionales (maquetas de arquitectura) y prototipos funcionales (diseñados), utilizando diversas técnicas; el arquitecto obtiene nuevos elemento visuales e interactivos que manifiesta el usuario durante los test. Estos son aprovechados para mejorar el diseño interactivo y visual, que se manifiesta en un mejor funcionamiento del producto cuando se implemente. Por ello, el propio usuario antes de tener el producto concluido actúa como co-diseñador en el desarrollo de software.

Estas características corresponden exactamente con el enfoque de este trabajo, el cual defiende la participación del usuario con su experiencia desde el inicio y hasta el fin del desarrollo de aplicaciones de interacción hombre-máquina. Si se toma en cuenta el tipo de audiencia, comunidad, grupo de personas, usuarios en cuestión, al que va dirigido un producto de software, así como su experiencia para manejar una aplicación informática; la AI tendrá la calidad esperada y los niveles de usabilidad requeridos.

El diseño centrado en el usuario durante la producción de software tiene una vital importancia, pues sus prácticas implican optimizar la facilidad de uso de los procesos, romper las barreras tecnológicas para personas discapacitadas, organizar la información de acuerdo con el modelo mental del público meta, evaluar la aplicación con usuarios reales y resolver errores de usabilidad. Además, colaborar en el diseño de la interfaz de las aplicaciones, comprobar en qué medida este diseño se adapta a los potenciales usuarios, comprobar el funcionamiento en diferentes plataformas, así como realizar diferentes test que contribuyan a validar el diseño de esta experiencia, contribuye a crear un estado emocional placentero en la interacción con los sistemas.

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 13 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 15 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

Actividades y técnicas de AI y DXU en el desarrollo de software. 4. Experiencias prácticas en la Universidad de las Ciencias Informáticas

La industria cubana del software no incorpora en su totalidad el diseño de experiencia de usuario al proceso de desarrollo de software, aunque sí se destacan algunas universidades que vinculan la investigación con la producción y aplican diversas técnicas reflejadas en sus investigaciones y productos informáticos, dentro de las que pueden mencionarse: la Universidad Central de las Villas (UCLV) (Paz, Hernández, y Manso, 2015; Paz y Cuellar, 2016), la Universidad de Oriente (UO) (Santana, 2011) y la Universidad de las Ciencias Informáticas (UCI) (García, 2010; Ramírez, 2009; Hernández, 2009; Moyares y Bretones, 2010; Sablón y Hernández, 2013; Arencibia et al., 2012; Castilla, Aveleira, González, y Fernández, 2014; Aveleira y Silva, 2011; Paz y Cuellar, 2016).

Sobre la UCI es importante resaltar que es una de las que desarrollan software a mayor escala en el país. Aunque aún son insuficientes los roles del arquitecto de información en los equipos de proyectos, sí se realizan actividades prácticas que se encarguen del diseño de experiencia de usuario en el desarrollo de software. Estas tareas, en la mayoría de los proyectos, se delegan empíricamente en desarrolladores y analistas, a quienes en muchas ocasiones se les dificulta comprender los beneficios potenciales de trabajar con un enfoque centrado en el DUX. Por ello, para contribuir a la mejora de usabilidad de los productos en esta institución, se analizaron las mejores prácticas desarrolladas con la finalidad de generalizar las experiencias en todos los equipos de proyectos de la Universidad (tabla 1).

Para el desarrollo de un software, es ideal la propuesta de arquitectura basada en la experiencia del usuario, pues esto le permite satisfacer sus necesidades de información al interactuar con el producto y garantiza una parte importante del éxito de su uso. La fabricación de un producto de software transita por varias fases, según la metodología de desarrollo que se utilice (Pressman, 2010). Estas etapas tienen incorporadas la AI dentro del diseño de la aplicación. Para hacer una AI con calidad, se aplican técnicas en las etapas requeridas del proceso de producción. Estas técnicas se adaptan a cada proyecto específico, según sea el producto que se desarrolla.

De manera general, el ciclo de vida de un software transita por cuatro fases fundamentales: modelo de negocio, requisitos, análisis y diseño, implementación y prueba. Visto desde el punto de vista gerencial, el arquitecto de información organiza sus actividades enfocadas a cada etapa. Los requisitos corresponden con las actividades de planificación, en el diseño con las actividades de organización, la implementación con la ejecución, y en la de prueba con el control del producto. Para ambos enfoques, el grueso de actividades relacionadas con la arquitectura de información se concentra en la etapa de requerimientos, diseño y parte de las pruebas del producto. Esto se puede visualizar mejor en los gráficos de los autores Revang (2007) y Garret (2000), quienes integran en sus modelos la arquitectura de información en la experiencia de usuario.

Cada etapa en la AI lleva implícito un grupo de tareas que buscan un acercamiento más real con las expectativas del usuario. Estas tareas están acompañadas de técnicas que permiten obtener mayor cantidad de información y realizar soluciones informáticas con mayor calidad y uso. Estas

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 14 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 16 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

técnicas pueden aplicarse de forma combinada en distintos momentos del proceso de desarrollo de software, según se requiera (Ronda, 2011).

El arquitecto de información tiene una alta participación en el proceso de desarrollo de un software, pues está presente en un 75 % de su ejecución (planificación, organización y control). Esto se manifiesta en las actividades y tareas que debe realizar durante el ciclo de desarrollo del software. Sin embargo, es al inicio del proyecto donde radican las mayores actividades por realizar para la obtención de información. El arquitecto de información siempre debe tener en cuenta aspectos como:

 Las metas y necesidades de los usuarios  Las metas del negocio u organización  Limitaciones tecnológicas  Limitaciones del contenido  Limitaciones del proyecto

Desarrollar un buen diseño del software centrado en la experiencia del usuario trae grandes beneficios para todos los involucrados en el proceso: el usuario al que va destinado y los miembros del equipo de trabajo. Al usuario le permite entender y moverse por grandes cantidades de información, buscar y encontrar la información que necesitan de manera simple; no tener que pensar y experimentar emociones al interactuar con el producto.

A los creadores (que incluye a todo el equipo de desarrollo-jefes del proyecto, analistas, arquitectos de información, programadores, diseñadores, entre otros), les permite generar estructuras que soporten el cambio y el crecimiento en el tiempo del producto. Asegurar la consistencia y localización de la información. Crear sistemas de navegación intuitivos y garantizar un amplio por ciento en la usabilidad del software.

En nuestra universidad-UCI, se realizan muchas de estas actividades y se aplican diversas técnicas (ver tabla 1) para el desarrollo de productos de software agrupados en diversas categorías: educativos, médicos, ingenieriles, entre otros. A continuación, se expone una relación entre las etapas del desarrollo de software y las actividades-técnicas de arquitectura de información y la experiencia de usuario, que se podían aplicar en los proyectos de la institución, a partir de las particularidades tecnológicas y metodologías de desarrollo de software que se utilizaban (ver tabla 1).

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 15 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 17 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

TABLA 1 Relación de etapas, actividades y técnicas aplicadas durante el desarrollo de software desde la arquitectura de información y la experiencia de usuario

Etapas Actividades Técnicas Investigación:Análisis de lasTormenta de ideas (brainstorming, focusgroup), crítica de Se obtiene todanecesidades generales:diseño, diseño participativo, tormenta de necesidades, la informacióntemática del producto,escenarios, benchmarking (comparación, análisis de posible delobjetivos, intensiónhomólogos), análisis de frecuencia de texto, diseño proyecto y delcomunicativa del producto,participativo (reunión entre productores y una muestra de producto adefinición general de losusuarios potenciales con para que formen parte del proyecto diseñarusuarios /contextoque se desea desarrollar). Algunos de los componentes /contenido, caracterizaciónrecomendados en este tipo de intercambios son: una mesa (tipología, roles), perfil deredonda (buscando correspondencia y equivalencia entre los usuarios, necesidades (departicipantes), una pizarra, proyector o pancarta (para hacer información, formación),apuntes sobre comentarios y observaciones de interés escenarios, tareas degeneral). Se recomienda que no sobrepasen de 10 usuarios.participantes (Ronda, 2007 ).

Estudio del contexto:Escenarios: la finalidad de este método es identificar el orden características del contextode los pasos que siguen los usuarios al observar el diseño. de uso (cultural, político,Para esto, se realizan ejercicios de completamiento de datos e económico, social yinformación. tecnológico), matriz DAFO, banco de problemas,Análisis de homólogos: evaluación de otros softwares flujograma de procesos,equivalentes al que se pretende desarrollar, utilizando para su escenarios, estudio deevaluación indicadores de contenido, diseño o programación. mercado, productos similares, etc. Para elAnálisis de la competencia permite analizar el medio para el rediseño de un producto seque se diseña y la existencia de productos equivalentes (parte realiza el análisis de usodesde el análisis de homólogos). Se realiza para comprobar (logs) y se evalúa alque no existan otros productos similares que puedan satisfacer producto anterior.las necesidades de información que van a satisfacer el nuevo que se propone diseñar. Estudio de los contenidos:Análisis de frecuencia de texto: se le piden los artículos lista de los componentesgenerados por un grupo de usuarios y se les aplica análisis de que serán incluidos en elfrecuencia con el objetivo de obtener los términos que más se producto, clasificación derepiten. cada uno y descripción conceptual.

Organización:Representación de lasTarjetas (cardsorting), agrupación-secuencia-posición de Procesoestructuras posibles de losbloques. Tabulación de contenidos. Diagramas de afinidad. cognitivo decontenidos, enValidación de términos. procesar toda lacorrespondencia con lasCon el cardsorting, se le entregan un grupo de tarjetas con informaciónnecesidades de usuarios ynombres escritos y se les pide que las organicen. Se observa para convertirlasu contexto; definición deel desempeño de los usuarios y se obtienen los resultados en un productolas formas de jerarquizarcualitativos, que se procesan en un software y se obtienen los los contenidos; hacerresultados cuantitativos. corresponder las estructuras planteadas conPuede aplicarse de dos formas (Ronda, 2013): las necesidades tanto de emisores (clientes) comoAbierta: se le muestra al usuario, un mapa de taxonomías o de receptores (usuarios).nombres de etiquetas que representan los contenidos del Continúa…

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 16 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 18 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

Etapas Actividades Técnicas producto o software, y este agrupa clases de forma espontánea en la cantidad de grupos que crea asociados pos los criterios que haya analizado.

Cerrada: se definen previamente las etiquetas de los contenidos del software clasificadas en categorías generales y específicas y el usuario solo debe ubicar cada clase en el conjunto que crea pertenezca y ordenar en una secuencia lógica las clases generales. Los usuarios pueden a partir de esto establecer nuevas clases, secuencias o bloques.

Diseño:Definición de la estructuraDiagramación en papel (paper prototype). Diagramación de Prototipos no(diagramas de clases yorganización del producto (blueprint), de funcionamiento (flow), funcionalestaxonomías, presentadosy de presentación (wireframe). Etiquetado. Prototipado digital en papel o a través de herramientas automatizados para representar el funcionamiento secuencial de los componentes del producto de software.

Representación visual (maquetas) de las pantallas a través de diagrama de presentación- wireframe; etiquetas- descripción de los servicios web (interactivos) que ofrecerá el producto digital; creación de modelos de bajo y alto nivel.

Prueba:Pruebas de prototipos;Evaluación de diseño visual (con usuarios y expertos) acorde a Continúa… Comprobaciónrevisión de diagramas;los prototipos no funcionales realizados. del diseño delrevisión funcional del productoproducto desarrollado.Pruebas de funcionamiento y navegación con usuarios reales propuestoa quien va destinado el producto. Pruebas de funcionamiento con expertos. Sorteo de tarjetas aplicado a una nueva muestra de usuarios.

Fuente: Elaborado a partir de las buenas prácticas obtenidas en los Grupos de Producción de Software de la Universidad de las Ciencias Informáticas, 2015.

Según Ronda (2013), también se pueden aplicar otras técnicas generales en cualquier etapa como: estudio del entorno cultural en el que se desarrollan los usuarios (lengua, país, tradiciones, nivel de enseñanza, nivel cultural, etc.), estudio del lenguaje que utilizan los usuarios (registro vulgar, científico, coloquial, etc.), compendio de documentos que utilizan, recopilación de palabras o vocablos de uso a partir de los documentos y los estudios de lenguaje, y análisis de frecuencia de términos dentro de la documentación (método cuantitativo).

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 17 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 19 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

5. Conclusiones

 La arquitectura de información y la experiencia de usuario son dos conceptos interrelacionados entre sí que, al aplicarlo de forma integrada en el desarrollo de software, garantizan un alto por ciento en la usabilidad del producto.

 Se considera al usuario como el elemento fundamental de éxito en el desarrollo de un software. Solo el uso eficiente, eficaz y satisfactorio del sistema, justificará la inversión en dinero, tiempo y personal de desarrollo.

 La AI y la UX se pueden aplicar en el desarrollo de cualquier producto de software: sitio web, multimedia, sistemas de información, sistema de gestión, buscadores u otros.

 El DUX está encaminado a crear interfaces directas, simples y fáciles de usar, además, innovadoras y placenteras, imponiéndole al desarrollo de software un nuevo enfoque que implique insertar sus prácticas para mejorar los productos.

 La participación activa de los usuarios, en un sistema bien diseñado, los hará sentirse hábiles, con dominio y lo entenderán de manera natural, logrando cumplir las metas que los llevaron a usarlo.

 El arquitecto de información juega un papel fundamental en el proceso de desarrollo de software, pues evita que se cometan errores de estructura, nomenclatura, navegación.

 El uso de técnicas para la obtención de información en cada etapa del proceso, ayuda a definir mejor un diseño de arquitectura pensada en la experiencia del usuario, permite relacionar las tareas técnicas de la ingeniería de software con las características creativas del DUX.

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 18 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 20 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

6. Referencias

Arencibia, J., Toll, Y., Soto, J., Tamayo, D., Moyares, Y., y Ril, Y. (2012). Guía práctica de Arquitectura de Información para aplicaciones multimedia educativas. Recuperado de http://www.nosolousabilidad.com/articulos/guia_ai.htm

Arhippainen, L., y Tähti, M. (2003). Empirical Evaluation of User Experience in Two Adaptive Mobile Application Prototypes. Ponencia presentada en el 2nd International Conference on Mobile and Ubiquitous Multimedia, Norrköping, Suecia.

Aveleira, Y. (2012). Marco de trabajo para diseñar la experiencia de usuario en el desarrollo de software (tesis de maestría inédita). Universidad de las Ciencias Informáticas, La Habana, Cuba.

Aveleira, Y., y Silva, D. (2011). Laboratorio para diseño de experiencia de usuario. Revista Cubana de Ciencias Informáticas-RCCI, 5(3). Recuperado de http://rcci.uci.cu/?journal=rcci&page=article&op=view&path%5B%5D=153

Castilla, L., Aveleira, Y., González, D., y Fernández, J. (2014). Diseño Centrado en el Usuario: estudio de caso de un portal bibliotecario. Recuperado de http://www.nosolousabilidad.com/articulos/dcu_biblioteca.htm

Clarenc, C. A. (2011). Nociones de Cibercultura y Periodismo. Recuperado de http://www.humanodigital.com.ar/Publicaciones/Nociones-de-Cibercultura-y- Periodismo.pdf

D'Hertefelt, S. (2000). Emerging and future usability challenges: designing user experiences and user communities. Recuperado de http://users.skynet.be/fa250900/future/vision20000202shd.htm

Dillon, A. (2001). Beyond Usability: Process, Outcome and Affect in human computer interactions. Recuperado de http://tecfa.unige.ch/tecfa/teaching/Ergo/textes/Periode3/Beyond_Usability.pdf

a Dix, A., Finlay, H., Abowd, G. D., y Beale, R. (2004). Human-computer intereaction (3ed.). Harlow, Inglaterra: Pearson. Recuperado de http://fit.mta.edu.vn/files/DanhSach/__Human_computer_interaction.pdf

FatDUX Group. (2013). Qué es UX? Recuperado de http://www.fatdux.com/es/what/what-is- ux

Folmer, E. y Bosch, J. (2004). Architecting for usability: a survey. Journal of Systems and Software, 70(1-2), 61-78. Recuperado de http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.13.7332

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 19 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 21 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

García, G. (2010). Metodología para el diseño y desarrollo de interfaces de usuario Web. Serie Científica de la Universidad de las Ciencias Informáticas (SC-UCI), 3(9). Recuperado de https://www.redib.org/recursos/Record/oai_articulo983182- metodologia-diseno-desarrollo-interfaces-usuario-web

Garret, J. (2000). Un vocabulario visual para describir arquitectura de información y diseño de interacción. Recuperado de http://www.jjg.net/ia/visvocab/spanish.html

Garrett, J. (2011). The Elements of User Experience: User-Centered Design for the Web and a Beyond (2ed.). Estados Unidos: Peachpit-Pearson Education.

Granollers, T. (2004). Características y Fases de MPIu+a. Recuperado de http://www.grihotools.udl.cat/mpiua/fases-mpiua/

Hassan, Y. (2009). Informe APEI sobre usabilidad. España: IPO. Recuperado de http://www.apeiasturias.org

Hassan Montero, Y., y Martín Fernández, F. (2005). La Experiencia del Usuario. HCI y Usabilidad. Recuperado de http://www.nosolousabilidad.com/articulos/experiencia_del_usuario.htm

Hernández, A. (2009). Arquitectura de información de los portales intranets: un componente esencial de la gestión de información en las universidades. Acimed, 19(4). Recuperado de http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S1024- 94352009000400006

International Standard Organization. (1994). ISO 9241-11: Ergonomic Requirements for Office Work with Visual Display Terminals (VDTs). Recuperado de http://www.iso.org/iso/catalogue_detail.htm?csnumber=16883

Kankainen, A. (2002). Thinking Model and Tools for Understanding User Experience Related to Information Appliance Product Concepts (tesis doctoral inédita). Helsinky University of Technology, Espoo, Finlandia. Recuperado de http://lib.tkk.fi/Diss/2002/isbn9512263076/

Krug, S. (2006). No Me Hagas Pensar 2E. España: Pearson Educación.

a Krug, S. (2013). Don't Make Me Think (3ed.). Estados Unidos: New Riders.

Montero, H. (2009). Informe APEI sobre usabilidad. España: IPO. Recuperado de http://www.apeiasturias.org

Montes de Oca, A. (2004). Arquitectura de información y usabilidad: nociones básicas para los profesionales de la información. Acimed, 12(6), 1-46. Recuperado de http://bvs.sld.cu/revistas/aci/vol12_6_04/aci04604.htm

Morville, P. (2004). User Experience Design. Recuperado de http://semanticstudios.com/publications/semantics/000029.php

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 20 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 22 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

Moyares, Y. y Bretones, D. (2010). La Arquitectura de Información (AI) en el proceso de desarrollo de software. Bibliotecas Anales de Investigación, (6). Recuperado de http://revistas.bnjm.cu/index.php/anales/article/view/47

Nielsen, J. (2001). Usabilidad. Diseño de páginas Web. España: Pearson Educación.

a Nielsen, J. (1999). Designing Web Usability: The Practice of Simplicity (7ed.). Indianapolis, Estados Unidos: New Riders Publishing.

Nielsen Norman Group. (2003). User Experience - Our Definition: NNG. Recuperado de http://www.nngroup.com/about/userexperience.html

Paz, L., y Cuellar, L. (2016). Diseño de la arquitectura de información del sitio web de la Facultad de Ingeniería Industrial y Turismo de la Universidad Central “Marta Abreu” de Las Villas (Cuba). Cuadernos de Documentación Multimedia, 27(2), 125-140. Recuperado de https://dialnet.unirioja.es/servlet/articulo?codigo=5631185

Paz, L., Hernández, E., y Manso, R. (2015). Diseño de la Arquitectura de Información para el Producto: InfoFEU-UCLV. Revista Científica Infociencia, 19(1), 1-12. Recuperado de http://webcache.googleusercontent.com/search?q=cache:fNb2Edr2mC0J:eprints.rclis .org/25038/+&cd=1&hl=es&ct=clnk&gl=cu

a Pressman, R. (2010). Ingeniería del software: un enfoque práctico (7ed.). España: McGraw- Hill Interamericana de España.

Ramírez, A. (2009). La usabilidad. Un acercamiento a su utilización en la UCI. Serie Científica de la Universidad de las Ciencias Informáticas (SC-UCI), 2(2). Recuperado de https://www.redib.org/recursos/Record/oai_articulo983055-usabilidad-acercamiento- utilizacion-uci

Revang, M. (2007). The User Experience Wheel: User Experience Project. Recuperado de http://userexperienceproject.blogspot.com/

Rodrigues de Albuquerque, A. F., y Lima-Marques, M. (2011). Sobre os fundamentos da arquitetura da informação. Perspectivas em Gestão & Conhecimento, 1, 60-72.

Ronda, R. (2007). Revisión de técnicas de arquitectura de información. Recuperado de http://www.nosolousabilidad.com/articulos/tecnicas_ai.htm

Ronda, R. (2011). Diseño de experiencia de usuario Teoría, Historia y Método. Recuperado de http://www.slideshare.net/rodricoco05/ux-teora-historiamtodos-38663194

Ronda, R. (2013). El etiquetado en el diseño de software. Recuperado de http://nosolousabilidad.com/articulos/etiquetado.htm

Sablón, Y., y Hernández, D. (2013). Arquitectura de Información en proyectos de desarrollo de software. Recuperado de http://www.nosolousabilidad.com/articulos/ai_rup.htm

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 21 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 23 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

Santana, Yudisel Pacheco. (2011). Arquitectura de Información en el Ciclo de Desarrollo del Software. Revista Electrónica Granma Ciencia, 15(1), 1-11. Recuperado de http://www.grciencia.granma.inf.cu/vol%2015/1/2011_15_n1.a15.pdf

Tramullas, J. (2002). Arquitectura de la información: más que diseño, hacia la findability. CLIP: Boletín de la CEDIC, (39), 1-3. Recuperado de http://www.sedic.es/clip39.pdf

Toub, S. (2000). Evaluation information architecture: a practical guide to assesing web site organization. Pensilvania, Estados Unidos: Argus Associates. Recuperado de http://argus-acia.com/white_papers/evaluating_ia.pdf

Wurman, R. (1975). Information Architects. Ponencia presentada en el American Institute of Architects, Zurich, Suiza.

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 22 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr

---

<!-- Página 24 -->

DOI: http://dx.doi.org/10.15517/eci.v7i1.24317

Volumen 7, número 1, Informe técnico 1 Ene-Jun 2017 e-Ciencias de la InformaciónRodríguez Castilla et al.

¿Desea publicar su trabajo? Ingrese aquí

O escríbanos a la siguiente dirección: revista.ebci@ucr.ac.cr

2011 2013 En la actualidad

Origen: respuesta a una necesidad Posicionamiento internacionalRevista de la UCR

En el año 2011, la Escuela dee-Ciencias de la Información es unaSe encuentra en el Cuartil A del UCR Índex Bibliotecología y Ciencias de la Informaciónrevista científica que aborda las nuevaspara el 2017, posicionándola como una de (EBCI) de la Universidad de Costa Ricatemáticas de desarrollo e investigación enlas mejores revistas de la Universidad de (UCR) reconoció la importancia de crearlas Ciencias de la Información, en elCosta Rica, un reflejo claro y conciso sobre nuevas y mejores alternativas paraámbito nacional e internacional. Así,su calidad y trascendencia en el área difusión de la investigación. e-Ciencias decolabora significativamente en el progresoapoyado por otros hitos como su ingreso a la Información es la respuesta a unde esta disciplina. Por sus parámetros deScielo, DOAJ, Latindex y otros. contexto actual marcado por una mayorcalidad, pertenece al grupo de las revistas apertura, flexibilidad, y rigurosidad en lamás importantes de la UCR y se verificación de los datos y suencuentra ampliamente indizada en los Volumen 4, número 2, Artículo 1procesamiento.importantes catálogos. Julio - Diciembre, 201

1 de j

Volumen 4, número 2, Artículo 1 Julio - Diciembre, 2014 23 Publicado 1 de julio, 2014ISSN 1659-4142 http://revistaebci.ucr.ac.cr revista.ebci@ucr.ac.cr