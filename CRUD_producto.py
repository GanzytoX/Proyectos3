from AbstractCRUD import CRUD

if __name__ == "__main__":
    class Crud_Producto(CRUD):
        def __init__(self, conection):
            self.__conection = conection
            self.__cursor = self.__conection.cursor()

        def add(self, nombre, descripcion, precio, imagen):
            script = ("INSERT INTO Producto(nombre, descripcion, precio, imagen)"
                      f"VALUES ({nombre}, {descripcion}, {precio}, {imagen}")
            self.__cursor.execute(script) #seria fetch si pidiera datos y execute si ingresa
            self.__conection.commit() # commit siempre que se modifique la tabla

        def Update(self, id):
            pass
        def Delete(self, id):
            pass
        def get(self, id):
            pass