from tkinter import Tk, Label, Button
from tkinter.ttk import Treeview
import tkinter.messagebox
import mysql.connector


class VentasViewer(Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventas")
        self.geometry("1200x700")

        # Titulo
        title = Label(self, text="Ventas", font="16")
        title.pack()

        # Tabla
        tablaVentas = Treeview(self, columns=("FechaVenta", "TotalCompra", "TipoPago", "Empleado",
                                              "TipoVenta"), show="headings")
        tablaVentas.heading("FechaVenta", text="Fecha de venta")
        tablaVentas.heading("TotalCompra", text="Total de la compra")
        tablaVentas.heading("TipoPago", text="Tipo de pago")
        tablaVentas.heading("Empleado", text="Empleado")
        tablaVentas.heading("TipoVenta", text="Tipo de venta")

        tablaVentas.column("FechaVenta", anchor="center")
        tablaVentas.column("TotalCompra", anchor="center")
        tablaVentas.column("TipoPago", anchor="center")
        tablaVentas.column("Empleado", anchor="center")
        tablaVentas.column("TipoVenta", anchor="center")

        tablaVentas.pack()

        tablaVentas.insert(parent="", index=0, values=("262545", "$23", "SI", "Rasputin", "Efectivo"))

    def insert_values(self, start_index: int = 1, maximum: int = 10, offset: int = 0):
        sql = (f"SELECT v.fecha_DE_VENTA, v.total_De_Compra, p.nombre, e.nombre, e.apellido_paterno,"
               f"e.apellido_materno, v.id_cliente INNER JOIN")




ventana = VentasViewer()
ventana.mainloop()