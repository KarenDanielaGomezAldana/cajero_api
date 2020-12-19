from pydantic import BaseModel
from pydantic.networks import EmailStr
class UserIn(BaseModel):
    username: str
    password: str
class UserOut(BaseModel):
    username: str
    email: str
