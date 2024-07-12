import conexionBD

try:
   micursor=conexionBD.conexion.cursor()
   sql="create table clientes(id int primary key auto_increment,nombre varchar(60),direccio9n varchar(120),tel varchar(10))"

   micursor.execute(sql)
except:
   print(f"ocurrio un error porfavor vuelva a intentar")
else:
   print("se creo la tabla exitosamente")