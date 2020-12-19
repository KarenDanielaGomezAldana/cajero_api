from datetime import date
from pydantic import BaseModel
class ReservaIn(BaseModel):
    Nombre: str
    Destino: str
    Hotel: str
class ReservaOut(BaseModel):
    id_reserva: int
    Nombre: str
    Destino: str
    Hotel: str
    Habitaciones: int
    Valor: int
    Fecha_entrada: date
    Fecha_salida: date