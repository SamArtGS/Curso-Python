# El lenguaje de programación Python - Avanzado 🐳

 **<div style="text-align: right"> Samuel Arturo Garrido Sánchez</div>**

Python es un lenguaje de programación **multiparadigma**, muy útil para demasiadas ramas de la investigación, desarrollos y procesos. 
Su filosofía radica en un código legible que cualquier persona no enfocada en el área de programación, pueda comprender.

![](img/let.png)

# MarkDown ⚽️

# Cabeceras

# H1
## H2
### H3

Negrita:	**Texto negritas**
Cursiva:	*Texto en cursiva*
Tachado:    ~~El mundo es plano.~~



Comentario:	

> En este ejemplo pudimos notar algo excepcional

## Listas:

1. Primer elemento
2. Segundo elemento
3. Tercer elemento


## Listas desordenadas:

- Primer elemento
- Segundo elemento
- Tercer elemento

## Listas para tachar

- [x] Dar la clase
- [x] Poner su moodle
- [ ] Calificar sus tareas

## Código

#### Terminal
`pip install proteco`

#### Python
```python
import numpy as np
print("Hola mundo")
```

#### Swift
```swift
import Foundation

let hola = "Hola a todos"
print(hola)

```


#### Java

```java
public class HolaMundo {
	public static void main(String[] args) {		
		System.out.println("Hola Mundo");
	}
}
```

Barra horizontal

---


## Link	

[Titulo Del Link](https://developer.apple.com)


## Imagen	

![Descripcion](img/1.jpg)


## LaTEX (válido solo en Jupyter Notebook,Colab o Azure)

$$\int_{x^2}^{x^5} y^t_i s^t dt$$

## Tablas 

| Criterio      | Puntos | Obtenidos | Observaciones     |
|---------------|--------|-----------|-------------------|
| Examen        | 1      | 4         | Nada que comentar |
| Tareas        | 2      | 4         | Nada que comentar |
| Participacion | 3      | 4         | Nada que comentar |

## Tablas con formato

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

## Algo de Web

Tambien podemos poner cosas exclusivas de web por ejemplo imágenes que tengan una forma. 

**Ejemplo:**

<dl>
  <dt>Lista de definición</dt>
  <dd>Promulgamos algo mejor</dd>

  <dt>Markdown en HTML</dt>
  <dd>No *funciona* **muy** bien. Use mejor tags <em>HTML</em>.</dd>
</dl>

## VIDEOS

<a href="http://www.youtube.com/watch?feature=player_embedded&v=HzZxcfVn_08
" target="_blank"><img src="http://img.youtube.com/vi/HzZxcfVn_08/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="400" height="200" border="10" /></a>

<a href="http://www.youtube.com/watch?feature=player_embedded&v=afvT1c1ii0c
" target="_blank"><img src="http://img.youtube.com/vi/afvT1c1ii0c/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="400" height="200" border="10" /></a>

# Derivada

Voy a hacer la siguiente derivada 

$$\frac{d(x^2+2x)}{dx}$$

Y lo hago así con Python


```python

```

Y eso es todo! 😀

# Gestor de paquetes PIP 🍀

Nadie quiere inventar la rueda 2 veces y construir artefactos con mejores instrumentos nos ayuda a tener mejores resultados. El éxito de Python mayormente se basa en su comunidad, donde varios códigos funcionales de Python se liberan al mundo para que otras personas puedan desarrollar sus soluciones a partir de estas herramientas. 

#### Estos programas funcionales que nos pueden ayudar a crear gráficas o hacer análisis de datos más rápidamente se llaman paquetes.

Un administrador de paquetes o un sistema de administración de paquetes es una colección de herramientas de software que automatiza el proceso de instalación, actualización, configuración y eliminación de programas de computadora para el sistema operativo de una computadora de manera consistente.

El gestor de paquetes pip nos permitirá tener biblitecas de Python y podremos instalarlas con pip install <algo\>. 

- Para la instalación en: Windows

Descarga el código de Pip en: https://bootstrap.pypa.io/get-pip.py
luego córrelo con python3 get-pip.py

- Para la instalación en: Mac

easy_install pip
o si ya lo instalaste por homebrew no hay problema. Viene incluido en brew install python3

- Para la instalación en: GNU/Linux Ubuntu


sudo apt install python3-pip

**LA MAYORÍA DEL TIEMPO YA VIENE INSTALADO, PARA VERIFICAR ESTO ESCRIBA EN SU TERMINAL: pip**

## 💯 Numpy: De vuelta a Matemáticas

NumPy es una biblioteca para el lenguaje de programación Python, que agrega soporte para matrices y matrices grandes y multidimensionales, junto con una gran colección de funciones matemáticas de alto nivel para operar en estas matrices.





```python
#NP es un alias, para no escribir completamente numpy
import numpy as np
arreglo = np.array([1, 2, 3, 4, 5])
print(arreglo)
print("Tipo: ",type(arreglo))
print("Elementos del array:",arreglo.dtype)
```

    [1 2 3 4 5]
    Tipo:  <class 'numpy.ndarray'>
    Elementos del array: int64



```python
lista = [1,2,3]

vector = np.array(lista)

print("El vector:",vector)
print("Dimensiones del vector: ",vector.shape)
print("Cada elemento del vector +1:",vector+1)
print("Cada elemento del vector multiplicado por 5:",vector*5)
print("Suma de todos sus elementos: ",np.sum(vector))
print("Media de todos sus elementos:",np.mean(vector))

print("Suma del mismo vector:",vector+vector)

vector2 = np.array([8,9,10])

print("Suma de 2 vectores: ",vector + vector2)

print("Producto Punto de vectores:",vector.dot(vector2))
print("Producto Cruz de vectores",np.cross(vector,vector2))
```

    El vector: [1 2 3]
    Dimensiones del vector:  (3,)
    Cada elemento del vector +1: [2 3 4]
    Cada elemento del vector multiplicado por 5: [ 5 10 15]
    Suma de todos sus elementos:  6
    Media de todos sus elementos: 2.0
    Suma del mismo vector: [2 4 6]
    Suma de 2 vectores:  [ 9 11 13]
    Producto Punto de vectores: 56
    Producto Cruz de vectores [-7 14 -7]


### Matrices

Las matrices en numpy las usaremos de la siguiente forma, tomando en cuenta que cada lista que insertemos dentro de numpy singifica una nueva fila o de números dentro de la matriz.



```python
##Producto punto entre 2 matrices
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]])

print("Matriz 1:")
print(a)

print("Matriz 2:")
print(b)

print("Producto Punto entre ambas matrices:")
print(np.dot(a,b))
```

    Matriz 1:
    [[1 2]
     [3 4]]
    Matriz 2:
    [[11 12]
     [13 14]]
    Producto Punto entre ambas matrices:
    [[37 40]
     [85 92]]



```python
matriz1 = np.array([[1,2,3], [4,5,6]])
matriz2 = np.array([[4,5,6], [1,2,3]])
print("Producto cruz entre matrices:")
print(np.cross(matriz1,matriz2))
```

    Producto cruz entre matrices:
    [[-3  6 -3]
     [ 3 -6  3]]


Agregar una fila completa a una matriz solo es cuestión de utilizar el método append. **Si queremos añadir una coluna deberemos especificar una correcta forma y dimensión del arreglo**


```python
# Añadir fila
primeraMatriz = np.array([[1, 2, 3], [4, 5, 6]])

print("Primera Matriz: ")
print(primeraMatriz)

nuevaMatriz = np.append(primeraMatriz, [[50, 60, 70]], axis = 0)
print("\nSegunda Matriz, añadiendo una fila: ")
print(nuevaMatriz)
```

    Primera Matriz: 
    [[1 2 3]
     [4 5 6]]
    
    Segunda Matriz, añadiendo una fila: 
    [[ 1  2  3]
     [ 4  5  6]
     [50 60 70]]



```python
#Añadir una columna

import numpy
 
primerMatrix = numpy.array([[1, 2, 3], [4, 5, 6]])

#Podemos agregar un array de numpy o una lista al método append
segundaMatrix = numpy.array([[400], [800]])

print("Primera Matriz: ")
print(primerMatrix)
print("\nSegunda Matriz: ")
print(segundaMatrix)

nuevaMatriz = numpy.append(primerMatrix, segundaMatrix, axis = 1)

print("\nResultado de matrices, añadiendo una columna:")

print(nuevaMatriz)
```

    Primera Matriz: 
    [[1 2 3]
     [4 5 6]]
    
    Segunda Matriz: 
    [[400]
     [800]]
    
    Resultado de matrices, añadiendo una columna:
    [[  1   2   3 400]
     [  4   5   6 800]]


#### Dimensiones,tamaños y formas de los arrreglos
Una cosa es la forma de los arreglos o matrices, o sea cuántos elementos tiene de ancho y alto y otra muy distinta es si es un número escalar, un vector, una matriz o algo más. La dimensión es como decir estoy en el plano 2D pero tengo un rectángulo que mide 5x10, el atributo .shape me da las medidas mientas .ndim me dirá que es 2 ya que estamos en dimensión 2D y el tamaño es la cantidad de elementos que tenemos en el arreglo, si es de forma 5x10, tendrá 50 elementos.


```python
cero = np.array(1) 
uno = np.array([1, 2, 3, 4, 5])
dos = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tres = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

#con el atributo ndim conoceremos su dimensión
print("Arreglo 1 => Dimensión: ",cero.ndim,"  Forma:",cero.shape, "         Tamaño: ",cero.size)
print("Arreglo 2 => Dimensión: ",uno.ndim,"  Forma:",uno.shape,"       Tamaño: ",uno.size)
print("Arreglo 3 => Dimensión: ",dos.ndim,"  Forma:",dos.shape,"     Tamaño: ",dos.size)
print("Arreglo 4 => Dimensión: ",tres.ndim,"  Forma:",tres.shape,"  Tamaño: ",tres.size)

#Si queremos crear un arreglo de n dimensiones tendremos que colocar como parámetro a ndim
cinco = np.array([1,2,3,4], ndmin = 5)
print("\nArreglo de dimensión 5:",cinco)
```

    Arreglo 1 => Dimensión:  0   Forma: ()          Tamaño:  1
    Arreglo 2 => Dimensión:  1   Forma: (5,)        Tamaño:  5
    Arreglo 3 => Dimensión:  2   Forma: (3, 3)      Tamaño:  9
    Arreglo 4 => Dimensión:  3   Forma: (2, 2, 3)   Tamaño:  12
    
    Arreglo de dimensión 5: [[[[[1 2 3 4]]]]]


**Podemos además, reformar o cambiar la estructura de este arreglo, por ejemplo pasar de una matriz de 1x12 a una matriz de 4x3**


```python
arreglo = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

nuevo_arr = arreglo.reshape(4,3) # Método reshape me cambia la forma
print("Arreglo original:")
print(arreglo)
print("\nArreglo cambiado de forma:")
print(nuevo_arr)
```

    Arreglo original:
    [ 1  2  3  4  5  6  7  8  9 10 11 12]
    
    Arreglo cambiado de forma:
    [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]]



```python
# Recorrer arreglo con  np.ndinter nos permite recorrer el arreglo sin importar su dimensión:

for elemento in np.nditer(arreglo):
    print(elemento)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12


#### Acceso a los elementos dentro de los vectores Numpy
Para acceder a un elemento específico, podemos hacerlo igual como hacíamos con listas o tuplas en Python, indicamos la posición pero ahora como tenemos muchas dimensiones, tendremos qué especificar qué elementos querremos.


```python
#Acceso a elementos individuales
print("Elemento en el arreglo uno, pos 0: ",uno[0])
print("Elemento en la pos 1,0 de dos: ",dos[1,0])
print("Elemento en la pos 0,1,1 de tres:",tres[0,1,1])
```

    Elemento en el arreglo uno, pos 0:  1
    Elemento en la pos 1,0 de dos:  4
    Elemento en la pos 0,1,1 de tres: 5



```python
#Acceso a rango de elementos

arregloAcceso = np.array([1, 2, 3, 4, 5])
print("Arreglo:",arregloAcceso)
print("Del arreglo uno, de la pos 1 a la 3:",arregloAcceso[1:3])
print("Desde la pos. 1 hasta terminar:",arregloAcceso[1:])
print("Desde el principio hasta la pos 4:",arregloAcceso[:4])
print("De la posición -3 a la pos -1 (empezar a contar desde el final):",arregloAcceso[-3:-1])
print("De la pos 1, hasta la 4 saltando de 2 en 2:",arregloAcceso[1:4:2])
```

    Arreglo: [1 2 3 4 5]
    Del arreglo uno, de la pos 1 a la 3: [2 3]
    Desde la pos. 1 hasta terminar: [2 3 4 5]
    Desde el principio hasta la pos 4: [1 2 3 4]
    De la posición -3 a la pos -1 (empezar a contar desde el final): [3 4]
    De la pos 1, hasta la 4 saltando de 2 en 2: [2 4]


### Arreglos de otras cosas
Podemos tener arreglos de decimales, de strings pero no se utilizan tanto como los números en numpy.

Además podemos indicar si nuestro arreglo lo queremos pasar a un tipo de dato como un número complejo o a flotante.


```python
matrizCadena = np.array(['Hola','Adios','Permiso'])
print("Tipo de Cadena:",matrizCadena.dtype)

matrizFlotante = np.array([10.411, 20.533, 30.851])
print("Tipo de cadena:",matrizFlotante.dtype)

matrizConversion = np.array([1, 2, 3, 4], dtype='f')
print("Arreglo de float:",matrizConversion.dtype)

cerosComplejos = np.zeros((2,2),dtype=np.complex_)
print("\n")
print(cerosComplejos)
print("\n")
print("Tipo dato de arreglo de complejos:",cerosComplejos.dtype)

#Con el método AsType podremos pedirle que nos pase 
## toda la matriz en un tipo de dato Específico
matrizEnteros = matrizFlotante.astype(int)

print("Castear todos los elementos, usar astype:",matrizEnteros)
```

    Tipo de Cadena: <U7
    Tipo de cadena: float64
    Arreglo de float: float32
    
    
    [[0.+0.j 0.+0.j]
     [0.+0.j 0.+0.j]]
    
    
    Tipo dato de arreglo de complejos: complex128
    Castear todos los elementos, usar astype: [10 20 30]


### Arreglos aleatorios y funciones útiles
Podemos utilizar la función random de numpy para optener números aleatorios a través de numpy


```python
from numpy import random

enteroAleatorio = random.randint(100) #del 0 a 100
print("Número entero aleatorio entre 0 y 100:",enteroAleatorio)

#Para una matriz aleatoria especificamos la forma en que la queremos 
# Y saldrán solo número entre 0 y 1

matrizAleatoriaFlotantes = random.rand(2,3) 
print("\nMatriz Flotantes:\n",matrizAleatoriaFlotantes)

#Para una matriz aleatoria especificamos la forma en que la queremos 
# Y saldrán solo número entre 0 y 1
matrizAleatoriaEnteros = random.randint(100, size = (5,5))
print("\nMatriz Enteros:\n",matrizAleatoriaEnteros)
```

    Número entero aleatorio entre 0 y 100: 63
    
    Matriz Flotantes:
     [[0.37067447 0.70828821 0.66149885]
     [0.38387195 0.79572182 0.70431242]]
    
    Matriz Enteros:
     [[ 1 56 58 95  6]
     [67 19 91 30  7]
     [12 71 21 56 92]
     [33 85 34 51 43]
     [65  0 57 66 73]]



```python
#Crear arreglo dado rangos
arregloPersonalizado = np.arange(2,30,3) #Inicio, fin, de cuánto en cuánto
print("Arreglo rangos 1D:",arregloPersonalizado)

#Crear matriz de ceros
matrizCeros = np.zeros((3,3), dtype=int)
print("\nMatriz Ceros:\n",matrizCeros,"\n")

#Crear matriz de unos
matrizUnos = np.ones((3,3), dtype=int)
print("\nMatriz Unos:\n",matrizUnos,"\n")


#Sacar raíz cuadrada a cada elemento
raiz = np.sqrt(np.array([1,4,9,16,25]))
print("Matriz raíz cuadrada:",raiz)


#Rellenar con vectores una matriz
relleno = np.full((2,2), [3,5])
print("\nMatriz rellenada:\n",relleno)
```

    Arreglo rangos 1D: [ 2  5  8 11 14 17 20 23 26 29]
    
    Matriz Ceros:
     [[0 0 0]
     [0 0 0]
     [0 0 0]] 
    
    
    Matriz Unos:
     [[1 1 1]
     [1 1 1]
     [1 1 1]] 
    
    Matriz raíz cuadrada: [1. 2. 3. 4. 5.]
    
    Matriz rellenada:
     [[3 5]
     [3 5]]


### Operaciones fundamentales de matrices

- T = Transpuesta
- H = Hermitiana


```python
matrix = np.array([[1,2,3],[3,4,5],[4,5,6]])
```


```python
import sympy as sp

sp.pi.evalf(100)

x = Symbol('x')
sp.integrate(x**3,x)
```




## 📊 Matplolib: Todos merecemos ver 

Matplotlib es una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays en el lenguaje de programación Python y su extensión matemática NumPy. Por ejemplo, si yo quiero graficar la siguiente función:

$$ f(x) = x^2$$


Lo haremos de la siguiente manera:


```python
import matplotlib.pyplot as plt # Importamos matplotlib pyplot y le ponemos un alias: plt
import numpy as np # Importamos numpy y ponemos un alias, np

%matplotlib inline 
##Esta línea es importante para que muestre las gráficas en Jupyter Notebook
```


```python
x = np.linspace(-10, 10, 100) ## Especificamos un rango y cuántos puntos intermedios irá calculando
#print(x)

y = x**2   ## Definimos la función
#print(y)

figura, imagen = plt.subplots() ## Este método regresa una figura para exportar a png y la imagen para proyectar
imagen.plot(x, y) ## Mostramos la imagen
plt.show() ## Es importante para que nos muestre la imagen
```


    
![](img/output_36_0.png)
    



```python
x = np.arange(0.,2.,.05)

y1= x
y2= x**2

plt.plot(x,y1, '.b', label='Lineal', markersize=1)
plt.plot(x,y2, '--g', label="Cuadrada", linewidth=2)

#Nombres: Podemos colocar el nombre de la gráfica, del eje x y del eje y
plt.title('Gráfica de ventas')
plt.xlabel('Ventas')
plt.ylabel('Ganancias')


plt.legend() # Nos muestra la simbología
plt.grid(True) ## Nos muestra la cuadrícula
plt.show() # Nos muestra la gráfica
```


    
![png](img/output_37_0.png)
    



```python
import matplotlib.pyplot as plt
import numpy as np

# Información para plotear
rango = np.arange(0.0, 2.0, 0.01)

onda = 1 + np.sin(2 * np.pi * rango)

figura, grafica = plt.subplots()
grafica.plot(rango, onda)

grafica.set(xlabel='Tiempo (s)', ylabel='Voltaje (V)',title='Ejemplo')
grafica.grid()

## figura.savefig("imagen.png")
plt.show()
```


    
![](img/output_38_0.png)
    



```python
x=np.arange(0.,10., 0.2)
seno=np.sin(x)
coseno=np.cos(x)

plt.plot(x,seno, label="Seno")
plt.plot(x,coseno, label="Coseno")
plt.title('Gráficas de Seno y Coseno')

plt.legend()
plt.grid(True)
plt.show()
```


    
![](img/output_39_0.png)
    



```python
x = [2,4,6,7,9,13,19,26,29,31,36,40,48,51,57,67,69,71,78,88]
y = [54,72,43,2,8,98,109,5,35,28,48,83,94,84,73,11,464,75,200,54]
plt.scatter(x,y)
plt.show()
```


    
![](img/output_40_0.png)
    



```python
plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45],'r--d')
plt.show()
```


    
![](img/output_41_0.png)
    



```python
import matplotlib.pyplot as plt
x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]
num_bins = 6
n, bins, patches = plt.hist(x, num_bins, facecolor = 'green')
plt.show()
```


    
![png](img/output_42_0.png)
    



```python
import matplotlib.pyplot as plt
plt.plot((4,8,13,17,20),(54, 67, 98, 78, 45))
plt.show()
```


    
![png](img/output_43_0.png)
    



```python
from scipy import misc
import matplotlib.pyplot as plt

face = misc.face()
plt.imshow(face)
plt.show()
```


    
![png](img/output_44_0.png)
    


## Ejemplo: Cantidad de Sistemas Operativos




```python
DataSetSO = {'iOS':1, 'Android':5, 'Windows':10, 'macOS':2, 'GNU/Linux':20}

SO_Nombre= list(monedas.keys())
SO_Cantidad=list(monedas.values())
```


```python
import matplotlib.pyplot as plt

plt.pie(SO_Cantidad, labels=SO_Nombre, colors=['blue','cyan','red','green','gold'], autopct='%.4f%%', startangle=90)
plt.title('Gráfica de pastel de Sistemas Operativos')

plt.show()
```


    
![png](img/output_47_0.png)
    


## Gráfica de Barras


```python
plt.bar(SO_Nombre, SO_Cantidad, color='red', linewidth='4')
plt.title('Sistemas operativos')
plt.show()
```


    
![png](img/output_49_0.png)
    


## Gráfica de burbujas


```python
N=50 ## Cantidad de puntos
x=np.random.rand(N)
y=np.random.rand(N)

colors = np.random.rand(N) ## colores aleatorios

area = (30*np.random.rand(N))**2

plt.scatter(x,y, s=area, c=colors, alpha=0.5)
plt.show()
```


    
![png](img/output_51_0.png)
    



```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt # Importamos matplotlib pyplot y le ponemos un alias: plt
%matplotlib inline 
fig = plt.figure()
ax=Axes3D(fig)

x= np.linspace(-4,4,50)
y= np.linspace(-4,4,50)
X,Y=np.meshgrid(x,y)


ax.plot_surface(X,Y,np.cos(np.sqrt(X**2+Y**2)), color='green')

#Para girar la imagen usamos view_init
#elev: es el angulo de elevación sobre el eje z
#azim: es el azimuth, rota la gráfica en los ejes x y y, es decir de manera horizontal
#Los valores por defecto utilizados son azim=-60 elev=30
ax.view_init(elev=30, azim=-60)

plt.show()
```


    
![png](img/output_52_0.png)
    



```python
%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax=Axes3D(fig)

x= np.linspace(-4,4,50)
y= np.linspace(-4,4,50)
X,Y=np.meshgrid(x,y)

ax.plot_surface(X,Y,np.cos(np.sqrt(X**2+Y**2)), color='red')
plt.show()
```


 <IPython.core.display.Javascript object>

## Ejemplo de métodos numéricos 🍦

**<span style="color:red"> ** IMPORTANTE ** </span>**

Para escribir una ecuación tienes que separar todo y multiplicar con \*:  
f=2x+3 ❌     
f = 2*x + 3 ✅

Para poner una potencia por ejemplo $2^3$ es poniendo doble asterísco. Ejemplo:

$$f(x) = x^2 + 2x +1$$

Equivale a:


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

    El polinomios de Taylor es:  x**4/24 - x**2/2 + 1



```python
#Coloca aquí la evaluación del mismo
x=math.pi/3
## COLOCA AQUÍ EL RESULTADO DEL ANTERIOR POR AHORA D:
VALOROBTENIDO = x**4/24 - x**2/2 + 1
print("El valor de taylor es: ",VALOROBTENIDO)
```

    El valor de taylor es:  0.501796201500181


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

    i   a     c    b     f(a)   f(c)  f(b)  toler
    1 -5.000 -1.500 2.000 -16.000 -7.250 26.000 7.000 
    2 -1.500 0.250 2.000 -7.250 6.312 26.000 3.500 
    3 -1.500 -0.625 0.250 -7.250 -1.234 6.312 1.750 
    4 -0.625 -0.188 0.250 -1.234 2.348 6.312 0.875 
    5 -0.625 -0.406 -0.188 -1.234 0.509 2.348 0.438 
    6 -0.625 -0.516 -0.406 -1.234 -0.375 0.509 0.219 
    7 -0.516 -0.461 -0.406 -0.375 0.064 0.509 0.109 
    8 -0.516 -0.488 -0.461 -0.375 -0.156 0.064 0.055 
    9 -0.488 -0.475 -0.461 -0.156 -0.046 0.064 0.027 
    10 -0.475 -0.468 -0.461 -0.046 0.009 0.064 0.014 
    11 -0.475 -0.471 -0.468 -0.046 -0.019 0.009 0.007 
    raiz:  -0.47119140625



```python
import scipy.optimize as opt
#Inserta tu función
f1 = lambda x: x**3 + 4*x**2 - 10
# Solo cambia el rango 1,2 y la tolerancia, no cambies el xtol o tronará
print(opt.bisect(f1,1,2,xtol=0.001))
```

    1.3642578125


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

    i	   xi	     Error Absoluto Porcentual
    0 0 100.000000000000
    1 -1.00000000000000 27.8703862327451
    2 -0.782041901539138 0.427334129760588
    3 -0.785398175999702 1.60456876032265e-6


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

    3.6666666666666665



```python
def metodoFalso(f,a,b):
    anterior = 0
    error = 1
    while(error>tolerancia):
        l = (Px(a)*b - Px(b)*a)/(Px(a)-Px(b))
        
```

## Introducción a Inteligencia Artificial 🤖

La investigación en inteligencia artificial comenzó en la década de los 50, continuando el trabajo llevado a cabo por el matemático británico Alan Turing durante la Segunda Guerra Mundial. Sin embargo, no ha sido hasta la última década cuando se han producido los avances más rápidos en cuanto a IA, como consecuencia de la combinación de tres factores cruciales: el cloud computing (computación en la nube), la gran cantidad de datos y los grandes avances en machine learning (aprendizaje automático).

## SciKitLearn: Aprendizaje Máquina con Python ⚽️


## Regresión 🍔

¿Les gustaría predecir el futuro?
Bueno antes que nada para los de ciencias e ingeniería y los área 1: ¿Qué es una pendiente y una ordenada al origen?

Bueno en el sentido de la palabra, una regresión lineal es obtener la relación entre unas variables independietes y una variable dependiente. 

- X's son nuestros inputs
- Y es nuestro target

La expresión matemática general de una regresión lineal es:


$$y = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n + \epsilon$$

$$ y = \beta_0 + \sum_{i=1}^n\beta_ix_i + \epsilon $$

## Regresión: Regresión Lineal Simple

Cuando solo tenemos la expresión con i = 1 tendremos la expresión dada en:

$$\beta_0 + \beta_1x_1 + \epsilon$$

Los que tratamos de hacer es: Obtener las betas y epsilon. Para quedar más claro imagen la expresión anterior como:

$$y = mx + b$$

Si recordarán de su curso de matemáticas en la secundaria m es la pendiente y b la ordenada al origen y podemos decir que beta 0 es equivalente a b y beta 1 es equivalente a beta 1.

Ahora.¿Cómo calculaban la pendiente?

$$ m = \frac{y_2-y_1}{x_2-x_1}$$

¿Esto se valía si tenía puntos regados? NEL, solo se vale cuando tenemos puntos alieados. Qué pasa si quiero encontrar m que tenga el mejor ajuste a todos los puntos de la recta?




```python
import pandas as pd

Data = {'X': [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2],
        'Y': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
       }
  
tablita = pd.DataFrame(Data,columns=['X','Y'])
tablita
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6.1</td>
      <td>1500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.8</td>
      <td>1520</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.7</td>
      <td>1525</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.7</td>
      <td>1523</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.8</td>
      <td>1515</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.6</td>
      <td>1540</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5.5</td>
      <td>1545</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.3</td>
      <td>1560</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5.2</td>
      <td>1555</td>
    </tr>
    <tr>
      <th>9</th>
      <td>5.2</td>
      <td>1565</td>
    </tr>
  </tbody>
</table>
</div>



¿Cómo se están comportando esos datos? Imprimimos la gráfica scatter para saberlo.


```python
import matplotlib.pyplot as plt
%matplotlib inline

plotPuntos = tablita.plot(x ='X', y='Y', kind = 'scatter')
plt.show()
```


    
![png](img/output_75_0.png)
    



```python
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pendiente, ordenadaOrigen, valor_r, valor_p, error = stats.linregress(tablita['X'].tolist(),tablita['Y'].tolist())

t = np.arange(5.2,6.2,0.1)

plt.plot(t,pendiente*t+ordenadaOrigen,'--r')
plt.scatter(tablita['X'].tolist(),tablita['Y'].tolist())
plt.show()
```


    
![png](img/output_76_0.png)
    


#### Mínimos cuadrados
Para poder determinar la recta que tenga mejor ajuste necesitaremos una técnica llamada mínimos cuadrados y esto como para qué?

Bueno lo que hace es minimizar el error cuadrático medio dado:

$$b = \frac{\sum y\sum x^2 - \sum x-\sum x y}{N\sum x^2 - (\sum x)^2}$$

$$ m = \frac{N\sum xy - \sum x\sum y}{N\sum x^2 - (\sum x)^2} $$

**Peeeero**, imagínense con un dataset enorme, gigantesco donde la memoria es primordial. ¿Volverían a ejecutar estas ecuaciones para cada nuevo dato que tengamos en el dataset?

**Pues la respuesta es NO**. Para ello existen los métodos numéricos.

Para calcular b y m no es necesario seguir esas ecuaciones, ya que son muy precisas. 

> Los que ya hayan llevado métodos numéricos me entenderán.

Cuando una computadora realiza cálculos siempre lo hace con métodos numéricos y estos tienen una tolerancia y mediante iteraciones vamos reduciendo esa tolerancia lo más posible siendo un tiempo determinado. Se aceptan errores, claro, y esto nos permite que si ya tenemos ajustado nuestro modelo solo tengamos que moverlo un poquito.




## Tamaños de predicción. 

Por lo general en el área de estadística existe algo llamado estadística inferencial donde tomamos de una muestra de la población. Considerarlo al momento de obtener muestras muy pequeñas.

Para calcular ese error o tolerancia se recurre a algo llamado el cálculo del error cuadrático medio de estadística que quiere decir, la suma de todas las diferencias de la función calculada hasta los inputs cuánto me da. Buscamos que se la mínima posible y al ser una función cuadrática esta es una parábola.


$$ECM(\theta') = E[(\theta' - \theta)^2] = Var(\theta') + sesgo(\theta') ^2$$


```python
import numpy as np
import random
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

%matplotlib inline
 
# Generador de distribución de datos para regresión lineal simple
def generador_datos_simple(beta, muestras, desviacion):
    # Genero n (muestras) valores de x aleatorios entre 0 y 100
    x = np.random.random(muestras) * 100
    # Genero un error aleatorio gaussiano con desviación típica (desviacion)
    e = np.random.randn(muestras) * desviacion
    # Obtengo el y real como x*beta + error
    y = x * beta + e
    return x.reshape((muestras,1)), y.reshape((muestras,1))
 
# Parámetros de la distribución normal
desviacion = 200
beta = 10
n = 50

x, y = generador_datos_simple(beta, n, desviacion)

plt.scatter(x, y)
plt.title("Gráfica de puntos aleatorios")
plt.show()
```


    
![png](img/output_80_0.png)
    



```python
# Creo un modelo de regresión lineal
modelo = linear_model.LinearRegression()

# Entreno el modelo con los datos (X,Y)
modelo.fit(x, y)


# Ahora puedo obtener el coeficiente b_1
print ('Coeficiente beta1: ', modelo.coef_[0])
 
# Podemos predecir usando el modelo
y_pred = modelo.predict(x)


# Por último, calculamos el error cuadrático medio y el estadístico R^2
print ("Error cuadrático medio: ", mean_squared_error(y, y_pred))

plt.scatter(x, y) ## Graficamos los puntos

plt.plot(x, y_pred, color='red') ## Graficamos la predicción de SciKitLearn

x_real = np.array([0, 100])
y_real = x_real*beta

plt.plot(x_real, y_real, color='green') ## Graficamos con Método de Mínimos Cuadrados
plt.show()
```

    Coeficiente beta1:  [8.0409]
    Error cuadrático medio:  51423.42693265156



    
![png](img/output_81_1.png)
    


**¿Conclusiones?**

## Clasificación: Regresión Logística


```python
import matplotlib.pyplot as plt

# Importar el dataset, clasificadores y métricas de rendimiento

from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

digitos = datasets.load_digits()

_, renglon = plt.subplots(2, 4) ## imprimimos un arreglo de imágenes de 2 x 4

imagenes_con_etiquetas = list(zip(digitos.images, digitos.target)) 

## Aquí vamos recorriendo cada una de nuestras imágenes con etiquetas 
for grafo, (imagen, etiqueta) in zip(renglon[0, :], imagenes_con_etiquetas[:4]):
    grafo.set_axis_off()
    grafo.imshow(imagen, cmap=plt.cm.gray_r, interpolation='nearest')
    grafo.set_title('Entrena:'+str(etiqueta))

# Para aplicar un clasificador a estos, necesitamos una imagen plana,

##Reacomodamos la imagen a una lineal
CantidadImagenes = len(digitos.images)
print("Hay ",CantidadImagenes,"imágenes")
data = digitos.images.reshape((CantidadImagenes, -1)) ## Las hacemos todas lineales

# Creamos un vector clasificador
clasificador = svm.SVC(gamma=0.001)

# Sacar el conjunto de train y de test
X_train, X_test, y_train, y_test = train_test_split(data, digitos.target, test_size=0.5, shuffle=False)

# Entrenamos con los subconjuntos de traing
clasificador.fit(X_train, y_train)

# Tomamos una imagen, la probamos y mandamos a predicción
imagen_predicha = clasificador.predict(X_test)

## Ahora tomamos las imágenes de prueba, las de TEST
test = list(zip(digitos.images[CantidadImagenes // 2:], imagen_predicha))

for grafo, (imagen, prediccion) in zip(renglon[1, :], test[:4]):
    grafo.set_axis_off()
    grafo.imshow(imagen, cmap=plt.cm.gray_r, interpolation='nearest')
    grafo.set_title("Predicción:"+str(prediccion))

plt.show()

```

    Hay  1797 imágenes



    
![png](img/output_84_1.png)
    


## No sé si poner algoritmo: Diagnóstico de Wisconsin para el cáncer de mama. 😬

El cáncer de mama (BC) es uno de los cánceres más comunes entre las mujeres en todo el mundo, y representa la mayoría de los casos nuevos de cáncer y las muertes relacionadas con el cáncer según las estadísticas mundiales, lo que lo convierte en un problema de salud pública importante en la sociedad actual.

Lo que tenemos disponible en el DataSet es:

- radio (media de las distancias desde el centro hasta los puntos del perímetro)
- textura (desviación estándar de los valores de escala de grises)
- perímetro
- zona
- suavidad (variación local en longitudes de radio)
- compacidad (perímetro² / área - 1.0)
- concavidad (gravedad de las porciones cóncavas del contorno)
- puntos cóncavos (número de porciones cóncavas del contorno)
- simetría
- dimensión fractal ("aproximación de la línea costera" - 1)

## Extra: TensorFlow - Framework para Redes Neuronales ⭐️

### Primer Algoritmo: MNIST


<p>
  <img src="https://storage.googleapis.com/kaggle-datasets-images/2243/3791/9384af51de8baa77f6320901f53bd26b/dataset-cover.png" align = "right" width="600"/>
</p>


MNIST es un dataset muy popular y algunos lo consideran el "Hola mundo" para Tensor. Básicamente consta de varias imágenes de ropa para poder clasificar a través de una Red Neuronal Artificial, ya que todas son del mismo tamaño.

Para ello usaremos una capa densa, una capa de Dropout y una segunda capa densa de Salida.

- Compilaremos y entrenaremos el modelo para poder sacar los respectivos pesos de la función.


```python
import numpy as np #Importamos numpy para los arreglos
import datetime
import tensorflow as tf # Importamos TensorFlow
from tensorflow.keras.datasets import fashion_mnist ## Importams un dataset de Keras, el MNIST

#Cargar el dataset Fashion Mnist y las variables Xtrain, Xtest, Ytrain Ytest guardan los valores de retorno
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
```

### Normalización de las imágenes

Se divide cada imagen en los conjunto de entrenamiento (train) y de pruebas (test) entre el valor máximo de cada uno de los píxeles (255), ya que 0 significa negro y 255 significa un pixel blanco.

De este modo, cada píxel se hallará en el rango [0, 1], siendo 0 negro y 1 blanco. 

- ¿Para qué hacemos esto? 

Al normalizar las imágenes, nos aseguramos que nuestro modelo de RNA entrenará más rápidamente.


```python
 X_train = X_train / 255.0
X_test = X_test / 255.0
```

### Redimensionar el dataset

Como vamos a utilizar una red neuronal totalmente conectada, vamos a redimensionar los subconjuntos de entrenamiento y testing a formato de vector en lugar de en formato de matriz. Esto significa, nuestras imágenes tienen 28x28 pixeles, podemos representar cada uno de sus pixeles como un color entre 0 y 1 ya que normalizamos las imágenes. Ahora en lugar de ponerlo como matriz pondremos un arreglo lineal de 1x(28x28) = 1x784. Esto para tener la primera capa 784 neuronas.


```python
#Como cada imagen tiene 28x28 píxeles, usamos la función reshape en todo el dataset de entrenamiento para convertirlo 
# en vectores de tamaño [-1 (todos los elementos), anchura * altura]
X_train = X_train.reshape(-1, 28*28)
print(X_train.shape)
X_test = X_test.reshape(-1, 28*28)
print(X_test.shape)
```

    (60000, 784)
    (10000, 784)


## Que empiece la construcción del RNA 🍀

## - Definir el modelo
Simplemente se define un objeto de modelo Sequential.


```python
model = tf.keras.models.Sequential()
```

## - Añadir la primera capa totalmente conectada (capa Densa)

Hyper-parametros de la capa:

- Número de unidades/neuronas: **128**

- Función de activación: **ReLU**


```python
model.add(tf.keras.layers.Dense(units=128, activation='relu', input_shape=(784, )))
```

## - Añadir una capa de Dropout

Dropout es una técnica de Regularization donde aleatoriamente se asignan a ciertas neuronas de la red el valor cero. De este modo, mientras se entrena, estas neuronas no actualizarán sus valores. Al tener cierto porcentaje de neuronas sin actualizar, el proceso de entrenamiento toma más tiempo pero por contra tenemos menos posibilidades de sufrir sobreentrenamiento (overfitting).


```python
model.add(tf.keras.layers.Dropout(0.2))
```

## - Añadir capa de salida

En el caso de MNIST tenemos 10 posibles prendas de ropa, por lo que añadiremos una capa con 10 neuronas únicamente al final, en este caso como es una capa de salida y queremos probabilidades por lo mismo, utilizaremos una función de activación SoftMax

- Número de unidades/neuronas: **10** en el caso del Fashion MNIST

- Función de activación: **softmax** (probabilidades de cada clase)


```python
model.add(tf.keras.layers.Dense(units=10, activation='softmax'))
```

## Compilar el modelo

Ahora compilaremos todo nuestro modelo, para ello es necesario una función de 

- Función optimización: Adam

- Función de costo o pérdida: Sparse softmax (categorical) crossentropy

- Métrica: sparse_categorical_accuracy comprueba si el valor verdadero máximo es igual al índice del valor predicho máximo.


```python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])
model.summary()
```

    Model: "sequential"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    dense (Dense)                (None, 128)               100480    
    _________________________________________________________________
    dropout (Dropout)            (None, 128)               0         
    _________________________________________________________________
    dense_1 (Dense)              (None, 10)                1290      
    =================================================================
    Total params: 101,770
    Trainable params: 101,770
    Non-trainable params: 0
    _________________________________________________________________


## Entrenar el modelo



```python
model.fit(X_train, y_train, epochs=5)
```

    Train on 60000 samples
    Epoch 1/5
    60000/60000 [==============================] - 4s 63us/sample - loss: 0.5341 - sparse_categorical_accuracy: 0.80953
    Epoch 2/5
    60000/60000 [==============================] - 3s 57us/sample - loss: 0.4030 - sparse_categorical_accuracy: 0.8540
    Epoch 3/5
    60000/60000 [==============================] - 3s 52us/sample - loss: 0.3692 - sparse_categorical_accuracy: 0.8644
    Epoch 4/5
    60000/60000 [==============================] - 3s 49us/sample - loss: 0.3500 - sparse_categorical_accuracy: 0.8712
    Epoch 5/5
    60000/60000 [==============================] - 3s 49us/sample - loss: 0.3320 - sparse_categorical_accuracy: 0.87820s - loss: 0.3326 - sparse_categorical_accuracy: 0.8





    <tensorflow.python.keras.callbacks.History at 0x149bc7710>



# Evaluación del modelo


```python
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Precisión del modelo: ",test_accuracy)
```

    10000/10000 [==============================] - 0s 37us/sample - loss: 0.3555 - sparse_categorical_accuracy: 0.8684
    Precisión del modelo:  0.8684


Si deseamos, podemos guardar los pesos del modelo en un JSON o en un archivo de nuestra preferencia


```python
#model_json = model.to_json()
#with open("fashion_model.json", "w") as json_file:
#    json_file.write(model_json)
##GUARDAR LOS PESOS
#model.save_weights("fashion_model.h5")
```

## Google Maps API 🗺

Google Maps es un servicio de mapas web desarrollado por Google. Ofrece imágenes satelitales, fotografía aérea, mapas de calles, vistas panorámicas interactivas de 360 ° de las calles, condiciones del tráfico en tiempo real y planificación de rutas para viajar a pie, en automóvil, bicicleta y aire, o en transporte público.


```python
import pandas as pd

import folium
import googlemaps
import gmaps

clinicas = pd.read_csv('ConsultasGmaps.csv', sep=',',encoding='utf_8',dtype="unicode")
clinicas
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CLUES</th>
      <th>LATITUD</th>
      <th>LONGITUD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ASIMS000185</td>
      <td>21.835575</td>
      <td>-102.284527</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ASSSA000960</td>
      <td>21.8463</td>
      <td>-102.711</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BCIMS000460</td>
      <td>32.608992</td>
      <td>-115.3826</td>
    </tr>
    <tr>
      <th>3</th>
      <td>GTSSA016580</td>
      <td>20.5667</td>
      <td>-101.186</td>
    </tr>
    <tr>
      <th>4</th>
      <td>SRSSA017655</td>
      <td>27.048359</td>
      <td>-109.436685</td>
    </tr>
    <tr>
      <th>5</th>
      <td>TCIMS000401</td>
      <td>17.97565</td>
      <td>-92.928943</td>
    </tr>
    <tr>
      <th>6</th>
      <td>TSSSA017791</td>
      <td>23.7319</td>
      <td>-99.1469</td>
    </tr>
    <tr>
      <th>7</th>
      <td>TSSSA017803</td>
      <td>23.7683</td>
      <td>-99.1711</td>
    </tr>
    <tr>
      <th>8</th>
      <td>YNSSA013580</td>
      <td>20.3994</td>
      <td>-89.5377</td>
    </tr>
    <tr>
      <th>9</th>
      <td>ZSIMS000440</td>
      <td>22.953428</td>
      <td>-102.702333</td>
    </tr>
    <tr>
      <th>10</th>
      <td>ZSSSA012504</td>
      <td>22.7398</td>
      <td>-102.504</td>
    </tr>
  </tbody>
</table>
</div>




```python
mapa = folium.Map(
    location=[float(clinicas.iloc[0].LATITUD),
              float(clinicas.iloc[0].LONGITUD)],zoom_start=5,
)

for x in range(len(clinicas.index)):
    folium.Marker(
        location=[float(clinicas.iloc[x].LATITUD), float(clinicas.iloc[x].LONGITUD)],
        popup=clinicas.iloc[x].CLUES,
        icon=folium.Icon(color='blue', icon='asterisk')
).add_to(mapa)
    
mapa
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgCiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgTF9OT19UT1VDSCA9IGZhbHNlOwogICAgICAgICAgICBMX0RJU0FCTEVfM0QgPSBmYWxzZTsKICAgICAgICA8L3NjcmlwdD4KICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjUuMS9kaXN0L2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0xLjEyLjQubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjUuMS9kaXN0L2xlYWZsZXQuY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vYm9vdHN0cmFwLzMuMi4wL2Nzcy9ib290c3RyYXAubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9mb250LWF3ZXNvbWUvNC42LjMvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLzIuMC4yL2xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2Nkbi5naXRoYWNrLmNvbS9weXRob24tdmlzdWFsaXphdGlvbi9mb2xpdW0vbWFzdGVyL2ZvbGl1bS90ZW1wbGF0ZXMvbGVhZmxldC5hd2Vzb21lLnJvdGF0ZS5jc3MiLz4KICAgIDxzdHlsZT5odG1sLCBib2R5IHt3aWR0aDogMTAwJTtoZWlnaHQ6IDEwMCU7bWFyZ2luOiAwO3BhZGRpbmc6IDA7fTwvc3R5bGU+CiAgICA8c3R5bGU+I21hcCB7cG9zaXRpb246YWJzb2x1dGU7dG9wOjA7Ym90dG9tOjA7cmlnaHQ6MDtsZWZ0OjA7fTwvc3R5bGU+CiAgICAKICAgICAgICAgICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwKICAgICAgICAgICAgICAgIGluaXRpYWwtc2NhbGU9MS4wLCBtYXhpbXVtLXNjYWxlPTEuMCwgdXNlci1zY2FsYWJsZT1ubyIgLz4KICAgICAgICAgICAgPHN0eWxlPgogICAgICAgICAgICAgICAgI21hcF84MTMyNDM5NGU0YjA0MDM1ODFjOGY3OTE4ZGVhOTNjMCB7CiAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgICAgIHdpZHRoOiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfODEzMjQzOTRlNGIwNDAzNTgxYzhmNzkxOGRlYTkzYzAiID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFwXzgxMzI0Mzk0ZTRiMDQwMzU4MWM4Zjc5MThkZWE5M2MwID0gTC5tYXAoCiAgICAgICAgICAgICAgICAibWFwXzgxMzI0Mzk0ZTRiMDQwMzU4MWM4Zjc5MThkZWE5M2MwIiwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBjZW50ZXI6IFsyMS44MzU1NzUsIC0xMDIuMjg0NTI3XSwKICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3LAogICAgICAgICAgICAgICAgICAgIHpvb206IDUsCiAgICAgICAgICAgICAgICAgICAgem9vbUNvbnRyb2w6IHRydWUsCiAgICAgICAgICAgICAgICAgICAgcHJlZmVyQ2FudmFzOiBmYWxzZSwKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgKTsKCiAgICAgICAgICAgIAoKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl85MTc0YjU3MmNhNzg0Yzk4YWNmOTM5ZGFiZWQ3MDIyMyA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgImh0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nIiwKICAgICAgICAgICAgICAgIHsiYXR0cmlidXRpb24iOiAiRGF0YSBieSBcdTAwMjZjb3B5OyBcdTAwM2NhIGhyZWY9XCJodHRwOi8vb3BlbnN0cmVldG1hcC5vcmdcIlx1MDAzZU9wZW5TdHJlZXRNYXBcdTAwM2MvYVx1MDAzZSwgdW5kZXIgXHUwMDNjYSBocmVmPVwiaHR0cDovL3d3dy5vcGVuc3RyZWV0bWFwLm9yZy9jb3B5cmlnaHRcIlx1MDAzZU9EYkxcdTAwM2MvYVx1MDAzZS4iLCAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsICJtYXhOYXRpdmVab29tIjogMTgsICJtYXhab29tIjogMTgsICJtaW5ab29tIjogMCwgIm5vV3JhcCI6IGZhbHNlLCAib3BhY2l0eSI6IDEsICJzdWJkb21haW5zIjogImFiYyIsICJ0bXMiOiBmYWxzZX0KICAgICAgICAgICAgKS5hZGRUbyhtYXBfODEzMjQzOTRlNGIwNDAzNTgxYzhmNzkxOGRlYTkzYzApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfYWJiYjc4YjYxZDk1NDVmOWI1Nzk2ZjRmY2Q5MjYxOWMgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFsyMS44MzU1NzUsIC0xMDIuMjg0NTI3XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzgxMzI0Mzk0ZTRiMDQwMzU4MWM4Zjc5MThkZWE5M2MwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl85OGQ0MGNhZmEzZDc0NzJkOWQ0NjI1MjVmNTdiZmNmOCA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiYXN0ZXJpc2siLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImJsdWUiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl9hYmJiNzhiNjFkOTU0NWY5YjU3OTZmNGZjZDkyNjE5Yy5zZXRJY29uKGljb25fOThkNDBjYWZhM2Q3NDcyZDlkNDYyNTI1ZjU3YmZjZjgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2FiYjI4Y2JmY2FiYzRmZGZhMzcyNTJjZTk5MzRiMDY5ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF82ZTIyYjAyM2Q5NjI0M2UzOTRjYmQxNDJjNDFiMjhkYyA9ICQoYDxkaXYgaWQ9Imh0bWxfNmUyMmIwMjNkOTYyNDNlMzk0Y2JkMTQyYzQxYjI4ZGMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFTSU1TMDAwMTg1PC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2FiYjI4Y2JmY2FiYzRmZGZhMzcyNTJjZTk5MzRiMDY5LnNldENvbnRlbnQoaHRtbF82ZTIyYjAyM2Q5NjI0M2UzOTRjYmQxNDJjNDFiMjhkYyk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9hYmJiNzhiNjFkOTU0NWY5YjU3OTZmNGZjZDkyNjE5Yy5iaW5kUG9wdXAocG9wdXBfYWJiMjhjYmZjYWJjNGZkZmEzNzI1MmNlOTkzNGIwNjkpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfNjViMmRkMjNmMWM3NGExNWFiMmJiNDY5MDUyNGNlZTggPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFsyMS44NDYzLCAtMTAyLjcxMV0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF84MTMyNDM5NGU0YjA0MDM1ODFjOGY3OTE4ZGVhOTNjMCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fODJmNzRmODRhNDdiNDRiZDkzN2I0MDcyZjc1MDlmMmYgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogImFzdGVyaXNrIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibHVlIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfNjViMmRkMjNmMWM3NGExNWFiMmJiNDY5MDUyNGNlZTguc2V0SWNvbihpY29uXzgyZjc0Zjg0YTQ3YjQ0YmQ5MzdiNDA3MmY3NTA5ZjJmKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF83ZDhmODM4MmZhM2M0NDJlYTkzMjQyNDc4ODkwMTc2ZSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYzAxODA0YWMzZWMyNGEyYTlhMTIyNDI1MmY1MGU3MTcgPSAkKGA8ZGl2IGlkPSJodG1sX2MwMTgwNGFjM2VjMjRhMmE5YTEyMjQyNTJmNTBlNzE3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BU1NTQTAwMDk2MDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF83ZDhmODM4MmZhM2M0NDJlYTkzMjQyNDc4ODkwMTc2ZS5zZXRDb250ZW50KGh0bWxfYzAxODA0YWMzZWMyNGEyYTlhMTIyNDI1MmY1MGU3MTcpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfNjViMmRkMjNmMWM3NGExNWFiMmJiNDY5MDUyNGNlZTguYmluZFBvcHVwKHBvcHVwXzdkOGY4MzgyZmEzYzQ0MmVhOTMyNDI0Nzg4OTAxNzZlKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzllOGJkZGJhOTZjNjQ2MTg5OTFjMzBlNmVhZjYxM2VjID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzIuNjA4OTkyLCAtMTE1LjM4MjZdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfODEzMjQzOTRlNGIwNDAzNTgxYzhmNzkxOGRlYTkzYzApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzljNmY3OTNkOThmNjQ3OThiMmM5ODNjMTVmMGZiNTFmID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJhc3RlcmlzayIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmx1ZSIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyXzllOGJkZGJhOTZjNjQ2MTg5OTFjMzBlNmVhZjYxM2VjLnNldEljb24oaWNvbl85YzZmNzkzZDk4ZjY0Nzk4YjJjOTgzYzE1ZjBmYjUxZik7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYTdkYmRjNmMxMDUwNDA0Mjg0Y2RiYmMzMmNhYzc2MDUgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2EyM2ZkMTMzNTkwNzQwOGZiM2ZhMDM2YzUyNTQ4NDAwID0gJChgPGRpdiBpZD0iaHRtbF9hMjNmZDEzMzU5MDc0MDhmYjNmYTAzNmM1MjU0ODQwMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QkNJTVMwMDA0NjA8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTdkYmRjNmMxMDUwNDA0Mjg0Y2RiYmMzMmNhYzc2MDUuc2V0Q29udGVudChodG1sX2EyM2ZkMTMzNTkwNzQwOGZiM2ZhMDM2YzUyNTQ4NDAwKTsKICAgICAgICAKCiAgICAgICAgbWFya2VyXzllOGJkZGJhOTZjNjQ2MTg5OTFjMzBlNmVhZjYxM2VjLmJpbmRQb3B1cChwb3B1cF9hN2RiZGM2YzEwNTA0MDQyODRjZGJiYzMyY2FjNzYwNSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl8wYTFhNWVlMGFkNWI0NzliODQwMDI2ZDU3MjRhYTA1OSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzIwLjU2NjcsIC0xMDEuMTg2XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzgxMzI0Mzk0ZTRiMDQwMzU4MWM4Zjc5MThkZWE5M2MwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl8wN2U4MjI4NThlMjY0MjY0OWZjMGFlYzU4YmUwM2VmNiA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiYXN0ZXJpc2siLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImJsdWUiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl8wYTFhNWVlMGFkNWI0NzliODQwMDI2ZDU3MjRhYTA1OS5zZXRJY29uKGljb25fMDdlODIyODU4ZTI2NDI2NDlmYzBhZWM1OGJlMDNlZjYpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2IxNjdhZWFiNDJlOTRhODBiZTljOGVjZTZjNDU3N2Q1ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF83OTE4NjgzYzcxODM0NjQwODI4ZTgwZTk1NDFkYzg5OSA9ICQoYDxkaXYgaWQ9Imh0bWxfNzkxODY4M2M3MTgzNDY0MDgyOGU4MGU5NTQxZGM4OTkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdUU1NBMDE2NTgwPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2IxNjdhZWFiNDJlOTRhODBiZTljOGVjZTZjNDU3N2Q1LnNldENvbnRlbnQoaHRtbF83OTE4NjgzYzcxODM0NjQwODI4ZTgwZTk1NDFkYzg5OSk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl8wYTFhNWVlMGFkNWI0NzliODQwMDI2ZDU3MjRhYTA1OS5iaW5kUG9wdXAocG9wdXBfYjE2N2FlYWI0MmU5NGE4MGJlOWM4ZWNlNmM0NTc3ZDUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfMTMzZWQ1OWE2MTg3NGMzOThiNDMwM2EzMzc1ODc4NWMgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFsyNy4wNDgzNTksIC0xMDkuNDM2Njg1XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzgxMzI0Mzk0ZTRiMDQwMzU4MWM4Zjc5MThkZWE5M2MwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl85MzYzZTEyYWM1ZGE0NjE2Yjk2MmQzNmRhY2ZiZWQzYiA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiYXN0ZXJpc2siLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImJsdWUiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl8xMzNlZDU5YTYxODc0YzM5OGI0MzAzYTMzNzU4Nzg1Yy5zZXRJY29uKGljb25fOTM2M2UxMmFjNWRhNDYxNmI5NjJkMzZkYWNmYmVkM2IpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2NjYzRhNzhlMGZhZDQ2MDdiNjlkMzhhMzhjODA3MDAxID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9lNTdhYjVjYmYxMTQ0OTJiYmJmNjMyZWY2MjFiZGFiOCA9ICQoYDxkaXYgaWQ9Imh0bWxfZTU3YWI1Y2JmMTE0NDkyYmJiZjYzMmVmNjIxYmRhYjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNSU1NBMDE3NjU1PC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2NjYzRhNzhlMGZhZDQ2MDdiNjlkMzhhMzhjODA3MDAxLnNldENvbnRlbnQoaHRtbF9lNTdhYjVjYmYxMTQ0OTJiYmJmNjMyZWY2MjFiZGFiOCk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl8xMzNlZDU5YTYxODc0YzM5OGI0MzAzYTMzNzU4Nzg1Yy5iaW5kUG9wdXAocG9wdXBfY2NjNGE3OGUwZmFkNDYwN2I2OWQzOGEzOGM4MDcwMDEpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfNzQ1MTc1YjBmMjQ0NDg3YmIwNGEwZTkxZWFkMTU0NzIgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFsxNy45NzU2NSwgLTkyLjkyODk0M10sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF84MTMyNDM5NGU0YjA0MDM1ODFjOGY3OTE4ZGVhOTNjMCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fMDBhZDM3MDdkNWIyNDgzZmFjNDI4M2FiYmZjYWY1NGIgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogImFzdGVyaXNrIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibHVlIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfNzQ1MTc1YjBmMjQ0NDg3YmIwNGEwZTkxZWFkMTU0NzIuc2V0SWNvbihpY29uXzAwYWQzNzA3ZDViMjQ4M2ZhYzQyODNhYmJmY2FmNTRiKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8zZDQ0NjA1ODUzN2Y0MmNjYTE0YjFjNmNjNmNiN2RiZSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfODExZThjOGJiNzA4NDUyOTkxZWMyN2ZiODZiNWY5ODYgPSAkKGA8ZGl2IGlkPSJodG1sXzgxMWU4YzhiYjcwODQ1Mjk5MWVjMjdmYjg2YjVmOTg2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UQ0lNUzAwMDQwMTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8zZDQ0NjA1ODUzN2Y0MmNjYTE0YjFjNmNjNmNiN2RiZS5zZXRDb250ZW50KGh0bWxfODExZThjOGJiNzA4NDUyOTkxZWMyN2ZiODZiNWY5ODYpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfNzQ1MTc1YjBmMjQ0NDg3YmIwNGEwZTkxZWFkMTU0NzIuYmluZFBvcHVwKHBvcHVwXzNkNDQ2MDU4NTM3ZjQyY2NhMTRiMWM2Y2M2Y2I3ZGJlKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyX2Q5NzkyYjI2NDczNjRmNWRhN2YzODVlMmI0M2NhMzMyID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMjMuNzMxOSwgLTk5LjE0NjldLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfODEzMjQzOTRlNGIwNDAzNTgxYzhmNzkxOGRlYTkzYzApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzU2ZGM1YzhhYjU2OTRhNmViMjNjYWUxMmU4ZTIxNTQ2ID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJhc3RlcmlzayIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmx1ZSIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyX2Q5NzkyYjI2NDczNjRmNWRhN2YzODVlMmI0M2NhMzMyLnNldEljb24oaWNvbl81NmRjNWM4YWI1Njk0YTZlYjIzY2FlMTJlOGUyMTU0Nik7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYTdhZWY4M2VkMjYxNGExYmIwMDg2MGI3NGUyMTZjOGYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2NjYTJkM2Q2N2JkNjRiY2VhYjFjOTQwM2FhZDFiMzc4ID0gJChgPGRpdiBpZD0iaHRtbF9jY2EyZDNkNjdiZDY0YmNlYWIxYzk0MDNhYWQxYjM3OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VFNTU0EwMTc3OTE8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTdhZWY4M2VkMjYxNGExYmIwMDg2MGI3NGUyMTZjOGYuc2V0Q29udGVudChodG1sX2NjYTJkM2Q2N2JkNjRiY2VhYjFjOTQwM2FhZDFiMzc4KTsKICAgICAgICAKCiAgICAgICAgbWFya2VyX2Q5NzkyYjI2NDczNjRmNWRhN2YzODVlMmI0M2NhMzMyLmJpbmRQb3B1cChwb3B1cF9hN2FlZjgzZWQyNjE0YTFiYjAwODYwYjc0ZTIxNmM4ZikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl9iNzNmZmY0NDA2NTM0ZWIxYmI2MTBhNTQzYzQwM2MxOSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzIzLjc2ODMsIC05OS4xNzExXSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzgxMzI0Mzk0ZTRiMDQwMzU4MWM4Zjc5MThkZWE5M2MwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl8zZmY4OGQ3Yjk2OTY0NGYwYmU0ZTVkNDM5NTI3OTI5YSA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiYXN0ZXJpc2siLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImJsdWUiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl9iNzNmZmY0NDA2NTM0ZWIxYmI2MTBhNTQzYzQwM2MxOS5zZXRJY29uKGljb25fM2ZmODhkN2I5Njk2NDRmMGJlNGU1ZDQzOTUyNzkyOWEpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2YwODczYTQwYjc5MjQwYzdhNGRiYTFjOGJjY2VhNzc4ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF80MzYxN2Y0OTFjZGY0MzliOGRhNzY0YmI5ZDYwYTUzMSA9ICQoYDxkaXYgaWQ9Imh0bWxfNDM2MTdmNDkxY2RmNDM5YjhkYTc2NGJiOWQ2MGE1MzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRTU1NBMDE3ODAzPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2YwODczYTQwYjc5MjQwYzdhNGRiYTFjOGJjY2VhNzc4LnNldENvbnRlbnQoaHRtbF80MzYxN2Y0OTFjZGY0MzliOGRhNzY0YmI5ZDYwYTUzMSk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9iNzNmZmY0NDA2NTM0ZWIxYmI2MTBhNTQzYzQwM2MxOS5iaW5kUG9wdXAocG9wdXBfZjA4NzNhNDBiNzkyNDBjN2E0ZGJhMWM4YmNjZWE3NzgpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfM2JhMGMyNWYxMGVlNGU1ZWEyZDUwMmY0MzM0MWNlYzkgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFsyMC4zOTk0LCAtODkuNTM3N10sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF84MTMyNDM5NGU0YjA0MDM1ODFjOGY3OTE4ZGVhOTNjMCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fNjA1MzIwZTFiNjgwNDQ3ZWFjOTAxZmE4ZmE2MDBmN2MgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogImFzdGVyaXNrIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibHVlIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfM2JhMGMyNWYxMGVlNGU1ZWEyZDUwMmY0MzM0MWNlYzkuc2V0SWNvbihpY29uXzYwNTMyMGUxYjY4MDQ0N2VhYzkwMWZhOGZhNjAwZjdjKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9lNDliM2JmNjk1MmE0NmE0OWI1MTBjNjdmY2U2OTRmYSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZWE2MzZhNDk5OGQ5NDQ5NmJmMzJmMWIxMWE5YjJmNjggPSAkKGA8ZGl2IGlkPSJodG1sX2VhNjM2YTQ5OThkOTQ0OTZiZjMyZjFiMTFhOWIyZjY4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5ZTlNTQTAxMzU4MDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9lNDliM2JmNjk1MmE0NmE0OWI1MTBjNjdmY2U2OTRmYS5zZXRDb250ZW50KGh0bWxfZWE2MzZhNDk5OGQ5NDQ5NmJmMzJmMWIxMWE5YjJmNjgpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfM2JhMGMyNWYxMGVlNGU1ZWEyZDUwMmY0MzM0MWNlYzkuYmluZFBvcHVwKHBvcHVwX2U0OWIzYmY2OTUyYTQ2YTQ5YjUxMGM2N2ZjZTY5NGZhKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzM0YTA3NGFjYmFlYzQ1M2NiMDE0N2YwNjdiZTIxNjI5ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMjIuOTUzNDI4LCAtMTAyLjcwMjMzM10sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF84MTMyNDM5NGU0YjA0MDM1ODFjOGY3OTE4ZGVhOTNjMCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fMTZkNTllNWVlNmFmNDk2ZGI1NDFjOGE3MDU5YWViMjEgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogImFzdGVyaXNrIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibHVlIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfMzRhMDc0YWNiYWVjNDUzY2IwMTQ3ZjA2N2JlMjE2Mjkuc2V0SWNvbihpY29uXzE2ZDU5ZTVlZTZhZjQ5NmRiNTQxYzhhNzA1OWFlYjIxKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8yNGUzNDgwY2RhNTY0MDdhOGI2MjFkM2ExY2FiMWI4NiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYWJiZTNjM2EwMjAxNDRjMDg5ZDQwMDE4ZTE3MGU1YTkgPSAkKGA8ZGl2IGlkPSJodG1sX2FiYmUzYzNhMDIwMTQ0YzA4OWQ0MDAxOGUxNzBlNWE5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5aU0lNUzAwMDQ0MDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8yNGUzNDgwY2RhNTY0MDdhOGI2MjFkM2ExY2FiMWI4Ni5zZXRDb250ZW50KGh0bWxfYWJiZTNjM2EwMjAxNDRjMDg5ZDQwMDE4ZTE3MGU1YTkpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfMzRhMDc0YWNiYWVjNDUzY2IwMTQ3ZjA2N2JlMjE2MjkuYmluZFBvcHVwKHBvcHVwXzI0ZTM0ODBjZGE1NjQwN2E4YjYyMWQzYTFjYWIxYjg2KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyX2QwZTgyMDY4OWM4NTQ0YTJiZmExNDA2YTgyZTBhODYwID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMjIuNzM5OCwgLTEwMi41MDRdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfODEzMjQzOTRlNGIwNDAzNTgxYzhmNzkxOGRlYTkzYzApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uX2Q2ZTdkYzI5MWRlMzRmZjViNDA5NjQxOTVkODFiN2I0ID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJhc3RlcmlzayIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmx1ZSIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyX2QwZTgyMDY4OWM4NTQ0YTJiZmExNDA2YTgyZTBhODYwLnNldEljb24oaWNvbl9kNmU3ZGMyOTFkZTM0ZmY1YjQwOTY0MTk1ZDgxYjdiNCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZTdmNDBmYTY4NzQ3NGU2MzliMjhmOGVkZmYwMWZlNjUgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2YyNDAzODhmMzhjMzRjNWI4YmMwYzJmZmExNDA4MjFhID0gJChgPGRpdiBpZD0iaHRtbF9mMjQwMzg4ZjM4YzM0YzViOGJjMGMyZmZhMTQwODIxYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+WlNTU0EwMTI1MDQ8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZTdmNDBmYTY4NzQ3NGU2MzliMjhmOGVkZmYwMWZlNjUuc2V0Q29udGVudChodG1sX2YyNDAzODhmMzhjMzRjNWI4YmMwYzJmZmExNDA4MjFhKTsKICAgICAgICAKCiAgICAgICAgbWFya2VyX2QwZTgyMDY4OWM4NTQ0YTJiZmExNDA2YTgyZTBhODYwLmJpbmRQb3B1cChwb3B1cF9lN2Y0MGZhNjg3NDc0ZTYzOWIyOGY4ZWRmZjAxZmU2NSkKICAgICAgICA7CgogICAgICAgIAogICAgCjwvc2NyaXB0Pg== onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
gmaps.configure(api_key="AIzaSyCaEFgabVDlUztxMCOfeGo3FmCpQvskmWc")
APIGoogleMaps = googlemaps.Client(key='AIzaSyCaEFgabVDlUztxMCOfeGo3FmCpQvskmWc')
```


```python
figura = gmaps.figure()

for x in range(len(clinicas)):
    if float(clinicas.iloc[x].LATITUD)==21.835575 and float(clinicas.iloc[x].LONGITUD) == -102.284527:
        continue
    RUTA = gmaps.directions_layer((21.835575,-102.284527), (float(clinicas.iloc[x].LATITUD), float(clinicas.iloc[x].LONGITUD)))
    figura.add_layer(RUTA)

figura
```


    Figure(layout=FigureLayout(height='420px'))



```python
request = APIGoogleMaps.distance_matrix((float(clinicas.iloc[0].LATITUD),float(clinicas.iloc[0].LONGITUD)), (float(clinicas.iloc[1].LATITUD), float(clinicas.iloc[1].LONGITUD)))
print(request)
```

    {'destination_addresses': ['Privada Articulo 115 Constitución 912, Zona Centro, 20800 Calvillo, Ags., Mexico'], 'origin_addresses': ['Carolina Villanueva de García 316, Cd Industrial, 20290 Aguascalientes, Ags., Mexico'], 'rows': [{'elements': [{'distance': {'text': '54.8 km', 'value': 54833}, 'duration': {'text': '52 mins', 'value': 3133}, 'status': 'OK'}]}], 'status': 'OK'}



```python
listaLugares = []
listaLugares.clear()

centro = (21.835575,-102.284527)

for x in range(len(clinicas)):
    if float(clinicas.iloc[x].LATITUD)==21.835575 and float(clinicas.iloc[x].LONGITUD) == -102.284527:
        continue
    destino = (float(clinicas.iloc[x].LATITUD), float(clinicas.iloc[x].LONGITUD))
    request = APIGoogleMaps.distance_matrix((21.835575,-102.284527), destino)
    distanciaKM = request["rows"][0]["elements"][0]["distance"]["text"]
    distanciaM = request["rows"][0]["elements"][0]["distance"]["value"]
    tiempoMinH = request["rows"][0]["elements"][0]["duration"]["text"]
    tiempoRealSeg = request["rows"][0]["elements"][0]["duration"]["value"]
    listaLugares.append([clinicas.iloc[0].CLUES,clinicas.iloc[x].CLUES,distanciaKM,distanciaM,tiempoMinH,tiempoRealSeg])
Distancias = pd.DataFrame(listaLugares, columns=["CLUES ORIGEN","CLUES DESTINO","Distancia KM","Distancia M","Tiempo Horas-Min","Tiempo Seg"])
Distancias
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CLUES ORIGEN</th>
      <th>CLUES DESTINO</th>
      <th>Distancia KM</th>
      <th>Distancia M</th>
      <th>Tiempo Horas-Min</th>
      <th>Tiempo Seg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ASIMS000185</td>
      <td>ASSSA000960</td>
      <td>54.8 km</td>
      <td>54833</td>
      <td>52 mins</td>
      <td>3133</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ASIMS000185</td>
      <td>BCIMS000460</td>
      <td>2,248 km</td>
      <td>2248077</td>
      <td>23 hours 52 mins</td>
      <td>85935</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ASIMS000185</td>
      <td>GTSSA016580</td>
      <td>209 km</td>
      <td>209454</td>
      <td>2 hours 18 mins</td>
      <td>8265</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ASIMS000185</td>
      <td>SRSSA017655</td>
      <td>1,246 km</td>
      <td>1245712</td>
      <td>14 hours 6 mins</td>
      <td>50783</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ASIMS000185</td>
      <td>TCIMS000401</td>
      <td>1,226 km</td>
      <td>1226458</td>
      <td>13 hours 30 mins</td>
      <td>48582</td>
    </tr>
    <tr>
      <th>5</th>
      <td>ASIMS000185</td>
      <td>TSSSA017791</td>
      <td>499 km</td>
      <td>499373</td>
      <td>6 hours 0 mins</td>
      <td>21629</td>
    </tr>
    <tr>
      <th>6</th>
      <td>ASIMS000185</td>
      <td>TSSSA017803</td>
      <td>508 km</td>
      <td>508237</td>
      <td>6 hours 8 mins</td>
      <td>22085</td>
    </tr>
    <tr>
      <th>7</th>
      <td>ASIMS000185</td>
      <td>YNSSA013580</td>
      <td>1,772 km</td>
      <td>1771573</td>
      <td>20 hours 44 mins</td>
      <td>74636</td>
    </tr>
    <tr>
      <th>8</th>
      <td>ASIMS000185</td>
      <td>ZSIMS000440</td>
      <td>145 km</td>
      <td>145358</td>
      <td>2 hours 4 mins</td>
      <td>7419</td>
    </tr>
    <tr>
      <th>9</th>
      <td>ASIMS000185</td>
      <td>ZSSSA012504</td>
      <td>118 km</td>
      <td>118321</td>
      <td>1 hour 41 mins</td>
      <td>6079</td>
    </tr>
  </tbody>
</table>
</div>




```python
Distancias.to_csv("DistanciasGoogleMaps.csv")
```


```python
import networkx as nx 
import matplotlib.pyplot as plt 

G= nx.barabasi_albert_graph(40,15) 
nx.draw(G, with_labels=True) 
plt.show() 
```


    
![png](output_118_0.png)
    

