from customtkinter import CTkScrollableFrame

class ScrollableFrame(CTkScrollableFrame):
    def __init__(self, master:any, height = None, width = None,length=1):
        if height is not None and width is not None:
            super().__init__(master, height=height, width=width)
        self.__items = []
        self.length = length
        self.x = 0
        self.y = 0
        self.index = 0


    def add(self, element:any):
        if (self.x <= self.length):
            element.grid(column=self.x,row = self.y)
            self.x += 1
        if (self.x > self.length):
            self.x = 0
            self.y += 1
            element.grid(column=self.x, row = self.y)
            self.x += 1
        self.__items.append(element)
        self.update_idletasks()
    def clear(self):
        print(self.__items)
        for item in self.__items:
            item.destroy()
        self.__items.clear()
        self.update()

    def get_item(self, index: int):
        return self.__items[index]

    def get_lenght(self):
        return len(self.__items)

    def deleteAt(self, index):
        self.__items[index].destroy()
        self.__items.pop(index)
        self.update_idletasks()
