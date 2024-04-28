DELIMITER //
CREATE TRIGGER after_insert_transaccion
AFTER INSERT ON transaccion
FOR EACH ROW
BEGIN
    -- Intentar restar el monto de la transacción de la cuenta correspondiente
    DECLARE cuenta_existente INT;
    SET cuenta_existente = (SELECT COUNT(*) FROM cuenta WHERE no_cuenta = NEW.no_cuenta);

    IF cuenta_existente > 0 THEN
        UPDATE cuenta
        SET cantidad_disponible = cantidad_disponible - NEW.dinero_cantidad
        WHERE no_cuenta = NEW.no_cuenta;
    END IF;

    -- Restar el monto de la transacción del cajero (siempre es el cajero 1)
    UPDATE cajero
    SET cantidad = cantidad - NEW.dinero_cantidad
    WHERE id = 1;
END;
//
DELIMITER ;

-- cuenta_v1
DELIMITER //
CREATE TRIGGER after_insert_transaccion_v1
AFTER INSERT ON transaccion
FOR EACH ROW
BEGIN
    DECLARE cuenta_existente INT;
    SET cuenta_existente = (SELECT COUNT(*) FROM cuenta_v1 WHERE numero_cuenta = NEW.no_cuenta);

    IF cuenta_existente > 0 THEN
        UPDATE cuenta_v1
        SET disponible = disponible - NEW.dinero_cantidad
        WHERE numero_cuenta = NEW.no_cuenta;
    END IF;

    UPDATE cajero
    SET cantidad_dinero = cantidad_dinero - NEW.dinero_cantidad
    WHERE id = 1;
END;
//
DELIMITER ;

--cuenta_v2
DELIMITER //
CREATE TRIGGER after_insert_transaccion_v2
AFTER INSERT ON transaccion
FOR EACH ROW
BEGIN
    DECLARE cuenta_existente INT;
    SET cuenta_existente = (SELECT COUNT(*) FROM cuenta_v2 WHERE num_cuenta = NEW.no_cuenta);

    IF cuenta_existente > 0 THEN
        UPDATE cuenta_v2
        SET cantidad = cantidad - NEW.dinero_cantidad
        WHERE num_cuenta = NEW.no_cuenta;
    END IF;

    UPDATE cajero
    SET monto_disponible = monto_disponible - NEW.dinero_cantidad
    WHERE id = 1;
END;
//
DELIMITER ;

--cuenta_v3
DELIMITER //
CREATE TRIGGER after_insert_transaccion_v3
AFTER INSERT ON transaccion
FOR EACH ROW
BEGIN
    DECLARE cuenta_existente INT;
    SET cuenta_existente = (SELECT COUNT(*) FROM cuenta_v3 WHERE cuenta_numero = NEW.no_cuenta);

    IF cuenta_existente > 0 THEN
        UPDATE cuenta_v3
        SET disponible_cantidad = disponible_cantidad - NEW.dinero_cantidad
        WHERE cuenta_numero = NEW.no_cuenta;
    END IF;

    UPDATE cajero
    SET saldo_actual = saldo_actual - NEW.dinero_cantidad
    WHERE id = 1;
END;
//
DELIMITER ;

