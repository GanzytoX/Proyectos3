import datetime
from Interfaces.Ventas_Interface import *
import mysql.connector
from tkinter import messagebox
import time
def validar(main:VentasInterFace, producto:siFrame, idpro: int,count=1):
    conection = mysql.connector.connect(
        user="u119126_pollos2LaVengazaDelPollo",
        host="174.136.28.78",
        port="3306",
        password="$ShotGunKin0805",
        database="u119126_pollos2LaVengazaDelPollo"
    )
    cursor = conection.cursor()
    script = "SELECT p.id_producto, p.nombre, pro.id_promocion, pro.descripcion, pro.fecha_de_inicio, pro.fecha_de_finalizacion, tipo.id_tipo_promocion, tipo.nombre, tipo.codigo FROM promocion as pro INNER JOIN producto as p ON p.id_producto = pro.id_producto INNER JOIN tipo_de_promocion tipo ON pro.id_tipo_promocion = tipo.id_tipo_promocion WHERE pro.id_producto = %s and pro.activo = 'V'"
    cursor.execute(script, [idpro])
    results = cursor.fetchone()
    #[0]id_producto, [1]nombre prod, [2]id_promocion,
    #[3]descripcion,[4]fecha_de_inicio,[5]fecha_de_finalizacion,
    #[6]id_tipo_promocion,[7]nombretipo,[8]codigotipo
    if results:
        actual_time = time.localtime()
        timeFormatted = time.strftime("%Y/%m/%d", actual_time)
        timeFormatted=timeFormatted.split("/")
        print(datetime.date(int(timeFormatted[0]), int(timeFormatted[1]), int(timeFormatted[2])))
        print(results[5])
        if results[4] <= datetime.date(int(timeFormatted[0]), int(timeFormatted[1]), int(timeFormatted[2])) <= results[5]:
            ask = messagebox.askokcancel(title="Promocion!", message=f"Hay una promocion con este producto, es de tipo {results[7]}, inicio el {results[4]}, termina el {results[5]} y su codigo es {8}, ¿desea aplicarla?")
            if ask:
                if results[7] == "2X1":
                    flag = False
                    for i in range(producto.main.scrollPreventa.countItems()):
                        if producto.main.scrollPreventa.getItem(i).get_nombre() == producto.nombreProducto + " 2X1":
                            print(f"Encontre un producto con nombre {producto.nombreProducto}")
                            flag = True
                        if flag:
                            producto.main.scrollPreventa.getItem(i).set_cantidad(count)
                            producto.countPromocionesAplicadas += 1
                        else:
                            producto.main.add_venta_frame(nombre=producto.nombreProducto + " " + results[7], cantidad=1, precio=0, id=idpro, promocion=True)




        else:
            print("Tiene promocion pero no esta vigente por lo tanto no es valida :(")
    else:
        print("No tiene promocion")




