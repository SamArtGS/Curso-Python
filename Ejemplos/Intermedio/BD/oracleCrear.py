import cx_Oracle

## DATOS DE CONEXIÓN
dsn_tns = cx_Oracle.makedsn('python.c7rbflvluzyk.us-east-2.rds.amazonaws.com', '1521', 'ORCL')
BasedeDatos = cx_Oracle.connect(user='PYTHON_INTERMEDIO', password='python', dsn=dsn_tns)

## CREACIÓN DE LA TABLA O ENTIDAD

# Para poder ejecutar un comando SQL dentro de Python usaremos: el objeto BaseDeDatos, tiene un objeto cursor
## Y este a su vez tiene un método llamado Execute que ejecuta un SQL en forma de cadena String.

BasedeDatos.cursor().execute("""CREATE TABLE PROFESOR(
                                ID number (10,0) NOT NULL,
                                NOMBRE VARCHAR2(30),
                                APELLIDO_PAT VARCHAR2(30),
                                APELLIDO_MAT VARCHAR2(30),
                                EDAD NUMBER(3,0),
                                DOMICILIO VARCHAR2(100),
                                SALARIO NUMBER(10,2))
                                """ )


## PARA QUE GUARDE LOS CAMBIOS AUTOMÁTICAMENTE

BasedeDatos.autocommit = True 


# INSERCIÓN DE DATOS

## Imaginemos que creamos objetos de tipo profesor con estos atributos

class Profesor:
    def __init__(self,id,nombre,apellido_pat,apellido_mat,edad,domicilio,salario):
        self.id = id
        self.nombre = nombre
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.edad = edad
        self.domicilio = domicilio
        self.salario = salario

## creamos a missConchi, a mrRafa, a missDulce y a missLoli, todos objetos de tipo Profesor

missConchi = Profesor(1,'Ana Concepción','Castillo','Corona',33,'Av.Robles, Tabasco, Mex',13000)
mrRafa     = Profesor(2,'Rafael','García','Rueda',44,'Av. Maya, Tabasco, Mex',12000)
missDulce  = Profesor(3,'Dulce Mónica','Escalante','Garrido',30,'Av. Olmeca, Campeche, Mex',12000)
missLoli   = Profesor(4,'Maria Dolores','Taracena','Blé',31,'Av. Palenque, Chiapas, Mex',15000)

# Hacemos una lista de profesores

listaDeProfesores = [missConchi,mrRafa,missDulce,missLoli]

sqls = [] # Y una lista para poder poner nuestras cadenas de texto SQL

#Ahora hacemos los strings SQL para ver qué tal quedan

## Imprimimos como quedan los strings SQL
for profe in listaDeProfesores:
    comandosql = 'INSERT INTO PROFESOR VALUES ('+str(profe.id)+',\''+profe.nombre+'\',\''+profe.apellido_pat+'\',\''+profe.apellido_mat+'\','+str(profe.edad)+',\''+profe.domicilio+'\','+str(profe.salario)+')'
    print(comandosql)
    sqls.append(comandosql)

## Y los ejecutamos
for comandos in sqls:
    BasedeDatos.cursor().execute(comandos)