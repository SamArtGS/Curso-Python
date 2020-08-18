import sqlite3

Base = sqlite3.connect("Tiendas.db")

cursor = Base.cursor()

#Crear la tabla con cada uno de los atributos

try:
	cursor.execute("CREATE TABLE sucursales (id INTEGER PRIMARY KEY , delegacion TEXT, telefono INTEGER, gerente TEXT)")
	cursor.execute("INSERT INTO sucursales VALUES(1,'Coyoacan',556442312,'Juan Lopez')")
	cursor.execute("INSERT INTO sucursales VALUES(2,'Coyoacan',524343323,'Jorge Cardenas')")
	cursor.execute("INSERT INTO sucursales VALUES(3,'Coyoacan',435423423,'David Alejandro')")
	cursor.execute("INSERT INTO sucursales VALUES(4,'Coyoacan',643523234,'Daniel Ernesto')")

	cursor.execute("SELECT * FROM sucursales")
	resultados = cursor.fetchall()
	print(resultados)
	Base.commit()
	Base.close()
except:
	print("Había una BD existente, se elimina")
	cursor.execute('DROP TABLE sucursales')