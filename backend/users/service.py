import bcrypt
from backend.users import repository
import jwt
import config
import exceptions

def register_user(user):
    try:
        ensuer_email_not_exists(user.email)
        valid_password(user.password)
        hashed_password = hash_password(user.password)
        repository.create_user(user, hashed_password)

    except exceptions.UserAlreadyExistsError:
        raise

    except exceptions.InvalidPasswordError:
        raise

    except Exception as e:
        print("Błą∂", e)
        raise exceptions.UserRegisterError("Wystąpił błąd podczas tworzenia konta")

def valid_password(password):
    special_chars = "!@#$%^&*()_+-=[]{}|;':\",.<>/?"
    found = False

    if len(password) < 8:
        raise exceptions.InvalidPasswordError("Hasło musi być dłższe niż 8 znaków")

    for char in password:
        if char in special_chars:
            found = True
            break

    if not found:
        raise exceptions.InvalidPasswordError("Hasło nie posiada znaku specjalnego")

    return None

def hash_password(password:str)->str:

    bpassword = password.encode("utf-8")
    hashed = bcrypt.hashpw(bpassword, bcrypt.gensalt())
    return hashed.decode("utf-8")


def check_password(password:str, hashed_password:str) ->bool:
    bpassword = password.encode("utf-8")
    return bcrypt.checkpw(bpassword, hashed_password.encode("utf-8"))


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



def create_jwt_toc(user, email):
    token = jwt.encode(
        {"id": user[1],
         "name": user[2],
         "email": email},
        config.SECRET_KEY,
        algorithm="HS256"
    )
    return token

def decode_token(token):
    result = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
    return result


def login_user(user):
    try:
        result = ensuer_email_exists(user.email)
        if check_password(user.password, result[0]):
            return {"token":create_jwt_toc(result, user.email)}
        else:
            raise exceptions.InvalidPasswordError("Podano niepoprawne hasło")

    except Exception as e:
        print("Błą∂", e)
        raise exceptions.UserLoginError("Wystąpił błą∂ podczas logowania użytkownika")

def user_info(token):
    user_id = decode_token(token)
    user = repository.download_user_info(user_id["id"])
    return {
        "id": user_id["id"],
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

def change_email(data, token):
    try:
        user = decode_token(token)
        user_email = user["email"]
        ensuer_email_not_exists(data.new_email)
        if user_email != data.old_email:
            raise exceptions.DiffrentEmailError("Podałeś ten sam email")
        if user_email == data.new_email:
            raise exceptions.EmailisCurrentlyUseError("Nie można użyć tego e-maila")

        repository.changeEmail(user["id"], data.new_email)

    except Exception as e:
        print("Error", e)
        raise exceptions.ChangeEmailError("Wystąpił błąd podczas zmiany emailu")


def change_password(data, token):
    user = decode_token(token)
    valid_password(data.new_password)

    if data.new_password == data.old_password:
        raise exceptions.ThisSamePasswordError("To hasło było już przez ciebie użyte")

    user_inf = repository.check_user_password(user["email"])

    if not check_password(data.old_password, user_inf[0]):
        raise exceptions.NotTheSamePasswordError("Podano nieprawidłowe hasło")
    if check_password(data.new_password, user_inf[0]):
        raise exceptions.ThisSamePasswordError("To hasło było już przez ciebie użyte")

    hashed_password = hash_password(data.new_password)

    repository.changePassword(hashed_password, user_inf[1])

