#Задание 1.4 и 1.5
from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int

class UserAge(BaseModel):
    name: str
    age: int