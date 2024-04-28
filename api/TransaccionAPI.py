from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from model.Cuenta import Cuenta
from controller.RetiroController import controllerRetirarDinero, controllerRetiroExterno

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5501"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/retirar/{no_cuenta}/{nip}/{monto}/{is_externo}")
def retirarDinero(no_cuenta, nip, monto, is_externo):
    cuenta = controllerRetirarDinero(no_cuenta, nip, monto, is_externo)
    return {"result": cuenta}

@app.post("/retirarExterno/{no_cuenta}/{nip}/{monto}/{banco}")
def retirarDineroExterno(no_cuenta, nip, monto, banco):
    cuenta = controllerRetiroExterno(no_cuenta, nip, monto, banco)
    return {"result": cuenta}

