import tkinter as tk
from tkinter import Tk
from typing import Callable, Literal

from customtkinter import CTkScrollableFrame
from tkinter import messagebox
import mysql.connector
from Crud.CRUD_Usuario import CrudEmpleado
from PIL import Image, ImageTk
from multipledispatch import dispatch


class AutomaticScrollableFrame(CTkScrollableFrame):
    def __init__(self, master: any, height=None, width=None):
        if height is not None and width is not None:
            super().__init__(master, height=height, width=width)
        elif height is not None:
            super().__init__(master, height=height)
        elif width is not None:
            super().__init__(master, width=width)
        self.__items = []
        self.columnconfigure(0, weight=3)

    def add(self, element: any) -> None:
        element.grid(column=0, row=len(self.__items), sticky="ew", pady="5")
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


class NoImageFrame(tk.Frame):
    def __init__(self, master: AutomaticScrollableFrame, text: str = None, objet = None):
        super().__init__(master=master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        imagen_raw = Image.open("../img/dot.png")
        imagen_raw.thumbnail((10, 10))
        imagen_tk = ImageTk.PhotoImage(imagen_raw)
        self.__image = tk.Label(self, image=imagen_tk)
        self.__image.image = imagen_tk
        self.__image.grid(column=0, row=0)
        self.__text = tk.Label(self, height=4, justify="left", text=text)
        self.__text.grid(column=1, row=0, sticky="W")
        if objet is not None:
            self.object = objet

    def addEvent(
            self: tk.W,
            sequence: str | None = ...,
            func: Callable[[object], None] | None = ...):
        self.__function = func
        string = super().bind(sequence, self.__returnObject)
        self.__image.bind(sequence, self.__returnObject)
        self.__text.bind(sequence, self.__returnObject)
        return string

    def __returnObject(self, event):
        self.__function(self.object)


class CUInterface(Tk):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="root",
            host="localhost",
            port="3307",
            #port="3306",
            #password="0123456789",
            database="pollosexpress"
        )
        self.__userManager = CrudEmpleado(self.__conection)
        self.title("Empleados")
        self.geometry("1200x700")
        self.resizable(False, False)

        # No se si use esto pero será para ver si la interfaz ya ha sido activada
        self.__singleActivated = False

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
        nav = tk.Entry(marginEmpleados, background="#397bb8", foreground="white")
        nav.pack(pady=20, fill="x", padx=20)

        # Un frame donde acomodar los empleados
        listEmpleados = AutomaticScrollableFrame(marginEmpleados, height=500)
        listEmpleados.pack(fill="both", padx=20)


        #Agregar todos los empleados posibles:
        empleados = self.__userManager.Read()
        for empleado in empleados:
            newElement = NoImageFrame(listEmpleados, f"{empleado.nombre} {empleado.apellido_paterno} {empleado.apellido_materno}", empleado)
            newElement.addEvent("<Button-1>", self.__showEmpleado)
            listEmpleados.add(newElement)
        empleados.clear()

        self.__marginUnEmpleado = tk.Frame(self)
        self.__marginUnEmpleado.grid(column=1, row=0, padx=(30, 50), pady=50, ipadx=30, ipady=20, sticky="ewns")
        self.mainloop()

    # Esta funcion se manda a llamar cuando clickean algo de la lista
    def __showEmpleado(self, empleado):
        print("clicked")
        isAdmin = tk.IntVar()
        # Si no se ha activado el panel que muestra un solo empleado, entonces lo crea
        if not self.__singleActivated:
            labelName = tk.Label(self.__marginUnEmpleado, text="Nombre: ")
            labelName.grid(column=0, row=0)
            inputName = tk.Entry(self.__marginUnEmpleado)
            inputName.grid(column=0, row=1)

            labelLastname1 = tk.Label(self.__marginUnEmpleado, text="Apellido Paterno: ")
            labelLastname1.grid(column=1, row=0)
            inputLastname1 = tk.Entry(self.__marginUnEmpleado)
            inputLastname1.grid(column=1, row=1)

            labelLastname2 = tk.Label(self.__marginUnEmpleado, text="Apellido Materno: ")
            labelLastname2.grid(column=3, row=0)
            inputLastname2 = tk.Entry(self.__marginUnEmpleado)
            inputLastname2.grid(column=3, row=1)

            labelCel = tk.Label(self.__marginUnEmpleado, text="Celular: ")
            labelCel.grid(column=0, row=2)
            inputCel = tk.Entry(self.__marginUnEmpleado)
            inputCel.grid(column=0, row=3, columnspan=4, sticky="ew")

            labelSueldo = tk.Label(self.__marginUnEmpleado, text="Sueldo: ")
            labelSueldo.grid(column=0, row=4)
            inputSueldo = tk.Entry(self.__marginUnEmpleado)
            inputSueldo.grid(column=0, row=5, columnspan=4, sticky="ew")

            labelContraseña = tk.Label(self.__marginUnEmpleado, text="Contraseña: ")
            labelContraseña.grid(column=0, row=6)
            inputContraseña = tk.Entry(self.__marginUnEmpleado)
            inputContraseña.grid(column=0, row=7, columnspan=2, sticky="ew")

            radioAdmin = tk.Checkbutton(self.__marginUnEmpleado, text="Admin", variable=isAdmin, onvalue=1, offvalue=0)
            radioAdmin.grid(column=3, row=7, columnspan=4, sticky="ew")

        inputName.delete(0, tk.END)
        inputName.insert(0, empleado.nombre)
        inputLastname1.delete(0, tk.END)
        inputLastname1.insert(0, empleado.apellido_paterno)
        inputLastname2.delete(0, tk.END)
        inputLastname2.insert(0, empleado.apellido_materno)
        inputCel.delete(0, tk.END)
        inputCel.insert(0, empleado.celular)
        inputSueldo.delete(0, tk.END)
        inputSueldo.insert(0, empleado.sueldo)
        inputContraseña.delete(0, tk.END)
        if empleado.contraseña is not None:
            inputContraseña.insert(0, empleado.contraseña)
        isAdmin.set(empleado.administrador)
        radioAdmin.mainloop()




ventana = CUInterface()


