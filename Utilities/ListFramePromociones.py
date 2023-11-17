import tkcalendar

from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
import tkinter as tk
from typing import Callable
from Crud.CRUDOfertas import *
from tkinter import ttk
from tkcalendar import Calendar

class ListFrame(tk.Frame):
    __image = None
    __text = str
    __object = None

    def __init__(self, master: AutomaticScrollableFrame, text: str, objeto):
        tk.Frame.__init__(self, master)
        self.grid()
        self.label = tk.Label(self, text=text)
        self.label.grid(row=0, column=0)
        self.object = objeto

    def addevento(self: tk.W,
                  sequence: str | None = ...,
                  func: Callable[[object], None] | None = ...):
        self.function = func
        super().bind(sequence, self.returnObject)
        self.label.bind(sequence, self.returnObject)

    def returnObject(self, event):
        self.function(self.object)


class CuadrotePromociones(tk.Frame):
    def __init__(self):
        super().__init__()
        self.connection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"

        )
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.config(padx=10,pady=10)
        # Para seleccionar el id de producto para enviarlo a la base de datos
        self.listaProdtexto = tk.Label(self, text="A que producto referencia la promocion: ", padx=30,pady=10).grid(column=0, row=0)
        self.listaProd = ttk.Combobox(self, state="readonly", values=self.getProductos()[1])
        self.listaProd.grid(column=0, row=1)
        #Para seleccionar el id del tipo de promocion y enviarlo a la base de datos
        self.listaTipoPromocionTexto = tk.Label(self,text="Que tipo de promocion es:",padx=30,pady=10).grid(column=1,row=0)
        self.listaTipoPromocion = ttk.Combobox(self, state= "readonly", values=self.getPromociones()[1])
        self.listaTipoPromocion.grid(column=1,row=1)

        #descripcion
        self.cuadroDescripcionTexto = tk.Label(self,text="Descripcion: ",padx=30,pady=10).grid(column=0,row=2)
        self.cuadroDescripcion = tk.Text(self, height=10,width=20)
        self.cuadroDescripcion.grid(column=0, row= 3)
        #fechas
        self.fechaInicioText = tk.Label(self, text="Fecha inicio: (AAAA/MM/DD)",pady=10,padx=30).grid(column=1,row=2)
        self.fechaInicio = tk.Entry(self)
        self.fechaInicio.bind("<Button-1>",self.crearCalendario)
        self.fechaInicio.grid(column=1, row=3)

        self.fechaFinalText = tk.Label(self, text="Fecha final: (AAAA/MM/DD)", pady=10, padx=30).grid(column=1, row=4)
        self.fechaFinal = tk.Entry(self)
        self.fechaFinal.bind("<Button-1>", self.crearCalendario)
        self.fechaFinal.grid(column=1,row=5)
        #elemento actual para editar
        self.current = -1

    def getProductos(self):
        script = "SELECT id_producto, nombre from producto where activo = 'V'"
        cursor = self.connection.cursor()
        cursor.execute(script)
        result = cursor.fetchall()
        nombres = []
        ids = []
        resultados = []
        #ids y nombres de productos separados
        for i in result:
            nombres.append(i[1])
            ids.append(i[0])
        resultados.append(ids)
        resultados.append(nombres)
        return resultados
    def getPromociones(self):
        connection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"

        )
        script = "SELECT id_tipo_promocion, nombre from tipo_de_promocion"
        cursor = connection.cursor()
        cursor.execute(script)
        result = cursor.fetchall()
        ids = []
        nombres = []
        resultados = []
        #separar ids y nombres para devolver un arreglo de arreglos
        for i in result:
            ids.append(i[0])
            nombres.append(i[1])
        resultados.append(ids)
        resultados.append(nombres)
        connection.close()
        return resultados

    def crearCalendario(self,event):
        self.calendario = tk.Tk()
        self.si = Calendar(self.calendario, day=10,month=11,year=2023)
        self.si.pack()
        botoncito = tk.Button(self.calendario,text="Ya", command=lambda: self.darFormato(event.widget))
        botoncito.pack()
        self.calendario.mainloop()


    def darFormato(self, entry:tk.Entry):
        entry.delete(0,tk.END)
        entry.insert(0, self.si.get_date())
        aformatear = entry.get()
        formato = aformatear.split("/")
        formateo = f"20{formato[2]}/{formato[0]}/{formato[1]}"
        entry.delete(0,tk.END)
        entry.insert(0,formateo)
        self.calendario.destroy()



