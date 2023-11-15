from mysql import connector
conection = connector.connect(
            user="u119126_pollos",
            host="174.136.28.78",
            port="3306",
            password="$BulletKin0805",
            database="u119126_pollos"

        )
scrip2 = "SELECT MAX(id_Venta) FROM venta;"
cursor = conection.cursor()
cursor.execute(scrip2)
idelast = cursor.fetchone()
print(idelast)