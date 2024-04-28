from pydantic import BaseModel
from model.Usuario import Usuario

class Cuenta(BaseModel):
    id: int
    numero_cuenta: int
    dinero_disponible_c: float
    nip_seg: int
    id_usuario: int
