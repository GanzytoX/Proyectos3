import time
from tkinter import *
from tkinter import messagebox
import mysql.connector

class GastoRapido(Tk):

    def __init__(self, idU):
        super().__init__()
        self.title("Gastos")
        self.geometry("370x500")
        self.grid_columnconfigure(0, weight=2)
        self.resizable(False, False)

        self.__idU = idU

        self.__title = Label(self, text="Agregar gasto")
        self.__title.grid(column=0, row=0, pady=(0, 10))

        self.__titulo = Label(self, text="Título")
        self.__titulo.grid(column=0, row=1, sticky="W", padx=10)

        self.__title_entry = Entry(self)
        self.__title_entry.grid(column=0, row=2, pady=(0, 10), sticky="W", padx=10)

        self.__descripcion = Label(self, text="Descripción")
        self.__descripcion.grid(column=0, row=3, sticky="W", padx=10)

        self.__descripcion_entry = Text(self, height=15)
        self.__descripcion_entry.grid(column=0, row=4, pady=(0, 10), sticky="W", padx=10)

        self.__monto = Label(self, text="Monto")
        self.__monto.grid(column=0, row=5, sticky="W", padx=10)

        self.__monto_entry = Entry(self)
        self.__monto_entry.grid(column=0, row=6, pady=(0, 10), sticky="W", padx=10)

        self.__button = Button(self, text="Enviar", command=self.__subir)
        self.__button.grid(column=0, row=7, pady=(15, 5))

    def __subir(self):
        conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        cursor = conection.cursor()

        actual_time = time.localtime()
        timeFormatted = time.strftime("%Y/%m/%d %H:%M:%S", actual_time)
        print(timeFormatted)

        try:
            monto = float(self.__monto_entry.get())
        except ValueError as e:
            messagebox.showerror("Error", "El monto ingresado es incorrecto")
        else:
            sql = "INSERT INTO gasto(titulo, descripcion, monto, fecha, id_empleado) VALUES (%s, %s, %s, %s, %s);"
            values = (self.__title_entry.get(), self.__descripcion_entry.get(0.0, END),
                      monto, timeFormatted, self.__idU)
            cursor.execute(sql, values)
            conection.commit()
            messagebox.showinfo("Listo", "El gasto se ha agregado")
        finally:
            conection.close()
            self.__title_entry.delete(0, END)
            self.__descripcion_entry.delete("1.0", END)
            self.__monto_entry.delete(0, END)
            return


gasto = GastoRapido(1)
gasto.mainloop()