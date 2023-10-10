-- CREATE DATABASE BaseDeDatos_Polleria;
-- USE BaseDeDatos_Polleria;

-- SHOW TABLES;

CREATE TABLE Pago (
    id_Pago INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    metodo VARCHAR(50)
);

CREATE TABLE Rol (
    id_Rol INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Empleado (
    id_Empleado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    celular VARCHAR(11) NOT NULL,
    sueldo DOUBLE NOT NULL,
    id_RolFK INT,
    contraseña VARCHAR(20),
    FOREIGN KEY (id_RolFK) REFERENCES Rol(id_Rol)
);

/*
CREATE TABLE usuario(
	id_usuario int AUTO_INCREMENT PRIMARY KEY,
    id_empleado int,
    
);
*/

CREATE TABLE Venta (
    id_Venta INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha_De_Venta DATE NOT NULL,
    total_De_Compra DOUBLE NOT NULL,
    id_PagoFK INT,
    id_EmpleadoFK INT,
    FOREIGN KEY (id_PagoFK) REFERENCES Pago(id_Pago),
    FOREIGN KEY (id_EmpleadoFK) REFERENCES Empleado(id_Empleado)
);


/*SELECT * FROM Pago;*/

CREATE TABLE Producto (
    id_Producto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    precio DOUBLE NOT NULL,
    imagen VARCHAR(200) NOT NULL
);

CREATE TABLE Gasto (
    id_Gasto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(150) NOT NULL,
    monto DOUBLE NOT NULL,
    fecha DATE NOT NULL,
    id_EmpleadoFK INT,
    FOREIGN KEY (id_EmpleadoFK) REFERENCES Empleado(id_Empleado)
);

CREATE TABLE Cliente (
    id_Cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    celular VARCHAR(11) NOT NULL,
    direccion VARCHAR(150) NOT NULL
);

CREATE TABLE Tipo_de_promocion (
    id_Tipo_Promocion INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    codigo VARCHAR(50) NOT NULL
);

CREATE TABLE Venta_Producto (
    id_Venta_Producto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_VentaFK INT,
    id_ProductoFK INT,
    FOREIGN KEY (id_VentaFK) REFERENCES Venta(id_Venta),
    FOREIGN KEY (id_ProductoFK) REFERENCES Producto(id_Producto)
);

CREATE TABLE Promocion (
    id_Promocion INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_ProductoFK INT,
    descripcion VARCHAR(200) NOT NULL,
    fecha_de_inicio DATE NOT NULL,
    fecha_de_finalizacion DATE,
    id_Tipo_PromocionFK INT,
    FOREIGN KEY (id_ProductoFK) REFERENCES Producto(id_Producto),
    FOREIGN KEY (id_Tipo_PromocionFK) REFERENCES Tipo_de_promocion(id_Tipo_Promocion),
    CONSTRAINT fecha_valida CHECK (fecha_de_inicio <= fecha_de_finalizacion) --VERIFICA QUE LA FECHA DE INICIO SEA MENOR A LA FECHA FINAL
);