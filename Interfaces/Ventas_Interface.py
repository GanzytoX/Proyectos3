from tkinter import *
import mysql.connector
from Utilities.VentasScrollableFrame import ScrollableFrame
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
from Utilities.ListFrames import ventaFrame
from Crud.CRUD_producto import *
from PIL import Image,ImageTk
import time
from tkinter import messagebox
from Utilities.ValidadorDeOfertas import validar
from Interfaces.PagoInterface import Pagos


class VentasInterFace(Tk):
    def __init__(self, idU):
        super().__init__()
        self.idU = idU
        self.__conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.resizable(False, False)
        self.columnconfigure(index=0, weight=4)
        self.columnconfigure(index=1, weight=3)
        self.rowconfigure(0, weight=1)
        self.geometry("1200x700")

        # scroll como tal
        self.scrollCuadro = ScrollableFrame(self, width=500, height=500,length=3)
        self.scrollCuadro.grid(column=0, row=0, sticky="nsew", pady=20, padx=20)
        self.scrollCuadroProductos = []

        # Cuadro ventas
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

        # Cuadro de las preventas
        self.scrollPreventa = AutomaticScrollableFrame(self.__cuadroProductos,height=350,width=200)
        self.scrollPreventa.grid(columnspan=3,column=0, row=2, sticky="nsew", padx=10)
        self.preventa = []
        self.TotalLabel = Label(self.__cuadroProductos, text= "Total")
        self.TotalLabel.grid(column=0, row=3)
        self.TotalLabelCant = Label(self.__cuadroProductos, text= "$0")
        self.TotalLabelCant.grid(column=2, row=3)
        self.botonPagar = Button(self.__cuadroProductos,text="Pagar", command=self.__send_info, state="disabled")
        self.botonPagar.grid(column=1, row=4)

        # Add products to scroll
        self.add_products_to_scroll()
        self.mainloop()

    def get_products(self):
        crud = CrudProducto(self.__conection)
        #todo aqui
        results = crud.Read()
        self.productos = []
        for result in results:
            self.productos.append(result)
        for producto in self.productos:
            print(f"Hay un producto llamado {producto.nombre}")

    def add_products_to_scroll(self):
        self.get_products()
        for item in self.productos:
            toAdd = siFrame(self.scrollCuadro, item.nombre, item.precio, self, item.id)
            self.scrollCuadro.add(toAdd)
            self.scrollCuadroProductos.append(toAdd)

    def add_venta_frame(self, nombre, cantidad, precio, id):
        cantidad = int(cantidad)
        precio = float(precio)
        print(precio)
        print("llamada")
        if cantidad > 0:
            for i in range(self.scrollPreventa.countItems()):
                if self.scrollPreventa.getItem(i).get_nombre() == nombre:
                    print(precio)
                    self.scrollPreventa.getItem(i).set_cantidad(cantidad)
                    self.scrollPreventa.getItem(i).set_subtotal(precio)

                    return
            self.scrollPreventa.add(ventaFrame(self.scrollPreventa,nombre,cantidad,precio, id))
        else:
            for i in range(self.scrollPreventa.countItems()):
                if self.scrollPreventa.getItem(i).get_nombre() == nombre:
                    print("Encontre uno similar")
                    self.scrollPreventa.deleteAt(i)
                    break

    def calcularTotal(self) -> float:
        total = 0
        for i in range(self.scrollPreventa.countItems()):
            total += self.scrollPreventa.getItem(i).get_subtotal()
        self.TotalLabelCant.config(text=f"${total}")
        return total

    def agregar_venta(self):
        scrip = "INSERT INTO venta(fecha_De_Venta, total_De_Compra, id_pago, id_empleado) VALUES(%s, %s, %s, %s);"
        actual_time = time.localtime()
        timeFormatted = time.strftime("%Y/%m/%d", actual_time)

        values = (timeFormatted, self.calcularTotal(), 1, self.idU)
        self.__conection.cursor().execute(scrip, values)
        self.__conection.commit()

        messagebox.showinfo("Listo", "La venta ha sido agregada")

        scrip2 = "SELECT MAX(id_Venta) FROM venta;"
        cursor = self.__conection.cursor()
        cursor.execute(scrip2)
        idelast = cursor.fetchone()

        scrip3 = "INSERT INTO venta_producto(id_venta, id_producto, cantidad) VALUES(%s, %s, %s);"
        for i in range (self.scrollPreventa.countItems()):
            values = (idelast[0], self.scrollPreventa.getItem(i).idP, self.scrollPreventa.getItem(i).get_cantidad())
            self.__conection.cursor().execute(scrip3, values)
            self.__conection.commit()

        self.reset()

    # Resetea la venta al regresar
    def reset(self):
        self.scrollPreventa.clear()
        self.TotalLabelCant.config(text="$0")
        for item in self.scrollCuadroProductos:
            item.cantidadLabel.config(text="0")

    # Recolecta todos los elementos para mandarlos a la interfaz de venta
    def __send_info(self):
        lista = []
        for i in range(self.scrollPreventa.countItems()):
            item = self.scrollPreventa.getItem(i)
            lista.append((item.get_nombre(), item.get_cantidad(), item.get_subtotal(), item.idP))
        ventanaPago = Pagos(lista, self.idU, self)
        ventanaPago.mainloop()



class siFrame(Frame):
    def __init__(self, master:any, nombreProducto:str, precio:float, main:VentasInterFace, id_product):
        super().__init__(master, width=240, height=260, bg="#f0f0f0",relief="groove", borderwidth=5)
        self.propagate(False)

        #Parametros
        self.nombreProducto = nombreProducto
        self.preciofloat = precio
        self.main = main
        self.__id_product = id_product

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
        if int(self.cantidadLabel.cget("text")) == 0:
            validar(self.__id_product)
        self.cantidadLabel.config(text=(str(int(self.cantidadLabel.cget("text")) + 1))) if int(self.cantidadLabel.cget("text")) < 25 else 25
        self.main.add_venta_frame(nombre=self.nombreProducto, cantidad=self.cantidadLabel.cget("text"),
                             precio=self.preciofloat * float(self.cantidadLabel.cget("text")), id=self.__id_product)
        self.main.calcularTotal()

    def __subtract(self):
        self.cantidadLabel.config(text=str(int(self.cantidadLabel.cget("text")) - 1)) if (
                    int(self.cantidadLabel.cget("text")) > 0) else 0
        self.main.add_venta_frame(nombre=self.nombreProducto, cantidad=self.cantidadLabel.cget("text"),
                                  precio=float(self.preciofloat * float(self.cantidadLabel.cget("text"))), id=self.__id_product)
        self.main.calcularTotal()
    def __reset(self):
        self.cantidadLabel.config(text="0")




