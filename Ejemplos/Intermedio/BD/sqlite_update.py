import sqlite3

Base = sqlite3.connect("Tiendas.db")

cursor = Base.cursor()

cursor.execute("UPDATE sucursales SET gerente = 'Pedro Díaz' WHERE id = 3")
cursor.execute("UPDATE sucursales SET gerente = 'Francisco Espejel' WHERE telefono = 524343323")

try:
	cursor.execute("SELECT * FROM sucursales")
	resultados = cursor.fetchall()
	print("Resultados: ")
	print(resultados)
except:
	print("Hubo un error al conectar con la base")