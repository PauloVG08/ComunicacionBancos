from dao.BancoDAO import daoObtenerBancoPorNombre
from dao.CajeroDAO import daoObtenerMontoCajero
from dao.CuentaDAO import daoObtenerCuenta
from dao.UsuarioDAO import daoObtenerUsuarioId
from dao.transaccionDAO import daoRetirarDinero
from model.Cuenta import Cuenta
from model.Usuario import Usuario
import requests

def cqrsRetirarDinero(tarjeta, nip, monto, is_externo):
    cuenta = daoObtenerCuenta(tarjeta)

    if cuenta == None:
        return {"Error": "Cuenta No Localizada Verifiquela"}

    montoCajero = daoObtenerMontoCajero()
    montoCajero = montoCajero[0]

    if cuenta.nip_seg != int(nip):
        return {"Error": "Nip Incorrecto"}
    if cuenta.dinero_disponible_c < float(monto):
        return {"Error": "Fondos insuficientes"}
    elif int(is_externo) == 0:
        if float(monto) > montoCajero:
            return {"Error": "Fondos del cajero insuficientes"}

    # usuario = daoObtenerUsuarioId(cuenta.id_usuario)

    #Se comprueba que no haya valores nulos
    result = daoRetirarDinero(cuenta.numero_cuenta, monto, 0, int(is_externo))  # Aqui se llama al dao
    return result

def cqrsRetirarDineroExterno(tarjeta, monto, banco, resultado):
    if resultado["result"] == True:
        resultado = daoRetirarDinero(tarjeta, monto, banco.id, 0)  # Aqui se llama al dao
        return resultado
    elif resultado["result"] == False:
        return {"ERROR": "No se realizo la transaccion"}
    else:
        return resultado["result"]
