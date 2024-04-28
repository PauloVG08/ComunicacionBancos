from ViewModel.BancoPublicViewModel import BancoPublic
from dao.BancoDAO import daoGetBancos

def serviceGetAllBancos():
    bancos = daoGetBancos()
    publicBancos = []

    for banco in bancos:
        publicBanco = BancoPublic(banco.id, banco.nombre_banco)
        publicBancos.append(publicBanco)

    return publicBancos