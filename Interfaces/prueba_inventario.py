import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import ttk, simpledialog

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario")
        self.root.geometry("1200x700")
        self.root.resizable(False, False)
        self.root.iconbitmap("../img/logo.ico")

        # Conectar a la base de datos
        self.connection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )

        # Cargar la imagen de fondo
        try:
            background_image = Image.open("../img/imagen_inventario.png")
            background_image = ImageTk.PhotoImage(background_image, master=self.root)

            # Crear un widget Label para mostrar la imagen de fondo
            bgImage_label = tk.Label(self.root, image=background_image)
            bgImage_label.image = background_image
            bgImage_label.place(x=0, y=0, relwidth=1, relheight=1)

        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        # Marco para contener los botones de actualizar y editar
        button_frame = tk.Frame(self.root)
        button_frame.place(relx=0.5, rely=0.05, anchor=tk.N)  # Ubicar en la parte superior centrada

        # Botón de actualización
        self.actualizar_button = tk.Button(button_frame, text="Actualizar Datos", command=self.actualizar_datos)
        self.actualizar_button.pack(side=tk.LEFT)

        # Botón de edición
        self.editar_button = tk.Button(button_frame, text="Editar Cantidad", command=self.editar_cantidad_seleccionada)
        self.editar_button.pack(side=tk.LEFT, padx=5)

        # Crear Treeview con scrollbar
        self.tree = ttk.Treeview(self.root, columns=('Código', 'ID Producto', 'Nombre Producto', 'Unidad', 'Cantidad'), height=20)
        self.tree.place(relx=0.5, rely=0.4, anchor=tk.CENTER)  # Ubicar debajo de los botones y centrada verticalmente

        # Configuración de las columnas
        self.tree.column('#0', anchor=tk.CENTER, width=0)
        self.tree.column('#1', anchor=tk.CENTER, width=100)  # Código
        self.tree.column('#2', anchor=tk.CENTER, width=100)  # ID Producto
        self.tree.column('#3', anchor=tk.CENTER, width=100)  # Nombre Producto
        self.tree.column('#4', anchor=tk.W, width=100)  # Unidad
        self.tree.column('#5', anchor=tk.CENTER, width=100)  # Cantidad

        # Encabezados de las columnas
        self.tree.heading('#0', text='*')
        self.tree.heading('#1', text='Código')
        self.tree.heading('#2', text='ID Producto')
        self.tree.heading('#3', text='Nombre Producto')
        self.tree.heading('#4', text='Unidad')
        self.tree.heading('#5', text='Cantidad')

        # Obtener datos de la base de datos y mostrar en la tabla
        self.obtener_datos_de_bd()

    def obtener_datos_de_bd(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT codigo, id_producto, nombre_producto, unidad, cantidad FROM inventario")

        # Limpiar datos actuales en la tabla antes de actualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar nuevos datos en la tabla
        for row in cursor.fetchall():
            codigo, id_producto, nombre_producto, unidad, cantidad = row
            self.tree.insert('', 'end', iid=codigo,
                             values=(codigo, id_producto, nombre_producto, unidad, cantidad))

    def editar_cantidad_seleccionada(self):
        # Obtener la fila seleccionada
        selected_item = self.tree.selection()
        if not selected_item:
            return  # No hay ninguna fila seleccionada

        # Obtener el nombre del producto y la cantidad actual
        nombre_producto = self.tree.item(selected_item, 'values')[2]
        cantidad_actual = self.tree.item(selected_item, 'values')[4]

        # Mostrar un cuadro de diálogo para que el usuario ingrese la nueva cantidad
        nueva_cantidad = simpledialog.askinteger("Editar Cantidad",
                                                 f"Editar cantidad para el producto '{nombre_producto}':",
                                                 initialvalue=cantidad_actual)

        if nueva_cantidad is not None:
            # Actualizar la cantidad en la base de datos
            cursor = self.connection.cursor()
            cursor.execute("UPDATE inventario SET cantidad = %s WHERE nombre_producto = %s",
                           (nueva_cantidad, nombre_producto))
            self.connection.commit()

            # Actualizar la cantidad en la tabla
            self.tree.set(selected_item, '#5', nueva_cantidad)

    def actualizar_datos(self):
        self.obtener_datos_de_bd()

