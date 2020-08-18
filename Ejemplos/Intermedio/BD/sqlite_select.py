import sqlite3

Base = sqlite3.connect("Tiendas.db")

cursor = Base.cursor()

try:
	cursor.execute("SELECT * FROM sucursales")
	resultados = cursor.fetchall()
	print(resultados)
except:
	print("Hubo un error al conectar con la base")