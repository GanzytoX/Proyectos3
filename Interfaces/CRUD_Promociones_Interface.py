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
from Utilities.twoSideWindow import twoSideWindow


# Esteticas:


# Ventana:
class PromocionInterface(twoSideWindow):
    def __init__(self):
        super().__init__(window_name="Promociones", size="1200x700", resizable=False,
                         background_image="../img/promociones.jpg")
        self.__conection = mysql.connector.connect(
            user="sql5660121",
            host="sql5.freesqldatabase.com",
            port="3306",
            password="GWes4WXpXH",
            database="sql5660121"

        )

        self.crud = CRUDPromociones(conection=self.__conection)

        self.get_frame_left().config(background="#442250")
        self.get_agregar_elemento_button().pack_forget()
        self.get_list_elements().pack(pady=(0, 20))
        self.update_idletasks()

        #Cuadrote promociones
        self.cuadrotePromociones = CuadrotePromociones()
        self.cuadrotePromociones.place(x=394,y=82)
        self.BotonCrear = Button(self.cuadrotePromociones, text="Crear Promocion", command=self.crearPromocion)
        self.BotonCrear.grid(column=1, row=6, pady=(50, 5))
        self.BotonBorrar = Button(self.cuadrotePromociones, text="Borrar Promocion", command=self.borrarPromocion)
        self.BotonBorrar.grid(column=0, row=6, pady=(50, 5))
        self.BotonEditar = Button(self.cuadrotePromociones, text="Editar Promocion", command=self.actualizarPromocion)
        self.BotonEditar.grid(column=0, row=7, pady=(10, 5))
        self.BotonLimpiar = Button(self.cuadrotePromociones, text="Limpiar", command=self.limpiar)
        self.BotonLimpiar.grid(column=0, row=8, pady=(10, 5))
        self.promociones = []
        #self.bind("<Button-1>", self.aaa)

        self.refresh()

    #  prueba para añadir las promociones a la lista
    def refresh(self):
        self.get_list_elements().clear()
        promociones= self.crud.Read()
        for promocion in promociones:
            if len(promocion.descripcion) > 40:
                enseñar = promocion.descripcion[0:40] + "..."
            else:
                enseñar = promocion.descripcion
            self.promociones.append(promocion)
            frame = ListFrame(self.get_list_elements(), enseñar, promocion)
            frame.addevento("<Button-1>", self.mostrarPromocion)
            self.get_list_elements().add(frame)
        promociones.clear()

    def limpiar(self):
        self.cuadrotePromociones.listaProd.set("")
        self.cuadrotePromociones.listaTipoPromocion.set("")
        self.cuadrotePromociones.fechaInicio.delete(0, END)
        self.cuadrotePromociones.fechaFinal.delete(0,END)
        self.cuadrotePromociones.cuadroDescripcion.delete("1.0", END)
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
        self.cuadrotePromociones.cuadroDescripcion.delete("1.0", END)
        self.cuadrotePromociones.cuadroDescripcion.insert("1.0",promocion.descripcion)
        self.cuadrotePromociones.fechaInicio.delete(0,END)
        self.cuadrotePromociones.fechaInicio.insert(0,promocion.fechainicio)
        self.cuadrotePromociones.fechaFinal.delete(0, END)
        self.cuadrotePromociones.fechaFinal.insert(0, promocion.fechainicio)
        self.cuadrotePromociones.current = promocion.id
        print(self.cuadrotePromociones.current)
        self.__conection.close()
        self.refresh()


    def actTipoPromocion(self,conection,promocion:Promocion):
        script = (f'SELECT tipo_de_promocion.id_tipo_promocion, tipo_de_promocion.nombre FROM tipo_de_promocion INNER JOIN promocion ON promocion.id_tipo_promocion = tipo_de_promocion.id_tipo_promocion WHERE %s = tipo_de_promocion.id_tipo_promocion')
        print(promocion.id_tipopromocion)
        cursor = conection.cursor()
        cursor.execute(script, [promocion.id_tipopromocion])
        result = cursor.fetchone()
        print(result)
        print(result[1])
        self.cuadrotePromociones.listaTipoPromocion.set(result[1])
    def actualizarPromocion(self):
        coonection = mysql.connector.connect(
            user="sql5660121",
            host="sql5.freesqldatabase.com",
            port="3306",
            password="GWes4WXpXH",
            database="sql5660121"

        )
        aSubir = []
        script = ('select id_producto from producto where %s = nombre')
        cursor = coonection.cursor()
        cursor.execute(script, [self.cuadrotePromociones.listaProd.get()])
        result = cursor.fetchone()
        aSubir.append(result[0])
        aSubir.append(self.cuadrotePromociones.cuadroDescripcion.get("1.0", END))
        aSubir.append(self.cuadrotePromociones.fechaInicio.get())
        aSubir.append(self.cuadrotePromociones.fechaFinal.get())
        # Buscar id tipo promocion
        script = ('select id_tipo_promocion from tipo_de_promocion where %s = nombre')
        cursor.execute(script, [self.cuadrotePromociones.listaTipoPromocion.get()])
        result = cursor.fetchone()
        aSubir.append(result[0])
        aSubir[1] = aSubir[1][0:len(aSubir[1]) - 1]
        print(aSubir)

        script =("Update promocion set id_producto = %s, descripcion = %s, fecha_de_inicio = %s, fecha_de_finalizacion = %s, id_tipo_promocion = %s where id_promocion = %s")
        cursor.execute(script,[aSubir[0],aSubir[1],aSubir[2],aSubir[3],aSubir[4], self.cuadrotePromociones.current])
        coonection.commit()
        coonection.close()
        self.refresh()
    def borrarPromocion(self):
        coonection = mysql.connector.connect(
            user="sql5660121",
            host="sql5.freesqldatabase.com",
            port="3306",
            password="GWes4WXpXH",
            database="sql5660121"

        )
        script = "Delete from promocion where id_promocion = %s"
        cursor = coonection.cursor()
        cursor.execute(script,[self.cuadrotePromociones.current])
        coonection.commit()
        print(f"se borro la promocion con id {self.cuadrotePromociones.current}")
        self.refresh()
        coonection.close()
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
        self.refresh()
    def aaa(self,event):
        print(event.x, event.y)
