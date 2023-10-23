# #pip install mysql-connector-python
# Esa librería es necesaria para los CRUD
import mysql.connector.errors

from Crud.AbstractCRUD import CRUD

if __name__ != "__main__":

    class Empleado:
        def __init__(self, nombre, apellido_paterno, apellido_materno, celular, sueldo, id_rol, administrator: bool, contraseña=None, id=None):
            self.contraseña = None
            self.id = None
            if id is not None:
                self.id = id
            if contraseña is not None:
                self.contraseña = contraseña
            self.nombre = nombre
            self.apellido_paterno = apellido_paterno
            self.apellido_materno = apellido_materno
            self.celular = celular
            self.sueldo = sueldo
            self.id_rol = id_rol
            self.administrador = administrator


    class CrudEmpleado(CRUD):

        def __init__(self, conexion):
            self.__conexion = conexion
            self.__cursor = self.__conexion.cursor()

        def Create(self, empleado: Empleado) -> None:
            if empleado.contraseña is None:
                SQLScript = ("INSERT INTO empleado(nombre,apellido_paterno, apellido_materno, celular, sueldo, id_rol, administrator) "
                             f"VALUES('{empleado.nombre}', '{empleado.apellido_paterno}', '{empleado.apellido_materno}', '{empleado.celular}', {empleado.sueldo}, {empleado.id_rol}, {empleado.administrador})")
                self.__cursor.execute(SQLScript)
            else:
                SQLScript = ("INSERT INTO empleado(nombre, apellido_paterno, apellido_materno, celular, sueldo, id_rol, contraseña, administrator)"
                             f"VALUES('{empleado.nombre}', '{empleado.apellido_paterno}', '{empleado.apellido_materno}', '{empleado.celular}', {empleado.sueldo}, {empleado.id_rol}, '{empleado.contraseña}', {empleado.administrador})")
                self.__cursor.execute(SQLScript)

            self.__conexion.commit()

        def Read(self, id=None, condition=None):
            if id is None and condition is None:
                script = "SELECT empleado.*, rol.nombre FROM empleado LEFT JOIN rol ON empleado.id_rol = rol.id_rol;"
                self.__cursor.execute(script)
                result = self.__cursor.fetchall()
                empleados = []
                for empleado in result:
                    empleados.append(Empleado(nombre=empleado[1],
                                              apellido_paterno=empleado[2],
                                              apellido_materno=empleado[3],
                                              celular=empleado[4],
                                              sueldo=empleado[5],
                                              id_rol=empleado[9],
                                              contraseña=empleado[7],
                                              administrator=empleado[8]))
                return empleados

        def Delete(self, id) -> None:
            SQLScript = f"DELETE FROM empleado WHERE id_empleado = {id}"
            self.__cursor.execute(SQLScript)
            self.__conexion.commit()

        def Update(self, id, empleado: Empleado) -> None:
            SQLScript = (f"UPDATE empleado SET nombre = '{empleado.nombre}', apellido_paterno = '{empleado.apellido_paterno}', apellido_materno = '{empleado.apellido_materno}'"
                         f"celular = '{empleado.celular}', sueldo = {empleado.sueldo}, id_rol = {empleado.id_rol}, contraseña = '{empleado.contraseña}', administrator = {empleado.administrador}"
                         f"WHERE id_Empleado = {id}")
            self.__cursor.execute(SQLScript)
            self.__conexion.commit()

        def iniciarSesion(self, numeroTelefono, contraseña) -> (bool, bool):
            SQLScript = f"SELECT pass, administrator FROM empleado WHERE celular = '{numeroTelefono}'"
            self.__cursor.execute(SQLScript)
            result = self.__cursor.fetchone()

            if result:
                if result[0] == contraseña:
                    return True, result[1]
                else:
                    print("Inicio de sesion fallido")
                    return False, False
            else:
                raise DataException("Usuario no encontrado en la base de datos")


class DataException(Exception):
    def __int__(self, mensaje):
        super().__init__(mensaje)
