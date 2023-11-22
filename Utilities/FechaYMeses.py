import time
import datetime


class fecha:
    def __init__(self):
        self.actual_time = time.localtime()
        self.timeFormatted = time.strftime("%Y/%m/%d", self.actual_time)
        self.timeFormatted = self.timeFormatted.split("/")
        self.mes = int(self.timeFormatted[1])
        self.año = int(self.timeFormatted[0])
        self.dias = int
        self.dia = int(self.timeFormatted[2])
        self.diaDeLaSemana = datetime.datetime.today().weekday()
        self.calcularDias()
        self.biciesto = False
        self.semana = datetime.date(self.año, self.mes, self.dia).isocalendar().week
    def calcularDias(self):
        MesesTYU = [1, 3, 5, 7, 8, 10, 12]
        MesesT = [4, 6, 9, 11]
        if self.mes in MesesTYU:
            self.dias = 31
        elif self.mes in MesesT:
            self.dias = 30
        elif (self.año % 400 == 0 or self.año % 100 != 0) and self.año % 4 == 0:
            self.dias = 29
            self.biciesto = True
        else:
            self.dias = 28

