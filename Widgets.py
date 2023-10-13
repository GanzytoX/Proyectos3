from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
class Window(CTk):
    def __init__(self, title: str, size: str, **kwargs):
        super().__init__(**kwargs)
        self.geometry(size)
        self.title(title)
        self.update()
        print(self.winfo_width())
        self.canva = Canvas(self, width=self.winfo_width(), height=self.winfo_height(), background="black")


    def setBackgroundImage(self, imageRoute: str):
        raw = Image.open(imageRoute)
        resized = raw.resize((1200, 700))
        resized.save("prueba.png")
        image = ImageTk.PhotoImage(resized)

        label = Label(self, image=image, text="", background="black", compound="left")
        label.image = image
        label.pack()
        #raw.thumbnail((1100, 700))
        #self.canva.create_image(0, 0, image=image, anchor='nw')

        #self.canva.pack(expand=True, fill=BOTH)



class ScrollableFrame(CTkScrollableFrame):
    def __init__(self, master: any):
        super().__init__(master)
        self.__list = []

    def add(self, item: any):
        item.grid(row=len(self.__list), column=0)
        self.__list.append(item)




