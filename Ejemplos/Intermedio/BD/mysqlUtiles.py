import mysql.connector

#Creamos el conector a la BD
mydb = mysql.connector.connect(
  host="pythoninter.c7rbflvluzyk.us-east-2.rds.amazonaws.com",
  user="admin",
  password="proteco123"
)

## Creamos un cursor dada la conexión
cursor = mydb.cursor()

## Algunas instrucciones últiles





cursor.close() ## Por buenas prácticas, cerrar las conexiones