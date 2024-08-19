from conexion import *
from autos import *
from clientes import *
from transacciones import *
from funciones import *
import getpass
from usuarios import usuario

def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")

def validar_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar un número decimal válido. Intenta de nuevo.")
            esperarTecla()

def menuAutos():
    ciclo1 = True
    while ciclo1:
        try:
            borrarPantalla()
            print("\n.:: BIENVENIDO AL MENU DE AUTOS ::.")
            print("""SELECCIONA UNA OPCIÓN:
            1.- Añadir auto
            2.- Consultar información de un auto
            3.- Actualizar información
            4.- Eliminar auto
            5.- Salir""")
            
            opcion = validar_entero("Selecciona una opción numérica: ")
            
            if 1 <= opcion <= 5:
                if opcion == 1:
                    print("AÑADIR...")
                    matricula = input("Matricula del auto: ").upper()
                    marca = input("Marca del auto: ")
                    modelo = input("Modelo del auto: ")
                    color = input("Color del auto: ")
                    nif = validar_entero("NIF del cliente:")
                    if Autos.insertar(matricula, marca, modelo, color, nif):
                        print("Auto añadido con éxito.")
                    else:
                        print("Error al añadir el auto.")
                elif opcion == 2:
                    print("CONSULTA...")
                    Autos.consultar()
                    esperarTecla()
                elif opcion == 3:
                    print("ACTUALIZAR DATOS...")
                    matricula = input("Matricula del auto a actualizar: ").upper()
                    Autos.actualizar(matricula)
                elif opcion == 4:
                    print("ELIMINAR...")
                    matricula = input("Matricula del auto a eliminar: ").upper()
                    if Autos.eliminar(matricula):
                        print("Auto eliminado con éxito.")
                    else:
                        print("Error al eliminar el auto.")
                elif opcion == 5:
                    print("Saliendo...")
                    ciclo1 = False  
            else:
                print("Opción no válida. Intenta de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

def menuClientes():
    ciclo2 = True
    while ciclo2:
        try:
            borrarPantalla()

            print("\n.: BIENVENIDO AL MENU DE CLIENTES :.")
            print("""
                  1.- Registrar un cliente
                  2.- Consultar información de un cliente
                  3.- Actualizar información del cliente
                  4.- Dar de baja un cliente
                  5.- Salir""")
            
            opcion = validar_entero("Selecciona una opción numérica: ")

            if 1 <= opcion <= 5:
                if opcion == 1:
                    print("REGISTRAR...")
                    nif = validar_entero("Inserta NIF: ")
                    nombre = input("Nombre del cliente: ")
                    direccion = input("Dirección del cliente: ")
                    ciudad = input("Ciudad del cliente: ")
                    tel = validar_entero("Número de teléfono del cliente: ")
                    if Cliente.insertar(nif, nombre, direccion, ciudad, tel):
                        print("Cliente registrado con éxito.")
                    else:
                        print("Error al registrar el cliente.")
                elif opcion == 2:
                    print("CONSULTAR...")
                    Cliente.consultar() 
                    esperarTecla()
                elif opcion == 3:
                    print("ACTUALIZAR...")
                    nif = validar_entero("Inserta NIF del cliente a actualizar: ")
                    Cliente.actualizar(nif)
                elif opcion == 4:
                    print("ELIMINAR...")
                    nif = validar_entero("Inserta NIF del cliente: ")
                    if Cliente.eliminar(nif):
                        print("Cliente eliminado con éxito.")
                    else:
                        print("Error al eliminar el cliente.")
                elif opcion == 5:
                    print("Saliendo...")
                    ciclo2 = False
            else:
                print("Opción no válida. Intenta de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

def menuVentas():
    ciclo3 = True
    while ciclo3:
        try:
            borrarPantalla()
            print("\n.:: BIENVENIDO AL MENU DE VENTAS ::.")
            print("""SELECCIONA UNA OPCIÓN:
            1.- Hacer una venta
            2.- Consultar ventas
            3.- Actualizar información de una venta
            4.- Eliminar venta
            5.- Salir""")
            
            opcion = validar_entero("Selecciona una opción numérica: ")
            
            if 1 <= opcion <= 5:
                if opcion == 1:
                    print("AÑADIR VENTA...")
                    id_venta = validar_entero("ID de la venta: ")
                    matricula = input("Matricula del auto vendido: ").upper()
                    fecha = input("Fecha de venta (YYYY-MM-DD): ")
                    precio = validar_float("Precio de venta: ")
                    nif_cliente = validar_entero("NIF del cliente: ")
                    if Transacciones.insertar_venta(id_venta, matricula, fecha, precio, nif_cliente):
                        print("Venta añadida con éxito.")  
                    else:
                        print("Error al añadir la venta.")
                    esperarTecla()
                elif opcion == 2:
                    print("CONSULTAR VENTAS...")
                    Transacciones.consultar_ventas()
                    esperarTecla()
                elif opcion == 3:
                    print("ACTUALIZAR VENTA...")
                    id_venta = validar_entero("ID de la venta a actualizar: ")
                    Transacciones.actualizar_venta(id_venta)
                    esperarTecla()
                elif opcion == 4:
                    print("ELIMINAR VENTA...")
                    id_venta = validar_entero("ID de la venta a eliminar: ")
                    if Transacciones.eliminar_venta(id_venta):
                        print("Venta eliminada con éxito.")
                    else:
                        print("Error al eliminar la venta.")
                    esperarTecla()
                elif opcion == 5:
                    print("Saliendo...")
                    ciclo1 = False
                    esperarTecla()
            else:
                print("Opción no válida. Intenta de nuevo.")
                esperarTecla()
        except Exception as e:
            print(f"Error: {e}")
            esperarTecla()

def menuCompras():
    ciclo4 = True
    while ciclo4:
        try:
            borrarPantalla()
            print("\n.: BIENVENIDO AL MENU DE COMPRAS :.")
            print("""
                  1.- Hacer una compra
                  2.- Consultar compras
                  3.- Actualizar información de una compra
                  4.- Eliminar compra
                  5.- Salir""")
            
            opcion = validar_entero("Selecciona una opción numérica: ")

            if 1 <= opcion <= 5:
                if opcion == 1:
                    print("AÑADIR COMPRA...")
                    id_compra = validar_entero("ID de la compra: ")
                    matricula = input("Matricula del auto comprado: ").upper()
                    fecha = input("Fecha de compra (YYYY-MM-DD): ")
                    precio = validar_float("Precio de compra: ")
                    nif_cliente = validar_entero("NIF del cliente: ")
                    if Transacciones.insertar_compra(id_compra, matricula, fecha, precio, nif_cliente):
                        print("Compra añadida con éxito.")
                    else:
                        print("Error al añadir la compra.")
                    esperarTecla()
                elif opcion == 2:
                    print("CONSULTAR COMPRAS...")
                    Transacciones.consultar_compras()
                    esperarTecla()
                elif opcion == 3:
                    print("ACTUALIZAR COMPRA...")
                    id_compra = validar_entero("ID de la compra a actualizar: ")
                    Transacciones.actualizar_compra(id_compra)
                    esperarTecla()
                elif opcion == 4:
                    print("ELIMINAR COMPRA...")
                    id_compra = validar_entero("ID de la compra a eliminar: ")
                    if Transacciones.eliminar_compra(id_compra):
                        print("Compra eliminada con éxito.")
                    else:
                        print("Error al eliminar la compra.")
                    esperarTecla()
                elif opcion == 5:
                    print("Saliendo...")
                    ciclo2 = False
                    esperarTecla()
            else:
                print("Opción no válida. Intenta de nuevo.")
                esperarTecla()
        except Exception as e:
            print(f"Error: {e}")
            esperarTecla()



def menu_login():
    while True:
        try:
            borrarPantalla()
            print("""
            ..:: INICIO DE SESIÓN ::..
            1.- Iniciar sesión
            2.- Registrarse
            3.- Salir""")
            
            opcion = validar_entero("Selecciona una opción numérica: ")

            if 1 <= opcion <= 3:
                if opcion == 1:
                    borrarPantalla()
                    print("\n..:: Inicio de Sesión ::..")
                    email = input("\t Ingresa tu E-mail: ")
                    password = getpass.getpass("\t Ingresa tu Contraseña: ")
                    registro = usuario.Usuario.iniciar_sesion(email, password)
                    if registro:
                        menu_principal()
                    else:
                        menu_principal()

                elif opcion == 2:
                    borrarPantalla()
                    print("\n..:: Registro en el Sistema ::..")
                    nombre = input("\t ¿Cuál es tu nombre?: ")
                    apellidos = input("\t ¿Cuáles son tus apellidos?: ")
                    email = input("\t Ingresa tu email: ")
                    password = getpass.getpass("\t Ingresa tu contraseña: ")
                    obj_usuario = usuario.Usuario(nombre, apellidos, email, password)
                    resultado = obj_usuario.registrar()
                    if resultado:
                        print(f"\n\t {nombre} {apellidos}, se registró correctamente con el email: {email}")
                    else:
                        print(f"\n\t ** No se pudo registrar el usuario. Inténtalo de nuevo. **")
                    esperarTecla()
                elif opcion == 3:
                    print("\n\t.. ¡Gracias, Bye! ...")
                    break
            else:
                print("\n\t Opción no válida. Intenta de nuevo.")
                esperarTecla()
        except Exception as e:
            print(f"Error: {e}")

def menu_principal():
    while True:
        
        try:
            borrarPantalla()
            print("Bienvenido Edgar Burciaga")
            print("""
            .:BIENVENIDO:.
            1.- MENU CLIENTES
            2.- MENU AUTOS
            3.- MENU VENTAS
            4.- MENU COMPRAS
            5.- SALIR""")
            eleccion = validar_entero("Selecciona una opción numérica: ")

            if 1 <= eleccion <= 5:
                if eleccion == 1:
                    menuClientes()
                elif eleccion == 2:
                    menuAutos()
                elif eleccion == 3:
                    menuVentas()
                elif eleccion == 4:
                    menuCompras()
                elif eleccion == 5:
                    print("Saliendo del sistema. ¡Hasta luego!")
                    break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

def borrarPantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def esperarTecla():
    input("Presiona Enter para continuar...")

def main():
    menu_login()

if __name__ == "__main__":
    main()