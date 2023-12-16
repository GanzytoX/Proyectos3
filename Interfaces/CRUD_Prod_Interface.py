import os

import PIL.Image
import PIL.ImageTk
import mysql.connector
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
from Utilities.ListFrames import ImageFrame
from Utilities.twoSideWindow import twoSideWindow
from Crud.CRUD_producto import CrudProducto, Producto
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import messagebox


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


class CPr_Interface(twoSideWindow):

    __conection = None

    def __init__(self):
        super().__init__(window_name="Productos", size="1200x700", resizable=False, background_image="../img/Producto.png")
        self.__conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.__productManager = CrudProducto(conection=self.__conection)
        self.protocol("WM_DELETE_WINDOW", self.__cerrar_ventana)

        # Boton para buscar
        self.get_boton_buscar().config(command=self.__search)

        # Un boton para agregar productos
        self.get_agregar_elemento_button().config(command=self.__configureAgregar, text="Crear producto")

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
        self.__CantidadLabel = Label(self.__singleProduct, text="Cantidad")
        self.__CantidadEntry = Entry(self.__singleProduct)

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
        self.__editarProductoButton = Button(self.__singleProduct, text="Editar Producto",
                                             command=self.__editarProducto)
        self.__eliminarProductoButton = Button(self.__singleProduct, text="Eliminar Producto",
                                               command=self.__eliminarProducto)

    def __updateProductos(self):
        self.__conection.reconnect()
        for file in os.listdir("../userImages"):
            f = os.path.join("../userImages", file)
            os.remove(f)

        self.get_list_elements().clear()

        cuenta = int
        procesados = 0

        ids = self.__productManager.getIds()
        barraCarga = BarraCarga(self, length=400, bg="white", fg="black", text="Cargando imágenes", variable=cuenta,
                                maximun=len(ids))
        barraCarga.place(x=600, y=350, anchor="center")
        self.update_idletasks()

        for id in ids:
            producto = self.__productManager.Read(id[0])
            if producto.activo == "V":
                newElement = ImageFrame(self.get_list_elements(),
                                            f"{producto.nombre}",
                                            producto, producto.imagen)
                newElement.addEvent("<Button-1>", self.__showProduct)
                self.get_list_elements().add(newElement)
                procesados += 1
            barraCarga.set(procesados)
            self.update_idletasks()
        barraCarga.destroy()


    def __update_productos_simplified(self):
        productos = self.__productManager.ReadSimplified()
        cantidad_productos = self.get_list_elements().countItems()
        for i in range(cantidad_productos-1, -1, -1):
            if any(elemento.id == self.get_list_elements().getItem(i).object.id for elemento in productos):
                productos = [elemento for elemento in productos if elemento.id != self.get_list_elements().getItem(i).object.id]
            else:
                self.get_list_elements().deleteAt(i)

        cuenta = int
        procesados = 0
        barraCarga = BarraCarga(self, length=400, bg="white", fg="black", text="Cargando imágenes", variable=cuenta,
                                maximun=len(productos))
        barraCarga.place(x=600, y=350, anchor="center")
        self.update_idletasks()

        for producto in productos:
            producto = self.__productManager.Read(producto.id)
            if producto.activo == "V":
                newElement = ImageFrame(self.get_list_elements(),
                                        f"{producto.nombre}",
                                        producto, producto.imagen)
                newElement.addEvent("<Button-1>", self.__showProduct)
                self.get_list_elements().add(newElement)
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
            self.__CantidadLabel.grid(column=1,row=4)
            self.__CantidadEntry.grid(column=1, row = 5)
            self.__singleActivated = True
        else:
            self.__CantidadEntry.delete(0,END)
            self.__entryNombre.delete(0, END)
            self.__entryDescripcion.delete("0.0", END)
            self.__entryPrecio.delete(0, END)
            self.__setImage("../img/noImage.jpg")

    # Pone en la interfaz el producto activo
    def __showProduct(self, producto: Producto):
        self.__conection.reconnect()
        self.__CantidadEntry.delete(0,END)
        self.__agregarProducto.grid_forget()
        self.__displayProductoMenu()
        self.__entryNombre.insert(0, producto.nombre)
        self.__entryPrecio.insert(0, str(producto.precio))
        self.__entryDescripcion.insert("0.0", producto.descripcion)
        self.__setImage(producto.imagen)
        self.__editarProductoButton.grid(column=0, row=8, sticky="w", pady=10, padx=20)
        self.__eliminarProductoButton.grid(column=1, row=8, sticky="w", pady=10, padx=20)
        self.__activeProduct = producto
        script = "SELECT cantidad FROM inventario WHERE id_producto = %s"
        cursor = self.__conection.cursor()
        cursor.execute(script,[producto.id])
        result =cursor.fetchone()
        self.__CantidadEntry.insert(0, result[0])

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
        self.uwu = self.__entryNombre.get()
        try:
            self.__productManager.Create(self.__crearObjetoProducto())
            cursor = self.__conection.cursor()
            script = "INSERT INTO inventario(id_producto, nombre_producto, unidad, cantidad) VALUES (%s, %s, %s, %s)"
            self.__conection.reconnect()
            script2 = "SELECT MAX(id_producto) FROM producto"
            cursor.execute(script2)
            result = cursor.fetchone()
            paramss = [result[0], self.uwu, "--", int(self.__CantidadEntry.get())]
            print(paramss)
            cursor.execute(script, paramss)
            self.__conection.commit()
            self.__CantidadEntry.delete(0, END)

        except Exception as e:
            messagebox.showerror("Error", "Ocurrió un error al crear el producto, cheque los datos "
                                          "ingresados e intente de nuevo")
            print(e)
        else:
            self.__update_productos_simplified()
            self.__displayProductoMenu()
        finally:
            barraCarga.destroy()


    def __editarProducto(self):

        barraCarga = BarraCarga(self, length=400, bg="white", fg="black", text="Creando producto", mode="indeterminate")
        barraCarga.place(x=600, y=350, anchor="center")
        barraCarga.start()
        try:
            self.__productManager.Update(self.__activeProduct.id, self.__crearObjetoProducto())
            script = "Update inventario Set cantidad = %s Where id_producto = %s"
            cursor = self.__conection.cursor()
            asubir = [int(self.__CantidadEntry.get()), self.__activeProduct.id]
            cursor.execute(script, asubir)
            self.__conection.commit()
        except:
            messagebox.showerror("Ocurrió un error al editar el producto, cheque los datos ingresados e intente de nuevo")
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
        self.__update_productos_simplified()

        if self.get_list_elements().countItems() > 0:
            self.__showProduct(self.get_list_elements().getItem(0).object)
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
        if len(self.get_navegation_bar().get()) > 0:
            self.get_list_elements().clear()

            barraCarga = BarraCarga(self, length=400, bg="white", fg="black", text="Cargando imágenes",
                                    mode="indeterminate")
            barraCarga.place(x=600, y=350, anchor="center")
            self.update_idletasks()

            productos = self.__productManager.findSimilar(self.get_navegation_bar().get())
            for producto in productos:
                if producto.activo == "V":
                    newElement = ImageFrame(self.get_list_elements(),
                                                f"{producto.nombre}",
                                                producto, producto.imagen)
                    newElement.addEvent("<Button-1>", self.__showProduct)
                    self.get_list_elements().add(newElement)
                self.update_idletasks()
            barraCarga.destroy()
        else:
            self.__updateProductos()

    def __cerrar_ventana(self):
        self.__conection.close()
        self.destroy()
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

