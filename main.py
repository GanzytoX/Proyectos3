from Crud.CRUD_producto import CrudProducto, Producto
import mysql.connector
from Crud.CRUD_Usuario import *
from PIL import Image, ImageTk
from Crud.CRUDOfertas import CRUDPromociones, Promocion
from Crud.CRUD_Rol import *


#Comenten el port y la contraseña cuando lo vayan a utilizar
if __name__ == "__main__":
    connection = mysql.connector.connect(
        user="sql5660121",
        host="sql5.freesqldatabase.com",
        port="3306",
        password="GWes4WXpXH",
        database="sql5660121"
    )
    #NO ME BORREN DE AQUI SON PRUEBAS QUE USARE

    #
    #with open('img/logo.png', 'rb') as archivo:
        #imagen = archivo.read()
    
    #productManager.Create(Producto("Papitas", "Estan ricas", 25.48, imagen))

    #script = "SELECT * FROM producto WHERE id_producto = 1"
    #cursor = conection.cursor()
    #cursor.execute(script)
    #data = cursor.fetchone()

    #with open("filename.png", 'wb') as file:
        #file.write(data[4])

    #userManager = CrudEmpleado(conection)
    #userManager.Create(Empleado("victor","Escalante","Alpuche","9994413308",40000,1,True,"Si"))
    #userManager.Create(Empleado("Dios", "Si", "quiza", "8788", 25000, 1, "si"))
    #print(userManager.iniciarSesion("2788", "si"))
    #empleadito = Empleado("Diosito", "Si", "8788", 25000, 1, "si", 12)
    #userManager.Update(empleadito)
    #gestorProducto = CrudProducto(conection)
    #gestorProducto.Create(Producto("si", "a veces", 200, "img/mimikiu.png"))

    #productManager = CrudProducto(conection)
    #with open('img/logo.png', 'rb') as archivo:
        #imagen = archivo.read()
    #productManager.Update(Producto("Papitas", "Estan ricas", 26, imagen, 1))
    """""
    productManager = CrudProducto(conection)
    productos = productManager.Read()
    productos[0].imagen.show()
    
    productManager = CrudProducto(conection)
    productos = productManager.Read(1)
    productos.imagen.show()
    """""
    #productManager = CrudProducto(conection)
    #productManager.Create(Producto("Si", "Takvez", 69.420,driveCode= productManager.UploadImage("img/mimikiu.png")["id"]))
    #productManager.Read(1)
    #productManager.Delete(3)


    #  promocionManager = CRUDPromociones(conection)
    #  promocionManager.Create(Promocion(6, "La verdad no se si funciones", "2023/10/21","2023/10/21",1))

    #for i in promocionManager.Read():
    #    print(i.descripcion)

    #promocionManager.Update(5, Promocion(1,"Acabo de actualizar la prueba", "2023/10/20", "2023/10/29",1,2))

    #promocionManager.Delete(6)

    #roles = CrudRol(conection)
    #print()
    #roles.Create(Rol("De manzana"))
    #roles.Delete("a")
    #roles.Update(1, Rol("De sus"))
    #roles.Read(1)

    #imagen = Image.open("img/noImage.jpg")
    #imagen.thumbnail((200, 200))
    #imagen.save("img/noImage.jpg")

    promocionManager = CRUDPromociones(connection)
    promocionManager.Create(Promocion(1, 1,"Ya duermete", "2023/10/21","2023/10/21",1))