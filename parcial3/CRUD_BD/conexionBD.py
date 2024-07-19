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
    print(f"ocurrio un error porfavor vuelva a intentar")
