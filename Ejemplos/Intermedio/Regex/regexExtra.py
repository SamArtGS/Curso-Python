import re

#Compilamos nuestra expresión regular
miExpresionRegular = re.compile(r'\d+\.\d+\.\d+\.\d+ - - \[1[2-5]\/Dec\/\d+:.{17}POST \/administrator\/.+')

#Al abrir el archivo apache.log como 'archivo' has esto:

with open('apache.log') as archivo:
    contenido = archivo.read()
    print("Número de conexiones del 12-15 Dic POST por arministrador: ",len(miExpresionRegular.findall(contenido)))
    print("\nEjemplos: \n")
    print(miExpresionRegular.findall(contenido)[0]+"\n")
    print(miExpresionRegular.findall(contenido)[1])

