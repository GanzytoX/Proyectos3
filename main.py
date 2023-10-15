from CRUD_Usuario import CrudEmpleado, Empleado
from CRUD_producto import CrudProducto, Producto
import mysql.connector

import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

if __name__ == "__main__":
    conection = mysql.connector.connect(
        user="root",
        host="localhost",
        port="3307",
        database="pollosExpress"
    )

    productManager = CrudProducto(conection)
    with open('img/logo.png', 'rb') as archivo:
        imagen = archivo.read()
    
    #productManager.Create(Producto("Papitas", "Estan ricas", 25.48, imagen))

    script = "SELECT * FROM producto WHERE id_producto = 1"
    cursor = conection.cursor()
    cursor.execute(script)
    data = cursor.fetchone()

    with open("filename.png", 'wb') as file:
        file.write(data[4])

    #userManager = CrudEmpleado(conection)
    #userManager.Create(Empleado("Dios", "Si", "quiza", "8788", 25000, 1, "si"))
    #print(userManager.iniciarSesion("2788", "si"))
    #empleadito = Empleado("Diosito", "Si", "8788", 25000, 1, "si", 12)
    #userManager.Update(empleadito)
    #gestorProducto = Crud_Producto(conection)
    #gestorProducto.add("si", "a veces", 200, "img/mimikiu.png")


