from Crud.AbstractCRUD import CRUD

if __name__ != "__main__":

    class Rol:
        def __init__(self, nombre:str, id: int = None):
            self.__id = None
            if id is not None:
                self._setId(id)
            self.setNombre(nombre)

        def _getId(self) -> int:
            return self.__id

        def _setId(self, id:int) -> None:
            if isinstance(id, int) and id > 0 :
                print("puse los indices")
                self.__id = id
            else:
                raise ValueError("id must be an int and must be greater than 0")

        def getNombre(self) -> str:
            return self.__nombre

        def setNombre(self, nombre: str) -> None:
            if isinstance(nombre, str) and nombre != "":
                self.__nombre = nombre
            else:
                raise ValueError("Nombre must be a string and can't be an empty string")

    class CrudRol(CRUD):
        def __init__(self, conection):
            self.__conection = conection
            self.__cursor = self.__conection.cursor()

        def Read(self, id=None, condition=None):
            if id is None and condition is None:
                script = f"SELECT * FROM rol"
                self.__cursor.execute(script)
                results = self.__cursor.fetchall()
                roles = []
                for result in results:
                    roles.append(Rol(id=result[0], nombre=result[1]))
                return roles
            elif id is not None and condition is None:
                script = f"SELECT * FROM rol WHERE id_rol={id}"
                self.__cursor.execute(script)
                results = self.__cursor.fetchone()
                return Rol(results[0], results[1])
            elif id is None and condition is not None:
                raise NotImplementedError()
            else:
                raise ValueError("Can only take either an id or a condition, not both")

        def Delete(self, id: int):
            if isinstance(id, int):
                script = f"DELETE FROM rol WHERE id_rol={id}"
                self.__cursor.execute(script)
                self.__conection.commit()
            else:
                raise ValueError("id must be an Int")

        def Update(self, id: int, object: Rol):
            if isinstance(id, int):
                if isinstance(object, Rol):
                    script = f"UPDATE rol SET nombre='{object.getNombre()}' WHERE id_rol={id}"
                    self.__cursor.execute(script)
                    self.__conection.commit()
                else:
                    raise ValueError("object was expected to be type: Rol")
            else:
                raise ValueError("id must be an Int")

        def Create(self, rol: Rol):
            script = ("INSERT INTO rol(nombre)"
                      f"VALUES('{rol.getNombre()}')")
            self.__cursor.execute(script)
            self.__conection.commit()
""""
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
"""