import sqlite3
from tkinter import *
from tkinter import messagebox as tkMessageBox

Base = sqlite3.connect("Contacts.db")

cursor = conexion.cursor()
#Crear la tabla con cada uno de los atributos
try:
	cursor.execute("""CREATE TABLE sucursales (id INTEGER PRIMARY KEY , delegacion TEXT, telefono INTEGER, gerente TEXT)""")
	cursor.execute("""INSERT INTO sucursales VALUES(1,"Coyoacán",556442312,"Juan Lopez")""")
	cursor.execute("""INSERT INTO sucursales VALUES(2,"Coyoacán",524343323,"Jorge Cardenas")""")
	cursor.execute("""INSERT INTO sucursales VALUES(3,"Coyoacán",435423423,"David Alejandro")""")
	cursor.execute("""INSERT INTO sucursales VALUES(4,"Coyoacán",643523234,"Daniel Ernesto")""")
	cursor.execute("SELECT * FROM sucursales")
	resultados = cursor.fetchall()
	print(resultados)

	cursor.execute("""UPDATE sucursales SET gerente = "Pedro Díaz" WHERE id = 3""")
	conexion.commit()

	cursor.execute("""DELETE FROM sucursal WHERE id=4""")
	resultados = cursor.fetchall()
	resultados(resultados)
except:
	cursor.execute('''DROP TABLE sucursales''')