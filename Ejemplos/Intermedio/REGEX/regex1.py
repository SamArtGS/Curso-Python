import re

p = re.compile(r'\d+')

x = p.findall('11 es un número y 12 también, después tenemos al 13, 14, 15 y sin olvidar al 20')

print(x)

if x:
    print("Hay al menos una coincidencia!")
else:
    print("No hay coincidencias")