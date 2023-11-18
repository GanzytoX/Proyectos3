import tkinter
from tkinter import Tk, Frame, Button, Entry, Toplevel, Label
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
from Utilities.ListFrames import ventaFrame
import copy


class Pagos(Toplevel):
    __frame_izquierdo = Frame
    __lista_compra = AutomaticScrollableFrame
    __TotalLabelCant = Label

    def __init__(self, elementos):
        super().__init__()
        self.geometry("900x600")
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=4)

        # Frame del lado izquierdo
        self.__frame_izquierdo = Frame(self)
        self.__frame_izquierdo.grid(column=0, row=0, sticky="nsew", padx=10, pady=20)

        # Creamos la lista de compra
        self.__lista_compra = AutomaticScrollableFrame(self.__frame_izquierdo, height=350,width=200)
        self.__lista_compra.pack(padx=10, fill="x")
        self.__copy_elements(elementos)

        # Frame de los totales
        frameTotal = Frame(self.__frame_izquierdo)
        frameTotal.columnconfigure(index=0, weight=2)
        frameTotal.columnconfigure(index=1, weight=4)
        frameTotal.pack()

        # Label "total"
        label_total = Label(frameTotal, text="Total")
        label_total.grid(column=0, row=0, padx=10)

        # Poner el label del total
        self.__TotalLabelCant =Label(frameTotal)
        self.__TotalLabelCant.grid(column=1, row=0, padx=10)
        self.__calcularTotal()

        # Button de cancelar venta (aunque simplemente se podría cerrar la ventana y queda)
        self.__button_cancelar = Button(self.__frame_izquierdo, text="Cancelar",
                                        command=self.destroy)
        self.__button_cancelar.pack(side=tkinter.LEFT)

        # Frame del lado izquierdo
        self.__frameDerecho = Frame(self, background="e7e7e5")
        self.__frameDerecho.grid(column=1, row=0, sticky="NSEW", pady=20)
        self.__frameDerecho.columnconfigure(0, weight=3)
        self.__frameDerecho.columnconfigure(1, weight=5)

        # Frame de botones para pagar con efectivo o tarjeta
        frame_formas = Frame(self.__frameDerecho, background="white")
        frame_formas.grid(column=0, row=0, sticky="EW")

        # Boton para efectivo
        self.__buton_efectivo = Button(frame_formas, background="#185791", text="Efectivo")
        self.__buton_efectivo.pack()

    def __copy_elements(self, elementos_list):
        for element in elementos_list:
            self.__lista_compra.add(
                ventaFrame(self.__lista_compra, element[0], element[1], element[2], element[3])
            )
        self.__lista_compra.update_idletasks()

    def __calcularTotal(self) -> float:
        total = 0
        for i in range(self.__lista_compra.countItems()):
            total += self.__lista_compra.getItem(i).get_subtotal()
        self.__TotalLabelCant.config(text=f"${total}")
        return total

