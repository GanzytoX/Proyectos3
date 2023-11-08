from tkinter import *
import PIL.Image
import PIL.ImageTk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from Crud.CRUDOfertas import CRUDPromociones, Promocion
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
from Utilities.ListFramePromociones import ListFrame


# Esteticas:


# Ventana:
class PromocionInterface(Tk):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="sql5660121",
            host="sql5.freesqldatabase.com",
            port="3306",
            password="GWes4WXpXH",
            database="sql5660121"

        )
        self.imagen_fondo = Image.open("../img/promociones.jpg")
        self.imagen_fondo = self.imagen_fondo.resize((1200, 700), Image.LANCZOS)
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen_fondo)
        self.label_imagen = Label(self, image=self.imagen_fondo)
        self.label_imagen.grid(row=0, column=0, sticky="NWSE")
        self.crud = CRUDPromociones(conection=self.__conection)
        self.title = "Promociones"
        self.geometry("1200x700")
        self.config(bg="#812634")
        self.resizable(False, False)

        # Pa que se acomode un cuadrito a la izquierda y uno grandote a la derecha
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        # El cuadrito de las promociones
        self.cuadritoPromociones = Frame(self, width=350, height=500, bg="#442250")
        self.cuadritoPromociones.grid(column=0, row=0, pady=50, padx=50, ipadx=20, sticky="W")

        # la barra de búsqueda
        self.busqueda = Entry(self.cuadritoPromociones, fg="red")
        self.busqueda.pack(fill="x")  # fill x es pa que lo llene de los lados

        # el cuadro donde se van a seleccionar las promociones
        self.cuadroPromociones = AutomaticScrollableFrame(self.cuadritoPromociones, height=470)
        self.cuadroPromociones.pack(fill="both", padx=30)

        #  boton para agregar promociones
        self.botoncito = Button(self.cuadritoPromociones, text="refresh(porahora)", font=("Arial", 15), command=self.prueba)
        self.botoncito.pack()

        #  Empezamos con el cuadrote de las promociones que tiene todos los datos
        self.Cuadrote = Frame(self)
        #  la primera columna mas ancha que la segunda
        self.Cuadrote.columnconfigure(0, weight=4)
        self.Cuadrote.columnconfigure(1, weight=1)

        self.mainloop()
    #  prueba para añadir las promociones a la lista
    def prueba(self):
        self.cuadroPromociones.clear()
        promociones= self.crud.Read()
        for promocion in promociones:
            if len(promocion.descripcion) > 40:
                promocion.descripcion = promocion.descripcion[0:40] + "..."
            frame = ListFrame(self.cuadroPromociones, promocion.descripcion,40)
            frame.addEvento("<Button-1>",self.mostrarPromocion(promocion))
            self.cuadroPromociones.add(frame)
        promociones.clear()


    def mostrarPromocion(self, promocion : Promocion):
        print(f'hay una promocion con descripcion "{promocion.descripcion}" ')

interfaz = PromocionInterface()