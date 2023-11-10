from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
import tkinter as tk
from typing import Callable
from Crud.CRUDOfertas import *
from tkinter import ttk


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
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=4)

        # Para selectionar el id de producto para enviarlo a la base de datos
        self.listaProdtexto = tk.Label(self, text="A que producto referencia la promocion: ").grid(column=0, row=0)
        self.listaProd = ttk.Combobox(self, state="readonly", values=self.getProductos())
        self.listaProd.grid(column=0, row=1)
        print(self.getProductos())

    def getProductos(self):
        connection = mysql.connector.connect(
            user="sql5660121",
            host="sql5.freesqldatabase.com",
            port="3306",
            password="GWes4WXpXH",
            database="sql5660121"

        )
        script = "SELECT nombre from producto"
        cursor = connection.cursor()
        cursor.execute(script)
        result = cursor.fetchall()
        resultados = []
        for i in result:
            resultados.append(i[0])

        return resultados
