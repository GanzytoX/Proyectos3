USE u119126_pollos2LaVengazaDelPollo;

# SHOW TABLES;
DROP TABLE IF EXISTS inventario;

SELECT * FROM producto;

CREATE TABLE inventario (
	codigo VARCHAR(10) NOT NULL,
    id_producto INT,
    nombre_producto VARCHAR(100) NOT NULL,
    unidad VARCHAR(10) NOT NULL,
    cantidad INT NOT NULL,
    PRIMARY KEY(codigo),
    FOREIGN KEY(id_producto) REFERENCES producto(id_producto)
);

INSERT INTO inventario(codigo, id_producto, nombre_producto, unidad, cantidad) VALUES 
("123ABC", 1, "Pollo asado", "Kg", 5),
("456DEF", 3, "Queso con pelos", "Kg", 99),
("789GHI", 4, "deez nuts", "Kg", 69);

SELECT * FROM inventario;