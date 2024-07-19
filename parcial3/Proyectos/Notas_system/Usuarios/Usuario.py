from ConexionBD import *
import hashlib
import datetime

class Usuarios:
    def __init__(self,nombre,apellido,email,password):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.contrasena=self.hash_password(password)

    def hash_password(self,contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()
    
    def registrar(self):
        try:
            fecha=datetime.datetime.now()
            cursor.excute(
            "insert into usuarios values(null,%s,%s,%s,%s,%s)",
            (self.nombre,self.apellido,self.email,self.contrasena,fecha)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def iniciar_sesion(email,contrasena):
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        try:
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email,contrasena)
            )
            Usuarios=cursor.fetchone()
            if Usuarios:
                return Usuarios
            else:
                return []
        except:
            return[]