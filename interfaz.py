# Importamos las librerías
from tkinter import *
from customtkinter import *


# Configuración de la ventana
root = CTk()
root.geometry("600x500")
root.title("Interfaz")
root.config()

# Cargar el logo
logo = PhotoImage(file = "img/logo.png")

root.call("wm", "iconphoto", root._w, logo)
root.mainloop()
