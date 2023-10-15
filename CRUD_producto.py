#pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
from AbstractCRUD import CRUD

if __name__ != "__main__":


    class Producto():
        def __init__(self, nombre: str, descripcion: str, precio: float, imagen: any):
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
            self.__cursor.execute(script, datos_producto) #seria fetch si pidiera datos y execute si ingresa
            self.__conection.commit() # commit siempre que se modifique la tabla

        def Update(self, product: Producto):
            raise NotImplementedError()

        def Delete(self, id):
            raise NotImplementedError()

        def Read(self, id=None):
            raise NotImplementedError()
