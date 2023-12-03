from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
import tkinter as tk
from PIL import Image, ImageTk
from typing import Callable

class ListFrame(tk.Frame):
    __image = None
    __text = str
    object = None

    def __init__(self, master, text: str, objet, imageroute: str, imageSize: (int, int)):
        super().__init__(master=master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        imagen_raw = Image.open(imageroute)
        imagen_raw.thumbnail(imageSize)

        self.__image = tk.Label(self)
        imagen_tk = ImageTk.PhotoImage(imagen_raw, master=self.__image)
        self.__image.configure(image=imagen_tk)
        self.__image.image = imagen_tk
        self.__image.grid(column=0, row=0)
        self.__text = tk.Label(self, height=4, justify="left", text=text)
        self.__text.grid(column=1, row=0, sticky="W")
        self.object = objet

        imagen_raw.close()

    def addEvent(
            self: tk.W,
            sequence: str | None = ...,
            func: Callable[[object], None] | None = ...):
        self.__function = func
        string = super().bind(sequence, self.__returnObject)
        self.__image.bind(sequence, self.__returnObject)
        self.__text.bind(sequence, self.__returnObject)
        return string

    def __returnObject(self, event):
        self.__function(self.object)


class NoImageFrame(ListFrame):
    def __init__(self, master, text: str, objet):
        super().__init__(master, text, objet, "../img/dot.png", (10, 10))


class ImageFrame(ListFrame):
    def __init__(self, master, text: str, objet, imageroute: str):
        super().__init__(master, text, objet, imageroute, (60, 60))


class ventaFrame(tk.Frame):
    def __init__(self, master:any, nombre,cantidad,precio, idP):
        super().__init__(master, width=200, height=20, bg="#f0f0f0")
        super().columnconfigure(index=0, weight=2)
        super().columnconfigure(index=1, weight=2)
        super().columnconfigure(index=2, weight=2)
        self.__nombre = nombre
        self.__subtotal = float(precio)
        self.__cantidad = float(cantidad)
        self.idP = idP
        if len(nombre) > 20:
            aescribirNombre = nombre[0:20] + "..."
        else:
            aescribirNombre = nombre
        self.nombreLabel = tk.Label(self, text=f"{aescribirNombre}",padx=10)
        self.nombreLabel.grid(column=0, row=0, sticky="w")
        self.cantidadLabel = tk.Label(self, text=f"{cantidad}",padx=25)
        self.cantidadLabel.grid(column=2, row=0, sticky="ew")
        self.precioLabel = tk.Label(self,text=f"${self.__subtotal}",padx=20)
        self.precioLabel.grid(column=3, row=0, sticky="e")

    def get_nombre(self):
        return self.__nombre

    def set_subtotal(self, value: float):
        if isinstance(value, float):
            if value >= 0:
                self.__subtotal = value
                self.precioLabel.config(text=f"${value}")
            else:
                raise ValueError("El subtotal no puede ser negativo")
        else:
            raise ValueError("El subtotal debe ser un numero")

    def set_cantidad(self, value: float):
        if isinstance(value, float) or isinstance(value, int):
            if value >= 0:
                self.__cantidad = value
                self.cantidadLabel.config(text=f"{value}")
            else:
                raise ValueError("La cantidad no puede ser negativo")
        else:
            raise ValueError("La cantidad debe ser un numero")

    def get_subtotal(self) -> float:
        return self.__subtotal

    def get_cantidad(self):
        return self.__cantidad