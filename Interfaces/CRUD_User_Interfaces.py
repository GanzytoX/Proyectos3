import tkinter as tk
from tkinter import Tk
from customtkinter import CTkScrollableFrame
from tkinter import messagebox
import mysql.connector
from Crud.CRUD_Usuario import CrudEmpleado
from PIL import Image, ImageTk


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

        #Creare un widget donde desplegar los empleados
        marginEmpleados = CTkScrollableFrame(self, height=500, width=250)
        marginEmpleados.grid(column=0, row=0, pady=50, ipadx=20, ipady=20, sticky=tk.NS)

        #Barra del buscador
        nav = tk.Entry(marginEmpleados)
        nav.pack()


        marginUnEmpleado = tk.Frame(self)
        marginUnEmpleado.grid(column=1, row=0, padx=(30, 50), pady=50, ipadx=30, ipady=20, sticky="ewns")
        self.mainloop()

ventana = CUInterface()


class NoImageFrame(tk.Frame):
    def __init__(self):
        super().__init__()

