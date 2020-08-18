import cx_Oracle

## DATOS DE CONEXIÓN
dsn_tns = cx_Oracle.makedsn('python.c7rbflvluzyk.us-east-2.rds.amazonaws.com', '1521', 'ORCL')
BasedeDatos = cx_Oracle.connect(user='PYTHON_INTERMEDIO', password='python', dsn=dsn_tns)

## Creamos un cursor
cursor = BasedeDatos.cursor() ## El curso se utiliza para recorrer cada fila
cursor.execute('SELECT * FROM PROFESOR') # Ejecuta la instrucción SQL

for fila in cursor: ## Para cada fila que encuentre en la tabla(s)
    print(fila)  ## Imprimimos esa fila

BasedeDatos.cursor().close()