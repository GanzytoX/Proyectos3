# Bibliotecas
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from Crud.CRUD_Inventario import *


connection = mysql.connector.connect(
    user="u119126_pollos2LaVengazaDelPollo",
    host="174.136.28.78",
    port="3306",
    password="$ShotGunKin0805",
    database="u119126_pollos2LaVengazaDelPollo"
    )

ventana = Tk()
ventana.title("Inventario")
ventana.geometry("1200x700")
ventana.resizable(False, False)
ventana.iconbitmap("../img/logo.ico")

# Cargar la imagen de fondo
background_image = Image.open("../img/imagen_inventario.png")
background_image = ImageTk.PhotoImage(background_image, master=ventana)

# Crear un widget Label para mostrar la imagen de fondo
bgImage_label = tk.Label(ventana, image=background_image)
bgImage_label.place(relwidth=1, relheight=1)


ventana.mainloop()