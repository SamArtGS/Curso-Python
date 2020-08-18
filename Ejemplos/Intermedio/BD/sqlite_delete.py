import sqlite3

Base = sqlite3.connect("Tiendas.db")

cursor = Base.cursor()

cursor.execute("DELETE FROM sucursales WHERE id=4")

try:
	cursor.execute("SELECT * FROM sucursales")
	resultados = cursor.fetchall()
	print("Resultados al eliminar")
	print(resultados)
except:
	print("Hubo un error al conectar con la base")