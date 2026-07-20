from fastapi import APIRouter
from schemas import User
import service
router = APIRouter()

@router.get("/")
def get_users():
    try:
        service.get_all_users()
    except ValueError:
        return {"error":"Nieprawidłowe dane"}, 400

@router.post("/add-user")

def create_user(user:User):
    try:
        service.register_user(user)
        return {"information": "Pomyslnie stworzono użytkownika"}, 200
    except ValueError:
        return {"error": "Podano niewłaściwe dane"}, 400