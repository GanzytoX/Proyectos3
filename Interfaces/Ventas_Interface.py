from tkinter import *
import mysql.connector
from Utilities.VentasScrollableFrame import ScrollableFrame
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
from Crud.CRUD_producto import *
from PIL import Image,ImageTk

class VentasInterFace(Tk):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="u119126_pollos",
            host="174.136.28.78",
            port="3306",
            password="$BulletKin0805",
            database="u119126_pollos"

        )
        self.resizable(False, False)
        self.columnconfigure(index=0, weight=4)
        self.columnconfigure(index=1, weight=3)
        self.rowconfigure(0, weight=1)
        self.geometry("1200x700")

        #scroll como tal
        self.scrollCuadro = ScrollableFrame(self, width=500, height=500,length=3)
        self.scrollCuadro.grid(column=0, row=0, sticky="nsew", pady=20, padx=20)

        #Cuadro ventas
        self.__cuadroProductos = Frame(self, width=200,relief="groove", borderwidth=2)
        self.__cuadroProductos.columnconfigure(index = 0, weight=2)
        self.__cuadroProductos.columnconfigure(index = 1, weight=2)
        self.__cuadroProductos.columnconfigure(index = 2, weight=2)
        self.__cuadroProductos.config(bg="#F0f0F0")
        self.__cuadroProductos.grid(column=1, row=0, sticky="nsew")
        self.textoVenta = Label(self.__cuadroProductos, text="Venta", font=("Arial", 15))
        self.textoVenta.grid(columnspan=3,column=0, row=0)
        self.textoVenta = Label(self.__cuadroProductos, text="Producto  |  Cantidad  |  Subtotal", font=("Arial", 10))
        self.textoVenta.grid(columnspan=3, column=0,row=1)

        #Cuadro de las preventas
        self.scrollPreventa = AutomaticScrollableFrame(self.__cuadroProductos,height=350,width=200)
        self.scrollPreventa.grid(columnspan=3,column=0, row=2, sticky="nsew", padx=10)
        self.preventa = []
        self.TotalLabel = Label(self.__cuadroProductos, text= "Total")
        self.TotalLabel.grid(column=0, row = 3)
        self.TotalLabelCant = Label(self.__cuadroProductos, text= "$0")
        self.TotalLabelCant.grid(column=2, row = 3)
        self.botonPagar = Button(self.__cuadroProductos,text="Pagar", command=print("pagado"))
        self.botonPagar.grid(column=1,row=4)
        #Add products to scroll
        self.add_products_to_scroll()
        self.mainloop()

    def get_products(self):
        crud = CrudProducto(self.__conection)
        results = crud.Read()
        self.productos = []
        for result in results:
            self.productos.append(result)
        for producto in self.productos:
            print(f"Hay un producto llamado {producto.nombre}")

    def add_products_to_scroll(self):
        self.get_products()
        for item in self.productos:
            self.scrollCuadro.add(siFrame(self.scrollCuadro, item.nombre, item.precio, self))

    def add_venta_frame(self, nombre, cantidad, precio):
        cantidad = int(cantidad)
        precio = float(precio)
        print(precio)
        print("llamada")
        if cantidad > 0:
            for i in range(self.scrollPreventa.countItems()):
                if self.scrollPreventa.getItem(i).get_nombre() == nombre:
                    print("Hay similar")
                    self.scrollPreventa.getItem(i).set_cantidad(cantidad)
                    self.scrollPreventa.getItem(i).set_subtotal(precio)

                    return
            self.scrollPreventa.add(ventaFrame(self.scrollPreventa,nombre,cantidad,precio))
        else:
            for i in range(self.scrollPreventa.countItems()):
                if self.scrollPreventa.getItem(i).get_nombre() == nombre:
                    print("Encontre uno similar")
                    self.scrollPreventa.deleteAt(i)
                    break
    def calcularTotal(self):
        total = 0
        for i in range(self.scrollPreventa.countItems()):
            total += self.scrollPreventa.getItem(i).get_subtotal()
        self.TotalLabelCant.config(text=f"${total}")

class siFrame(Frame):
    def __init__(self, master:any, nombreProducto:str, precio:float, main:VentasInterFace):
        super().__init__(master, width=240, height=260, bg="#f0f0f0",relief="groove", borderwidth=5)
        self.propagate(False)

        #Parametros
        self.nombreProducto = nombreProducto
        self.preciofloat = precio
        self.main = main

        #imagen
        self.unresized = Image.open(f"../userImages/product_{str(nombreProducto)}.png")
        self.resized_image = self.unresized.resize((150, 150))
        self.photoimage = ImageTk.PhotoImage(self.resized_image)
        self.image = Label(self, image=self.photoimage)
        self.image.pack()

        #nombre producto
        self.label = Label(self, text=nombreProducto)
        self.label.pack()

        #frame con botones
        self.cantidadFrame = Frame(self, width=250)
        self.cantidadFrame.columnconfigure(index=0, weight=2)
        self.cantidadFrame.columnconfigure(index=1, weight=2)
        self.cantidadFrame.columnconfigure(index=2, weight=2)
        self.botonMas = Button(self.cantidadFrame, text="+", command=self.__add)
        self.botonMas.grid(column=2,row=0)
        self.botonMenos = Button(self.cantidadFrame, text="-", command=self.__subtract)
        self.botonMenos.grid(column= 0, row = 0)
        self.cantidadLabel = Label(self.cantidadFrame, text="0")
        self.cantidadLabel.grid(column=1, row=0)
        self.cantidadFrame.pack()
        self.precio = Label(self, text=f"${str(precio)} MXN")
        self.precio.pack()


    def __add(self):

        self.cantidadLabel.config(text=(str(int(self.cantidadLabel.cget("text")) + 1))) if int(self.cantidadLabel.cget("text")) < 25 else 25
        self.main.add_venta_frame(nombre=self.nombreProducto, cantidad=self.cantidadLabel.cget("text"),
                             precio=self.preciofloat * float(self.cantidadLabel.cget("text")))
        self.main.calcularTotal()

    def __subtract(self):
        self.cantidadLabel.config(text=str(int(self.cantidadLabel.cget("text")) - 1)) if (
                    int(self.cantidadLabel.cget("text")) > 0) else 0
        self.main.add_venta_frame(nombre=self.nombreProducto, cantidad=self.cantidadLabel.cget("text"),
                                  precio=float(self.preciofloat * float(self.cantidadLabel.cget("text"))))
        self.main.calcularTotal()

class ventaFrame(Frame):
    def __init__(self, master:any, nombre,cantidad,precio):
        super().__init__(master, width=200, height=20, bg="#652341")
        super().columnconfigure(index=0, weight=2)
        super().columnconfigure(index=1, weight=2)
        super().columnconfigure(index=2, weight=2)
        self.__nombre = nombre
        self.__subtotal = float(precio)
        self.__cantidad = float(cantidad)
        if len(nombre) > 20:
            aescribirNombre = nombre[0:20] + "..."
        else:
            aescribirNombre = nombre
        self.precio = float(precio) * int(cantidad)
        self.nombreLabel = Label(self, text=f"{aescribirNombre}",padx=10)
        self.nombreLabel.grid(column=0, row=0, sticky="w")
        self.cantidadLabel = Label(self, text=f"{cantidad}",padx=25)
        self.cantidadLabel.grid(column=2, row=0, sticky="ew")
        self.precioLabel = Label(self,text=f"${self.precio}",padx=20)
        self.precioLabel.grid(column=3, row=0, sticky="e")

    def get_nombre(self):
        return self.__nombre

    def set_subtotal(self, value: float):
        if isinstance(value, float):
            if value >= 0:
                self.__subtotal = value
                self.precioLabel.config(text=f"${value}")
            else:
                raise ValueError("El subtotal no puede ser negativo")
        else:
            raise ValueError("El subtotal debe ser un numero")

    def set_cantidad(self, value: float):
        if isinstance(value, float) or isinstance(value, int):
            if value >= 0:
                self.__cantidad = value
                self.cantidadLabel.config(text=f"{value}")
            else:
                raise ValueError("La cantidad no puede ser negativo")
        else:
            raise ValueError("La cantidad debe ser un numero")

    def get_subtotal(self) -> float:
        return self.__subtotal

    def get_cantidad(self):
        return self.__cantidad

ventas = VentasInterFace()