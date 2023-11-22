from tkinter import Tk, Label, Button, Scrollbar, Frame, Toplevel
from tkinter.ttk import Treeview, Style
import tkinter.messagebox
import mysql.connector
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
from Ventas_Interface import ventaFrame


class VentasViewer(Tk):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.__cursor = self.__conection.cursor()

        self.title("Ventas")

        # Titulo
        title = Label(self, text="Ventas", font="16")
        title.pack()

        # Frame
        frameTable = Frame(self)
        frameTable.pack()

        # Index de la paginación
        self.__pagina = 0
        self.__cantidad_elementos = 15

        # Tabla
        self.__tablaVentas = Treeview(frameTable, columns=("id", "FechaVenta", "TotalCompra", "TipoPago", "Empleado_Nombre",
                                              "Empleado_Apellido_P", "Empleado_Apellido_M", "TipoVenta"), show="headings", height=self.__cantidad_elementos)

        self.__tablaVentas.heading("id", text="Id_venta")
        self.__tablaVentas.heading("FechaVenta", text="Fecha de venta")
        self.__tablaVentas.heading("TotalCompra", text="Total de la compra")
        self.__tablaVentas.heading("TipoPago", text="Tipo de pago")
        self.__tablaVentas.heading("Empleado_Nombre", text="Nombre del Empleado")
        self.__tablaVentas.heading("Empleado_Apellido_P", text="Apellido Paterno")
        self.__tablaVentas.heading("Empleado_Apellido_M", text="Apellido Materno")
        self.__tablaVentas.heading("TipoVenta", text="Tipo de venta")

        self.__tablaVentas.column("id", anchor="center", width=5)
        self.__tablaVentas.column("FechaVenta", anchor="center")
        self.__tablaVentas.column("TotalCompra", anchor="center")
        self.__tablaVentas.column("TipoPago", anchor="center")
        self.__tablaVentas.column("Empleado_Nombre", anchor="center")
        self.__tablaVentas.column("TipoVenta", anchor="center")
        self.__tablaVentas.column("Empleado_Apellido_P", anchor="center")
        self.__tablaVentas.column("Empleado_Apellido_M", anchor="center")

        #Que haya rayas de diferentes colores
        self.__tablaVentas.tag_configure("par", background="white")
        self.__tablaVentas.tag_configure("impar", background="#d3eaf2")
        s =Style()
        s.configure('Treeview', rowheight=40)

        self.__tablaVentas.pack(side="left", padx=10, pady=15)

        # ScrollBar
        self.__scroll = Scrollbar(frameTable, command=self.__tablaVentas.yview)
        self.__scroll.pack(fill="both", side="right")
        self.__tablaVentas.config(yscrollcommand=self.__scroll.set)

        self.__insert_values()

        # Frame de la paginación
        frame_paginacion = Frame(self)
        frame_paginacion.pack()

        # Botones de la paginación
        self.__buton_atras = Button(frame_paginacion, text="No", background="#d3eaf2", state="disabled",
                                    command=self.__previous)
        self.__buton_adelante = Button(frame_paginacion, text="Si", background="#d3eaf2", command=self.__next)

        self.__buton_atras.pack(side="left", padx=50)
        self.__buton_adelante.pack(side="right", padx=50)

        # Ver si va a haber siguiente pagina
        cuenta = self.__count_ventas()
        if cuenta < self.__cantidad_elementos:
            self.__buton_adelante.config(state="disabled")

        # Evento por si selecciona algo de la tabla
        self.bind("<Button-3>", self.__clear_table)
        self.__tablaVentas.bind("<<TreeviewSelect>>", self.__dar_detalles)


        # Pop up de cuando abres una venta
        self.__pop_window = None

    def __insert_values(self, maximum: int = 15, offset: int = 0):
        self.__conection.commit()
        sql = (f"SELECT v.id_venta, v.fecha_De_Venta, v.total_De_Compra, p.nombre, e.nombre, e.apellido_paterno,"
               f"e.apellido_materno, v.id_cliente FROM venta as v INNER JOIN pago as p ON p.id_pago = v.id_pago "
               f"INNER JOIN empleado as e ON e.id_empleado = v.id_empleado ORDER BY v.fecha_De_Venta DESC, id_venta DESC "
               f"LIMIT {maximum} OFFSET {offset}")
        self.__cursor.execute(sql)
        ventas = self.__cursor.fetchall()
        i = 1

        for venta in ventas:
            if venta[7] is None:
                agregar = (venta[0], venta[1], f"${venta[2]}", venta[3], venta[4], venta[5], venta[6], "En caja")
            else:
                agregar = (venta[0], venta[1], f"${venta[2]}", venta[3], venta[4], venta[5], venta[6], "A domicilio")
            if i % 2 == 0:
                self.__tablaVentas.insert(parent="", values=agregar, index=tkinter.END, tags="par")
            else:
                self.__tablaVentas.insert(parent="", values=agregar, index=tkinter.END, tags="impar")
            i += 1

    def __limpiar_datos(self):
        # Eliminar todas las filas de la tabla
        for i in self.__tablaVentas.get_children():
            self.__tablaVentas.delete(i)

    def __next(self):
        self.__pagina += 1
        self.__limpiar_datos()
        self.__insert_values(maximum=self.__cantidad_elementos, offset=self.__pagina * self.__cantidad_elementos)

        # Ver si va a haber siguiente pagina
        cuenta = self.__count_ventas()
        if cuenta < self.__cantidad_elementos * (self.__pagina+1):
            self.__buton_adelante.config(state="disabled")
        self.__buton_atras.config(state="normal")

    def __previous(self):
        self.__pagina -= 1
        self.__limpiar_datos()
        self.__insert_values(maximum=self.__cantidad_elementos, offset=self.__pagina * self.__cantidad_elementos)

        if self.__pagina == 0:
            self.__buton_atras.config(state="disabled")
        self.__buton_adelante.config(state="normal")


    def __count_ventas(self) -> int:
        sql = "SELECT COUNT(*) FROM venta"
        self.__conection.commit()
        self.__cursor.execute(sql)
        cuenta = self.__cursor.fetchone()
        return cuenta[0]

    def __dar_detalles(self, event):
        if self.__pop_window is not None:
            self.__pop_window.destroy()

        id_element = self.__tablaVentas.item(self.__tablaVentas.selection()[0])["values"][0]

        # Configurar la ventana pop up del desglose
        self.__pop_window = Toplevel(self)
        self.__pop_window.resizable(False, False)

        texto_titulo = f"Desglose de la venta {id_element}"

        # Titulo de la pagina
        label_titulo = Label(self.__pop_window, text=texto_titulo, font="20")
        label_titulo.pack(pady=10)

        # Colocar los elementos de la BD en la tabla de desglose
        detalles = AutomaticScrollableFrame(self.__pop_window, width=350)

        self.__conection.commit()
        sql = ("SELECT p.nombre, vp.cantidad , vp.subtotal, vp.id_producto FROM venta_producto AS vp "
               f"INNER JOIN producto AS p ON p.id_producto = vp.id_producto WHERE vp.id_venta = {id_element}")

        self.__cursor.execute(sql)
        productos = self.__cursor.fetchall()

        for producto in productos:
            detalles.add(ventaFrame(detalles, producto[0], producto[1], 0.0, producto[3]))

        detalles.pack(padx=5, pady=(0, 10))

    def __clear_table(self, event=None):
        for item in self.__tablaVentas.selection():
            self.__tablaVentas.selection_remove(item)


ventana = VentasViewer()
ventana.mainloop()
