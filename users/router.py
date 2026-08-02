from fastapi import APIRouter,HTTPException
from users.schemas import RegisterUser, LoginUser
import users.service
import exceptions
router_user = APIRouter()

@router_user.get("/")
def get_users():
    try:
        return users.service.load_all_users()
    except exceptions.DbDownloadError as e :
        return HTTPException(
            status_code=400,
            detail= str(e)
        )

@router_user.post("/add-user")
def sign_up(user:RegisterUser):
    try:
        users.service.register_user(user)
        return {"information": "Pomyslnie stworzono użytkownika"}, 200
    except exceptions.DbAddError as e :
        return HTTPException(
            status_code=400,
            detail= str(e)
        )

@router_user.post("/login")
def sign_in(user:LoginUser):
    try:
        return users.service.login_user(user)
    except exceptions.UserLoginError as e:
        return HTTPException(
            status_code=400,
            detail= str(e)
        )

@router_user.get("/me")
def get_user_inf(token: str):
    try:
        return users.service.user_info(token)
    except exceptions.DbDownloadError as e:
        return HTTPException(
            status_code=400,
            detail= str(e)
        )