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
        self.rowconfigure(0, weight=10)

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
        total = self.__calcularTotal()

        # Button de cancelar venta (aunque simplemente se podría cerrar la ventana y queda)
        self.__button_cancelar = Button(self.__frame_izquierdo, text="Cancelar",
                                        command=self.destroy)
        self.__button_cancelar.pack(side=tkinter.LEFT)

        # Frame del lado izquierdo
        self.__frameDerecho = Frame(self, background="#e7e7e5")
        self.__frameDerecho.grid(column=1, row=0, sticky="NSEW", pady=20)
        self.__frameDerecho.columnconfigure(0, weight=3)
        self.__frameDerecho.columnconfigure(1, weight=5)

        # Frame de botones para pagar con efectivo o tarjeta
        frame_formas = Frame(self.__frameDerecho, background="white")
        frame_formas.grid(column=0, row=0, sticky="EW", padx=10)

        # Boton para efectivo
        self.__buton_efectivo = Button(frame_formas, background="#185791", text="Efectivo", foreground="white")
        self.__buton_efectivo.pack(padx=5)

        # Frame para para efectivo
        frame_efectivo = Frame(self.__frameDerecho, background="white")
        frame_efectivo.grid(column=1, row=0, sticky="EW", padx=5)

        # Elementos del frame de efectivo
        texto_efectivo = Label(frame_efectivo, text="Efectivo")
        texto_efectivo.pack(pady=5)

        texto_total = Label(frame_efectivo, text="Total")
        texto_total.pack(pady=5)

        entry_total = Entry(frame_efectivo)
        entry_total.insert(0, str(total))
        entry_total.config(state="readonly")
        entry_total.pack()

        texto_recibido = Label(frame_efectivo, text="Recibido")
        texto_recibido.pack(pady=5)

        entry_recibido = Entry(frame_efectivo)
        entry_recibido.pack()

        texto_cambio = Label(frame_efectivo, text="Cambio")
        texto_cambio.pack(pady=5)

        entry_cambio = Entry(frame_efectivo, state="readonly")
        entry_cambio.pack()

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

