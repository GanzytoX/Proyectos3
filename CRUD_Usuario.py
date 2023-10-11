# #pip install mysql-connector-python
# Esa librería es necesaria para los CRUD

import mysql.connector
from AbstractCRUD import CRUD

if __name__ != "__main__":
    class CrudEmpleado(CRUD):

        def get(self, id=None):
            raise NotImplementedError()

        def __init__(self, conexion):
            self.__conexion = conexion
            self.__cursor = self.__conexion.cursor()

        def add(self, nombre, apellido, celular, sueldo, id_rol, contraseña=None) -> None:
            if contraseña is None:
                SQLScript = ("INSERT INTO empleado(nombre, apellido, celular, sueldo, id_rolFK) "
                             f"VALUES('{nombre}', '{apellido}', '{celular}', {sueldo}, {id_rol})")
                self.__cursor.execute(SQLScript)
            else:
                SQLScript = ("INSERT INTO empleado(nombre, apellido, celular, sueldo, id_rolFK, contraseña) "
                             f"VALUES('{nombre}', '{apellido}', '{celular}', {sueldo}, {id_rol}, '{contraseña}')")
                self.__cursor.execute(SQLScript)

            self.__conexion.commit()

        def Delete(self, id) -> None:
            SQLScript = f"DELETE FROM empleado WHERE id_Empleado = {id}"
            self.__cursor.execute(SQLScript)
            self.__conexion.commit()

        def Update(self, id) -> None:
            raise NotImplementedError()

        def iniciarSesion(self, numeroTelefono, contraseña) -> bool:
            SQLScript = f"SELECT contraseña FROM empleado WHERE celular = {numeroTelefono}"
            self.__cursor.execute(SQLScript)
            result = self.__cursor.fetchone()

            if result:
                print(result[0])
                if result[0] == contraseña:
                    print("Iniciando sesion")
                else:
                    print("Inicio de sesion fallido")





else:
    print("Ejecutado como main")
