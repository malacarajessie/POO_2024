import tkinter as tk
from tkinter import messagebox, simpledialog
from conexion import *
from autos import *
from clientes import *
from transacciones import *
from funciones import *
from usuarios import usuario

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión")
        self.geometry("500x300")
        self.menu_login()

    def validar_entero(self, mensaje):
        while True:
            try:
                valor = simpledialog.askinteger("Entrada", mensaje)
                return valor
            except ValueError:
                messagebox.showerror("Error", "Debes ingresar un número válido.")

    def validar_float(self, mensaje):
        while True:
            try:
                valor = simpledialog.askfloat("Entrada", mensaje)
                return valor
            except ValueError:
                messagebox.showerror("Error", "Debes ingresar un número decimal válido.")

    def menu_login(self):
        self.clear_window()
        self.login_frame = tk.Frame(self)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="..:: INICIO DE SESIÓN ::..").pack()

        tk.Button(self.login_frame, text="Iniciar sesión", command=self.iniciar_sesion).pack(fill="x", pady=5)
        tk.Button(self.login_frame, text="Registrarse", command=self.registrarse).pack(fill="x", pady=5)
        tk.Button(self.login_frame, text="Salir", command=self.quit).pack(fill="x", pady=5)

    def iniciar_sesion(self):
        self.clear_window()

        email = simpledialog.askstring("Inicio de Sesión", "Ingresa tu E-mail:")
        password = simpledialog.askstring("Inicio de Sesión", "Ingresa tu Contraseña:", show='*')

        registro = usuario.Usuario.iniciar_sesion(email, password)
        if registro:
            self.menu_principal()
        else:
            self.menu_principal()


    def registrarse(self):
        self.clear_window()

        nombre = simpledialog.askstring("Registro", "¿Cuál es tu nombre?")
        apellidos = simpledialog.askstring("Registro", "¿Cuáles son tus apellidos?")
        email = simpledialog.askstring("Registro", "Ingresa tu email:")
        password = simpledialog.askstring("Registro", "Ingresa tu contraseña:", show='*')

        obj_usuario = usuario.Usuario(nombre, apellidos, email, password)
        resultado = obj_usuario.registrar()

        if resultado:
            messagebox.showinfo("Registro", f"{nombre} {apellidos}, se registró correctamente con el email: {email}")
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario. Inténtalo de nuevo.")
        self.menu_login()

    def menu_principal(self):
        self.clear_window()
        tk.Label(self, text="Bienvenido Edgar Burciaga").pack(pady=10)

        tk.Button(self, text="MENU CLIENTES", command=self.menuClientes).pack(fill="x", pady=5)
        tk.Button(self, text="MENU AUTOS", command=self.menuAutos).pack(fill="x", pady=5)
        tk.Button(self, text="MENU VENTAS", command=self.menuVentas).pack(fill="x", pady=5)
        tk.Button(self, text="MENU COMPRAS", command=self.menuCompras).pack(fill="x", pady=5)
        tk.Button(self, text="SALIR", command=self.quit).pack(fill="x", pady=5)

    def menuClientes(self):
        self.clear_window()

        tk.Label(self, text="MENU DE CLIENTES").pack(pady=10)

        tk.Button(self, text="Registrar un cliente", command=self.registrar_cliente).pack(fill="x", pady=5)
        tk.Button(self, text="Consultar información de un cliente", command=self.consultar_cliente).pack(fill="x", pady=5)
        tk.Button(self, text="Actualizar información del cliente", command=self.actualizar_cliente).pack(fill="x", pady=5)
        tk.Button(self, text="Dar de baja un cliente", command=self.eliminar_cliente).pack(fill="x", pady=5)
        tk.Button(self, text="Volver", command=self.menu_principal).pack(fill="x", pady=5)

    def registrar_cliente(self):
        nif = self.validar_entero("Inserta NIF:")
        nombre = simpledialog.askstring("Registro de Cliente", "Nombre del cliente:")
        direccion = simpledialog.askstring("Registro de Cliente", "Dirección del cliente:")
        ciudad = simpledialog.askstring("Registro de Cliente", "Ciudad del cliente:")
        tel = self.validar_entero("Número de teléfono del cliente:")

        if Cliente.insertar(nif, nombre, direccion, ciudad, tel):
            messagebox.showinfo("Registro", "Cliente registrado con éxito.")
        else:
            messagebox.showerror("Error", "Error al registrar el cliente.")

    def consultar_cliente(self):
        Cliente.consultar()

    def actualizar_cliente(self):
        nif = self.validar_entero("Inserta NIF del cliente a actualizar:")
        Cliente.actualizar(nif)

    def eliminar_cliente(self):
        nif = self.validar_entero("Inserta NIF del cliente:")
        if Cliente.eliminar(nif):
            messagebox.showinfo("Eliminar", "Cliente eliminado con éxito.")
        else:
            messagebox.showerror("Error", "Error al eliminar el cliente.")

    def menuAutos(self):
        self.clear_window()

        tk.Label(self, text="MENU DE AUTOS").pack(pady=10)

        tk.Button(self, text="Añadir auto", command=self.añadir_auto).pack(fill="x", pady=5)
        tk.Button(self, text="Consultar información de un auto", command=self.consultar_auto).pack(fill="x", pady=5)
        tk.Button(self, text="Actualizar información", command=self.actualizar_auto).pack(fill="x", pady=5)
        tk.Button(self, text="Eliminar auto", command=self.eliminar_auto).pack(fill="x", pady=5)
        tk.Button(self, text="Volver", command=self.menu_principal).pack(fill="x", pady=5)

    def añadir_auto(self):
        matricula = simpledialog.askstring("Añadir Auto", "Matricula del auto:").upper()
        marca = simpledialog.askstring("Añadir Auto", "Marca del auto:")
        modelo = simpledialog.askstring("Añadir Auto", "Modelo del auto:")
        color = simpledialog.askstring("Añadir Auto", "Color del auto:")
        nif = self.validar_entero("NIF del cliente:")

        if Autos.insertar(matricula, marca, modelo, color, nif):
            messagebox.showinfo("Añadir", "Auto añadido con éxito.")
        else:
            messagebox.showerror("Error", "Error al añadir el auto.")

    def consultar_auto(self):
        Autos.consultar()

    def actualizar_auto(self):
        matricula = simpledialog.askstring("Actualizar Auto", "Matricula del auto a actualizar:").upper()
        Autos.actualizar(matricula)

    def eliminar_auto(self):
        matricula = simpledialog.askstring("Eliminar Auto", "Matricula del auto a eliminar:").upper()
        if Autos.eliminar(matricula):
            messagebox.showinfo("Eliminar", "Auto eliminado con éxito.")
        else:
            messagebox.showerror("Error", "Error al eliminar el auto.")

    def menuVentas(self):
        self.clear_window()

        tk.Label(self, text="MENU DE VENTAS").pack(pady=10)

        tk.Button(self, text="Hacer una venta", command=self.hacer_venta).pack(fill="x", pady=5)
        tk.Button(self, text="Consultar ventas", command=self.consultar_ventas).pack(fill="x", pady=5)
        tk.Button(self, text="Actualizar información de una venta", command=self.actualizar_venta).pack(fill="x", pady=5)
        tk.Button(self, text="Eliminar venta", command=self.eliminar_venta).pack(fill="x", pady=5)
        tk.Button(self, text="Volver", command=self.menu_principal).pack(fill="x", pady=5)

    def hacer_venta(self):
        id_venta = self.validar_entero("ID de la venta:")
        matricula = simpledialog.askstring("Venta", "Matricula del auto vendido:").upper()
        fecha = simpledialog.askstring("Venta", "Fecha de venta (YYYY-MM-DD):")
        precio = self.validar_float("Precio de venta:")
        nif_cliente = self.validar_entero("NIF del cliente:")

        if Transacciones.insertar_venta(id_venta, matricula, fecha, precio, nif_cliente):
            messagebox.showinfo("Venta", "Venta añadida con éxito.")
        else:
            messagebox.showerror("Error", "Error al añadir la venta.")

    def consultar_ventas(self):
        Transacciones.consultar_ventas()

    def actualizar_venta(self):
        id_venta = self.validar_entero("ID de la venta a actualizar:")
        Transacciones.actualizar_venta(id_venta)

    def eliminar_venta(self):
        id_venta = self.validar_entero("ID de la venta a eliminar:")
        if Transacciones.eliminar_venta(id_venta):
            messagebox.showinfo("Eliminar", "Venta eliminada con éxito.")
        else:
            messagebox.showerror("Error", "Error al eliminar la venta.")

    def menuCompras(self):
        self.clear_window()

        tk.Label(self, text="MENU DE COMPRAS").pack(pady=10)

        tk.Button(self, text="Hacer una compra", command=self.hacer_compra).pack(fill="x", pady=5)
        tk.Button(self, text="Consultar compras", command=self.consultar_compras).pack(fill="x", pady=5)
        tk.Button(self, text="Actualizar información de una compra", command=self.actualizar_compra).pack(fill="x", pady=5)
        tk.Button(self, text="Eliminar compra", command=self.eliminar_compra).pack(fill="x", pady=5)
        tk.Button(self, text="Volver", command=self.menu_principal).pack(fill="x", pady=5)

    def hacer_compra(self):
        id_compra = self.validar_entero("ID de la compra:")
        matricula = simpledialog.askstring("Compra", "Matricula del auto comprado:").upper()
        fecha = simpledialog.askstring("Compra", "Fecha de compra (YYYY-MM-DD):")
        precio = self.validar_float("Precio de compra:")
        nif_cliente = self.validar_entero("NIF del cliente:")

        if Transacciones.insertar_compra(id_compra, matricula, fecha, precio, nif_cliente):
            messagebox.showinfo("Compra", "Compra añadida con éxito.")
        else:
            messagebox.showerror("Error", "Error al añadir la compra.")

    def consultar_compras(self):
        Transacciones.consultar_compras()

    def actualizar_compra(self):
        id_compra = self.validar_entero("ID de la compra a actualizar:")
        Transacciones.actualizar_compra(id_compra)

    def eliminar_compra(self):
        id_compra = self.validar_entero("ID de la compra a eliminar:")
        if Transacciones.eliminar_compra(id_compra):
            messagebox.showinfo("Eliminar", "Compra eliminada con éxito.")
        else:
            messagebox.showerror("Error", "Error al eliminar la compra.")

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
