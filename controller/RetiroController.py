from appService.BancoAPPService import serviceGetAllBancos
from model.Cuenta import Cuenta
from appService.TransaccionAPPService import serviceRetirar, serviceRetirarExterno


def controllerRetirarDinero(no_cuenta, nip, monto, is_externo):
    try:
        result = serviceRetirar(no_cuenta, nip, monto, is_externo)
        return result
    except:
        return {}


def controllerRetiroExterno(no_cuenta, nip, monto, banco):
    try:
        result = serviceRetirarExterno(no_cuenta, nip, monto, banco)
        return result
    except:
        return {""}
