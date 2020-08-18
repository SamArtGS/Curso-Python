import re

#Compilamos nuestra expresión regular
miExpresionRegular3 = re.compile(r'\d+\.\d+\.\d+\.\d+ - - \[1[3-4]\/Dec\/\d+:\d+:\d+:\d+ \+\d+\] "\w+ [^ ]+ [^ ]+ 200 .+')

#Al abrir el archivo apache.log como 'archivo' has esto:

with open('apache.txt') as archivo:
    contenido = archivo.read() # Lee su contenido
    print("Conexiones Exitosas (200) el 13 y 14 de Diciembre: ",len(miExpresionRegular3.findall(contenido))) #Imprime el tamaño del arreglo de todas las coincidencias
    print("\nEjemplos: \n") 
    print(miExpresionRegular3.findall(contenido)[0]+"\n")
    print(miExpresionRegular3.findall(contenido)[1])