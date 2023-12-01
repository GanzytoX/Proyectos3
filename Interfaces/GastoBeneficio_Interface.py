
from tkinter import *
import mysql.connector
from Utilities.FechaYMeses import *
from tkinter import ttk
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta

class GastoBeneficioInterface(Tk):
    def __init__(self):
        super().__init__()
        self.conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.cursor = self.conection.cursor()
        self.script = ""
        self.title("Gasto-Beneficio")
        self.geometry("800x400")
        self.config(background="#bff0f5")
        self.gasto = float
        self.ganancia = float

        # Cosas relacionadas a la barra de búsqueda
        frameBusqueda = Frame(self, background="white")
        frameBusqueda.pack(ipadx=5, ipady=5, pady=15)
        self.__comboBoxMode = ttk.Combobox(frameBusqueda)
        self.__comboBoxMode["values"] = ("Diario", "Semanal", "Mesual")
        self.__comboBoxMode.set("Diario")
        self.__comboBoxMode['state'] = 'readonly'
        self.__comboBoxMode.pack(side="left", padx=5)
        self.__buttonReturn = Button(frameBusqueda, text="<")
        self.__buttonReturn.pack(side="left")
        self.__labelTiempo = Entry(frameBusqueda, relief="solid", borderwidth=2, background="white", width=50)
        self.__labelTiempo.insert(0, "Waos")
        self.__labelTiempo.pack(side="left", padx=6, ipady=2, ipadx=3)
        self.__buttonNext = Button(frameBusqueda, text=">")
        self.__buttonNext.pack(side="left")
        #self.__buttonBusqueda = Button(frameBusqueda, text="Calendario")
        #self.__buttonBusqueda.pack(side="left")

        frameDatos = Frame(self, background="white")
        frameDatos.pack(ipadx=10, ipady=10)
        self.__gastoLabel = Label(frameDatos, text="Gasto total", background="white")
        self.__gastoLabel.pack()
        self.__gastoEntry = Entry(frameDatos, width=84, background="#e0e4e5")
        self.__gastoEntry.pack(pady=(0,10))

        self.__ventaLabel = Label(frameDatos, text="Ventas totales", background="white")
        self.__ventaLabel.pack()
        self.__ventaEntry = Entry(frameDatos, width=84, background="#e0e4e5")
        self.__ventaEntry.pack(pady=(0,10))

        self.__gananciaLabel = Label(frameDatos, text="Ganancias totales", background="white")
        self.__gananciaLabel.pack()
        self.__gananciaEntry = Entry(frameDatos, width=84, background="#e0e4e5")
        self.__gananciaEntry.pack()

        # Parametros para saber la fecha
        self.__ticks = 0

        self.__setFecha(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)

        # Binds
        self.__comboBoxMode.bind('<<ComboboxSelected>>', self.__reset_ticks)
        self.__buttonReturn.config(command=self.__rewind)
        self.__buttonNext.config(command=self.__next)

        #self.si = Button(self, text="si", command=lambda: (self.calcularGastosDiarios(self.choose.get()), self.calcularGanacia(self.choose.get())))
        #self.si.pack()


    def calcularGastosDiarios(self, estado, año, mes, dia) ->float:
        """"Empleados"""
        self.conection.reconnect()
        self.script = "SELECT SUM(sueldo) FROM empleado WHERE activo = 'V'"
        self.cursor.execute(self.script)
        self.sueldoEmpleadoSemanal = self.cursor.fetchone()
        self.sueldoEmpleadoDiario = self.sueldoEmpleadoSemanal[0] / 7
        """Gastos como tal"""
        #Necesito calcular conforme al dia que fueron hechos
        #Agarrar solo el dia
        if estado == "Diario":
            self.script = f"SELECT SUM(monto) FROM gasto WHERE fecha BETWEEN '{año}-{mes}-{dia} 00:00:00' AND '{año}-{mes}-{dia} 23:59:59'"
            self.cursor.execute(self.script)
            result = self.cursor.fetchone()
            if result[0] == None:
                result = [0,0]
            return float(result[0]+self.sueldoEmpleadoDiario)

        elif estado == "Semanal":
            self.script = f"SELECT SUM(monto) FROM gasto WHERE WEEK(fecha) = {date(año, mes, dia).isocalendar().week} AND YEAR(fecha) = {año}"
            self.cursor.execute(self.script)
            result = self.cursor.fetchone()
            if result[0] == None:
                result = [0,0]
            return float(result[0]) + self.sueldoEmpleadoSemanal[0]

        #Agarrando el mes completo
        elif estado == "Mensual":
            # Cambiar dia por dias
            self.script = f"SELECT SUM(monto) FROM gasto WHERE fecha BETWEEN '{año}-{mes}-01' AND '{año}-{mes}-{dia}'"
            self.cursor.execute(self.script)
            result = self.cursor.fetchone()
            if result[0] == None:
                result = [0,0]
            self.sueldoEmpleadoMensual = int(self.sueldoEmpleadoDiario)*int(Fecha.dia)
            self.gastoLabel.config(text=f"Total de gasto mensual: {result[0]+self.sueldoEmpleadoMensual}")


    def calcularVentas(self, estado, año, mes, dia):
        self.conection.reconnect()
        Fecha = fecha()
        if estado == "Diario":
            self.script = f"SELECT SUM(total_De_Compra) FROM venta WHERE fecha_De_Venta BETWEEN '{Fecha.año}-{Fecha.mes}-{Fecha.dia} 00:00:00' AND '{Fecha.año}-{Fecha.mes}-{Fecha.dia} 23:59:59'"
            self.cursor.execute(self.script)
            result = self.cursor.fetchone()
            if result[0] == None:
                result = [0,0]
            self.gananciaLabel.config(text=f"Total ganancia diaria: {result[0]}")
        if estado == "Semanal":
            self.script = f"SELECT SUM(total_De_Compra) FROM venta WHERE WEEK(fecha_De_Venta) = {Fecha.semana}"
            self.cursor.execute(self.script)
            result = self.cursor.fetchone()
            if result[0] == None:
                result = [0,0]
            self.gananciaLabel.config(text=f"Total ganancia Semanal: {result[0]}")
        if estado == "Mensual":
            self.script = f"SELECT SUM(total_De_Compra) FROM venta WHERE fecha_De_Venta BETWEEN '{Fecha.año}-{Fecha.mes}-01' AND '{Fecha.año}-{Fecha.mes}-{Fecha.dias}'"
            self.cursor.execute(self.script)
            result = self.cursor.fetchone()
            if result[0] == None:
                result = [0, 0]
            self.gananciaLabel.config(text=f"Total ganancia mensual: {result[0]}")

    def __setFecha(self, fecha):
        self.__labelTiempo.delete(0, END)
        self.__labelTiempo.insert(0, fecha)


    def __rewind(self):
        self.__ticks -= 1
        self.__setFecha( self.__get_date(self.__comboBoxMode.get()))

    def __next(self):
        self.__ticks += 1
        self.__setFecha( self.__get_date(self.__comboBoxMode.get()))

    def __get_date(self, mode):
        if mode == "Diario":
            fechaTicks = datetime.datetime.now() + timedelta(days=self.__ticks)
        elif mode == "Semanal":
            fechaTicks = datetime.datetime.now() + timedelta(weeks=self.__ticks)
        else:
            fechaTicks = datetime.datetime.now() + relativedelta(months=self.__ticks)

        return f"{fechaTicks.date().year}/{fechaTicks.date().month}/{fechaTicks.date().day}"

    def __reset_ticks(self, event):
        self.__ticks = 0

gasto = GastoBeneficioInterface()
gasto.mainloop()