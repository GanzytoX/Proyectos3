from Crud.AbstractCRUD import CRUD
from Drive.drive import DriveManager


if __name__ != "__main__":

    class Producto:
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
            super().__init__(conection)
            self.__driveConnection = DriveManager()

        def Create(self, product: Producto):
            script = "INSERT INTO producto(nombre, descripcion, precio, imagen) VALUES (%s, %s, %s, %s)"
            datos_producto = (product.nombre, product.descripcion, product.precio, product._driveCode)
            self._CRUD__cursor.execute(script, datos_producto) #seria fetch si pidiera datos
            self._CRUD__conection.commit() # commit siempre que se modifique la tabla

        def Update(self, id, product: Producto):
            script = ("UPDATE producto "
                      "SET nombre = %s, descripcion = %s, precio = %s, imagen = %s "
                      "WHERE id_producto = %s")
            datos_producto = (product.nombre, product.descripcion, product.precio, product._driveCode, id)

            producto = self.Read(id)
            self.__driveConnection.deleteImage(producto._driveCode)
            self._CRUD__cursor.execute(script, datos_producto)
            self._CRUD__conection.commit()

        def Delete(self, id):
            if isinstance(id, int):
                producto = self.Read(id)
                self.__driveConnection.deleteImage(producto._driveCode)
                script = f"DELETE FROM producto WHERE id_producto = {id}"
                self._CRUD__cursor.execute(script)
                self._CRUD__conection.commit()
            else:
                raise ValueError("Id must be an integer")

        def Read(self, id=None, condition:str=None):
            if id is None and condition is None:
                script = "SELECT * from producto"
                self._CRUD__cursor.execute(script)
                result = self._CRUD__cursor.fetchall()
                productos = []
                for resultado in result:
                    route = f"../userImages/product_{resultado[1]}.png"
                    self.__driveConnection.downloadImage(resultado[4], route)
                    producto = Producto(resultado[1], resultado[2], resultado[3], route, resultado[0], driveCode=resultado[4])
                    productos.append(producto)
                return productos
            elif isinstance(id, int):
                script = f"SELECT * from producto WHERE id_producto = {id}"
                self._CRUD__cursor.execute(script)
                resultado = self._CRUD__cursor.fetchone()
                route = f"../userImages/product_{resultado[1]}.png"
                self.__driveConnection.downloadImage(resultado[4], route)
                producto = Producto(resultado[1], resultado[2], resultado[3], route, resultado[0], driveCode=resultado[4])
                return producto

            elif not isinstance(id, int):
                raise ValueError("Id must be an integer")

        def UploadImage(self, url):
            id = self.__driveConnection.uploadImage(url)
            return id

        def countProducts(self):
            script = f"SELECT COUNT(*) from producto"
            self._CRUD__cursor.execute(script)
            result = self._CRUD__cursor.fetchone()
            return result

        def getIds(self):
            script = f"SELECT id_producto from producto"
            self._CRUD__cursor.execute(script)
            result = self._CRUD__cursor.fetchall()
            return result
