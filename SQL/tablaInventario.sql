USE u119126_pollos2LaVengazaDelPollo;

# SHOW TABLES;
DROP TABLE IF EXISTS inventario;

SELECT * FROM producto;

CREATE TABLE inventario (
    id_producto INT NOT NULL,
    nombre_producto VARCHAR(100) NOT NULL,
    unidad VARCHAR(10) NOT NULL,
    cantidad INT NOT NULL,
    PRIMARY KEY(id_producto),
    FOREIGN KEY(id_producto) REFERENCES producto(id_producto)
);

INSERT INTO inventario(id_producto, nombre_producto, unidad, cantidad) VALUES 
(1, "Pollo asado", "kg", 5),
(2, "Spaguetti", "kg", 10);
#(3, "deez nuts", "Kg", 69);

SELECT * FROM inventario;