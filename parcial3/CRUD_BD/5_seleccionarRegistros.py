from conexionBD import *

try:
   micursor=conexion.cursor()
   sql="select * from clientes"

   micursor.execute(sql)
   
   resultado=micursor.fetchall()

   for fila in resultado:
      print(f"id:{fila[0]} | nombre: {fila[1]} | direccion:{fila[2]} | telefono:{fila[3]}")

except:
   print(f"ocurrio un error porfavor vuelva a intentar")
else:
   print("registro insertado exitosamente")