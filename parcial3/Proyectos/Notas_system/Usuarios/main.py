from Usuario import Usuarios
from Notas.Nota import Nota
import getpass
from Funciones import *

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre = input("\t ¿Cuál es tu nombre?: ")
            apellidos = input("\t ¿Cuáles son tus apellidos?: ")
            email = input("\t Ingresa tu email: ")
            password = getpass.getpass("\t Ingresa tu contraseña: ")
            # Agregar código
            obj_usuario = Usuarios.Usuario(nombre, apellidos, email, password)
            resultado = obj_usuario.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registró correctamente, con el email: {email}")
            else:
                print(f"\n\t Por favor ententelo de nuevo, no fue posible insertar el registro")
            esperarTecla()
        elif opcion == '2' or opcion == "LOGIN":
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email = input("\t Ingresa tu E-mail: ")
            password = getpass.getpass("\t Ingresa tu Contraseña: ")
            # Agregar código
            registro = Usuarios.usuario.iniciar_sesion(email, password)
            if len(registro) > 0:
                menu_notas(registro[0], registro[1], registro[2])
            else:
                print(f"\n\t Email y/o contraseña incorrectos.") 
                esperarTecla()  
        elif opcion == '3' or opcion == "Salir":
            print("\n\t.. ¡Gracias Bye! ...")
            break
            # exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_notas(usuario_id, nombre, apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Menu Notas ::. 
                  1.- Crear 
                  2.- Mostrar
                  3.- Cambiar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ").upper()

        if opcion == '1' or opcion == "CREAR":
            borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo = input("\tTítulo: ")
            descripcion = input("\tDescripción: ")
            # Agregar código
        elif opcion == '2' or opcion == "MOSTRAR":
            borrarPantalla()
            # Agregar código    
        elif opcion == '3' or opcion == "CAMBIAR":
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar una Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            # Agregar código
        elif opcion == '4' or opcion == "ELIMINAR":
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar una Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            # Agregar código
        elif opcion == '5' or opcion == "SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()
