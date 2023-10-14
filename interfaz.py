# Importamos las librerías
from customtkinter import *
from Widgets import *
from tkinter import *


# Paleta de colores
c_gris_claro = "#e7e7e5"
c_rojo = "#e73a4b"
c_gris = "#b8bab9"
c_azul = "#185791"
c_rojo_palido = "#c9636c"
c_blanco = "#ffffff"

# Configuración ventana
ventana = Window("Inicio de sesión", "1200x700")
ventana.setBackgroundImage("img/inicioDeSesion.png")
ventana.iconbitmap("img/logo.ico")

frame = CTkFrame(ventana, bg_color="gray")
frame.place(x=ventana.winfo_width() /2, y=ventana.winfo_height() /10, anchor=CENTER)

button = CTkButton(ventana)

ventana.mainloop()