import mysql


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


def consulta_productos(conexion): # Recibe todos los datos de la tabla
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM inventario")
    for prod in cursor:
        print(prod)
    cursor.close()

def consulta_productos_porID(conexion, id): # Se hace una consulta de los productos por ID
    consulta = '''SELECT * FROM inventario WHERE id = %s'''
    cursor = conexion.cursor()
    cursor.execute(consulta, (id,))
    productos = cursor.fetchall()
    print(productos)
    return productos