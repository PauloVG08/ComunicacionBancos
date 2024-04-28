from cqrs.RetiroCQRS import cqrsRetirarDinero, cqrsRetirarDineroExterno
from dao.BancoDAO import daoObtenerBancoPorNombre
from dao.CajeroDAO import daoObtenerMontoCajero
import requests


def serviceRetirar(tarjeta, nip, monto, is_externo):
    result = cqrsRetirarDinero(tarjeta, nip, monto, is_externo)
    return result

def serviceRetirarExterno(tarjeta, nip, monto, banco):
    resultado, banco = retirarExterno(tarjeta, nip, monto, banco)
    result = cqrsRetirarDineroExterno(tarjeta, float(monto), banco, resultado)
    return result

def retirarExterno(tarjeta, nip, monto, banco):
    banco = daoObtenerBancoPorNombre(banco)
    montoCajero = daoObtenerMontoCajero()
    montoCajero = montoCajero[0]

    if banco is None:
        return {"Error": "Banco No Existe"}
    elif float(monto) > montoCajero:
        return {"Error": "Fondos del cajero insuficientes"}

    url = f"{banco.enlace_banco}{tarjeta}/{nip}/{monto}/1"

    headers = {}

    # Ya que no necesitas enviar un payload, puedes omitir esa parte
    resultado = requests.post(url, headers=headers)
    resultado = resultado.json()
    return (resultado, banco)

