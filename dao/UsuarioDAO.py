from ast import List
from controller.Conexion import startConexion
from model.Cuenta import Cuenta
from model.Usuario import Usuario

def daoObtenerUsuarioId(id_usuario):
    conexion, cursor = startConexion()
    try:
        consulta = f"SELECT * FROM usuario WHERE id={id_usuario}"
        cursor.execute(consulta)
        result = cursor.fetchone()
        #Cierra el cursor
        cursor.close()
        #Cierra la conexion
        conexion.close()
        return dataToUsuario(result)
    except:
        cursor.close()
        conexion.close()
        return None

def dataToUsuario(data: List):
    return Usuario(
        id=data[0],
        nombre_u= data[1],
        p_apellido=data[2],
        s_apellido=data[3],
        estado_civil=data[4]
    )
