from tkinter import *
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
import PIL.Image
import PIL.ImageTk


class twoSideWindow(Tk):
    __frame_left = Frame
    __frame_buscador = Frame
    
    def __init__(self, window_name: str = None, size: str = None, resizable: bool = None, background_image: str = None):
        super().__init__()
        # Configuraciones generales de la ventana
        self.title(window_name)
        self.geometry(size)
        self.resizable(resizable, resizable)
        
        # Crear un widget Label para mostrar la imagen de fondo
        if background_image != "" and background_image != None:
            imagen_fondo = PIL.Image.open("../img/Empleado.png")
            imagen_fondo = PIL.ImageTk.PhotoImage(imagen_fondo, master=self)
            label_imagen = Label(self, image=imagen_fondo)
            label_imagen.place(relwidth=1, relheight=1)  # Estirar la imagen para que cubra toda la ventana
            label_imagen.imagen = imagen_fondo

        # Configurar cuadrícula de la ventana
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        # Widget para desplegar elementos en una lista scrolleable
        self.__set_frame_left(Frame(self, height=500, width=250, background="#204484"))
        self.get_frame_left().grid(column=0, row=0, pady=50, padx=50, ipadx=20, sticky="NSW")
        self.get_frame_left().columnconfigure(0, weight=5)
        self.get_frame_left().columnconfigure(1, weight=1)

        # Margin de la barra de buscador
        self.__set_frame_buscador(Frame(self.get_frame_left(), background="#204484"))
        self.get_frame_left().columnconfigure(0, weight=5)
        self.get_frame_left().columnconfigure(1, weight=1)
        self.get_frame_left().pack(pady=20, padx=20, fill="x")

    def get_frame_left(self) -> Frame:
        return self.__frame_left

    def __set_frame_left(self, frame: Frame):
        if isinstance(frame, Frame):
            self.__frame_left = frame

    def get_frame_buscador(self) -> Frame:
        return self.__frame_buscador

    def __set_frame_buscador(self, frame: Frame):
        if isinstance(frame, Frame):
            self.__frame_buscador = frame