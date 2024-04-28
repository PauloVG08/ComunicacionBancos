from pydantic import BaseModel

class Cuenta(BaseModel):
    id: int
    cantidad_dinero: float
    banco_origen: str
    numero_cuenta_destino: int

