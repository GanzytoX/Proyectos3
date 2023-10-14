# Configuración de la ventana
# root = CTk()
# root.geometry("600x500")
# root.title("Interfaz")
# root.config()

# # Cargar el logo
# logo = PhotoImage(file = "img/logo.png")

# root.call("wm", "iconphoto", root._w, logo)
# root.mainloop()

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

# ventana = Tk()
# ventana.geometry("1200x700")
# ventana.title("Inicio de Sesión")

ventana = Window("Inicio de sesión", "1200x700")
ventana.setBackgroundImage("img/inicioDeSesion.png")
ventana.iconbitmap("img/logo.jpg")

frame = CTkFrame(ventana, bg_color="gray")
frame.place(x=ventana.winfo_width() /2, y=ventana.winfo_height() /10, anchor=CENTER)

button = CTkButton(ventana)

ventana.mainloop()