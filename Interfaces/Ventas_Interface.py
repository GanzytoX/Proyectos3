from tkinter import *
import mysql.connector
from Utilities.VentasScrollableFrame import ScrollableFrame
from Crud.CRUD_producto import *
from PIL import Image,ImageTk
class siFrame(Frame):
    def __init__(self, master:any, nombreProducto:str, precio:float):
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
        self.botonAgregar = Button(self, text = "Agregar", command=lambda: print("si"))
        self.botonAgregar.pack()
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
        self.scrollCuadro = ScrollableFrame(self, width=500, height=500)
        self.scrollCuadro.grid(column=0, row=0, sticky="nsew", pady=20, padx=20)

        #Cuadro ventas
        self.__cuadroProductos = Frame(self, padx=20, pady=20, width=200)
        self.__cuadroProductos.config(bg="#FF00FF")
        self.__cuadroProductos.grid(column=1, row=0, sticky="nsew", padx=20, pady=20)

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
            self.scrollCuadro.add(siFrame(self.scrollCuadro, item.nombre,item.precio))

ventas = VentasInterFace()