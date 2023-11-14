import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from Crud.CRUD_producto import CrudProducto




carrito = []

# Importo el Crud Usuario para poder hacer inicio de sesion y le paso un conection, o sea coneccion a la BD
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    port="3306",
    #password="0123456789",
    database="pollosexpress"
)

# utilidades
crud_producto = CrudProducto(connection)

# Crea la ventana principal
ventana = Tk()
ventana.title("Ventas")
ventana.geometry("1200x700")

# Cargar la imagen de fondo y redimensionarla
imagen_fondo = Image.open("../img/fondoventas.png")
imagen_fondo = imagen_fondo.resize((1200, 700), Image.LANCZOS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Agrega la imagen de fondo a un label
label_imagen = tk.Label(ventana, image=imagen_fondo)
label_imagen.pack(fill=tk.BOTH, expand=True)

# etiquetas
label1 = Label(ventana, bg="light gray", height=40, width=90)
label1.place(x=50, y=30)

# Crear el label
label2 = tk.Label(ventana, bg="#18358e", height=40, width=60)

# Configurar el padding interno
label2.config(padx=20, pady=20)
# Configurar el borde
label2.config(bd=5, relief="raised")
# Colocar el label en la ventana
label2.place(x=700, y=30)

label3 = Label(ventana, bg="#18358e", text="VENTA", font=100, fg="White")
label3.place(x=900, y=30)

label4 = Label(label2, bg="red", height=3, width=60)
label4.place(x=15, y=100)

label5 = Label(label2, text="Producto", bg="red", fg="White", font=50)
label5.place(x=15, y=110)

label6 = Label(label2, text="Cantidad", bg="red", fg="White", font=50)
label6.place(x=240, y=110)

label7 = Label(label2, text="SubTotal", bg="red", fg="White", font=50)
label7.place(x=340, y=110)

label8 = Label(label2, bg="#c4c4c4", height=30, width=60)
label8.place(x=15, y=137)

label9 = Label(label2, text="TOTAL", bg="#18358e", fg="White", font=100)
label9.place(x=15, y=600)

label10 = Label(label2, text="$$$$$$", bg="#18358e", fg="White", font=100)
label10.place(x=250, y=600)

botonpagar = tkinter.Button(label2, text="PAGAR", bg="#18358e", fg="White", font=100)
botonpagar.place(x=350, y=600)

# botones
botonagregar = tkinter.Button(ventana, text="agregar producto")
botoneliminar = tkinter.Button(ventana, text="X")
botonañadir = tkinter.Button(ventana, text="+")
botonquitar = tkinter.Button(ventana, text="-")

#CREAR UNA LISTA PARA EL CARRITO
##LOS PRODUCTOS SE ALMACENAN EN LA LISTA
###SE ELIMINA DEL INVENTARIO DE LA BASE DE DATOS (¿AL FINAL O AL PRINCIPIO?)

##otras funciones:
def añadir_producto(producto):
    producto = crud_producto.Read(producto_id)

    carrito.append(producto)
    print(f"Producto '{producto.nombre}' añadido al carrito.")

def quitar_producto(producto):


def eliminar_producto(producto):
    producto = crud_producto.Read(producto_id)

    if producto in carrito:
        carrito.remove(producto)
        print(f"Producto '{producto.nombre}' quitado del carrito.")
    else:
        print(f"Producto '{producto.nombre}' no encontrado en el carrito.")

##fin de funciones preeliminares

##bucle prueba 3 para mostrar los dateishons
def mostrar_productos():
    ventana_productos = Tk()
    ventana_productos.title("Lista de Productos")

    for producto in productos:
        frame_producto = Frame(ventana_productos)
        frame_producto.pack(pady=10)

        label_nombre = Label(frame_producto, text=producto["nombre"])
        label_nombre.pack()

        imagen_producto = Image.open(producto["imagen"])
        imagen_producto = imagen_producto.resize((100, 100), Image.LANCZOS)
        imagen_producto = ImageTk.PhotoImage(imagen_producto)
        label_imagen_producto = Label(frame_producto, image=imagen_producto)
        label_imagen_producto.image = imagen_producto
        label_imagen_producto.pack()

        label_precio = Label(frame_producto, text=f"Precio: ${producto['precio']}")
        label_precio.pack()

        boton_añadir = Button(frame_producto, text="+", command=lambda p=producto: añadir_producto(p))
        boton_quitar = Button(frame_producto, text="-", command=lambda p=producto: quitar_producto(p))
        boton_eliminar = Button(frame_producto, text="X", command=lambda p=producto: eliminar_producto(p))

        boton_añadir.pack()
        boton_quitar.pack()
        boton_eliminar.pack()
##fin del bucle




# Muestra la ventana
ventana.mainloop()
