from controller.BancoController import controllerGetBancos
from api.TransaccionAPI import app

@app.get("/obtenerBancos")
def obtenerBancos():
    bancos = controllerGetBancos()
    return {"result": bancos}