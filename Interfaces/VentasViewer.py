from tkinter import Tk, Label, Button
from tkinter.ttk import Treeview
import tkinter.messagebox
import mysql.connector


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

        # Tabla
        self.__tablaVentas = Treeview(self, columns=("FechaVenta", "TotalCompra", "TipoPago", "Empleado_Nombre",
                                              "Empleado_Apellido_P", "Empleado_Apellido_M", "TipoVenta"), show="headings")

        self.__tablaVentas.heading("FechaVenta", text="Fecha de venta")
        self.__tablaVentas.heading("TotalCompra", text="Total de la compra")
        self.__tablaVentas.heading("TipoPago", text="Tipo de pago")
        self.__tablaVentas.heading("Empleado_Nombre", text="Nombre del Empleado")
        self.__tablaVentas.heading("Empleado_Apellido_P", text="Apellido Paterno")
        self.__tablaVentas.heading("Empleado_Apellido_M", text="Apellido Materno")
        self.__tablaVentas.heading("TipoVenta", text="Tipo de venta")

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

        self.__tablaVentas.pack()

        self.__tablaVentas.insert(parent="", index=0, values=("262545", "$23", "SI", "Rasputin", "Efectivo"))

        self.__insert_values()

    def __insert_values(self, maximum: int = 10, offset: int = 0):
        self.__conection.commit()
        sql = (f"SELECT v.fecha_De_Venta, v.total_De_Compra, p.nombre, e.nombre, e.apellido_paterno,"
               f"e.apellido_materno, v.id_cliente FROM venta as v INNER JOIN pago as p ON p.id_pago = v.id_pago "
               f"INNER JOIN empleado as e ON e.id_empleado = v.id_empleado ORDER BY v.fecha_De_Venta DESC "
               f"LIMIT {maximum} OFFSET {offset}")
        self.__cursor.execute(sql)
        ventas = self.__cursor.fetchall()
        i = 1
        for venta in ventas:
            if venta[6] is None:
                agregar = (venta[0], f"${venta[1]}", venta[2], venta[3], venta[4], venta[5], "En caja")
            else:
                agregar = (venta[0], f"${venta[1]}", venta[2], venta[3], venta[4], venta[5], "A domicilio")

            if i % 2 == 0:
                self.__tablaVentas.insert(parent="", values=agregar, index=tkinter.END, tags="par")
            else:
                self.__tablaVentas.insert(parent="", values=agregar, index=tkinter.END, tags="impar")
            i += 1


ventana = VentasViewer()
ventana.mainloop()