# El lenguaje de programación Python - Intermedio 🐬

**<div style="text-align: right"> Samuel Arturo Garrido Sánchez</div>**
<div style="text-align: right"> samuelarturogs@gmail.com</div>

Python es un lenguaje de programación **multiparadigma**, muy útil para demasiadas ramas de la investigación, desarrollos y procesos. 
Su filosofía radica en un código legible que cualquier persona no enfocada en el área de programación, pueda comprender.

![](img/let.png)

## Excepciones 💥

Los errores de ejecución son llamados comúnmente excepciones. Si dentro de una función surge una excepción y la función no la maneja, la excepción se propaga hacia la función que la invocó, si esta otra tampoco la maneja, la excepción continua propagándose hasta llegar a la función inicial del programa y si esta tampoco la maneja se interrumpe la ejecución del programa. 

**Errores de ejecución comunes:**
- No se encontró el archivo
- División entre 0
- Lectura incorrecta
- Objeto no iterable

Etc. etc. etc. Al menos alguna vez hasta ahora les debió aparecer uno.

```python
try:
    # aquí ponemos el código que puede lanzar excepciones
    
    
except IOError: # <- Error de Entrada y Salida (Objeto tipo IOError)
    # entrará aquí en caso que se haya producido
    # una excepción IOError
    
    
except ZeroDivisionError: ## <- Objeto tipo exception, ZeroDivisionError
    # entrará aquí en caso que se haya producido
    # una excepción ZeroDivisionError
    
    
except:
    # entrará aquí en caso que se haya producido
    # una excepción que no corresponda a ninguno
    # de los tipos especificados en los except previos
    
else: 
    # es mejor que agregar código adicional en el try porque
    # evita capturar accidentalmente una excepción que no 
    # fue generada por el código que está protegido por la 
    #sentencia try … except.
    
finally:
    # Código que se ejecutará luego de que pase el try catch. Siempre se ejecutará y no se espera otro error
```


```python
lista = [1, 2, 3, 4, 5]
try:
    lista[10]
except IndexError:
    print("Error: El índice se encuentra fuera del rango")
```


```python
import math

def RaizCuadrada(numero):
    try:
        return math.sqrt(numero)
    except ValueError:
        return 'Error al calcular raíz de ' + str(numero)

print(RaizCuadrada(4))
print(RaizCuadrada(13))
print(RaizCuadrada(100))
print(RaizCuadrada(-1))
print(RaizCuadrada(25))
```


```python
import sys ## Este solo funcionará en terminal y qué será sys?
for argumento in sys.argv[1:]:
    try:
        f = open(argumento, 'r')
    except IOError:
        print('no pude abrir', arg)
    else:
        print(argumento, 'tiene', len(f.readlines()), 'lineas')
        f.close()
```

### Levantar errores 🔥

Para qué querríamos provocar un error... eh? 

Bueno en muchos casos tapar el problema de los usuarios no es una buena práctica. Lo mejor es que los errores ocurran e irlos subiendo hasta poder manejarlo desde arriba. 

A qué me refiero con esto. Imaginemos que trabajamos en un proyecto con muchas clases, si tratamos de corregir todos los errores desde abajo será muy complicado revisar archivo por archivo a ver cuál try catch es que está mal. Mejor sube los errores y hasta un único try catch pones todos los casos.


```python
raise NameError('Te has equivocado')
```

## Módulos del sistema operativo  🦜

### OS 🍪

El módulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo. Sobre todo, aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular la estructura de directorios.

|Descripción|	Método|
|:----------|:-------:|
|Saber si se puede acceder a un archivo o directorio |	os.access(path, modo_de_acceso) |
|Conocer el directorio actual|	os.getcwd()|
|Cambiar de directorio de trabajo|	os.chdir(nuevo_path)|
|Cambiar al directorio de trabajo raíz|	os.chroot()|
|Cambiar los permisos de un archivo o directorio|	os.chmod(path, permisos)|
|Cambiar el propietario de un archivo o directorio|	os.chown(path, permisos)|
|Crear un directorio|	os.mkdir(path[, modo])|
|Crear directorios recursivamente|	os.mkdirs(path[, modo])|
|Eliminar un archivo|	os.remove(path)|
|Eliminar un directorio|	os.rmdir(path)|
|Eliminar directorios recursivamente|	os.removedirs(path)|
|Renombrar un archivo|	os.rename(actual, nuevo)|
|Crear un enlace simbólico|	os.symlink(path, nombre_destino)|


```python
import os 
os.listdir("./")
```


```python
os.getcwd()
```


```python
os.path.getsize("apache.txt") ## En bytes
```


```python
os.path.isfile("ArchivoQueNoExiste.jpg")
```


```python
os.path.isdir("CarpetaInexistente")
```


```python
os.rename("Ana_Poleo","Ana_Carolina")
```

## Manejadores de Contextos 🦏

Los administradores de contexto te permiten asignar y liberar recursos precisamente cuando lo desee. El ejemplo más utilizado de administradores de contexto es la declaración `with`. 

Suponga que tiene dos operaciones relacionadas que le gustaría ejecutar como un par, con un bloque de código en el medio. Los administradores de contexto le permiten hacer eso específicamente. Por ejemplo:



```python
with open('nombreArchivo', 'w') as MiArchivito: ## Acabamos de escribir un crear un archivo y ponerle Hola!
    MiArchivito.write('Hola!')
```

Que sería algo equivalente a lo siguiente, dejamos un conjunto de instrucciones que se harán en conjunto y las usaremos cuando las necesitemos.


```python
file = open('otroArchivo', 'w')
try:
    file.write('Hola x2!')
finally:
    file.close()
```

### Administrador de contexto como clase

Como mínimo, un administrador de contexto tiene definidos un método \__enter\__ y \__exit\__.


```python
class AperturaArchivos(object):
    def __init__(self, nombreArchivo, formaDeAbrir):
        self.objetoArchivo = open(nombreArchivo, formaDeAbrir)
    def __enter__(self):
        return self.objetoArchivo
    def __exit__(self, type, value, traceback):
        self.objetoArchivo.close()
```


```python
with ('NombreArchivo.txt', 'w') as archivoAbierto:
    archivoAbierto.write('Hola!')
```

## Expresiones Regulares 📝

Una expresión regular es un modelo con el que el motor de expresiones regulares intenta buscar una coincidencia en el texto de entrada. Un modelo consta de uno o más literales de carácter, operadores o estructuras.

**En otras palabras, buscamos PATRONES.**


La siguiente tabla nos muestra algunas formas de poder denotar un conjunto de símbolos por ejemplo un dígito puede escribirse como `\d` pero `\d+` significa todos los números de cualquier longitud.`\w` significa una letra pero `\w+` significa todas las palabras habidas y por haber de todos los idiomas. 

![](img/picu.png)


Digamos que somos desarrolladores de software en una compañía donde un programa nos genera un **LOG** (traducción: Bitácora) y este es un texto largo largo largo. Un log es como el chismógrafo donde cada acción que hagas o los printf() que coloque el programador van al registro, como su nombre lo dice, una bitácora.

Ejemplo:

    109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "GET /administrator/ HTTP/1.1" 200 4263 
    109.169.248.247 - - [13/Dec/2015:18:25:11 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 
    46.72.177.4 - - [15/Dec/2015:18:31:08 +0100] "GET /administrator/ HTTP/1.1" 200 4263 
    46.72.177.4 - - [15/Dec/2015:18:31:08 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494
    83.167.113.100 - - [17/Dec/2015:18:31:25 +0100] "GET /administrator/ HTTP/1.1" 200 4263 
    83.167.113.100 - - [18/Dec/2015:18:31:25 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 

Si su trabajo consistiera en, tengo un archivo con más de 100 Millones de éstas líneas, me respondan las siguientes preguntas:

- ¿Cuántas conexiones se realizaron del 12 al 15 de Diciembre por /administrator y con el método POST?
- ¿Cuántas conexiones GET de usuarios que no sean /administrator se realizaron en horario de 12 am a 9 am?
- ¿Cuántas conexiones fueron exitosas (Código 200) el 13 y 14 de Diciembre?

### ¿Nos ponemos a contar? 🤯 

Quien no tenga nada que hacer en cuarentena, adelante. Sin embargo podríamos calcularlo con solo unas cuántas líneas de código. Lo veremos más adelante, mientras tanto lo básico.

Python tiene un paquete incorporado llamado **re**, que se puede usar para trabajar con expresiones regulares.
Puedes comenzar a usar expresiones regulares usando el módulo **re**.

**Funciones incluidas en el paquete:**


- `findall`: Devuelve una lista que contiene todas las coincidencias
- `search`:	 Devuelve un objeto Match si hay una coincidencia en cualquier parte de la cadena
- `split`:	 Devuelve una lista donde la cadena se ha dividido en cada coincidencia
- `sub`:	 Reemplaza una o varias coincidencias con una cadena
- `match`:	 Determina si la expresión coincide al principio de la cadena


```python
import re

p = re.compile(r'((([1-9][0-9]*)|0)(u|U)?(l|L)?)')

x = p.findall('100')

print(x)

if x:
    print("Hay al menos una coincidencia!")
else:
    print("No hay coincidencias")
```


```python
expresion = "(([1-9][0-9]+)|0)(u|U)?(l|L)?"

correo = "12ul"

print(re.match(expresion, correo))

if re.match(expresion, correo):
    print("Es válida ✅")
else:
    print("NO es válida ❌")
```

## Contestemos las preguntas iniciales con un archivo externo

### 1. ¿Cuántas conexiones se realizaron del 12 al 15 de Diciembre por /administrator y con el método POST?

**Expresión regular:** `\d+\.\d+\.\d+\.\d+ - - \[1[2-5]\/Dec\/\d+:.{17}POST \/administrator\/.+`


```python
import re

#Compilamos nuestra expresión regular
miExpresionRegular = re.compile(r'\d+\.\d+\.\d+\.\d+ - - \[1[2-5]\/Dec\/\d+:.{17}POST \/administrator\/.+')

#Al abrir el archivo apache.log como 'archivo' has esto:

with open('apache.txt') as archivo:
    contenido = archivo.read()
    print("Número de conexiones del 12-15 Dic POST por administrador: ",len(miExpresionRegular.findall(contenido)))
    print("\nEjemplos: \n")
    print(miExpresionRegular.findall(contenido)[0]+"\n")
    print(miExpresionRegular.findall(contenido)[1])
```

### 2. ¿Cuántas conexiones GET de usuarios que no sean /administrator se realizaron en horario de 12 am a 9 am?

**Expresión regular:** `\d+\.\d+\.\d+\.\d+ - - \[\d+\/\w+\/\d+:0[0-9]:\d+:\d+ \+\d+\] "GET \/(?!administrator).+`


```python
import re

#Compilamos nuestra expresión regular
miExpresionRegular2 = re.compile(r'\d+\.\d+\.\d+\.\d+ - - \[\d+\/\w+\/\d+:0[0-9]:\d+:\d+ \+\d+\] "GET \/(?!administrator).+')

#Al abrir el archivo apache.log como 'archivo' has esto:

with open('apache.log') as archivo:
    contenido = archivo.read() # Lee su contenido
    print("Número de conexiones GET no realizadas por /administrator de 0 am a 9 am: ",len(miExpresionRegular2.findall(contenido))) #Imprime el tamaño del arreglo de todas las coincidencias
    print("\nEjemplos: \n") 
    print(miExpresionRegular2.findall(contenido)[0]+"\n")
    print(miExpresionRegular2.findall(contenido)[1])
```

### 3. ¿Cuántas conexiones fueron exitosas (Código 200) el 13 y 14 de Diciembre?

**Expresión regular:** `\d+\.\d+\.\d+\.\d+ - - \[1[3-4]\/Dec\/\d+:\d+:\d+:\d+ \+\d+\] "\w+ [^ ]+ [^ ]+ 200 .+`


```python
import re

#Compilamos nuestra expresión regular
miExpresionRegular3 = re.compile(r'\d+\.\d+\.\d+\.\d+ - - \[1[3-4]\/Dec\/\d+:\d+:\d+:\d+ \+\d+\] "\w+ [^ ]+ [^ ]+ 200 .+')

#Al abrir el archivo apache.log como 'archivo' has esto:

with open('apache.log') as archivo:
    contenido = archivo.read() # Lee su contenido
    print("Conexiones Exitosas (200) el 13 y 14 de Diciembre: ",len(miExpresionRegular3.findall(contenido))) #Imprime el tamaño del arreglo de todas las coincidencias
    print("\nEjemplos: \n") 
    print(miExpresionRegular3.findall(contenido)[0]+"\n")
    print(miExpresionRegular3.findall(contenido)[1])
```

# Bases de Datos ⛴

### Diseño Físico, Diseño Lógico (Relacional) y Diseño Conceptual (E-R)

El modelo relacional, para el modelado y la gestión de bases de datos, es un modelo de datos basado en la lógica de predicados y en la teoría de conjuntos.


```python
import mysql.connector

#Creamos el conector a la BD
mydb = mysql.connector.connect(
  host="pythoninter.c7rbflvluzyk.us-east-2.rds.amazonaws.com",
  user="admin",
  password="proteco123"
)

## Creamos un cursor por la conexión creada--------------------------------------------
cursor1 = mydb.cursor()
cursor1.execute("CREATE DATABASE asistente") ## FAVOR DE CREAR UNA BASE DE DATOS LLAMADA asistente_<numero_asistente>
cursor1.execute("SHOW DATABASES")   ### Ej: asistente_1, asistente_2, asistente_3, etc.
print("Mis bases de datos son: ")
for baseDatos in cursor1:
    print(baseDatos)

cursor1.execute("use asistente") ## FAVOR DE INGRESAR asistente_<su_numero> ------------

        
## Creamos otro cursor y creamos una entidad en la base de datos

cursor2 = mydb.cursor()
cursor2.execute("""CREATE TABLE PROFESOR (ID INT AUTO_INCREMENT PRIMARY KEY, 
                                          NOMBRE VARCHAR(40),
                                          APELLIDO_PAT VARCHAR(40),
                                          APELLIDO_MAT VARCHAR(40),
                                          EDAD INT,
                                          DOMICILIO VARCHAR(255),
                                          SALARIO DECIMAL(5,2))
                                          """);

print("\nSe ha creado la entidad de profesor")

######## --------- Creamos unos objetos profesores.


class Profesor:
    def __init__(self,id,nombre,apellido_pat,apellido_mat,edad,domicilio,salario):
        self.id = id
        self.nombre = nombre
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.edad = edad
        self.domicilio = domicilio
        self.salario = salario   

missConchi = Profesor(1,'Ana Concepción','Castillo','Corona',33,'Av.Robles, Tabasco, Mex',13000)
mrRafa     = Profesor(2,'Rafael','García','Rueda',44,'Av. Maya, Tabasco, Mex',12000)
missDulce  = Profesor(3,'Dulce Mónica','Escalante','Garrido',30,'Av. Olmeca, Campeche, Mex',12000)
missLoli   = Profesor(4,'Maria Dolores','Taracena','Blé',31,'Av. Palenque, Chiapas, Mex',15000)

#Hacemos una lista de objetos profesor
listaDeProfesores = [missConchi,mrRafa,missDulce,missLoli]

print("Se han creado objetos de la clase Profesor y los hemos puesto en una lista ")
## Hacemos la instrucción SQL

sql = "INSERT INTO PROFESOR (NOMBRE, APELLIDO_PAT,APELLIDO_MAT,EDAD,DOMICILIO,SALARIO) VALUES (%s,%s,%s,%s,%s,%s)"

# Y mandamos a través del SQL y de la lista de profesores los datos a la base de datos en MySQL

for profe in listaDeProfesores:
    valores = (profe.nombre, profe.apellido_pat,profe.apellido_mat,profe.edad,profe.domicilio,profe.salario)
    cursor2.execute(sql, valores)

print("Se han insertado a los profesores en la base")

mydb.commit() ## Confirmamos los cambios

## Por buenas prácticas, cerramos todas las conexiones

if cursor1.close() and cursor2.close():
    print("Se han cerrado correctamente las conexiones :)")
    print("Algoritmo finalizado!")
```


```python
otroCursor = mydb.cursor()

otroCursor.execute("SELECT * FROM PROFESOR")

consulta = otroCursor.fetchall()

for fila in consulta:
    print(fila)
    
otroCursor.close()
```


```python
cursorDelete = mydb.cursor()
cursorDelete.execute("DROP DATABASE asistente")
cursorDelete.close()
```


```python
import cx_Oracle as orcl

## DATOS DE CONEXIÓN
dsn_tns = orcl.makedsn('clasespring.c7rbflvluzyk.us-east-2.rds.amazonaws.com',
                            '1521',
                            'ORCL')

BasedeDatos = orcl.connect(user='spring', password='hola1234', dsn=dsn_tns)
```


```python
## CREACIÓN DE LA TABLA O ENTIDAD

# Para poder ejecutar un comando SQL dentro de Python usaremos: el objeto BaseDeDatos, tiene un objeto cursor
## Y este a su vez tiene un método llamado Execute que ejecuta un SQL en forma de cadena String.

BasedeDatos.cursor().execute("""CREATE TABLE PROFESOR(
                                ID number (10,0) NOT NULL,
                                NOMBRE VARCHAR2(30),
                                APELLIDO_PAT VARCHAR2(30),
                                APELLIDO_MAT VARCHAR2(30),
                                EDAD NUMBER(3,0),
                                DOMICILIO VARCHAR2(100),
                                SALARIO NUMBER(10,2))
                                """ )

BasedeDatos.autocommit = True  ## PARA QUE GUARDE LOS CAMBIOS AUTOMÁTICAMENTE
```


```python
# INSERCIÓN DE DATOS
## Imaginemos que creamos objetos de tipo profesor con estos atributos

class Profesor:
    def __init__(self,id,nombre,apellido_pat,apellido_mat,edad,domicilio,salario):
        self.id = id
        self.nombre = nombre
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.edad = edad
        self.domicilio = domicilio
        self.salario = salario

## creamos a missConchi, a mrRafa, a missDulce y a missLoli, todos objetos de tipo Profesor

missConchi = Profesor(1,'Ana Concepción','Castillo','Corona',33,'Av.Robles, Tabasco, Mex',13000)
mrRafa     = Profesor(2,'Rafael','García','Rueda',44,'Av. Maya, Tabasco, Mex',12000)
missDulce  = Profesor(3,'Dulce Mónica','Escalante','Garrido',30,'Av. Olmeca, Campeche, Mex',12000)
missLoli   = Profesor(4,'Maria Dolores','Taracena','Blé',31,'Av. Palenque, Chiapas, Mex',15000)

# Hacemos una lista de profesores

listaDeProfesores = [missConchi,mrRafa,missDulce,missLoli]
```


```python
sqls = [] # Y una lista para poder poner nuestras cadenas de texto SQL

#Ahora hacemos los strings SQL para ver qué tal quedan

for profe in listaDeProfesores:
    comandosql = 'INSERT INTO PROFESOR VALUES ('+str(profe.id)+',\''+profe.nombre+'\',\''+profe.apellido_pat+'\',\''+profe.apellido_mat+'\','+str(profe.edad)+',\''+profe.domicilio+'\','+str(profe.salario)+')'
    print(comandosql)
    sqls.append(comandosql)

for comandos in sqls:
    BasedeDatos.cursor().execute(comandos)
```

    INSERT INTO PROFESOR VALUES (1,'Ana Concepción','Castillo','Corona',33,'Av.Robles, Tabasco, Mex',13000)
    INSERT INTO PROFESOR VALUES (2,'Rafael','García','Rueda',44,'Av. Maya, Tabasco, Mex',12000)
    INSERT INTO PROFESOR VALUES (3,'Dulce Mónica','Escalante','Garrido',30,'Av. Olmeca, Campeche, Mex',12000)
    INSERT INTO PROFESOR VALUES (4,'Maria Dolores','Taracena','Blé',31,'Av. Palenque, Chiapas, Mex',15000)



```python
## RECUPERAR INFORMACIÓN DE ESA BASE DE DATOS

cursor = BasedeDatos.cursor() ## El curso se utiliza para recorrer cada fila
cursor.execute('SELECT * FROM CARRERAS') # Ejecuta la instrucción SQL


for fila in cursor: ## Para cada fila que encuentre en la tabla(s)
    print(fila)

BasedeDatos.cursor().close()
```

    (1, 'Ana Concepción', 'Castillo', 'Corona', 33, 'Av.Robles, Tabasco, Mex', 13000.0)
    (2, 'Rafael', 'García', 'Rueda', 44, 'Av. Maya, Tabasco, Mex', 12000.0)
    (3, 'Dulce Mónica', 'Escalante', 'Garrido', 30, 'Av. Olmeca, Campeche, Mex', 12000.0)
    (4, 'Maria Dolores', 'Taracena', 'Blé', 31, 'Av. Palenque, Chiapas, Mex', 15000.0)
    (5, 'Hernando', 'Huerta', 'Echeverria', 50, 'Calle Xochitenco, Cd.Nezahualcoyotl, Mex', 10000.0)
    (5, 'Jose Luis', 'Pulido', 'Becerril', 45, 'Calle Loma bonita, Cd.Nezahualcoyotl, Mex', 10000.0)


## Sockets en Python 🧩

En python podemos hacer uso de los Sockets para poder recibir o mandar paquetes de información entre dispositivos. Lo que se necesita para abrir un socket es una dirección IP y un puerto. 

## La parte del Servidor ⚽️


```python
import socket  
  
s = socket.socket()   
s.bind(("localhost", 9999))  
s.listen(1)  
  
sc, addr = s.accept()  
  
while True:  
    recibido = sc.recv(1024)  
      
    if recibido == "quit":
        print("adios")  
        break        
    print("Recibido:", recibido ) 
    sc.send(recibido)  
sc.close()  
s.close() 
```

## La parte del cliente 🏀


```python
import socket  
  
s = socket.socket()   
s.connect(("localhost", 9999))  
  
while True:  
    mensaje = raw_input("> ")  
    s.send(mensaje)  
    if mensaje == "quit":  
        break  

print("adios")  
  
s.close() 
```

