# Bibliotecas
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Crud.CRUD_Usuario import CrudEmpleado
import mysql.connector
from AdminMainMenu import AdminMainMenu

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
    user="u119126_pollos2LaVengazaDelPollo",
    host="174.136.28.78",
    port="3306",
    password="$ShotGunKin0805",
    database="u119126_pollos2LaVengazaDelPollo"
    )

# Función para iniciar sesión
def iniciarSesion():
    user = user_entry.get()
    password = password_entry.get()

    if user != "" and password != "":
        try:
            userManager = CrudEmpleado(connection)
            result, is_administrator, idU = userManager.iniciarSesion(user, password)

            if result:
                messagebox.showinfo("Mensaje de inicio de sesión", "Sesión iniciada con éxito")
                if is_administrator == 1:
                    adminWindow = AdminMainMenu(idU)
                    ventana.destroy()
                    adminWindow.mainloop()


                return
            else:
                messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrecto(s)")
                return

        except Exception as e:
            messagebox.showerror("Error de inicio de sesión", "ERROR: " + str(e))
            return

    messagebox.showerror("Error", "Debe rellenar todos los campos")

def limitar_caracteres(entry, max_chars):
    if len(entry.get()) > max_chars:
        entry.delete(max_chars, tk.END)

# Crear una ventana de inicio de sesión
ventana = Tk()
ventana.title("Inicio de sesión")
ventana.geometry("1200x700")
ventana.resizable(False, False)
ventana.iconbitmap("../img/logo.ico")


# Cargar la imagen de fondo
background_image = Image.open("../img/inicioDeSesion.png")
background_image = ImageTk.PhotoImage(background_image, master=ventana)

# Crear un widget Label para mostrar la imagen de fondo
bgImage_label = tk.Label(ventana, image=background_image)
bgImage_label.place(relwidth=1, relheight=1)  # Estirar la imagen para que cubra toda la ventana

# Crear un frame para los elementos de inicio de sesión
frame = tk.Frame(ventana, bg=c_gris_claro, padx=100, pady=100)
frame.pack(expand=True)

# Cargar la imagen del icono de foto de perfil y ajustar su tamaño (más pequeño)
icon_image = Image.open("../img/iconoFotoDePerfil.png")
icon_image = icon_image.resize((50, 50), Image.LANCZOS)
icon_image = ImageTk.PhotoImage(icon_image, master= ventana)

# Agregar la imagen en el frame, arriba de la etiqueta "Login User"
icon_label = tk.Label(frame, image=icon_image, bg=c_gris_claro)
icon_label.pack(pady=10)

# Etiqueta "Login User" en la parte superior en negritas
login_label = tk.Label(frame, text="Login User", bg=c_gris_claro, font=("Helvetica", 16, "bold"), justify="center")
login_label.pack()

# Cargar la imagen del logo y ajustar su tamaño
logo_image = Image.open("../img/logo.png")
logo_image = logo_image.resize((100, 100), Image.LANCZOS)  # Ajusta el tamaño aquí
logo_image = ImageTk.PhotoImage(logo_image, master=ventana)

# Agregar la imagen en la parte superior izquierda
logo_label = tk.Label(ventana, image=logo_image)
logo_label.place(x=20, y=20)  # Coordenadas para la posición de la imagen

# Etiqueta de usuario
user_label = tk.Label(frame, text="Usuario:", bg=c_gris_claro)
user_label.pack()

# Campo de entrada para el usuario
user_entry = tk.Entry(frame, width=30, bg=c_azul_palido)
user_entry.pack(pady=5)  # Espacio entre usuario y contraseña

# Llamar a la función limitar_caracteres cuando se escriba en el Entry
user_entry.bind("<KeyRelease>", lambda event, entry=user_entry, max_chars=10: limitar_caracteres(entry, max_chars))

# Etiqueta de contraseña
password_label = tk.Label(frame, text="Contraseña:", bg=c_gris_claro)
password_label.pack()

# Campo de entrada para la contraseña
password_entry = tk.Entry(frame, show="*", width=30, bg=c_azul_palido)
password_entry  .pack()

# Separación entre contraseña y el botón
separador2 = tk.Label(frame, text=" ", bg=c_gris_claro)
separador2.pack()

# Botón para iniciar sesión
log_in_button = tk.Button(frame, text="Iniciar Sesión", bg=c_azul, fg=c_blanco, command=iniciarSesion)
log_in_button.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
