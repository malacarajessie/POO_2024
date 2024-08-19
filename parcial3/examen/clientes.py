from conexionbd import *

class empleado:
    def __init__(self,nombre, puesto, salario):
        self.nombre=nombre
        self.puesto=puesto
        self.salario=salario


    def crear_empleado(conexionbd, nombre, puesto, salario):
        cursor=conexionbd.cursor()
        query="INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
        valores=(nombre, puesto, salario)
        cursor.execute(query, valores)
        conexionbd.commit()
        print("registro del empleado creado")

    def leer_empleados(conexionbd):
        cursor = conexionbd.cursor()
        query ="SELECT * FROM empleados"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"id:{fila[0]},nombre:{fila[1]},puesto:{fila[2]},salario: {fila[3]}")

            
    def actualizar_empleado(conexionbd,id,nombre,puesto,salario):
        cursor=conexionbd.cursor()
        query="UPDATE empleados SET nombre=%s, puesto=%s, salario=%s WHERE empleadoid=%s"
        valores=(nombre,puesto,salario,id)
        cursor.execute(query,valores)
        conexionbd.commit()
        print("empleado actualizado exitosamente")


    def eliminar_empleado(conexionbd, id):
        cursor=conexionbd.cursor()
        query="DELETE FROM empleados WHERE EmpleadoID = %s"
        cursor.execute(query, (id,))
        conexionbd.commit()
        print("empleado eliminado exitosamente")
 