from tkinter import *
import mysql.connector

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
        self.mainloop()

    def calcularGastosDiarios(self):
        """"Empleados"""
        self.conection.reconnect()
        self.script = "SELECT SUM(sueldo) FROM empleado WHERE activo = 'V'"
        self.cursor.execute(self.script)
        self.sueldoEmpleadoSemanal = self.cursor.fetchone()
        self.sueldoEmpleadoDiario = self.sueldoEmpleadoSemanal[0] / 7

        """Gastos como tal"""


    def calcularGanacia(self):
        self.conection.reconnect()

gastobeneficio = GastoBeneficioInterface()
gastobeneficio.calcularGastosDiarios()
print(gastobeneficio.sueldoEmpleadoDiario)