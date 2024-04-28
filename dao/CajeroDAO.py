from controller.Conexion import startConexion


def daoObtenerMontoCajero():
    conexion, cursor = startConexion()
    try:
        consulta = f"SELECT dinero_disponible FROM cajero WHERE id = 1"
        cursor.execute(consulta)
        result = cursor.fetchone()

        cursor.close()
        conexion.close()
        return result
    except:
        cursor.close()
        conexion.close()
        return None