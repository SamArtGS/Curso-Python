import mysql.connector

#Creamos el conector a la BD
mydb = mysql.connector.connect(
  host="pythoninter.c7rbflvluzyk.us-east-2.rds.amazonaws.com",
  user="admin",
  password="proteco123"
)
print("Nos hemos conectado a la base de datos remota")

cursor1 = mydb.cursor()

cursor1.execute("CREATE DATABASE asistente") ##Creamos una BD

cursor1.execute("use asistente") ## USAMOS ESA BD

## Creamos otro cursor

cursor2 = mydb.cursor()
cursor2.execute("CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), direccion VARCHAR(255))")

print("\nHemos creado una entidad en nuestra base\n")

## Primera instrucción insert SQL, solo para agregar 1 valor

sql = "INSERT INTO clientes (nombre, direccion) VALUES (%s, %s)" 

valores = ("Alice", "Av.Siempre Viva 21 CDMX")

cursor2.execute(sql, valores) ## Ejecuta 1 vez

## Segunda instrucción INSERT SQL
sql2 = "INSERT INTO clientes (nombre, direccion) VALUES (%s, %s)"
 
## Varios Valores de Clientes en tuplas
valoresVarios = [
  ('Antonio Balam', 'Av. Kukulcán 31'),
  ('Ana Petch', 'Av. 4 Ciénegas 33'),
  ('Samuel Garrido', 'Av. Tulum Nacajuca 21'),
  ('Alicia Carballido', 'Av. Xalapa 52'),
  ('Mario Álvarez', 'Av. Palenque 34'),
  ('Beatriz Pinzón', 'Av. Palacios 44'),
  ('Richard Stallman', 'Av. Bonampak 100'),
  ('César Govantes', 'Av. Mayas 200'),
  ('Alberto Templos', 'Av. Olmecas 55'),
  ('Tadeo Blé', 'Av. Mérida 12'),
  ('Javier Salinas', 'Av. San Francisco Campeche 120'),
  ('Carlos Santander', 'Av. Valladolid 77'),
  ('Mateo Espejel', 'Av. Chichen Itzá 39')
]

cursor2.executemany(sql2, valoresVarios) ## Ejecuto varias veces el SQL

mydb.commit() ## Confirmamos los cambios

print("\nHemos insertado todos los datos :)") ## Para dejar un espacio

print(cursor2.rowcount, "filas fueron insertadas.") ## Imprimimos la cantidad de filas insertadas

if cursor1.close() and cursor2.close():
  print("Se han cerrado correctamente las conexiones :)")
  print("Algoritmo finalizado!")
