from CRUD_Usuario import CrudEmpleado
from CRUD_producto import Crud_Producto
import mysql.connector

if __name__ == "__main__":
    conection = mysql.connector.connect(
        user="root",
        host="localhost",
        port="3306",
        database="basededatos_polleria"
    )
    userManager = CrudEmpleado(conection)
    #userManager.add("Diego", "Si", "8788", 25000, 1, "si")
    userManager.iniciarSesion("8788", "si")
    gestorProducto = Crud_Producto(conection)
    gestorProducto.add("si", "a veces", 200, "img/mimikiu.png")
