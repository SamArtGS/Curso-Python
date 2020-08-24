import re

expresion = re.compile(r'\d+')

busqueda = expresion.findall('11 es un número, pero también 12, y 13 sin olvidar al 14 ni al 15 y 20')

print(busqueda)