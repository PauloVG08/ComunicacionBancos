CREATE TABLE cajero(
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cantidad FLOAT NOT NULL
);

-- Versiones de los cajeros
CREATE TABLE cajero_v1 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cantidad_dinero FLOAT NOT NULL
);

CREATE TABLE cajero_v2 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    monto_disponible FLOAT NOT NULL
);

CREATE TABLE cajero_v3 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    saldo_actual FLOAT NOT NULL
);
