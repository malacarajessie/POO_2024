from POO import *
from conexion import *

def menu():
    conexion=crear_conexion()
    if conexion:
        while True:
            print("\n--- Menú de Opciones ---")
            print("1. Crear empleado")
            print("2. Leer empleados")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion=='1':
                nombre=input("Nombre: ")
                puesto=input("Puesto: ")
                salario=input("Salario: ")
                Empleado.crear_empleado(conexion, nombre, puesto, salario)
            elif opcion=='2':
                Empleado.leer_empleados(conexion)
            elif opcion=='3':
                id=int(input("ID del empleado a actualizar: "))
                nombre=input("Nuevo nombre: ")
                puesto=input("Nuevo puesto: ")
                salario=input("Nuevo salario: ")
                Empleado.actualizar_empleado(conexion, id, nombre, puesto, salario)
            elif opcion=='4':
                id=int(input("ID del empleado a eliminar: ")) 
                Empleado.eliminar_empleado(conexion, id)
            elif opcion=='5':
                cerrar_conexion(conexion)
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__=="__main__":
    menu()