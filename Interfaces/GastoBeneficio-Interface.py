from tkinter import *
import mysql.connector
from Utilities.FechaYMeses import *
from tkinter import ttk
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
        self.geometry("1200x700")
        self.gasto = float
        self.ganancia = float
        self.gastoLabel = Label(self, text="Aqui va el gasto cuando le des al boton")
        self.gastoLabel.pack()
        self.choose = ttk.Combobox(self, state="readonly", values=["Diario", "Mensual"])
        self.choose.pack()
        self.si = Button(self, text="si", command=lambda:self.calcularGastosDiarios(self.choose.get()))
        self.si.pack()
        self.mainloop()

    def calcularGastosDiarios(self,estado):
        """"Empleados"""
        self.conection.reconnect()
        self.script = "SELECT SUM(sueldo) FROM empleado WHERE activo = 'V'"
        self.cursor.execute(self.script)
        self.sueldoEmpleadoSemanal = self.cursor.fetchone()
        self.sueldoEmpleadoDiario = self.sueldoEmpleadoSemanal[0] / 7
        Fecha = fecha()
        """Gastos como tal"""
        #Necesito calcular conforme al dia que fueron hechos
        #Agarrar solo el dia
        if estado == "Diario":
            self.script = f"SELECT SUM(monto) FROM gasto WHERE fecha BETWEEN '{Fecha.año}-{Fecha.mes}-{Fecha.dia} 00:00:00' AND '{Fecha.año}-{Fecha.mes}-{Fecha.dia} 23:59:59'"
            self.cursor.execute(self.script)
            result = self.cursor.fetchone()
            if result[0] == None:
                result = [0,0]
            self.gastoLabel.config(text = f"Total de gasto diario: {result[0]+self.sueldoEmpleadoDiario}")
        #Agarrando el mes completo
        if estado == "Mensual":
            self.script = f"SELECT SUM(monto) FROM gasto WHERE fecha BETWEEN '{Fecha.año}-{Fecha.mes}-01' AND '{Fecha.año}-{Fecha.mes}-{Fecha.dias}'"
            self.cursor.execute(self.script)
            result = self.cursor.fetchone()
            if result[0] == None:
                result = [0,0]
            self.sueldoEmpleadoMensual = int(self.sueldoEmpleadoDiario)*int(Fecha.dia)
            self.gastoLabel.config(text=f"Total de gasto mensual: {result[0]+self.sueldoEmpleadoMensual}")

    def calcularGanacia(self):
        self.conection.reconnect()

gastobeneficio = GastoBeneficioInterface()
gastobeneficio.calcularGastosDiarios()
print(gastobeneficio.sueldoEmpleadoDiario)