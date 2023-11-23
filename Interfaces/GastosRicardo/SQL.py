import mysql.connector


def conectar():  # -------------------------------------------
    conexion = mysql.connector.connect(
        user="u119126_pollos2LaVengazaDelPollo",
        host="174.136.28.78",
        port="3306",
        password="$ShotGunKin0805",
        database="u119126_pollos2LaVengazaDelPollo")
    if conexion.is_connected():
        print("Conexión +")
    return conexion


def consulta_gastos(conexion): #     -----     Read all
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM gasto")
    for bd in cursor:
        print(bd)
    cursor.close()


def consulta_gastos_uno_id(conexion, id):  #     -----     Consulta por id
    consulta = '''SELECT * FROM gasto WHERE id_gasto = %s'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (id, ))
    resultado = cursor.fetchall()
    print(resultado)
    return resultado

def consulta_gastos_uno_tit(conexion, tit):  #     -----     Consulta por titulo
    consulta = '''SELECT * FROM gasto WHERE titulo = %s'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (tit,))
    resultado = cursor.fetchall()
    print(resultado)
    return resultado

def consulta_gastos_uno_desc(conexion, des):  #     -----     Consulta por descripción
    consulta = '''SELECT * FROM gasto WHERE descripcion = %s'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (des,))
    resultado = cursor.fetchall()
    print(resultado)
    return resultado


def consulta_gastos_uno_monto(conexion, monto):  #     -----     Consulta por monto
    consulta = '''SELECT * FROM gasto WHERE monto = %s'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (monto,))
    resultado = cursor.fetchall()
    print(resultado)
    return resultado


def consulta_gastos_uno_date(conexion, date):  #     -----     Consulta por fecha
    consulta = '''SELECT * FROM gasto WHERE fecha = %s'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (date,))
    resultado = cursor.fetchall()
    print(resultado)
    return resultado


def consulta_gastos_uno_emp(conexion, emp):  #     -----     Consulta por id de empleado
    consulta = '''SELECT * FROM gasto WHERE id_empleado = %s'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (emp,))
    resultado = cursor.fetchall()
    print(resultado)
    return resultado


def eliminar_uno(conexion, id): #     -----     Eliminar por id de empleado
    consulta = '''DELETE FROM gasto WHERE id_gasto = %s'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (id,))
    conexion.commit()
    cursor.close()


def actualizar_uno(conexion, dato, id):
    consulta = '''UPDATE gasto SET descripcion = %s WHERE id_gasto = %s'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (dato, id))
    conexion.commit()
    cursor.close()


def agregar(conexion, tit, des, monto, date, id_e):#     -----     Agregar empleado
    consulta = '''INSERT INTO gasto(titulo, descripcion, monto, fecha, id_empleado) VALUES (%s, %s, %s, %s, %s)'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (tit, des, monto, date, id_e))
    conexion.commit()
    cursor.close()


def actualizar_todo(conexion, tit, dato, monto, date, emp, id):
    consulta = '''UPDATE gasto SET titulo = %s, descripcion = %s, monto = %s, fecha = %s, id_empleado = %s WHERE id_gasto = %s'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (tit, dato, monto, date, emp, id))
    conexion.commit()
    cursor.close()


def id_max():
    consulta = '''SELECT MAX(id_gasto) FROM gasto'''
    cursor = conexion.cursor()
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    num = int(resultado[0][0])
    return num+1


global r
conexion = conectar()
#consulta_gastos(conexion)
#actualizar_uno(conexion, "test7", 7, )
#actualizar_todo(conexion, "test", 234, '2023/02/01', 4, 6)
r = consulta_gastos_uno_id(conexion, 2)
#consulta_gastos_uno_desc()
#consulta_gastos_uno_monto()
#consulta_gastos_uno_date()
#consulta_gastos_uno_emp(conexion, 2)
#print(r[2][0])
#agregar(conexion,8,'gasto8', 48, '2023/02/01', 4)
print(r[0][5])