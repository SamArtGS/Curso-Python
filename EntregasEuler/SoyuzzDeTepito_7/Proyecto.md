
<br><br><p style="text-align: center;">
<font size="6">**Python Proyecto Equipo 1**</font></p>
<br><br><br>
<font size="5">**Integrantes:**</font>
<font size="4"> <br>
* Galindo Ruiz Abraham
* García Miranda Athenas Marlene
* García Serrano Héctor Mauricio
* Huarte Nolasco Mario
* Merino Hernández Ailyn
* Minero Pineda Erick Rodrigo
* Lira Navarro Juan Arturo
    
</font>

# Problema 1

Si enumeramos todos los números naturales por debajo de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

Encuentra la suma de todos los múltiplos de 3 o 5 por debajo de 1000.


```python
suma=0
for i in range(1000):
    if i%5==0 or i%3==0:
        suma+=i
print(suma)
```

    233168


# Problema 2
Cada nuevo término de la secuencia de Fibonacci se genera sumando los dos términos anteriores. Al comenzar con 1 y 2, los primeros 10 términos son:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Considerando los términos en la secuencia de Fibonacci cuyos valores no excedan los cuatro millones, encuentre la suma de los términos pares.


```python
actual=2
anterior=1
sumaPares=0
while actual<=4000000:
    if actual%2==0:
        sumaPares+=actual
    actual+=anterior
    anterior=actual-anterior
print(sumaPares)
```

    4613732


# Problema 3
Los factores primos de 13195 son 5, 7, 13 y 29.

¿Cuál es el factor primo más grande del número 600851475143?


```python
#Definimos la constante
numero=600851475143
#Para buscar el divisor y por definición de número primo, iniciamos en 2
i=2 
#Iteramos para encontrar el divisor primo
#Verificamos que el factor que estamos buscando sea menor al número en cuestión
while i<=numero: 
    #este contador sirve para enumerar cuántos valores anteceden a "i" 
    #por lo tanto para cada valor de "i" se reinicia la cuenta
    contador=0
    #Para saber cuántos antecesores tiene el supuesto número primo ("i")..
    for j in range(2,i):
        #Contamos cuando el módulo entre "i" y el antecesor es diferente de cero
        if i%j!=0:
            contador=contador+1
    #En la siguiente condición validamos que "i" es un número primo
    #Primero verificamos que ninguno de los números que le anteceden lo puedan dividir
    #Después calculamos el módulo del "número" entre "i" para corroborar que es factor 
    if contador==i-2 and numero%i==0 :
        #Sabiendo que "i" es primo y a la vez factor de "número"
        #consideramos momentaneamente a "i" como el factor primo más grande
        primoMayor=i
        #Validamos al primo más grande dividiendo al número original varias veces
        #para esto necesitamos una bandera que detenga dicha división
        bandera=0
        while bandera==0:
            numero=numero/primoMayor
            #Debido a que "i" va en aumento y la división disminuye
            #cuando éstos dos valores se encuentran
            #quiere decir que encontramos al factor primo más grande
            if numero%primoMayor!=0:
                bandera=1
    #buscamos el siguiente número primo           
    i=i+1
print(primoMayor)
```

    6857


# Problema 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


```python
bandera=0 #esta variable es para que no muestre mas palindromos mas que el mas grande
#usamos dos for para obtener la multiplicacion ya que con solo la operacion de multiplicacion no podemos obtener
#todos los numeros del 0 al 999*999
for i in range(999,900,-1):
    for j in range(999,900,-1):
        #transformamos el numero en string para poder invertirlo sin problema
        numero=str(i*j)
        numero_rev=numero[::-1]#invertimos el numero para comprobar que sea palindromo
        if(numero==numero_rev):#comparamos que sea palindromo
            print(numero)
            bandera=1
            break
    if bandera ==1:        
        break
```

    906609


# Problema 5

2520 es el número positivo más pequeño que se puede dividir por cada uno de los números del 1 al 10 sin ningún residuo.

¿Cuál es el número positivo más pequeño que es divisible por todos los números del 1 al 20?


```python
bandera=0
numero=0
while bandera==0:
    numero=numero+19
    contador=0
    for j in range(1,21):
        if numero%j==0:
            contador=contador+1
        else:
            break
    if contador>=20:
        bandera=1
    
print(numero)
```

    232792560


# Problema 6

La suma de los cuadrados de los primeros diez números naturales es:

<p style="text-align: center;">$1^2 + 2^2 + ... + 10^2 = 385$</p>

El cuadrado de la suma de los primeros diez números naturales es:

<p style="text-align: center;">$(1 + 2 + ... + 10)^2 = 55^2 = 3025$</p>


Por tanto, la diferencia entre la suma de los cuadrados de los primeros diez números naturales y el cuadrado de la suma es:
$3025 - 385 = 2640$.


Calcula la diferencia entre la suma de los cuadrados de los primeros cien números naturales y el cuadrado de la suma.


```python
sumaCuadrados=0
suma=0
for i in range(101):
    sumaCuadrados=sumaCuadrados+i**2
    suma=suma+i
diferencia=suma**2-sumaCuadrados
print(diferencia)
```

    25164150


# Problema 7

Al enumerar los primeros seis números primos: 2, 3, 5, 7, 11 y 13, podemos ver que el sexto primo es 13.

¿Cuál es el 1001° número primo?


```python
numero=10001
i=2
primoAct=1
while primoAct<=numero:
    contador=0
    j=2
    while j<i:
        if i%j!=0:
            contador=contador+1
        else:
            break
        j=j+1
    if contador==i-2:
        primo=i
        primoAct=primoAct+1
    i=i+1
     
print(primo)
```

    104743


# Problema 8

Los cuatro dígitos adyacentes en el número de 1000 dígitos que tienen el mayor producto son 9 × 9 × 8 × 9 = 5832.

<p style="text-align: center;">73167176531330624919225119674426574742355349194934<br>
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
71636269561882670428252483600823257530420752963450</p>

Encuentra los trece dígitos adyacentes en el número de 1000 dígitos que tienen el mayor producto. ¿Cuál es el valor de este producto?


```python
digitos="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

valorMayor=0
j=0
digitosAd=[]
while j+13<digitos.__len__():
    mult=1
    for i in range(j,j+13):
        mult=mult*int(digitos[i])
    if mult>valorMayor:
        valorMayor=mult
        digitosAd.clear()
        for i in range(j,j+13):
            digitosAd.append(digitos[i])
    j=j+1
print("Producto: ", valorMayor)
print("Numeros adyacentes: ",digitosAd)
```

    Producto:  23514624000
    Numeros adyacentes:  ['5', '5', '7', '6', '6', '8', '9', '6', '6', '4', '8', '9', '5']


# Problema 9

Un triplete pitagórico es un conjunto de tres números naturales, a <b <c, para los cuales:
<p style="text-align: center;">$a^2 + b^2 = c^2$</p>
Por ejemplo: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$


Existe únicamente un triplete pitagórico para el cual $a + b + c = 1000$.<br>
Encuentre el producto $abc$.


```python
lim=1000
i=1
bandera=0
while i<lim:
    a=i
    j=i+1
    while j<(lim-a):
        b=j
        c=(a**2+b**2)**(1/2)
        if c-int(c)==0 and a+b+c==1000:
            bandera=1
            break
        j=j+1
    if bandera==1:
        break
    i=i+1
print("a = ",a,", b = ",b,", c = ",c)
print("abc = ",a*b*c)
```

    a =  200 , b =  375 , c =  425.0
    abc =  31875000.0


# Problema 10


La suma de los números primos por debajo de 10 es 2 + 3 + 5 + 7 = 17.

Encuentra la suma de todos los números primos por debajo de dos millones.


```python
from datetime import datetime 
start_time = datetime.now() 
lim=2000001
numeros=[]
for x in range(3,lim,2):
    if x%3!=0 :
        numeros.append(x)
        if  x%5==0 or x%7==0 or x%11==0 or x%13==0 or x%17==0 or x%19==0:
            numeros.remove(x)

suma=77
while numeros[0]<= lim ** (0.5):
    suma+=numeros[0]
    multiplos=[]
    k=numeros[0]
    multiplo=numeros[0]
    aux=numeros[0]
    while multiplo<lim:
        if multiplo in numeros:
            numeros.remove(multiplo)
        multiplo=aux*k
        k=k+1
for x in range (len(numeros)):
    suma+=numeros[x]
print("Suma de los números primos inferiores a 2000000: ",suma)
print('Tiempo de cálculo (hh:mm:ss.ms) {}'.format(datetime.now() - start_time))
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-13-021ac686c92b> in <module>()
          7         numeros.append(x)
          8         if  x%5==0 or x%7==0 or x%11==0 or x%13==0 or x%17==0 or x%19==0:
    ----> 9             numeros.remove(x)
         10 
         11 suma=77


    KeyboardInterrupt: 

