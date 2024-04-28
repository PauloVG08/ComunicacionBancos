from controller.Conexion import startConexion
from model.Banco import Banco


def daoObtenerBancoPorNombre(nombre):
    conexion, cursor = startConexion()
    try:
        consulta = f"SELECT * FROM banco WHERE nombre_banco = '{nombre}'"
        cursor.execute(consulta)
        result = cursor.fetchone()
        banco = dataToBanco(result)
        cursor.close()
        conexion.close()
        return banco
    except:
        cursor.close()
        conexion.close()
        return None

def daoGetBancos():
    conexion, cursor = startConexion()
    try:
        consulta = f"SELECT * FROM banco"
        cursor.execute(consulta)
        result = cursor.fetchall()

        bancos = []

        for banco in result:
            banco = dataToBanco(banco)
            bancos.append(banco)

        cursor.close()
        conexion.close()

        return bancos
    except:
        cursor.close()
        conexion.close()
        return None

def dataToBanco(data):
    return Banco(
        id=data[0],
        nombre_banco= data[1],
        enlace_banco=data[2]
    )