
# El lenguaje de programación Python🐍

 **<div style="text-align: right"> Samuel Arturo Garrido Sánchez</div>**


```python
print("Hola n!")  #Es costumbre entre los programadores
#(Postdata, esto es un comentario)
```

Python es un lenguaje de programación **multiparadigma**, muy útil para demasiadas ramas de la investigación, desarrollos y procesos. 
Su filosofía radica en un código legible que cualquier persona no enfocada en el área de programación, pueda comprender.

![](img/let.png)

$$ x^2 = \int_0^9 x $$

# ¿Qué es Python?

Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.

Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.

Es administrado por la Python Software Foundation. Posee una licencia de código abierto, denominada Python Software Foundation License, que es compatible con la Licencia pública general de GNU a partir de la versión 2.1.1, e incompatible en ciertas versiones anteriores.

![](img/python.jpg)

### Las ventajas de Python pueden ser muchas pero en las que destacan:

- La cantidad de librerías que contiene, tipos de datos y funciones incorporadas en el propio lenguaje, que ayudan a realizar muchas tareas habituales sin necesidad de tener que programarlas desde cero.

- La sencillez y velocidad con la que se crean los programas. Un programa en Python puede tener de 3 a 5 líneas de código menos que su equivalente en Java o C.

- La cantidad de plataformas en las que podemos desarrollar, como Unix, Windows, OS/2, Mac, Amiga y otros.

- Además, Python es gratuito, incluso para propósitos empresariales.

### Filosofía Python

La filosofía que rigen las personas que de sean programar en Pythonn están escritas en The Zen of Python (PEP 20), que incluye:

- Hermoso es mejor que feo
- Explícito es mejor que implícito
- Simple es mejor que complejo
- Elaborado es mejor que complicado
- La legibilidad cuenta.

## Y a todo esto, ¿cómo se instala?

### Windows


https://www.python.org/downloads/windows/. 

Click en el enlace "Latest Python 3 Release -Python x.x.x". Si tu ordenador ejecuta la versión de 64 bits de Windows, descarga Windows x86-64 executable installer. De lo contrario, descarga Windows x86 executable installer. Después de descargar el instalador, deberías ejecutarlo (dándole doble click) y seguir las instrucciones.

Una cosa para tener en cuenta: Durante la instalación, verás una ventana de "Setup". Asegúrate de marcar las casillas "Add Python 3.6 to PATH" o "Add Python to your environment variables" y hacer click en "Install Now", como se muestra aquí (puede que se vea un poco diferente si estás instalando una versión diferente)

![](img/windows.png)

### Mac

Si has utilizado GNU/Linux alguna vez habrás escuchado la palabra sistema de gestor de paquetes. En macOS se cuenta con ello también, para poder instalar componentes extras a nuestro ordenador.

![](img/scr4.png)

En escencia para instalar **Python, PHP nativo, MySQL**, y entre más cosas como kits para desarrollar entre otras podrán ser descargadas solo con el comando:


```console
MacBook-Pro-de-Sam:~$ brew install <Lo que quieras instalar>
```

Para poder instalar homebrew necesitarás colocar ésto en tu terminal. Lo usaremos mucho en éste curso y lo usarás mucho si serás desarrollador en general.

```console
MacBook-Pro-de-Sam:~$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

En nuestro caso, una vez instalado Homebrew en nuestra Mac, en la terminal insertaremos: brew install python.
Y se instalará automáticamente.

### Linux


Para los Pro, dependiendo la distribución de linux que tengan, **Fedora, Ubuntu, OpenSUSE**.

En la terminal colocan el comando:

#### Debians (Ubuntu, Mint, etc.) 
```console
:~$ sudo apt-get install python3
```

#### Fedora
```console
:~$ sudo dnf install python3
```

#### OpenSUSE
```console
:~$ sudo zypper install python3
```

## ¿Y quién desarrolló todo esto? ❤️

<p>
  <img src="img/Guido.jpg" align = "right"  width="130" />
</p>

Python fue creado a finales de los ochenta3 por **Guido van Rossum** en el Centro para las Matemáticas y la Informática (CWI, Centrum Wiskunde & Informatica), en los Países Bajos, como un sucesor del lenguaje de programación ABC, capaz de manejar excepciones e interactuar con el sistema operativo Amoeba.

**El nombre del lenguaje proviene de la afición de su creador por los humoristas británicos Monty Python.**

Van Rossum es el principal autor de Python, y su continuo rol central en decidir la dirección de Python es reconocido, refiriéndose a él como Benevolente Dictador Vitalicio (en inglés: Benevolent Dictator for Life, BDFL)

## Ejemplos de uso de Python

### Álgebra: Solución a un sistema de ecuaciones

Podemos usar Python para encontrar la solución a un sistema de ecuaciones.

Tenemos el siguiente sistema de ecuaciones:

$$ 2x + y - 3z = 7 $$
$$ 5x - 4y + z = -19  $$
$$ x - y - 4z = 4 $$

Buscaremos la solución del sistema a través de python con uso de matrices.


```python
import numpy as np                            #Importar una biblioteca
A = np.matrix([[2,1,-3],[5,-4,1],[1,-1,-4]])  #Matriz A
B = np.matrix([[7],[-19],[4]])                #Matriz B
X = A**(-1)*B                                 #Inversa de matriz A por B
print("El resultado es: \n",X)                #Impresión de la solución
```

### Crear ventanas: Interfaz gráfica

Podemos importar Tkinter que nos permite la creación de entornos gráficos tales como botones, ventanas, textfields, etc, aunque tendremos que definir desde lo que contendrán éstos elementos hasta su posición x, y.


```python
from tkinter import *

def MainVentana(): #Esto es una función
    primerVentana=Tk()
    primerVentana.geometry("700x700+50+50") 
    primerVentana.mainloop()

MainVentana()
```

### Buscador de palabras: Expresiones regulares

Dentro del mundo del big data y minería de datos, la búsqueda de elementos dentro de grandes archivos es escencial. RE se encarga de esto.


```python
import re
texto = "En esta cadena existe una palabra magica"
print(re.search("magica",texto))
print(re.search("hola",texto))


# Match en palabras dentro de Strings
```

### Gráficas

Para el área de ciencias e ingenierías, los grafos son instrumentos escenciales para poder dar una interpretación de imagen a un fenómeno, de esta manera, la mente humana pueda analizar mejor dicha información.


```python
from matplotlib import pyplot

def f(x):
    y = x**2
    return y

x = range(-10,11)
pyplot.plot(x, [f(i) for i in x])
print("Gráfica de f(x) = x^2")
pyplot.show()
```

## Python es usado para muchísimas otras cosas como: 

* Creación de modelos predictivos (Machine Learning).
* Creación de Sockets (comunicación entre computadores).
* Creación del backend de páginas web junto con php.
* Inteligencia Artificial
* Realizar simulaciones de fenómenos físicos
* Scripts que ayudan al funcionamiento de muchos programas que usamos (Mac OS tiene Python 2.7 de fábrica)
* **Y mucho, muuuuchooo más**



# <center> 🖥   ¿Qué esperamos?   🖍 </center>

## Tipos de "datos" - (objetos)

En Python, todas las **variables son objetos**. Todas las cosas que "declaremos", que reside en algún lugar de la memoria, posee un identificador único que lo diferencia del resto. Piensa en él como si fuera su INE. Para conocer ese identificador, Python dispone de la función id().


```python
numero = 6.989796967
id(numero)
print(id(numero))
```

**Al contrario de otros lenguajes de programación como Java, no es necesario declarar el tipo de variable que se crea.**

Los tipos de datos primitivos no existen como tal en Python, sin embargo podemos saber el tipo de dato que contiene una variable con el método type(dato)


```python
# Los enteros
opcion = 5 
print(opcion)
type(opcion)
```

Una cadena o String es un tipo de dato que guarda una oración o conjunto de letras, símbolos y números para tratarlo como uno solo. En C en cambio un "String" en realidad es un arreglo de caracteres.


```python
saludo = str("Hola")
print(saludo)
saludo1 = "Las saladitas son horneadas"
print(saludo1)
```


```python
#Floats
# ESto es un comentario


enunciado = "Un automóvil se movió 1135.67 metros en 140.86 segundos. Calcule su velocidad"

distancia = 1135.67
tiempo = 140.86 

velocidad = distancia/(tiempo**2)

print(enunciado)
print("\n \t La velocidad del automóvil fue:",velocidad,"m/s")
```

### Operadores y comparadores matemáticos

Dentro de la programación existe mucha lógica. Varios elementos de comparación en matemáticas como lo es <, >, ≤, ≥, ≠(!=), o algún método dentro de los objetos tienen la función de devolver un elemento **BOOLEANO** (BOOLEANO: TRUE OR FALSE). Nos devuelve este booleano para determinar si es cierto o falso el enunciado del código.


```python
a = 6
b = 5
c = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print("\n")
print(a%b)
#ESTO encuentra el residuo de la división o la congruencia de un número con un módulo



print("\n")
print(a == b) # un signo = significa asignación, == doble significa preguntar si son iguales a python
print(b == c)
print(a<5) #a es menor que 5
print(b>c)
print(c!=6)

# No solamente se pueden comparar números

texto1 = "Hola, ¿qué tal?"
texto2 = "Hola, qué tal?"
print(texto1 == texto2)

```


```python
par = 11%2
par == 0
```


```python
# Booleanos

#Ejercicio: Quitar la variable de "puedoSalirAlCine" pero obtener el mismo resultado

puedoSalirAlCine = bool() # ¿Por qué no viene al caso hacer ésto?

tareas = 8 # Un control de flujo if/else -> próxima clase
if tareas < 8:
    if puedoSalirAlCine:
        print("Yeih! 😁")
    else:
        print("No yeih ☹️")
        puedoSalirAlCine = False
else:
    puedoSalirAlCine = True


```

**<center>¿Y cómo ingreso elementos a la ejecución (a manera de Scanner)? </center>**


```python
numeroInsertado = int(input("Ingrese un número: ")) # ¿Por qué el int al principio? Pista: String
if numeroInsertado  < 5:
    print("😀")
elif numeroInsertado < 10: #O elif?
    print("⭐️")
    
elif numeroInsertado < 30:
    print("🍀")
else:
    print("Es más grande que 30")
```

### Palabras reservadas: 👀

Las palabras reservadas son un conjunto de palabras que **NO** podremos usar como nombre de nuestas variables ya que python sabe que tiene que realizar ciertas acciones si se encuentra con alguna de éstas palabras. Entre las cuales podemos encontrar:

- and
- if
- del
- else
- for
- elif
- is
- from
- raise
- lambda
- assert
- return
- break
- global
- not
- try
- class
- except
- or
- while
- continue
- exec
- import
- yield
- def
- finally
- print

**No vayan a intentar usar alguna de éstas palabras como nombre de sus variables o no funcionará su programa**

## Operadores lógicos.

Los operadores lógicos son los que trabajan con valores booleanos, nos devuelven falso o verdadero y son la escencia de las condiciones

### Operador AND

El operador and evalúa si las condiciones TODAS se cumplen:

#### Ejemplo de ayer:


```python
True and False
```


```python
examenes = int(input("Ingrese el número de exámenes: "))
tareas = int(input("Ingrese el número de tareas: "))
participaciones = int(input("Ingrese el número de participaciones: "))

if examenes >= 10 and tareas >=10 and participaciones >=10:
    print("Podrás ir a la peda")
else:
    print("Híjole creo que no se va a poder")
```

### Operador OR

El operador or evalúa si ALGUNO DE LOS VALORES ES VERDADERO


```python
tengoPaseFiesta = False
miCompaTiene = True

if tengoPaseFiesta or miCompaTiene:
    print("Podemos pasar")
else:
    print("Nos quedamos fuera")
```


```python
edad = 18
dinero = 10000
fama = 80 #supongamos que se mide del 1 al 100

if edad >= 18 or dinero >= 1000 or fama >= 50:
    print("Ya llegué paps")
else:
    print("No te preocupes príncipe, ahí para la otra")
```

### Operador NOT

El operador not devuelve el valor opuesto al valor booleano


```python
not True
```


```python
mayonesa1 = "Hellmans"
mayonesa2 = "Nestlé"

if mayonesa1 is not "McCORMICK":
    print("Un toque del sabor de mayonesa McCORMICK")
    
if mayonesa2 != "McCORMICK":
    print("Un toque del sabor de mayonesa McCORMICK")
```

Aquí aparece una situación. **IS**: Bastante frecuente que se use de sinónimos a is y == o is not con !=. Aunque suelen funciona de forma similar sus comportamientos no son exactamente iguales. 


**is** devolverá TRUE si las 2 variables apuntan al mismo objecto.

**==** devolverá True si los valores de las variables son iguales.



```python
a = 1000

b = 999

```


```python
a is b
```


```python
a == b +1
```

### ¿Se pueden combinar todo lo visto hasta ahora? Sí


```python
a = 5==5 
b = True
c = 5 is not 7

if not((a or b) and c):
    print("Ya les dio calambre cerebral?")
else:
    print("Todavía")
```

## Colecciones 🐆

### Mutabilidad

La mutabilidad radica si un elemento dentro de un objeto o el objeto mismo puede cambiar algún atributo que posea. Si es mutable, podemos hacer el cambio, en caso contrario recibiremos un error.

### Listas

Son colecciones de elementos que permiten la mutabilidad de elementos. Existen una serie de funciones que nos permiten interactuar con una lista. Para una función solo agregamos a la lista un punto, seguido de la función y sus parámetros.     **lista.funcion(parámetro)**

**Métodos importantes:**  append(x), insert(i, x), remove(x), pop( ), clear( ), index(x), count(x), sort( ), len( )*

**<center> Actividad: ¿Para qué sirve cada uno? </center>** 


```python
lista = [4, 8, 16, 43, 23, 300, 44, 76, 65,44,44]
print(lista)
print(lista[8])
lista.append(100)
print(lista)

print(len(lista))
```


```python
lista = [4, 8, 16, 43, 23, 300, 29, 44, 76, 65]

print(lista)

lista.append(8)
print(lista)

lista.remove(16)
print(lista)

print(lista.index(300))

lista.sort()
print(lista)
```


```python
# ¿Se podrá hacer una lista de elementos múltiples?

otraLista = [[[1,2],2,4],[4,5,6],[8,9,0]]

print(otraLista[0][0][0])
```

Como **TODO** es un objeto en Python en teoría la lista contiene elementos del mismo tipo: Objetos con diferentes parámetros. Por lo tanto es posible una lista con diferentes tipos de datos.

### Tuplas

Como las listas, las tuplas siguen la misma estructura. Son idénticas a las listas pero con una pequeña excepción: No son mutables. Si tratamos de cambiar algún elemento por otro o eliminar, nos marcará un error.


```python
tupla = (16,53,23,76,98,43,56,99,77,21,32) #Se usan paréntesis en lugar de corchetes
print(tupla[1])
```

Los errores generados son gracias a que queríamos modificar una tupla la cual no permite la asignación o no tiene el  método pop o similares que modifican a la misma. Podemos probar los métodos que no manipulen su estructura.


```python
print(tupla.index(99))
```

**Y a todo ésto... ¿Para qué necesitamos tuplas si tenemos listas?**


```python
x = [1,2,3,4,5]
y = x
print(y)
```


```python
x[0] = 10
print(y)
```


```python
id(x) == id(y)
```


```python
z = (1,2,3,4,5)
y = z
x[1] = 50
print(x)
print(y)
print(z)

p = (1,2)
q = [1,2]

p is q
```

### Diccionarios

Los diccionarios son lo equivalente a tablas Hash, a cada llave se le asigna un valor. De manera sencilla podemos dar un ejemplo: Tenemos un buró con muchos cajones, en los cajones podemos guardar cosas que en este caso serán variables y cuando queramos buscar una crema en el buró, naturalmente tendremos qué saber en qué cajón está. Los cajones tienen una referencia (el cajón de abajo por ejemplo) y en el caso de los diccionarios, las llaves son los cajones y guardan variables.


```python
miDiccionario = {"Hola":[(1,2),6,7,True],"verde":"kiwi","amarillo":"platano"}
```


```python
print(miDiccionario["Hola"][0][1])
```


```python
print(otroDiccionario[True])
```


```python
print(otroDiccionario["p"][0]) ## para ir por el elemento dentro del arreglo.
```

Como podemos ver, se hace una colección de elementos para podernos referirnos a éstos más adelante por otro nombre o con una llave.

**Hasta éste momento:**

## <center> [ ] corchetes para listas -> mutable</center>

## <center> ( ) paréntesis para tuplas -> inmutable </center>

## <center> { } llaves para diccionarios -> cajones </center>

 

# <center> 🤨 ¿DUDAS? 👀</center>


```python
profesores = ["Laura","Samuel","Otro","Hola"]
if profesores[0] == "Laura":
    print("Laura se encuentra en la posición: ",profesores.index("Laura"))
if len(profesores) == 3:
    print("Hay 3 profesores en el curso")
else:
    profesores.append("Fulano")
    print(profesores)
```


```python
arreglo = [1,2,3,4,5]
if arreglo[1]*arreglo[2] == 2:
    print(2)
elif arreglo[3]*arreglo[2] == 12:
    print(12)
elif arreglo[1]*arreglo[3] == 8: # ¿Qué pasaría si reemplazo elif por if?
    print(8)
else:
    print(0)
```

## Ciclos

Los ciclos nos permiten hacer repeticiones de procesos dentro de un rango que nosotros determinemos. Esto es útil para NO hacer cada uno de los procesos, por lo que haríamos líneas de código innecesarias. (Además, ¡qué flojera!)

### Ciclo for (para cada)

Los ciclos for en python funcionan tienen una estructura algo distinta en Python que por ejemplo C o Java. Para poder utilizarlo tendremos que hacer uso de la palabra reservada **in** y luego a decisión,

La función range() nos devuelve un arreglo de números.

Si range(x) le insertamos solo 1 parámetro, **"x"** simboliza el punto de llegada -1 desde 0 de 1 en 1.

Si a range(x,y) le insertamos 2 parámetros, **"x"** simboliza el punto de partida y **"y"** el punto de llegada -1 y va contando de 1 en 1 hasta llegar.

Si a range(x,y,z) le insertamos 3 parámetros, **"x"** simboliza el punto de partida, **"y"** el punto de llegada -1 y z de cuanto en cuánto va salteando.


```python
jaja = [1,4,6,8]
jaja.append(1)
jaja.append(2)
jaja.append(3)
print(jaja)
```


```python
listaNormal = []

for numeroInsertar in range(-4,-60,-2):
        listaNormal.append(numeroInsertar)

print(listaNormal)
```


```python
a = range(10)
b = range(-10,10)
c = range(-10,10,2)

for i in a:
    print(i)
print("\n")
for i in b:
    print(i)
print("\n")
for i in c:
    print(i)
```

Los ciclos for responden a range() y a una colección (lista, tupla o diccionario) para que sea recorrido. No es necesario colocar contadores adicionales.


```python
for i in [1,5,9,2,6,9,0]:
    print(i)
```


```python
jaja2 = [1,4,6,8]
for i in range(0,3,1): # ¿Cómo modifico ésto para que sea más sencillo?
    jaja2.append(i)
print(jaja2)
```


```python
frutas = {'Fresa':'Roja','Limón':'Verde','Papaya':'Naranja','Manzana':'amarilla','Guayaba':'rosa'}
for llave in frutas:
    print(llave, 'es de color', frutas[llave])
    
```

## Ciclos while

El ciclo while permite ejecutar un bloque de instrucciones mientras se cumpla la condición dada. Primero comprueba que en efecto se cumple la condición dada y entonces, ejecuta el segmento de código correspondiente hasta que la condición no se cumpla.


```python
numero = 0
while numero <= 10:
    print(numero)
    numero += 1
```


```python
nombre = ""

while not nombre:
    nombre = input('Escribe tu nombre')
```


```python
while True:
    entrada = input('Escibe tu nombre: ')
    if not entrada: 
        break
```

## Algunos elementos que nos pueden servir en ambos ciclos: Controles de bucles

#### Break: 
Nos permite romper el ciclo, o sea que deje de ciclar


```python
for number in range(10):
    if number == 5:
        break    # break here

    print('El número es: ',number)
    
print('Se murió')
```

    El número es:  0
    El número es:  1
    El número es:  2
    El número es:  3
    El número es:  4
    Se murió
    El número es:  0
    El número es:  1
    El número es:  2
    El número es:  3
    El número es:  4
    Se murió



```python
ejemplo = 0
while True:   
    if ejemplo == 6:
        break
    print(ejemplo)
    ejemplo += 1
```

    0
    1
    2
    3
    4
    5
    0
    1
    2
    3
    4
    5


#### Continue: 
Nos permite saltar uno o muchos pasos de todo el ciclo por si a caso no los queremos


```python
for numero in range(10):
    if numero == 5 or numero == 4:
        continue    # continue here
    print(numero)
```

    0
    1
    2
    3
    6
    7
    8
    9
    0
    1
    2
    3
    6
    7
    8
    9


#### Pass: 
Por ultimo tenemos a pass, que tal como su nombre lo indica es una operación nula, o sea que no pasa nada cuando se ejecuta. Se utiliza cuando se requiere por sintaxis una declaración pero no se quiere ejecutar ningún comando o código. También se utiliza en lugares donde donde el código irá finalmente, pero no ha sido escrita todavía


```python
for number in range(10):
    if number == 5:
        print("Hola")
        pass
        print("Adiós")
    print('Number is ' + str(number))

print('Out of loop')
```

    Number is 0
    Number is 1
    Number is 2
    Number is 3
    Number is 4
    Hola
    Adiós
    Number is 5
    Number is 6
    Number is 7
    Number is 8
    Number is 9
    Out of loop
    Number is 0
    Number is 1
    Number is 2
    Number is 3
    Number is 4
    Hola
    Adiós
    Number is 5
    Number is 6
    Number is 7
    Number is 8
    Number is 9
    Out of loop


### Listas por comprensión

No, no es comprender literalmente las listas o tuplas o lo que sea, significa que podemos ahorrarnos unas líneas de código escribiendo o creando una lista con un for dentro. Veamos un ejemplo:


```python
saludo = "ola ke ace"
print(saludo)

print(saludo.capitalize())
```

    ola ke ace
    Ola ke ace
    ola ke ace
    Ola ke ace



```python
lenguajes = ["python", "c", "c++", "java","swift","kotlin","c#","shell","php","js"]
lenguajesEnMayusculas = []

for cadaUno in lenguajes:
    lenguajesEnMayusculas.append(cadaUno.capitalize())

print(lenguajesEnMayusculas)
```

    ['Python', 'C', 'C++', 'Java', 'Swift', 'Kotlin', 'C#', 'Shell', 'Php', 'Js']
    ['Python', 'C', 'C++', 'Java', 'Swift', 'Kotlin', 'C#', 'Shell', 'Php', 'Js']



```python
##Podemos reducirlo a ésto:
otraVezEnMayusculas = [cadaLenguaje.capitalize() for cadaLenguaje in lenguajes]
print(otraVezEnMayusculas)
```


```python
numeros = [1, 2, 3, 4, 5]
alcuadrado = [n ** 2 for n in numeros]
print(alcuadrado)
```

## Preparados listos: Funciones ⭐️

Una función es un bloque de código con un nombre asociado, que recibe cero o más argumentos como entrada, sigue una secuencia de sentencias, la cuales ejecuta una operación deseada y devuelve un valor y/o realiza una tarea.

La sentencia def es una definición de función usada para crear objetos funciones definidas por el usuario.


```python
 def hola(nombre):   # def: Se utiliza siempre que queramos definir una función
        print("Hola", nombre, "!")
```


```python
hola("Alicia")
```

    Hola Alicia !
    Hola Alicia !


### ¿Cómo se le conoce a lo que va entre paréntesis? 
Al definir una función los valores los cuales se reciben se denominan parámetros, pero durante la llamada los valores que se envían se denominan argumentos


```python
def suma(a,b): ## Aquí a y b se le conoce como parámetros
    print(a+b)

suma(5,2) ## aquí a 5 y 2 se le denomina argumentos
```

    7
    7



```python
def f(x,y):
    print(x**2 + 2*x + 1 + y**2)

f(2,4)
```

    25
    25


### Valores de retorno
Qué tal si queremos lo que suceda dentro de la función para otras cosas, no sé digamos que hace una operación matemática y queremos el resultado para otras cuentas. Existe algo que se llama return o valor retorno que quiere decir lo que devuelve la función



```python
def suma(a, b):
    return a + b

print(suma(5,3))
```

    8
    8



```python
## Achis achis y mi suma?

print(suma(5,3))
```


```python
#Vamos a ver un ejemplo matemático x^2

def f(x):
    y = x**2
    return y

operacion = f(5) + 10
print(operacion)
```

    35
    35



```python
## Se puede llamar a los parámetros de una función por posición o por nombre:

def algo(a,b):
    print(a-b)
    
algo(5,1)
algo(b=5,a=1)
```

    4
    -4
    4
    -4



```python
## También puede tener parámetros por defecto:

def cosa(a=0,b=5):
    print(a-b)
    
cosa()
cosa(b=5,a=1)
cosa(10,1)
```

    -5
    -4
    9
    -5
    -4
    9



```python
## Puede haber una función dentro de otra?

def funcion(p,q):
    r = p + q
    
    def funcion2(s):
        print(s)
        
    funcion2(5)

print(funcion(8,8))
```

    5
    None
    5
    None



```python
def multiplo(n):
    def multiploDe(num):
        return num%n == 0
    return multiploDe
(multiplo(9))(3)
```




    False






    False




```python
(multiplo(3))(9)
```


```python
##Podemos mandar de lo que sea a los parámetros, hasta listas:

def sumar(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(sumar([4,5]))
```

    9
    9


## Ejercicio: Hacer una calculadora 🧮

- Suma
- Resta
- Multiplicación
- División
- Cuadrado
- Residuo

## Recursividad: Llamada a sí misma de una función

![](remote.jpg)


```python
print("Trump: Hey siri, how many miles did i ran today?")
print("Siri: ok, sending missiles to Iran today!")

def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print(numero)

cuenta_regresiva(5)
```


```python
def factorial(numero):
    if numero > 1:
        numero = numero * factorial(numero -1)
    print ("Factorial de: ",numero)
    return numero
print("El factorial de 9 es: ",factorial(9))
```

## Iteradores y generadores
Los "iteradores" y "generadores" son objetos que cuentan con el método __next__(), el cual regresa una serie de objetos de uno en uno cada vez que es invocado.


```python
lista = ['1', 2, 'tres', 4.0]
print(lista)
```


```python
iterador = iter(lista)
print(iterador)
```


```python
next(iterador)
```


```python
next(iterador)
```


```python
next(iterador)
```

### Yield
Básicamente los generadores se escriben funciones normales, pero usan la sentencia yield en vez de un return dentro de un bucle. Yield funciona de manera similar al return, pero la gracia de usar el yield es que conserva la iteración del bucle para la siguiente vez que se le invoque


```python
def contador(max):
    n=0
    while n < max:
            yield n
            n=n+1

miCuenta = contador(5)
print(miCuenta)
for i in miCuenta:
    print(i)
```

El resultado es el mismo que si, en lugar de mycont = contador(5) hubiéramos instanciado una lista: mycont = [0,1,2,3,4] o mycont = range(0,5). Pero de hecho lo que ocurre es muy diferente.

Cuando el intérprete Python encuentra una función que incluye un yield (o varios), entiende que al llamar esta función no obtendremos un valor devuelto con un return, sino que obtendremos un generador (generator).

Un generador se comporta parecido a una lista, en el sentido que puede ser recorrida con un iterador - la diferencia es que los valores no están almacenados en una colección, sino que se generan "on the fly".

## Decoradores 🕯

Los decoradores son en sí mismos funciones, que toman como argumento una función y retornan otra función.


```python
def decorador(pasadaSuma):
    def function(a, b):
        print("Función sumar() llamada!")
        return pasadaSuma(a, b)
    return function

@decorador
def sumar(a, b):
    return a + b

print(sumar(7, 5))
```

    Función sumar() llamada!
    12


## Lambdas

Se trata de crear funciones de manera rápida, just in time, sobre la marcha, para prototipos ligeros que requieren únicamente de una pequeña operación o comprobación.

```python
lambda argumentos: resultado
```


```python
def f(x, y, z):
    return (x+y) * z

print(f(5,6,4))
```


```python
f = lambda x, y, z: (x+y) * z

print(f(5,6,7))
```


```python
def funcionNormal(n):
    return lambda a : a * n

resultado = funcionNormal(3)

print(resultado(11))
```

### Ejercicio si no tienen nada qué hacer en casa, el primero que lo envíe ya tiene su constacia:

Si enlistamos los números primos: 2, 3, 5, 7, 11, y 13, vemos que el 13 es el 6to primo.

¿Cuál es el primo de la posición 10 001?

# Programación Orientada a Objectos con Python 🐆

La Programación Orientada a Objetos (POO u OOP según sus siglas en inglés) es un paradigma de programación que usa objetos y sus interacciones para diseñar aplicaciones y programas de computadora. Está basado en varias técnicas, incluyendo herencia, modularidad, polimorfismo, y encapsulamiento. Su uso se popularizó a principios de la década de 1990. Actualmente son muchos los lenguajes de programación que soportan la orientación a objetos.

La programación Orientada a objetos (POO) es una forma especial de programar, más cercana a como se expresan las cosas en la vida real que otros tipos de programación.

## Para su ditcionario 🚢

#### Clase
Definiciones de las propiedades y comportamiento de un tipo de objeto concreto. La instanciación es la lectura de estas definiciones y la creación de un objeto a partir de ellas.

#### Objeto
Instancia de una clase. Entidad provista de un conjunto de propiedades o atributos (datos) y de comportamiento o funcionalidad (métodos), los mismos que consecuentemente reaccionan a eventos. Se corresponden con los objetos reales del mundo que nos rodea, o con objetos internos del sistema (del programa). Es una instancia a una clase.

#### Método
Algoritmo asociado a un objeto (o a una clase de objetos), cuya ejecución se desencadena tras la recepción de un “mensaje”. Desde el punto de vista del comportamiento, es lo que el objeto puede hacer. Un método puede producir un cambio en las propiedades del objeto, o la generación de un “evento” con un nuevo mensaje para otro objeto del sistema.

#### Comportamiento
Está definido por los métodos o mensajes a los que sabe responder dicho objeto, es decir, qué operaciones se pueden realizar con él.

#### Atributos
Características que tiene la clase

#### Componentes de un objeto
Atributos, identidad, relaciones y métodos.

#### Identificación de un objeto
Un objeto se representa por medio de una tabla o entidad que esté compuesta por sus atributos y funciones correspondientes.


```python
ruedas = 9
# Esta clas ecrea una persona 
class Coche:
    
    def __init__(self, rueditas,puertitas):
        self.ruedas = rueditas
        self.puertas = puertitas
    def desplazarse(self):
        print("El coche se esta desplazando sobre ruedas")



print("Mi coche tiene volante: ", Coche.desplazarse())

#print("Mi coche es color ", miCoche.color)
#print("Mi coche tiene las tenencias del: ", miCoche.tenenciasPagadas[0],miCoche.tenenciasPagadas[1])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-33-6c02b9b97ef6> in <module>()
         11 
         12 
    ---> 13 print("Mi coche tiene volante: ", Coche.desplazarse())
         14 
         15 #print("Mi coche es color ", miCoche.color)


    TypeError: desplazarse() missing 1 required positional argument: 'self'



```python
class Persona:
    cedula = "V-13458796"
    nombre = "Leonardo"
    apellido = "Caballero"
    sexo = "M"
    
    def saludar(self):
        print("Hola soy ",self.nombre,", mi cédula es: ",self.cedula," y mi sexo es: ",self.sexo)

PersonaCreada = Persona()

PersonaCreada.saludar()
print(PersonaCreada.sexo)
```

    Hola soy  Leonardo , mi cédula es:  V-13458796  y mi sexo es:  M
    M


## Atributos y métodos 🐘

### Atributos: características con las que cuenta un objeto -> Adjetivos calificativos
### Métodos: cosas que puede hacer el objecto -> verbos

### Atributos de instancia
Atributos de Instancia

Los atributos de instancia son aplicables a un solo objeto. Determinan el estado en el que se encuentra un objeto.

**Ejemplo:**
El atributo altura en la clase Persona es de instancia, debido a que cada persona tendrá su propia altura.

### Atributos de clase

  Un atributo de clase es un atributo común a todos los objetos instanciados de la clase. Al estar definido en la clase no hace falta instanciar la clase para utilizarlo. Las constantes se suelen definir como atributos de clase.

**Ejemplo:**
El atributo cantidadDeOjos en la clase Persona es de clase, debido a que todas las instancias de la clase persona tendrán igual cantidad de ojos.


```python
class Empleado:
    cedula = "V-13458796"
    nombre = ""
    def inicializar(self,nombreInsertado):
        self.nombre = nombreInsertado

juanito = Empleado()
juanito.inicializar("Juan")
print(juanito.cedula)
print(juanito.nombre)
```

    V-13458796
    Juan


### Métodos de clase -> Puede o no existir el objeto 🐳
Un método de clase puede modificar el estado de una clase, accediendo a los atributos de dicha clase, aún cuando el método es invocado desde una clase. En lugar de definirse utilizando self como primer parámetro, se utiliza cls.

### Métodos de instancia -> Tiene a fuerzas que existir el objeto 🌱
Son los que hemos visto def(self):

### Métodos estáticos -> Puede o no existir el objeto pero no puede acceder a los atributos del mismo 🐙
Los métodos estáticos están restringidos en su ámbito, de tal manera que no tienen acceso a los atributos del objeto. Se definen de forma idéntica a una función, sin necesidad de ingresar el parámetro inicial self.



```python
class PoblacionCensada:
    poblacion = 0
    nombre = ""
    poblacion = 0
    @classmethod
    def opera_poblacion(cls, operador, cantidad):
        cls.poblacion = eval(str(cls.poblacion) + operador + str(cantidad))
    
    @classmethod
    def despliega_total(cls):
        return cls.poblacion
    
    def __init__(self, nombre, numero=0):
        print("Se ha creado la población",nombre," con ",numero," habitantes")
        self.nombre = nombre
        self.poblacion = numero
        self.opera_poblacion('+', self.poblacion)   
    
    
    def imprimirHola(self):
        print("Hola mi nombre es: ",self.nombre," y mi número de habitantes es: ",self.poblacion)
```


```python
print(PoblacionCensada.despliega_total())
```

    0



```python
print(PoblacionCensada.imprimirHola())
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-38-e8b56c7390ef> in <module>()
    ----> 1 print(PoblacionCensada.imprimirHola())
    

    TypeError: imprimirHola() missing 1 required positional argument: 'self'



```python
Chalco = PoblacionCensada("Valle de Chalco",1000000)
Chalco.imprimirHola()
```

    Se ha creado la población Valle de Chalco  con  1000000  habitantes
    Hola mi nombre es:  Valle de Chalco  y mi número de habitantes es:  1000000



```python


class Servidor:
    usuarios_activos = set(())
    
    def __init__(self, dominio, lista):
        self.lista_usuarios = lista
        self.dominio = dominio
    
    def conexion(self, usuario):
        if usuario in self.lista_usuarios:
            self.usuarios_activos.add(usuario)
        else:
            return False
        
    @staticmethod
    def ping(ip):
        return ip
    
    @staticmethod
    def ImprimirHola():
        print("Hola")
```


```python
Servidor.ping("192.168.17.8")
```




    '192.168.17.8'



### Método init 🐶

El método __init__ es el primer método que se ejecuta cuando se crea un objeto.
El método __init__ se llama automáticamente. Es decir es imposible de olvidarse de llamarlo ya que se llamará automáticamente.


```python
class Empleado:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado:")
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")
```


```python
ivan = Empleado()
```

    Ingrese el nombre del empleado:Iván
    Ingrese el sueldo:1000000



```python
ivan.imprimir()
```

    Nombre: Iván
    Sueldo: 1000000.0



```python
Jorge.paga_impuestos()
```

    Debe pagar impuestos



```python
# otro ejemplo

class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def imprimir(self):
        print("Coordenada del punto")
        print("(",self.x,",",self.y,")")

    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrange")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")

punto1=Punto(3,4)
punto2 = Punto(-5,6)
punto3 = Punto(7,-9)
punto4 = Punto(-6,-6)
##Puede iniciarlizarse en el objeto

punto1.imprimir_cuadrante()
punto2.imprimir_cuadrante()
punto3.imprimir_cuadrante()
punto4.imprimir_cuadrante()
```

    Primer cuadrange
    Segundo cuadrante
    Cuarto cuadrante
    Tercer cuadrante


## Pilares de la programación orientada a objetos 🦁

### Abstracción
permite identificar las características y comportamientos de un objeto y con los cuales se construirá la clase (plantilla).  Esto quiere decir que a través de este pilar o fundamento es posible reconocer los atributos y métodos de un objeto.

### Encapsulamiento
Es la característica de la POO que permite el ocultamiento de la complejidad del código, pertenece a la parte privada de la clase y que no puede ser vista desde ningún otro programa.

### Herencia
Es el pilar más fuerte que asegura la reutilización de código, ya que a partir de esta característica es posible reutilizar (heredar) las características y comportamientos de una clase superior llamada clase padre, a sus clases hijas, denominadas clases derivadas. Esto implica que una vez desarrollado el código de una clase base, su código puede ser reutilizado por las clases derivadas.

### Polimorfismo
A través de esta característica es posible definir varios métodos o comportamientos de un objeto bajo un mismo nombre, de forma tal que es posible modificar los parámetros del método, o reescribir su funcionamiento, o incrementar más funcionalidades a un método.


```python
## Abstracción : Ejercicio -> Abstraigan a un animal y luego a un perro
```


```python
### Encapsulamiento:

class Ejemplo():
    __luces = 100
    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        return 418046193
    def regresarCuenta(self):
        return "6363434582"+str(self.__privado())+"6277841"
```


```python
miEjemplito = Ejemplo()
print(miEjemplito.publico())
```

    Soy un método público, a la vista de todo



```python
miEjemplito.privado()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-76-65715abe343b> in <module>()
    ----> 1 miEjemplito.privado()
    

    AttributeError: 'Ejemplo' object has no attribute 'privado'



```python
print(miEjemplito.regresarCuenta())
```

    63634345824180461936277841



```python
class CajaDeSeguridad:
    __contraclave = "123qwe"
    
    def seguro(self, clave):
        if self.__contraclave == clave:
            print("Acceso concedido.")
        else:
            print("Acceso denegado.")
```


```python
unaCaja = CajaDeSeguridad()
unaCaja.seguro("123456")
```

    Acceso denegado.



```python
unaCaja.seguro("123qwe")
```

    Acceso concedido.



```python
print(unaCaja.__contraclave)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-68-6ab4700a3208> in <module>()
    ----> 1 print(unaCaja.__contraclave)
    

    AttributeError: 'CajaDeSeguridad' object has no attribute '__contraclave'



```python
class SerVivo():
    def __init__(self, tipo, reino):
        self.tipo = tipo
        self.reino = reino
```


```python
## Herencia
class Persona:
    def __init__(self, cedula, nombre, apellido, sexo):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def hablar(self, mensaje):
        return mensaje

    def getGenero(self, sexo):
        genero = ('Masculino','Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Desconocido"
```


```python
class Supervisor(Persona):

    def __init__(self, cedula, nombre, apellido, sexo, rol):
        Persona.__init__(self, cedula, nombre, apellido, sexo)
        self.rol = rol
        self.tareas = ['10','11','12','13']

    def consulta_tareas(self):
        return self.tareas
```


```python
Fulano = Supervisor(123,"Erick","Aguilar","M","supervisor de caja 1")
print(Fulano.consulta_tareas())
```

    ['10', '11', '12', '13']



```python
class Chalan(Persona,SerVivo):
    def __init__(self, cedula, nombre, apellido, sexo, rol,tipo,reino):
        Persona.__init__(self, cedula, nombre, apellido, sexo)
        SerVivo.__init__(self,tipo,reino)
        self.rol = rol
        self.tareas = ['Cargar bultos','Tirar losa',"Alinear"]
        
    def consulta_tareas(self):
        return self.tareas
```


```python
ElCarlangas = Chalan(1234,"Carlos","De Dios","M","Chalanazo","Humano","Animal")
```


```python
ElCarlangas.tipo
```




    'Humano'




```python
ElCarlangas.consulta_tareas()
```




    ['Cargar bultos', 'Tirar losa', 'Alinear']




```python
ElCarlangas.getGenero('M') ## Cómo arreglarían este error??
```




    'Masculino'



## Polimorfismo

Múltiples formas. Un león es a la vez un animal.


```python
class Persona():
    def __init__(self):
        self.cedula = 13765890
    def mensaje(self):
        print("mensaje desde la clase Persona")

class Obrero(Persona):
    def __init__(self):
        self.__especialista = 1
    def mensaje(self):
        print("mensaje desde la clase Obrero")

class Ingeniero(Persona):
    def __init__(self):
        self.__especialista = 2
    def mensaje(self):
        print("Mensaje desde la clase Ingeniero")

class Arquitecto(Persona):
    def __init__(self):
        self.__especialista = 3
    def mensaje(self):
        print("Mensaje desde la clase Arquitecto💅")

obrero_planta = Obrero()
ingeniero_fresa = Ingeniero()
arquitecto_pirruris = Arquitecto()

obrero_planta.mensaje()
ingeniero_fresa.mensaje()
arquitecto_pirruris.mensaje()

print("\n")

super(Arquitecto, arquitecto_pirruris).mensaje()
super(Ingeniero, ingeniero_fresa).mensaje()
super(Obrero, obrero_planta).mensaje()


```

    mensaje desde la clase Obrero
    Mensaje desde la clase Ingeniero
    Mensaje desde la clase Arquitecto💅
    
    
    mensaje desde la clase Persona
    mensaje desde la clase Persona
    mensaje desde la clase Persona



```python
class Perros(object): #Declaramos la clase principal Perros
    def ladrar (self):
        print ("""GUAAAUU GUAAAUU!""")
    def grunir (self):
        print ("""GRRRRRR GRRRRR""")

class Caniche (Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""guau guau guau""")
        
    def grunir(self):
        print ("""gññññiii gñññiiii""")

class Pastor_Aleman(Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""GuaUUU GUAAAUUU GuaUUU""")
        
    def grunir(self):
        print ("Agrfgregreff aggrrfsgrrr")
 
    
class Shepadoodle (Caniche,Pastor_Aleman):#La clase hereda de las clases hijas de su padre Perros
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Shepadoodle, self).ladrar()

Tommy = Pastor_Aleman()
Piny = Caniche()
Cuchele = Shepadoodle()
Cuchele.ladrarx(5)
```

    guau guau guau
    guau guau guau
    guau guau guau
    guau guau guau
    guau guau guau


# Bibliotecas externas, necesario: pip

El gestor de paquetes pip nos permitirá tener biblitecas de Python y podremos instalarlas con pip install <algo\>

- Para la instalación en: Windows

Descarga el código de Pip en: https://bootstrap.pypa.io/get-pip.py
luego córrelo con python3 get-pip.py

- Para la instalación en: Mac

easy_install pip
o si ya lo instalaste por homebrew no hay problema. Viene incluido en brew install python3

- Para la instalación en: GNU/Linux Ubuntu


sudo apt install python3-pip

## Llamar a bibliotecas externas : Numpy 🚂

NumPy es una extensión de Python, que le agrega mayor soporte para vectores y matrices, constituyendo una biblioteca de funciones matemáticas de alto nivel para operar con esos vectores o matrices


```python
import numpy.matlib 
import numpy as np 

##Producto punto entre 2 matrices
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
print(np.dot(a,b))
```

    [[37 40]
     [85 92]]



```python
#Añadir una columna

import numpy
 
a = numpy.array([[1, 2, 3], [4, 5, 6]])
 
b = numpy.array([[400], [800]])
 
nuevaMatriz = numpy.append(a, b, axis = 1)
 
print(nuevaMatriz)
```

    [[  1   2   3 400]
     [  4   5   6 800]]



```python
# Nueva fila

import numpy
 
a = numpy.array([[1, 2, 3], [4, 5, 6]])
 
nuevaMatriz = numpy.append(a, [[50, 60, 70]], axis = 0)
 
print(nuevaMatriz)
```

    [[ 1  2  3]
     [ 4  5  6]
     [50 60 70]]



```python
#Producto cruz
x = np.array([[1,2,3], [4,5,6]])
y = np.array([[4,5,6], [1,2,3]])
np.cross(x, y)
```




    array([[-3,  6, -3],
           [ 3, -6,  3]])



## Llamar a bibliotecas externas : Matplolib 🎹

Matplotlib es una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays en el lenguaje de programación Python y su extensión matemática NumPy.

$$ f(x) = x^2$$


```python
import matplotlib.pyplot as plt
plt.plot((4,8,13,17,20),(54, 67, 98, 78, 45))
plt.show()
```


![png](img/output_225_0.png)



```python
plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45],'b--d')
```




    [<matplotlib.lines.Line2D at 0x116f78390>]




![png](img/output_226_1.png)



```python
import matplotlib.pyplot as plt
x = [2,4,6,7,9,13,19,26,29,31,36,40,48,51,57,67,69,71,78,88]
y = [54,72,43,2,8,98,109,5,35,28,48,83,94,84,73,11,464,75,200,54]
plt.scatter(x,y)
plt.show()
```


![png](img/output_227_0.png)



```python
import matplotlib.pyplot as plt
x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]
num_bins = 6
n, bins, patches = plt.hist(x, num_bins, facecolor = 'green')
plt.show()
```


![png](output_228_0.png)


## Ejemplo locochón: Principios de análisis de datos con éstas 2 herramientas + pandas 🐼


```python
#En otra hoja xd. Porque sí pesa mucho.
```

# Solución al reto de primos 🤠:



```python
limite = 100001
i = 3
cuenta = 1
primo = 2
while cuenta < limite:
    for x in range(3, int(i ** 0.5) + 1, 2):
        if i % x == 0:
            break
    else:
        primo = i
        cuenta += 1
    i += 2
print(primo)
```

    1299721


## Extra : Ligar con base de datos 🦴


```python
import sqlite3
from tkinter import *
from tkinter import messagebox as tkMessageBox

Base = sqlite3.connect("Contacts.db")

cursor = conexion.cursor()
#Crear la tabla con cada uno de los atributos
try:
	cursor.execute("""CREATE TABLE sucursales (id INTEGER PRIMARY KEY , delegacion TEXT, telefono INTEGER, gerente TEXT)""")
	cursor.execute("""INSERT INTO sucursales VALUES(1,"Coyoacán",556442312,"Juan Lopez")""")
	cursor.execute("""INSERT INTO sucursales VALUES(2,"Coyoacán",524343323,"Jorge Cardenas")""")
	cursor.execute("""INSERT INTO sucursales VALUES(3,"Coyoacán",435423423,"David Alejandro")""")
	cursor.execute("""INSERT INTO sucursales VALUES(4,"Coyoacán",643523234,"Daniel Ernesto")""")
	cursor.execute("SELECT * FROM sucursales")
	resultados = cursor.fetchall()
	print(resultados)

	cursor.execute("""UPDATE sucursales SET gerente = "Pedro Díaz" WHERE id = 3""")
	conexion.commit()

	cursor.execute("""DELETE FROM sucursal WHERE id=4""")
	resultados = cursor.fetchall()
	resultados(resultados)
except:
	cursor.execute('''DROP TABLE sucursales''')
```

Para poder acceder a los elementos dentro de la base de datos podemos utilizar un complemento de SQLite. Primero necesitamos conectarnos a la base y luego con comandos SQL podemos agregar valores, crear tablas y eliminarlas. Podemos ver un bloque Try Catch aquí.

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
         break        
      print "Recibido:", recibido  
      sc.send(recibido)  
  
print("adios")  
  
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
  
print "adios"  
  
s.close() 
```

## Ejemplo de métodos numéricos 🍦

**<span style="color:red"> ** IMPORTANTE ** </span>**

Para escribir una ecuación tienes que separar todo y multiplicar con \*:  
f=2x+3 ❌     
f = 2*x + 3 ✅

Para poner una potencia por ejemplo $2^3$ es poniendo doble asterísco. Ejemplo:
$$f(x) = x^2 + 2x +1$$
*Equivale a:*

#### Si quieres ejecutar debes hacerlo desde el principio del documento o desde donde empiezas a definir o no te saldrá el resultado. Para ejecutar debes presionar ALT + Enter en tu teclado sobre la celda que vas a interpretar


```python
import sympy as sy
from sympy.functions import sin,cos
import math
import matplotlib.pyplot as plt
x = sy.symbols('x')
def taylor(funcion,c,n):
    i = 0
    p = 0
    while i <= n:
        p = p + (funcion.diff(x,i).subs(x,c))/(math.factorial(i))*(x-c)**i
        i += 1
    return p
```


```python
#CAMBIA LA FUNCION, en dónde está alineado taylor (este caso c=0) y cuál es el mayor exponenete que quieres (este es 4)
p = taylor(cos(x),0,4)
print("El polinomios de Taylor es: ",p)
```


```python
#Coloca aquí la evaluación del mismo
x=math.pi/3
## COLOCA AQUÍ EL RESULTADO DEL ANTERIOR POR AHORA D:
VALOROBTENIDO = x**4/24 - x**2/2 + 1
print("El valor de taylor es: ",VALOROBTENIDO)
```

## Método de bisección 📊


```python
# Inserta la ecuación a buscar raíz
fx = lambda x: x**2 + 9*x + 4
```


```python
# Inserta tu rango y tolerancia
a = -5
b = 2
tolera = 0.01
```


```python
# PROCEDIMIENTO
tabla = []
tramo = b-a
fa = fx(a)
fb = fx(b)
i = 1
while (tramo>tolera):
    c = (a+b)/2
    fc = fx(c)
    tabla.append([i,a,c,b,fa,fc,fb,tramo])
    i = i+1
                 
    cambia = np.sign(fa)*np.sign(fc)
    if (cambia<0):
        b = c
        fb = fc
    else:
        a=c
        fa = fc
    tramo = b-a
c = (a+b)/2
fc = fx(c)
tabla.append([i,a,c,b,fa,fc,fb,tramo])
tabla = np.array(tabla)
raiz = c
np.set_printoptions(precision = 4)
print('i   a     c    b     f(a)   f(c)  f(b)  toler')
n=len(tabla)
for i in range(0,n,1):
    unafila = tabla[i]
    formato = '{:.0f}'+' '+(len(unafila)-1)*'{:.3f} '
    unafila = formato.format(*unafila)
    print(unafila)
print('raiz: ',raiz)
```


```python
import scipy.optimize as opt
#Inserta tu función
f1 = lambda x: x**3 + 4*x**2 - 10
# Solo cambia el rango 1,2 y la tolerancia, no cambies el xtol o tronará
print(opt.bisect(f1,1,2,xtol=0.001))
```

### Método de Newton Raphson ⭐️


```python
x=sy.symbols('x')
#funcion
funcion=sin(x) + cos(x)

derivada=sy.diff(funcion,x)

x_0=0
xr=x_0

ea=100/100

es=0.001/100
contador=-1
print("i\t   xi\t     Error Absoluto Porcentual")
while ea>es:
    xra=xr
    contador+=1
    newton_rhapson=x-(funcion/derivada)

    xr=newton_rhapson.evalf(subs={x: xr})
    
    #error aproximado relativo porcentual
    ea=sy.Abs(((xr-xra)/xr)*100)
    #resultado
    print(contador   ,xra, ea)
```

## Método de la regla falsa.

El método de regla falsa o interpolación se basa en tener 2 limitantes o rango que sepamos que contienen a la raíz de la función. Su ecuación es:


$$r\in[a,b]$$


$$ x_i = \frac{f(a_i)bi - f(b_i)a_i}{f(a_i)-f(b_i)} $$


```python
## Inserte la ecuación aquí
x=sy.symbols('x')
Px = lambda x: x**2 - 2*x - 10

## Fija los rangos de a y b donde buscarán
a = 2
b = 6
tolerancia = 0.1
l = (Px(a)*b - Px(b)*a)/(Px(a)-Px(b))
print(l)
```


```python
def metodoFalso(f,a,b):
    anterior = 0
    error = 1
    while(error>tolerancia):
        l = (Px(a)*b - Px(b)*a)/(Px(a)-Px(b))
        
```

# FIN
