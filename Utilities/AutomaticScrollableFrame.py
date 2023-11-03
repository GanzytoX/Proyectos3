from customtkinter import CTkScrollableFrame


class AutomaticScrollableFrame(CTkScrollableFrame):
    def __init__(self, master: any, height=None, width=None):
        if height is not None and width is not None:
            super().__init__(master, height=height, width=width)
        elif height is not None:
            super().__init__(master, height=height)
        elif width is not None:
            super().__init__(master, width=width)
        self.__items = []
        self.columnconfigure(0, weight=3)

    def add(self, element: any) -> None:
        element.grid(column=0, row=len(self.__items), sticky="ew", pady="5")
        self.__items.append(element)

    def deleteAt(self, index):
        if len(self.__items) > index >= 0:
            item = self.__items[index]
            self.__items[index].remove(index)
            item.destroy()

    def clear(self):
        print("activado")
        print(self.__items)
        for item in self.__items:
            item.destroy()
        self.__items.clear()
        self.update()

    def getItem(self, index):
        if len(self.__items) > index >= 0:
            return self.__items[index]
        raise IndexError("Index out of range")

    def countItems(self) -> int:
        return len(self.__items)