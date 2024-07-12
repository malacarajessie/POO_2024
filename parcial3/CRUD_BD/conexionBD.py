import mysql.connector

#conexion con la BD de mysql
try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
    )
except Exception as e:
    print(f"error: {e}")
    print(f"tipo de eroor: {type(e).__name__}")
    print(f"ocurrio un error porfavor vuelva a intentar")
#verificar conexion
if conexion.is_connected():
    print(f"se creo la conexion correctamente")
else:
    print(f"no fue posible conectar con la BD, verificar de nuevo")