CREATE DATABASE pollosexpress;
USE pollosexpress;

SHOW TABLES;

CREATE TABLE pago (
    id_pago INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre NVARCHAR(50)
);

CREATE TABLE rol (
    id_rol INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL,
    CONSTRAINT UNIQUE(nombre)
);


CREATE TABLE empleado (
    id_empleado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
	apellido_paterno NVARCHAR(50) NOT NULL,
    apellido_materno NVARCHAR(50) NOT NULL,
    celular VARCHAR(11) NOT NULL,
    sueldo DOUBLE NOT NULL,
    id_rol INT,
    pass NVARCHAR(30),
    FOREIGN KEY (id_rol) REFERENCES rol(id_Rol),
    CONSTRAINT UQcelular UNIQUE(celular)
);

ALTER TABLE empleado
ADD COLUMN administrator bool NOT NULL;

CREATE TABLE cliente (
    id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    celular VARCHAR(11) NOT NULL,
    direccion VARCHAR(150) NOT NULL
);

CREATE TABLE venta (
    id_Venta INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha_De_Venta DATE NOT NULL,
    total_De_Compra DOUBLE NOT NULL,
    id_pago INT,
    id_empleado INT,
    FOREIGN KEY (id_pago) REFERENCES pago(id_Pago),
    FOREIGN KEY (id_empleado) REFERENCES empleado(id_Empleado),
    id_cliente INT,
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)
);


CREATE TABLE producto (
    id_producto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    descripcion NVARCHAR(200) NOT NULL,
    precio DOUBLE NOT NULL,
    imagen text NOT NULL
);

CREATE TABLE gasto (
    id_gasto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(150) NOT NULL,
    monto DOUBLE NOT NULL,
    fecha DATE NOT NULL,
    id_empleado INT,
    FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
);


CREATE TABLE tipo_de_promocion (
    id_tipo_promocion INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    codigo VARCHAR(50) NOT NULL
);

CREATE TABLE venta_producto (
    id_venta_producto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_venta INT,
    id_producto INT,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES venta(id_venta),
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

CREATE TABLE promocion (
    id_promocion INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_producto INT,
    descripcion VARCHAR(200) NOT NULL,
    fecha_de_inicio DATE NOT NULL,
    fecha_de_finalizacion DATE,
    id_tipo_promocion INT,
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto),
    FOREIGN KEY (id_tipo_promocion) REFERENCES tipo_de_promocion(id_tipo_promocion),
    CONSTRAINT fecha_valida CHECK (fecha_de_inicio <= fecha_de_finalizacion)
);