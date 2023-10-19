# Bibliotecas
import subprocess
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Crud.CRUD_Usuario import CrudEmpleado
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


# Función para abrir INTERFAZ_DE_PRUEBA.py
# def openMain():
#     # Utiliza subprocess para ejecutar el archivo (nombre del archivo)
#     subprocess.Popen(["python", "(archivo_a_abrir)"], shell=True)
#     print("Ventana abierta")


# Importo el Crud Usuario para poder hacer inicio de sesion y le paso un conection, o sea coneccion a la BD
conection = mysql.connector.connect(
        user="root",
        host="localhost",
        port="3307",
        database="pollosexpress"
    )
userManager = CrudEmpleado(conection)

# Funcion para poner en marcha el inicio de sesion
def iniciarSesion():
    user = usuario_entry.get()
    password = contrasena_entry.get()

    if user != "" and password != "":
        try:
            result = userManager.iniciarSesion(user, password)
            if result[0]:
                messagebox.showinfo("Message", "Iniciando sesión")
                if result[1]:
                    print("Es admin")

                else:
                    print("NO Es admin")
                return
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            return
        except:
            messagebox.showerror("Error", "Usuario no registrado")
            return 

    messagebox.showerror("Error", "Rellene los campos por favor")



# Crear una ventana de inicio de sesión
ventana = Tk()
ventana.title("Inicio de sesión")
ventana.geometry("1200x700")
ventana.resizable(False, False)

# Cargar la imagen de fondo
imagen_fondo = Image.open("../img/inicioDeSesion.png")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget Label para mostrar la imagen de fondo
label_imagen = tk.Label(ventana, image=imagen_fondo)
label_imagen.place(relwidth=1, relheight=1)  # Estirar la imagen para que cubra toda la ventana

# Crear un frame para los elementos de inicio de sesión
frame = tk.Frame(ventana, bg=c_gris_claro, padx=100, pady=100)
frame.pack(expand=True)

# Cargar la imagen del icono de foto de perfil y ajustar su tamaño (más pequeño)
icono_imagen = Image.open("../img/iconoFotoDePerfil.png")
icono_imagen = icono_imagen.resize((50, 50), Image.LANCZOS)  # Ajusta el tamaño aquí
icono_imagen = ImageTk.PhotoImage(icono_imagen)

# Agregar la imagen en el frame, arriba de la etiqueta "Login User"
icono_label = tk.Label(frame, image=icono_imagen, bg=c_gris_claro)
icono_label.pack(pady=10)

# Etiqueta "Login User" en la parte superior en negritas
login_label = tk.Label(frame, text="Login User", bg=c_gris_claro, font=("Helvetica", 16, "bold"), justify="center")
login_label.pack()

# Cargar la imagen del logo y ajustar su tamaño
logo_imagen = Image.open("../img/logo.png")
logo_imagen = logo_imagen.resize((100, 100), Image.LANCZOS)  # Ajusta el tamaño aquí
logo_imagen = ImageTk.PhotoImage(logo_imagen)

# Agregar la imagen en la parte superior izquierda
logo_label = tk.Label(ventana, image=logo_imagen)
logo_label.place(x=20, y=20)  # Coordenadas para la posición de la imagen

# Etiqueta de usuario
usuario_label = tk.Label(frame, text="Usuario:", bg=c_gris_claro)
usuario_label.pack()

# Campo de entrada para el usuario
usuario_entry = tk.Entry(frame, width=30, bg=c_azul_palido)
usuario_entry.pack(pady=5)  # Espacio entre usuario y contraseña

# Etiqueta de contraseña
contrasena_label = tk.Label(frame, text="Contraseña:", bg=c_gris_claro)
contrasena_label.pack()

# Campo de entrada para la contraseña
contrasena_entry = tk.Entry(frame, show="*", width=30, bg=c_azul_palido)
contrasena_entry.pack()

# Separación entre contraseña y el botón
separador2 = tk.Label(frame, text=" ", bg=c_gris_claro)
separador2.pack()

# Botón para iniciar sesión
iniciar_sesion_button = tk.Button(frame, text="Iniciar Sesión", bg=c_azul, fg=c_blanco, command=iniciarSesion)
iniciar_sesion_button.pack(pady=10)


# Ejecutar la ventana
ventana.mainloop()
