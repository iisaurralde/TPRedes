# Universidad Nacional de Rosario
Facultad de Ciencias Exactas, Ingeniería y Agrimensura

IA3.5 Redes de Datos
### Tecnicatura Universitaria en Inteligencia Artificial

## Informe - Comunicación API Cliente-Servidor entre dos hosts

### Descripción general:
El objetivo de este proyecto es desarrollar una comunicación API Cliente-Servidor entre dos hosts. El host servidor correra un uvicorn server, el archivo main.py descargara automáticamente datos en formato JSON y procesará consultas y modificaciones a los mismos, mientras que el host utilizado como cliente, implementado sobre el archivo client.py realizará estas consultas y modificaciones.

### Etapa 1: Elección y consulta de los datos
En mi caso, utilicé el archivo JSON correspondiente a un registro de eventos de la Municipalidad de Rosario (eventos.json). El archivo contiene múltiples objetos, cada uno representando una "ocurrencia", a la que a lo largo del TP se nombró como evento. Cada evento tiene propiedades o atributos como "name" (nombre del evento), "date_start" (fecha de inicio) y "ticket_value" (valor de la entrada). Para la implementación de el post que agrega nuevos objetos a la base de datos JSON, se crearon 2 clases (attributes y ocurrencias). Dentro de estas clases podremos ver en detalle cada tipo de dato correspondiente al objeto ocurrencia y sus atributos.

### Etapa 2: Desarrollar el servidor API
En esta etapa, se utilizan los módulos de Python fastapi, request y uvicorn para implementar un servidor API que gestionará las consultas  y modificaciones a los datos almacenados en el archivo JSON. Las funciones principales del servidor API incluyen:

Consulta de todos los eventos del año.
Consulta de eventos de un mes en particular.
Agregar un nuevo evento al archivo JSON.
Actualizar el nombre de un evento existente por su ID.
Eliminar un evento existente por su ID.
El servidor API responde preguntas como:

#### El servidor API responde a las siguientes preguntas: 

¿Cuáles son todos los eventos del año?
¿Cuáles son los eventos de un mes específico?
¿Cómo agregar un nuevo evento al archivo JSON?
¿Cómo actualizar el nombre de un evento existente?
¿Cómo eliminar un evento existente?


### Etapa 3: Desarrollar el cliente API
En esta etapa, se desarrolla un programa en Python para implementar un cliente API que pueda realizar consultas y modificaciones al servidor. El cliente API se comunica con el servidor API utilizando solicitudes HTTP, mediante el uso de la libraría request. Se verifica el correcto funcionamiento del cliente API realizando consultas y modificaciones, y asegurándose de que se obtengan las respuestas adecuadas. Como una mejora interesante del cliente, sería crear una interfaz interactiva más orientada al usuario para empaquetar la aplicación y utilizar librerias GUI como Tkinter, PyQt, PySide para ver ventanas con botones, campos de entrada y otros elementos que faciliten la interacción con el cliente API. Actualmente el cliente admite 2 diferentes tipos de usuarios: tipo Usuario y tipo Administrador. 
El usuario de tipo Usuario, podrá solamente ejecutar tareas de solo lectura sobre la base de datos.
El usuario de tipo Administrador, podrá ejecutar tareas de lectura y escritura sobre la base de datos.

### Etapa 4: Establecer comunicación entre host
En la última etapa, se montan la aplicación servidor y la aplicación cliente en dos hosts distintos. Se realizan las configuraciones de red y dependencias necesarias en los hosts para preparar el entorno y la comunicación. Se establece la conexión entre el servidor y el cliente y se verifica que las consultas y modificaciones al archivo JSON puedan realizarse correctamente a través de la comunicación entre los dos hosts.


#### Configuraciones realizadas en los hosts:

Configuración de red para permitir la comunicación entre el servidor y el cliente:

Si ya nos encontramos en una red lan, optar por un rango de ips dentro de la misma red. En caso de crear una nueva red, podremos tomar el siguiente ejemplo:

Configuración de red del servidor: 
    IP: 10.10.10.100
    mask: 255.255.255.0
    default-gateway: 10.10.10.254

Configuración de red del cliente: 
    IP: 10.10.10.5
    mask: 255.255.255.0
    default-gateway: 10.10.10.254

Configuración de los puertos utilizados por el servidor y el cliente:
    Por default el servidor uvicorn escucha sobre el puerto 8000
    Por default el cliente escucha sobre el puerto 8000


Instalación de los módulos Python necesarios:

    Ejecutar sobre el servidor:
    pip install fastapi
    pip install uvicorn
    pip install pandas
    pip install json
    pip install wget
    pip install pydantic

    Ejecutar sobre el host cliente:
    pip install requests
    pip install pandas
    pip install json



Verificación de la disponibilidad y accesibilidad del archivo JSON en el servidor.

    Verificar la conexión a internet del host servidor, ya que este obtiene la base de datos JSON desde internet, utilizando la librería wget para descargarla.


## En conclusión, el proyecto consiste en implementar una comunicación API Cliente-Servidor entre dos hosts, donde el servidor almacena datos en un archivo JSON y el cliente realiza consultas y modificaciones. Las etapas abordadas incluyen la elección y consulta de los datos, el desarrollo del servidor API, el desarrollo del cliente API y la conexión y verificación. Si bien esta implementación cliente-servidor tiene muchas posibilidades de mejora, como configuraciones de seguridad, reducción de código mediante modularizaciones, tambien tiene gran potencial de crecimiento y adaptabilidad a mejoras y de responder a más preguntas con otro grado de complejidad. Se entiende que para el objetivo del TP, se llegó a cumplir con lo esperado, empleando las dependencias aconcejadas y ejecutando las requests solicitadas.
