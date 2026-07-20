import bcrypt

def hash_password(password):
    errors = []
    special_chars = "!@#$%^&*()_+-=[]{}|;':\",.<>/?"
    found = False

    if len(password) < 8:
        errors.append("Hasło musi zawierać conajmniej 8 znaków")

    for char in password:
        if char in special_chars:
            found = True
            break

    if not found:
        errors.append("Hasło nie posiada znaku specjalnego")

    bpassword = password.encode("utf-8")
    hashed = bcrypt.hashpw(bpassword, bcrypt.gensalt())
    return hashed.decode("utf-8")


def check_password(password, hashed_password):
    bpassword = password.encode("utf-8")
    return bcrypt.checkpw(bpassword, hashed_password.encode("utf-8"))
