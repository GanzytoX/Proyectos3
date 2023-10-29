# Importa la biblioteca tkinter
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Paleta de colores
c_blanco = "#ffffff"
c_gris = "#b8bab9"
c_gris_claro = "#e7e7e5"
c_rojo = "#e73a4b"
c_rojo_palido = "#c9636c"
c_azul = "#185791"
c_azul_claro = "#397bb8"
c_azul_palido = "#AFEEEE"

# Función para realizar la búsqueda
def buscar_promociones():
    # Obtiene el texto ingresado en el Entry
    texto_busqueda = entry_busqueda.get()
    # Aquí deberías realizar la búsqueda de promociones con el texto ingresado
    # y mostrar los resultados en el Listbox, incluyendo los precios
    resultados = [("2 pzs. de Pollo", "$10.99"), ("1 pz + 1/4 de Pollo", "$7.99")]
    # Borra el contenido actual del Listbox
    listbox_promociones.delete(0, tk.END)
    # Agrega los resultados al Listbox con sus precios
    for promocion, precio in resultados:
        listbox_promociones.insert(tk.END, f"{promocion} - {precio}")

# Función para agregar promoción
def agregar_promocion():
    texto_busqueda = entry_busqueda.get()
    listbox_promociones.insert(tk.END, f"{texto_busqueda}")
    pass

# Función para actualizar promociones
def actualizar_promociones():

    pass

# Crea la ventana principal
ventana = Tk()
ventana.title("Promociones")
ventana.geometry("1200x700")
ventana.resizable(False, False)

# Cargar la imagen de fondo y redimensionarla
imagen_fondo = Image.open("../img/promociones.jpg")
imagen_fondo = imagen_fondo.resize((1200, 700), Image.LANCZOS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Agrega la imagen de fondo a un label
label_imagen = tk.Label(ventana, image=imagen_fondo)
label_imagen.pack(fill=tk.BOTH, expand=True)

# Crea un frame a la izquierda del frame
frame_pequeno = tk.Frame(ventana, bg=c_gris, width=800, height=400)
frame_pequeno.place(relx=0.25, rely=0.5, anchor=tk.W)

# Crea un contenedor para Entry y Botón
contenedor_entry_boton = tk.Frame(frame_pequeno, bg=c_gris)
contenedor_entry_boton.pack(side=tk.TOP, padx=10, pady=10)

# Crea un Entry para la búsqueda
entry_busqueda = tk.Entry(contenedor_entry_boton)
entry_busqueda.pack(side=tk.LEFT, padx=(0, 10))  # Agrega espacio a la derecha del Entry

# Crea un botón para activar la búsqueda
boton_buscar = tk.Button(contenedor_entry_boton, text="Buscar", command=buscar_promociones)
boton_buscar.pack(side=tk.LEFT)

# Crea un Listbox para mostrar las promociones
listbox_promociones = tk.Listbox(frame_pequeno)
listbox_promociones.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Crea un contenedor para los botones "Agregar Promoción" y "Actualizar"
contenedor_botones = tk.Frame(frame_pequeno, bg=c_gris)
contenedor_botones.pack(side=tk.TOP, padx=10, pady=10)

# Crea un botón "Agregar Promoción" debajo del Listbox
boton_agregar_promocion = tk.Button(contenedor_botones, text="Agregar Promoción", command=agregar_promocion)
boton_agregar_promocion.pack(side=tk.LEFT)

# Crea un espacio horizontal entre los botones
espacio_horizontal = tk.Label(contenedor_botones, text=" ", bg=c_gris)
espacio_horizontal.pack(side=tk.LEFT, padx=10)  # Espacio horizontal entre los botones

# Crea un botón "Actualizar"
boton_actualizar = tk.Button(contenedor_botones, text="Actualizar", command=actualizar_promociones)
boton_actualizar.pack(side=tk.LEFT)


ventana.mainloop()
