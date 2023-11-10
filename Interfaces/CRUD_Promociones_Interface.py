from tkinter import *
import PIL.Image
import PIL.ImageTk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from Crud.CRUDOfertas import CRUDPromociones, Promocion
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
from Utilities.ListFramePromociones import ListFrame
from Utilities.ListFramePromociones import CuadrotePromociones


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
        self.botoncito = Button(self.cuadritoPromociones, text="crear promocion", font=("Arial", 15), command=self.crearPromocion)
        self.botoncito.pack()

        #Cuadrote promociones
        self.cuadrotePromociones = CuadrotePromociones()
        self.cuadrotePromociones.place(x=394,y=82)

        #self.bind("<Button-1>", self.aaa)
        self.refresh()
        self.mainloop()
    #  prueba para añadir las promociones a la lista
    def refresh(self):
        self.cuadroPromociones.clear()
        promociones= self.crud.Read()
        for promocion in promociones:
            if len(promocion.descripcion) > 40:
                enseñar = promocion.descripcion[0:40] + "..."
            else:
                enseñar = promocion.descripcion
            frame = ListFrame(self.cuadroPromociones, enseñar, promocion)

            frame.addevento("<Button-1>", self.mostrarPromocion)
            self.cuadroPromociones.add(frame)
        promociones.clear()
    def crearPromocion(self):
        pass

    def mostrarPromocion(self, promocion : Promocion):
        script = (f'SELECT producto.id_producto, producto.nombre from producto inner join promocion on promocion.id_producto = producto.id_producto WHERE %s = promocion.descripcion')
        cursor = self.__conection.cursor()
        cursor.execute(script, [promocion.descripcion])
        result = cursor.fetchone()
        resultado = []
        for i in result:
            resultado.append(i)
        #resultado tiene el id y el nombre del prooduto
        self.cuadrotePromociones.listaProd.set(resultado[1])
    def aaa(self,event):
        print(event.x, event.y)

interfaz = PromocionInterface()