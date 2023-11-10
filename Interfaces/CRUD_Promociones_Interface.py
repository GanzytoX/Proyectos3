from tkinter import *
import PIL.Image
import PIL.ImageTk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from Crud.CRUDOfertas import CRUDPromociones, Promocion
from Utilities.AutomaticScrollableFrame import AutomaticScrollableFrame
from Utilities.ListFramePromociones import ListFrame
from Utilities.ListFramePromociones import CuadrotePromociones


# Esteticas:


# Ventana:
class PromocionInterface(Tk):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="sql5660121",
            host="sql5.freesqldatabase.com",
            port="3306",
            password="GWes4WXpXH",
            database="sql5660121"

        )
        self.imagen_fondo = Image.open("../img/promociones.jpg")
        self.imagen_fondo = self.imagen_fondo.resize((1200, 700), Image.LANCZOS)
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen_fondo)
        self.label_imagen = Label(self, image=self.imagen_fondo)
        self.label_imagen.grid(row=0, column=0, sticky="NWSE")
        self.crud = CRUDPromociones(conection=self.__conection)
        self.title = "Promociones"
        self.geometry("1200x700")
        self.resizable(False, False)

        # Pa que se acomode un cuadrito a la izquierda y uno grandote a la derecha
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        # El cuadrito de las promociones
        self.cuadritoPromociones = Frame(self, width=350, height=500, bg="#442250")
        self.cuadritoPromociones.grid(column=0, row=0, pady=50, padx=50, ipadx=20, sticky="W")

        # la barra de búsqueda
        self.busqueda = Entry(self.cuadritoPromociones, fg="red")
        self.busqueda.pack(fill="x")  # fill x es pa que lo llene de los lados

        # el cuadro donde se van a seleccionar las promociones
        self.cuadroPromociones = AutomaticScrollableFrame(self.cuadritoPromociones, height=470)
        self.cuadroPromociones.pack(fill="both", padx=30)

        #Cuadrote promociones
        self.cuadrotePromociones = CuadrotePromociones()
        self.cuadrotePromociones.place(x=394,y=82)
        self.BotonCrear = Button(self.cuadrotePromociones, text="Crear Promocion", command=self.crearPromocion)
        self.BotonCrear.grid(column=1, row=6, pady=(50, 5))
        self.promociones = []
        #self.bind("<Button-1>", self.aaa)

        self.refresh()

    #  prueba para añadir las promociones a la lista
    def refresh(self):
        self.cuadroPromociones.clear()
        promociones= self.crud.Read()
        for promocion in promociones:
            if len(promocion.descripcion) > 40:
                enseñar = promocion.descripcion[0:40] + "..."
            else:
                enseñar = promocion.descripcion
            self.promociones.append(promocion)
            frame = ListFrame(self.cuadroPromociones, enseñar, promocion)

            frame.addevento("<Button-1>", self.mostrarPromocion)
            self.cuadroPromociones.add(frame)
        promociones.clear()

    def mostrarPromocion(self, promocion : Promocion):
        self.__conection = mysql.connector.connect(
            user="sql5660121",
            host="sql5.freesqldatabase.com",
            port="3306",
            password="GWes4WXpXH",
            database="sql5660121"

        )
        script = (f'SELECT producto.id_producto, producto.nombre from producto inner join promocion on promocion.id_producto = producto.id_producto WHERE %s = promocion.descripcion')
        cursor = self.__conection.cursor()
        cursor.execute(script, [promocion.descripcion])
        result = cursor.fetchone()
        #resultado tiene el id y el nombre del prooduto
        print(result)
        self.cuadrotePromociones.listaProd.set(result[1])
        #buscar aquel tipo de promocion con el que esta relacionado promocion
        self.actTipoPromocion(self.__conection, promocion)

        self.__conection.close()


    def actTipoPromocion(self,conection,promocion:Promocion):
        script = (f'SELECT tipo_de_promocion.id_tipo_promocion, tipo_de_promocion.nombre FROM tipo_de_promocion INNER JOIN promocion ON promocion.id_tipo_promocion = tipo_de_promocion.id_tipo_promocion WHERE %s = tipo_de_promocion.id_tipo_promocion')
        print(promocion.id_tipopromocion)
        cursor = conection.cursor()
        cursor.execute(script, [promocion.id_tipopromocion])
        result = cursor.fetchone()
        print(result)
        print(result[1])
        self.cuadrotePromociones.listaTipoPromocion.set(result[1])
    def crearPromocion(self):
        coonection = mysql.connector.connect(
            user="sql5660121",
            host="sql5.freesqldatabase.com",
            port="3306",
            password="GWes4WXpXH",
            database="sql5660121"

        )
        aSubir = []
        #Buscar id del producto seleccionado
        script = ('select id_producto from producto where %s = nombre')
        cursor = coonection.cursor()
        cursor.execute(script, [self.cuadrotePromociones.listaProd.get()])
        result = cursor.fetchone()
        aSubir.append(result[0])
        aSubir.append(self.cuadrotePromociones.cuadroDescripcion.get("1.0",END))
        aSubir.append(self.cuadrotePromociones.fechaInicio.get())
        aSubir.append(self.cuadrotePromociones.fechaFinal.get())
        #Buscar id tipo promocion
        script = ('select id_tipo_promocion from tipo_de_promocion where %s = nombre')
        cursor.execute(script, [self.cuadrotePromociones.listaTipoPromocion.get()])
        result = cursor.fetchone()
        aSubir.append(result[0])
        aSubir[1] = aSubir[1][0:len(aSubir[1])-1]
        print(aSubir)
        script = "INSERT INTO promocion(id_producto,descripcion,fecha_de_inicio,fecha_de_finalizacion,id_tipo_promocion) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(script,[aSubir[0],aSubir[1],aSubir[2],aSubir[3],aSubir[4]])
        coonection.commit()
        coonection.close()
    def aaa(self,event):
        print(event.x, event.y)
