import mysql.connector

#Creamos el conector a la BD
conexion = mysql.connector.connect(
  host="pythoninter.c7rbflvluzyk.us-east-2.rds.amazonaws.com",
  user="admin",
  password="proteco123"
)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PROFESOR")

consulta = cursor.fetchall()

for fila in consulta:
    print(fila)
    
otroCursor.close()