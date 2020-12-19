from typing import  Dict
from pydantic import BaseModel
from pydantic.networks import EmailStr

class UserInDB(BaseModel):
    username: str
    password: str
    email: str


database_users = Dict[str, UserInDB]


database_users = {
    "camilo24": UserInDB(**{"username":"camilo24", 
                            "password":"root", 
                            "email":"12000"}),

    "andres18": UserInDB(**{"username":"andres18", 
                            "password":"hola", 
                            "email":"34000"}),    
}


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else: 
        return None

def get_email(email: str):
    if email in database_users.keys():
        return database_users[email]
    else: 
        return None


def get_password(password: str):
    if password in database_users.keys():
        return database_users[password]
    else: 
        return None


    
def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db


def crear_user(user_in_db: UserInDB):
    if user_in_db.username in database_users.keys():
            if user_in_db.email in database_users.keys():
                return "Usuario existente"
    else:
        a = {user_in_db.username: user_in_db}
        database_users.update(a)
        return a


        

def crear_email(email_in_db: UserInDB):
    if email_in_db.email in database_users.keys():
        return "Usuario existente"
    else:
        b = {email_in_db.email: email_in_db}
        database_users.update(b)
        return b
