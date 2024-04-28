CREATE TABLE banco (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    compania_banco VARCHAR(50) NOT NULL,
    url_banco VARCHAR(100) NOT NULL
);

-- Versiones de las tablas
CREATE TABLE banco (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_banco VARCHAR(50) NOT NULL,
    enlace_banco VARCHAR(100) NOT NULL
);

CREATE TABLE banco (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_institucion VARCHAR(50) NOT NULL,
    sitio_web VARCHAR(100) NOT NULL
);

CREATE TABLE banco (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_compania VARCHAR(50) NOT NULL,
    direccion_web VARCHAR(100) NOT NULL
);