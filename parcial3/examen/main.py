from clientes import *
from conexionbd import *


def menu():
    conexion=crear_conexion()
    if conexion:
        while True:
            print("\nMENU CLIENTES")
            print("1.INSERTAR REGISTRO DE EMPLEADO")
            print("2.CONSULTAR EMPLEADOS")
            print("3.ACTUALIZAR EMPLEADO")
            print("4.ELIMINAR EMPLEADO")
            print("5.SALIR")
            opcion = input("elije una opcion: ")



            if opcion=='1':
                nombre=input("nombre:")
                puesto=input("puesto:")
                salario=input("salario:")
                empleado.crear_empleado(conexion,nombre,puesto,salario)
            elif opcion=='2':
                empleado.leer_empleados(conexion)
            elif opcion=='3':
                id=int(input("ID del empleado a actualizar: "))
                nombre=input("Nuevo nombre: ")
                puesto=input("Nuevo puesto: ")
                salario=input("Nuevo salario: ")
                empleado.actualizar_empleado(conexion,id,nombre,puesto,salario)
            elif opcion=='4':
                id=int(input("ID del empleado a eliminar: ")) 
                empleado.eliminar_empleado(conexion,id)
            elif opcion=='5':
                cerrar_conexion(conexion)
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__=="__main__":
        menu()
