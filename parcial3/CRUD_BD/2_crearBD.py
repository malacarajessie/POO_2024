import mysql.connector

#conexion con la BD de mysql
try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
    )

    #crear un objeto nuevo de tipo cursor para ejecitar SQL
    micursor=conexion.cursor()

    sql="crear database bd_python"

    micursor.execute(sql)
except Exception as e:
    print(f"error: {e}")
    print(f"tipo de eroor: {type(e).__name__}")
    print(f"ocurrio un error porfavor vuelva a intentar")
else:
   print(f"se creo la base de datos exitosamente")
   micursor.execute("show databases")
   for x in micursor:
       print(x)