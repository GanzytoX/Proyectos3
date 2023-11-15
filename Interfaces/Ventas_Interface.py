from tkinter import *
import mysql.connector
from Utilities.VentasScrollableFrame import ScrollableFrame
from Crud.CRUD_producto import *
from PIL import Image,ImageTk

class VentasInterFace(Tk):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="sql5660121",
            host="sql5.freesqldatabase.com",
            port="3306",
            password="GWes4WXpXH",
            database="sql5660121"

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
        self.textoVenta = Label(self.__cuadroProductos, text="Venta", font=("Arial", 15)).grid(columnspan=3,
                                                                                               column=0,
                                                                                               row=0)
        self.textoVenta = Label(self.__cuadroProductos, text="Producto  |  Cantidad  |  Subtotal", font=("Arial", 10)).grid(columnspan=3,
                                                                                               column=0,
                                                                                               row=1)
        self.scrollPreventa = ScrollableFrame(self.__cuadroProductos,height=350,width=200,length=1)
        self.scrollPreventa.grid(columnspan=3,column=0, row=2)
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
            self.scrollCuadro.add(siFrame(self.scrollCuadro, item.nombre,item.precio,self))

    def add_venta_frame(self, nombre, cantidad, precio):
        cantidad = int(cantidad)
        precio = int(precio)
        if cantidad > 0:
            self.scrollPreventa.add(ventaFrame(self.scrollPreventa,nombre,cantidad,precio))
            self.preventa.append(precio*cantidad)
        else:
            print("Intentaste meter 0 productos xd")
    def calcularTotal(self):
        total = 0
        for item in self.preventa:
            total += item
        self.TotalLabelCant.config(text=f"${total}")

class siFrame(Frame):
    def __init__(self, master:any, nombreProducto:str, precio:float, main:VentasInterFace):
        super().__init__(master, width=240, height=260, bg="#f0f0f0",relief="groove",borderwidth=5)
        self.propagate(False)

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
        self.botonMas = Button(self.cantidadFrame, text="+", command=lambda : (self.cantidadLabel.config(text=(str(int(self.cantidadLabel.cget("text")) + 1))) if int(self.cantidadLabel.cget("text")) < 25 else 25))
        self.botonMas.grid(column=2,row=0)
        self.botonMenos = Button(self.cantidadFrame, text="-", command=lambda : self.cantidadLabel.config(text= str(int(self.cantidadLabel.cget("text")) - 1)) if (int(self.cantidadLabel.cget("text")) > 0) else 0)
        self.botonMenos.grid(column= 0, row = 0)
        self.cantidadLabel = Label(self.cantidadFrame, text="0")
        self.cantidadLabel.grid(column=1, row=0)
        self.cantidadFrame.pack()
        self.precio = Label(self, text=f"${str(precio)} MXN")
        self.precio.pack()
        self.botonAgregar = Button(self, text = "Agregar", command=lambda:(main.add_venta_frame(nombre=nombreProducto,cantidad=self.cantidadLabel.cget("text"),precio=precio),self.cantidadLabel.config(text="0"),main.calcularTotal()))
        self.botonAgregar.pack()


class ventaFrame(Frame):
    def __init__(self, master:any, nombre,cantidad,precio):
        super().__init__(master, width=200, height=20, bg="#652341")
        super().propagate(FALSE)
        super().columnconfigure(index=0, weight=2)
        super().columnconfigure(index=1, weight=2)
        super().columnconfigure(index=2, weight=2)
        if len(nombre) > 10:
            aescribirNombre = nombre[0:11] + "..."
        else:
            aescribirNombre = nombre
        self.precio = int(precio) * int(cantidad)
        self.nombreLabel = Label(self, text=f"{aescribirNombre}",padx=10).grid(column=0, row=0)
        self.cantidadLabel = Label(self, text=f"{cantidad}",padx=25).grid(column=2, row=0)
        self.precioLabel = Label(self,text=f"${self.precio}",padx=20).grid(column=3, row=0)


ventas = VentasInterFace()