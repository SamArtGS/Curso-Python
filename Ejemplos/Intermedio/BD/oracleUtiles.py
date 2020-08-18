import cx_Oracle

## DATOS DE CONEXIÓN
dsn_tns = cx_Oracle.makedsn('python.c7rbflvluzyk.us-east-2.rds.amazonaws.com', '1521', 'ORCL')
BasedeDatos = cx_Oracle.connect(user='PYTHON_INTERMEDIO', password='python', dsn=dsn_tns)

cursor = BasedeDatos.cursor()

cursor.execute('DROP TABLE <nombre_de_su_tabla>')

cursor.close() ## Por buenas prácticas, cerrar las conexiones