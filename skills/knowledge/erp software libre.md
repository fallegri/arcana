<!-- Página 1 -->

# TRABAJO FIN DE GRADO

## Título: ERP DE SOFTWARE LIBRE EN PYMES

## Autor: ROBERTO GONZÁLEZ ROMÁN

## Titulación: Grado en Ingeniería Informática

## Tutor: Miguel A. Ramos

## Fecha: 24 de septiembre de 2014

---

<!-- Página 2 -->

ERP de software libre en pymes

## Sobre el trabajo

El contenido de este trabajo se refiere a la utilización de software tipo ERP

(Planificador de recursos empresariales) en pequeñas y medianas empresas, dado

que este tipo de software no se suele implementar en empresas de este tamaño

debido a su coste, este trabajo trata acerca de cómo implementar opciones de

licencia libre en este tipo de negocios.

## Motivación y objetivos

La motivación del trabajo es conocer el funcionamiento de los ERP y de la

consultoría en general.

El objetivo del proyecto es dar la máxima difusión a los ERP con licencia de

software libre, ya que las pymes no requieren tanta funcionalidad como las

grandes empresas y la opción del software es una opción perfectamente válida

para satisfacer sus necesidades.

Otro objetivo es evaluar si trabajar con software libre es una opción rentable de

negocio a largo plazo.

2

---

<!-- Página 3 -->

ERP de software libre en pymes

## Índice

Sobre el trabajo ......................................................................................................... 2

Motivación y objetivos .............................................................................................. 2

Estructura del documento ........................................................................................ 7

Glosario ................................................................................................................... 10

English summary ..................................................................................................... 13 1 Capitulo1: Introducción ....................................................................................... 23

1.1 Contexto del trabajo...................................................................................... 23

1.2 Objetivos........................................................................................................ 24

2 Capítulo 2: Estado actual de los ERP y consultoría de ERP .................................. 26

2.1 Software actual ............................................................................................. 26

2.1.1 ERP de software libre.............................................................................. 29

2.1.2 ERP propietarios ..................................................................................... 30 2.1.3 Otro tipo de licencias .............................................................................. 31

2.2 Consultoría sobre ERP ................................................................................... 32

2.2.1 Análisis de necesidades .......................................................................... 32

2.2.2 Implantación de servicios ERP ................................................................ 32

2.2.2 Adición de nueva funcionalidad ............................................................. 33

2.2.3 Servicios de soporte técnico y evolutivo ................................................ 33

2.2.4 Reingeniería del proceso ........................................................................ 33 2.2.5 Servicios de hospedaje ........................................................................... 33

2.2.6 Software como servicio .......................................................................... 34

2.3 Estado actual de ERP en el mundo empresarial............................................ 34

3 Capítulo 3: Requisitos para la elección de ERP .................................................... 42

3.1 Requisitos en pequeñas y medianas empresas ............................................ 42

3.1.1 Elección de ERP vs Software de Gestión................................................. 43 3.2 Requisitos del ERP ......................................................................................... 44

3

---

<!-- Página 4 -->

ERP de software libre en pymes

3.2.1 Módulos del ERP ..................................................................................... 45

4 Capítulo 4: Consultoría en la implementación de ERP ........................................ 50

4.1 Implementación de un ERP ........................................................................... 50

4.2 Consultoría e implementación desde el punto de vista empresarial ........... 51 4.3 Consultoría e implementación desde un punto de vista técnico. ................ 55

5 Capítulo 5: Presupuestar la implementación de un ERP ..................................... 60

6 Capítulo 6: Análisis de los ERP de software libre ................................................. 63

6.1 Adempiere/Compiere.................................................................................... 63

6.2 Odoo .............................................................................................................. 75

6.3 Openbravo ..................................................................................................... 87

7 Capítulo 7: Guía técnica de implementación de un ERP .................................... 101 7.1 Viabilidad del ERP ........................................................................................ 103

7.2 Definición de alcance y forma de operar .................................................... 104

7.2.1 Definición del proceso de operación de la empresa con la herramienta ....................................................................................................................... 104

7.2.2 Tipo de implementación ....................................................................... 105

7.2.3 Arquitectura .......................................................................................... 106

7.2.4 Decisiones respecto a hardware y accesibilidad .................................. 108 7.3 Definición de acciones a realizar ................................................................. 109

7.4 Planificación para la realización de las acciones ......................................... 109

7.4.1 Estimación del coste ............................................................................. 110

7.4.2 Estimación de los recursos necesarios ................................................. 111

7.4.3 Planificación de la realización de las acciones...................................... 111

7.4.4 Seguimiento de la planificación ............................................................ 111 7.5 Formación del equipo.................................................................................. 112

7.6 Prueba inicial ............................................................................................... 112

7.7 Adaptación del ERP a las necesidades de la empresa ................................. 113

7.8 Instalación del software esencial y sala piloto ............................................ 113

7.9 Migración de datos ...................................................................................... 114

7.9.1 Migración mediante archivo de texto .txt ............................................ 115

4

---

<!-- Página 5 -->

ERP de software libre en pymes

7.9.2 Migración mediante el programa administrador de la nueva base de datos .............................................................................................................. 116

7.9.3 Migración mediante asistentes ............................................................ 119

7.9.4 Opción de no realizar la migración ....................................................... 120 7.9.5 Comprobando la integridad.................................................................. 124

7.9.6 Caso de los ERP ..................................................................................... 125

7.10 Instalación hardware ................................................................................. 125

7.11 Instalación del sistema ERP ....................................................................... 126

7.11.1 Servidor genérico en una máquina virtual ......................................... 126

7.11.2 Instalación tradicional ........................................................................ 128

7.11.3 Utilización de SaaS .............................................................................. 133 7.11.4 Caso práctico ...................................................................................... 133

7.12 Evaluación y pruebas del software instalado ............................................ 135

7.13 Formación de los empleados .................................................................... 135

7.13.1 Guía para la formación de un equipo en el uso de ERP ..................... 135

7.14 Proceso de adaptación y mejora continua ................................................ 139

7.15 Finalización del proyecto ........................................................................... 140

8 Capítulo 8: Factores que influyen en la efectividad de los ERP ......................... 142 9 Capítulo 9: Plan de empresa .............................................................................. 146

9.1 Datos básicos de la empresa ....................................................................... 146

9.2 Datos básicos del producto ......................................................................... 146

9.3 Promotores .................................................................................................. 147

9.4 Productos y servicios ................................................................................... 147

9.5 Plan de producción ...................................................................................... 148 9.6 Análisis del mercado.................................................................................... 149

9.6.1 Análisis DAFO ........................................................................................ 150

9.7 Plan de marketing ....................................................................................... 151

9.8 Organización y personal .............................................................................. 152

9.9 Plan de inversiones...................................................................................... 153

9.10 Escenario económico ................................................................................ 154

5

---

<!-- Página 6 -->

ERP de software libre en pymes

9.10.1Escenario tradicional ........................................................................... 154

9.10.2 Escenario Startup ................................................................................ 167

9.11 Elección del escenario económico, empresa tradicional o Startup .......... 176

10 Capítulo 10: marco regulador de los ERP......................................................... 183 10.1 Ley de protección de datos ....................................................................... 183

10.2 Licencias de difusión freeware y ley de propiedad intelectual ................. 191

10.3 Prestación de servicios en consultoría ...................................................... 191

11 Capítulo 11: Tendencias futuras ...................................................................... 194

............................................................................................................................... 196

12 Capítulo 12: Conclusiones ................................................................................ 197

13 Anexo 1 Tablas de porcentaje utilización ERP ................................................. 199 14 Anexo 2 guía de implantación planificación Microsoft Project ...................... 205

15 Bibliografía ....................................................................................................... 209

6

---

<!-- Página 7 -->

ERP de software libre en pymes

## Estructura del documento

1. Capítulo 1 Introducción.

En este apartado se explica y define qué es un ERP, sus aplicaciones y el problema

que se presenta con ellos. También se determinan los objetivos del trabajo.

2. Capítulo 2. Estado actual de los ERP y la consultoría de los ERP.

En este capítulo se explica el panorama actual de los ERP y los tipos que existen,

se distinguen por su tipo de funcionamiento y tipo de licencia. Después se explica la licencia de software libre y la licencia de pago. En este capítulo también se

incluye una explicación sobre la consultoría y los servicios habituales que ofrece

con respecto a los ERP. Por último, en este capítulo se presenta un estudio sobre

la utilización del ERP en el mundo actual, cómo se ha ido utilizando a lo largo de

los años y las previsiones futuras en la utilización de este.

3. Capítulo 3. Requisitos para la elección del ERP.

Este punto trata sobre las distintas condiciones que deben cumplir los ERP para

que sean necesarios o puedan llegar a usarse. Para ello se estudian los requisitos

que se necesitarán en la empresa; estas circunstancias definirán qué tipo de

empresas pueden implementar el ERP y las ventajas que obtendrán con ello; en

este punto también hacemos un análisis del software de gestión frente a los ERP,

dentro del ámbito de utilización de la empresa. También analizamos los requisitos

del ERP y estas serán las características que le pediremos, destacando: usabilidad,

escalabilidad, etc. pero sobre todo la funcionalidad; se explicarán todos los

módulos y funcionalidades que podremos requerirle a un ERP. Por último se

detallarán los requisitos principales y necesarios para poder hacer una

implementación ERP.

7

---

<!-- Página 8 -->

ERP de software libre en pymes

4. Capítulo 4. Consultoría en la implementación de ERP.

Bajo este título contemplamos los diferentes elementos que intervienen en la

implementación de un ERP. En un principio se explica la dimensión de la

implementación de un ERP, además del coste y tiempo que puede suponer,

después se explica el proceso de implementación. Posteriormente se expone

desde el punto de vista empresarial, es decir, de los factores que influyen en la

empresa: cómo va a tener que proceder ésta y en qué le va a afectar. El otro

punto de vista que se ofrece es el técnico: con él vemos el proceso, cuáles serán

las acciones a realizar y en qué orden, para poder llevar a cabo una

implementación satisfactoria.

5. Capítulo 5. Presupuestar la implementación de un ERP.

En este capítulo se describen una serie de elementos y pasos clave para hacer el

presupuesto de la implementación de un ERP.

6. Capítulo 6. Análisis de los ERP de software libre.

En este apartado se hace un análisis de los diferentes ERP de software libre

existentes actualmente en el mercado y de cada una de sus características en

función de los requisitos descritos en el capítulo 3.

7. Capítulo 7. Guía técnica de implementación de un ERP.

La guía contiene todos los pasos a realizar para la implementación satisfactoria de un ERP; para ello se elige un caso de uso simple, donde podremos ver las

diferentes opciones que tenemos para poder realizar aspectos específicos, como

puede ser una migración de la base de datos, instalación del software… También se explican procedimientos que deberemos cumplir como puede ser la formación

de los empleados en el uso del ERP.

8

---

<!-- Página 9 -->

ERP de software libre en pymes

8. Capítulo 8. Factores que influyen en la efectividad de los ERP.

Trata acerca de los factores necesarios para que se pueda producir una

implementación satisfactoria de un ERP.

9. Capítulo 9. Plan de empresa.

Se presenta un plan de empresa para una consultoría que se dedica a

proporcionar servicios sobre software libre. Se describen también dos posibles

escenarios económicos configurando la empresa como una Startup o como una

empresa tradicional.

10. Capítulo 10. Marco regulador.

En este apartado se describen las leyes esenciales que nos afectan a la hora de

ejercer la consultoría.

11. Capítulo 11. Tendencias futuras.

Una vez realizada toda la investigación del trabajo, podemos describir hacia donde

se dirige el sector, cómo serán los modelos de negocio del futuro, qué papel

jugará el nuevo software en la nube en el entorno de cambio actual, etc.

12. Capítulo 12. Conclusiones.

Se presentan las conclusiones finales del proyecto.

13. Bibliografía

9

---

<!-- Página 10 -->

ERP de software libre en pymes

## Glosario  Brainstorming o lluvia de ideas: es un proceso para fomentar la creatividad,

en el que se reúnen varias personas y aportan ideas; al principio no tienen

que tener sentido por sí mismas sino que sirven para fomentar la creatividad,

después se valoran las propuestas y se escogen una o una combinación de

varias que sí tengan sentido.

 CEO (Chief Executive Officer): es el equivalente a Director Gerente.

 CRM (Customer Relationship Management): se refiere a sistemas

informáticos que ayudan a gestionar las relaciones con los clientes. Suelen

ser una parte de sistemas de información como son los ERP.

 Dashboard: en informática suele referirse a una pantalla inicial que ofrece,

mediante un vistazo, el estado actual del sistema; normalmente suelen ser

configurables.

 Dbms (Data Base Management System) o Sistema de gestión de bases de

datos: es el software encargado de proporcionar, a los demás programas del

ordenador o la red, acceso a la base de datos así como la administración de ésta si es necesario; en términos generales es sinónimo de base de datos.

 Drivers: es un programa informático que ayuda al sistema operativo a

interactuar con un elemento ajeno a él, ya sea físico o no.

 ERP: sistema de información que integra la mayoría de las operaciones de

una empresa.

 Feedback (o retroalimentación, en español): es un proceso mediante el cual

obtenemos información del estado de un objeto, a través de los usuarios de

ese objeto.

 Hosting: servicio de almacenamiento de datos, normalmente a través de

Internet; suele implicar también servicios para acceder a esos datos como

puede ser alojar una web.

 JRE (Java Run Enviroment): bibliotecas esenciales de Java para poder

ejecutarse en un equipo.

10

---

<!-- Página 11 -->

ERP de software libre en pymes

 Mail list o listas de correo: es una lista de difusión a través de e-mail, permite

que cuando enviamos un mensaje le llega a todas las personas incluidas en la

lista de correo.

 Middleware: este software actúa como capa intermedia para poder

establecer comunicación entre dos aplicaciones; se encuentra entre la capa

de aplicación y la de SO.

 ODBC: se trata de una capa de middleware que se sitúa entre las aplicaciones

y el Dbms y nos permite acceder a los datos desde cualquier aplicación

independientemente del DBMS que utilicemos, siempre que el DBMS tenga

el driver que lo haga compatible.

 On-premises: software tradicional en el que tenemos una aplicación de

escritorio para ejecutarlo y no se ejecuta de manera remota.

 On-site: tecnología que no llega a extenderse a través de Internet, solo se

tiene acceso de manera local.

 Partner: se aplica a terceros que tienen una asociación con una determinada empresa, normalmente para prestar servicios que ésta no proporciona. En el

ámbito de la informática suelen denominarse así las empresas locales que

proporcionan soporte de un producto.

 POS/TPV (Point Of Sales/Terminal Punto de Venta): software que ayuda en la

tarea de venta al público mediante un interfaz para los vendedores.

 SCM (Supply Chain Management): módulo de los ERP que permite gestionar

la cadena de suministro de la empresa y gestiona la distribución de los

productos de la empresa.

 Setup: en informática suele referirse a un archivo de instalación, que lleva a

cabo todo el proceso de manera automática.

 Shareware: software que podemos utilizar bajo unas condiciones específicas,

normalmente para poder probarlo.

11

---

<!-- Página 12 -->

ERP de software libre en pymes

 SI (Sistema de Información): elemento orientado al tratamiento de datos e

información, normalmente lo usamos para referirnos a los sistemas

informáticos que realizan esta labor.

 SO/OS: abreviatura de sistema operativo.

 Triggers o disparadores: en bases de datos, se trata de acciones programadas

que se producen cuando se cumple una determinada condición.

 Unicode: es un estándar de codificación de caracteres, actualmente es el más

completo y ampliamente utilizado.

 WAN (Wide Area Network): se refiere a redes de acceso público,

normalmente internet.

12

---

<!-- Página 13 -->

ERP de software libre en pymes

## English summary

## Chapter 1: Introduction.

Work context

As soon as the technology advance, new solutions for the companies arise, this solutions usually provide new benefits for our business, the problem is that

occasionally this solutions are or too new and as result too expensive to get used

to the new changes, or too expensive because are a novelty.

This is the case of the ERP, the ERP or business resources planning system are

information systems that integrate and handle a lot of the business process

associated with the production, distribution and other aspects of the company in

the production of goods or services.

They integrate all the information in our company so we can maintain the

consistence of the information in real time. Besides it allow us to access to the

information in all the departments of the business.

This kind of software is widely used in big enterprises being the most usual

providers SAP AG, Oracle y Microsoft.

The problem is that this software is neither profitable nor accessible for the mid

and low size business.

Goals

The goal of the project is provide an environment so we can use the freeware ERP

systems in the mid and low size business, give that actually this kind of software is

not widely used in this field and it provides a bunch of competitive advantages

that we have to consider. Actually there is consulting firms that make this kind of

implementations we will adapt the software generally and provide a general ERP

13

---

<!-- Página 14 -->

ERP de software libre en pymes

knowledge so we can make this software approachable for the mid and low size

business, We also will make a complete guideline for the ERP implementation.

## Chapter 2: Actual state of the ERP.

There is different kind of ERP software give some differences between them, we

can first classify them for the kind of license that they have we have the free

licensed software and the pay licensed software.

The free license software used to be developed for a community or a company

that provide additional services to the software by itself.

We also can classify the software if it runs in our computer or in a remote server

and we execute the interface. The software that runs in other server gives us

some advantages as for example that the implementation time is lower, also they

save the cost of maintain dedicated servers for the application in our building. But

it also has some disadvantages, as nowadays the functionality is lower than the

traditional software and we cannot modify the software as we wish.

Besides the size of this kind of software there are specialized companies that

make the implementation and adaptation of it.

These consulting firms provide a bunch of services for the companies that want to

use of this software, between them we can find add new functionality to the ERP,

study the needs of the company, technical support , hosting services, software as

service…

In the paste there was a fear about the freeware solutions because the instability

of this kind of software, but actually there is a tendency in all the kind of business

to adopt the freeware solutions, something similar happens with the ERP

solutions in the past was an expensive software with a lot of functionality that was

only useful in the big companies environment, but now they are expanding their

use to smaller companies.

14

---

<!-- Página 15 -->

ERP de software libre en pymes

## Chapter 3: Requirements for the ERP election.

When we are going to implement an ERP there is a number of requirements that

we have to consider.

In the company we have to realize that the implementation of the ERP have to

give benefits to the company, in order to make that the implementation of an ERP

is a decision that it can´t be taken lightly, we have to consider all the factors

implied.

Also we should have some requirements for the ERP, essentially we have to

consider if it fill our expectations it has to be easy to use, scalable, available

support, documentation …

But the most essential requirement that we will make to an ERP is the

functionality, usually the ERPs functionality is grouped by modules, this modules

cover an all of needs in a process of the company, we can find for example

financial modules, logistics, materials, production…

We will also need an infrastructure for the execution of the application, as for

example a server, a database, people for maintain the new system…

## Chapter 4: Consulting in the ERP implementation.

From the business point of view the process of implementation there is process

that we will have to follow:

Project analysis: in this step we will study the needs of the company and the

suitable solution for them.

15

---

<!-- Página 16 -->

ERP de software libre en pymes

Project initialization: the consulting firm has to reach an agreement with the

client.

Solution development: the consulting firm develops the solution for the client.

Solution implementation: in this point the software is implemented in the

company.

Project close: when we have finished the implementation successfully we can

close the project.

Analysis and future develops: we have to learn of the implementation and analyze

the information for future developments.

## Chapter 5: Making a budget for the ERP implementation.

Making a budget for the ERP implementation can be really complicate there are a

lot of issues that we have to consider.

 The cost of the license if it´s not freeware.

 The hardware equipment’s

 Maintenance.

 Consulting expenses

The cost of the license in know from the beginning, also the hardware equipment

will be easy to calculate, in the other side maintenance and the consulting expenses will be variable, and will depend of the project accomplishment, to

calculate this expenses the best option is to use the software engineering.

## Chapter 6: Freeware ERP analysis.

This chapter is an analysis of three the three ERP: Adempiere, Odoo and

Openbravo.

16

---

<!-- Página 17 -->

ERP de software libre en pymes

In this chapter we analyze all the functionality that this software offers the

usability, database support, operating system support, installation methods,

scalability, modularity, security, actual support and future support.

## Chapter 7: Technical guideline for the ERP implementation.

There are a number of steps that we have to follow in the ERP implementation

process:

Viability of the ERP: We have to get the requirements for the ERP software that

the company needs, so we can assure a successful implementation in long term

orientation.

Definition of the way to proceed and the scope: In this step we decide where are

we going to make the implementation how and the business areas that it´s going

to affect. We will decide the kind of implementation, architecture, hardware…

Definition of the actions to do: we will specify all the actions that we need to do to

accomplish the implementation.

Planning the realization of the actions in this point we estimate the cost the

resources and we will plan and put them in the schedule so we can plan the

project and have an idea of where we are in the implementation project.

Team formation: we´ll form a team and inform them of the plan to do.

Initial test: we will make an initial test so we can know the characteristics of the

software and if it´s going to be possible to make the implementation.

Installation of the essential software and the show room: we will make a show

room where we can have an idea of how is going to be the software in the future,

and where we can teach the employees how to use the tool, and get information

of the needs of their specific work.

17

---

<!-- Página 18 -->

ERP de software libre en pymes

Data migration: once we have evaluated and fix the errors of the system, we can

make the migration between the old database to the new if it´s necessary.

Hardware installation: we will install all the necessary hardware for the normal

use of the ERP.

ERP system installation: we will make the installation of the software in the server

and the clients, there are different kinds of installations we can use a virtual

machine, a dedicated server, SaaS…

Assessment and testing of the installed software: we will make the probes that

guarantee that the software makes his function.

Employees training: we will train the employees in the use of the tool, the

practical use to be the most useful approach.

Adaptation and continuous improvement: once we have made all these steps we

will have to follow up the use of the tool and solve all the problems that might

arise.

## Chapter 8: Factors that influence the ERP effectiveness.

Essentially the success or failure of an ERP system is the responsibility of the

consultancy firm, we will need a serial of factors for accomplish the success of the

ERP implementation:

Consultancy support: is important that the consulting firm gets involved in the

process and the ones that have to get the next factors.

Effective communication: it´s important a good communication between the

consulting firm and the client company.

18

---

<!-- Página 19 -->

ERP de software libre en pymes

Conflict resolution: it´s mandatory solve the problems that might arise in the best

way possible.

Knowledge transfer: we will need a good knowledge transfer between the

consulting firm and the environment of the company.

Support from the top management: it´s essential the support of the top

management for the success of the project, they give all the resources and

authorization to accomplish the goals.

Support from the users: the users are the people that will use the tool, so in the

last instance are they who determine the success or the failure of the system.

## Chapter 9: Business plan

This chapter is about a business plan for a consulting firm with that provides

services based in freeware ERP.

It also describes two possible economic approaches the traditional and the

startup.

## Chapter 10: Legal environment.

In the ERP consultancy we need to consider some laws.

The first one is the data protection law it establish the way that the private data

have to storage the private data, we have three levels of security basic, medium

and high. In function of the required security level we´ll have to adopt more

security measures.

19

---

<!-- Página 20 -->

ERP de software libre en pymes

We also have to know the intellectual property law that establish the points in the

diffusion of the licenses in the freeware, give that we will use this kind of

software.

We will also need to know the essential mercantile laws that affect us give that we

provide services to other clients.

## Chapter 11: Future trends.

There is a tendency to adopt the ERP software in the companies. Actually there is

more information, and the companies need to organize it.

Also the new SaaS provides a good environment for the implementation in the

small sized business.

Because this and proliferation of work with remote teams in other countries could

be a good option to develop an ERP that also integrates cooperative tools to work

remotely and allow all the company to work remotely and have all the

information in the same place.

## Chapter 12: Conclusions.

Give the actual tends in the corporative field, we can say that the use of the ERP is

becoming in to something essential for all the companies, we can appreciate that

the companies that provide this kind of software are trying cover the needs of the

new market. But the nature of this kind of software, more simple that the

designed for the big enterprises, allow us to use the freeware as a perfectly valid

option, and also allow us to save a lot of money in the software licenses.

20

---

<!-- Página 21 -->

ERP de software libre en pymes

With the realization of this project we want to give diffusion to this kind of

software, give that this project can get close this software to the mid and low size

business, give that it provides a general knowledge frame for this kind of systems,

and the process of the implementation and use of them. Making easier the

understanding of the freeware ERP and allowing to these companies make the

leap to the future management systems. Because of this we can affirm that we

have accomplished the goal of the project, which was providing a tool for the

SMEs so they can understand and access to the freeware ERP.

Make this project had allowed me get to know the enterprise software in deep,

specially the ERP, making the study of all the process of implementation I have

realized of the size of him and the factors involved. I also give a complete vision of

them, thing that is a novelty because there is no actual material about it, give that

all the publications treat the issue in a specific part of the process or a specific

ERP, with this project is a leap to the understanding of this vast software and the

present and future odds.

21

---

<!-- Página 22 -->

ERP de software libre en pymes

# Capitulo1: Íntroduccion

22

---

<!-- Página 23 -->

ERP de software libre en pymes

## 1 Capitulo1: Introducción

1.1 Contexto del trabajo

A medida que las tecnologías avanzan surgen más soluciones para la empresa, las

cuales suelen proporcionarnos nuevos beneficios para nuestro negocio.

El inconveniente surge porque, en determinadas ocasiones, estas soluciones son

demasiado nuevas (puede ser costoso adaptarnos a los actuales cambios) o

pueden ser bastante más caras que las soluciones tradicionales debido a su

actualidad.

Este es el caso de los ERP, el ERP o sistemas de planificación de recursos

empresariales, son sistemas de información gerenciales que integran y manejan

muchos de los negocios asociados con las operaciones de producción y de los

aspectos de distribución de una compañía en la producción de bienes o servicios.

(Wikipedia, 2014)

Es decir, que integran toda la información de nuestra empresa para así poder

mantener la consistencia de la información en todo momento. Además nos

permiten acceder a ésta por parte de todos los departamentos de nuestra

empresa.

Este tipo de software es ampliamente utilizado en grandes empresas siendo sus

proveedores más comunes SAP AG, Oracle y Microsoft.

El problema es que este tipo de software no suele ser accesible ni rentable para

pequeñas y medianas empresas.

23

---

<!-- Página 24 -->

ERP de software libre en pymes

1.2 Objetivos

El objetivo del trabajo es proporcionar un marco para poder implementar los ERP

de software libre en pymes ya que actualmente esta clase de software no está

muy difundido en este ámbito y propone una serie de ventajas competitivas a

tener en cuenta. Actualmente existen empresas consultoras que su modelo de negocio es exclusivamente adaptar este software a las necesidades de la empresa,

pero en nuestro caso adaptaremos el producto de manera general y haremos una

guía para poder dar la máxima difusión a este tipo de productos; se propondrá

una guía para la realización de las implementaciones.

24

---

<!-- Página 25 -->

ERP de software libre en pymes

# Capítulo 2: Estado actual de los

# ERP y consultoría de ERP

25

---

<!-- Página 26 -->

ERP de software libre en pymes

## 2 Capítulo 2: Estado actual de los ERP y consultoría de

## ERP

2.1 Software actual

Actualmente en el sector de las tecnologías de la información hay una clara

diferenciación en el tipo de software:

 Software con licencia cerrada: es el tradicional, en el que nosotros pagamos

un dinero por el software y obtenemos un derecho de utilización, en este tipo

de software siempre hay una empresa detrás que nos cobra una licencia por

usar el software.

 Software de código abierto o utilización abierta (GLP y similares): en este tipo

de software una comunidad habitualmente, aunque también puede ser una

empresa, como el caso de Red Hat, nos permite utilizar el software de manera

gratuita, en ocasiones modificarlo y a veces nos permite incluso comercializar

productos que contengan parte de ese software.

También existe una diferenciación dependiendo de cómo se ofrezca el servicio y

ha surgido hace poco con el desarrollo de Internet:

 Software on-premises: es el más tradicional, en el cual nosotros mantenemos

el hardware y lo instalamos en nuestros ordenadores. A su vez, nosotros

tenemos el servidor y nos ocupamos del mantenimiento, las copias de

seguridad, esto puede suponer un coste mayor para las pequeñas empresas y

un ahorro para las grandes. Como podemos ver en el esquema del dibujo todo

el sistema queda dentro de las empresas.

26

---

<!-- Página 27 -->

ERP de software libre en pymes

 Software en la nube o software como servicio: este tipo de servicios han

surgido de manera relativamente reciente y lo que nos permiten es utilizar el

software, normalmente en un navegador o en otro medio, de manera que el

software se ejecuta en un servidor o servidores remotos y nosotros nos

comunicamos con ellos por medio de una interfaz en nuestro ordenador.

27

---

<!-- Página 28 -->

ERP de software libre en pymes

Ventajas y desventajas del software como servicio.

Esto permite implementar el software de manera más rápida al no tener que

hacer instalaciones ni hardware ni software.

Este modelo también permite externalizar la mayoría de los servicios que si no

tendría que hacer la propia empresa como pueden ser mantenimiento del

servidor, copias de seguridad, redes, actualizaciones...

Suelen ser más sencillos de usar que los ERP tradicionales, esto a costa claro de

perder algo de funcionalidad.

Por lo tanto el tiempo y coste de implementación de la herramienta ERP se reduce

de manera drástica, suponiendo una ventaja más que notable para las compañías.

Además este tipo de ERP hace que el cliente final no tenga que contratar a nadie

para gestionar y administrar los sistemas con lo que es el tipo de modelo que deja

al cliente más libre para realizar su trabajo y despreocuparse de actividades que

suele desconocer (Arnesen, 2013).

Por otra parte, también tiene algunos inconvenientes.

En primer lugar, la información de nuestra empresa no se encuentra en nuestros

servidores y no sabemos la seguridad que nos ofrece del proveedor del servicio; si

nuestra información es muy valiosa, probablemente no sea la mejor opción ya

que puede haber fallos de seguridad.

Las opciones de configuración son mucho más limitadas que en un ERP tradicional

ya que todavía no han llegado al punto de especialización de estos; el software es

más genérico.

No permite añadir nuevas funcionalidades específicas al ERP, el SaaS no

disponemos de esta opción pues el ERP utiliza el mismo software para todos.

28

---

<!-- Página 29 -->

ERP de software libre en pymes

No se integra con otras aplicaciones. Al contrario que en el ERP tradicional, en el

software como servicio no podemos integrar otras aplicaciones que nos interesen

en el ERP.

Al ser un proveedor diferente a nosotros, el cual da servicio a muchas empresas,

puede suceder que el servicio sufra caídas, como ha pasado con WhatsApp,

Twitter, etc. Si la utilización del ERP es o puede ser crítica en nuestra empresa, no

es la mejor opción.

Es posible que en el software en la nube no disponga de un API con la cual

podamos descargar nuestros datos para hacer una migración a otro sistema.

2.1.1 ERP de software libre

Actualmente, dentro de este tipo de software existen varias soluciones, una de las

más conocidas es Adempiere, la cual nos ofrece un ERP, CRM y SCM. Otro ejemplo

de este tipo de software es Apache OFBiz.

Dentro de las soluciones más adaptadas a las pymes podemos encontrar

Openbravo Comunity, está implementada en JAVA, este ERP ha sido diseñada

como una aplicación web, y está basado en el modelo “vista controlador”, por ello

lo que podemos apreciar que tiene una interfaz muy sencilla. También existe una

versión profesional de pago con más funcionalidades, servicio técnico, etc.

Como podemos comprobar es habitual que algunos proveedores de ERP ofrezcan

versiones de pago con una funcionalidad más reducida y, a pesar de ello,

probablemente sea más que suficiente para una empresa de pequeño tamaño y

para la mayoría de tamaño medio.

Dentro de las licencias de software libre podemos encontrar:

 Licencias permisivas: se puede crear una obra derivada sin obligación de

protegerla de ninguna manera, es decir las obras derivadas pueden tener

29

---

<!-- Página 30 -->

ERP de software libre en pymes

la licencia que deseen. Dentro de estas podemos encontrar la licencia de

Apache y la de Perl.

 Licencias restrictivas: aplican restricciones a las obras derivadas en cuanto

a su protección pueden ser:

o Restrictivas completas: las obras derivadas tienen que tener los

mismos medios de copyleft que el original del que se tomaron.

Dentro de estas podemos encontrar GNU General Public License

v.3.0. o la licencia de Eclipse.

o Restrictivas parciales: las obras que se deriven de ésta han de tener la misma licencia, pero las que se deriven de la segunda obra

pueden tener otra licencia distinta. Englobada dentro de estas

podemos encontrar la licencia de Mozilla, o la Open Source License.

2.1.2 ERP propietarios

Los ERP de pago más difundido son los dirigidos hacia las grandes empresas; éstos

suelen encontrarse dentro de soluciones mayores, que dan servicio a varias áreas

de la empresa y trabajan de manera conjunta con otros módulos como pueden

ser CRM, PLM, SCM o SRM. Las empresas más conocidas que realizan estas

soluciones son SAP AG, Microsoft, Oracle y Dassaultsystemes.

En el campo de la pequeña y mediana empresa hay otros proveedores distintos

como pueden ser Openbravo y Activant.

Estas podemos encontrar licenciadas al distribuidor o al cliente: las de distribuidor

se le cobran al distribuidor y éste puede cobrar por ellas o no, y las de cliente se

licencian directamente al cliente.

30

---

<!-- Página 31 -->

ERP de software libre en pymes

2.1.3 Otro tipo de licencias

Hay otros modelos de licencias como la que utiliza Openbravo (OBPL), similar a la

que utiliza Mozilla; en este software hay determinadas versiones que nosotros

podemos utilizar de manera gratuita y otras que requieren ciertos pagos, lo

mismo ocurre con las funcionalidades, que nos permiten el acceso si abonamos el

importe correspondiente.

Este tipo de licencias híbridas son cada vez más habituales. También las podemos

encontrar en el shareware que nos permite la utilización, pero con ciertas

restricciones como días de prueba o número de usos.

A continuación podemos observar un diagrama que representa las diferentes

licencias en función de sus características (Labrador, 2005).

(Ubuntu, 2012)

31

---

<!-- Página 32 -->

ERP de software libre en pymes

2.2 Consultoría sobre ERP

Además del modelo tradicional de venta de productos software, en el que la

empresa nos da el software y nosotros lo instalamos y utilizamos, debido a la complejidad de este software hay un modelo de negocio muy difundido en este

campo y es la consultoría, esta lo que nos ofrece son facilidades a la hora de

trabajar con estos sistemas; estas consultorías, nos permiten externalizar los

servicios que deseemos y ofrecen servicios tales como:

2.2.1 Análisis de necesidades

En ocasiones, las empresas, dado que no conocen el entorno, tampoco saben qué

partes del ERP le pueden ser útiles y cuáles ser realmente posibles de

implementar, el consultor se encargará de ofrecer la mejor solución a las

necesidades del cliente.

2.2.2 Implantación de servicios ERP

Debido a la dimensión de este tipo de productos, la implantación de estos puede

ser muy complicada. Por ello este servicio es la tarea principal de las consultoras.

Hay que integrar toda la información de la compañía existente y ello supone un

cambio en varios niveles:

 A nivel de software: normalmente este tipo de software es configurable

por lo que podemos adaptarlo a las necesidades de nuestro negocio para

así poder ser más rentable y cubrir nuestras necesidades.

 A nivel de hardware: habrá que instalar el nuevo modelo en las

maquinas/equipos existentes y comprobar su funcionamiento, también es

32

---

<!-- Página 33 -->

ERP de software libre en pymes

posible que haya necesidades que nuestros equipos actuales no cubran y

tengamos que adquirir nuevos.

 A nivel personal: todo cambio en la forma de trabajo de las personas

supone un periodo de formación y otro de adaptación.

Este servicio en particular lo trataremos más en profundidad en los capítulos 4 y 7.

2.2.2 Adición de nueva funcionalidad

En ocasiones la herramienta no soluciona toda la funcionalidad que la empresa

requiere; por ello algunas consultorías ofrecen el servicio de programación de nuevas funcionalidades para la herramienta.

2.2.3 Servicios de soporte técnico y evolutivo

Como todo sistema requiere un mantenimiento este tipo de servicios nos

permiten despreocuparnos y que sea otra empresa la que mantenga nuestro

sistema siempre activo y en buenas condiciones.

2.2.4 Reingeniería del proceso

Este servicio nos permite comprobar si los procesos de nuestra empresa están

bien planeados y analizar si se pueden optimizar; esto nos ayuda a contrastar si

estamos utilizando nuestro ERP de la manera adecuada.

2.2.5 Servicios de hospedaje

Nos ofrecen almacenamiento on-line para nuestra información y nos protegen

contra la pérdida de datos.

33

---

<!-- Página 34 -->

ERP de software libre en pymes

2.2.6 Software como servicio

Ofrecen el software como servicio que como sabemos ofrece un servicio

prácticamente integral y permite que para el cliente sea más fácil de gestionar.

Esta información ha sido obtenida investigando los distintos servicios que ofrecían

diferentes consultorías en sus páginas web. Además de los artículos: (Arnesen,

2013) (Maditinos, Chatzoudes, & Tsairidis, Factors affecting ERP system

implementation effectiveness, 2012).

2.3 Estado actual de ERP en el mundo empresarial

Consultando el Instituto Nacional de Estadística (INE, 2013)podemos observar las

empresas que utilizan soluciones ERP de código abierto y las que utilizan

aplicaciones ERP para compartir información de compras y ventas con otras áreas

de la empresa. Las tablas están detalladas en el 13 Anexo 1.

34

---

<!-- Página 35 -->

ERP de software libre en pymes

## Media total de uso de ERP para compartir

## información por tamaño de empresa

80

70

60

50

40

30

20

10

0 De 10 a 49 trabajadores De 50 a 249 trabajadores De 249 o más trabajadores

(INE, 2013)

Como podemos ver en estos datos, en el total de las empresas, mientras que en

las empresas de más de 250 trabajadores se utilizaban ERP en un 75,4%, en los

casos de las empresas de 10 a 49 solo un 28,3%. Por ello, podemos deducir que el

uso de este tipo de software no está demasiado difundido en la pequeña

empresa.

En los datos, también observamos que el uso de ERP es importante en función del

sector en el que nos encontremos y del tamaño; por ejemplo, en empresas de

productos minerales no metálicos (CNAE 19-23) de más de 250 trabajadores, se

utilizan en un 46,2% mientras que en actividades administrativas y servicios

35

---

<!-- Página 36 -->

ERP de software libre en pymes

auxiliares (CNAE 77-82) solo en un 19,3%. Esto se debe a la necesidad que tiene

cada sector de este tipo de software, generalmente los ERP son útiles cuando nos

dedicamos a distribución o fabricación y la consistencia de nuestros datos a lo

largo de la cadena de producción y distribución es importante, cosa que no

ocurre en el sector de los servicios administrativos. Por otro lado este software

también ofrece ventajas como la visibilidad hacia arriba cuestión que

determinados sectores valoran mucho.

36

---

<!-- Página 37 -->

ERP de software libre en pymes

## Uso ERP software libre por sector

3.7. Actividades administrativas y servicios auxiliares (incl. agencias viajes) (CNAE 77-82)

3.6. Actividades profesionales, científicas y técnicas (excl. veterianias) (CNAE 69-74)

3.5. Actividades inmobiliarias (CNAE 68)

3.4. Información y comunicaciones (CNAE 58-63)

3.3. Servicios de alojamiento (CNAE 55)

3.2. Transporte y almacenamiento (CNAE 49-53)

3.1. Venta y reparación de vehículos de motor comercio al por mayor al por menor (CNAE 45-47)

3. Total Servicios (CNAE 45-82, excluídas CNAE 56: servicios de comidas y bebidas, CNAE 75 y…

2. Total Construcción (CNAE 41-43)

1.5. Energía y agua (CNAE 35-39)

1.4. Productos informáticos, electrónico y ópticos material y equipo eléctrico maquinaria y equipo…

1.3 Metalurgia fabricación de productos metálicos ( CNAE 24-25)

1.2 Coquerias y refino de petróleo produc. farmacéuticos caucho y plásticos Productos…

1.1. Alimentación bebidas tabaco textil prendas vestir cuero y calzado madera y corcho papel…

0 20 40 60

(INE, 2013)

También apreciamos diferencias en la utilización del software de tipo libre entre

sectores debido al conocimiento de estos sectores de las tecnologías de la

información; por ejemplo, en el de tecnologías de la información: del 59,2% de

37

---

<!-- Página 38 -->

ERP de software libre en pymes

empresas que utilizaban soluciones tipo ERP, un 56,6 también utilizaba soluciones

tipo software libre

Para el procesamiento de información; en otro tipo de sectores, como

automoción, éste margen se llega a aumentar hasta un 20%. Podemos decir que la

baja difusión de las soluciones libres, generalmente, viene dada por el

desconocimiento de éstas y la dificultad para adaptarlas sin tener demasiados

conocimientos; además estas soluciones carecen de un servicio técnico detrás que

nos permita despreocuparnos de las tareas que conlleva.

Vistos estos datos llegamos a la conclusión siguiente: la utilización de los ERP es

bastante útil ya que en la mayoría de empresas grandes están implementadas

este tipo de soluciones, pero el cambio todavía no ha llegado a las empresas

pequeñas.

Vistos estos datos llegamos a la conclusión de que la utilización de los ERP es

bastante útil ya que en la mayoría de empresas grandes están implementadas

este tipo de soluciones, pero el cambio todavía no ha llegado a las empresas

pequeñas.

Deducimos, por tanto, que hay una tendencia a adoptar este tipo de software

debido a las ventajas que ofrece; además es un mercado relativamente reciente

por lo que, a medida que se va asentando y ofrece soluciones más competitivas,

tendrá una difusión más amplia. Como nos dice la revista pymes.es se ha

producido un crecimiento notable durante 2013 y se prevé aun mayor para 2014

(ERP: la evolución imparable de un mercado muy dinámico, 2014).

38

---

<!-- Página 39 -->

ERP de software libre en pymes

50 45 40 35 De 10 a 49 trabajadores 30 25 De 50 a 249 trabajadores 20 15 De 249 o más 10trabajadores 5 0 Periodo 2010-Periodo 2011-Periodo 2012- 201120122013

(INE, 2013)

En el gráfico apreciamos que en las grandes empresas se está produciendo un

cambio radical, de las soluciones de pago a soluciones de software libre. Esto

producirá que cada vez encontremos más soluciones de software libre y en un

futuro poder hacerlas más accesibles a las pequeñas y medianas empresas.

Respecto a las empresas pequeñas y medianas el cambio suele ser más lento ya

que no se encuentran en un entorno tan competitivo ni es imprescindible para

ellos las soluciones ERP; aunque en el gráfico no se aprecie existe un crecimiento

alrededor de tres puntos cada año, él lo cual no es nada despreciable. Debemos

tener en cuenta que cada año el 3% de las empresas pequeñas y medianas hacen

una nueva implementación que hace un total de unas 94.173 empresas cada año.

(Ministerio de Industria Energía y Turismo, 2014)

Por lo tanto, claramente podemos observar un crecimiento durante años en las

pequeñas y medianas empresas, además es probable que se produzca aumento

radical en su uso debido a la simplificación de éstos, ya sea por el avance en la

facilidad de implementación debido a ofrecer el software como servicio, o la

llegada de un mercado más competitivo como el de las grandes empresas a las pymes.

39

---

<!-- Página 40 -->

ERP de software libre en pymes

40

---

<!-- Página 41 -->

ERP de software libre en pymes

# Capítulo 3: Requisitos para la

# eleccion de ERP

41

---

<!-- Página 42 -->

ERP de software libre en pymes

## 3 Capítulo 3: Requisitos para la elección de ERP

Ahora vamos a analizar los diferentes requisitos que a considerar para elegir ERP.

Estudiaremos los requisitos de los tres factores más importantes para el éxito de

un ERP.

3.1 Requisitos en pequeñas y medianas empresas

Las empresas deberán cumplir una serie de requisitos para que les pueda ser

beneficioso el cambio a un ERP.

Para las empresas el cambio de sistema les debe reportar beneficios, es decir, en

primer lugar la implantación del sistema tiene que tener cierta estabilidad; ello

implica que la empresa no puede cambiar su forma de gestión cada poco tiempo,

es decir, en la elección del ERP tenemos que darnos cuenta que va a ser una

decisión con repercusiones a largo plazo. Para las empresas, que debido a las

necesidades del mercado o a la falta de definición de procesos no tengan

estabilidad en su modo de operación, un ERP puede ser muy beneficioso si se

consigue implantar pero la dificultad de la implementación puede ser muy grande

por ello, tendremos que valorar si nos conviene el cambio.

La principal ventaja de los ERP es que integran todos los procesos del negocio (no

como el software de gestión que cada uno cumple cierta funcionalidad), por tanto

para hacer el salto del software de gestión al ERP tendremos que evaluar ciertos

elementos, comparándolo con las diferentes decisiones estratégicas que tenemos

en nuestra empresa. Puede que, en un breve periodo de tiempo tengamos

previsto cambiar los distintos departamentos u organigrama de la empresa, si

hacemos una implementación ERP y a los dos meses tenemos que adaptarlo al

42

---

<!-- Página 43 -->

ERP de software libre en pymes

nuevo cambio el incremento del coste puede ser inadmisible, probablemente nos

convenga retrasar la implementación.

Por tanto a la hora de determinar si una empresa cumple los requisitos, es decir, si

es viable, para un cambio a un sistema de gestión ERP tendremos que hacerlo

como una decisión estratégica de la empresa, en el momento adecuado y con el

cambio también apropiado para a la empresa. Sobre la viabilidad de la empresa

para el cambio se puede obtener más información en el capítulo7.

3.1.1 Elección de ERP vs Software de Gestión

Cuando hagamos la elección del tipo de software en nuestra empresa habremos

de tener especial cuidado pues debemos considerar el poder utilizarla el mayor

tiempo posible; por tanto éste este será nuestro principal elemento a valorar

cuando elijamos el sistema: Si nuestra empresa no tiene previsión de crecer a

largo plazo y no tiene un tamaño demasiado elevado probablemente nos

convenza más el software de gestión ya que suele ser más barato y más simple.

Lo primero que tenemos que darnos cuenta es que el cambio a un sistema ERP,

más que una decisión con implicación en los sistemas software, será mayor el

impacto en la forma de gestión y de trabajar de nuestra empresa; por ello

requiere que esté soportada por la alta dirección, ésta es la que tiene que decidir

si conviene la implantación del sistema ya que es una decisión estratégica más

que tecnológica. Tendremos que hacernos una serie de preguntas: si con el nuevo

sistema vamos a ganar una ventaja competitiva con respecto a nuestros

competidores, cómo afecta el nuevo sistema a nuestra posición en el mercado o

cómo afecta el sistema a la situación organizacional y cultural de la empresa.

(Niehaves, Klose, & Becker, 2006).

Por contra, si esperamos que nuestra empresa crezca es conveniente que

instalemos el ERP lo antes posible antes, ya que cuanto más tarde lo instalemos el

43

---

<!-- Página 44 -->

ERP de software libre en pymes

cambio será más costoso además cuanto antes adaptemos el ERP a nuestra

empresa mejor funcionaremos en el futuro. (Prasad Bingi, 1999).

3.2 Requisitos del ERP

Lo primero que buscamos en un ERP es que satisfaga las necesidades de la

empresa, pero como hemos comentado antes no solo nos podemos quedar en las

necesidades actuales, también tenemos que evaluar cuáles van a ser nuestras necesidades futuras y si el ERP las cumple.

Por otro lado tanto el ERP como todos los elementos que lo integran, es decir

ordenadores, base de datos, servidor, sistema operativo…

El ERP tiene que ser escalable, es decir, que podamos aumentar su funcionalidad

con la adición de nuevos módulos o elementos al sistema a medida que nuestra

empresa va creciendo.

También es importante la previsión de futuro del ERP, es decir, si va a seguir

habiendo soporte para el programa en un futuro, este es un factor a tener en

cuenta en los ERP de software libre, pues es más habitual que caigan en el olvido,

esto produciría que en un futuro nuestro software esté anticuado y tengamos que

hacer una nueva implementación.

Tiene que tener una comunidad o empresa activa detrás del producto, es decir

tiene que esté garantizado su funcionamiento en determinadas situaciones que

surjan en un momento determinado, como puede ser un fallo de seguridad.

El ERP ha de ser usable, es importante que para acortar el tiempo de

implementación el ERP sea lo más intuitivo y fácil de utilizar posible.

Pero sobre todo tiene que ser simple; una pequeña y mediana empresa no

necesita toda la funcionalidad que pueden proporcionar los grandes ERP como

44

---

<!-- Página 45 -->

ERP de software libre en pymes

SAP r/3, es mejor la instalación de otro programa que requiera menos tiempo de

implantación y sea escalable.

En cuanto a la funcionalidad del ERP podremos pedirle una serie de módulos o

funcionalidades.

3.2.1 Módulos del ERP

La agrupación de la funcionalidad incluida en los módulos varía según el ERP que

estemos utilizando, por ello esta clasificación la haremos en función de uno de los

ERP más difundidos SAP r3, además, es probablemente uno de los ERP más

modulares por lo que sus diferentes módulos están bien definidos.

Probablemente se vaya aceptando una división similar a la de SAP a medida que

se amplíe la funcionalidad de los ERP de software libre. Los diferentes módulos o

áreas de funcionalidad son las siguientes.

45

---

<!-- Página 46 -->

ERP de software libre en pymes

Finanzas

Este módulo nos permite gestionar la contabilidad de nuestra empresa de manera

eficaz, además proporciona una visión general hacia arriba de la situación

financiera de la empresa, como se están gestionando los activos y la situación de

la contabilidad. Dependiendo del ERP que utilicemos en este campo podemos

tener muchas más aplicaciones, como gestión de cuentas por pagar y cobrar,

gestión de los arrendamientos o gestión de los viajes de empresa.

Costos y control

Este módulo ofrece la funcionalidad necesaria para analizar los costes en los que

está incurriendo la empresa, qué es lo que le están aportando y de donde vienen.

Este módulo ofrece una visión general hacia arriba de la distribución de los costes

de la empresa. En los ERP más avanzados podemos encontrar distribución de

costes por productos y por actividades.

Logística

Este módulo se utiliza para organizar productos, suministros y demás se refiere,

los módulos más avanzados tienen opciones en este módulo como la gestión de

los procesos, configuraciones y demás; dando una buena visibilidad hacia arriba

de estos. Es habitual encontrarlo de manera conjunta con el módulo de ejecución

logística.

Ejecución de logística

Este módulo lo usamos para gestionar la logística del almacén, los recursos de la

empresa, expediciones transportes, etc. Este módulo es especialmente útil si

tenemos una red de almacenes.

Ventas y distribución

Este módulo recoge la funcionalidad relativa a ventas y distribución del producto, desde la gestión de la facturación, la gestión de los datos de los clientes que

compran mediante comercio electrónico, la facturación, gestión de envíos,

gestión de las tarifas e incluso soporte de venta y post-venta.

46

---

<!-- Página 47 -->

ERP de software libre en pymes

Gestión de materiales

Este módulo nos permite manejar la gestión de los materiales por parte de los

proveedores. Podemos planificar necesidades de consumo de nuestra empresa,

gestionar las compras, gestionar los inventarios, verificar las facturas a pagar.

Producción

Este módulo organiza la producción de nuestra empresa, dentro de él entran la

organización de la planta de producción, los procesos que utilizamos para fabricar

nuestros productos, controles de calidad, gestión respecto a la normativa de

medio ambiente.

Recursos humanos

Este módulo gestiona todo lo relativo al área de recursos humanos, contratación,

nóminas, formación, costes de personal, rendimiento de los empleados, gestión

de eventos…

Soluciones de desarrollo/Gestión de proyectos

Dentro de estos módulos podemos encontrar funcionalidades desde la creación

de informes, pantallas con flujos lógicos, constructores de clases… Es decir todo lo

que nos ayude en el desarrollo de un nuevo producto. Es también habitual

encontrar dentro de esta categoría también software para la gestión de equipos

de desarrollo. En ocasiones también encontramos algunas herramientas de ayuda

creativa como el Brainstorming.

Soluciones específicas por industria

Dentro de este campo de módulos entran los módulos que ofrecen

funcionalidades específicas para alguna de las industrias del mercado.

47

---

<!-- Página 48 -->

ERP de software libre en pymes

48

---

<!-- Página 49 -->

ERP de software libre en pymes

# Capítulo 4: Consultoría en la

# implementacion de ERP

49

---

<!-- Página 50 -->

ERP de software libre en pymes

## 4 Capítulo 4: Consultoría en la implementación de ERP

4.1 Implementación de un ERP

Lo primero que habremos de darnos cuenta a la hora de implementar un ERP es

que este de manera genérica no suele cumplir el 100% de las necesidades de nuestra empresa, u ofrece funcionalidades que no nos interesan. Esto se produce

ya que las empresas tienen su propio método de operación. Las empresas

demandan que sea el ERP se adapte a sus necesidades y no al revés. Por lo que las

empresas adaptar el sistema sus necesidades, aquí es donde entra la consultoría.

La mayoría de los ERP son personalizables dependiendo de las necesidades de

nuestra empresa, pero si bien el coste de desarrollo será menor que el de crear

software propio, este sigue siendo bastante alto.

Otra opción es cambiar la forma organizacional de la empresa y adaptarlo al ERP

aunque no nos guste, ya que los métodos de operación de los ERP suelen ser los

más habituales y más optimizados (Rosemann, 2010).

Otro problema es la necesidad de software especializado, suele producirse porque

nuestra empresa tiene necesidades de software específico. Dado que es posible

que en la empresa tengamos que utilizar software externo al ERP, para ello existe

el middleware que se encarga de adaptar estos programas externos a nuestro ERP

pudiendo hacer que los dos trabajen conjuntamente (Al-Mashari, 2003).

El problema de este tipo de software es el mantenimiento, suelen dar problemas

cuando tenemos que aplicar actualizaciones, normalmente debidos al software

ajeno y la forma de actuar con nuestro ERP, pudiendo suponer un gran gasto para

el departamento tecnológico de las empresas. Por ello tenemos que minimizar la

utilización de programas externos dentro de nuestro ERP pues generarán más

gastos y problemas futuros.

50

---

<!-- Página 51 -->

ERP de software libre en pymes

El trabajo de integración del ERP normalmente suele ser completamente externo

a la actividad de la empresa y es una gran carga de trabajo especializado, por lo

que los encargados de hacerlos suelen ser las consultoras.

En nuestro caso haremos una diferenciación entre el proceso a tener en cuenta en

la empresa a la que realizamos la implementación, y el proceso a tener en cuenta

si lo analizamos como un técnico.

4.2 Consultoría e implementación desde el punto de vista empresarial

Como sabemos la implementación del ERP suele ser una tarea compleja, pero

podemos utilizar métodos para dividir la complejidad de esta tarea y ayudarnos

en la toma de decisiones. Cada consultoría obviamente tendrá sus diferentes

métodos de analizar los casos, pero nosotros utilizaremos el método de la teoría

del gobernador (Yin, 2003).

51

---

<!-- Página 52 -->

ERP de software libre en pymes

Con esta metodología dividimos la implementación de la solución en siete etapas:

Etapa1 análisis del pre-proyecto

Primero estudiaremos los diferentes actores que se verán implicados y las

configuraciones institucionales necesarias. (Niehaves, Klose, & Becker, 2006).

Es decir estudiaremos la empresa, cuáles serán sus necesidades y su capacidad de

operación; no podrá destinar el mismo presupuesto a tecnologías de la

52

---

<!-- Página 53 -->

ERP de software libre en pymes

información una pequeña empresa que una gran multinacional, también

tomaremos en cuenta factores como: si la empresa tiene departamento de

tecnologías de la información, si su proceso de trabajo es adecuado para trabajar

con ERP, el conocimiento de los empleados con respecto al ERP además de otra

serie de aspectos críticos. Dependiendo de estos factores tomaremos unas

implementaciones u otras.

Etapa 2 Inicialización del proyecto

Es la etapa en la que negociamos con la empresa, en ella exponemos nuestra

solución con su presupuesto, forma de implementación, inconvenientes…

(Niehaves, Klose, & Becker, 2006).

Tenemos que llegar a un acuerdo con la empresa, probablemente tengamos que

adaptar nuestra solución ante las decisiones de los CEO y ceder por ambas partes.

En este punto es importante obtener el apoyo de la dirección de la empresa para

que el proyecto siga adelante, si no es probable que este fracase.

En este paso es donde decidiremos si podemos cumplir las expectativas del cliente

o no, si no podemos cumplir lo esperado lo que debemos hacer es retirarnos en

esta etapa o volver a proponer otra solución.

Etapa 3 análisis del problema

En esta etapa es en la que identificamos el problema que debe de ser resuelto

durante el proyecto. (Niehaves, Klose, & Becker, 2006).

53

---

<!-- Página 54 -->

ERP de software libre en pymes

La tarea principal en este punto es, una vez que sabemos lo que vamos a hacer,

encontrar los diferentes problemas que vamos a encontrar en este proceso,

principalmente los que influyen en la implementación de la solución, entre ellos

podemos encontrar, por ejemplo: que la planificación hecha en un inicio requiera

más trabajo.

Etapa 4 desarrollo de la solución

Cuando llegamos a esta etapa buscamos solución a los problemas encontrados,

definimos la dimensión real de la implementación del ERP y buscamos la forma de

implantación más óptima (Niehaves, Klose, & Becker, 2006).

Etapa 5 Implementación de la solución

En esta etapa hacemos implementación del despliegue de la solución (Niehaves,

Klose, & Becker, 2006), aquí es donde se la presentamos a los usuarios de la

solución, encontramos los fallos que puedan surgir al interactuar con el entorno

real y hacemos los cambios pertinentes para una implementación satisfactoria.

Etapa 6 cierre del proyecto

En este punto cerramos el proyecto, con la ayuda de un comité se evalúa el

resultado final del proyecto, la funcionalidad final del sistema, como se ha llevado el proyecto, la satisfacción del cliente, consistencia con la planificación, coste del

proyecto, y revisión del proceso en general. (Niehaves, Klose, & Becker, 2006).

54

---

<!-- Página 55 -->

ERP de software libre en pymes

Etapa 7 análisis y diseños futuros

En este punto ya que es probable que no hayamos implementado todos los

módulos de la compañía, es posible empezar de nuevo para así poder continuar e

integrar más elementos de la compañía en el ERP, esta vez utilizando la

experiencia obtenida en el caso anterior.

También en este punto es importante el mantenimiento del sistema y la

adaptación a los diferentes cambios.

4.3 Consultoría e implementación desde un punto de vista técnico.

Desde el punto de vista del consultor existen una serie de pasos que tenemos que

llevar a cabo para realizar una implementación satisfactoria del proyecto.

1. Elección del ERP, el consultor tiene que determinar si la empresa es la

adecuada para implementar el ERP y si este puede mejorar su capacidad

de operación.

2. Después necesitaremos saber cómo va a operar y que recursos y áreas de

la empresa va a cubrir.

3. Definición de las actividades a realiza: una vez sabemos el alcance del

proyecto el siguiente paso es conocer todas las acciones que tendremos

que realizar para poder implementar el ERP.

55

---

<!-- Página 56 -->

ERP de software libre en pymes

4. Planificación del proyecto: sabiendo las actividades a realizar el siguiente

paso es planificar como vamos a realizarlas, tenemos que hacer una

adecuada distribución del tiempo y recursos.

5. Formar al equipo: dado que vamos a implementar un nuevo sistema

bastante complejo, tendremos que formar al nuevo equipo en la

realización de la implantación,- informarle del proyecto y de las acciones a

realizar y el reparto de tareas.

6. Prueba inicial del sistema: servirá para comparar las diferentes opciones

disponibles mediante una pequeña implementación de cada una,

evaluaremos con que software podemos satisfacer las necesidades del

cliente de manera más óptima.

7. Adaptación del sistema: una vez elegido el software que más se adapta a

las necesidades de la empresa, es habitual añadir o modificar el software,

para que se adapte de manera completa a las necesidades de la empresa.

8. Creación de sala piloto: crearemos una sala piloto donde podamos evaluar

el sistema más a fondo, formar a los empleados en la nueva herramienta y

detectar posibles errores de interacción del usuario con la herramienta.

9. Migración y revisión de la integridad de los datos: en la empresa sus datos suelen ser uno de los activos más valiosos, por lo que poder migrarlos

íntegramente al nuevo sistema y evitar la pérdida de estos, es nuestra

prioridad principal.

56

---

<!-- Página 57 -->

ERP de software libre en pymes

10. Instalar el nuevo hardware: una vez tenemos nuestra base de datos

migrada de manera óptima el siguiente paso es instalar el nuevo hardware

que pueda dar soporte al nuevo sistema.

11. Instalar el nuevo software: haremos la instalación de sistema ERP en la

empresa, lo habitual que en esta fase no se haya hecho una instalación

completa, o que todavía funcionen de manera simultánea los dos sistemas

el antiguo y el nuevo.

12. Pruebas del sistema: probaremos toda la funcionalidad del sistema y

evaluaremos si cumple los acuerdos de servicio, esta fase puede incluir

pruebas con el consultor y los futuros usuarios de la herramienta.

13. Capacitación del personal de la empresa: formaremos a las personas que

van a estar en contacto continuo con el sistema y que lo van a utilizar.

14. Entrenamiento real: parte del entrenamiento de los empleados consistirá

en interactuar con la herramienta de manera directa para así tener un

entendimiento completo del mismo.

15. Mejora continua: es importante obtener retroalimentación de la utilización

del sistema para así saber que el sistema pueda adaptarse al cambio o

mejorar, haremos los cambios precisos para que la implementación del nuevo sistema tenga éxito. (Cuéllar, 2014)

57

---

<!-- Página 58 -->

ERP de software libre en pymes

58

---

<!-- Página 59 -->

ERP de software libre en pymes

# Capítulo 5: Presupuestar la

# implementacion de un ERP

59

---

<!-- Página 60 -->

ERP de software libre en pymes

## 5 Capítulo 5: Presupuestar la implementación de un

## ERP

Presupuestar un ERP es una de las tareas más complicadas a realizar en

consultoría aparte de ser por sí misma una tarea difícil ya que hay multitud de

elementos a tener en cuenta. Hay dos factores que empeoran esta situación, por

un lado tenemos la presión de las compañías para abaratar coste y acortar

tiempos de implementación. Y por otro lado es habitual que las empresas del

sector hagan presupuestos poco realistas (Solution Square, 2006).

Esto produce que de media el coste de los proyectos esté un 178% por encima

del presupuesto y el tiempo de entrega 2,5 veces por encima del planificado.

(Rouhani & Ravasan, Jun 2013).

Los tres factores que conforman el precio final de nuestro ERP, serán: los gastos

que tendremos al realizar la implementación, los gastos de la empresa y segundo

los beneficios que queramos obtener.

Para obtener una visión clara de los beneficios que vamos a obtener tendremos

que estimar los gastos de implementación.

Para saber el coste del proceso de implementación tendremos que tener en

cuenta todos los recursos que necesarios para realizar una implementación:

 Coste de licencia o SaaS, si es que existe.

 Personal consultor

 Equipos hardware

60

---

<!-- Página 61 -->

ERP de software libre en pymes

 Mantenimiento

De los equipos hardware será sencillo hacer una estimación bastante exacta de los

costes.

La dificultad de estimar el coste de una implementación será saber las horas que

necesitaremos para hacer la implementación.

Para determinar esto podemos utilizar ingeniería del software, una vez hemos escuchado los requisitos del cliente, sabremos cuáles serán las acciones a realizar

en la implementación.

Sumaremos todas las horas invertidas en cada uno de los pasos necesarios del

proceso de implementación desde el estudio de viabilidad hasta el cierre o

mantenimiento del proyecto.

Una vez determinado el número de horas necesarias, el resto es negociar con el

cliente el precio final de este, obteniendo nosotros siempre beneficio claro.

En la vida real suele producirse un problema y es que las negociaciones con el

cliente del presupuesto las hacen los comerciales no los técnicos, y en un mercado

muy competitivo como es el de la informática y debido al desconocimiento del

coste por parte de las personas de trabajar con algo no material, como es el

software, los presupuestos siempre son más ajustados de lo que deberían.

(Solution Square, 2006)

61

---

<!-- Página 62 -->

ERP de software libre en pymes

# Capítulo 6: Analisis de los ERP de

# software libre

62

---

<!-- Página 63 -->

ERP de software libre en pymes

## 6 Capítulo 6: Análisis de los ERP de software libre

Hay una gran cantidad de software ERP disponible, algunos de ellos son software

creado por comunidades, mientras que otros los crea una empresa y nos ofrece

ciertas funcionalidades y si queremos acceder a todas las funcionalidades

disponibles tenemos que pagar una cuota.

Lo que vamos a hacer en este capítulo es describir algunos de los ERP de software

libre del mercado actual y explicar y evaluar las funcionalidades que nos ofrece

cada uno de ellos.

Para las pruebas se han utilizado las versiones virtuales y de prueba pero también

se ha estudiado el proceso de instalación

6.1 Adempiere/Compiere

En un inicio Adempiere formaba parte de Compiere pero debido a discrepancias

se separaron, ahora Adempiere es un proyecto de código completamente libre,

mientras que Compiere ha tomado un modelo en el que cobra por determinadas

funcionalidades.

En nuestro caso analizaremos el ERP Adempiere al ser la solución de código libre,

pero hay que reseñar que los dos ERP son de similares características, se puede

apreciar en elementos como que el proceso de instalación es el mismo.

Facilidad de instalación

Para las instalaciones en Windows podemos encontrar un paquete que incluye

todo el necesario para montar un servidor rápidamente.

63

---

<!-- Página 64 -->

ERP de software libre en pymes

En los demás casos haremos una instalación normal, instalando cada uno de los

componentes y haciendo que funcionen entre sí, en este proceso seguimos una

serie de pasos que son:

 Instalación del software de soporte: Java JDK y la base de datos

 Instalación del software del servidor

 Configuramos el servidor

 Inicializamos y sincronizamos la base de datos con el servidor

 Lanzamiento del servidor de aplicaciones.

 Lanzamiento de la aplicación de Adempiere.

El proceso de instalación tiene las características habituales de cualquier ERP, en

este caso necesitaremos Java para interactuar con el ERP ya que la aplicación

utiliza Java.

Compatibilidad con bases de datos

Es compatible con las bases de datos: Oracle 10g free for developement, Oracle

10gXE y Postgre SQL.

Como podemos ver no es compatible con Mysql que aunque ahora pertenezca a

Oracle sigue siendo de licencia libre y una de las más utilizadas. Si bien es cierto

que la comunidad ha desarrollado una versión que funciona con él, esta versión

compatible con Mysql no está reconocida y su instalación no es trivial.

Como podemos ver cubre las principales bases de datos de software libre

exceptuando Mysql, pero no cubre ninguna de las bases de datos de pago ya que las versiones de Oracle a las que ofrece compatibilidad son de utilización libre. No

podemos tener acceso ni a Microsoft SQL Server, ni a DB2 de IBM, ni a las

versiones de Oracle de pago.

64

---

<!-- Página 65 -->

ERP de software libre en pymes

En cierta medida el software es compatible con las bases de datos de licencia

libre, ya que el producto es de licencia libre lo que es lógico, pero a pesar de que

el futuro de Mysql sea incierto respecto a Postgre SQL todavía es una opción muy

válida a tener en cuenta

Compatibilidad con sistemas operativos

Respecto a la compatibilidad con sistemas operativos tiene una compatibilidad

bastante amplia en los sistemas operativos de software libre.

 Es compatible con prácticamente todos los sistemas Linux que tienen una

amplia difusión y puede funcionar con:

o Suse.

o Red Hat.

o CentOS.

o Debian / Ubuntu

o FreeBSD.

 Dentro de otros sistemas UNIX puede funcionar con OpenSolaris.

 De los SO de Mac es compatible con MAC OSX

 Dentro de Windows es compatible con las versiones 2000, XP (con ciertas

limitaciones), Vista, Windows 7, Windows 8. Y de los servidores de Windows solo es compatible con la versión del 2003.

Como podemos ver tiene una amplia gama de sistemas operativos, cubre prácticamente todas las opciones posibles de software libre.

Facilidad de uso

En esta caso evaluamos la interfaz tipo web al ser la más actualizada, es una interfaz sencilla que presenta un menú lateral y es fácil de entender, pero la

estética no es atractiva, en un principio es probable que se tarde un tiempo en

adaptarse la nueva interfaz, pero es más óptimo que otras opciones más visuales.

65

---

<!-- Página 66 -->

---

<!-- Página 67 -->

En cuanto al punto de venta disponemos de varias interfaces distintas diseñadas

por la comunidad, actualmente la mayoría de ellas soporta pantalla táctil y son

sencillas y claras.

(Comunidad Adempiere, 2011)

Funcionalidad

Su funcionalidad no está dividida de la manera habitual por módulo, sino por procesos de negocio siendo los que ofrece (Openbiz, 2014):

---

<!-- Página 68 -->

ERP de software libre en pymes

Proceso de compras

Este proceso permite emitir órdenes de compra, procesamiento de facturas de

proveedores y pagos efectuados. Se integra con la Administración de la Cadena de

Suministro (SCM).

(Openbiz,2014)

Proceso de Ventas

Abarca los procesos de negocios utilizados para la creación de presupuestos,

administración de órdenes de venta, facturación y recibos. Esta funcionalidad se

integra con la Administración de la Cadena de Suministro (SCM) y con la

Administración de Relaciones con el Cliente (CRM).

68

---

<!-- Página 69 -->

ERP de software libre en pymes

(Openbiz,2014)

Proceso de Saldos Pendientes

Automatiza los procesos asociados con la entrada y asignación de dinero medios

de pago recibido de los clientes y los pagos efectuados a los proveedores. Aquí

puede también efectuar la conciliación de pagos en tránsito y cargos bancarios

que constarán en los libros de caja.

(Openbiz,2014)

Administración de Relaciones con el Cliente (CRM)

Al contrario que los demás este sí es tradicionalmente un módulo, provee una

vista de todas las actividades con los clientes. Permite administrar la creación,

distribución y seguimiento de los clientes, proveedores y los pedidos generados.

69

---

<!-- Página 70 -->

ERP de software libre en pymes

(Openbiz, 2014)

Administración de la Cadena de Suministro (Abastecimiento)

Cubre todas las actividades de administración de productos, incluyendo

recepciones, entregas, movimientos y administración, y procesamiento de tomas

de stock.

Permite definir productos y servicios con cuentas de materiales y sustitutos, estas

listas pueden ser actualizadas o importadas de la lista de precios del proveedor.

El sistema acepta tener múltiples listas de precios, no solo para ventas sino

también para compras, lo que permite controlar los descuentos y créditos de los

proveedores. Estas listas de precios son controladas por períodos, posibilitando el

manejo de ofertas especiales y precios por temporadas.

Maneja múltiples depósitos físicos y permite además, para cada uno de ellos,

configurar diferentes depósitos lógicos. Opera la recepción, el control de calidad,

la verificación, el almacenamiento y el despacho de productos. Admite también el

manejo de inventario “en tránsito”.

70

---

<!-- Página 71 -->

ERP de software libre en pymes

(Openbiz, 2014)

Contabilidad y Análisis de Resultados

Cubre el área de las finanzas y diferentes dimensiones contables de la aplicación.

Esta funcionalidad generalmente se encuentra en los módulos de Contabilidad

General. Utiliza un mecanismo de asignación contable basado en reglas aplicadas

a los documentos de manera automática y cuentas por defecto. En cada

transacción que se realiza existe una regla contable, evitando así que el usuario

tenga que recordar códigos contables, ya que los mismos son asignados por el

sistema utilizando las reglas mencionadas.

(Openbiz, 2014)

71

---

<!-- Página 72 -->

ERP de software libre en pymes

Modularidad

Como podemos ver en el apartado de funcionalidad, la clasificación mediante

procesos de negocio hace que perdamos cierto encapsulamiento respecto a los

módulos tradicionales pero desde luego es una opción interesante ya que nos

permite una modularidad mayor al hacer unidades modulares con menos

funcionalidad, pero no carentes de sentido por sí mismas.

Escalabilidad

El producto básico se distribuye como un paquete completo con todas las

funcionalidades antes mencionadas, pero gracias a la comunidad podemos añadir

diferentes funcionalidades que nos permiten adaptarlo a nuestras necesidades.

Conectividad con otras herramientas

No hemos encontrado compatibilidad con ninguna otra herramienta de las más

conocidas.

Seguridad

Respecto a la seguridad, tiene un esquema de seguridad mediante roles, los datos

que se presentan a cada rol así como las operaciones que le está permitido

realizar están controladas y se pueden modificar. Podemos gestionar los roles que

deseemos y gestionar los permisos de estos.

Además podemos gestionar los roles de manera que solo tengan acceso a

determinados tipos de datos, así como restringir el acceso sobre ciertos datos

específicos. De manera que podemos por ejemplo hacer distinciones

interdepartamentales, de manera similar al modelo de muralla china, además de

los habituales modelos de seguridad por nivel de acreditación por rol.

Soporte actual

Actualmente dispone de una wiki muy completa que posiblemente cumpla todas nuestras necesidades.

72

---

<!-- Página 73 -->

ERP de software libre en pymes

La comunidad dentro de Adempiere está formada por personas que antiguamente

formaban parte del proyecto de Compiere, y las dos comunidades están bastante

unidas, actualmente está formada por profesionales del sector, la comunidad no

tiene demasiados miembros, pero actualmente siguen haciendo aportes al

proyecto.

Existe un foro del proyecto donde podemos consultar nuestras dudas pero el

tiempo medio de respuesta es dos días, por lo que es posible que nuestra duda

quede sin resolver a tiempo.

Soporte futuro

El hecho de no tener una comunidad demasiado grande hace que el soporte

futuro sea incierto, de hecho la última versión del software estaba prevista para

2013 pero aún no se ha publicado de forma definitiva. El software más actual que

se sabe funciona de manera segura es del año 2011

(Adempiere ERP, 2014)

A pesar de ello en este gráfico podemos ver la cantidad de descargas que ha

tenido en los dos últimos años y deducir que su uso aún sigue siendo muy

difundido, como se suele decir si algo funciona bien no hay por qué cambiarlo.

73

---

<!-- Página 74 -->

ERP de software libre en pymes

De todas maneras se está apreciando una caída progresiva en su uso por lo que

probablemente no sea la mejor opción si pensamos obtener una mayor

funcionalidad en el futuro.

74

---

<!-- Página 75 -->

ERP de software libre en pymes

6.2 Odoo

Odoo es un ERP cada vez más difundido, siendo Odoo el nombre de la última

versión ya que hicieron bastantes cambios importantes. El proyecto y la

comunidad tienen bastante historia, la primera versión se publicó en 2005 bajo el

nombre de Tiny ERP, después una versión renovada y con más funcionalidades y una estética típica de ERP por módulos se liberó con el nombre de Open ERP,

versión que se sigue utilizando y ofreciendo soporte, y por último en mayo de

2014 surgió la plataforma ERP como la conocemos actualmente con el nombre de

Odoo, a pesar de ello sobre todo en el software libre disponible sigue utilizando el

nombre de open ERP.

Actualmente se trata de una herramienta ERP programada sobre Python formada

por pequeñas aplicaciones que ofrecen una funcionalidad completa, pero pueden

comunicarse entre sí. Actualmente el proyecto ofrece servicios de SaaS, se trata

de software de código abierto de origen comercial. A pesar de ello está publicado

sobre una licencia AGPL por lo que todo el código creado ha de ser difundido.

(Rozo development, 2014)

Como podemos ver tiene la configuración típica cliente servidor de tres capas que tienen habitualmente los ERP.

75

---

<!-- Página 76 -->

ERP de software libre en pymes

Facilidad de instalación

Si utilizamos la oferta de pago de SaaS, la instalación es prácticamente trivial y

solo tendremos que volcar nuestros datos mediante archivos .csv, el servidor de

aplicaciones se incluye en el precio, por lo que con abrir nuestro navegador

acceder al servicio por internet será suficiente para poder utilizar la herramienta.

En el caso de utilizar la versión on-site, el proceso de instalación será lógicamente

más complejo, pues tendremos que crear el servidor para dar servicio a las

aplicaciones.

Podemos instalar un cliente como aplicación de escritorio, pero recomiendan

utilizar la versión web, lo cual simplifica bastante la instalación.

Las instalaciones varían en función del sistema operativo:

En el caso de Linux primero tendremos que hacer la instalación de Postgre SQL y

configurarlo para comunicarse con el ERP, después el resto de la instalación se

hace mediante consola, ya que todo el código está vinculado a Linux y solo

tendremos que utilizar el comando apt-get para instalar todos los paquetes, por

último ejecutar un setup de Python para instalar el servidor. Tanto el servidor

como el cliente se instalan de manera similar.

En el caso de Windows dispone de dos opciones de instalación, la primera es

instalar un paquete todo en uno que hace una instalación general. La segunda

opción es una instalación por partes, en este caso también disponemos de un

setup que nos facilita el proceso de instalación.

Compatibilidad con bases de datos

El servidor de ERP solo es compatible con la base de datos Postgre SQL que si bien

es una base de datos muy potente el programa podría ser compatible con otras bases de datos de software libre.

76

---

<!-- Página 77 -->

ERP de software libre en pymes

Por tanto cuando hagamos la implementación de un sistema de este tipo,

probablemente tengamos la necesidad de hacer una migración de nuestros datos

a una nueva base de datos tipo Postgre, o utilizar una conversión tipo ODBC para

utilizar Postgre SQL como capa superior (más información en el capítulo 7).

Compatibilidad con sistemas operativos

En cuanto a sistemas operativos de software libre solo es compatible con las

arquitecturas Ubuntu, también existe una versión para Debian pero ya no tiene

soporte.

Se puede utilizar también en Windows en todas sus versiones a partir de 2000.

Y por último la comunidad ha creado una versión que funciona con Mac OSX pero

todavía no es estable.

Facilidad de uso

Es una de las máximas de este ERP, en el toda la información es muy visual y los

menús son de estética similar a la de los servicios que ofrece Google. Cada una de

las aplicaciones funciona por separado pero de manera integrada, con lo que

siempre sabes a donde dirigirte.

Se pueden encontrar todas las aplicaciones en la parte superior de la pantalla a

modo de menú horizontal, después como menú vertical tenemos las opciones

dentro de esa aplicación.

77

---

<!-- Página 78 -->

---

<!-- Página 79 -->

La interfaz del punto de venta también es muy visual y sencilla además de estar

preparada para interactuar con pantallas táctiles.

En cuanto a la Accesibilidad mediante dispositivos móviles y tabletas, es más

limitada, por ahora solo está disponible la aplicación de Android y se encuentra en

fase beta, además de que solo tiene soporte para la mensajería interna y las notas

personales.

Funcionalidad

Se divide por aplicaciones, dentro de las cuales cumplen un área de funcionalidad

determinada de manera similar a los sub-módulos de SAP, de la mismo forma

podemos agrupar estas aplicaciones según su naturaleza de manera similar a los

módulos.

Las aplicaciones principales son:

---

<!-- Página 80 -->

ERP de software libre en pymes

Ventas

Dentro de este rango se encuentran las aplicaciones que ayudan en el proceso de

ventas de la empresa.

CRM

Nos ayuda a gestionar las relaciones con los clientes, es bastante básica

pero cumple con la funcionalidad esencial.

Gestión de ofertas

Permite la gestión de ofertas de manera directa con los clientes, tiene

firma electrónica y comunicación con los clientes a través del ERP, está

orientado a clientes mayoristas.

Punto de venta

El punto de venta está bastante simplificado y aislado, no ofrece la

funcionalidad que ofrece Openbravo o Adempiere en el que puedes añadir

productos en el POS, pero cumple con las expectativas básicas y está

adaptado a entornos táctiles.

Administración

En este rango podemos encontrar las aplicaciones que nos ayudan en la

administración de la empresa dentro de esta categoría encontramos:

Gestión de proyectos

Ofrece una herramienta muy completa de gestión de proyectos que

permite desde el reparto de tareas y generación de gráficos Gantt hasta la

utilización de software colaborativo tipo Google Drive. No es tan potente como Microsoft Project pero cumple su cometido.

80

---

<!-- Página 81 -->

ERP de software libre en pymes

Facturación

Permite gestionar contratos, crear facturas y recibos, generar gráficos del

cobro de facturas.

Contabilidad

Permite llevar la contabilidad de la empresa, se integra con las aplicaciones

de compras y facturación permite generar informes de manera

automática.

Gestión de almacenes

Permite gestionar almacenes, hacer inventarios, seguimiento de los

productos…

Gestión de producción

Incluye toda la funcionalidad asociada a la gestión de la producción,

emisión de órdenes, planificación, manejo de bienes de producción…

Compras

Con esta aplicación se gestionan todos los recibos, compras, comparación

de precios, tendencias del mercado…

Marketing

Dentro de esta división se encuentran las aplicaciones de marketing y

comunicación

Mail

Aplicación que integra el servicio de mail dentro del ERP

Chat

Permite establecer un chat en tiempo real con los demás empleados

conectados al ERP

Encuestas

Permite hacer encuestas interactivas de opinión en la empresa.

81

---

<!-- Página 82 -->

ERP de software libre en pymes

Automatización de campañas

Permite la automatización de campañas como pueden ser las de

marketing, genera informes, envía mails de manera automática...

Eventos

Esta aplicación ayuda en la creación de eventos, permite generar páginas,

vender tickets, sincronizarse con Google Analyctics para llevar un

seguimiento…

Comunidad

Ayuda en la gestión de foros y blogs

Recursos humanos

En esta área se engloban las aplicaciones relativas a los recursos humanos de la

empresa.

Empleados

Se trata de un directorio de empleados.

Red social

Permite establecer una sencilla red social entre los empleados para

aumentar la comunicación y fomentar el sentimiento de equipo

Reclutamiento

Permite organizar los procesos que involucran la selección de nuevos

empleados, como puede ser lanzar ofertas de trabajo, informes de

procesos de selección, encuestas online...

Nóminas

Permite llevar las cuentas de las nóminas de los empleados

Evaluación Permite evaluar a los empleados, rendimiento, gastos…

82

---

<!-- Página 83 -->

ERP de software libre en pymes

Comidas

Permite gestionar los gastos relativos a comidas de empresa, se vincula

con cada empleado, genera cuentas…

Flota

Es una aplicación que ayuda en el seguimiento de la flota de vehículos de

la empresa, puede almacenar información como quién tiene el vehículo,

kilómetros recorridos, gasto en carburantes, estado de los vehículos…

Productividad

Estas aplicaciones nos ayudarán a mejorar la productividad de la empresa

BI

Aplicación de inteligencia de negocio para la dirección, genera estadísticas

para la empresa, previsiones futuras y estado actual de los procesos.

API

Permite la conexión con hardware externo al ERP, es bastante completo y

permite unir nuestro propio software al ERP.

Gamificación

Esta aplicación intenta aplicar reglas que se encuentran generalmente en

los videojuegos para motivar a los empleados para hacer determinadas

tareas, como pueden ser rankings, metas o competiciones.

Grupos de discusión

Ofrece una funcionalidad similar a las antiguas listas de correo.

Con todas las herramientas cooperativas que encontramos hay que decir que se

trata de una gran opción para desarrollos distribuidos, ya que permite una gran

interrelación entre los empleados y generar la idea de compañía, lo cual siempre

es importante.

83

---

<!-- Página 84 -->

ERP de software libre en pymes

Aparte de estas aplicaciones, que son las principales, el proyecto posee más

aplicaciones que proveen otras funcionalidades menores, el total de sus

aplicaciones actualmente es de 4166.

Escalabilidad

El ERP es bastante escalable ya que podemos utilizar las aplicaciones que

queramos, sabiendo que cada una de ellas cumple una funcionalidad específica, si

queremos integrar otra parte del funcionamiento de la empresa solo tendremos

que empezar a utilizar la aplicación correspondiente.

Modularidad

La división por aplicaciones ofrece una imagen visual bastante clara del

encapsulamiento, y permite una modularidad muy fina, podemos encontrar

aplicaciones como Horarios, Calendario, Directorio de Empleados…

También hay que decir que no todas las aplicaciones son del mismo tamaño, estos

pueden ser muy dispares, por ejemplo contabilidad y finanzas constituye solo una

aplicación pero en cambio tenemos otras mucho menores como una cuya utilidad

es únicamente escribir notas.

Seguridad

La seguridad en Odoo está basada también en roles, en los cuales podemos

definir, y asignar diferentes permisos según áreas de la empresa.

A continuación en la imagen se puede ver la pantalla de creación de un nuevo

usuario y las áreas de permisos diferenciables por departamentos.

84

---

<!-- Página 85 -->

ERP de software libre en pymes

Conectividad con otras herramientas

Tiene un API bastante desarrollado que permite una conectividad muy amplia con

las herramientas que nosotros diseñemos.

85

---

<!-- Página 86 -->

ERP de software libre en pymes

Aparte de ello la comunidad ha desarrollado código de manera que es compatible

con otras herramientas como las de comercio electrónico: Magento, PrestaShop,

OSCommerce, Zen Cart…

Soporte actual

Al ser software libre de origen comercial tiene una red de alrededor de 250

partners de los cuales 16 de ellos en España.

Con respecto a la comunidad, es muy activa en el repositorio de Github en el que

se encuentra el proyecto se puede ver que se hacen cambios cada hora

aproximadamente.

Existe también un foro para poder responder a las preguntas donde el tiempo

medio de respuesta son dos horas, algo más que razonable.

Soporte futuro

Respecto al soporte futuro al ser un software libre comercial, es habitual que se

siga trabajando en él para mejorar el servicio, y con el soporte de una empresa

detrás es más difícil que caiga en el olvido.

Se sabe que se está trabajando en el proyecto y que existe una nueva versión

llamada 8.0 que estaba prevista su publicación en julio de 2014.

86

---

<!-- Página 87 -->

ERP de software libre en pymes

6.3 Openbravo

Openbravo se trata de una plataforma ERP de software libre pero su licencia no es

GPL, sino Openbravo Public License, derivada de Mozilla Public License 1.1, esto le

permite hacer dos versiones: una es la versión Profesional, la cual es de pago y

dispone de las funcionalidad al completo y por otro lado la versión Comunity la cual tiene las funcionalidades más limitadas pero es de software libre. En nuestro

caso nos dedicaremos a estudiar la versión de software libre Comunity.

El software está basado en Java, la arquitectura es orientada a modelos por lo que

permite una buena integración con otros elementos.

Respecto a la versión Comunity no es tan completa como la versión Profesional,

pero cumple las necesidades básicas de la empresa, y si la empresa así lo necesita

siempre puede ampliar la funcionalidad suscribiéndose a la versión de pago.

Facilidad de instalación

Para la instalación del software se nos ofrecen varias opciones la primera es la

opción de utilizar el SaaS de la versión Profesional.

La segunda opción es la de utilizar una máquina virtual, la cual denominan

Openbravo Appliance para que funcione en nuestro servidor dentro de cualquier

sistema operativo, esto solo suele utilizarse como prueba para saber las

funcionalidades que ofrece la aplicación no es habitual utilizarlo en una

instalación estándar, debido a las escasas opciones de configuración, pero hay que

decir que como instalación es rápida y sencilla y si tenemos una máquina potente

puede que no nos importe virtualizar el servidor.

87

---

<!-- Página 88 -->

ERP de software libre en pymes

También nos permite utilizar la nube de Amazon, en ella utilizaremos el SaaS, pero

en este caso tendremos la capacidad de procesamiento en nuestro servidor que

contratemos con Amazon.

Instalación en Ubuntu, esta será la mejor opción de instalación si queremos crear

un servidor normal en nuestra red local sin tener que utilizar virtualización, para

hacer la instalación haremos una sucesión de comandos apt-get para instalar todo

el software necesario, utilizará un servidor web Tomcat que nos permitirá

comunicarnos con el servidor mediante un servicio HTTPS.

Por último disponemos de una guía de la instalación personalizada por pasos de

un modelo de tres capas que nos servirá para otras distribuciones de Windows y

de Linux.

Compatibilidad con bases de datos

Es compatible con Postgre SQL de software libre, y con las bases de datos de

Oracle, para poder utilizar Mysql tendremos que utilizar alguna solución tipo

ODBC.

Compatibilidad con sistemas operativos

En cuanto a sistemas operativos es compatible con todos los sistemas que sean

capaces de utilizar máquinas virtuales pero esto solo nos permitirá utilizar el

servidor de manera virtual.

Para poder hacer una instalación típica, tendremos que tener como sistema

operativo Ubuntu, Red Hat, o alguna de los sistemas operativos de Microsoft

desde la versión 2000.

Facilidad de uso El software igual que los demás funciona mediante web, la interfaz está bastante

depurada, según entramos en la aplicación nos encontramos con un dashboard

configurable, el que podemos colocar la información que deseemos: Figura1

88

---

<!-- Página 89 -->

---

<!-- Página 90 -->

Dispone de un menú en la parte superior de manera horizontal que nos permite

acceder a las aplicaciones y a las alertas.

Las aplicaciones se encuentran agrupadas por el área a la que pertenecen en

menús desplegables.

La primera vez pueden ser difíciles de encontrar pero el programa va

almacenando cuales son las aplicaciones del sistema que hemos utilizado y nos las

presenta en primer lugar.

Además en el Dashboard inicial al que llama Workspace, en la parte derecha,

podemos ver un histórico con los últimos documentos vistos y aplicaciones usadas

recientemente.

---

<!-- Página 91 -->

ERP de software libre en pymes

Soporta múltiples ventanas aumentando la visibilidad de las pantallas:

El menú de cada ventana se muestra en la parte superior y muestra toda la

funcionalidad mediante simbología bastante sencilla.

Permite una definición completa del diccionario de la aplicación permitiéndonos

definir todo los elementos que deseemos.

Respecto al POS o terminal punto de venta, es muy potente y avanzado, dispone

de todo lo necesario para gestionar ventas tanto para mayoristas como para

minoristas, permite crear productos, revisar stock, ventas, ver los pagos...

En el caso de POS se trata de una aplicación de escritorio pero es fácil de instalar y

conectar con la base de datos del servidor ERP.

91

---

<!-- Página 92 -->

ERP de software libre en pymes

92

---

<!-- Página 93 -->

ERP de software libre en pymes

Funcionalidad

(redk, 2014)

Respecto a funcionalidad, probablemente sea el más potente de los tres ERP

analizados, tiene la división por módulos típica de los ERP.

Diccionario de la aplicación

Permite la definición de los procesos de la herramienta, permite definir

determinados campos de la herramienta dándole una gran capacidad de

configuración.

Configuración general

En este apartado encontramos todas las herramientas de configuración de la

herramienta y los clientes. Dentro de ella podemos encontrar herramientas de

configuración sobre:

 La aplicación

 El cliente

93

---

<!-- Página 94 -->

ERP de software libre en pymes

 El modelo de negocio de la empresa

 Seguridad

 Planificación del proceso

 Configuración del espacio de trabajo

Gestión de datos maestros

En esta sección permite la gestión de datos relativos a la empresa, generalmente

la información de la empresa relativa a:

 Socios

 Productos

 Precios

Gestión de aprovisionamiento

Permite realizar todas las gestiones relativas a las compras de la empresa:

 Tarifas

 Pedidos de compra

 Recepción de mercancías (Notas de entrega)

 Registro y contabilización de facturas de proveedores

 Planificación de compras

 Facturas de compra

 Relación entre pedidos, notas de entrega y facturas

 Facturas de gastos  Informes de pedidos de compra, facturas de proveedores

Gestión de almacenes Permite todas las gestiones relativas a los almacenes y stocks de productos:

 Almacenes y ubicaciones (varias ubicaciones)

 Stock por producto en doble unidad

94

---

<!-- Página 95 -->

ERP de software libre en pymes

 Atributos del producto en almacén personalizable

 Lote y número de serie

 Impresión de etiqueta. Código de barras

 Gestión de bultos de almacén

 Control de reposición

 Trazabilidad configurable por producto

 Movimiento entre almacenes

 Gestión automática de salidas de stock

 Inventario físico, planificación de inventario, inventario continuo

 Informes de movimientos

Gestión de ventas

Permite la gestión de las ventas de la empresa hacia el exterior y permite

automatizar ciertos procesos de facturación entre otras cosas:

 Zonas de ventas

 Pedidos de venta

 Creación automática a partir de líneas de pedido pendientes

 Automatización de las salidas

 Generación automática de notas de entrega

 Proceso de facturación

 Pedido en PDA (Palm y PocketPC)

 Información unificada de clientes (visión 360°)  Gestión de peticiones. Integración con correo electrónico

Gestión financiera

Permite la gestión de la información financiera de la empresa y ofrece una vista

general de esta, y automatiza procesos financieros:

95

---

<!-- Página 96 -->

ERP de software libre en pymes

 Plan de cuentas

 Cuentas contables

 Presupuestos

 Impuestos

 Contabilidad general

 Cuentas por pagar

 Cuentas por cobrar

 Contabilidad bancaria

 Balance

 Cuenta de resultados

Aparte de las funcionalidades antes mencionadas tiene la capacidad de generar

informes y gráficos para el análisis de las diferentes situaciones de la empresa (BI).

Openbravo POS

Se trata de una herramienta muy potente, a diferencia del resto del ERP está

aislado y funciona sobre una aplicación de escritorio, según el rol de la persona

registrada podemos:

 Gestionar ventas, stock y clientes.

 Permite la generación automática de facturas mediante la creación de

iconos de acceso rápido.

 Gestiones de la caja.

 Gestión de clientes.

 Etc.

96

---

<!-- Página 97 -->

ERP de software libre en pymes

Escalabilidad

El software básico provee una funcionalidad bastante amplia pero siempre que lo deseemos podemos agregar funcionalidades con la versión de pago.

Modularidad El software no es demasiado modular ya que a pesar de estar organizado por

módulos, no podemos elegir instalar unos sí y otros no por lo que al final el ERP es

un gran paquete de software donde se encuentra toda la funcionalidad unida. Si

contratamos el SaaS es distinto ya que no tendremos que instalar nada y nos

permitirán el acceso a la funcionalidad que contratemos.

Conectividad con otras herramientas

Tiene una gran compatibilidad con otras herramientas, permite desde generar

tablas Excel con los datos, hasta exportar los informes en formato PDF…

97

---

<!-- Página 98 -->

ERP de software libre en pymes

Permite también la integración con las herramientas de Google como son Google

Drive, Google Analytics…

Seguridad

Dispone de una seguridad por roles en la que puede hacerse distinción por

departamentos, áreas geográficas, cargos… Por lo que el sistema de

diferenciación por roles es bastante eficiente.

Además de por el rol en la empresa podremos diferenciar también a los

empleados por el departamento al que pertenecen y por el área geográfica en la

que se encuentren.

Dispone además de servicio de auditoría que registra las acciones de cada uno de

los usuarios.

98

---

<!-- Página 99 -->

ERP de software libre en pymes

Soporte actual

Actualmente la empresa nos ofrece soporte, pero es de pago.

Disponemos de una wiki que contiene información sobre la instalación, manual de

uso…

También disponemos de un foro en la página web SourceForge, en el que pueden

solucionar nuestras dudas, disponemos incluso de un apartado para las dudas de

los técnicos y usuarios en España.

Soporte futuro

El problema de este software es que actualmente se está volviendo demasiado

comercial, es posible que dentro de unos años no dispongamos de solución de

software libre, pero actualmente se trata de uno de los ERP de software libre más

potentes.

99

---

<!-- Página 100 -->

ERP de software libre en pymes

# Capítulo 7: Guía tecnica de

# implementacion de un ERP

100

---

<!-- Página 101 -->

ERP de software libre en pymes

## 7 Capítulo 7: Guía técnica de implementación de un

## ERP

En este capítulo describiremos el proceso de implementación de un ERP desde el

primero hasta el último recorreremos todos los pasos que habremos de realizar

en la implementación de un sistema en pequeñas y medianas empresas.

101

---

<!-- Página 102 -->

ERP de software libre en pymes

102

---

<!-- Página 103 -->

ERP de software libre en pymes

Para poder ejemplificar los pasos que iremos realizando, describiremos un

pequeño escenario práctico donde podamos ejemplificar lo explicado en cada

paso.

En este ejemplo se trata de una pequeña empresa.

Actualmente posee un sistema tradicional y quiere renovar su software para

poder ser más competitivos en el sector y poder soportar en formato electrónico

la mayoría de sus archivos, las especificaciones que nos indican son las siguientes:

 Quieren que el ERP les permita llevar toda la información relacionada con

la empresa relativa a: o Clientes

o Contabilidad y finanzas

o Gestión de ventas

o Gestión de almacén

 Conservar todos sus datos, que actualmente se encuentran en una base de

datos Access.

 Tienen dos tiendas y un almacén separados geográficamente y quieren

que los datos sean consistentes entre todos.

 Poder hacer un registro de clientes en que se pueda ver que es lo que ha

comprado cada uno.

 Registro del inventario en tiempo real.

7.1 Viabilidad del ERP

Para determinar la viabilidad del proyecto tendremos en cuenta los

requerimientos de viabilidad que nos ha dado la empresa, evaluaremos si

podemos cumplirlos y en qué medida. Para poder hacer esto se requiere un

estudio de la empresa, y del software, una vez que sabemos que podremos

cumplir los requisitos de viabilidad de la empresa podremos continuar.

103

---

<!-- Página 104 -->

ERP de software libre en pymes

Además habremos de asegurarnos que es posible una implementación

satisfactoria a largo plazo, es decir tenemos que averiguar si será posible que el

nuevo software supere al actual en funcionalidad y eficiencia. Para ello tendremos

que tener en cuenta todos los factores de riesgo que afectan a la efectividad de

los ERP, (en el capítulo 8 se puede ver toda la información al respecto), una vez

hecho esto determinaremos en qué medida suponen un riesgo para la

implementación, estudiar este riesgo y si a pesar de ellos la implementación es

viable.

En nuestro caso práctico podemos observar que al tener las tiendas en diferentes

localizaciones y guardar un registro de las compras de cada cliente es importante

mantener la consistencia de los datos, además de saber el inventario en todo

momento, por tanto el ERP será mejor herramienta que otras herramientas

tradicionales.

7.2 Definición de alcance y forma de operar

En esta fase se decidirá cómo la forma de llevar a cabo la implementación, se

determinará a qué áreas de la empresa va a afectar y cómo específicamente.

Tomaremos decisiones como los departamentos a los que afectará, el tipo de

arquitectura que elegiremos para nuestra red…

En definitiva tendremos que tomar una serie de decisiones sobre cómo se va a

realizar la implementación, estas son algunas de las más importantes:

7.2.1 Definición del proceso de operación de la empresa con la herramienta La primera decisión y más importante no nos corresponde a nosotros tomarla, se

trata de consultar con la empresa cuál será su futura forma de operar con la

104

---

<!-- Página 105 -->

ERP de software libre en pymes

herramienta y como quiere que sea su nuevo proceso de negocio para las

determinadas áreas de la empresas.

Será importante tener muy claro cómo quieren que sean los nuevos procesos de

operación de la empresa, pues luego una vez implementado, si se encuentra algún

fallo será muy difícil de corregir, o explicar a la empresa que no puede hacer las

cosas como esperaba.

Es habitual que en este punto sobre todo las pequeñas y medianas empresas, no

tengan claro del todo que es lo que quieren, es nuestro trabajo también

asesorarlos y ayudarles en el proceso de toma de decisiones para que escojan la

mejor opción.

7.2.2 Tipo de implementación

Uno de los factores que habremos de decidir será el tipo de implementación que

haremos, esto tendrá repercusiones en el alcance de la implementación y en los

empleados, ya que determinará la forma en que les afecta a estos, tenemos varias

opciones:

 Incremental por departamentos: Podemos ir incluyendo poco a poco los

diferentes departamentos en el ERP y viendo su evolución con el software

 Incremental topológica: también podemos incrementar la implementación

de estas de manera geográfica por delegaciones.

 Incremental funcional: Iremos incrementando la funcionalidad a cumplir

por el ERP poco a poco para así poder llegar al cumplimiento de todas las expectativas.

 Convivencia simultánea: Durante un periodo conviven los dos sistemas, y

al cabo de un periodo de tiempo suprimimos el sistema antiguo. En el caso

de los ERP esta implantación es particularmente difícil, ya que al tener dos

105

---

<!-- Página 106 -->

ERP de software libre en pymes

sistemas acceder sobre los mismos datos, puede que pongamos en peligro

la consistencia de los datos.

 Cambio total: hacemos un cambio completo en un corto periodo de

tiempo.

Dependiendo de cada situación haremos una implementación distinta, tendremos

que decidir cuál es la que más nos conviene según las situaciones particulares.

7.2.3 Arquitectura

Tendremos que decidir que arquitectura necesitaremos para nuestro ERP, esta

decisión viene determinada en gran parte por la arquitectura del propio ERP, pero nosotros siempre tendremos diferentes opciones a tener en cuenta.

Lo más habitual en los ERP es implementar un modelo de tres capas en red, en el

que tenemos por un lado la base de datos por otro el servidor con los programas y

por último diferentes interfaces para los empleados en red.

106

---

<!-- Página 107 -->

ERP de software libre en pymes

A parte de la implementación por capas dentro de esta tenemos diferentes

opciones, por ejemplo podemos hacer la instalación de la primera capa en el

mismo servidor y el interfaz en otro ordenador.

Otro modelo habitual sobre todo cuando tenemos que comunicarnos o proveer

servicios a través de la red WAN, es el de cuatro capas, este tiene una capa

adicional que es la capa de servicio, esta nueva capa permite no tener que pasar

por la capa de interfaz para determinados servicios:

(Guidance Share, 2010)

En la práctica se suele utilizar cuando comunicamos con servicios externos, como

pueden ser otras máquinas que realizan procesos de manera automática, y

queremos diferenciar o dar un acceso más directo a estos. También se suelen

utilizar si queremos proporcionar capas adicionales de seguridad para

comunicarnos a través de la red.

107

---

<!-- Página 108 -->

ERP de software libre en pymes

7.2.4 Decisiones respecto a hardware y accesibilidad

Habremos de tomar una serie de decisiones para satisfacer las necesidades de la

empresa respecto a su nueva forma de operar, dentro de este aspecto tendremos

que decidir:

 Qué tipo de equipos se requieren para la operación: aquí decidiremos qué

tipo de equipos se desean para determinadas operaciones, por ejemplo es

habitual en los POS/TPV tener una pantalla táctil o un lector de códigos de

barras.

 Accesibilidad a la herramienta: Dentro de esta decisión determinaremos

como se accederá a la aplicación: a través de una aplicación de escritorio,

navegador web, dispositivos móviles …

Para el caso práctico propuesto:

Lo que nos damos cuenta es que la empresa necesita de un servidor que contenga

la información que utilizarán los dos puntos de venta y el almacén en tiempo real,

estos además tendrán que estar sincronizados para que la información sea

consistente.

También renovarán los equipos actuales por unos con pantalla táctil que permitan

operar de manera más sencilla y rápida a los cajeros.

Elegiremos un modelo en tres capas, con un servidor de la empresa. Necesitarán

POS/TPV, para realizar las ventas. Necesitarán poder realizar la gestión de

almacenes y del stock con la herramienta. Se realizará un cambio total en el

cambio de ejercicio de la empresa.

108

---

<!-- Página 109 -->

ERP de software libre en pymes

7.3 Definición de acciones a realizar

En esta fase planificaremos las acciones a realizar para poder obtener una

implementación satisfactoria, definiremos que es en lo que consiste cada acción y

la fase o fases en que se realizarán.

En nuestro caso práctico describiremos las acciones que habremos de realizar:

 Planificación de las acciones y su situación en el tiempo

 Evaluación del equipo y asignación de roles

 Pruebas iniciales

 Instalación del hardware sala piloto y nuevo servidor

 Instalación software sala piloto

 Interacción empleados sala piloto

 Formación de los empleados en la sala piloto

 Migración de datos al nuevo servidor

 Instalación software ERP definitivo en el servidor y conexión con la base de datos

 Configuración del ERP

 Instalación de bibliotecas y configuraciones necesarias en equipos cliente

 Evaluación y pruebas

 Cambio efectivo del sistema antiguo al nuevo

 Seguimiento de la implementación

Es habitual que estas actividades se dividan en actividades menores para su mejor

entendimiento y planificación, pero en este caso haremos una descripción general

de estas.

7.4 Planificación para la realización de las acciones

En este punto planificaremos la realización del proyecto.

109

---

<!-- Página 110 -->

ERP de software libre en pymes

1. Estimaremos el coste de realización de las acciones: esto lo podemos

determinar mediante, la utilización de métodos de estimación de

ingeniería del software, o mediante la experiencia si es que la tenemos,

pero siempre asignando un coste a la realización de todas las acciones.

2. Estimación de los recursos necesarios para la realización de las acciones.

3. Planificación de la realización de las tareas asignando tiempo y recursos a

cada una de ellas

4. Seguimiento de la planificación, de esta manera sabremos en qué punto

nos encontramos del proyecto y las previsiones de futuro del mismo.

Es importante tener en cuenta que a pesar de tratarse de una implementación, al

ser tan grande habremos de tratarla como a cualquier otro proyecto, planificando

y haciendo un seguimiento de cada una de las fases de este.

7.4.1 Estimación del coste

Para poder hacer una buena estimación del coste de realización de las acciones,

podemos utilizar el método que queramos, una de las opciones es utilizar

métodos de estimación de las metodologías ágiles, ya que son más generalistas

que los tradicionales, se basan en la experiencia y se pueden adaptar mejor a

nuestro caso en que las tareas no tienen por qué conllevar la realización de código.

Lo primero que debemos hacer es descomponer estas acciones en tareas menores

de manera que podamos hacernos una idea de su duración o complejidad,

110

---

<!-- Página 111 -->

ERP de software libre en pymes

después algunos de los métodos de estimación que podemos utilizar son:

planning poker, diagramas pert, complejidad por puntos de historia…

7.4.2 Estimación de los recursos necesarios

Al igual que al estimar los costes, nos ayudará la descomposición en tareas

menores para así saber que recursos necesitamos para la realización de cada

acción, los recursos necesarios a veces se especifican de manera estricta por la

acción que vayamos a y en otros casos podremos asignar los recursos que

deseemos.

7.4.3 Planificación de la realización de las acciones

Aquí al igual que antes podemos utilizar el método que deseemos, desde la

planificación adaptativa de metodologías tipo SCRUM hasta la planificación

tradicional. Cuanta más experiencia tengamos mejores serán las estimaciones del

coste de las tareas.

7.4.4 Seguimiento de la planificación

Habremos de hacer un seguimiento del trabajo realizado respecto a la

planificación planteada para saber en qué punto nos encontramos del proyecto y

la estimación de lo que vamos a tardar en completarlo.

Para realizar el seguimiento de nuevo podemos recurrir a distintas herramientas

como son: dashboards con el seguimiento de las tareas, diagramas de valor

ganado, diagramas de Gantt, etc.

Caso práctico

En nuestro caso haremos una estimación a modo de ejemplo. Sería más

conveniente hacer una estimación con algún método real de ingeniería del software.

111

---

<!-- Página 112 -->

ERP de software libre en pymes

Para describir la planificación que hemos realizado utilizamos Microsoft Project:

se puede ver la estructura en el anexo 2.

7.5 Formación del equipo

Tenemos que elegir un buen equipo de profesionales e informarles del plan a

seguir, es habitual, hacer una reunión con todo el equipo antes de comenzar el

proyecto para informarles de las acciones que se van a llevar a cabo y evaluar los

conocimientos de estos. Una vez que sabemos la calidad de nuestro equipo

determinaremos si necesitamos más ayuda o podemos trabajar de manera

satisfactoria.

Si alguno de los empleados necesita aprender a utilizar la herramienta lo más

recomendable es formarles antes de comenzar la implementación.

Se le asignará un rol a cada empleado, es importante desde un principio dejar

claro el papel de cada persona en el proyecto, asignaremos estos roles en función

del trabajo a realizar y la experiencia del trabajador.

Por último repartiremos el trabajo entre los miembros del equipo según se haya

especificado en la planificación.

7.6 Prueba inicial

Es importante hacer una prueba de instalación en una máquina virtual u otro

medio aislado para comprobar la utilización del sistema con el ERP, en esta fase

podemos hacer múltiples pruebas con los distintos tipos de ERP, para así poder determinar cuál es la mejor opción para nosotros, saber si podremos proporcionar

112

---

<!-- Página 113 -->

ERP de software libre en pymes

las funcionalidades acordadas y mantener los niveles de servicio previstos.

(Hessman, 2013)

En cuanto a la elección del ERP tendremos que tener en cuenta todos los

requisitos que se nos han dado, y los que nos vienen dados debido a las

limitaciones de la instalación. En función de estos requisitos escogeremos el

software más adecuado, y evaluaremos si tendremos que realizar alguna acción

adicional como la adición de funcionalidad a la aplicación para poder satisfacer las

necesidades del cliente.

En nuestro caso práctico al probar observamos que con el software Openbravo se

obtienen los mejores resultados en la prueba, cumple todas las necesidades del

cliente.

7.7 Adaptación del ERP a las necesidades de la empresa

Es habitual en este punto darnos cuenta que el software puede que no cumpla

ciertas necesidades de las empresas para ello, prácticamente todos los ERP

disponen de un API que nos permite programar sobre ellos y añadir nuevas

funcionalidades al sistema, de esta forma desarrollaremos la solución a implantar

que se adapte a las necesidades del cliente.

En nuestro caso real supondremos que el software genérico cumple todas sus

necesidades.

7.8 Instalación del software esencial y sala piloto

Será importante al principio hacer una implementación limitada en la que

haremos una pequeña simulación aislada del sistema, dispondremos del sistema

113

---

<!-- Página 114 -->

ERP de software libre en pymes

similar al que se hará cuando hagamos la instalación completa pero en un entorno

aislado y a prueba de fallos.

Una vez que tengamos la sala piloto configurada, haremos las pruebas pertinentes

en la sala, podremos detectar posible errores no detectados en la prueba inicial.

En este punto suele hacerse la instalación del servidor o servidores que se

utilizarán en el futuro sistema, y se hace la instalación básica del software, para así

poder evaluar el funcionamiento del futuro sistema.

Esta sala piloto tendrá otro uso fundamental, que será la formación de los

empleados de la empresa cliente, mediante esta sala tendrán la posibilidad de

acceder nuevo software y empezar a familiarizarse con él.

Esta interacción usuario sistema también nos ayudará en la detección de errores

al interactuar el usuario con la herramienta y poder corregirlos en una fase

temprana.

7.9 Migración de datos

Una vez que hemos hecho las pruebas del sistema y evaluado y corregido sus

errores, lo que haremos será comenzar con la implementación del sistema

definitivo, el primer paso será hacer los datos accesibles para el nuevo software,

probablemente tengamos que hacer una migración de la antigua base de datos a

una nueva.

La migración de los datos es una de las partes más críticas del proceso ya que la

información de la empresa suele ser muy sensible y valiosa. Por ello lo que

haremos será crear la nueva base de datos conservando siempre la antigua, y

después de un periodo de tiempo, cuando sepamos que no hay problemas en la

integridad de los datos, podremos hacer el cambio definitivo.

114

---

<!-- Página 115 -->

ERP de software libre en pymes

En nuestro caso explicaremos las diferentes opciones mediante el escenario del

cliente, este quería pasar de su antigua base de datos en Access 2000 a una en

Mysql, pero en el resto de migraciones el funcionamiento es similar, y tendremos

prácticamente las mismas opciones.

Para hacer las migraciones tenemos varias opciones:

Una opción será con una aplicación de migración si la nueva base de datos a la

que nos migramos dispone de ella, estas aplicaciones las hay que generan un

archivo .sql y también las hay que se comunican con las dos bases de datos y

hacen el volcado automáticamente, normalmente las proveen las bases de datos

de destino a las que nos vamos a migrar, pero también hay repositorios de

herramientas genéricos.

También podemos generar un archivo de texto por tabla, en el que los campos

están separados por símbolos, si el anterior sistema gestor de la base de datos nos

lo permite, en este caso Access también permite esta opción, el problema será

que solo migraremos datos y no migraremos otros elementos de configuración de

la base de datos como pueden ser los triggers por ejemplo, teniendo que hacer

todo este trabajo a mano.

De igual manera que utilizamos los archivos de texto también podremos hacer

mediante hojas de cálculo.

Elegiremos la función más conveniente en función de nuestro caso.

7.9.1 Migración mediante archivo de texto .txt

1 Lo que haremos será seleccionar cada una de las tablas y generar con ellas

un archivo de texto, para ello la herramienta Access nos permite exportar

como archivo de texto indicando los símbolos que queremos en nuestro caso el más adecuado es la configuración Unicode. (Microsoft, 2014)

115

---

<!-- Página 116 -->

ERP de software libre en pymes

2 Una vez que tenemos todas las tablas en archivos de texto habrá que

introducir cada uno de los datos en la nueva base de datos Mysql. Para ello

con el comando LOAD DATA indicando el separador de campo y el

separador de fila. Puede que en este paso tengamos problemas por el

formato de introducción de determinados campos como pueden ser las

fechas, si es el caso en el archivo de texto reemplazaremos este formato

con cualquier editor de texto que nos permita reemplazar.

Aquí se puede ver un ejemplo del uso del comando load data:

LOAD DATA [LOW_PRIORITY | CONCURRENT] [LOCAL] INFILE 'file_name.txt'

[REPLACE | IGNORE]

INTO TABLE tbl_name

[FIELDS

[TERMINATED BY ' ']

[[OPTIONALLY] ENCLOSED BY '']

[ESCAPED BY '\' ]

]

[LINES

[STARTING BY '']

[TERMINATED BY ' ']

]

[IGNORE number LINES]

[(col_name,...)]

7.9.2 Migración mediante el programa administrador de la nueva base de datos En nuestro caso revisaremos evaluando el programa de administración de bases

de datos PhpMyAdmin, se trata de un una herramienta de software libre escrita

116

---

<!-- Página 117 -->

ERP de software libre en pymes

en PHP, que nos permite administrar las bases de datos MySQL por medio de una

interfaz web (PhpMyAdmin).

Es una herramienta muy conocida y ampliamente utilizada, actualmente se

encuentra en multitud de idiomas y es la mejor opción para las personas no

iniciadas en las bases de datos ya que utiliza un entorno visual muy intuitivo que

nos permite trabajar evitando usar una consola.

Por el contrario tiene la desventaja de que no soporta toda la funcionalidad que

soporta el sistema tradicional, y posiblemente el manejo sea más rápido en

consola si tenemos conocimientos sobre bases de datos relacionales.

Para poder hacer la migración sobre la base de datos utilizando PhpMyAdmin

como método para introducir los datos en la nueva base de datos MySQL lo que

haremos será:

1 Exportaremos las tablas de la base de datos a tablas de hojas de cálculo

Excel, es muy posible que encontremos conflictos en los tipos de datos,

para solucionarlos existe una guía en la página de soporte de Microsoft

(Microsoft Office, 2014)

2 Una vez hecho esto abriremos las tablas de cálculo y las guardaremos

como hojas de cálculo de licencia libre (formato .odt), en este paso

probablemente encontremos menos problemas, ya que no debería haber

problemas con los tipos de datos.

3 Por último abriremos la interfaz de PhpMyAdmin y seleccionaremos la

opción de importar dentro de más opciones.

117

---

<!-- Página 118 -->

ERP de software libre en pymes

1 Una vez aquí lo que haremos será seleccionar el campo de hoja de cálculo

de open document y el archivo a abrir.

2 Una vez hecha la importación tendremos que definir las claves primarias

en la base de datos importada, ya que esta información no se refleja en las

hojas de cálculo.

3 También tendremos que corregir el valor de las fechas actualizando los

valores de string al tipo date, para ello haremos un:

UPDATE usuarios SET fechanueva=STR_TO_DATE(fechanacimiento, ‘%Y/%m/%d’);

4 Procederemos de manera similar con los valores booleanos los cuales

también tendremos que actualizar.

UPDATE usuarios SET fumadornuevo=true where fumador=’VERDADERO';

118

---

<!-- Página 119 -->

ERP de software libre en pymes

UPDATE usuarios SET fumadornuevo=false where fumador=’FALSO';

7.9.3 Migración mediante asistentes

La opción de utilizar un asistente probablemente sea la mejor opción si existe un

software especialmente para ello y si lo hemos probado y sabemos que funciona.

Este tipo de software también tiene la ventaja de que facilita el cambio

enormemente cuando funciona bien, ya que nos permite hacer el cambio más

rápido y con menos complicaciones.

Los asistentes suelen estar disponibles por parte de las diferentes bases de datos

para facilitar la migración a ellas, por ejemplo para el caso de IBM está disponible

el IBM migration toolkit con el que podemos hacer migraciones a la base de datos

de IBM (IBM Develorper Works, 2014).

Existe el mismo software por parte de Microsoft SQL Server tiene un asistente

gratuito que nos permite hacer el cambio desde Mysql (Microsoft Download

Center, 2014).

Oracle También tiene su software equivalente el Oracle SQL Developer (Oracle

software network, 2014).

En el caso que nos ocupa es el de Mysql y para él también existe una herramienta

de migración MySQL Migration Toolkit (Mysql Downloads, 2006) pero ha sido

descatalogada, ha sido reemplazada por MySQL Workbench (Mysql Workbench,

2014) una herramienta más completa que permite manejar las migraciones

además de otros elementos de la base de datos, se parece a PhpMyAdmin.

Dentro de esta herramienta podemos encontrar el asistente para las migraciones

119

---

<!-- Página 120 -->

ERP de software libre en pymes

7.9.4 Opción de no realizar la migración

Otra opción que tenemos es no realizar la migración de nuestra base de datos, lo

que haremos será instalar la nueva base de datos y comunicarla con la antigua

para ello podemos utilizar un pool para la base de datos.

Esto nos permite no realizar la migración y acceder a los datos dentro de la base

de datos antigua desde una nueva, siendo esta nueva la que comunica con la

aplicación. Dentro de estas opciones una de ellas es ODBC

120

---

<!-- Página 121 -->

ERP de software libre en pymes

Para poder empezar con la migración, lo que haremos será:

1. Instalar la nueva base de datos que interactuará con la aplicación. En

nuestro caso Mysql

2. Instalar el Mysql connector/ODBC. Es un archivo de drivers que nos

permitirá utilizar ODBC.

3. Después creamos el nuevo origen de datos, en nuestro caso como estamos

utilizando Windows Server 2003 será en herramientas administrativas

nuevo origen de datos ODBC.

121

---

<!-- Página 122 -->

ERP de software libre en pymes

4. Posteriormente vinculamos la base de datos Mysql, al nuevo origen de

datos creado, para ello utilizamos el Mysql connector/ODBC tiene un

asistente que nos permitirá hacer la vinculación de manera automática.

(Mysql Comunity , 2014)

122

---

<!-- Página 123 -->

ERP de software libre en pymes

5. Podremos hacer también el proceso inverso, si lo deseamos haremos la

migración a la nueva base de datos y mediante ODBC les damos soporte

para la antigua forma de operar. Para ello vincularemos la herramienta

Access al origen de datos ODBC desde Datos externos>Base de datos

ODBC>Vincular>base de datos desde sistema. (AJDB soft, 2011)

123

---

<!-- Página 124 -->

ERP de software libre en pymes

(AJDB soft, 2011)

Podemos optar por este tipo de solución durante el periodo de integración, si

vemos que todo funciona bien con la nueva base de datos siempre podremos

hacer el cambio de manera definitiva a la nueva base de datos, además es

beneficioso para los empleados tener un periodo de adaptación en el que pueden

seguir usando el antiguo sistema de acceso, aunque es posible que este tipo de

configuración cree problemas en la coherencia y consistencia de los datos.

7.9.5 Comprobando la integridad

Es fundamental que después de realizar la migración comprobemos la integridad

de los datos, como sabemos es uno de los recursos más importantes de la

empresa.

124

---

<!-- Página 125 -->

ERP de software libre en pymes

Podemos hacerlo de manera manual: haciendo diferentes consultas para

contabilizar número de campos, datos que nos pueden dar problemas como las

fechas o valores booleanos, una vista de la tabla a ver si hay algún problema…

También podemos utilizar herramientas de mantenimiento: como las que ofrece

Microsoft para su base de datos relacional, pero este tipo de software suele ser

más difícil de encontrar.

7.9.6 Caso de los ERP

Estamos hablando de la necesidad de las migraciones en cuanto a lo que la

utilización de los ERP se refiere pero hemos de tener en cuenta que puede que

esta migración no sea necesaria ya que estos suelen soportar varios tipos de bases

de datos.

Si no es así tendremos que hacer la migración de datos, y tendremos que escoger

el método que más se adapte a nuestro caso de los estudiados.

7.10 Instalación hardware

En este paso instalaremos todo el hardware necesario para una completa

implementación del ERP, dispondremos la arquitectura planificada y

conectaremos toda la red de equipos.

Una vez hecho todo esto estaremos listos para realizar la instalación del sistema.

125

---

<!-- Página 126 -->

ERP de software libre en pymes

7.11 Instalación del sistema ERP

Para realizar la instalación del sistema los ERP disponemos de diferentes

soluciones, como la instalación tradicional por componentes, SaaS o servidores

pre-configurados en una máquina virtual.

Dentro de la instalación del ERP se encuentran los servidores, los equipos de

acceso a la herramienta y los puntos de venta si es que existen.

En los equipos que accederán a la herramienta, habitualmente no tendremos que

instalar casi software, en el caso de que utilice una interfaz web, con el entorno

Java nos bastará, y si es una aplicación de escritorio, la instalación consistirá en

poco más que instalar la herramienta y sincronizarla con el servidor.

En el caso de los POS puede que se trate de un SO configurado como POS si

nuestro ERP es de mucha calidad, de una aplicación de escritorio como en el caso

de Openbravo e incluso en una interfaz web como en el caso de Odoo.

Cada una de ellas tiene sus ventajas e inconvenientes a continuación

estudiaremos cada una de ellas:

7.11.1 Servidor genérico en una máquina virtual

Con este tipo de instalaciones lo que hacemos es, una vez que tenemos el equipo

conectado a nuestra red local, virtualizamos un servidor dentro de este equipos

que nos permite asignar una parte específica de los recursos del equipo al

servidor.

Normalmente los servicios virtualizados con una instalación generalizada están

disponibles para descargar en las páginas. Otra opción es la de hacer una

instalación tradicional de todos los componentes por separado en una máquina

virtual.

126

---

<!-- Página 127 -->

ERP de software libre en pymes

Ventajas

 Acortan notablemente el tiempo de instalación sobre todo si virtualizamos

una máquina genérica.

 Es un buen tipo de instalación para hacer las pruebas iniciales en el

software, sobre todo los paquetes preinstalados, ya que en un tiempo muy

pequeño nos permiten ver y comparar las funcionalidades generales del

sistema con respecto a otros.

 Definimos específicamente los recursos asignados al ERP

 Permite un sistema de copias de seguridad más sencillo

 Se pueden migrar fácilmente a otras máquinas.

 Los fallos en el SO de la máquina virtual no afectarán a nuestro sistema.

127

---

<!-- Página 128 -->

ERP de software libre en pymes

Inconvenientes

 Si instalamos los paquetes genéricos no podemos decidir qué módulos

queremos instalar y cuáles no, además no son escalables ya que no es

habitual que podamos añadir módulos con más funcionalidades.

 No tenemos acceso directo para poder modificar la base de datos y operar

directamente con el servidor de esta por lo que el manejo de la

consistencia y migración de los datos ha de hacerse a través del ERP lo cual

es mucho más complicado.

 La instalación de actualizaciones se complica mucho, o se hace imposible

ya que puede que no tengamos soporte para actualizar el paquete

instalado.

Conclusiones

Se tratará de un sistema adecuado siempre que queramos hacer pruebas,

comprobar las funcionalidades, interfaz y demás características del software. Pero

no se trata de la elección más adecuada para una instalación funcional completa.

7.11.2 Instalación tradicional

Esta es la instalación más habitual en el caso de los ERP en las grandes empresas,

en este caso definiremos una arquitectura clara para el sistema y lo

implementaremos en nuestra red.

Tendremos cada uno de los componentes o capas que formarán nuestro sistema

por separado. Poco a poco iremos instalando, configurando e integrando cada uno

de ellos.

La arquitectura más habitual en un entorno real es un entorno en tres capas, por

ello la instalación tradicional puede que sea la mejor opción, ya que nos permite

configurar cada una de las capas del software y nos da acceso a ellas.

128

---

<!-- Página 129 -->

ERP de software libre en pymes

129

---

<!-- Página 130 -->

ERP de software libre en pymes

Instalación de la capa de datos

En esta fase instalaremos y configuraremos la base de datos que vamos a utilizar

en el sistema.

Lo primero que deberemos hacer es instalar la base de datos y migrar los datos si

no lo hemos hecho, una vez hecho esto podemos pasar al siguiente paso.

Instalación de la capa de servicio

En la capa de servicio se encontrará el software que nos proporcionará la

funcionalidad, para ello tendremos que instalar el ERP como tal, el proceso para

ello dependerá completamente del SO de del software a instalar.

Probablemente además de la aplicación tendremos una serie de bibliotecas y

herramientas que tendremos que instalar también, algunas de las más habituales

son:

 Apache Ant: nos permitirá ejecutar archivos de configuración para poder

automatizar este proceso.

 Tomcat/Apache: el servidor web nos permitirá proporcionar una interfaz

segura a través del navegador

 Librerías de Java: permitirán ejecutar la aplicación si esta está construida

sobre Java

 Librerías de Python: permitirán ejecutar la aplicación si esta está

construida sobre Python

Además de la instalación del ERP es habitual en este punto hacer la integración

con la base de datos y configuración del ERP

Instalación de la capa de usuario

En la capa de usuario, usualmente tenemos dos opciones:

 La interfaz se proporciona a través del navegador web, en este caso solo

tendremos que instalar las librerías correspondientes como puede ser Java

130

---

<!-- Página 131 -->

ERP de software libre en pymes

JRE por ejemplo que permiten una mayor funcionalidad a través del

navegador web.

 La interfaz se provee a través de una aplicación de escritorio, en este caso

instalaremos la aplicación y librerías necesarias y sincronizaremos la

aplicación con el servidor

Integración de las tres capas

Las tres capas pueden encontrarse separadas o juntas, lo más habitual es que al menos la capa de datos y de servicio se encuentren en la misma máquina física

sobre todo en las pequeñas empresas.

En cuanto a la integración de las tres dependerá del software que instalemos pero normalmente tendremos que:

 Comunicar la base de datos con el programa ERP

 Proporcionar y configurar un servidor web para poder comunicar los

equipos de la red con el servidor de aplicación

 Configurar el sistema en general para que se ajuste a nuestras

necesidades.

En este paso es muy habitual utilizar herramientas que nos ayudan a no tener que

hacer la configuración de manera manual como puede ser Ant, esta herramienta

reduce el tiempo de configuración al ejecutar scripts de configuración que

normalmente nos proporcionan los desarrolladores de los productos.

Ventajas

Nos permite una configuración completa del sistema y poder configurar el sistema

libremente.

Nos permite añadir funcionalidades específicas al software dentro de nuestro

sistema interno a diferencia de los paquetes y el SaaS

Permite hacer una migración más segura y eficiente de la base de datos.

131

---

<!-- Página 132 -->

ERP de software libre en pymes

Al ser nosotros los que configuramos el sistema podemos hacerlo de acuerdo a las

necesidades de nuestra empresa y por lo tanto adaptarlo de una manera más

adecuada.

Permite un ahorro de recursos a diferencia de los paquetes virtualizados al estar

instaladas sobre el sistema operativo básico y no sobre otro sistema operativo o

hipervisor.

La seguridad del sistema la establecemos nosotros, al tener configuración total

sobre el sistema podremos establecer los protocolos y sistemas de seguridad que

deseemos.

Nuestros datos no se encuentran en servicios de almacenamiento ajenos como

puede ser el caso del SaaS

Inconvenientes

Nosotros tendremos que hacer el mantenimiento del sistema.

La instalación es más compleja que la de los paquetes ya construidos.

Será necesaria una mayor inversión de tiempo y recursos para poder garantizar

unas cuotas mínimas de servicio.

Habremos de mantener al menos un servidor físico siempre operativo dentro de

la empresa.

Conclusiones

Esta instalación es la más habitual ya que es la única en la que nosotros tenemos

control completo sobre el sistema y por tanto la mejor opción siempre que

dispongamos de los suficientes recursos y queramos una aplicación que se adapte más a nuestra empresa.

132

---

<!-- Página 133 -->

ERP de software libre en pymes

Si nos conformamos con una aplicación genérica y los datos de la empresa no

tienen demasiada complejidad puede que encontremos opciones mejores.

Instalación en medios virtuales

También podemos optar por hacer una instalación tradicional dentro de una

máquina virtual, tendremos las ventajas y desventajas de esta y podremos tener

acceso a una configuración total sobre el sistema.

7.11.3 Utilización de SaaS

En este caso no tendremos que hacer ninguna instalación ni en la capa de servicio

ni de datos, ya que esta parte de la arquitectura nos la proporciona el proveedor

contratado.

Las ventajas e inconvenientes podemos encontrarlos en la sección SaaS del primer

capítulo.

7.11.4 Caso práctico

En el caso práctico como comentamos antes optaremos por la instalación de

Openbravo en una arquitectura de tres capas en un servidor local.

En nuestro caso el servidor será específicamente una instalación tradicional sobre

una máquina virtual de un servidor Ubuntu.

Lo primero que haremos será instalar el SO en la máquina virtual, una vez hecho

esto podemos comenzar la instalación:

Primero instalaremos Python que es el lenguaje de programación utilizado en

Openbravo.

sudo apt-get install python-software-properties

133

---

<!-- Página 134 -->

ERP de software libre en pymes

Activamos el paquete de archivos personal de Openbravo

sudo add-apt-repository ppa:openbravo-isv/ppa

Actualizamos el sistema

sudo apt-get update

Realizamos la instalación mediante el comando apt-get, existente en el repositorio

Linux.

$ sudo apt-get install openbravo-3

Una vez hecho esto podemos comprobar que la ejecución del ERP en nuestro

servidor es satisfactoria con la ejecución del comando top.

Podemos ver como esta versión de Openbravo que incluye todo el software

necesario para poder realizar la instalación, incluyendo la base de dato Postgre, el

servidor Apache, y las librerías necesarias para la configuración.

Una vez terminado podemos ver que el software estará listo para utilizar,

podremos empezar a configurar nuestro sistema para poder hacer una utilización

efectiva para la empresa

134

---

<!-- Página 135 -->

ERP de software libre en pymes

7.12 Evaluación y pruebas del software instalado

Una vez que hemos realizado una instalación funcional completa será importante

comprobar que cumple con todos los acuerdos de servicio especificados.

Para ello haremos pruebas de utilización en el límite, disponibilidad frente a caídas, pruebas de seguridad…

7.13 Formación de los empleados

Esta fase, será de carácter esencial para el éxito de la implementación consistirá

en la formación de los empleados en el uso de la herramienta. Si no ofrecemos

esta formación lo más habitual es que los empleados no sean tan eficientes como

deberían y en ocasiones pueden incluso dejar de utilizar la herramienta.

A pesar de estar colocada en esta fase es recomendable realizarla a la vez que

estamos realizando la implementación, y así damos la oportunidad de que los

empleados aprecien como se va realizando, además nos permite detectar posibles

necesidades en los empleados que los gerentes desconozcan y que ayuden a

obtener un éxito en la implementación.

A continuación existe una guía que puede ayudar en este proceso tan crítico:

7.13.1 Guía para la formación de un equipo en el uso de ERP

A pesar de que cada vez los ERP son más usables y cada vez más fáciles de

entender, la formación de los empleados es uno de los mayores factores de riesgo

en la implementación de los ERP, puede suponer el 10% al 20% del presupuesto

de la implementación, por tanto será importante tener apoyo de la alta dirección

135

---

<!-- Página 136 -->

ERP de software libre en pymes

para que se puedan satisfacer las necesidades tanto de presupuesto como de

implicación por parte del personal. (Nastase, 2012)

Tendremos que tener en cuenta una serie de factores a la hora de formar a los

empleados:

1. Empezaremos el programa de formación analizando las necesidades de

los empleados. De esta manera sabremos en qué áreas tenemos que

formar a cada empleado, cómo podemos hacerlo y los recursos que

necesitaremos para poder hacerlo.

2. Los empleados han de conocer por qué se les está formando;

habremos de explicarles los beneficios y objetivos del entrenamiento

en la herramienta.

3. Ajustar los contenidos de enseñanza a las competencias del empleado;

esto será importante pues dependiendo del rol que cumpla el

empleado en la empresa necesitará una formación específica en un

área de funcionalidad del ERP.

4. Ajustar la formación a medida que llevamos a cabo la implementación;

si hacemos esto podremos planificar la formación de manera que los

problemas que surjan de la diferencia de tiempo entre la formación de

los empleados y la instalación del ERP, puedan ser solucionados antes

de la finalización de la instalación del ERP. También si optamos por

formar a los empleados de manera precoz, podremos detectar posibles

problemas con la usabilidad de la herramienta antes de la fase de

producción del ERP.

5. Presupuestar la formación; el coste de la formación vendrá dado por los métodos de enseñanza que utilicemos y por las competencias del

personal al que formamos.

6. Evaluación de la enseñanza; igual que en cualquier otra parte del

proceso de implementación, habremos de tener una evaluación del

136

---

<!-- Página 137 -->

ERP de software libre en pymes

trabajo que estamos realizando, así sabremos si estamos formando de

manera adecuada a los empleados.

7. Elegir el método de formación más adecuado; en función de las

personas a las que estemos formando, tendremos que escoger una

serie de métodos de enseñanza.

Elección del método de formación más adecuado

A la hora de la elección de método habremos de analizar a nuestros alumnos y

elegir el método más acorde a sus necesidades, para ello podemos utilizar el

modelo de Kolb.

Características delCaracterísticas delCaracterísticas delCaracterísticas del

alumno convergentealumno divergentealumno asimiladoralumno acomodador

Pragmático Sociable Poco sociable Sociable

137

---

<!-- Página 138 -->

ERP de software libre en pymes

Racional Sintetiza bien Sintetiza bien Organizado

Analítico Genera ideas Genera modelos Acepta retos

Organizado Soñador Reflexivo Impulsivo

Buen discriminador Valora la comprensión Pensador abstracto Busca objetivos

Orientado a las Orientado a la tarea Orientado a la reflexión Orientado a la acción personas

Disfruta aspectosDependiente de los Espontáneo Disfruta la teoría técnicos demás

Gusta de laDisfruta el Disfruta hacer teoría Poca habilidad analítica experimentacióndescubrimiento

Es poco empático Empático Poco empático Empático

Hermético Abierto Hermético Abierto

Poco imaginativo Muy imaginativo Disfruta el diseño Asistemático

Buen líder Emocional Planificador Espontáneo

Insensible Flexible Poco sensible Flexible

Deductivo Intuitivo Investigador Comprometido

(Zazueta, 2009)

En él se dividen las personas en cuatro tipos, les clasificaremos según su forma de

reaccionar ante nuevos conceptos o problemas. En función de eso tendrán unas

características más acusadas que otras, en la siguiente tabla podemos ver las

características de cada grupo.

Una vez que hemos clasificado a las personas diseñaremos el plan de manera que

podamos ofrecer la formación lo más personalizada posible, de todas maneras es

habitual que en un determinado área de conocimiento las personas se clasifiquen

de manera similar en el gráfico (Nastase, 2012).

138

---

<!-- Página 139 -->

ERP de software libre en pymes

Una vez que sabemos qué clase de alumnos tenemos podremos escoger los

métodos de enseñanza más adecuados:

 Convergentes: En su caso lo mejor será un enfoque práctico, trabajar

directamente con el ordenador, otras opciones factibles para ellos son:

discusiones en grupo, simulaciones, asesoramiento online, pruebas y

participación en clase.

 Asimilador: Para ellos lo mejor serán libros y material de estudio, también

se puede utilizar formación práctica y materiales en línea.

 Divergente: Este grupo preferirá las clases tradicionales, pero se pueden

utilizar métodos alternativos como libros y material de estudio, asistencia

particular y formación práctica.

 Acomodador: Para este grupo lo mejor será también la formación práctica,

delante del ordenador, otras opciones son simulaciones, juegos y prácticas

en grupo. (Nastase, 2012)

Lo que podemos darnos cuenta es de que una de las mejores opciones es la

formación práctica en el ordenador pues es si no la mejor válida para todos los

grupos de personas, con mayor o menor eficacia.

7.14 Proceso de adaptación y mejora continua

Una vez que hemos realizado todos estos pasos, será importante hacer un

seguimiento del uso de la herramienta durante un tiempo y detectar los

problemas que se están encontrando.

Si es posible solucionaremos estos problemas estos problemas de manera que

aumentemos el uso y eficiencia de la aplicación.

139

---

<!-- Página 140 -->

ERP de software libre en pymes

7.15 Finalización del proyecto

Por último la finalización del proyecto, en el caso de los ERP la finalización de la

implantación no está claramente definida, a diferencia de otros proyectos, lo más

adecuado será hacer un seguimiento y mejora continua, detectando las

necesidades de la empresa y adaptando el software a ellas. El soporte y

mantenimiento es una parte esencial en el éxito del funcionamiento de los ERP.

140

---

<!-- Página 141 -->

ERP de software libre en pymes

# Capítulo 8: Factores que influyen

# en la efectividad de los ERP

141

---

<!-- Página 142 -->

ERP de software libre en pymes

## 8 Capítulo 8: Factores que influyen en la efectividad de

## los ERP

Hay muchos factores que pueden determinar el éxito o el fracaso a la hora de

implementar los ERP, algunos de estos factores habrá que tenerlos en cuenta a la

hora de la implementación, pero otros en cambio serán cruciales en fases posteriores.

Esencialmente el éxito de la implementación recae sobre los consultores ya que

son los encargados de instalar y mantener el nuevo sistema, pero también hay

142

---

<!-- Página 143 -->

ERP de software libre en pymes

otros implicados que tendrán que esforzarse para que la efectividad del sistema

sea máxima.

Hay seis factores que se deben cumplir para que la implementación del ERP sea

efectiva:

Soporte del consultor: los consultores son la parte más importante del cambio ya

que ellos son quienes poseen el conocimiento técnico para poder llevarlo a cabo,

los consultores han de estar comprometidos a dar un buen servicio, si no será

imposible realizar una implementación efectiva, son los encargados de hacer que

se produzcan todos los factores siguientes.

Comunicación efectiva: la comunicación es esencial en el proceso de la

consultoría, cuanto más se entiendan el consultor y el cliente mejor se satisfarán

las necesidades de este y por tanto haremos una implementación más efectiva.

Con una comunicación efectiva además generamos confianza entre la empresa

consultora y los clientes por lo que la resolución de conflictos será más sencilla.

Resolución de conflictos: si la implementación de cualquier programa suele

generar conflictos, la implementación de un ERP es particularmente problemática

ya que es particularmente larga, lo que debemos asumir es que es normal que

surjan discrepancias y solucionarlas de la mejor manera posible.

Transferencia de conocimiento: es prioritario que exista una transferencia efectiva

de conocimientos entre los consultores y el entorno de la compañía, de esta

manera se podrán obtener todas las ventajas de este ERP.

Soporte por parte de la alta dirección: es de vital importancia que la alta dirección

de la empresa apoye el cambio ya que ellos son los que pueden dar: el soporte, atención, recursos y autorización necesaria para que la implementación prospere.

Además son los que deben adaptar el cambio a las nuevas prácticas de la empresa

y preparar a los empleados para usar la nueva tecnología.

143

---

<!-- Página 144 -->

ERP de software libre en pymes

Soporte por parte del usuario: el usuario es el principal actor que interactúa con la

herramienta, si este reniega del cambio será imposible hacer una trasferencia de

conocimiento efectiva. Por ello habremos de recordarle las ventajas del cambio. Si

no conseguimos hacer ver las ventajas al usuario el aprendizaje por parte de este

será tarea imposible.

(Maditinos, Chatzoudes, & Tsairidis, Factors affecting ERP system implementation

effectiveness, 2012)

144

---

<!-- Página 145 -->

ERP de software libre en pymes

# Capítulo 9: Plan de empresa

145

---

<!-- Página 146 -->

ERP de software libre en pymes

## 9 Capítulo 9: Plan de empresa

Ahora vamos a proponer el caso de una empresa de consultoría que se especialice

en la consultoría de freeware para pymes. En este plan de empresa vamos a

estudiar aspectos como el producto, el mercado, el coste, la financiación, etc.

El pan de empresa lo vamos a realizar según las directrices del DGIPYME

(Dirección General de Industria de la Pequeña Y Mediana Empresa) (DGIPYME,

2014).

9.1 Datos básicos de la empresa

 Nombre: FERP.

 Domicilio social: Calle Carmen 43 San Martin de la Vega.

 Tipo de sociedad: Sociedad limitada nueva empresa.

 Sector de actividad: Servicios a empresas.

 Capital social: 3000euros.

9.2 Datos básicos del producto

 Explicación breve de la actividad a desarrollar: Se tratará de una

consultoría especializada en ERP del tipo freeware.

 Financiación Propia: 15.000.

 Financiación Ajena: 15.000.

146

---

<!-- Página 147 -->

ERP de software libre en pymes

9.3 Promotores

 Nombre del promotor: Roberto González.

 Puesto: Directivo.

 Dedicación: Estará desde el principio, trabajará tanto de directivo

como de técnico y se irá desplazando según crezca la empresa al área

directiva.

 Historia profesional: Un año de trabajo en la universidad Carlos III

como becario.

9.4 Productos y servicios

 Nombre: Implementación de ERP.

 Descripción: Este servicio incluirá todo el proceso de implementación de

un ERP en una pequeña o mediana empresa. Será diferente en el caso del

escenario económico tradicional que ofrecerá un servicio integral con una

instalación on-site y del de la Startup que ofrecerá un servicio de

implantación esencial.

 Nombre: Configuración de ERP.

 Descripción: Ayudamos a las empresas en la configuración de su entorno,

en puntos determinados de la implementación o cambio del ERP.

 Nombre: Nuevas funcionalidades ERP.

147

---

<!-- Página 148 -->

ERP de software libre en pymes

 Descripción: Adición de nueva funcionalidad a los ERP debido a

necesidades específicas de la empresa no reflejadas en el software

instalado.

 Nombre: Mantenimiento ERP.

 Descripción: Servicio de pago mensual, que dará asistencia técnica a las

empresas en el uso de los ERP y solución de problemas.

 Nombre: Alquiler de recursos.

 Descripción: alquiler de recursos informáticos, ya sean físicos (hardware) o

de la información (Espacios de almacenamiento remotos, servidores

remotos).

9.5 Plan de producción

Descripción de proceso productivo

Dependiendo del servicio que se ofrezca, se seguirá un método acorde con los

estándares del momento y de la forma más adecuada posible.

Sistemas de control y Gestión de calidad

En el caso de poder ser medible podemos determinar si una implementación es

exitosa por el porcentaje de uso de la aplicación se hará de esta manera,

en caso de que no sea posible se obtendrá un feedback de la empresa y de

los servicios ofrecidos, para ello se estudiará la satisfacción del cliente

mediante encuestas, uso de los servicios implantados, etc.

Tecnología utilizada

148

---

<!-- Página 149 -->

ERP de software libre en pymes

La tecnología utilizada será la acorde al momento y las necesidades del cliente,

siendo esencial la utilización de software tipo ERP y de equipos informáticos.

Instalaciones y maquinaria

Oficinas de pequeño tamaño así como equipos informáticos.

Proveedores

Comunidades y empresas dedicadas al desarrollo de software libre.

9.6 Análisis del mercado

 Aspectos generales del sector.

 Clientes potenciales: Los clientes potenciales son empresas de pequeño y

mediano tamaño que tengan alguna de las siguientes características:

o Tengan previsión de crecer

o Tengan sedes en diferentes puntos geográficos.

o Traten con multitud de clientes

o Incluyan en la misma empresa un proceso de producción y venta.

o Empresas que vayan a hacer un cambio de ejercicio en pocos

meses.

o Empresas que por su precio no pueden acceder a ERP de pago.

 Análisis de la competencia: El sector de consultoría sobre ERP dentro de

las tecnologías de SI es un sector bastante maduro y por lo tanto muy

competitivo, si bien es cierto que las empresas que se dedican de manera

específica a ofrecer servicios ERP freeware a PYMES son escasas.

149

---

<!-- Página 150 -->

ERP de software libre en pymes

9.6.1 Análisis DAFO

 Debilidades:

o Empresa nueva sin experiencia ni procesos definidos.

o Falta de personal experto en el estudio del proceso.

o Desconfianza de los clientes con respecto al freeware.

o Los ERP de software libre son accesibles para todo el mundo.

 Amenazas:

o Intrusismo por parte de otras consultoras en el campo del

freeware.

o Empresas de software de pago tipo SAP, antiguamente solo

orientadas al mercado de las grandes empresas, están creando

nuevos productos orientados especialmente para pymes.

 Fortalezas:

o Especialización en productos freeware que otras consultorías no

tienen.

o Introducción en el mercado de la consultoría freeware en un

momento muy temprano:

 Muy pocos competidores en el mercado español.

 Experiencia respecto a futuros competidores.

 Oportunidades:

o Precios competitivos con respeto a otras consultorías al acceder a

freeware.

o En las estadísticas del (INE, 2013) podemos ver como cada vez se

utilizan más las soluciones ERP de licencia libre.

150

---

<!-- Página 151 -->

ERP de software libre en pymes

o Exenciones fiscales al tratarse de una nueva empresa.

o Cada vez se crea más software de licencia libre por comunidades de

usuarios y empresas.

o El conocimiento y confianza en el software libre está creciendo.

o Las empresas tienden a diseminarse con el objetivo de ahorrar

costes.

o En el mercado actual cada vez es más necesaria la consistencia de

los datos en tiempo real.

o El Cloud Computing nos brinda la oportunidad de ofrecer ERP en

red acortando el tiempo de implementación.

9.7 Plan de marketing

Estrategia de precios

El producto se ofrecerá de manera gratuita, ya que su coste es de 0, pero se

cobrará por el trabajo realizado, como hemos visto la implementación de un ERP

es un proceso costoso e implica muchas horas por parte del consultor, de hecho

los honorarios de los consultores suponen alrededor del 50% de los costes de

implementación. (Redacción-Dataprix , 2014)

Instalando el software de licencia libre reduciremos alrededor del 35% el precio

final del producto sobre nuestros competidores (Redacción-Dataprix , 2014)

Política de ventas

Se ofrecerá el software de manera gratuita y se cobrará por el trabajo realizado

por los consultores de la empresa, así como servicios de mantenimiento y otros.

El precio de los de las horas de los consultores será el mismo para todas las

empresas independientemente de su tamaño.

151

---

<!-- Página 152 -->

ERP de software libre en pymes

Determinados servicios como mantenimiento y alquiler de equipos se cobrarán de

manera mensual.

Promoción y publicidad

El principal medio de difusión será internet, se utilizará SEO para darle mejor

visibilidad, de manera adicional se contratará Google Adds para dar visibilidad a la

empresa.

También se promocionará de manera telefónica con empresas que se sabe

cumplen una serie de condiciones y que les podría beneficiar el uso de ERP.

Esquema de distribución

La primera delegación se situará en Madrid, dada su situación geográfica y el

número de clientes potenciales.

El objetivo principal serán las empresas de pequeño y mediano tamaño, ya que no

tenemos capacidad operativa para dar servicio a empresas grandes.

Servicio post-venta y garantía

Dado que no se ha cobrado por la licencia de uso del producto, la garantía será

limitada.

En cuanto a servicio post venta se atenderán las solicitudes menores del cliente en

un plazo de seis meses a partir de entonces, todas las visitas serán cobradas.

Se ofrecerá también un servicio de mantenimiento previo pago.

9.8 Organización y personal

Equipo directivo

Director Gerente: Roberto González Román.

152

---

<!-- Página 153 -->

ERP de software libre en pymes

Plantilla de empresa

En el escenario tradicional:

3 Técnicos

1 Comercial

1 Administrativo

En el escenario Startup:

1 Técnico y trabajo por parte de los socios

Grupos de puestos de trabajo:

Técnicos: sus tareas serán dar los servicios que ofrece nuestra empresa a los

clientes.

Administrativo: Su tareas serán ocuparse de los aspectos financieros, legales y

administrativos de la empresa que no se externalicen.

Comercial. Su trabajo será traer nuevos clientes a la empresa.

9.9 Plan de inversiones

Inmovilizado material

Equipos informáticos

Mobiliario de oficina

Capital social 30000€ en escenario tradicional 5000 en Startup

Inmovilizado intangible

Licencias de software de pago.

153

---

<!-- Página 154 -->

ERP de software libre en pymes

Inmovilizado financiero

Préstamo bancario por 15000€ (Solo en el escenario tradicional)

Otras inversiones

Ninguna

9.10 Escenario económico

Para ilustrar los posibles configuraciones, de la empresa se presentarán dos

escenarios económicos el primero será, la configuración tradicional de la empresa,

en la que habrá una serie de trabajadores, un alquiler, servicio de limpieza…

En el segundo escenario se presentará una configuración de las nuevas conocidas

Startups, Startup es simplemente un modelo de emprendimiento en el que

lanzaremos un producto o servicio al mercado con una mínima inversión inicial.

En este caso se suelen hacer distintos planes de empresa, pero en nuestro caso los

datos anteriormente explicados serán comunes a los dos planes a excepción del

préstamo bancario, que solo existirá en el escenario tradicional.

9.10.1Escenario tradicional

Ingresos

Es este apartado podemos ver una estimación de los ingresos que obtendrá la

empresa por la venta de los servicios que ofrece, una estimación de las ventas y el

precio de los productos:

154

---

<!-- Página 155 -->

ERP de software libre en pymes

155

---

<!-- Página 156 -->

ERP de software libre en pymes

Estimando un periodo medio de cobro de los clientes de dos meses, la estimación

del porcentaje de ventas que tendrán los clientes al final del ejercicio será:

156

---

<!-- Página 157 -->

ERP de software libre en pymes

Gastos

Ahora analizaremos los gastos que producirá la empresa para poder prestar estos

servicios.

En el caso del escenario tradicional, los dos primeros años, al ser menores las

ventas, solo dispondremos de un técnico, un auxiliar y el gerente socio

mayoritario, en el tercer año contrataremos otro técnico.

También trabajará un administrativo a media jornada para llevar el papeleo de la

empresa, los trámites que este no pueda hacer se subcontratarán a una gestoría.

157

---

<!-- Página 158 -->

ERP de software libre en pymes

158

---

<!-- Página 159 -->

ERP de software libre en pymes

Además también tendremos otros gastos: alquiler de una oficina, servicio de

limpieza, luz y agua, consumibles de oficina, etc.

Además estimaremos un periodo medio de pago de dos meses, siendo este el

tiempo medio que tardaremos en pagar las facturas de nuestros proveedores,

servicios y alquileres.

159

---

<!-- Página 160 -->

ERP de software libre en pymes

Inversiones

A continuación evaluaremos las inversiones que realizará la empresa, estás

inversiones serán: equipos informáticos que nos permitirán proporcionar el

alquiler de estos, equipos de transporte que consistirá en un coche de empresa y

por último mobiliario para la oficina.

No tendremos consideraremos ninguna inversión intangible ni en I+D

160

---

<!-- Página 161 -->

ERP de software libre en pymes

Préstamos

Tendremos también un préstamo de 1500€ a un 5,16% de interés a pagar en 7

años y medio.

Estimación financiera

Con toda esta información de la empresa, podemos hacer una estimación de

cómo serán las cuentas de la empresa a cuatro años vista.

Balance

Nos permite ver el patrimonio de la empresa, en el final del ejercicio del año, los

activos y pasivos que posee y el tipo de estos.

161

---

<!-- Página 162 -->

ERP de software libre en pymes

Podemos darnos cuenta que en tres años aproximadamente recuperaremos el

patrimonio invertido en la empresa, que no tenemos un apalancamiento

demasiado grande que tenemos una relación de activo corriente pasivo corriente,

en general la situación de la empresa es buena.

162

---

<!-- Página 163 -->

ERP de software libre en pymes

163

---

<!-- Página 164 -->

ERP de software libre en pymes

Cuenta de resultados

La cuenta de resultados nos permite apreciar el resultado neto de la producción

de la empresa en los diferentes años y las razones que influyen en estos hechos.

También podemos apreciar la rentabilidad de determinados elementos como el

personal, entre 2017 y 2018 se contrataron más técnicos, y la rentabilidad de

estos respecto al ejercicio 2016-2017 es menor por lo que tendremos que estudiar

si esta bajada de rentabilidad redunda en otros beneficios como puede ser calidad

de servicio, o condiciones de trabajo, si no es así tendremos que volver al

esquema anterior.

En el caso de nuestra empresa tiene unas buenas cifras, el primer año el resultado

es negativo pero esto es habitual, ya que el primer año habremos de hacer la

inversión inicial, y no dispondremos de una cartera suficiente de clientes para

cubrir gastos.

164

---

<!-- Página 165 -->

ERP de software libre en pymes

165

---

<!-- Página 166 -->

ERP de software libre en pymes

Tesorería

La tesorería refleja la situación de las cuentas de la empresa, saber en qué nos

hemos gastado el dinero durante el año y conocer nuestra caja, en definitiva saber

del dinero que disponemos.

También podemos apreciar los recursos que hemos generado en el año, los gastos

en los que ha incurrido la empresa, y el exceso o necesidad de fondos de la

empresa teniendo en cuenta los recursos generados y los gastos.

166

---

<!-- Página 167 -->

ERP de software libre en pymes

9.10.2 Escenario Startup En el caso de la Startup nos encontraremos con una situación diferente, más

siempre ya que mantendremos nuestros gastos al mínimo.

En este caso la empresa al menos durante los dos primeros años estará formada

por dos personas que no recibirán ningún sueldo hasta que la empresa genere

ciertos beneficios. En el tercer año se contrataría un técnico para aliviar la carga

de trabajo y empezar a configurar una empresa más sólida.

Ingresos

Los servicios que tendremos la capacidad de ofrecer serán de una complejidad de

menor y menores en número que en el caso de una empresa tradicional.

167

---

<!-- Página 168 -->

ERP de software libre en pymes

168

---

<!-- Página 169 -->

ERP de software libre en pymes

Gastos

169

---

<!-- Página 170 -->

ERP de software libre en pymes

Otros gastos

Aquí los otros gastos más que a los gastos que generamos con el mantenimiento

de unas oficinas físicas, de las que no dispondremos, están reflejados gastos de

externalización de servicios como pueden ser, gestorías, abogados…

170

---

<!-- Página 171 -->

ERP de software libre en pymes

Balance

En el balance podemos ver al ser una Startup que todos los activos que posee la

empresa son corrientes, ya que la inversión que hemos realizado ha sido reducida

al mínimo.

Tampoco hemos solicitado préstamos y no tenemos deudas, excepto las

incurridas por el periodo medio de pago a los servicios externos contratados.

A su vez el valor de la empresa no es demasiado grande si tenemos en cuenta

todos los activos de los que disponemos, el valor de la empresa es más bien

escaso, si bien es cierto que la información de la empresa como puede ser el

proceso desarrollado o la cartera de clientes, suponen un elemento a tomar en

cuenta al calcular el valor de la empresa. Generalmente en las Startup su valor no

está en la empresa en sí sino en todo lo relativo a la información de la empresa,

como puede ser: imagen de marca, productos desarrollados, métodos de

operación…

171

---

<!-- Página 172 -->

ERP de software libre en pymes

172

---

<!-- Página 173 -->

ERP de software libre en pymes

Cuenta de resultados

En la cuenta de resultados podemos apreciar que la relación gastos ingresos de la

empresa no es mala, pero tendremos que

173

---

<!-- Página 174 -->

ERP de software libre en pymes

Estado de la caja

Al no tener gastos importantes como pueden ser los sueldos el estado de la caja

estará muy saneado, pero habremos de tener en cuenta que el “sueldo” de los

dos socios que trabajan en la empresa dependerá del dinero generado en la

empresa.

Por tanto teniendo en cuenta este hecho la situación de la empresa no es tan

buena como podemos creer.

Lo más adecuado sería o subir el precio de los productos o buscar más clientes.

174

---

<!-- Página 175 -->

ERP de software libre en pymes

175

---

<!-- Página 176 -->

ERP de software libre en pymes

9.11 Elección del escenario económico, empresa tradicional o Startup

Los dos escenarios son completamente distintos cada uno tendrá sus ventas e

inconvenientes.

En el caso del desarrollo tradicional, tendremos que hacer una inversión inicial

mayor para poder poner en marcha la empresa, pero también tendremos más

posibilidades de éxito.

En el caso de la status la inversión inicial será mayor pero necesitaremos aportar

nuestra propia capacidad del trabajo al proyecto.

A continuación mostraremos alguno de los indicadores económicos de la empresa

que nos ayudarán a explicar las diferencias entre ambas.

Ratios de solvencia

Con los ratios de solvencia analizaremos la capacidad de la empresa para pagar las

deudas que ha contraído, en el caso de la empresa tradicional nos encontramos

con un problema el primer año, puesto que los ingresos de la empresa todavía son

escasos.

En el segundo año también si comparamos la deuda con el EBITDA obtenemos un

resultado del 83,43 por ciento por lo que la empresa está más endeudada de lo

que realmente está produciendo lo cual es peligroso.

Con las cifras de ventas estimadas las cuentas se sanean el tercer año cuando ya

poseemos un mayor capital de trabajo con el que poder operar.

176

---

<!-- Página 177 -->

ERP de software libre en pymes

En el caso de la Startup veremos que como no ha contraído ninguna deuda su

solvencia será impecable, y prácticamente la totalidad de sus activos estará

formada por fondos propios.

Además no se generarán dividendos y todo el resultado del ejercicio se reservará

como fondos propios para el año siguiente, lo que produce que siempre tengamos

un buen capital de trabajo.

Ratios de rentabilidad

En la empresa tradicional el primer año no seremos demasiado rentables, puesto

que el primer año tenemos pérdidas, los indicadores económicos lógicamente nos

177

---

<!-- Página 178 -->

ERP de software libre en pymes

dicen que nuestra empresa no funciona bien, pero si analizamos los años

siguientes podemos observar que los ratios de rentabilidad son muy buenos.

Si bien es cierto que la productividad por empleado disminuye en el último año se

debe a que contratamos más personal.

En el caso de la empresa Startup en los dos primeros años, tendremos unos ratios

muy buenos pero se deberá a que no tenemos personal contratado y por tanto no

tenemos gastos, los datos de rentabilidad reales los podemos ver a partir de 2017

cuando podemos apreciar que son más bajos que en caso de la empresa

tradicional, por esta razón es habitual que empresas que comenzaron como

Startup o autónomos, sobre todo cuando el valor de la empresa no se basa sobre

un producto específico, sino sobre servicios o productos genéricos, con el tiempo

se vayan expandiendo a un modelo más tradicional que puede aportarles más

beneficios.

178

---

<!-- Página 179 -->

ERP de software libre en pymes

Indicadores del equilibrio

Los indicadores de equilibrio de la empresa son bastante adecuados pero

podemos ver respecto a los activos generados tendremos que encontrar un uso

más eficiente para ellos para generar una mayor cantidad de ventas, una de las

opciones posibles sería la contratación de un comercial o realizar una mayor

inversión en publicidad.

179

---

<!-- Página 180 -->

ERP de software libre en pymes

En el caso de la Startup como no hemos contraído ninguna deuda ni poseemos

ningún activo no corriente, el equilibrio de nuestra empresa no es malo, siempre

que tengamos en cuenta que siempre es mejor invertir el dinero que tenemos en

la empresa en ella misma para poder ampliarla de alguna manera, que tener el

dinero sin generar ninguna rentabilidad.

Indicadores de coherencia

Respecto a los indicadores de coherencia en la empresa tradicional, son todos

bastante normales y podemos suponer un funcionamiento adecuado en la

empresa.

180

---

<!-- Página 181 -->

ERP de software libre en pymes

Respecto los resultado de los indicadores de coherencia en la empresa Startup es

importante señalar que con respecto al volumen de ingresos y gastos tenemos un

saldo de caja demasiado grande sería aconsejable reinvertir en la empresa.

181

---

<!-- Página 182 -->

ERP de software libre en pymes

# Capítulo 10: marco regulador de

# los ERP

182

---

<!-- Página 183 -->

ERP de software libre en pymes

## 10 Capítulo 10: marco regulador de los ERP

En el marco regulador, explicaremos las leyes que nos afectan por proporcionar el

servicio de consultoría sobre los ERP. Pero además de ello tendremos que tener

en cuenta que al trabajar con los datos de carácter personal de las personas físicas en las implementaciones tendremos que estudiar también la ley de protección de

datos. Además de esto también nos interesarán las que regulan las licencias del

freeware pues utilizaremos este tipo de software.

10.1 Ley de protección de datos

Ya que en el sistema que implantaremos almacenaremos datos personales de

terceros, como pueden ser los clientes, tendremos que cumplir una serie de

normas para poder hacerlo de manera legal, todas estas normas están expuestas

en la ley de protección de datos, Ley Orgánica 15/1999, de 13 de diciembre,

desarrollado por el Real Decreto 1720/2007, de 21 de Diciembre, el cual se

encuentra vigente actualmente.

Lo primero que habremos de saber es lo que constituye un dato de carácter

personal, que son todos los datos que nos puedan servir para identificar a

personas físicas ya sean empresas, individuos, asociaciones, etc.

Con respecto a estos datos se les aplican una serie de normas como son informar

de que se van a recoger los datos, tener el consentimiento de la persona, los datos

han de estar puestos al día, etc.

Pero sobre todo a nosotros hay un punto en el que tendremos que tener especial

atención

183

---

<!-- Página 184 -->

ERP de software libre en pymes

El responsable del fichero, y, en su caso, el encargado del tratamiento

deberán adoptar las medidas de índole técnica y organizativas necesarias

que garanticen la seguridad de los datos de carácter personal y eviten su

alteración, pérdida, tratamiento o acceso no autorizado, habida cuenta del

estado de la tecnología, la naturaleza de los datos almacenados y los

riesgos a que están expuestos, ya provengan de la acción humana o del

medio físico o natural. (BOE, 1999)

Con este punto queda claro que en nuestro sistema tendremos que tener la

suficiente seguridad sobre los datos para evitar el acceso por parte de personas

no autorizadas, por ello será necesario comprobar la seguridad de nuestro sistema

antes de dar por finalizada la implantación.

En el campo de la ley de protección de datos personal las medidas de seguridad

necesarias se establecen en base a tres niveles de seguridad, básico, medio y alto.

Cada dato tendrá una clasificación en función a su naturaleza.

Todos los datos requieren un nivel de seguridad básico.

Se requerirá un nivel de seguridad media, entre otros tipos de datos, a los que

definan características o personalidad de los ciudadanos, y que permitan evaluar

características de la personalidad o del comportamiento.

Se requerirá un nivel de seguridad alto, entre otros tipos de datos, a los que

refieran a datos de ideología, afiliación sindical, religión, creencias, origen racial,

salud o vida sexual.

Los tipos de datos englobados dentro de estas clasificaciones de seguridad se

encuentran recogidos en el Real Decreto 1720/2007, de 21 de Diciembre, Título VIII artículo 81.

En nuestro caso nuestros datos habitualmente requerirán un nivel de seguridad básico y medio.

184

---

<!-- Página 185 -->

ERP de software libre en pymes

En el caso del nivel de seguridad básico estos serán sus requerimientos:

 Funciones y obligaciones del personal: Existirá un documento de seguridad

que recogerá las funciones y obligaciones de todos los usuarios con acceso

a los datos. También se recogerá en este documento las autorizaciones de

control que el responsable del fichero delegue. Será obligado informar a

todo el personal relacionado, de las medidas de seguridad necesarias.

 Registro de incidencias: Existirá un registro mediante el cual se puedan

gestionar las incidencias.

 Control de acceso:

o Los usuarios tendrán acceso únicamente a aquellos recursos que

precisen para el desarrollo de sus funciones.

o El responsable del fichero se encargará de que exista una relación

actualizada de usuarios y perfiles de usuarios, y los accesos

autorizados para cada uno de ellos.

o El responsable del fichero establecerá mecanismos para evitar que

un usuario pueda acceder a recursos con derechos distintos de los

autorizados.

o Exclusivamente el personal autorizado para ello en el documento de seguridad podrá conceder, alterar o anular el acceso autorizado

sobre los recursos, conforme a los criterios establecidos por el

responsable del fichero. o En caso de que exista personal ajeno al responsable del fichero que

tenga acceso a los recursos deberá estar sometido a las mismas

condiciones y obligaciones de seguridad que el personal propio.

 Gestión de soportes y documentos

185

---

<!-- Página 186 -->

ERP de software libre en pymes

o Los soportes y documentos que contengan datos de carácter

personal deberán permitir identificar el tipo de información que

contienen, ser inventariados y solo deberán ser accesibles por el

personal autorizado para ello en el documento de seguridad.

Se exceptúan estas obligaciones cuando las características físicas

del soporte imposibiliten su cumplimiento, quedando constancia

motivada de ello en el documento de seguridad.

o La salida de soportes y documentos que contengan datos de

carácter personal, incluidos los comprendidos y/o anejos a un

correo electrónico, fuera de los locales bajo el control del

responsable del fichero o tratamiento deberá ser autorizada por el

responsable del fichero o encontrarse debidamente autorizada en

el documento de seguridad.

o En el traslado de la documentación se adoptarán las medidas

dirigidas a evitar la sustracción, pérdida o acceso indebido a la

información durante su transporte.

o Siempre que vaya a desecharse cualquier documento o soporte

que contenga datos de carácter personal deberá procederse a su

destrucción o borrado, mediante la adopción de medidas dirigidas

a evitar el acceso a la información contenida en el mismo o su

recuperación posterior.

o La identificación de los soportes que contengan datos de carácter

personal que la organización considerase especialmente sensibles se podrá realizar utilizando sistemas de etiquetado comprensibles y

con significado que permitan a los usuarios con acceso autorizado a

los citados soportes y documentos identificar su contenido, y que dificulten la identificación para el resto de personas.

 Identificación y autenticación

186

---

<!-- Página 187 -->

ERP de software libre en pymes

o El responsable del fichero o tratamiento deberá adoptar las

medidas que garanticen la correcta identificación y autenticación

de los usuarios.

o El responsable del fichero o tratamiento establecerá un mecanismo

que permita la identificación de forma inequívoca y personalizada

de todo aquel usuario que intente acceder al sistema de

información y la verificación de que está autorizado.

o Cuando el mecanismo de autenticación se base en la existencia de

contraseñas existirá un procedimiento de asignación, distribución y

almacenamiento que garantice su confidencialidad e integridad.

o El documento de seguridad establecerá la periodicidad, que en

ningún caso será superior a un año, con la que tienen que ser

cambiadas las contraseñas que, mientras estén vigentes, se

almacenarán de forma ininteligible.

 Copias de respaldo y recuperación:

o Deberán establecerse procedimientos de actuación para la

realización como mínimo semanal de copias de respaldo, salvo que

en dicho período no se hubiera producido ninguna actualización de

los datos.

o Asimismo, se establecerán procedimientos para la recuperación de

los datos que garanticen en todo momento su reconstrucción en el

estado en que se encontraban al tiempo de producirse la pérdida o

destrucción.

o Únicamente, en el caso de que la pérdida o destrucción afectase a

ficheros o tratamientos parcialmente automatizados, y siempre

que la existencia de documentación permita alcanzar el objetivo al

que se refiere el párrafo anterior, se deberá proceder a grabar

187

---

<!-- Página 188 -->

ERP de software libre en pymes

manualmente los datos quedando constancia motivada de este

hecho en el documento de seguridad.

o El responsable del fichero se encargará de verificar cada seis meses

la correcta definición, funcionamiento y aplicación de los

procedimientos de realización de copias de respaldo y de

recuperación de los datos.

o Las pruebas anteriores a la implantación o modificación de los

sistemas de información que traten ficheros con datos de carácter

personal no se realizarán con datos reales, salvo que se asegure el

nivel de seguridad correspondiente al tratamiento realizado y se

anote su realización en el documento de seguridad.

En el caso del nivel de seguridad medio además de las medidas de seguridad

básicas tendremos en cuenta:

 Responsable de seguridad: En el documento de seguridad deberán

designarse uno o varios responsables de seguridad encargados de

coordinar y controlar las medidas definidas en el mismo. Esta designación

puede ser única para todos los ficheros o tratamientos de datos de

carácter personal o diferenciada según los sistemas de tratamiento

utilizados, circunstancia que deberá hacerse constar claramente en el

documento de seguridad.

 Auditoría:

o A partir del nivel medio, los sistemas de información e instalaciones

de tratamiento y almacenamiento de datos se someterán, al menos

cada dos años, a una auditoría interna o externa que verifique el

cumplimiento del presente título.

o Con carácter extraordinario deberá realizarse dicha auditoría

siempre que se realicen modificaciones sustanciales en el sistema

188

---

<!-- Página 189 -->

ERP de software libre en pymes

de información que puedan repercutir en el cumplimiento de las

medidas de seguridad implantadas con el objeto de verificar la

adaptación, adecuación y eficacia de las mismas. Esta auditoría

inicia el cómputo de dos años señalado en el párrafo anterior.

o El informe de auditoría deberá dictaminar sobre la adecuación de

las medidas y controles a la Ley y su desarrollo reglamentario,

identificar sus deficiencias y proponer las medidas correctoras o

complementarias necesarias. Deberá, igualmente, incluir los datos,

hechos y observaciones en que se basen los dictámenes alcanzados

y las recomendaciones propuestas.

o Los informes de auditoría serán analizados por el responsable de

seguridad competente, que elevará las conclusiones al responsable

del fichero o tratamiento para que adopte las medidas correctoras

adecuadas y quedarán a disposición de la Agencia Española de

Protección de Datos o, en su caso, de las autoridades de control de

las comunidades autónomas.

 Gestión de soportes y documentos:

o Deberá establecerse un sistema de registro de entrada de soportes

que permita, directa o indirectamente, conocer el tipo de

documento o soporte, la fecha y hora, el emisor, el número de

documentos o soportes incluidos en el envío, el tipo de información

que contienen, la forma de envío y la persona responsable de la

recepción que deberá estar debidamente autorizada.

o Igualmente, se dispondrá de un sistema de registro de salida de

soportes que permita, directa o indirectamente, conocer el tipo de

documento o soporte, la fecha y hora, el destinatario, el número de

documentos o soportes incluidos en el envío, el tipo de información

189

---

<!-- Página 190 -->

ERP de software libre en pymes

que contienen, la forma de envío y la persona responsable de la

entrega que deberá estar debidamente autorizada.

 Identificación y autenticación: El responsable del fichero o tratamiento

establecerá un mecanismo que limite la posibilidad de intentar

reiteradamente el acceso no autorizado al sistema de información.

 Control de acceso físico: Exclusivamente el personal autorizado en el

documento de seguridad podrá tener acceso a los lugares donde se hallen

instalados los equipos físicos que den soporte a los sistemas de

información.

 Registro de incidencias:

o En el registro regulado en el artículo 90 deberán consignarse,

además, los procedimientos realizados de recuperación de los

datos, indicando la persona que ejecutó el proceso, los datos

restaurados y, en su caso, qué datos ha sido necesario grabar

manualmente en el proceso de recuperación.

o Será necesaria la autorización del responsable del fichero para la

ejecución de los procedimientos de recuperación de los datos.

Esta explicación es parte una explicación del Real Decreto 1720/2007 otras están representadas de manera literal.

Las medidas de seguridad de nivel alto raramente serán necesarias en el ámbito

de los ERP pero si se quieren conocer se encuentran recogidas de los artículos del

101 al 104 del Real Decreto 1720/2007.

190

---

<!-- Página 191 -->

ERP de software libre en pymes

Además tendremos que permitir eliminar los datos totalmente de nuestro fichero,

pues las personas tienen el derecho de revocar su consentimiento en el

almacenamiento de los datos.

10.2 Licencias de difusión freeware y ley de propiedad intelectual

Habrá otra ley que nos afectará sobre todo a la hora de desarrollar la

funcionalidad de los ERP. Es habitual en el software libre que exista un copyleft sobre los productos, las obligaciones en las que incurriremos al utilizar o modificar

todo o parte de un software dependerán de la licencia de uso de este que tenga

este producto.

La primera y más común de las licencias es la GPL de GNU (GNU, 2007).

Aquí en España estas licencias se rigen por la ley de propiedad intelectual, en ellas

se disponen las bases para considerarse el autor de una obra, (BOE Ley de

propiedad intelectual, 1996) también se dispone el derecho a encomendar la

gestión de los derechos de propiedad intelectual.

10.3 Prestación de servicios en consultoría

Normalmente cuando hemos hecho un acuerdo con el cliente, se hace un

contrato de prestación de servicio en él se establecen las bases del intercambio

entre el cliente y la consultora.

Estos contratos de prestación de servicios, generalmente se rigen por el código

civil, dentro del código civil el título cuarto, en el que se hacen las disposiciones

que a contratos de compra venta se refiere.

191

---

<!-- Página 192 -->

ERP de software libre en pymes

También nos puede interesar el título seis sobre contratos de arrendamiento y en

especial en el capítulo cuarto, en el que se recogen los contratos de

arrendamiento de obras y servicios.

Debido a la prestación de los servicios y al ejercicio de la actividad económica

empresarial en el campo de la consultoría, también pueden ser interesantes:

 Ley 11/1986, de 20 de marzo, de Patentes de Invención y Modelos de Utilidad. La cual regula el registro de patentes, copyright …

 Ley 34/1988, de 11 de noviembre, General de Publicidad.

 Ley 3/1991, de 10 de enero, de Competencia Desleal.

 Ley 12/1991, de 29 de abril, de Agrupaciones de Interés Económico.

 Real Decreto 1784/1996, de 19 de julio, por el que se aprueba el

Reglamento del Registro Mercantil.

 Ley27/1999, de 16 de julio, de Cooperativas.

 Ley 17/2001, de 7 de diciembre, de Marcas.

 Ley 22/2003, de 9 de julio, Concursal. La cual regula el procedimiento a

seguir en casos de quiebra y suspensión de pagos.

 Ley 15/2007, de 3 de julio, de Defensa de la Competencia.

 Ley 3/2009, de 3 de abril, sobre modificaciones estructurales de las

sociedades mercantiles.

 Real Decreto Legislativo 1/2010, de 2 de julio, por el que se aprueba el

Texto Refundido de la Ley de Sociedades de Capital.

192

---

<!-- Página 193 -->

ERP de software libre en pymes

# Capítulo 11: Tendencias futuras

193

---

<!-- Página 194 -->

ERP de software libre en pymes

## 11 Capítulo 11: Tendencias futuras

Evaluando la situación actual de los ERP podemos darnos cuenta de que cada vez

se está produciendo una implementación más amplia de estos, como suele ocurrir

con todas las tecnologías en un principio se utilizan en grandes entornos como los

gubernamentales o militares, luego en grandes empresas y posteriormente se produce una utilización masiva de estos, fue el caso de inventos como el GPS, el

radar, internet o la propia informática.

Por lo tanto podemos deducir que existe una necesidad organizacional mayor hoy en día que antiguamente, hasta en las pequeñas empresas, ya que surgen nuevos

modelos de negocio distintos de los tradicionales, además la necesidad del

almacenamiento de datos es mucho mayor que antiguamente.

Por tanto el futuro uso de los sistemas tipo ERP va a ser masivo, además cada vez

se está simplificando más su utilización con la utilización del SaaS.

Respecto a los nuevos sistemas en la nube desde luego pueden ser un buen

sistema para las pymes sobre todo en un futuro cuando su funcionalidad y

disponibilidad sea equiparable a la de los sistemas on-site que a día de hoy

todavía ofrecen una mayor capacidad de configuración. Estamos asistiendo a una

remodelación completa de la forma de ofrecer servicios en informática con la

aparición del SaaS y los sistemas ERP no son una excepción.

En cuanto al software libre hay que decir que se está difundiendo más su uso y

configurándose como una posible opción de desarrollo de la industria a largo

plazo, sin ir más lejos tenemos casos de que este tipo de desarrollo se está

configurando como su base para ofrecer servicios adicionales o soporte, como el

de los explicados Openbravo y Odoo. El software libre será difícil que llegue a

194

---

<!-- Página 195 -->

ERP de software libre en pymes

tener la capacidad de operación que tiene el software desarrollado de manera

tradicional, pero desde luego es un competidor a tener en cuenta en el futuro y

siempre es una opción siempre que queramos ahorrar dinero en licencias y

tengamos la capacidad de hacerlo por nuestra cuenta.

Dada la situación sería interesante la creación de un ERP integrado con el

desarrollo virtual de proyectos, debido a la globalización cada vez es más habitual

el desarrollo de proyectos en diferentes partes del planeta, por ello cada vez se

desarrollan más las herramientas colaborativas que facilitan esta tarea y

aumentan la producción.

El mayor problema de las tecnologías colaborativas es que hoy por hoy son

muchas, pues cada una de ellas cubre una parte del proceso de desarrollo, en un

proyecto con equipos virtuales integrados se utiliza una media de 10 a 20

herramientas colaborativas distintas desde wikis, hasta redes sociales, editores

colaborativos, blogs, etc.

Por ello sería muy interesante un ERP que permitiese una completa integración

con las herramientas colaborativas, permitiendo así evitar duplicidades de datos y

tener un acceso consistente con los datos necesarios para el desarrollo del

proyecto.

De esta manera el ERP se convertiría en una herramienta integral para el tratamiento de la información en la empresa.

Podemos ver que ciertos ERP como Odoo han empezado a incluir funcionalidades de este tipo en sus ERP pero sería más interesante la integración de las

herramientas actuales del sector, mucho más maduras y funcionales.

195

---

<!-- Página 196 -->

ERP de software libre en pymes

# Capítulo 12: Conclusiones

196

---

<!-- Página 197 -->

ERP de software libre en pymes

## 12 Capítulo 12: Conclusiones

Dadas las tendencias actuales en el campo empresarial, podemos decir que la

utilización de ERP se está convirtiendo en algo indispensable tanto para grandes

como para pequeñas empresas, podemos apreciar que las empresas productoras de este tipo de software como es SAP ya están intentando cubrir esta demanda.

Pero dada la naturaleza de este tipo de software, más sencillo que el destinado a

grandes empresas, la opción de utilización de software libre se configura como

una opción perfectamente válida, permitiendo además un ahorro significativo en los costes.

La motivación de este proyecto era conseguir la difusión de este tipo de software,

este proyecto permite acercar este tipo de software a las pequeñas y medianas

empresas al proporcionar un marco de descripción general de este tipo de

sistemas, la descripción integral del proceso de implementación y uso de estos;

haciendo más fácil el entendimiento de los ERP de software libre y permitiendo a

estas empresas dar el salto a los sistemas de gestión del futuro. Por tanto se

puede afirmar que se ha cumplido el objetivo del proyecto, que es proporcionar

una herramienta para que las pymes conozcan y puedan acceder a los ERP de

software libre.

Personalmente la realización de este proyecto me ha permitido conocer el

software empresarial a fondo, especialmente los ERP, al realizar el estudio sobre

todo el proceso de implementación de estos he conocido la magnitud del mismo y

la cantidad de factores implicados. A su vez he conseguido dar una visión

completa respecto a ellos, lo cual no conseguí encontrar ya que todo el material al

respecto, o estaba orientado a una herramienta específica o a una determinada

fase del proceso, con este trabajo se puede dar un paso más para el

entendimiento de este software tan amplio y de sus posibilidades, presentes y

futuras.

197

---

<!-- Página 198 -->

ERP de software libre en pymes

198

---

<!-- Página 199 -->

ERP de software libre en pymes

## 13 Anexo 1 Tablas de porcentaje utilización ERP

En las siguientes tablas se pueden ver la el porcentaje de empresas que utilizaba

ERP para la información de compra venta y el porcentaje de empresa que utilizaba

software libre para procesar información tipo ERP. Los datos se agrupan además por tamaño de la empresa y por las distintas agrupaciones de empresas.

DeDe

ToDe50250

tal10 aay

Total Empresas49249más

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O1930,

CRM (p. e. Open ERP, Joomla, Ruby on Rails, MySQL.),7 17,48 45,6

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre3358,

compras/ventas con otras áreas de la empresa,1 28,34 75,4

1. Total Industria (CNAE 10-39)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O1928,

CRM (p. e. Open ERP, Joomla, Ruby on Rails, MySQL.),2 16,98 38,6

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre3772,

compras/ventas con otras áreas de la empresa,4 29,64 89

1.1. Alimentación bebidas tabaco textil prendas vestir cuero

y calzado madera y corcho papel artes gráficas y reproducción de soportes grabados (CNAE 10-18)

199

---

<!-- Página 200 -->

ERP de software libre en pymes

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O1729,

CRM (p. e. Open ERP, Joomla, Ruby on Rails, MySQL.),8 15,42 41

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre3068,

compras/ventas con otras áreas de la empresa,6 23,19 89

1.2 Coquerías y refino de petróleo produc. farmacéuticos

caucho y plásticos Productos minerales no metálicos (CNAE

19-23)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O1927,

CRM (p. e. Open ERP, Joomla, Ruby on Rails, MySQL.),4 16,81 38,8

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre46

compras/ventas con otras áreas de la empresa,2 37,1 77 93,1

1.3 Metalurgia fabricación de productos metálicos ( CNAE

24-25)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O1925,

CRM (p. e. Open ERP, Joomla, Ruby on Rails, MySQL.),1 17,97 33,4

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre3870,

compras/ventas con otras áreas de la empresa,4 32,78 94,4

1.4. Productos informáticos, electrónico y ópticos material y

equipo eléctrico maquinaria y equipo mecánico vehículos a

motor material de transporte muebles industria

200

---

<!-- Página 201 -->

ERP de software libre en pymes

manufacturera reparación maquinaria y equipo (CNAE 26-

33)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O2030,

CRM (p. e. Open ERP, Joomla, Ruby on Rails, MySQL.),9 18,56 36,2

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre41

compras/ventas con otras áreas de la empresa,1 32,1 81 90,6

1.5. Energía y agua (CNAE 35-39)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O2231,

CRM (p. e. Open ERP, Joomla, Ruby on Rails, MySQL.),3 17,48 44

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre3950,

compras/ventas con otras áreas de la empresa,1 32,82 71

2. Total Construcción (CNAE 41-43)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O1023,

CRM (p. e. Open ERP, Joomla, Ruby on Rails, MySQL.),4 9,23 40

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre2043,

compras/ventas con otras áreas de la empresa,3 17,93 82,9

3. Total Servicios (CNAE 45-82, excluidas CNAE 56: servicios

de comidas y bebidas, CNAE 75 y financieras)

3.5 % de empresas que utilizaban software de código2233,

abierto según tipología: Aplicaciones de código abierto para,4 202 49,6

201

---

<!-- Página 202 -->

ERP de software libre en pymes

el procesamiento automático de información del tipo ERP O

CRM (p. e. Open ERP, Joomla, Ruby on Rails, MySQL.)

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre3452,

compras/ventas con otras áreas de la empresa,4 30,77 67,9

3.1. Venta y reparación de vehículos de motor comercio al

por mayor al por menor (CNAE 45-47)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O1929,

CRM (p. e. Open ERP, Joomia, Ruby on Rails, MySQL.),8 18,16 51,3

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre3960,

compras/ventas con otras áreas de la empresa,6 36,73 75,3

3.2. Transporte y almacenamiento (CNAE 49-53)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O1731,

CRM (p. e. Open ERP, Joomia, Ruby on Rails, MySQL.),4 14,63 49,9

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre2755,

compras/ventas con otras áreas de la empresa,5 22,77 64,3

3.3. Servicios de alojamiento (CNAE 55)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O2025,

CRM (p. e. Open ERP, Joomia, Ruby on Rails, MySQL.),4 18,97 31,7

28 % de empresas que disponían de herramientas2648,

informáticas ERP para compartir información sobre,4 19,99 65,4

202

---

<!-- Página 203 -->

ERP de software libre en pymes

compras/ventas con otras áreas de la empresa

3.4. Información y comunicaciones (CNAE 58-63)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O5560,

CRM (p. e. Open ERP, Joomia, Ruby on Rails, MySQL.),9 53,97 67,4

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre4963,

compras/ventas con otras áreas de la empresa,1 43,29 80,7

3.5. Actividades inmobiliarias (CNAE 68)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O22

CRM (p. e. Open ERP, Joomia, Ruby on Rails, MySQL.),7 20,1 49 35,2

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre2955,

compras/ventas con otras áreas de la empresa,7 26,27 80

3.6. Actividades profesionales, científicas y técnicas (excl.

veteranías) (CNAE 69-74)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O2945,

CRM (p. e. Open ERP, Joomia, Ruby on Rails, MySQL.),3 26,23 63

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre3558,

compras/ventas con otras áreas de la empresa,8 31,68 78,8

3.7. Actividades administrativas y servicios auxiliares (incl.

agencias viajes) (CNAE 77-82)

3.5 % de empresas que utilizaban software de código 15 12,1 23, 38,1

203

---

<!-- Página 204 -->

ERP de software libre en pymes

abierto según tipología: Aplicaciones de código abierto para,5 2

el procesamiento automático de información del tipo ERP O

CRM (p. e. Open ERP, Joomia, Ruby on Rails, MySQL.)

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre1930,

compras/ventas con otras áreas de la empresa,3 14,44 51,1

4. Sector TIC (261-264, 268, 465, 582, 61, 6201, 6202, 6203,

6209, 631, 951)

3.5 % de empresas que utilizaban software de código

abierto según tipología: Aplicaciones de código abierto para

el procesamiento automático de información del tipo ERP O5659,

CRM (p. e. Open ERP, Joomia, Ruby on Rails, MySQL.),6 55,34 66,9

28 % de empresas que disponían de herramientas

informáticas ERP para compartir información sobre5967,

compras/ventas con otras áreas de la empresa,2 55,89 82,5

Fuente: (INE, 2013)

204

---

<!-- Página 205 -->

## 14 Anexo 2 guía de implantación planificación

## Microsoft Project

En las siguientes tablas y diagramas de Gantt se explica una posible planificación para el caso real explicado en el capítulo siete.

---

<!-- Página 206 -->

---

<!-- Página 207 -->

ERP de software libre en pymes

207

---

<!-- Página 208 -->

ERP de software libre en pymes

208

---

<!-- Página 209 -->

## 15 Bibliografía

Adempiere ERP. (29 de 8 de 2014). Sourceforge. Recuperado el 29 de 8 de 2014, de Sourceforge: http://sourceforge.net/projects/adempiere/files/ADempiere%20Official%20Relea se/stats/timeline

AJDB soft. (14 de 8 de 2011). ajdf soft principal. Recuperado el 4 de 9 de 2014, de ajdf soft : http://www.ajpdsoft.com/modules.php?name=News&file=article&sid=573

Al-Mashari, M. (2003). Enterprise resource planning (ERP) systems: A research agenda. Industrial Management + Data Systems, 22-27.

Arnesen, S. C. (2013). Is a Cloud ERP Solution Right for You? Strategic Finance, 45-50.

BOE. (13 de 12 de 1999). Ley Orgánica 15/1999, de 13 de diciembre, de Protección de Datos. BOE. Madrid, Madrid, España.

BOE Ley de propiedad intelectual. (1996). Ley de propiedad intelectual «BOE» núm. 97, de 22/04/1996. Madrid: BOE.

Comunidad Adempiere. (3 de 9 de 2011). Adempiere wiki. Recuperado el 10 de 9 de 2014, de Adempiere: http://www.adempiere.com/index.php?title=Touchscreen_POS&action=history

Cuéllar, G. A. (2014). Universidad del cauca. Recuperado el 20 de Agosto de 2014, de F.C.C.E.A: http://fccea.unicauca.edu.co/old/erp.htm

DGIPYME. (2014). web de la secretaría general de industria de pequeña y mediana empresa. Recuperado el 3 de 9 de 2104, de http://planempresa.ipyme.org/Paginas/Home.aspx

ERP: la evolución imparable de un mercado muy dinámico. (2014). pymes.es, 4-12.

GNU. (5 de 6 de 2007). GNU General Public License. Recuperado el 14 de 9 de 2014, de gnu: http://www.gnu.org/copyleft/gpl.html

Guidance Share. (22 de 1 de 2010). Recuperado el 16 de 8 de 2014, de Guidance Share: http://www.guidanceshare.com/wiki/Application_Architecture_Guide_- _Chapter_9_-_Layers_and_Tiers

Hessman, T. (4 de 10 de 2013). Tales of an ERP Implementation. Industry Week.

---

<!-- Página 210 -->

ERP de software libre en pymes

IBM Develorper Works. (2014). Developer works. Recuperado el 2014 de 9 de 5, de ibm: http://www.ibm.com/developerworks/data/library/techarticle/dm-0807patel/

INE. (1 de 1 de 2013). Variables de uso de TIC (a enero de 2013) por agrupación de actividad (excepto CNAE 56, 64-66 y 95.1), principales variables y tamaño de la empresa. España.

Labrador, R. M. (2005). Artículos-Escuela Técnica Superior de Ingeniería Informática - Universidad de Sevilla. Recuperado el 2014 de 9 de 5, de Escuela Técnica Superior de Ingeniería Informática - Universidad de Sevilla: http://www.informatica.us.es/~ramon/articulos/LicenciasSoftware.pdf

Maditinos, D., Chatzoudes, D., & Tsairidis, C. (2012). Factors affecting ERP system implementation effectiveness. Journal of Enterprise Information Management, 25(1), 60-78.

Maditinos, D., Chatzoudes, D., & Tsairidis, C. (2012). Factors affecting ERP system implementation effectiveness. Journal of Enterprise Information Management, 60-78.

Microsoft. (2014). soporte Microsoft. Recuperado el 4 de 9 de 2014, de sitio web de microsoft office: http://office.microsoft.com/es-es/access-help/exportar-datos-a- un-archivo-de-texto-HA010006905.aspx

Microsoft Download Center. (2014). Dowload Center. Recuperado el 5 de 11 de 2014, de http://www.microsoft.com/en-us/download/details.aspx?id=42657

Microsoft Office. (2014). Soporte Microsoft Office. Recuperado el 4 de 9 de 2014, de Microsoft office: http://office.microsoft.com/es-es/access-help/exportar-datos-a- excel-HA101819737.aspx?CTT=1

Ministerio de Industria Energía y Turismo. (2014). Retrato de las PYME.

Mysql Comunity . (2014). Recuperado el 29 de 8 de 2014, de dev.mysql: http://dev.mysql.com/doc/connector-odbc/en/connector-odbc-examples-tools- with-access-linked-tables.html

Mysql Downloads. (2006). Downloads. Recuperado el 9 de 5 de 2014, de Mysql: http://downloads.mysql.com/archives/migration/

Mysql Workbench. (2014). Mysql.com. Recuperado el 5 de 9 de 2014, de Mysql: http://www.mysql.com/products/workbench/

Nastase, I. D. (2012). TRAINING ISSUES IN ERP IMPLEMENTATIONS. Accounting and Management Information Systems, 11(4), 621–636.

210

---

<!-- Página 211 -->

ERP de software libre en pymes

Niehaves, B., Klose, K., & Becker, J. (2006). Governance Theory Perspectives on IT Consulting Projects: The Case of ERP Implementation. E - Service Journal, 5(1), 5- 11,13,15,17-21,23-26.

Openbiz. (10 de 9 de 2014). Adempiere ERP. Recuperado el 10 de 9 de 2014, de openbiz: http://www.openbiz.com.ar/adempiere.php

Oracle software network. (2014). Oracle. Recuperado el 5 de 9 de 2014, de software network: http://www.oracle.com/technetwork/database/migration/connect- step-mysql-1946352.html

PhpMyAdmin. (s.f.). Acerca de nosotros PhpMyAdmin. Recuperado el 21 de 8 de 2014, de Bringing MySQL to the web: http://www.phpmyadmin.net/home_page/index.php

Prasad Bingi, M. K. (1999). Critical Issues Affecting an ERP. Information Systems Management,, 16:3, 7-14,.

Redacción-Dataprix . (9 de 4 de 2014). Dataprix-¿Qué es un ERP y qué ventajas aporta a las empresas que lo implantan? Recuperado el 4 de 9 de 2014, de Dataprix: http://www.dataprix.com/articulo/erp/cuanto-cuesta-implementar-erp-empresa

redk. (2014). Servicios para openbravo. Recuperado el 11 de 9 de 2014, de redk: http://www.redk.net/tecnologias/openbravoerp/funcionalidad.html

Rosemann, J. v. (2010). Handbook on Business Process Managemen. Moscow.

Rouhani, S., & Ravasan, A. Z. (Jun 2013). ERP success prediction: An artificial neural network approach. Scientia Iranica. Transaction E, Industrial Engineering, 992- 1001.

Rozo development. (16 de 5 de 2014). rozo: openerp. Recuperado el 29 de 8 de 2014, de rozo.

Solution Square. (2006). Solution Square. Recuperado el 8 de 8 de 2014, de Solution Square: http://www.solutionsquare.com/articles/Why_does_software_cost_so_much.pdf

Ubuntu. (12 de 7 de 2012). doc.ubuntu: licencias software. Recuperado el 21 de 8 de 2014, de doc.ubuntu: http://doc.ubuntu-es.org/Licencias_de_software

Wikipedia. (18 de 7 de 2014). Wikipedia. Recuperado el 18 de 7 de 2014, de http://es.wikipedia.org/wiki/Sistema_de_planificaci%C3%B3n_de_recursos_empr esariales

Yin, R. (2003). Case Study Research: Design and Methods. Thousand Oaks: CA.

211

---

<!-- Página 212 -->

ERP de software libre en pymes

Zazueta, U. H. (2009). Estilos de aprendizaje:modelo de kolb. Recuperado el 14 de 8 de 2014, de Estilos de aprendizaje: https://sites.google.com/site/estilosdeaprendizajeitt/home/modelo-de-kolb

212