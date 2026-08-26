from pydantic import BaseModel

class RegisterUser(BaseModel):
    name: str
    email: str
    password: str

class LoginUser(BaseModel):
    email:str
    password:str

class ChangeEmail(BaseModel):
    new_email: str
    old_email: str