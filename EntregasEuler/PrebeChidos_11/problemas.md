
# Ejercico 8

### Encontrar los 13 numeros adyacentes que tenga el mayor producto.

73167176531330624919225119674426574742355349194934 <br>
96983520312774506326239578318016984801869478851843<br>
85861560789112949495459501737958331952853208805511<br>
12540698747158523863050715693290963295227443043557<br>
66896648950445244523161731856403098711121722383113<br>
62229893423380308135336276614282806444486645238749<br>
30358907296290491560440772390713810515859307960866<br>
70172427121883998797908792274921901699720888093776<br>
65727333001053367881220235421809751254540594752243<br>
52584907711670556013604839586446706324415722155397<br>
53697817977846174064955149290862569321978468622482<br>
83972241375657056057490261407972968652414535100474<br>
82166370484403199890008895243450658541227588666881<br>
16427171479924442928230863465674813919123162824586<br>
17866458359124566529476545682848912883142607690042<br>
24219022671055626321111109370544217506941658960408<br>
07198403850962455444362981230987879927244284909188<br>
84580156166097919133875499200524063689912560717606<br>
05886116467109405077541002256983155200055935729725<br>
71636269561882670428252483600823257530420752963450<br>


```python
#Se declara como variable global la lista que contiene los numeros
lista= "\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

#Se define una funcion que recibe la posicion actual, la posicion del producto mayor y el producto más grande hasta el momento
def mayorProducto(posicion,Mayor_producto, posicionMayor):
    longitud=13 #Se declara una variable con la longitud que buscamos
    if posicion + longitud < len(lista): #Se comprueba que exista una cadena de 13
        producto=1                       #Se declara el producto en 1
        for i in range(longitud):        #un ciclo que recorrera los 13 numeros
            num=int(lista[posicion+i])   #Se transforma el nuero a entero(se declararon como cadena de texto)
            producto *= num              #Se calcula el producto
        if producto>Mayor_producto:      #Se comprueba si el producto es mayor que el anterior calculado
            Mayor_producto= producto     #Si es mayor el producto, entonces la variable Mayor_producto adquiere este nuevo valor
            posicionMayor=posicion       #La posicion también se guarda para posteriormente imprimir los numeros
        posicion+=1                      #Se recorre en 1 la posicion para probar la nueva cadena
        mayorProducto(posicion,Mayor_producto, posicionMayor)        #Se llama nuevamente la funcion
    else:                                #Si ya no es posible generar una nueva cadena entra en esta condicion
        print('Los numeros que generan el mayor producto: ',lista[posicionMayor:posicionMayor+longitud]) #Se imprime  la cadena de números
        print('Producto = ',Mayor_producto)
posicion_actual=0
posicionMayor=0
Mayor_producto=-1
mayorProducto(posicion_actual, Mayor_producto, posicionMayor)
```

    Los numeros que generan el mayor producto:  5576689664895
    Producto =  23514624000



```python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#El entero positivo más pequeño que es divisible por los numeros de 1 a 20
#O sea, el mínimo común múltiplo
#Podemos utilizar el máximo común divisor para encontrarlo
#El máximo común divisor puede encontrarse con el algoritmo Euclidiano

"""
El algoritmo Euclidiano o algoritmo de Euclides es una técnica que nos permite 
encontrar rapidamente el máximo común divisor de dos enteros dados a,b.
1. Se divide el número mayor entre el menor
2. Si la división es exacta, el divisor es el MCD
3. Si no es exacta, dividimos el divisor entre el resto obtenido y continua
   hasta obtener una división exacta. El MCD es el último divisor.
"""

#Implementando el algoritmo Euclidiano para Maximo Comun Divisor
def algoritmo_Euclides(numerador,denominador):
    divResiduo = numerador%denominador       #Si es 0, la división es exacta y paramos
    while divResiduo != 0:                   #Mientras el residuo no sea 0
        numerador = denominador              #El denominador se vuelve numerador
        denominador = divResiduo             #El residuo se vuelve el denominador
        divResiduo = numerador % denominador # Efectuamos la division de numerador y denominador.
    return denominador        #cuando el residuo sea 0, entonces retornamos el MCD

```


```python
#Probando el algoritmo de Euclides para ontener el MINIMO COMUN DIVISOR
print(algoritmo_Euclides(15,10)) #Debe ser 5
print(algoritmo_Euclides(21,28)) #Debe ser 7
print(algoritmo_Euclides(18,81)) #Debe ser 9
```

    5
    7
    9



```python
#Implementando el algoritmo del minimo común múltiplo
"""
La formula para obtener el minimo común multiplo entre dos numeros se ve de la forma
MCM = (A*B)/MCD(A,B)
"""

resultado = 1              #Inicializamos la variable, asignamos 1 porque no modifica el resultado inicial.
for i in range(1,21):      # Rango de 1 a 20, excluye el 21
    min_com_div = algoritmo_Euclides(i, resultado) #El MCD entre el iterador i y resultado
    resultado = (resultado * i)/ min_com_div       #Obtenemos el MCM para el valor i y el resultado de la iteracion
print("El mínimo común múltiplo es: ", resultado)  #Cuando termina imprime el resultado final.

#Ojo, la variable resultado cambia de valor con cada iteración y por consecuencia cambia el resultado final.
```

    El mínimo común múltiplo es:  232792560.0


# Special Pythagorean triplet

Un Triplete Pitagórico se trata de la combinación de 3 números enteros que cumpla con la siguiente característica:

\begin{equation}
    a^2 + b^2 = c^2
\end{equation}

En donde debe cumplirse que:
\begin{equation}
    a < b < c
\end{equation}


Aquí tienes un ejemplo:
\begin{equation}
    3^2 + 4^2 = 9 + 16 = 25 = 5^2
\end{equation}

Pero existe un triplete especial en donde la suma de los tres números da como resultado 1000.

\begin{equation}
    a + b + c = 1000
\end{equation}

### Problema

Es requerido encontrar el producto de los 3 números que cumplen la condición de dicho triplete.

### Solución

Para el plantamiento de la solución que se realizó fue el siguiente:

#### Función de verificación
Primeramente se define una función para que realice un proceso de verificación para saber si una de las combinaciones es 
válida.

Básicamente, esta función define si tres números cumplen con la condición de $a^2 + b^2 = c^2$, en dado caso que se cumpla, se muestra en pantalla los resultados y se retorna un **True** para que paren las iteraciones de los ciclos que generan las combinaciones de números.


```python
def verificar(a,b,c):
    if ((a**2)+(b**2)) == (c**2):
        print("#\tEl conjunto de los tres valores naturales que cumplen\t\t#\n#\tcon la condición son los siguientes:\t\t\t\t#")
        print("#\t\ta =",a,"\t\t\t\t\t\t#")
        print("#\t\tb =",b,"\t\t\t\t\t\t#")
        print("#\t\tc =",c,"\t\t\t\t\t\t#")
        print("#\tAquí puede verse la comprobación con los valores indicados:\t#")
        print("#\ta^2 =",(a**2),"b^2 =",(b**2),"c^2 =",(c**2),"\t\t\t\t#")
        print("#\ta^2 + b^2 =",(a**2)+(b**2),"\t\t\t\t\t\t#")
        print("#\tEl resultado final es: ", (a*b*c),"\t\t\t\t#")
        print("#                                                                       #")
        print("#########################################################################")
        return True
    else:
        return False
```

#### Función de ejecución

Para esta solución se propone una función que desarrolle las combinaciones a probar, en medida de esto, se manejaron 3 ciclos itereativos anidados. En donde cada uno de los límites se maneja mediante el requerimiento donde $a < b < c$.

La idea principal es saber hasta que punto pueden llegar cada una de las variables donde se cumpla la condición.
Ya que se busca iniciar la iteración con el número mayor, entonces el movimiento de las variables será algo como lo siguente:

\begin{equation}
    [ 1, 2, 3 ] \\
    [ 1, 2, 4 ] \\
    [ 1, 2, 5 ] \\
    [ 1, 2, 6 ] \\
     ... \\
    [ 1, 2, 995 ] \\
    [ 1, 2, 996 ] \\
    [ 1, 2, 997 ] \\
    [ 1, 3, 4 ] \\
\end{equation}

De forma general, las combinaciones que pasarán por la verificación serán aquellas combinaciones donde $a + b + c = 1000$, por lo que hay muchísimas combinaciones de números omitidas, en consecuencia, hace que el algoritmo tarde menos tiempo de ejecución.


```python
def encontrar_triplete():
    print("\n#########################################################################")
    print("#                                                                       #")
    print("#\tComenzó la búsqueda del triplete pitagórico especial!\t\t#")
    print("#                                                                       #")
    
    # Como resultado base, se define que el éxito en la búsqueda es False para que en su momento pueda cambiar su valor y ser
    # capaz de romper los ciclos iterativos que ya no son necesarios de ejecutar.
    exito = False
    
    # Para el primer ciclo iterativo, se mantiene que los valores de "a" siempre estarán entre 1 y 332, pues si llega a un 333
    # el requerimiento donde a + b + c YA NO es igual a 1000.
    for a in range(1,333):
        
        # Para el caso del segundo ciclo, es necesario que siempre comience siendo una unidad mayor a la "a", por otro lado,
        # para el caso de b los posibles valores válidos siempre estarán entre 2 y 499, ya que si "b" alcanza alguno de los 
        # valores fuera de ese rango ya no se cumpirían los requerimientos mencionados en el ciclo anterior.
        for b in range(a+1,500):
            
            # En este último ciclo se maneja la misma estructura que los anteriores, pero este estará delimitado en un rango
            # de 3 hasta 997.
            for c in range(b+1,998):
                
                # Posteriormente, es necesario indicar que solo las combinaciones que sumen en total 1000 con las posibles 
                # cantidatas a ser "verificadas", por esto mismo es que si no se cumple es como solo se salta a la siguiente 
                # itereación con la palabra reservada "continue".
                if a+b+c == 1000:
                    
                    # Ya que si una combinación si es contada como candidata, se manda a llamar a la función "verificar" con
                    # aquella combinación de números en ese momento. Retornará un valor booleano, si este es un True
                    # (referente a "se trata de la solución al problema") hará que se detengan los demás ciclos mediante la 
                    # palabra reservada "break".
                    exito = verificar(a,b,c)
                    if exito:
                        break
                else:
                    continue
            if exito:
                break
        if exito:
            break
```

#### Ejecución de la implementación propuesta

Para la ejecución de este programa, es más que suficiente mandar a llamar a la función que implementa todo el algoritmo propuesto, ya que la función verificar se encargar de realizar la muestra de resultados.


```python
encontrar_triplete()
```

    
    #########################################################################
    #                                                                       #
    #	Comenzó la búsqueda del triplete pitagórico especial!		#
    #                                                                       #
    #	El conjunto de los tres valores naturales que cumplen		#
    #	con la condición son los siguientes:				#
    #		a = 200 						#
    #		b = 375 						#
    #		c = 425 						#
    #	Aquí puede verse la comprobación con los valores indicados:	#
    #	a^2 = 40000 b^2 = 140625 c^2 = 180625 				#
    #	a^2 + b^2 = 180625 						#
    #	El resultado final es:  31875000 				#
    #                                                                       #
    #########################################################################


# Solución de problemas de *Proyect Euler*

## Problema 1. ##

```
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
```

**Solución:**
```
Nos pide el problema cuál es la suma de todos los multiplos de 3 o 5 debajo de 100. Entonces es el siguiente código:
```



```python
n=1000 #Es el n que se quiere calcular, mejor dicho el natural.
lista=[]
#Se hace el ciclo para un rango de (1,1000) 
#Dentro del ciclo pregunta si es multiplo de 3 o 5
#Si es así lo agrega a la lista y aumenta el valor de x.
for x in range(1,n): 
	if x%3==0 or x%5==0:
		lista.append(x)
		x+=1
print("La suma de los multiplos de 3 o 5 hasta el 100 es:",sum(lista)) #Finalmente imprime la suma

```

    La suma de los multiplos de 3 o 5 hasta el 100 es: 233168


## Problema 3. ##

```
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
```

**Solución:**
```
Nos pide el problema cuál es el factor primo mayor del numero 600851475143. En Python se declaró la siguiente función:
```



```python
def imprimir_max_factor_primo(number): #Se declara la función que recibe como parametro "number".
    lista=[] #En esta lista vacia se va guardar el factor primo en forma de lista.
    factor = 2 #Se declara la variable con valor igual a 2 para el inicio número primo.
    '''En el siguiente "while" se cumple mientras que factor primo sea menor igual a "numero".
    Al entrar al ciclo verifica si el factor es un divisor de numero'''
    while factor <= number:
        if not (number % factor != 0):#Si cumple entonces se divide entre el original.
            number /= factor 
            lista.append(factor)#Con cada ciclo que pasa se va agregando un elemento a la lista.
        else:# Si no se cumple el factor aumenta 1.
            factor += 1
    print("El factor primo máximo es:",max(lista)) #Con max() se obtiene el valor máximo de la lista y se imprime.

imprimir_max_factor_primo(600851475143)

```

    El factor primo máximo es: 6857


## Problema 6. ##

```
The sum of the squares of the first ten natural numbers is,
```
\begin{equation}
    1^2+2^2+\dots+10^2=385.
\end{equation}
```
The square of the sum of the first ten natural numbers is,
```
\begin{equation}
    (1+2+\dots+10)^2=55^2=3025.
\end{equation}
```
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
```
\begin{equation*}
 3025-385=2640
\end{equation*}
```
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
```

**Solución:**
```
En realidad este es un problema sencillo, y no tan laborioso de programar teniendo en cuenta algunos conceptos.
Dando un repaso de un poco de álgebra o cálculo depende el caso. Para saber cuanto es la suma de 1 hasta 100 tenemos que recordar algo importante de un señor llamado Johann Carl Friedrich Gauss quien se dice que en juventud cuando iba en la primaria su profesor les dejo un ejercicio para estuvieran quietos, les dejo sumar lo números naturales del 1 a 100, en pocos instantes el joven Gauss lo resolvió en poco tiempo, la respuesta del problema para la suma de n números naturales que después se le llamó "La suma de Gauss".
```
```
Para la suma de naturales:
```
\begin{equation}
\sum_{k=1}^{n}=\frac{n(n+1)}{2}.
\end{equation}
```
Esto se puede llevar a los polinomios de grado n, con la siguiente expresión
```
\begin{equation}
\sum_{k=1}^{p}=\frac{n^{p+1}}{p+1}+An^{p}+Bn^{p-1}+Cn^{p-2}+\dots.
\end{equation}

```
Después de todo esta discución, el problema dice que se tiene que calcular la suma de los cuadrados, y esto se logra fácilmente aplicando la suma Gaussiana. Tenemos que:
```
\begin{equation}
    1^2+2^2+\dots+n^2=\frac{n(n+1)(2n+1)}{6}.
\end{equation}
```
Esto es verdadero y se puede demostrar usando inducción matemática (Como dice el autor del libro de Calculus de Michael Spivak "Se le queda como ejercicio al lector").
Finalmente hay una manera eficas de calcular el segundo punto que es el cuadrado de la suma, tenemos una equivalencia en matemáticas que es la siguiente:
```
\begin{equation}
    (1+2+\dots+n)^2=1^3+\dots+n^3.
\end{equation}
```
Finalmente ya podemos hacer el código, si para la suma de los cuadrados que vamos a tener n=100, y para los cuadrados de la suma tenemos m=100.
```


```python
n=100
lista=[] #Dejamos esta lista vacia para que podamos guardar los elementos en el for.
m=100
sum_square=((n*(n+1)*(2*n+1))/6)#Aplicamos la ecuación de Gauss.

#En el for se va ir agregando los elementos al cubo.
for square_sum in range(1,m+1):
	square_sum=(square_sum**3)
	lista.append(square_sum)

#Se hace la diferencia.
dif_square=sum(lista)-int(sum_square)
print("La diferencia es: ",dif_square)
```

    La diferencia es:  25164150


## Problema 10. ##

```
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
```
```
En este problema principalmente lo que pide es la suma de los números primos abajo de 2,000,000.
Primero vamos a definir una función y con ello se trabajará.
```



```python
def prime_numbers(max_number):#Definimos a la función prime_numbers()
    # Crear una lista que contiene el estado (tachado/no tachado)
    # de cada número desde 2 hasta max_number.
    numbers = [True, True] + [True] * (max_number-1) #Se crea una lista que contiene si está en True y disminuye una unidad el número. 
    #Esta lista esta inicializada en 2, porque es el primer número donde está definido el campo.
    last_pr_number = 2# Esta variable contiene el número actual en la lista, que siempre es un múltiplo de last_pr_number.
    i = last_pr_number
    
    """Volviendo al problema 3 se aplica la misma condición nada más que es el cuadrado de último número primo tenido y que 
    se compara con el numero sea mayor o igual""" 
    while last_pr_number**2 <= max_number:
        i += last_pr_number #Obtener el último digito del número primo
        while i <= max_number: #En el segundo while se obtiene el siguiente número primo y se cumpla la condición
            numbers[i] = False
            i += last_pr_number
        j = last_pr_number + 1
        while j < max_number:
            if numbers[j]:
                last_pr_number = j
                break
            j += 1
        i = last_pr_number
        """Finalamente hasta que sea difierente se rompe el ciclo, y se agreaga el último número primo"""
    
    #Retornar todas los números de la lista de todos los núemeros primos.
    return [i + 2 for i, not_sin in enumerate(numbers[2:]) if not_sin] #Se hace una función compacta 
a=2000000
print("La suma de numeros primos de la cantidad debajo",a, "fue de:", sum(prime_numbers(a))) #En la última linea de código es para optimizar, ya que se intentó hacer de otra manera pero es más tardada.

```

    La suma de numeros primos de la cantidad debajo 2000000 fue de: 142913828922


# Problem 11: Largest product in a grid

In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

*What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?*


```python
cuadrilla =[]
cuadrilla.append([8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8])
cuadrilla.append([49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0])
cuadrilla.append([81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65])
cuadrilla.append([52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91])
cuadrilla.append([22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80])
cuadrilla.append([24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50])
cuadrilla.append([32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70])
cuadrilla.append([67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21])
cuadrilla.append([24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72])
cuadrilla.append([21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95])
cuadrilla.append([78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92])
cuadrilla.append([16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57])
cuadrilla.append([86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58])
cuadrilla.append([19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40])
cuadrilla.append([4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66])
cuadrilla.append([88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69])
cuadrilla.append([4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36])
cuadrilla.append([20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16])
cuadrilla.append([20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54])
cuadrilla.append([1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67, 48])
```


```python
#Máximo producto horizontalmente
maximoResultado = 0 #Inicializamos la variable en la que se guardara el producto máximo
for j in range(20): #Con j recorremos cada renglón
    for k in range(0,20,4): #Utilizamos k con un paso de 4 para conocer el primero de los 4 números que vamos a multiplicar
        i = k #inicio
        t = k + 4 #tope
        multiplicacion = 1  #Inicializamos la variable en la que vamos a guardar el resultado de la multiplicación actual 
        for i in range(k, t): #Recorremos los cuatro números que vamos a multiplicar
            multiplicacion *= (cuadrilla[j][i]) #Llevamos el total de la multiplicación
            if multiplicacion > maximoResultado: #Comparamos si es la mayor hasta el momento
                maximoResultado = multiplicacion #En caso de ser así actualizamos el valor de maximoResultado

#Máximo producto verticalmente
for j in range(20): #Con j recorremos las columnas 
    for k in range(0,20,4):
        i = k #inicio
        t = k + 4 #tope
        multiplicacion = 1 
        for i in range(k, t):
            multiplicacion *= (cuadrilla[i][j])
            if multiplicacion > maximoResultado:
                maximoResultado = multiplicacion
                
#Máximo producto en diagonal de izquierda a derecha
for k in range(3,20): #Con k iniciamos en la posición 3 ya que apartir de ella se pueden realizar multiplicaciones en diagonal
    multiplicacion = 1
    for i in range(len(cuadrilla)-4): #Cuidamos no exceder los límites del arreglo
        #Hacemos una multiplicación desplazandonos hacia abajo y a la derecha con respecto a k e i
        multiplicacion = ((cuadrilla[k][i]) * (cuadrilla[k-1][i+1]) * (cuadrilla[k-2][i+2]) * (cuadrilla[k-3][i+3]))
        if multiplicacion > maximoResultado:
            maximoResultado = multiplicacion    
            
#Máximo producto en diagonal de derecha a izquierda
for j in range(len(cuadrilla)-4): #Con j recorremos los renglones pero sin pasar de la posición 16 ya que a partir de ella deja de ser posible hacer multiplicaciones en diagonal de 4 números
    for k in range(len(cuadrilla[j])-4):#De la misma manera con k evitamos llegar más alla de la columna 16
        multiplicacion = 1
        for i in range(4): #Utilizamos i para mover a j y k del 0 al 3 de 1 en 1
            multiplicacion *= (cuadrilla[j+i][k+i])
            if multiplicacion > maximoResultado:
                maximoResultado = multiplicacion
print("El producto máximo es:", maximoResultado) #Mostramos el resultado final
```

    El producto máximo es: 70600674


The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

Omar Armando Olazábal Baquero
En este problema nos piden hallar el numero triangular con mas de 500 divisores


```python
from math import sqrt #importamos raiz cuadrada ya que el método a utilizar la usa
def numero_triangular(a):#Esta función regresará una lista de numeros triangulares, recibiendo la cantidad de iteraciones a realizar
    lista=[]#creamos la lista
    ult_num=0#aqui se guardará el ultimo numero generado
    for i in range (1,a+1):#Generamos un ciclo que empieza en 1 y acaba en a
    #(no puede ser solo a por que faltaria un paso para ser la cantidad total)
        ult_num+=i
        lista.append(ult_num)
    return lista
def numero_de_divisores(a):#con esta función contaremos el número de divisores de un número
    raiz = sqrt(a) #Usamos la raiz ya que el máximo divisor de un numero es su raiz antes de que se roten los divisores
    #como por ejemplo podemos tomar 100, cuya lista de divisores seria 1,2,4,5,10,25,50,100, y su raiz cuadrada es 10
    #le llamo "rotar" a que los divisores de la izquierda de la raiz se multiplican con los de la derecha, entonces
    #al sobrepasar la raíz simplemente es la segunda pareja de los numeros a la izquierda
    cont=0#numero de divisores
    i=1
    while i<=raiz:#empezamos en 1 y terminamos en el maximo divisor, osease, la raíz
        if (a%i)==0:
            cont+=2# contamos dos por que es el numero encontrado y su pareja a la derecha de la raiz
        i+=1
    if raiz * raiz == a:
        cont-=1 #en el caso de que sea raiz perfecta quitamos 1 para no contar dos veces la raiz
    return cont


#vamos a probar con el ejemplo dado (7 deberia terminar en 28)
print(numero_triangular(7))
#ahora para hallar el que sobrepase los 500 divisores, usamos un while que compruebe el ultimo de cada iteración
j=1#contador para el while que empieza en 1
while numero_de_divisores(numero_triangular(j)[-1]) < 500:
    j+=1
print("El numero con mas de 500 divisores es: "+str(numero_triangular(j)[-1]))#vemos el numero
#hay metodos más rápidos pero no los entendi xd


 

```

    [1, 3, 6, 10, 15, 21, 28]
    El numero con mas de 500 divisores es: 76576500



```python
#Problem 13 Project Euler. 
#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import time
start_time = time.time()

#Importamos time para ver el tiempo de ejecución   

#Al ser un numero tan grande, meteremos los números en un String 
chicharron = '''37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690'''

#metemos los números a una lista, para poder manejarlos y ocuparemos strip para quitar los caracteres iniciales y finales. 
numeros = chicharron.strip().split('\n')

#Casteamos los numeros a enteros. 
numeros = [int(x) for x in numeros]
solution = sum(numeros)

suma = str(solution)[:10] #Con los dos puntos especificamos los numeros que queremos que aparezcan. 

print("Los diez primeros dígitos de la sumade los 100 - 50 numeros es  "+ suma)

end_time = time.time()

total_time = end_time - start_time

print ('Total time taken: '+str(total_time)) #Imprimimos el tiempo total de ejecución 
```

    Los diez primeros dígitos de la sumade los 100 - 50 numeros es  5537376230
    Total time taken: 0.0010204315185546875



```python
#Problema 2 de Proyect Euler.net

#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Creamos nuestras variables que vamos a utilizar:
primerNumero = 0
segundoNumero = 1
resultadoFibonacci = 0
sumaPares = 0

#Hacemos un ciclo while para generar los números de la serie de fibonacci hasta que sean menores o iguales a 4 millones:
while resultadoFibonacci <= 4000000:
    #Hacemos la suma de los dos primeros números para obtener el siguiente número de la serie de Fibonacci.
	resultadoFibonacci = primerNumero + segundoNumero
	primerNumero = segundoNumero #Actualizamos el valor del primer número con el segundo número, para seguir avanzando.
	segundoNumero = resultadoFibonacci #De igual manera actualizamos el segundo número con el nuevo valor de la serie de Fibonacci.
	if resultadoFibonacci % 2 == 0: #Si el número de la serie de fibonacci es par, entonces hagamos la suma.
		sumaPares += resultadoFibonacci#Acumulamos el valor de la suma.

#Con el último valor de la variable sumaPares, obtenemos la solución.
print ("El total de la suma de los números pares generados por la serie de Fibonacci")
print ("y que no exceden el valor de 4 millones es: {}".format(sumaPares))
```

    El total de la suma de los numeros pares generados por la serie de Fibonacci
    y que no exceden el valor de 4 millones es: 4613732



```python
#Problema 2 de Proyect Euler.net
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#Creamos nuestra función que nos va a permitir verificar que un número es palíndromo.
def numeroPalindromo(i):#Recibe el valor del producto de dos números con 3 digitos cada uno.
    #Converimos el número recibido en un string y verificamos si es igual al string que representa ese mismo número pero invertido.
    #Si ambas cadenas son iguales, entonces tenemos un número palíndromo.
    return str(i) == str(i)[::-1] #Ejemplo: 100 * 101 = 10100;  10100 = 00101 ? la respuesta es: False.

#Creamos nuestras variables que vamos a utilizar:
palindromoMasGrande = 0
numero1 = 0
numero2 = 0

#Creamos 2 ciclos for anidados que nos permitirán hacer solamente el producto 
#de números con 3 digitos en adelante, de esta manera obtimizamos código
#ignorando a los números que son menores que 100.
for i in range(100, 999):
    for j in range(i+1, 1000):
        #Realizamos el producto de 2 números con 3 digitos, este valor lo vamos a ingresar en nuestra función: "numeroPalindromo".
        producto = i * j 
        #Si el valor del producto es un número Palíndromo y es mayor que el Palíndromo más grande, entonces haz lo siguiente:
        if numeroPalindromo(producto) and producto > palindromoMasGrande:
            palindromoMasGrande = producto #Actualizamos el valor del "palindromo más grande".
            numero1 = i #Almacenamos el valor de los dos números que formaron el producto.
            numero2 = j

#Finalmente imprimimos los resultados que han sido almacenados durante la ejecución de los ciclos anteriores:
print("El palíndromo más grande hecho del producto de dos números de 3 dígitos es: {}".format(palindromoMasGrande))
print("Formado por el producto de los números:")
print("Primer número: {}".format(numero1))
print("Segundo número: {}".format(numero2))
```

    El palíndromo más grande hecho del producto de dos números de 3 dígitos es: 906609
    Formado por el producto de los números:
    Primer número: 913
    Segundo número: 993


# 10001 st


```python
posicion = 10001 #st primo
primo = 1
num = 2 
cont = 1
while cont <=posicion: #mientras el contador sea menor o igual a 10001st hacer:
    primo = 1
    for i in range (2,num): #En este for se determina si el numero es primo
        if num%i == 0:      #al obtener el modulo el cual si es = 0
            primo = 0       #la bandera cambia de estado para no tomar el cuenta el numero
            break           
    if primo :   #si la badera ES_PRIMO tiene el valor 1  
        cont += 1 #se incrementa el contador para tomar en cuenta ese numero
    num += 1  #numero se incrementa +1 

print(num-1) #al ya no cumplir con la condicion el numero final se imprime -1 
#ya que despues de entrar al ultimo while se incremente num 
            
```
