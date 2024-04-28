from ast import List
from controller.Conexion import startConexion
from model.Cuenta import Cuenta
from model.Usuario import Usuario

def daoObtenerMontoCajero():
    conexion, cursor = startConexion()
    try:
        consulta = f"SELECT dinero_disponible_c FROM cajero WHERE id = 1"
        cursor.execute(consulta)
        result = cursor.fetchone()

        cursor.close()
        conexion.close()
        return result
    except:
        cursor.close()
        conexion.close()
        return None

def daoObtenerCuenta(no_cuenta):
    conexion, cursor = startConexion()
    try:
        consulta = f"SELECT * FROM cuenta WHERE numero_cuenta = {no_cuenta}"
        cursor.execute(consulta)
        result = cursor.fetchone()

        cuenta = dataToCuenta(result)
        cursor.close()
        conexion.close()
        return cuenta
    except:
        cursor.close()
        conexion.close()
        print("Hubo un error")
        return None

def daoRetirarDinero(cuenta, monto, banco):
    conexion, cursor = startConexion()

    try:
        inserccion = (f"INSERT INTO transaccion (no_cuenta,dinero_cantidad, banco_procedencia ) VALUES"
                  f" ({int(cuenta)}, {float(monto)}, {int(banco)})")
        cursor.execute(inserccion)
        conexion.commit()
        cursor.close()
        conexion.close()

        return True
    except:
        return False

def dataToCuenta(data):
    return Cuenta(
        id=data[0],
        numero_cuenta= data[1],
        dinero_disponible_c=data[2],
        nip_seg=data[3],
        id_usuario=data[4]
    )
