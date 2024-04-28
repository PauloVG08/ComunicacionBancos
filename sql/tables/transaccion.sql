CREATE TABLE transaccion (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    dinero_cantidad FLOAT(20) NOT NULL,
    banco_procedencia VARCHAR(75) NOT NULL,
    no_cuenta INT(20) NOT NULL
);

-- Versiones de transaccion

CREATE TABLE transaccion_v1 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cantidad_dinero FLOAT(20) NOT NULL,
    banco_origen VARCHAR(75) NOT NULL,
    numero_cuenta_destino INT(20) NOT NULL
);

CREATE TABLE transaccion_v2 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    monto FLOAT(20) NOT NULL,
    banco_origen VARCHAR(75) NOT NULL,
    cuenta_destino INT(20) NOT NULL
);

CREATE TABLE transaccion_v3 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cantidad_transferida FLOAT(20) NOT NULL,
    banco_origen_nombre VARCHAR(75) NOT NULL,
    cuenta_destino_numero INT(20) NOT NULL
);
