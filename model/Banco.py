from pydantic import BaseModel

class Banco(BaseModel):
    id: int
    nombre_banco: str
    enlace_banco: str