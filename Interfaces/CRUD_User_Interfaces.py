import tkinter as tk
from tkinter import Tk
from customtkinter import CTkScrollableFrame
from tkinter import messagebox
import mysql.connector
from Crud.CRUD_Usuario import CrudEmpleado
from PIL import Image, ImageTk


class NoImageFrame(tk.Frame):
    def __init__(self, text: str):
        super().__init__()
        self.config(height=50)
        contenedor = tk.Label(self, text=text)
        contenedor.pack(side=tk.LEFT)


class AutomaticScrollableFrame(CTkScrollableFrame):
    def __init__(self, master: any, height=None, width=None):
        if height is not None and width is not None:
            super().__init__(master, height=height, width=width)
        elif height is not None:
            super().__init__(master, height=height)
        elif width is not None:
            super().__init__(master, width=width)
        self.__items = []

    def add(self, element: any) -> None:
        element.grid(column=0, row=len(self.__items), sticky="ew")
        self.__items.append(element)

    def deleteAt(self, index):
        if len(self.__items) > index >= 0:
            item = self.__items[index]
            self.__items[index].remove(index)
            item.destroy()

    def getItem(self, index):
        if len(self.__items) > index >= 0:
            return self.__items[index]
        raise IndexError("Index out of range")


class CUInterface(Tk):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="root",
            host="localhost",
            port="3307",
            database="pollosexpress"
        )
        self.__userManager = CrudEmpleado(self.__conection)
        self.title("Empleados")
        self.geometry("1200x700")
        self.resizable(False, False)
        imagen_fondo = Image.open("../img/Empleado.png")
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

        # Crear un widget Label para mostrar la imagen de fondo
        label_imagen = tk.Label(self, image=imagen_fondo)
        #label_imagen.imagen = imagen_fondo
        label_imagen.place(relwidth=1, relheight=1)  # Estirar la imagen para que cubra toda la ventana

        #Configurar cuadrícula de la ventana
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=2)

        # Creare un widget donde desplegar las cosas para buscar los empleados
        marginEmpleados = tk.Frame(self, height=500, width=250)
        marginEmpleados.grid(column=0, row=0, pady=50, ipadx=20, ipady=20, sticky=tk.NS)

        # Barra del buscador
        nav = tk.Entry(marginEmpleados, background="#397bb8")
        nav.pack(pady=20)

        # Un frame donde acomodar los empleados
        listEmpleados = AutomaticScrollableFrame(marginEmpleados, height=500)
        listEmpleados.pack(fill="both", padx=20)


        marginUnEmpleado = tk.Frame(self)
        marginUnEmpleado.grid(column=1, row=0, padx=(30, 50), pady=50, ipadx=30, ipady=20, sticky="ewns")
        self.mainloop()

ventana = CUInterface()


