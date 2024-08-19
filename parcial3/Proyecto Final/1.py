import tkinter as tk
from tkinter import simpledialog, messagebox

class Cliente:
    @staticmethod
    def insertar(nif, nombre, direccion, ciudad, telefono):
        pass

    @staticmethod
    def consultar(nif):
        return {"nif": nif, "nombre": "Nombre", "direccion": "Dirección", "ciudad": "Ciudad", "telefono": "Teléfono"}

    @staticmethod
    def actualizar(nif, nombre, direccion, ciudad, telefono):
        pass

    @staticmethod
    def eliminar(nif):
        pass

class Auto:
    @staticmethod
    def insertar(marca, modelo, año, precio):
        pass

    @staticmethod
    def consultar(id_auto):
        return {"marca": "Marca", "modelo": "Modelo", "año": 2023, "precio": 25000}

    @staticmethod
    def actualizar(id_auto, marca, modelo, año, precio):
        pass

    @staticmethod
    def eliminar(id_auto):
        pass

class Venta:
    @staticmethod
    def insertar(id_cliente, id_auto, fecha, precio):
        pass

    @staticmethod
    def consultar(id_venta):
        return {"id_cliente": 1, "id_auto": 2, "fecha": "2024-08-15", "precio": 20000}

    @staticmethod
    def actualizar(id_venta, id_cliente, id_auto, fecha, precio):
        pass

    @staticmethod
    def eliminar(id_venta):
        pass

class Compra:
    @staticmethod
    def insertar(nif_cliente, id_auto, fecha, precio):
        pass

    @staticmethod
    def consultar(id_compra):
        return {"nif_cliente": 1, "id_auto": 2, "fecha": "2024-08-15", "precio": 15000}

    @staticmethod
    def actualizar(id_compra, nif_cliente, id_auto, fecha, precio):
        pass

    @staticmethod
    def eliminar(id_compra):
        pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión")
        self.geometry("1000x700")
        self.config(bg="#f0f0f0")
        self.menu_login()

    def validar_entero(self, mensaje):
        while True:
            try:
                valor = int(simpledialog.askstring("Entrada", mensaje))
                return valor
            except ValueError:
                messagebox.showerror("Error", "Debes ingresar un número válido.")

    def validar_float(self, mensaje):
        while True:
            try:
                valor = float(simpledialog.askstring("Entrada", mensaje))
                return valor
            except ValueError:
                messagebox.showerror("Error", "Debes ingresar un número decimal válido.")

    def menu_login(self):
        self.clear_window()
        tk.Label(self, text="INICIO DE SESIÓN", font=("Arial", 32)).pack(pady=40)
        tk.Button(self, text="Iniciar sesión", font=("Arial", 24), command=self.iniciar_sesion).pack(fill="x", pady=20)
        tk.Button(self, text="Registrarse", font=("Arial", 24), command=self.registrarse).pack(fill="x", pady=20)
        tk.Button(self, text="Salir", font=("Arial", 24), command=self.quit).pack(fill="x", pady=20)

    def iniciar_sesion(self):
        email = simpledialog.askstring("Inicio de Sesión", "Ingresa tu E-mail:")
        password = simpledialog.askstring("Inicio de Sesión", "Ingresa tu Contraseña:", show="*")
        if True:
            self.menu_principal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    def registrarse(self):
        nombre = simpledialog.askstring("Registro", "¿Cuál es tu nombre?:")
        apellidos = simpledialog.askstring("Registro", "¿Cuáles son tus apellidos?:")
        email = simpledialog.askstring("Registro", "Ingresa tu email:")
        password = simpledialog.askstring("Registro", "Ingresa tu contraseña:", show="*")
        if True:
            messagebox.showinfo("Registro", f"{nombre} {apellidos}, se registró correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario. Inténtalo de nuevo.")

    def menu_principal(self):
        self.clear_window()
        tk.Label(self, text="BIENVENIDO", font=("Arial", 32)).pack(pady=40)
        tk.Button(self, text="MENU CLIENTES", font=("Arial", 24), command=self.menuClientes).pack(fill="x", pady=20)
        tk.Button(self, text="MENU AUTOS", font=("Arial", 24), command=self.menuAutos).pack(fill="x", pady=20)
        tk.Button(self, text="MENU VENTAS", font=("Arial", 24), command=self.menuVentas).pack(fill="x", pady=20)
        tk.Button(self, text="MENU COMPRAS", font=("Arial", 24), command=self.menuCompras).pack(fill="x", pady=20)
        tk.Button(self, text="SALIR", font=("Arial", 24), command=self.quit).pack(fill="x", pady=20)

    def menuClientes(self):
        self.clear_window()
        tk.Label(self, text="MENU DE CLIENTES", font=("Arial", 32)).pack(pady=40)
        tk.Button(self, text="Registrar un cliente", font=("Arial", 24), command=self.registrar_cliente).pack(fill="x", pady=20)
        tk.Button(self, text="Consultar información de un cliente", font=("Arial", 24), command=self.consultar_cliente).pack(fill="x", pady=20)
        tk.Button(self, text="Actualizar información del cliente", font=("Arial", 24), command=self.actualizar_cliente).pack(fill="x", pady=20)
        tk.Button(self, text="Dar de baja un cliente", font=("Arial", 24), command=self.eliminar_cliente).pack(fill="x", pady=20)
        tk.Button(self, text="Volver", font=("Arial", 24), command=self.menu_principal).pack(fill="x", pady=20)

    def registrar_cliente(self):
        nif = simpledialog.askstring("Registro de Cliente", "NIF del Cliente:")
        nombre = simpledialog.askstring("Registro de Cliente", "Nombre del Cliente:")
        direccion = simpledialog.askstring("Registro de Cliente", "Dirección del Cliente:")
        ciudad = simpledialog.askstring("Registro de Cliente", "Ciudad del Cliente:")
        telefono = simpledialog.askstring("Registro de Cliente", "Teléfono del Cliente:")
        Cliente.insertar(nif, nombre, direccion, ciudad, telefono)
        messagebox.showinfo("Registro", f"Cliente {nombre} registrado exitosamente.")

    def consultar_cliente(self):
        nif = simpledialog.askstring("Consulta de Cliente", "NIF del Cliente:")
        cliente_info = Cliente.consultar(nif)
        if cliente_info:
            info = f"NIF: {cliente_info['nif']}\nNombre: {cliente_info['nombre']}\nDirección: {cliente_info['direccion']}\nCiudad: {cliente_info['ciudad']}\nTeléfono: {cliente_info['telefono']}"
            messagebox.showinfo("Información del Cliente", info)
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")

    def actualizar_cliente(self):
        nif = simpledialog.askstring("Actualizar Cliente", "NIF del Cliente:")
        cliente_info = Cliente.consultar(nif)
        if cliente_info:
            nombre = simpledialog.askstring("Actualizar Cliente", "Nombre del Cliente:", initialvalue=cliente_info['nombre'])
            direccion = simpledialog.askstring("Actualizar Cliente", "Dirección del Cliente:", initialvalue=cliente_info['direccion'])
            ciudad = simpledialog.askstring("Actualizar Cliente", "Ciudad del Cliente:", initialvalue=cliente_info['ciudad'])
            telefono = simpledialog.askstring("Actualizar Cliente", "Teléfono del Cliente:", initialvalue=cliente_info['telefono'])
            Cliente.actualizar(nif, nombre, direccion, ciudad, telefono)
            messagebox.showinfo("Actualización", "Cliente actualizado correctamente.")
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")

    def eliminar_cliente(self):
        nif = simpledialog.askstring("Eliminar Cliente", "NIF del Cliente:")
        Cliente.eliminar(nif)
        messagebox.showinfo("Eliminación", "Cliente eliminado correctamente.")

    def menuAutos(self):
        self.clear_window()
        tk.Label(self, text="MENU DE AUTOS", font=("Arial", 32)).pack(pady=40)
        tk.Button(self, text="Añadir auto", font=("Arial", 24), command=self.anadir_auto).pack(fill="x", pady=20)
        tk.Button(self, text="Consultar información de un auto", font=("Arial", 24), command=self.consultar_auto).pack(fill="x", pady=20)
        tk.Button(self, text="Actualizar información de un auto", font=("Arial", 24), command=self.actualizar_auto).pack(fill="x", pady=20)
        tk.Button(self, text="Eliminar un auto", font=("Arial", 24), command=self.eliminar_auto).pack(fill="x", pady=20)
        tk.Button(self, text="Volver", font=("Arial", 24), command=self.menu_principal).pack(fill="x", pady=20)

    def anadir_auto(self):
        marca = simpledialog.askstring("Añadir Auto", "Marca del Auto:")
        modelo = simpledialog.askstring("Añadir Auto", "Modelo del Auto:")
        año = self.validar_entero("Año del Auto:")
        precio = self.validar_float("Precio del Auto:")
        Auto.insertar(marca, modelo, año, precio)
        messagebox.showinfo("Registro", f"Auto {marca} {modelo} registrado exitosamente.")

    def consultar_auto(self):
        id_auto = self.validar_entero("ID del Auto:")
        auto_info = Auto.consultar(id_auto)
        if auto_info:
            info = f"Marca: {auto_info['marca']}\nModelo: {auto_info['modelo']}\nAño: {auto_info['año']}\nPrecio: {auto_info['precio']}"
            messagebox.showinfo("Información del Auto", info)
        else:
            messagebox.showerror("Error", "Auto no encontrado.")

    def actualizar_auto(self):
        id_auto = self.validar_entero("ID del Auto:")
        auto_info = Auto.consultar(id_auto)
        if auto_info:
            marca = simpledialog.askstring("Actualizar Auto", "Marca del Auto:", initialvalue=auto_info['marca'])
            modelo = simpledialog.askstring("Actualizar Auto", "Modelo del Auto:", initialvalue=auto_info['modelo'])
            año = self.validar_entero("Año del Auto:")
            precio = self.validar_float("Precio del Auto:")
            Auto.actualizar(id_auto, marca, modelo, año, precio)
            messagebox.showinfo("Actualización", "Auto actualizado correctamente.")
        else:
            messagebox.showerror("Error", "Auto no encontrado.")

    def eliminar_auto(self):
        id_auto = self.validar_entero("ID del Auto:")
        Auto.eliminar(id_auto)
        messagebox.showinfo("Eliminación", "Auto eliminado correctamente.")

    def menuVentas(self):
        self.clear_window()
        tk.Label(self, text="MENU DE VENTAS", font=("Arial", 32)).pack(pady=40)
        tk.Button(self, text="Registrar una venta", font=("Arial", 24), command=self.registrar_venta).pack(fill="x", pady=20)
        tk.Button(self, text="Consultar información de una venta", font=("Arial", 24), command=self.consultar_venta).pack(fill="x", pady=20)
        tk.Button(self, text="Actualizar información de una venta", font=("Arial", 24), command=self.actualizar_venta).pack(fill="x", pady=20)
        tk.Button(self, text="Eliminar una venta", font=("Arial", 24), command=self.eliminar_venta).pack(fill="x", pady=20)
        tk.Button(self, text="Volver", font=("Arial", 24), command=self.menu_principal).pack(fill="x", pady=20)

    def registrar_venta(self):
        id_cliente = self.validar_entero("ID del Cliente:")
        id_auto = self.validar_entero("ID del Auto:")
        fecha = simpledialog.askstring("Registro de Venta", "Fecha de la Venta:")
        precio = self.validar_float("Precio de la Venta:")
        Venta.insertar(id_cliente, id_auto, fecha, precio)
        messagebox.showinfo("Registro", "Venta registrada exitosamente.")

    def consultar_venta(self):
        id_venta = self.validar_entero("ID de la Venta:")
        venta_info = Venta.consultar(id_venta)
        if venta_info:
            info = f"ID Cliente: {venta_info['id_cliente']}\nID Auto: {venta_info['id_auto']}\nFecha: {venta_info['fecha']}\nPrecio: {venta_info['precio']}"
            messagebox.showinfo("Información de la Venta", info)
        else:
            messagebox.showerror("Error", "Venta no encontrada.")

    def actualizar_venta(self):
        id_venta = self.validar_entero("ID de la Venta:")
        venta_info = Venta.consultar(id_venta)
        if venta_info:
            id_cliente = self.validar_entero("ID del Cliente:")
            id_auto = self.validar_entero("ID del Auto:")
            fecha = simpledialog.askstring("Actualizar Venta", "Fecha de la Venta:", initialvalue=venta_info['fecha'])
            precio = self.validar_float("Precio de la Venta:")
            Venta.actualizar(id_venta, id_cliente, id_auto, fecha, precio)
            messagebox.showinfo("Actualización", "Venta actualizada correctamente.")
        else:
            messagebox.showerror("Error", "Venta no encontrada.")

    def eliminar_venta(self):
        id_venta = self.validar_entero("ID de la Venta:")
        Venta.eliminar(id_venta)
        messagebox.showinfo("Eliminación", "Venta eliminada correctamente.")

    def menuCompras(self):
        self.clear_window()
        tk.Label(self, text="MENU DE COMPRAS", font=("Arial", 32)).pack(pady=40)
        tk.Button(self, text="Registrar una compra", font=("Arial", 24), command=self.registrar_compra).pack(fill="x", pady=20)
        tk.Button(self, text="Consultar información de una compra", font=("Arial", 24), command=self.consultar_compra).pack(fill="x", pady=20)
        tk.Button(self, text="Actualizar información de una compra", font=("Arial", 24), command=self.actualizar_compra).pack(fill="x", pady=20)
        tk.Button(self, text="Eliminar una compra", font=("Arial", 24), command=self.eliminar_compra).pack(fill="x", pady=20)
        tk.Button(self, text="Volver", font=("Arial", 24), command=self.menu_principal).pack(fill="x", pady=20)

    def registrar_compra(self):
        nif_cliente = simpledialog.askstring("Registro de Compra", "NIF del Cliente:")
        id_auto = self.validar_entero("ID del Auto:")
        fecha = simpledialog.askstring("Registro de Compra", "Fecha de la Compra:")
        precio = self.validar_float("Precio de la Compra:")
        Compra.insertar(nif_cliente, id_auto, fecha, precio)
        messagebox.showinfo("Registro", "Compra registrada exitosamente.")

    def consultar_compra(self):
        id_compra = self.validar_entero("ID de la Compra:")
        compra_info = Compra.consultar(id_compra)
        if compra_info:
            info = f"NIF Cliente: {compra_info['nif_cliente']}\nID Auto: {compra_info['id_auto']}\nFecha: {compra_info['fecha']}\nPrecio: {compra_info['precio']}"
            messagebox.showinfo("Información de la Compra", info)
        else:
            messagebox.showerror("Error", "Compra no encontrada.")

    def actualizar_compra(self):
        id_compra = self.validar_entero("ID de la Compra:")
        compra_info = Compra.consultar(id_compra)
        if compra_info:
            nif_cliente = simpledialog.askstring("Actualizar Compra", "NIF del Cliente:", initialvalue=compra_info['nif_cliente'])
            id_auto = self.validar_entero("ID del Auto:")
            fecha = simpledialog.askstring("Actualizar Compra", "Fecha de la Compra:", initialvalue=compra_info['fecha'])
            precio = self.validar_float("Precio de la Compra:")
            Compra.actualizar(id_compra, nif_cliente, id_auto, fecha, precio)
            messagebox.showinfo("Actualización", "Compra actualizada correctamente.")
        else:
            messagebox.showerror("Error", "Compra no encontrada.")

    def eliminar_compra(self):
        id_compra = self.validar_entero("ID de la Compra:")
        Compra.eliminar(id_compra)
        messagebox.showinfo("Eliminación", "Compra eliminada correctamente.")

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()

