# #pip install mysql-connector-python
# Esa librería es necesaria para los CRUD

from Crud.AbstractCRUD import CRUD
from  Objects.Empleados import Empleado

if __name__ != "__main__":

    class CrudEmpleado(CRUD):

        def __init__(self, conexion):
            super().__init__(conexion)

        def Create(self, empleado: Empleado) -> None:
            if empleado.getContraseña() is None:
                SQLScript = ("INSERT INTO empleado(nombre,apellido_paterno, apellido_materno, celular, sueldo, id_rol, administrator) "
                             f"VALUES('{empleado.getNombre()}', '{empleado.getApellido_paterno()}', "
                             f"'{empleado.getApellido_materno()}', '{empleado.getCelular()}', {empleado.getSueldo()}, "
                             f"{empleado.getIdRol()}, {empleado.getAdministrador()})")
                self._cursor.execute(SQLScript)
            else:
                SQLScript = ("INSERT INTO empleado(nombre, apellido_paterno, apellido_materno, celular, sueldo, id_rol, pass, administrator)"
                             f"VALUES('{empleado.getNombre()}', '{empleado.getApellido_paterno()}', "
                             f"'{empleado.getApellido_materno()}', '{empleado.getCelular()}', {empleado.getSueldo()}, "
                             f"{empleado.getIdRol()}, '{empleado.getContraseña()}', {empleado.getAdministrador()})")
                self._cursor.execute(SQLScript)

            self._conection.commit()

        def Read(self, id: int = None, condition: str = None) -> list[Empleado] | Empleado:
            self._conection.commit()
            if id is None and condition is None:
                script = "SELECT empleado.*, rol.nombre FROM empleado LEFT JOIN rol ON empleado.id_rol = rol.id_rol;"
                self._cursor.execute(script)
                result = self._cursor.fetchall()
                empleados = []
                for empleado in result:
                    empleados.append(Empleado(nombre=empleado[1],
                                              apellido_paterno=empleado[2],
                                              apellido_materno=empleado[3],
                                              celular=empleado[4],
                                              sueldo=empleado[5],
                                              id_rol=empleado[9],
                                              contraseña=empleado[7],
                                              administrator=empleado[8],
                                              id=empleado[0]))
                return empleados
            elif id is not None and condition is None:
                script = (f"SELECT empleado.*, rol.nombre FROM empleado LEFT JOIN rol ON empleado.id_rol = rol.id_rol"
                          f" WHERE id_empleado = {id};")
                self._cursor.execute(script)
                empleado = self._cursor.fetchone()
                return Empleado(nombre=empleado[1],
                                              apellido_paterno=empleado[2],
                                              apellido_materno=empleado[3],
                                              celular=empleado[4],
                                              sueldo=empleado[5],
                                              id_rol=empleado[9],
                                              contraseña=empleado[7],
                                              administrator=empleado[8],
                                              id=empleado[0])

        def Delete(self, id) -> None:
            SQLScript = f"DELETE FROM empleado WHERE id_empleado = {id}"
            self._cursor.execute(SQLScript)
            self._conection.commit()

        def Update(self, id, empleado: Empleado) -> None:

            SQLScript = (f"UPDATE empleado SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, "
                             f"celular = %s, sueldo = %s, id_rol = %s, pass = %s, administrator = %s "
                             f"WHERE id_Empleado = {id}")
            valores = (empleado.getNombre(), empleado.getApellido_paterno(), empleado.getApellido_materno(),
                       empleado.getCelular(), empleado.getSueldo(), empleado.getIdRol(), empleado.getContraseña(),
                       empleado.getAdministrador())

            self._cursor.execute(SQLScript, valores)
            self._conection.commit()

        def iniciarSesion(self, numeroTelefono, contraseña) -> (bool, bool):
            self._conection.commit()
            SQLScript = f"SELECT pass, administrator FROM empleado WHERE celular = '{numeroTelefono}'"
            self._cursor.execute(SQLScript)
            result = self._cursor.fetchone()

            if result:
                if result[0] == contraseña:
                    return True, result[1]
                else:
                    print("Inicio de sesion fallido")
                    return False, False
            else:
                raise DataException("Usuario no encontrado en la base de datos")

        def find_similar(self, substring: str):
            self._conection.commit()
            script = (f"SELECT empleado.*, rol.nombre FROM empleado LEFT JOIN rol ON empleado.id_rol = rol.id_rol"
                      f" WHERE empleado.nombre LIKE '{substring}%';")
            self._cursor.execute(script)
            result = self._cursor.fetchall()
            empleados = []
            for empleado in result:
                empleados.append(Empleado(nombre=empleado[1],
                                          apellido_paterno=empleado[2],
                                          apellido_materno=empleado[3],
                                          celular=empleado[4],
                                          sueldo=empleado[5],
                                          id_rol=empleado[9],
                                          contraseña=empleado[7],
                                          administrator=empleado[8],
                                          id=empleado[0]))
            return empleados


class DataException(Exception):
    def __int__(self, mensaje):
        super().__init__(mensaje)
