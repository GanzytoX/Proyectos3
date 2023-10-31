import os

import PIL.Image
import PIL.ImageTk
import mysql.connector
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
from Utilities.ListFrames import ImageFrame
from Crud.CRUD_producto import CrudProducto, Producto
from tkinter import *




class CPr_Interface(Tk):

    __conection = None

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
        self.__productManager = CrudProducto(conection=self.__conection)
        self.title("Productos")
        self.geometry("1200x700")
        self.resizable(False, False)

        imagen_fondo = PIL.Image.open("../img/Empleado.png")
        imagen_fondo = PIL.ImageTk.PhotoImage(imagen_fondo)
        # Crear un widget Label para mostrar la imagen de fondo
        label_imagen = Label(self, image=imagen_fondo)
        label_imagen.place(relwidth=1, relheight=1)  # Estirar la imagen para que cubra toda la ventana

        # Configurar cuadrícula de la ventana
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=2)

        # Creare un widget donde desplegar las cosas para buscar los producos
        marginProductos = Frame(self, height=500, width=250)
        marginProductos.grid(column=0, row=0, pady=50, ipadx=20, ipady=20, sticky=NS)

        # Barra del buscador
        nav = Entry(marginProductos, background="#397bb8", foreground="white")
        nav.pack(pady=20, fill="x", padx=20)

        # Un frame donde acomodar los productos
        self.__listProductos = AutomaticScrollableFrame(marginProductos, height=470)
        self.__listProductos.pack(fill="both", padx=20)

        # Cosas del margen de un solo producto
        self.__singleProduct = Frame(self)

        self.__labelNombre = Label(self.__singleProduct, text="Nombre")
        self.__entryNombre = Entry(self.__singleProduct)
        self.__imagenProduct = Label(self.__singleProduct, text="Imagen")
        self.__labelDescripcion = Label(self.__singleProduct, text="Descripcion")
        self.__entryDescripcion = Entry(self.__singleProduct)

        # Saber si el panel individual ya se activo:
        self.__singleActivated = False

        # Saber el producto activo
        self.__activeProduct = None

        # Jalar todos los productos posibles
        self.__updateProductos()

        self.mainloop()

    def __updateProductos(self):
        for file in os.listdir("../userImages"):
            f = os.path.join("../userImages", file)
            os.remove(f)

        self.__listProductos.clear()
        productos = self.__productManager.Read()
        for producto in productos:
            newElement = ImageFrame(self.__listProductos,
                                      f"{producto.nombre}",
                                      producto, producto.imagen)
            newElement.addEvent("<Button-1>", self.__showProducto)
            self.__listProductos.add(newElement)
        productos.clear()

    def __showProducto(self, producto):
        if not self.__singleActivated:
            self.__singleProduct.grid(column=1, row=0, padx=(30, 50), pady=50, ipadx=30, ipady=20, sticky="ewns")
            self.__labelNombre.grid(row=0, column=0)
            self.__entryNombre.grid(column=0, row=1)
            self.__imagenProduct.grid(column=1, row=0)
            self.__labelDescripcion.grid(column=0, row=2)
            self.__entryDescripcion.grid(column=0, row=3, columnspan=1)

        pass

conection = mysql.connector.connect(
            user="root",
            host="localhost",
            port="3307",
            #port="3306",
            #password="0123456789",
            database="pollosexpress"
        )
#gestorProducto = CrudProducto(conection)
#productManager = CrudProducto(conection)
#productManager.Create(Producto("Si", "Takvez", 69.420, driveCode=productManager.UploadImage("../img/mimikiu.png")["id"]))
ventana = CPr_Interface()
