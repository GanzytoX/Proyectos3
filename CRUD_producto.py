from AbstractCRUD import CRUD

if __name__ != "__main__":


    class Producto():
        def __init__(self, nombre: str, descripcion: str, precio: float, imagen):
            self.nombre = nombre
            self.descripcion = descripcion
            self.precio = precio
            self.imagen = imagen

    # Perdón por romper tu clase, asi que la arreglé
    class Crud_Producto(CRUD):
        def __init__(self, conection):
            self.__conection = conection
            self.__cursor = self.__conection.cursor()

        def Create(self, product: Producto):
            script = ("INSERT INTO Producto(nombre, descripcion, precio, imagen)"
                      f"VALUES ({product.nombre}, {product.descripcion}, {product.precio}, {product.imagen}")
            self.__cursor.execute(script) #seria fetch si pidiera datos y execute si ingresa
            self.__conection.commit() # commit siempre que se modifique la tabla

        def Update(self, product: Producto):
            raise NotImplementedError()

        def Delete(self, id):
            raise NotImplementedError()

        def Read(self, id=None):
            raise NotImplementedError()
