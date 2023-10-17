from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk


class Window(CTk):
    def __init__(self, title: str, size: str, **kwargs):
        super().__init__(**kwargs)
        self.geometry(size)
        self.title(title)
        self.update()
        self.__bgImage = None
        self.bind("<Configure>", self.__onResize)


    def setBackgroundImage(self, imageRoute: str):
        self.raw = Image.open(imageRoute)
        resized = self.raw.resize((self.winfo_width(), self.winfo_height()))
        image = ImageTk.PhotoImage(resized)

        self.__bgImage = Canvas(self, width=self.winfo_width(), height=self.winfo_height())
        self.__bgImage.create_image(0,0, image=image, anchor='nw')
        self.__bgImage.image = image
        self.__bgImage.place(x=0, y=0)

    def __onResize(self, event):
        if self.raw is not None:
            self.update_idletasks()
            self.__bgImage.config(width=self.winfo_width(), height=self.winfo_height())
            resized = self.raw.resize((event.width, event.height))
            image = ImageTk.PhotoImage(resized)

            self.__bgImage.create_image(0, 0, image=image, anchor='nw')
            self.__bgImage.image = image






class ScrollableFrame(CTkScrollableFrame):
    def __init__(self, master: any):
        super().__init__(master)
        self.__list = []

    def add(self, item: any):
        item.grid(row=len(self.__list), column=0)
        self.__list.append(item)




