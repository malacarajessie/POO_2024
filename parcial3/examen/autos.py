from conexionbd import *

class autos:
    def __init__(self,matricula, marca, modelo,color):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo
        self.color=color


    def crear_autos(conexionbd,matricula,marca,modelo,color):
        cursor=conexionbd.cursor()
        query="INSERT INTO autos (matricula,marca,modelo,color) VALUES (%s,%s,%s,%s)"
        valores=(matricula,marca,modelo,color)
        cursor.execute(query, valores)
        conexionbd.commit()
        print("registro del auto creado")

    def leer_autos(conexionbd):
        cursor = conexionbd.cursor()
        query ="SELECT * FROM autos"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"matricula:{fila[0]},marca:{fila[1]},modelo:{fila[2]},color: {fila[3]}")

            
    def actualizar_auto(conexionbd,id,nombre,puesto,salario):
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
 