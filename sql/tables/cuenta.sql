CREATE TABLE cuenta (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    no_cuenta INT(20) NOT NULL,
    cantidad_disponible FLOAT(20) NOT NULL,
    nip_tarjeta INT(4) NOT NULL,
    id_usuario INT(2) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

--Versiones de cuenta

CREATE TABLE cuenta_v1 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    numero_cuenta INT(20) NOT NULL,
    disponible FLOAT(20) NOT NULL,
    pin_tarjeta INT(4) NOT NULL,
    identificador_usuario INT(2) NOT NULL,
    FOREIGN KEY (identificador_usuario) REFERENCES usuario(id)
);

CREATE TABLE cuenta_v2 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    num_cuenta INT(20) NOT NULL,
    cantidad FLOAT(20) NOT NULL,
    pin_tarjeta INT(4) NOT NULL,
    usuario_id INT(2) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE cuenta_v3 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cuenta_numero INT(20) NOT NULL,
    disponible_cantidad FLOAT(20) NOT NULL,
    tarjeta_nip INT(4) NOT NULL,
    user_id INT(2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuario(id)
);
