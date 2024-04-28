from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre_u: str
    p_apellido: str
    s_apellido: str
    edad: str
    estado_civil: str

