from pydantic import BaseModel

class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
    active: bool

class LoginUser(BaseModel):
    email:str
    password:str