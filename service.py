import bcrypt
from database import create_connection
import repository

def register_user(user):
    valid_email(user.email)
    ensuer_email_not_exists(user.email)
    valid_password(user.password)
    hash_password(user.password)
    repository.create_user()

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

def hash_password(password):

    bpassword = password.encode("utf-8")
    hashed = bcrypt.hashpw(bpassword, bcrypt.gensalt())
    return hashed.decode("utf-8")


def check_password(password, hashed_password):
    bpassword = password.encode("utf-8")
    return bcrypt.checkpw(bpassword, hashed_password.encode("utf-8"))

def valid_email(email):
    if "@" not in email:
        return {"error": "email jest nieprawidłowy"}

def ensuer_email_not_exists(email):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users WHERE email = %s", (email,))
        result = cur.fetchone()
        if result is not None:
            raise ValueError("Ten email jest już zajęty")


def get_all_users():
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, role FROM users")
        rows = cur.fetchall()
        return [{
            "id":row[0],
            "name":row[1],
            "role":row[2]
        }
            for row in rows
        ]
