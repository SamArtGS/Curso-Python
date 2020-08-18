import mysql.connector

#Creamos el conector a la BD
mydb = mysql.connector.connect(
  host="pythoninter.c7rbflvluzyk.us-east-2.rds.amazonaws.com",
  user="admin",
  password="proteco123"
)

## Creamos un cursor por la conexión creada--------------------------------------------
cursor1 = mydb.cursor()
cursor1.execute("CREATE DATABASE asistente") ## FAVOR DE CREAR UNA BASE DE DATOS LLAMADA asistente_<numero_asistente>

cursor1.execute("use asistente") ## FAVOR DE INGRESAR asistente_<su_numero> ------------

        
## Creamos otro cursor y creamos una entidad en la base de datos

cursor2 = mydb.cursor()
cursor2.execute("""CREATE TABLE PROFESOR (ID INT AUTO_INCREMENT PRIMARY KEY, 
                                          NOMBRE VARCHAR(40),
                                          APELLIDO_PAT VARCHAR(40),
                                          APELLIDO_MAT VARCHAR(40),
                                          EDAD INT,
                                          DOMICILIO VARCHAR(255),
                                          SALARIO DECIMAL(5,2))
                                          """)

print("\nSe ha creado la entidad de profesor")

######## --------- Creamos unos objetos profesores.


class Profesor:
    def __init__(self,id,nombre,apellido_pat,apellido_mat,edad,domicilio,salario):
        self.id = id
        self.nombre = nombre
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.edad = edad
        self.domicilio = domicilio
        self.salario = salario   

missConchi = Profesor(1,'Ana Concepción','Castillo','Corona',33,'Av.Robles, Tabasco, Mex',13000)
mrRafa     = Profesor(2,'Rafael','García','Rueda',44,'Av. Maya, Tabasco, Mex',12000)
missDulce  = Profesor(3,'Dulce Mónica','Escalante','Garrido',30,'Av. Olmeca, Campeche, Mex',12000)
missLoli   = Profesor(4,'Maria Dolores','Taracena','Blé',31,'Av. Palenque, Chiapas, Mex',15000)

#Hacemos una lista de objetos profesor
listaDeProfesores = [missConchi,mrRafa,missDulce,missLoli]

print("Se han creado objetos de la clase Profesor y los hemos puesto en una lista ")
## Hacemos la instrucción SQL

sql = "INSERT INTO PROFESOR (NOMBRE, APELLIDO_PAT,APELLIDO_MAT,EDAD,DOMICILIO,SALARIO) VALUES (%s,%s,%s,%s,%s,%s)"

# Y mandamos a través del SQL y de la lista de profesores los datos a la base de datos en MySQL

for profe in listaDeProfesores:
    valores = (profe.nombre, profe.apellido_pat,profe.apellido_mat,profe.edad,profe.domicilio,profe.salario)
    cursor2.execute(sql, valores)

print("Se han insertado a los profesores en la base")

mydb.commit() ## Confirmamos los cambios

## Por buenas prácticas, cerramos todas las conexiones, si ambas me marcan cerradas ya!

if cursor1.close() and cursor2.close():
    print("Se han cerrado correctamente las conexiones :)")
    print("Algoritmo finalizado!")