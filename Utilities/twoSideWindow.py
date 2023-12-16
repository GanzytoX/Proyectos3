from tkinter import *
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
import PIL.Image
import PIL.ImageTk


class twoSideWindow(Tk):
    __frame_left = Frame
    __frame_buscador = Frame
    __nav = Entry
    __boton_buscar = Button
    __list_elements = AutomaticScrollableFrame
    __agregar_elemento_button = Button

    def __init__(self, window_name: str = None, size: str = None, resizable: bool = None, background_image: str = None):
        super().__init__()
        # Configuraciones generales de la ventana
        self.title(window_name)
        self.geometry(size)
        self.resizable(resizable, resizable)
        
        # Crear un widget Label para mostrar la imagen de fondo
        if background_image != "" and background_image != None:
            imagen_fondo = PIL.Image.open(background_image)
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
        self.get_frame_buscador().columnconfigure(0, weight=5)
        self.get_frame_buscador().columnconfigure(1, weight=1)
        self.get_frame_buscador().pack(pady=20, padx=20, fill="x")

        # Barra del buscador
        self.__set_navegation_bar(Entry(self.get_frame_buscador(), background="#d8dce4"))
        self.get_navegation_bar().grid(column=0, row=0, padx=(0, 5), sticky="NSEW")

        # Boton para buscar
        self.__set_boton_buscar(Button(self.get_frame_buscador(), text="B"))
        self.get_boton_buscar().grid(column=1, row=0, sticky="NSEW")

        # Un frame donde acomodar los elementos
        self.__set_list_elements(AutomaticScrollableFrame(self.get_frame_left(), height=470))
        self.get_list_elements().pack(fill="both", padx=20)


        # Un boton para poder agregar elementos
        self.__set_agregar_elemento_button(Button(self.get_frame_left()))
        self.get_agregar_elemento_button().pack(pady=10)

    # Encapsulamientos
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

    def get_navegation_bar(self) -> Entry:
        return self.__nav

    def __set_navegation_bar(self, nav: Entry):
        if isinstance(nav, Entry):
            self.__nav = nav

    def get_boton_buscar(self) -> Button:
        return self.__boton_buscar

    def __set_boton_buscar(self, button: Button):
        if isinstance(button, Button):
            self.__boton_buscar = button

    def get_list_elements(self) -> AutomaticScrollableFrame:
        return self.__list_elements

    def __set_list_elements(self, automaticScrollableFrame: AutomaticScrollableFrame):
        if isinstance(automaticScrollableFrame, AutomaticScrollableFrame):
            self.__list_elements = automaticScrollableFrame

    def get_agregar_elemento_button(self) -> Button:
        return self.__agregar_element_button

    def __set_agregar_elemento_button(self, button: Button):
        if isinstance(button, Button):
            self.__agregar_element_button = button


