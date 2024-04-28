CREATE TABLE usuario (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_u VARCHAR(75) NOT NULL,
    p_apellido VARCHAR(75) NOT NULL,
    s_apellido VARCHAR(75) NOT NULL,
    edad VARCHAR(3) NOT NULL,
    estado_civil VARCHAR(75) NOT NULL
);

-- Versiones de usuario

CREATE TABLE usuario_v1 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(75) NOT NULL,
    primer_apellido VARCHAR(75) NOT NULL,
    segundo_apellido VARCHAR(75) NOT NULL,
    edad_persona VARCHAR(3) NOT NULL,
    estado_civil_actual VARCHAR(75) NOT NULL
);

CREATE TABLE usuario_v2 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_cliente VARCHAR(75) NOT NULL,
    apellido_paterno VARCHAR(75) NOT NULL,
    apellido_materno VARCHAR(75) NOT NULL,
    edad_cliente VARCHAR(3) NOT NULL,
    estado_civil_actual VARCHAR(75) NOT NULL
);

CREATE TABLE usuario_v3 (
	id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_persona VARCHAR(75) NOT NULL,
    primer_apell VARCHAR(75) NOT NULL,
    segundo_apell VARCHAR(75) NOT NULL,
    edad_persona VARCHAR(3) NOT NULL,
    situacion_sentimental VARCHAR(75) NOT NULL
);
