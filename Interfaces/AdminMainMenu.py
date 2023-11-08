from tkinter import *
from CRUD_User_Interfaces import *
from CRUD_Prod_Interface import *

class AdminMainMenu(Tk):
    __titleLabel = Label
    __frameBotones = Frame
    __openEmpleadosButton = Button
    __openProductosButton = Button
    __openOfertasButton = Button

    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("500x250")
        self.__titleLabel = Label(self, text="Bienvenido \n ¿Qué acción le gustaría hacer?")
        self.__titleLabel.pack()
        self.__frameBotones = Frame(self)
        self.__frameBotones.pack()

        self.__frameBotones.columnconfigure(0, weight=3)
        self.__frameBotones.columnconfigure(1, weight=3)
        self.__frameBotones.columnconfigure(2, weight=3)

        self.__openEmpleadosButton = Button(self.__frameBotones, text="Abir empleados", command=self.__openEmpleados)
        self.__openEmpleadosButton.grid(column=0, row=0, padx=20)

        self.__openProductosButton = Button(self.__frameBotones, text="Abir productos", command=self.__openProductos)
        self.__openProductosButton.grid(column=1, row=0, pady=20)

        self.__openOfertasButton = Button(self.__frameBotones, text="Abir ofertas")
        self.__openOfertasButton.grid(column=2, row=0, padx=20)


    def __openEmpleados(self):
        newVentana = CUInterface()
        newVentana.mainloop()

    def __openProductos(self):
        newVentana = CPr_Interface()
        newVentana.mainloop()

