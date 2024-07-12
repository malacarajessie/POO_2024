from conexionBD import *

try:
   micursor=conexion.cursor()
   sql="update clientes set direccion='col. del maestro' where id=2"

   micursor.execute(sql)
   #es necesario ejecutar el commit para que finalice el sql con exito
   conexion.commit()
except:
   print(f"ocurrio un error porfavor vuelva a intentar")
else:
   print("registro actualizado exitosamente")