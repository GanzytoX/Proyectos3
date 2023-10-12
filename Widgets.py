from customtkinter import *
from PIL import Image
class Window(CTk):
    def __init__(self, title: str, size: str, **kwargs):
        super().__init__(**kwargs)
        self.geometry(size)
        self.title(title)
        self.xSize = 1
        self.ySize = 1


    def backgroundImage(self, imageRoute: str):
        print(self.winfo_width())
        raw = Image.open(imageRoute)
        raw.resize((self.xSize, self.ySize))
        raw.show()
        image = CTkImage(raw)
        background = CTkLabel(self, text="", image=image, bg_color="black")
        background.pack(expand=True, fill=BOTH)

    def obtener_tamano_ventana(self, event):
        self.xSize = event.width
        self.ySize = event.height
        self.backgroundImage("img/Inicio de sesión.png")


class ScrollableFrame(CTkScrollableFrame):
    def __init__(self, master: any):
        super().__init__(master)
        self.__list = []

    def add(self, item: any):
        item.grid(row=len(self.__list), column=0)
        self.__list.append(item)




