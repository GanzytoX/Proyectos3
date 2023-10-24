from Crud.AbstractCRUD import CRUD

if __name__ != "__main__":

    class Rol:
        def __init__(self, nombre:str, id: int = None):
            self.__id = None
            if id is not None:
                self.__id = id
            self.__nombre = nombre

        def _getId(self) -> int:
            return self.__id

        def _setId(self, id:int) -> None:
            if isinstance(id, int) and id > 0 :
                self.__id = id
            else:
                raise ValueError("id must be greater than 0 and must be an string")

        def getNombre(self)-> str :
            return  self.__nombre

        def setNombre(self, nombre:str) -> None:
            if isinstance(nombre, str) and nombre != "" :
                self.__nombre = nombre
            else:
                raise ValueError("Nombre must be a string and can't be an empty string")



    class CrudRol(CRUD):
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
