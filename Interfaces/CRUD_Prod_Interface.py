from PIL import ImageTk, Image

from Interfaces.CRUD_User_Interfaces import AutomaticScrollableFrame
from tkinter import *

class ImageFrame(Frame):
    __image = None
    __text = str
    __object = None

    def __init__(self, master: AutomaticScrollableFrame, text: str, objet, imageroute: str):
        super().__init__(master=master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        imagen_raw = Image.open("../img/dot.png")
        imagen_raw.thumbnail((10, 10))
        imagen_tk = ImageTk.PhotoImage(imagen_raw)
        self.__image = Label(self, image=imagen_tk)
        self.__image.image = imagen_tk
        self.__image.grid(column=0, row=0)
        self.__text = Label(self, height=4, justify="left", text=text)
        self.__text.grid(column=1, row=0, sticky="W")
        self.object = objet