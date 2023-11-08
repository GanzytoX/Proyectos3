from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
import tkinter as tk
from PIL import Image, ImageTk
from typing import Callable

class ListFrame(tk.Frame):
    __image = None
    __text = str
    __object = None
    def __init__(self, master : AutomaticScrollableFrame, text:str, width:int):
        super().__init__()
        self.label = tk.Label(self, text=text)
        self.config(height=width)

