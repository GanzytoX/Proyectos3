# Bibliotecas
from tkinter import *
import mysql.connector
from Crud.CRUD_Inventario import *


class InventarioInterface():
    def __init__(self):
        super().__init__(window_name="Inventario", size="1200x700", resizable=False,
                         background_image="../img/fondo_inventario.png")
        self.connection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
