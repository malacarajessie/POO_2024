from conexion import *

class Transacciones():
    def __init__(self, id_ventas, matricula, fecha, precio, nif_cliente):
        self.id_ventas = id_ventas
        self.matricula = matricula
        self.fecha = fecha
        self.precio = precio
        self.nif_clinte = nif_cliente

    @staticmethod
    def insertar_venta(id_venta, matricula, fecha, precio, nif_cliente):
        sentencia = "INSERT INTO ventas (id_venta, matricula, fecha, precio, nif_cliente) VALUES (%s, %s, %s, %s, %s)"
        valores = (id_venta, matricula, fecha, precio, nif_cliente)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Venta añadida con éxito.")

    @staticmethod
    def consultar_ventas():
        cursor.execute("SELECT * FROM ventas")
        resultados = cursor.fetchall()
        if resultados:
            for i in resultados:
                print(f"id_venta: {i[0]}, matricula: {i[1]}, fecha: {i[2]}, precio: {i[3]}, nif_cliente: {i[4]}")
        else:
            print("No se encontraron ventas.")
    

    @staticmethod
    def actualizar_venta(id_venta):
        matricula = input("Matricula del auto vendido: ").upper()
        fecha = input("Fecha de venta (YYYY-MM-DD): ")
        precio = float(input("Precio de venta: "))
        nif_cliente = int(input("NIF del cliente: "))
        sentencia = "UPDATE ventas SET matricula = %s, fecha = %s, precio = %s, nif_cliente = %s WHERE id_venta = %s"
        valores = (matricula, fecha, precio, nif_cliente, id_venta)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("La venta ha sido actualizada exitosamente.")

    @staticmethod
    def eliminar_venta(id_venta):
        cursor.execute("DELETE FROM ventas WHERE id_venta = %s", (id_venta,))
        conexion.commit()
        print("La venta ha sido eliminada exitosamente.")

class Transacciones():
    def __init__(self, id_compras, matricula, fecha, precio, nif_cliente):
        self.id_compras = id_compras
        self.matricula = matricula
        self.fecha = fecha
        self.precio = precio
        self.nif_cliente = nif_cliente

    @staticmethod
    def insertar_compra(id_compra, matricula, fecha, precio, nif_cliente):
        sentencia = "INSERT INTO compras (id_compra, matricula, fecha, precio, nif_cliente) VALUES (%s, %s, %s, %s, %s)"
        valores = (id_compra, matricula, fecha, precio, nif_cliente)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Compra añadida con éxito.")

    @staticmethod
    def consultar_compras():
        cursor.execute("SELECT * FROM compras")
        resultados = cursor.fetchall()
        if resultados:
            for i in resultados:
                print(f"id_compra: {i[0]}, matricula: {i[1]}, fecha: {i[2]}, precio: {i[3]}, nif_cliente: {i[4]}")
        else:
            print("No se encontraron compras.")

    @staticmethod
    def actualizar_compra(id_compra):
        matricula = input("Matrícula del auto comprado: ").upper()
        fecha = input("Fecha de compra (YYYY-MM-DD): ")
        precio = float(input("Precio de compra: "))
        nif_cliente = input("NIF del cliente: ")
        sentencia = "UPDATE compras SET matricula = %s, fecha = %s, precio = %s, nif_cliente = %s WHERE id_compra = %s"
        valores = (matricula, fecha, precio, nif_cliente, id_compra)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("La compra ha sido actualizada exitosamente.")

    @staticmethod
    def eliminar_compra(id_compra):
        cursor.execute("DELETE FROM compras WHERE id_compra = %s", (id_compra,))
        conexion.commit()
        print("La compra ha sido eliminada exitosamente.")

