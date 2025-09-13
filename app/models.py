from pydantic import BaseModel

class ServicioFunerario(BaseModel):
    id: int
    nombre: str
    precio: float
