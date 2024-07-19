import mysql.connector

try:
 #Conexion con la BD de Mysql
 conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_python"
)
 #Se crear un objeto de tipo cursor con un parametrro que permita reutilizar el mismo objeto
 cursor=conexion.cursor(buffered=True)
except Exception as e:
 print(f"Error: {e}")
 print(f"Tipo de error: {type(e).__name__}")
 print(f"Ocurrio un error por favor vuelva a intentar mas tarde")

else:

#Verificar si la conexion es correcta
 if conexion.is_connected():
    print(f"Se creo la conexion exitosamente")
 else:
    print(f"No fue posible conectar con la BD")
