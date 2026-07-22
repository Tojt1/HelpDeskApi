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

def check_user_password(email):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT password, id FROM users WHERE email = %s", (email,))
        return cur.fetchone()

def get_all_users():
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, role FROM users")
        return cur.fetchall()

def get_id(email):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users WHERE email = %s", (email, ))
        return cur.fetchone()

def download_user_info(id):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT name, email, role, active, created FROM users WHERE id = %s", (id, ))
        return cur.fetchone()



