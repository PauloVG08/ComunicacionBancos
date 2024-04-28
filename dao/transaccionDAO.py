from controller.Conexion import startConexion


def daoRetirarDinero(cuenta, monto, banco, is_externo):
    conexion, cursor = startConexion()

    try:
        inserccion = (f"INSERT INTO transaccion (numero_cuenta_destino, cantidad_dinero, banco_origen, is_externo) VALUES"f" ({int(cuenta)}, {float(monto)}, {int(banco)}, {int(is_externo)})")
        cursor.execute(inserccion)
        conexion.commit()
        cursor.close()
        conexion.close()

        return True
    except:

        return False