from tkinter import *


class AdminMainMenu(Tk):
    __titleLabel = Label

    def __init__(self):
        super().__init__()
        self.title = "Main Menu"
        self.geometry = "100x250"
        self.__titleLabel = Label(self, text="Bienvenido \n ¿Qué acción le gustaría hacer?")

        self.mainloop()


mainWindow = AdminMainMenu()
