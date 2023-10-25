# Bibliotecas
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# Paleta de colores
c_blanco = "#ffffff"
c_gris = "#b8bab9"
c_gris_claro = "#e7e7e5"
c_rojo = "#e73a4b"
c_rojo_palido = "#c9636c"
c_azul = "#185791"
c_azul_claro = "#397bb8"
c_azul_palido = "#AFEEEE"


ventana = Tk()
ventana.title("Promociones")
ventana.geometry("1200x700")
ventana.resizable(False, False)

# Cargar la imagen de fondo y redimensionarla
imagen_fondo = Image.open("../img/promociones.jpg")
imagen_fondo = imagen_fondo.resize((1200, 700), Image.LANCZOS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

label_imagen = tk.Label(ventana, image=imagen_fondo)
label_imagen.pack(fill=tk.BOTH, expand=True)


ventana.mainloop()
