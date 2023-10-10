#pip install mysql-connector-python
#Esa librería es necesaria para los CRUD

import mysql.connector

class CrudUser:
    def __init__(self):
        self.cursor = None
        self.conexion = None
        self.conectar()

    def conectar(self):
        self.conexion = mysql.connector.connect(
            user="root",
            host="localhost",
            port="3307",
            database="pollosexpress"
        )
        self.cursor = self.conexion.cursor()

    def addUser(self, nombre, apellido, celular, sueldo, id_rol, contraseña=None):
        if contraseña == None:
            SQLScriptAddUser = ("INSERT INTO empleado(nombre, apellido, celular, sueldo, id_rolFK) "
                                f"VALUES('{nombre}', '{apellido}', '{celular}', {sueldo}, {id_rol})")
            self.cursor.execute(SQLScriptAddUser)

        self.conexion.commit()


conexion = CrudUser()
conexion.addUser("Fernando", "Arcos", "9995018941", 155, 1)
