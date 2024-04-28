from appService.BancoAPPService import serviceGetAllBancos


def controllerGetBancos():
    try:
        result = serviceGetAllBancos()
        return result
    except:
        return {""}