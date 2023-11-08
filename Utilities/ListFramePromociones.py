from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
import tkinter as tk
from PIL import Image, ImageTk
from typing import Callable

class ListFrame(tk.Frame):
    __image = None
    __text = str
    __object = None
    def __init__(self, master : AutomaticScrollableFrame, text:str, objeto):
        tk.Frame.__init__(self, master)
        self.grid()
        self.label = tk.Label(self, text=text)
        self.label.grid(row=0, column=0)
        self.object = objeto
    def addEvento(self: tk.W,
            sequence: str | None = ...,
            func: Callable[[object], None] | None = ...):
        self.function = func
        super().bind(sequence, self.returnObject)
        self.label.bind(sequence,self.returnObject)

    def returnObject(self, event):
        self.function(self.object)

