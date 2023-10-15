from AbstractCRUD import CRUD
from PIL import Image
from io import BytesIO


if __name__ != "__main__":


    class Producto():
        def __init__(self, nombre: str, descripcion: str, precio: float, imagen: any, id: int = None ):
            self.id = 0
            if id is not None:
                self.id = id
            self.nombre = nombre
            self.descripcion = descripcion
            self.precio = precio
            self.imagen = imagen


    class CrudProducto(CRUD):
        def __init__(self, conection):
            self.__conection = conection
            self.__cursor = self.__conection.cursor()

        def Create(self, product):
            script = "INSERT INTO producto(nombre, descripcion, precio, imagen) VALUES (%s, %s, %s, %s)"
            datos_producto = (product.nombre, product.descripcion, product.precio, product.imagen)
            self.__cursor.execute(script, datos_producto) #seria fetch si pidiera datos
            self.__conection.commit() # commit siempre que se modifique la tabla

        def Update(self, product: Producto):
            script = ("UPDATE producto "
                      "SET nombre = %s, descripcion = %s, precio = %s, imagen = %s "
                      "WHERE id_producto = %s")
            datos_producto = (product.nombre, product.descripcion, product.precio, product.imagen, product.id)
            self.__cursor.execute(script, datos_producto)
            self.__conection.commit()

        def Delete(self, id):
            script = f"DELETE FROM producto WHERE id = {id}"
            self.__cursor.execute(script)
            self.__conection.commit()

        def Read(self, id=None):
            if id is None:
                script = "SELECT * from producto"
                self.__cursor.execute(script)
                result = self.__cursor.fetchall()
                productos = []
                for resultado in result:
                    imgBytes = BytesIO(resultado[4])
                    img = Image.open(imgBytes)

                    producto = Producto(resultado[1], resultado[2], resultado[3], img, resultado[0])
                    productos.append(producto)
                return productos
            elif id is int:
                script = f"SELECT * from producto WHERE id_empleado = {id}"
                self.__cursor.execute(script)
                resultado = self.__cursor.fetchone()
                imgBytes = BytesIO(resultado[4])
                img = Image.open(imgBytes)
                producto = Producto(resultado[1], resultado[2], resultado[3], img, resultado[0])
                return producto
