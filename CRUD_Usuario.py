# #pip install mysql-connector-python
# Esa librería es necesaria para los CRUD
import mysql.connector.errors

from AbstractCRUD import CRUD

if __name__ != "__main__":

    class Empleado:
        def __init__(self, nombre, apellido, celular, sueldo, id_rol, contraseña=None, id=None):
            if id is not None:
                self.id = id
            if contraseña is not None:
                self.contraseña = contraseña
            self.nombre = nombre
            self.apellido = apellido
            self.celular = celular
            self.sueldo = sueldo
            self.id_rol = id_rol



    class CrudEmpleado(CRUD):

        def __init__(self, conexion):
            self.__conexion = conexion
            self.__cursor = self.__conexion.cursor()

        def Create(self, empleado: Empleado) -> None:
            if empleado.contraseña is None:
                SQLScript = ("INSERT INTO empleado(nombre, apellido, celular, sueldo, id_rolFK) "
                             f"VALUES('{empleado.nombre}', '{empleado.apellido}', '{empleado.celular}', {empleado.sueldo}, {empleado.id_rol})")
                self.__cursor.execute(SQLScript)
            else:
                SQLScript = ("INSERT INTO empleado(nombre, apellido, celular, sueldo, id_rolFK, contraseña) "
                             f"VALUES('{empleado.nombre}', '{empleado.apellido}', '{empleado.celular}', {empleado.sueldo}, {empleado.id_rol}, '{empleado.contraseña}')")
                self.__cursor.execute(SQLScript)

            self.__conexion.commit()

        def Read(self, id=None):
            raise NotImplementedError()

        def Delete(self, id) -> None:
            SQLScript = f"DELETE FROM empleado WHERE id_Empleado = {id}"
            self.__cursor.execute(SQLScript)
            self.__conexion.commit()

        def Update(self, empleado: Empleado) -> None:
            SQLScript = (f"UPDATE empleado SET nombre = '{empleado.nombre}', apellido = '{empleado.apellido}',"
                         f"celular = '{empleado.celular}', sueldo = {empleado.sueldo}, id_rolFK = {empleado.id_rol}, contraseña = '{empleado.contraseña}'"
                         f"WHERE id_Empleado = {empleado.id}")
            self.__cursor.execute(SQLScript)
            self.__conexion.commit()
        def iniciarSesion(self, numeroTelefono, contraseña) -> bool:
            SQLScript = f"SELECT contraseña FROM empleado WHERE celular = {numeroTelefono}"
            self.__cursor.execute(SQLScript)
            result = self.__cursor.fetchone()

            if result:
                if result[0] == contraseña:
                    return True
                else:
                    print("Inicio de sesion fallido")
                    return False
            else:
                raise DataException("Usuario no encontrado en la base de datos")


class DataException(Exception):
    def __int__(self, mensaje):
        super().__init__(mensaje)
