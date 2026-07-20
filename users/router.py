from fastapi import APIRouter
from users.schemas import User
import users.service

router_user = APIRouter()

@router_user.get("/")
def get_users():
    try:
        return users.service.get_all_users()
    except ValueError:
        return {"error":"Nieprawidłowe dane"}, 400

@router_user.post("/add-user")

def create_user(user:User):
    try:
        users.service.register_user(user)
        return {"information": "Pomyslnie stworzono użytkownika"}, 200
    except ValueError:
        return {"error": "Podano niewłaściwe dane"}, 400