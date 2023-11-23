from CRUD_User_Interfaces import *
from CRUD_Prod_Interface import *
from CRUD_Promociones_Interface import *
from Interfaces.Inventario_Interface import InventarioApp
from Ventas_Interface import *
from VentasViewer import *
from GastoBeneficio_Interface import *

class AdminMainMenu(Tk):
    __titleLabel = Label
    __frameBotones = Frame
    __openEmpleadosButton = Button
    __openProductosButton = Button
    __openOfertasButton = Button

    def __init__(self, userId):
        super().__init__()
        self.title("Main Menu")
        self.geometry("500x250")
        self.__titleLabel = Label(self, text="Bienvenido \n ¿Qué acción le gustaría hacer?")
        self.__titleLabel.pack()
        self.__frameBotones = Frame(self)
        self.__frameBotones.pack()
        self.__userId = userId
        self.__frameBotones.columnconfigure(0, weight=3)
        self.__frameBotones.columnconfigure(1, weight=3)
        self.__frameBotones.columnconfigure(2, weight=3)

        self.__openEmpleadosButton = Button(self.__frameBotones, text="Abrir empleados", command=self.__openEmpleados)
        self.__openEmpleadosButton.grid(column=0, row=0, padx=20)

        self.__openProductosButton = Button(self.__frameBotones, text="Abrir productos", command=self.__openProductos)
        self.__openProductosButton.grid(column=1, row=0, pady=20)

        self.__openOfertasButton = Button(self.__frameBotones, text="Abrir ofertas", command=self.__openPromocion)
        self.__openOfertasButton.grid(column=2, row=0, padx=20)

        self.__openVentasButton = Button(self.__frameBotones, text="Abrir ventas", command=self.__openVentas)
        self.__openVentasButton.grid(column=0, row=1, padx=20)

        self.__openVentasVisualizadorButton = Button(self.__frameBotones, text="Ver detalle ventas", command=self.__openVentasVis)
        self.__openVentasVisualizadorButton.grid(column=1, row=1, padx=20)

        self.__openGastoBeneficioButton = Button(self.__frameBotones, text="Ver Gasto-Beneficio", command=self.__openGastoBeneficio)
        self.__openGastoBeneficioButton.grid(column=2, row=1, padx=20)

        self.__openGastoBeneficioButton = Button(self.__frameBotones, text="Ver Inventario",
                                                 command=self.__openInventario)
        self.__openGastoBeneficioButton.grid(column=0, row=2, pady=20)


    def __openEmpleados(self):
        newVentana = CUInterface()
        newVentana.mainloop()

    def __openProductos(self):
        newVentana = CPr_Interface()
        newVentana.mainloop()

    def __openPromocion(self):
        newVentana = PromocionInterface()
        newVentana.mainloop()
    def __openVentas(self):
        newVentana = VentasInterFace(self.__userId)
        newVentana.mainloop()
    def __openVentasVis(self):
        newVentana = VentasViewer()
        newVentana.mainloop()

    def __openGastoBeneficio(self):
        newVentana = GastoBeneficioInterface()
        newVentana.mainloop()
    def __openInventario(self):
        newVentana = InventarioApp(Tk())
        newVentana.mainloop()

class EmpleadoMainMenu(Tk):
    __titleLabel = Label
    __frameBotones = Frame
    __open_ventas = Button
    __open_gasto = Button
