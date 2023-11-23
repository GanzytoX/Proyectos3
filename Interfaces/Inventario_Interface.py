import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import ttk, simpledialog

# Paleta de colores
c_blanco = "#ffffff"
c_gris = "#b8bab9"
c_gris_claro = "#e7e7e5"
c_rojo = "#e73a4b"
c_rojo_palido = "#c9636c"
c_azul = "#185791"
c_azul_claro = "#397bb8"
c_azul_palido = "#AFEEEE"

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

        # Marco para contener los botones de actualizar, buscar y editar
        button_frame = tk.Frame(self.root)
        button_frame.place(relx=0.5, rely=0.05, anchor=tk.N)

        # Botón de actualización
        self.actualizar_button = tk.Button(button_frame, text="Actualizar Datos", bg=c_azul, fg=c_blanco, command=self.actualizar_datos)
        self.actualizar_button.pack(side=tk.LEFT, padx=5)

        # Botón de búsqueda
        self.buscar_button = tk.Button(button_frame, text="Buscar", bg=c_azul, fg=c_blanco, command=self.buscar_producto)
        self.buscar_button.pack(side=tk.LEFT, padx=5)

        # Botón de agregar producto
        self.agregar_button = tk.Button(button_frame, text="Agregar Producto", bg=c_azul, fg=c_blanco, command=self.agregar_producto)
        self.agregar_button.pack(side=tk.LEFT, padx=5)

        # Botón de eliminar producto
        self.eliminar_button = tk.Button(button_frame, text="Eliminar Producto", bg=c_rojo, fg=c_blanco, command=self.eliminar_producto)
        self.eliminar_button.pack(side=tk.LEFT, padx=5)

        # Botón de edición
        self.editar_button = tk.Button(button_frame, text="Editar Cantidad", bg=c_azul, fg=c_blanco, command=self.editar_cantidad_seleccionada)
        self.editar_button.pack(side=tk.LEFT, padx=5)

        # Crear Treeview con scrollbar
        self.tree = ttk.Treeview(self.root, columns=('Código', 'ID Producto', 'Nombre Producto', 'Unidad', 'Cantidad'), height=20)
        self.tree.place(relx=0.5, rely=0.4, anchor=tk.CENTER, relwidth=0.95)

        # Configuración de las columnas
        self.tree.column('#0', anchor=tk.CENTER, width=0)
        self.tree.column('#1', anchor=tk.CENTER, width=100)  # Código
        self.tree.column('#2', anchor=tk.CENTER, width=100)  # ID Producto
        self.tree.column('#3', anchor=tk.CENTER, width=125)  # Nombre Producto
        self.tree.column('#4', anchor=tk.CENTER, width=100)  # Unidad
        self.tree.column('#5', anchor=tk.CENTER, width=100)  # Cantidad

        # Encabezados de las columnas
        self.tree.heading('#0', text='*')
        self.tree.heading('#1', text='Código')
        self.tree.heading('#2', text='ID Producto')
        self.tree.heading('#3', text='Nombre Producto')
        self.tree.heading('#4', text='Unidad')
        self.tree.heading('#5', text='Cantidad')

        # Verificar si hay registros al iniciar
        if not self.hay_registros_en_inventario():
            tk.messagebox.showinfo("Información", "No hay registros en el inventario.")

        # Obtener datos de la base de datos y mostrar en la tabla
        # self.obtener_datos_de_bd()

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

    def hay_registros_en_inventario(self):
        # Verificar si hay registros en la tabla de inventario
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM inventario")
        cantidad_registros = cursor.fetchone()[0]
        return cantidad_registros > 0

    def buscar_producto(self):
        # Mostrar un cuadro de diálogo para ingresar el código del producto
        codigo_producto = simpledialog.askstring("Buscar Producto", "Ingrese el código del producto:")

        if codigo_producto:
            # Aquí implementa la lógica para buscar el producto en tu base de datos
            cursor = self.connection.cursor()
            cursor.execute("SELECT codigo, id_producto, nombre_producto, unidad, cantidad FROM inventario WHERE codigo = %s", (codigo_producto,))

            # Limpiar datos actuales en la tabla antes de actualizar
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insertar nuevos datos en la tabla
            for row in cursor.fetchall():
                codigo, id_producto, nombre_producto, unidad, cantidad = row
                self.tree.insert('', 'end', iid=codigo, values=(codigo, id_producto, nombre_producto, unidad, cantidad))

    def agregar_producto(self):
        nuevo_codigo = simpledialog.askstring("Agregar Producto", "Ingrese el nuevo código del producto:")
        nuevo_id_producto = simpledialog.askstring("Agregar Producto", "Ingrese el nuevo ID del producto:")
        nuevo_nombre_producto = simpledialog.askstring("Agregar Producto", "Ingrese el nombre del nuevo producto:")
        nueva_unidad = simpledialog.askstring("Agregar Producto", "Ingrese la nueva unidad del producto:")
        nueva_cantidad = simpledialog.askinteger("Agregar Producto", "Ingrese la cantidad inicial del producto:")

        if nuevo_codigo and nuevo_id_producto and nuevo_nombre_producto and nueva_unidad and nueva_cantidad is not None:
            # Verificar si el código del producto ya existe en la base de datos
            cursor = self.connection.cursor()
            cursor.execute("SELECT codigo FROM inventario WHERE codigo = %s", (nuevo_codigo,))
            existing_code = cursor.fetchone()

            # Verificar si el ID del producto ya existe en la base de datos
            cursor.execute("SELECT id_producto FROM inventario WHERE id_producto = %s", (nuevo_id_producto,))
            existing_id = cursor.fetchone()

            if existing_code:
                tk.messagebox.showerror("Error", f"El código {nuevo_codigo} ya existe en la base de datos.")
            elif existing_id:
                tk.messagebox.showerror("Error", f"El ID {nuevo_id_producto} ya existe en la base de datos.")
            else:
                # Insertar el nuevo producto en la base de datos
                cursor.execute("INSERT INTO inventario (codigo, id_producto, nombre_producto, unidad, cantidad) VALUES (%s, %s, %s, %s, %s)",
                            (nuevo_codigo, nuevo_id_producto, nuevo_nombre_producto, nueva_unidad, nueva_cantidad))
                self.connection.commit()

                self.obtener_datos_de_bd()

    def eliminar_producto(self):
        # Obtener la fila seleccionada
        selected_item = self.tree.selection()
        if not selected_item:
            return  # No hay ninguna fila seleccionada

        # Obtener el ID del producto seleccionado
        id_producto = self.tree.item(selected_item, 'values')[1]

        # Mostrar un cuadro de diálogo de confirmación antes de eliminar
        confirmacion = tk.messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de eliminar el producto con ID {id_producto}?")

        if confirmacion:
            # Eliminar el producto de la base de datos
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM inventario WHERE id_producto = %s", (id_producto,))
            self.connection.commit()

            # Eliminar la fila de la tabla en la interfaz gráfica
            self.tree.delete(selected_item)

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
            # Verificar que la nueva cantidad no sea inferior a 0
            if nueva_cantidad < 0:
                tk.messagebox.showwarning("Advertencia", "La cantidad no puede ser inferior a 0.")
            else:
                # Actualizar la cantidad en la base de datos
                cursor = self.connection.cursor()
                cursor.execute("UPDATE inventario SET cantidad = %s WHERE nombre_producto = %s",
                               (nueva_cantidad, nombre_producto))
                self.connection.commit()

                # Actualizar la cantidad en la tabla
                self.tree.set(selected_item, '#5', nueva_cantidad)

    def actualizar_datos(self):
        self.obtener_datos_de_bd()