from database import  create_connection


def create_user(user, hashed_password):
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s)", (user.name, user.email, hashed_password))
            conn.commit()
            print('j')
        return {"information": "Pomyślnie utworzono użytkownika"}
    except ValueError:
        return {"error": "Wystąpił porblem podczas tworzenia"}

def check_user_email(email):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users WHERE email = %s", (email,))
        return cur.fetchone()

