from CRUD_Usuario import CrudEmpleado, Empleado
from CRUD_producto import Crud_Producto
import mysql.connector

if __name__ == "__main__":
    conection = mysql.connector.connect(
        user="root",
        host="localhost",
        port="3307",
        database="pollosExpress"
    )

    userManager = CrudEmpleado(conection)
    #userManager.Create(Empleado("Dios", "Si", "8788", 25000, 1, "si"))
    #print(userManager.iniciarSesion("2788", "si"))
    empleadito = Empleado("Diosito", "Si", "8788", 25000, 1, "si", 12)
    userManager.Update(empleadito)
    #gestorProducto = Crud_Producto(conection)
    #gestorProducto.add("si", "a veces", 200, "img/mimikiu.png")
