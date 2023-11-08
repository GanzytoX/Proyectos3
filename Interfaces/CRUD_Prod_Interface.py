import os

import PIL.Image
import PIL.ImageTk
import mysql.connector
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
from Utilities.ListFrames import ImageFrame
from Crud.CRUD_producto import CrudProducto, Producto
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import messagebox
import threading

class BarraCarga(Frame):
    def __init__(self, master, length: int, bg=None, fg=None, text=None, variable=None, maximun=None, mode=None):
        super().__init__(master, background=bg)
        self.update_idletasks()
        self.__titleLabel = Label(self, text=text, background=bg, fg=fg)
        self.__barraCarga = Progressbar(self, length=length)

        if mode == "indeterminate":
            self.__barraCarga.config(mode=mode)
        else:
            self.__barraCarga.config(mode=mode, variable=variable, maximum=maximun)

        self.__titleLabel.pack()
        self.__barraCarga.pack(pady=10, padx=10)

    def set(self, value: int):
        self.__barraCarga["value"] = value

    def start(self):
        self.__barraCarga.start()


class CPr_Interface(Tk):

    __conection = None

    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="sql5660121",
            host="sql5.freesqldatabase.com",
            port="3306",
            password="GWes4WXpXH",
            database="sql5660121"
        )
        self.__productManager = CrudProducto(conection=self.__conection)
        self.title("Productos")
        self.geometry("1200x700")
        self.resizable(False, False)

        imagen_fondo = PIL.Image.open("../img/Empleado.png")
        imagen_fondo = PIL.ImageTk.PhotoImage(imagen_fondo, master=self)

        # Crear un widget Label para mostrar la imagen de fondo
        label_imagen = Label(self, image=imagen_fondo)
        label_imagen.place(relwidth=1, relheight=1)  # Estirar la imagen para que cubra toda la ventana
        label_imagen.imagen = imagen_fondo

        # Configurar cuadrícula de la ventana
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        # Creare un widget donde desplegar las cosas para buscar los producos
        marginProductos = Frame(self, height=500, width=250, background="#204484")
        marginProductos.grid(column=0, row=0, pady=50, padx=50, ipadx=20, sticky="NSW")
        marginProductos.columnconfigure(0, weight=5)
        marginProductos.columnconfigure(1, weight=1)

        # Margin de la barra de buscador
        frameBuscador = Frame(marginProductos, background="#204484")
        frameBuscador.columnconfigure(0, weight=5)
        frameBuscador.columnconfigure(1, weight=1)
        frameBuscador.pack(pady=20, padx=20, fill="x")

        # Barra del buscador
        self.__nav = Entry(frameBuscador, background="#d8dce4")
        self.__nav.grid(column=0, row=0, padx=(0, 5), sticky="NSEW")

        # Boton para buscar
        botonBuscar = Button(frameBuscador, text="B", command=self.__search)
        botonBuscar.grid(column=1, row=0, sticky="NSEW")

        # Un frame donde acomodar los productos
        self.__listProductos = AutomaticScrollableFrame(marginProductos, height=470)
        # Un boton para agregar productos
        self.__agregarProductoMenu = Button(marginProductos, text="Crear producto", command=self.__configureAgregar)
        self.__agregarProductoMenu.pack(pady=10)

        # Cosas del margen de un solo producto
        self.__singleProduct = Frame(self)
        self.__singleProduct.columnconfigure(0, weight=4)
        self.__singleProduct.columnconfigure(1, weight=1)
        self.__frameNombres = Frame(self.__singleProduct)
        self.__labelNombre = Label(self.__frameNombres, text="Nombre")
        self.__entryNombre = Entry(self.__frameNombres)
        self.__labelPrecio = Label(self.__singleProduct, text="Precio")
        self.__entryPrecio = Entry(self.__singleProduct)
        self.__imageDescription = Label(self.__singleProduct, text="Imagen: ")
        self.__imagenProduct = Label(self.__singleProduct, text="Imagen", anchor="e")
        self.__imageChangeButton = Button(self.__singleProduct, text="Cambiar imagen", command=self.__changeImagen)
        self.__labelDescripcion = Label(self.__singleProduct, text="Descripcion")
        self.__entryDescripcion = Text(self.__singleProduct, height=3)


        # Saber si el panel individual ya se activo:
        self.__singleActivated = False

        # Saber el producto activo
        self.__activeProduct = None
        self.__activeImage = ""

        # Jalar todos los productos posibles
        self.__updateProductos()

        # Boton para mandar a agregar
        self.__agregarProducto = Button(self.__singleProduct, text="Agregar Producto", command=self.__agregarUnProducto)

        # Boton para editar producto
        self.__editarProductoButton = Button(self.__singleProduct, text="Editar Producto", command=self.__editarProducto)
        self.__eliminarProductoButton = Button(self.__singleProduct, text="Eliminar Producto", command=self.__eliminarProducto)

    def __updateProductos(self):
        for file in os.listdir("../userImages"):
            f = os.path.join("../userImages", file)
            os.remove(f)

        self.__listProductos.clear()

        cuenta = int
        procesados = 0

        ids = self.__productManager.getIds()
        barraCarga = BarraCarga(self, length=400, bg="white", fg="black", text="Cargando imágenes", variable=cuenta,
                                maximun=len(ids))
        barraCarga.place(x=600, y=350, anchor="center")
        self.update_idletasks()

        for id in ids:
            producto = self.__productManager.Read(id[0])
            newElement = ImageFrame(self.__listProductos,
                                        f"{producto.nombre}",
                                        producto, producto.imagen)
            newElement.addEvent("<Button-1>", self.__showProduct)
            self.__listProductos.add(newElement)
            procesados += 1
            barraCarga.set(procesados)
            self.update_idletasks()
        barraCarga.destroy()

    def __displayProductoMenu(self):
        if not self.__singleActivated:
            self.__singleProduct.grid(column=1, row=0, padx=(20, 20), pady=50, ipadx=30, ipady=20, sticky="ewns")
            self.__imageDescription.grid(column=1, row=0, sticky="sw", padx=80)
            self.__frameNombres.grid(column=0, row=1, rowspan=2, sticky="nwe", padx=(20, 0))
            self.__labelNombre.pack(side="top", anchor="w", pady=15)
            self.__entryNombre.pack(side="top", anchor="w", expand=True, fill="x", ipady=15)
            self.__imagenProduct.grid(column=1, row=1, sticky="new", rowspan=2, padx=(0, 20))
            self.__imageChangeButton.grid(column=1, row=3, sticky="ne", padx=(0, 20))
            self.__labelPrecio.grid(column=0, row=4, sticky="nw", pady=10, padx=20)
            self.__entryPrecio.grid(column=0, row=5, sticky="nw", padx=20)
            self.__labelDescripcion.grid(column=0, row=6, sticky="nw", pady=15, padx=20)
            self.__entryDescripcion.grid(column=0, row=7, columnspan=2, ipady=15, sticky="we", padx=(20, 20))
            self.__setImage("../img/noImage.jpg")

            self.__singleActivated = True
        else:
            self.__entryNombre.delete(0, END)
            self.__entryDescripcion.delete("0.0", END)
            self.__entryPrecio.delete(0, END)
            self.__setImage("../img/noImage.jpg")

    # Pone en la interfaz el producto activo
    def __showProduct(self, producto: Producto):
        self.__agregarProducto.grid_forget()
        self.__displayProductoMenu()
        self.__entryNombre.insert(0, producto.nombre)
        self.__entryPrecio.insert(0, str(producto.precio))
        self.__entryDescripcion.insert("0.0", producto.descripcion)
        self.__setImage(producto.imagen)
        self.__editarProductoButton.grid(column=0, row=8, sticky="w", pady=10, padx=20)
        self.__eliminarProductoButton.grid(column=1, row=8, sticky="w", pady=10, padx=20)
        self.__activeProduct = producto

    # Configurar para Poder agregar un producto
    def __configureAgregar(self):
        self.__editarProductoButton.grid_forget()
        self.__eliminarProductoButton.grid_forget()
        self.__displayProductoMenu()
        self.__agregarProducto.grid(column=0, row=8, sticky="w", pady=10, padx=20)

    def __crearObjetoProducto(self) -> Producto:
        try:
            float(self.__entryPrecio.get())
        except ValueError:
            messagebox.showerror("Error", "El precio ingresado es invalido")
        else:
            newProduct = Producto(
                self.__entryNombre.get(),
                self.__entryDescripcion.get("0.0", 'end-1c'),
                float(self.__entryPrecio.get()),
                imagen=self.__activeImage,
                driveCode=self.__productManager.UploadImage(self.__activeImage)["id"]
            )
            return newProduct

    def __agregarUnProducto(self):
        barraCarga = BarraCarga(self, length=400, bg="white", fg="black", text="Creando producto", mode="indeterminate")
        barraCarga.place(x=600, y=350, anchor="center")
        barraCarga.start()
        self.update_idletasks()
        try:
            self.__productManager.Create(self.__crearObjetoProducto())
        except:
            pass
        else:
            self.__updateProductos()
            self.__displayProductoMenu()
        finally:
            barraCarga.destroy()

    def __editarProducto(self):

        barraCarga = BarraCarga(self, length=400, bg="white", fg="black", text="Creando producto", mode="indeterminate")
        barraCarga.place(x=600, y=350, anchor="center")
        barraCarga.start()
        try:
            self.__productManager.Update(self.__activeProduct.id, self.__crearObjetoProducto())
        except:
            pass
        else:
            self.__updateProductos()
        finally:
            barraCarga.destroy()



    def __eliminarProducto(self):
        barraCarga = BarraCarga(self, length=400, bg="white", fg="black", text="Eliminando producto", mode="indeterminate")
        barraCarga.place(x=600, y=350, anchor="center")
        barraCarga.start()
        self.__productManager.Delete(self.__activeProduct.id)
        barraCarga.destroy()
        self.__activeProduct = None
        self.__updateProductos()

        if self.__listProductos.countItems() > 0:
            self.__showProduct(self.__listProductos.getItem(0).object)
        else:
            self.__configureAgregar()

    # Tiene el objetivo de poner la imagen en la imagen de producto inicial
    def __setImage(self, ruta):
        imagen_producto = PIL.Image.open(ruta)
        imagen_producto = imagen_producto.resize((200, 200))
        imagen_producto = PIL.ImageTk.PhotoImage(imagen_producto, master=self.__imagenProduct)
        self.__activeImage = ruta
        self.__imagenProduct.configure(image=imagen_producto)
        self.__imagenProduct.Image = imagen_producto

    def __changeImagen(self):
        ruta = filedialog.askopenfilename(filetypes=[("Image", ["*.jpg", "*.png"])])
        self.__setImage(ruta)

    def __search(self):
        if len(self.__nav.get()) > 0:
            self.__listProductos.clear()

            barraCarga = BarraCarga(self, length=400, bg="white", fg="black", text="Cargando imágenes",
                                    mode="indeterminate")
            barraCarga.place(x=600, y=350, anchor="center")
            self.update_idletasks()

            productos = self.__productManager.findSimilar(self.__nav.get())
            for producto in productos:
                newElement = ImageFrame(self.__listProductos,
                                            f"{producto.nombre}",
                                            producto, producto.imagen)
                newElement.addEvent("<Button-1>", self.__showProduct)
                self.__listProductos.add(newElement)
                self.update_idletasks()
            barraCarga.destroy()
        else:
            self.__updateProductos()

#gestorProducto = CrudProducto(conection)
"""""
conection = mysql.connector.connect(
            user="root",
            host="localhost",
            port="3307",
            #port="3306",
            #password="0123456789",
            database="pollosexpress"
        )
productManager = CrudProducto(conection)
productManager.Create(Producto("Si", "Takvez", 69.420, driveCode=productManager.UploadImage("../img/mimikiu.png")["id"]))
"""

