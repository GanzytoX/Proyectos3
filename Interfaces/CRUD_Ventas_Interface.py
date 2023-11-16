import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
#from CRUD_producto import CRUD_producto, producto
# Lista para almacenar los productos en el carrito
carrito = []


# Paleta de colores
c_blanco = "#ffffff"
c_gris = "#b8bab9"
c_gris_claro = "#e7e7e5"
c_rojo = "#e73a4b"
c_rojo_palido = "#c9636c"
c_azul = "#185791"
c_azul_claro = "#397bb8"
c_azul_palido = "#AFEEEE"

# Importo el Crud Usuario para poder hacer inicio de sesion y le paso un conection, o sea coneccion a la BD
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    port="3306",
    #password="0123456789",
    database="pollosexpress"
)

def mostrar_lista_productos():
    # Crear una conexión a la base de datos
    connection = mysql.connector.connect(
        user="root",
        host="localhost",
        port="3306",
        database="pollosexpress"
    )

# Crear un cursor para ejecutar consultas SQL
    cursor = connection.cursor()

    # Ejecutar la consulta para obtener los productos desde la base de datos
    cursor.execute("SELECT nombre_producto FROM productos")

    # Obtener los resultados de la consulta
    productos = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    # Crear un nuevo frame para la lista de productos
    frame_productos = tk.Toplevel(ventana)
    frame_productos.title("Lista de Productos")
    # Definir la posición de la ventana secundaria (por ejemplo, x=100, y=100)
    x_pos = 500
    y_pos = 100
    frame_productos.geometry(f"+{x_pos}+{y_pos}")

    ##personalizar
    frame_productos.configure(bg="#1F618D")
    frame_productos.geometry("400x400")

    # Crear etiquetas para cada producto
    for i, producto in enumerate(productos):
        label_producto = Label(frame_productos, text=producto[0], font=("Arial", 12))
        label_producto.grid(row=i, column=0, padx=10, pady=5, sticky="w")

 # Crear botones para cada producto
    for i, producto in enumerate(productos):
        # Crear un botón para cada producto
        boton_producto = Button(frame_productos, text=producto[0], font=("Arial", 14, "bold"), bg="#AFEEEE", fg="#ffffff", command=lambda p=producto[0]: agregar_producto(p))
        boton_producto.grid(row=i, column=0, padx=10, pady=5, sticky="w")

def eliminar_producto(producto):
    # Eliminar el producto del carrito
    carrito.remove(producto)
    print(f"Producto eliminado del carrito: {producto}")
    print("Carrito actual:", carrito)
    actualizar_label_carrito()  # Actualiza el label del carrito
    actualizar_contenedor_azul()  # Actualiza el contenedor azul


def actualizar_contenedor_azul():
    # Limpiar el contenedor antes de actualizarlo con los productos seleccionados
    for widget in contenedor_azul.winfo_children():
        widget.destroy()

    # Mostrar los productos seleccionados como etiquetas en el contenedor azul
    for i, producto in enumerate(carrito):
        label_producto = Label(contenedor_azul, text=producto, font=("Arial", 12), bg="blue", fg="#ffffff")
        label_producto.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        # Mostrar los productos seleccionados como etiquetas y botones "X" en el contenedor azul
        for i, producto in enumerate(carrito):
            label_producto = Label(contenedor_azul, text=producto, font=("Arial", 12), bg="blue", fg="#ffffff")
            label_producto.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            # Crear botones "X" para eliminar productos del carrito
            boton_eliminar = Button(contenedor_azul, text="X", command=lambda p=producto: eliminar_producto(p))
            boton_eliminar.grid(row=i, column=1, padx=5, pady=5)

# Función para agregar un producto (puedes personalizar esta función según tus necesidades)
def agregar_producto(producto):
    # Agregar el producto al carrito
    carrito.append(producto)
    actualizar_contenedor_azul()
    actualizar_label_carrito()
    print(f"Producto agregado al carrito: {producto}")
    print("Carrito actual:", carrito)


def actualizar_label_carrito():
    # Crear una cadena para almacenar el contenido del carrito
    contenido_carrito = "Carrito:\n"

    # Crear un diccionario para contar la cantidad de cada producto
    conteo_productos = {}

    # Recorrer la lista del carrito
    for producto in carrito:
        # Si el producto ya está en el diccionario, aumentar el conteo
        if producto in conteo_productos:
            conteo_productos[producto] += 1
        else:
            conteo_productos[producto] = 1

    # Agregar la información al contenido del carrito
    for producto, cantidad in conteo_productos.items():
        if cantidad > 1:
            contenido_carrito += f"{producto} ({cantidad} unidades)\n"

        else:
            contenido_carrito += f"{producto}\n"

    # Actualizar el contenido del Label en el contenedor rojo
    label_carrito.config(text=contenido_carrito)





# Crea la ventana principal
ventana = Tk()
ventana.title("Ventas")
ventana.geometry("1200x700")
ventana.resizable(False,False)


# Cargar la imagen de fondo y redimensionarla
imagen_fondo = Image.open("../img/fondoventas.png")
imagen_fondo = imagen_fondo.resize((1200, 700), Image.LANCZOS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
# Agrega la imagen de fondo a un label
label_imagen = tk.Label(ventana, image=imagen_fondo)
label_imagen.pack(fill=tk.BOTH, expand=True)

# etiquetas
label1 = Label(ventana, bg="#ffffff", height=40, width=90)
label1.place(x=50, y=30)

# Crear el label
label2 = tk.Label(ventana, bg="#185791", height=40, width=60)

# Configurar el padding interno
label2.config(padx=20, pady=20)
# Configurar el borde
label2.config(bd=5, relief="raised")
# Colocar el label en la ventana
label2.place(x=700, y=30)

label3 = Label(ventana, bg="#185791", text="VENTA", font=100, fg="#ffffff")
label3.place(x=900, y=30)

label4 = Label(label2, bg="#e73a4b", height=3, width=60)
label4.place(x=15, y=100)

label5 = Label(label2, text="Producto", bg="#e73a4b", fg="#ffffff", font=50)
label5.place(x=15, y=110)

label6 = Label(label2, text="Cantidad", bg="#e73a4b", fg="#ffffff", font=50)
label6.place(x=240, y=110)

label7 = Label(label2, text="SubTotal", bg="#e73a4b", fg="#ffffff", font=50)
label7.place(x=340, y=110)

label8 = Label(label2, bg="#c4c4c4", height=30, width=60)
label8.place(x=15, y=137)

label9 = Label(label2, text="TOTAL", bg="#18358e", fg="#ffffff", font=100)
label9.place(x=15, y=600)

label10 = Label(label2, text="$$$$$$", bg="#18358e", fg="#ffffff", font=100)
label10.place(x=250, y=600)

botonpagar = tkinter.Button(label2, text="PAGAR", bg="#18358e", fg="#ffffff", font=100)
botonpagar.place(x=350, y=600)


# Crear el botón para mostrar la lista de productos
boton_mostrar_lista = Button(ventana, text="Mostrar Lista de Productos", command=mostrar_lista_productos)
boton_mostrar_lista.place(x=50, y=50)



# Crear un contenedor rojo en el centro de la ventana
contenedor_rojo = Frame(label2, bg="#ffffff", width=410, height=450)
contenedor_rojo.place(x=20, y=140)

# Crear el Label para mostrar la lista del carrito dentro del contenedor rojo
label_carrito = Label(contenedor_rojo, text="Carrito:\n", font=("Arial", 14), bg="#e73a4b", fg="#ffffff")
label_carrito.pack(padx=20, pady=20)

#crear contendor para colocar los productos seleccionados
contenedor_azul = Frame(ventana, bg="#ffffff",width=635,height=450)
contenedor_azul.place(x=50,y=150)



#Muestra la ventana
ventana.mainloop()