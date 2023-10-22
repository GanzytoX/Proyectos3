#from Crud.CRUD_producto import CrudProducto, Producto
import mysql.connector
from PIL import Image, ImageTk
from Crud.CRUDOfertas import CRUDPromociones, Promocion


#Comenten el port y la contraseña cuando lo vayan a utilizar
if __name__ == "__main__":
    conection = mysql.connector.connect(
        user="root",
        host="localhost",
        #port="3307",
        port="3306",
        password="0123456789",
        database="pollosexpress"
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
    #userManager.Create(Empleado("Dios", "Si", "quiza", "8788", 25000, 1, "si"))
    #print(userManager.iniciarSesion("2788", "si"))
    #empleadito = Empleado("Diosito", "Si", "8788", 25000, 1, "si", 12)
    #userManager.Update(empleadito)
    #gestorProducto = Crud_Producto(conection)
    #gestorProducto.add("si", "a veces", 200, "img/mimikiu.png")

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
    #productManager.Create(Producto("Si", "Takvez", 69.420, productManager.UploadImage("img/mimikiu.png")["id"]))
    #productManager.Read(1)
    #productManager.Delete(3)

    promocionManager = CRUDPromociones(conection)
    #promocionManager.Create(Promocion(1, "Esto es una prueba 2", "2023/10/21","2023/10/21",1))

    #for i in promocionManager.Read():
    #    print(i.descripcion)

    #promocionManager.Update(5, Promocion(1,"Acabo de actualizar la prueba", "2023/10/20", "2023/10/29",1,2))

    #promocionManager.Delete(6)
