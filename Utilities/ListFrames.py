from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
import tkinter as tk
from PIL import Image, ImageTk
from typing import Callable

class ListFrame(tk.Frame):
    __image = None
    __text = str
    __object = None

    def __init__(self, master: AutomaticScrollableFrame, text: str, objet, imageroute: str, imageSize: (int, int)):
        super().__init__(master=master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        imagen_raw = Image.open(imageroute)
        imagen_raw.thumbnail(imageSize)
        imagen_tk = ImageTk.PhotoImage(imagen_raw)
        self.__image = tk.Label(self, image=imagen_tk)
        self.__image.image = imagen_tk
        self.__image.grid(column=0, row=0)
        self.__text = tk.Label(self, height=4, justify="left", text=text)
        self.__text.grid(column=1, row=0, sticky="W")
        self.object = objet

    def addEvent(
            self: tk.W,
            sequence: str | None = ...,
            func: Callable[[object], None] | None = ...):
        self.__function = func
        string = super().bind(sequence, self.__returnObject)
        self.__image.bind(sequence, self.__returnObject)
        self.__text.bind(sequence, self.__returnObject)
        return string

    def __returnObject(self, event):
        self.__function(self.object)


class NoImageFrame(ListFrame):
    def __init__(self, master: AutomaticScrollableFrame, text: str, objet):
        super().__init__(master, text, objet, "../img/dot.png", (10, 10))


class ImageFrame(ListFrame):
    def __init__(self, master: AutomaticScrollableFrame, text: str, objet, imageroute: str):
        super().__init__(master, text, objet, imageroute, (60, 60))