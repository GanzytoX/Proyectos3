from Crud.AbstractCRUD import CRUD
from Drive.drive import DriveManager


if __name__ != "__main__":

    class Producto():
        def __init__(self, nombre: str, descripcion: str, precio: float, imagen: str = None, id: int = None, driveCode: str = None):
            self.id = None
            if id is not None:
                self.id = id
            self.nombre = nombre
            self.descripcion = descripcion
            self.precio = precio
            if imagen is not None:
                self.imagen = imagen
            self._driveCode = None
            if driveCode is not None:
                self._driveCode = driveCode


    class CrudProducto(CRUD):
        def __init__(self, conection):
            self.__conection = conection
            self.__cursor = self.__conection.cursor()
            self.__driveConnection = DriveManager()

        def Create(self, product: Producto):
            script = "INSERT INTO producto(nombre, descripcion, precio, imagen) VALUES (%s, %s, %s, %s)"
            datos_producto = (product.nombre, product.descripcion, product.precio, product.driveCode)
            self.__cursor.execute(script, datos_producto) #seria fetch si pidiera datos
            self.__conection.commit() # commit siempre que se modifique la tabla

        def Update(self, id, product: Producto):
            script = ("UPDATE producto "
                      "SET nombre = %s, descripcion = %s, precio = %s, imagen = %s "
                      "WHERE id_producto = %s")
            datos_producto = (product.nombre, product.descripcion, product.precio, product.imagen, id)

            producto = self.Read(id)
            self.__driveConnection.deleteImage(producto._driveCode)
            self.__cursor.execute(script, datos_producto)
            self.__conection.commit()

        def Delete(self, id):
            if isinstance(id, int):
                producto = self.Read(id)
                self.__driveConnection.deleteImage(producto._driveCode)
                script = f"DELETE FROM producto WHERE id_producto = {id}"
                self.__cursor.execute(script)
                self.__conection.commit()
            else:
                raise ValueError("Id must be an integer")

        def Read(self, id=None, condition:str=None):
            if id is None and condition is None:
                script = "SELECT * from producto"
                self.__cursor.execute(script)
                result = self.__cursor.fetchall()
                productos = []
                for resultado in result:
                    route = f"img/product_{resultado.name}"
                    self.__driveConnection.downloadImage(resultado[4], route)

                    producto = Producto(resultado[1], resultado[2], resultado[3], route, resultado[0], driveCode=resultado[4])
                    productos.append(producto)
                return productos
            elif isinstance(id, int):
                script = f"SELECT * from producto WHERE id_producto = {id}"
                self.__cursor.execute(script)
                resultado = self.__cursor.fetchone()
                route = f"img/product_{resultado[1]}.png"
                print(resultado[4])
                self.__driveConnection.downloadImage(resultado[4], route)
                producto = Producto(resultado[1], resultado[2], resultado[3], route, resultado[0], driveCode=resultado[4])
                return producto

            elif not isinstance(id, int):
                raise ValueError("Id must be an integer")

        def UploadImage(self, url):
            id = self.__driveConnection.uploadImage(url)
            return id
