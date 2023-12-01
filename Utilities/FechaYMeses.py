import time
import datetime


class fecha:
    mes = int
    def __init__(self):
        self.actual_time = time.localtime()
        self.timeFormatted = time.strftime("%Y/%m/%d", self.actual_time)
        self.timeFormatted = self.timeFormatted.split("/")
        self.mes = int(self.timeFormatted[1])
        self.año = int(self.timeFormatted[0])
        self.dia = int(self.timeFormatted[2])
        self.diaDeLaSemana = datetime.datetime.today().weekday()
        self.biciesto = False
        self.semana = datetime.date(self.año, self.mes, self.dia).isocalendar().week

    @classmethod
    def calcularDias(self, numerodemes:int, año:int):
        año = int(año)
        numerodemes = int(numerodemes)
        print(numerodemes)
        MesesTYU = [1, 3, 5, 7, 8, 10, 12]
        MesesT = [4, 6, 9, 11]
        if numerodemes in MesesTYU:
            return 31
        elif numerodemes in MesesT:
            return 30
        elif ((año % 400 == 0 or año % 100 != 0) and año % 4 == 0):
            return 29
        else:
            return 28

fecha.calcularDias(2,2023)