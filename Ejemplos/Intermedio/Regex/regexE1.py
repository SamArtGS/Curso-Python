import re

#Compilamos nuestra expresión regular
miExpresionRegular = re.compile(r'\d+\.\d+\.\d+\.\d+ - - \[1[2-5]\/Dec\/\d+:.{17}POST \/administrator\/.+')

#Al abrir el archivo apache.log como 'archivo' has esto:

with open('apache.txt') as archivo:
    contenido = archivo.read()
    listaQueMeTrae = miExpresionRegular.findall(contenido)
    print("Número de conexiones del 12-15 Dic POST por arministrador: ",len(listaQueMeTrae))
    print("\nEjemplos: \n")
    print(listaQueMeTrae[0])
    print(listaQueMeTrae[1])
    print(listaQueMeTrae[2])


