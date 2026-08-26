from fastapi import APIRouter,HTTPException, Depends
from backend.users.schemas import RegisterUser, LoginUser, ChangeEmail
import backend.users.service
import exceptions
from authorisation import oauth2
router_user = APIRouter()

@router_user.get("/")
def get_users():
    try:
        return backend.users.service.load_all_users()
    except exceptions.DbDownloadError as e :
        return HTTPException(
            status_code=400,
            detail= str(e)
        )

@router_user.post("/register")
def sign_up(user:RegisterUser):
    try:
        print("1")
        backend.users.service.register_user(user)
        return {"information": "Pomyslnie stworzono użytkownika"}, 200
    except exceptions.UserAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail="Ten email jest już zajęty"
        )
    except exceptions.DbAddError:
        raise HTTPException(
            status_code=400,
            detail="Wystąpił błąd podczas tworzenia użytkownika"
        )
    except exceptions.InvalidPasswordError:
        raise HTTPException(
            status_code=400,
            detail="Podano nieprawidłowe hasło"
        )

@router_user.post("/login")
def  sign_in(user:LoginUser):
    try:
        return backend.users.service.login_user(user)
    except exceptions.InvalidPasswordError:
        raise HTTPException(
            status_code=401,
            detail= "Podano nieprawidłowe hasło"
        )
    except exceptions.EmaildoesnotExistsError:
        raise HTTPException(
            status_code=404,
            detail="NIe znaleziono takiego użytkownika"
        )
    except exceptions.UserLoginError:
        raise HTTPException(
            status_code=400,
            detail="Podano nieprawidłowy email lub hasło"
        )

@router_user.get("/me")
def get_user_inf(token = Depends(oauth2)):
    try:
        return backend.users.service.user_info(token)
    except exceptions.DbDownloadError as e:
        return HTTPException(
            status_code=400,
            detail= str(e)
        )

@router_user.patch("/me/email")
def change_email(new_email: ChangeEmail , token = Depends(oauth2)):
    try:
        backend.users.service.change_email(new_email, token)
        return {"information": "Pomyślnie zmieniono email"}, 200
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Nie udalo sie zmienic e-meila"
        )