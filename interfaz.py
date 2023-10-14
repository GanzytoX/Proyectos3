# Importamos las librerías y componentes
from Widgets import *
from tkinter import *
from PIL import Image, ImageTk


# Paleta de colores
c_gris_claro = "#e7e7e5"
c_rojo = "#e73a4b"
c_gris = "#b8bab9"
c_azul = "#185791"
c_rojo_palido = "#c9636c"
c_blanco = "#ffffff"

# Ventana de inicio de sesión
ventana = Tk()
ventana.title("Inicio de sesión")
ventana.geometry("1200x700")
ventana.resizable(False, False)
ventana.iconbitmap("img/logo.ico")

# Fondo
imagen_fondo = Image.open("img/inicioDeSesion.png")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Creamos un widget Label para mostrar la imagen de fondo
label_imagen = Label(ventana, image=imagen_fondo)
label_imagen.place(relwidth=1, relheight=1)  # Estirar la imagen para que cubra toda la ventana

# Creamos el frame
marco = Frame(ventana, bg=c_gris_claro)
marco.grid(row=0, column=0, sticky='nsew', padx=450, pady=150)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)


ventana.mainloop()