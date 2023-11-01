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

        # Creare un widget donde desplegar las cosas para buscar los producos
        marginProductos = Frame(self, height=500, width=250, background="#204484")
        marginProductos.grid(column=0, row=0, pady=50, padx=50, ipadx=20, ipady=20, sticky="NSW")

        # Barra del buscador
        nav = Entry(marginProductos, background="#d8dce4", foreground="white")
        nav.pack(pady=20, fill="x", padx=20)

        # Un frame donde acomodar los productos
        self.__listProductos = AutomaticScrollableFrame(marginProductos, height=470)
        self.__listProductos.pack(fill="both", padx=20)

        # Cosas del margen de un solo producto
        self.__singleProduct = Frame(self)
        self.__singleProduct.columnconfigure(0, weight=4)
        self.__singleProduct.columnconfigure(1, weight=1)
        self.__frameNombres = Frame(self.__singleProduct)
        self.__labelNombre = Label(self.__frameNombres, text="Nombre")
        self.__entryNombre = Entry(self.__frameNombres)
        self.__imageDescription = Label(self.__singleProduct, text="Imagen: ")
        self.__imagenProduct = Label(self.__singleProduct, text="Imagen", anchor="e")
        self.__imageChangeButton = Button(self.__singleProduct, text="Cambiar imagen")
        self.__labelDescripcion = Label(self.__singleProduct, text="Descripcion")
        self.__entryDescripcion = Text(self.__singleProduct, height=3)

        # Saber si el panel individual ya se activo:
        self.__singleActivated = False

        # Saber el producto activo
        self.__activeProduct = None
        self.__activeImage = ""

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
            newElement.addEvent("<Button-1>", self.__showProduct)
            self.__listProductos.add(newElement)
        productos.clear()

    def __displayProductoMenu(self):
        if not self.__singleActivated:
            self.__singleProduct.grid(column=1, row=0, padx=(20, 20), pady=50, ipadx=30, ipady=20, sticky="ewns")
            self.__imageDescription.grid(column=1, row=0, sticky="sw", padx=80)
            self.__frameNombres.grid(column=0, row=1, rowspan=2, sticky="nwe", padx=(20, 0))
            self.__labelNombre.pack(side="top", anchor="w", pady=15)
            self.__entryNombre.pack(side="top", anchor="w", expand=True, fill="x", ipady=15)
            self.__imagenProduct.grid(column=1, row=1, sticky="new", rowspan=2, padx=(0, 20))
            self.__imageChangeButton.grid(column=1, row=3, sticky="ne", padx=(0, 20))
            self.__labelDescripcion.grid(column=0, row=4, sticky="nw", pady=20, padx=30)
            self.__entryDescripcion.grid(column=0, row=5, columnspan=2, ipady=15, sticky="we", padx=(20, 20))
            imagen_producto = PIL.Image.open("../img/noImage.jpg")
            imagen_producto = PIL.ImageTk.PhotoImage(imagen_producto)
            self.__imagenProduct.configure(image=imagen_producto)
            self.__imagenProduct.Image = imagen_producto
            self.__singleActivated = True
        else:
            self.__entryNombre.delete(0, END)
            self.__entryDescripcion.delete("0.0", END)
            imagen_producto = PIL.Image.open("../img/noImage.jpg")
            imagen_producto = PIL.ImageTk.PhotoImage(imagen_producto)
            self.__imagenProduct.configure(image=imagen_producto)
            self.__imagenProduct.Image = imagen_producto


    def __showProduct(self, producto:Producto):
        self.__displayProductoMenu()
        self.__entryNombre.insert(0, producto.nombre)
        self.__entryDescripcion.insert("0.0", producto.descripcion)

        imagen_producto = PIL.Image.open(producto.imagen)
        imagen_producto.resize((200, 200))
        imagen_producto = PIL.ImageTk.PhotoImage(imagen_producto)
        self.__imagenProduct.configure(image=imagen_producto)
        self.__imagenProduct.Image = imagen_producto
        pass


#gestorProducto = CrudProducto(conection)
#productManager = CrudProducto(conection)
#productManager.Create(Producto("Si", "Takvez", 69.420, driveCode=productManager.UploadImage("../img/mimikiu.png")["id"]))
ventana = CPr_Interface()
