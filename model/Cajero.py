from pydantic import BaseModel

class Cajero(BaseModel):
    id: int
    dinero_disponilbe: float
