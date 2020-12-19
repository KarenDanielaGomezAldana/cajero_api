from datetime import date
from typing import  Dict, TYPE_CHECKING
from pydantic import BaseModel
from pydantic.types import StrictStr


class UserInR(BaseModel):
    id_reserva: int = 0
    Nombre: str
    Destino: str
    Hotel: str
    Habitaciones: int
    Valor: int
    Fecha_entrada: date
    Fecha_salida: date


database_usersR = Dict[str, UserInR]
generator = {"id":0}

database_usersR = {
    "Serengueti": UserInR(**{"Nombre":"Serengueti", 
                            "Destino":"xxx", 
                            "Hotel":"xxx", 
                            "Habitaciones": 23,
                            "Valor": 45, 
                            "Fecha_entrada":23/10/2005,
                            "Fecha_salida":12/12/2005}),

    "Panaca": UserInR(**{"Nombre":"Panaca", 
                        "Destino":"xxx", 
                        "Hotel":"xxx", 
                        "Habitaciones":23,
                        "Valor": 43, 
                        "Fecha_entrada":15/9/2011,
                        "Fecha_salida":22/10/2012}),    
}

def save_reserva(reserva_in_db: UserInR):
    generator["id"] = generator["id"] + 1
    reserva_in_db.id_reserva = generator["id"]
    database_usersR.append(reserva_in_db)
    return reserva_in_db
    

def get_Reserva(Name: str):
    if Name in database_usersR.keys():
        return database_usersR[Name]
    else: 
        return None

def update_Reserva(user_in_db: UserInR):
    database_usersR[user_in_db.Nombre] = user_in_db
    return user_in_db

def crear_Reserva(user_in_db: UserInR):
    if user_in_db.Nombre in database_usersR.keys():
        return "Usuario existente"
    else:
        b = {user_in_db.Nombre: user_in_db}
        database_usersR.update(b)
        return b