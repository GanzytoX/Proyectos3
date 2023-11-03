import mysql.connector.errors
from Crud.AbstractCRUD import CRUD

class Promocion():
    def __init__(self,id, id_producto : int, descripcion : str, fechaInicio : str, fechaFinal : str, id_tipopromocion : int ):
        self.id = None
        if id is not None:
            self.id = id
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.fechainicio = fechaInicio
        self.fechafinal = fechaFinal
        self.id_tipopromocion = id_tipopromocion


class CRUDPromociones(CRUD):
    def __init__(self, conection):
        super().__init__(conection)
        self.__conection = conection
        self.__cursor = self.__conection.cursor()

    def Create(self, promocion):
        script = "INSERT INTO promocion(id_producto, descripcion, fecha_de_inicio, fecha_de_finalizacion, id_tipo_promocion) VALUES (%s, %s, %s, %s,%s)"
        datos_promocion = (promocion.id_producto, promocion.descripcion, promocion.fechainicio, promocion.fechafinal, promocion.id_tipopromocion)
        self.__cursor.execute(script, datos_promocion)  # seria fetch si pidiera datos
        self.__conection.commit()  # commit siempre que se modifique la tabla

    def Read(self, id=None, condition=None):
        if id is None:
            script = "SELECT * from promocion"
            self.__cursor.execute(script)
            result = self.__cursor.fetchall()
            promociones = []
            for resultado in result:
                promocion = Promocion(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[0])
                promociones.append(promocion)
            return promociones
        elif isinstance(id, int):
            script = f"SELECT * from promocion WHERE id_promocion = {id}"
            self.__cursor.execute(script)
            resultado = self.__cursor.fetchone()
            promocion = Promocion(resultado[1], resultado[2], resultado[3], resultado[4], resultado[0])
            return promocion
        else:
            raise ValueError("Id must be an integer")

    def Delete(self, id):
        if isinstance(id, int):
            oferta = self.Read(id)
            script = f"DELETE FROM promocion WHERE id_promocion = {id}"
            self.__cursor.execute(script)
            self.__conection.commit()
        else:
            raise ValueError("Id must be an integer")

    def Update(self, id: int, promocion: Promocion):
        script = ("UPDATE promocion "
                  "SET id_producto = %s, descripcion = %s, fecha_de_inicio = %s, fecha_de_finalizacion = %s, id_promocion = %s  "
                  "WHERE id_promocion = %s")
        datos_promocion = (promocion.id_producto, promocion.descripcion, promocion.fechainicio, promocion.fechafinal, promocion.id, id)
        promocion = self.Read(id)
        self.__cursor.execute(script, datos_promocion)
        self.__conection.commit()

