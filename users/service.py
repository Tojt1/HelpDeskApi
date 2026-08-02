import bcrypt
from users import repository
import jwt
import config
import exceptions

def register_user(user):
    try:
        valid_email(user.email)
        ensuer_email_not_exists(user.email)
        valid_password(user.password)
        hashed_password = hash_password(user.password)
        repository.create_user(user, hashed_password)
    except:
        raise ValueError("Wystąpił błąd podczas logowania")

def valid_password(password):
    special_chars = "!@#$%^&*()_+-=[]{}|;':\",.<>/?"
    found = False

    if len(password) < 8:
        raise ValueError("Hasło musi być dłższe niż 8 znaków")

    for char in password:
        if char in special_chars:
            found = True
            break

    if not found:
        raise ValueError("Hasło nie posiada znaku specjalnego")

    return None

def hash_password(password:str)->str:

    bpassword = password.encode("utf-8")
    hashed = bcrypt.hashpw(bpassword, bcrypt.gensalt())
    return hashed.decode("utf-8")


def check_password(password:str, hashed_password:str) ->bool:
    bpassword = password.encode("utf-8")
    return bcrypt.checkpw(bpassword, hashed_password.encode("utf-8"))

def valid_email(email:str):
    if "@" not in email:
        return {"error": "email jest nieprawidłowy"}

def ensuer_email_not_exists(email):
    result = repository.check_user_email(email)
    if result is not None:
        raise exceptions.UserAlreadyExistsError("Ten email jest już zajęty")

def ensuer_email_exists(email):
    result = repository.check_user_password(email)
    if result is None:
        raise exceptions.EmaildoesnotExistsError("Nie ma takiego e-maila")

    return result



def load_all_users():
    rows = repository.get_all_users()
    return [{
        "id":row[0],
        "name":row[1],
        "role":row[2]
    }
        for row in rows
    ]



def create_jwt_toc(id):
    token = jwt.encode(
        {"id": id[1]},
        config.SECRET_KEY,
        algorithm="HS256"
    )
    return token

def decode_token(token):
    result = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
    return result["id"]


def login_user(user):
    try:
        valid_email(user.email)
        result = ensuer_email_exists(user.email)
        if check_password(user.password, result[0]):
            return create_jwt_toc(result)
        else:
            raise exceptions.InvalidPasswordError("Podano niepoprawne hasło")
    except Exception:
        raise exceptions.UserLoginError("Wystąpił błą∂ podczas logowania użytkownika")

def user_info(token:str):
    user_id = decode_token(token)
    user = repository.download_user_info(user_id)
    return {
        "name":user[0],
        "email": user[1],
        "role": user[2],
        "active": user[3],
        "created": user[4]
    }

def check_user_admin(user_id)->bool:
    if repository.get_user_role(user_id)[0] == "ADMIN":
        return True
    return False