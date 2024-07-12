from conexionBD import *

try:
   micursor=conexion.cursor()
   sql="INSERT INTO clientes (id, nombre, direccion, tel) Values (NULL, 'juan polainas',' col.del valle', 6181234566) "

   micursor.execute(sql)
   #es necesario ejecutar el commit para que finalice el sql con exito
   conexion.commit()
except:
   print(f"ocurrio un error porfavor vuelva a intentar")
else:
   print("registro insertado exitosamente")
