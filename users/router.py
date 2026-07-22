from fastapi import APIRouter
from users.schemas import RegisterUser, LoginUser
import users.service

router_user = APIRouter()

@router_user.get("/")
def get_users():
    try:
        return users.service.load_all_users()
    except ValueError:
        return {"error":"Nieprawidłowe dane"}, 400

@router_user.post("/add-user")
def sign_up(user:RegisterUser):
    try:
        users.service.register_user(user)
        return {"information": "Pomyslnie stworzono użytkownika"}, 200
    except ValueError:
        return {"error": "Podano niewłaściwe dane"}, 400

@router_user.post("/login")
def sign_in(user:LoginUser):
    return users.service.login_user(user)

@router_user.get("/get_post")
def get_user_post(token: str):
    return users.service.decode_token(token)