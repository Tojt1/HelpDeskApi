from database import  pool


def create_user(user, hashed_password):
    conn = pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s)", (user.name, user.email, hashed_password))
            conn.commit()
        return {"information": "Pomyślnie utworzono użytkownika"}
    except ValueError:
        return {"error": "Wystąpił porblem podczas tworzenia"}
    finally:
        pool.putconn(conn)

def check_user_email(email):
    conn = pool.getconn()
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users WHERE email = %s", (email,))
        return cur.fetchone()
    pool.putconn(conn)

def check_user_password(email):
    conn = pool.getconn()
    with conn.cursor() as cur:
        cur.execute("SELECT password, id FROM users WHERE email = %s", (email,))
        return cur.fetchone()
    pool.putconn(conn)

def get_all_users():
    conn = pool.getconn()
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, role FROM users")
        return cur.fetchall()
    pool.putconn()

def get_id(email):
    conn = pool.getconn()
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users WHERE email = %s", (email, ))
        return cur.fetchone()
    pool.putconn(conn)

def download_user_info(id):
    conn = pool.getconn()
    with conn.cursor() as cur:
        cur.execute("SELECT name, email, role, active, created FROM users WHERE id = %s", (id, ))
        return cur.fetchone()

    pool.putconn(conn)

def get_user_role(user_id):
    conn = pool.getconn()
    with conn.cursor() as cur:
        cur.execute("SELECT role FROM users WHERE id = %s", (user_id, ))
        return cur.fetchone()

    pool.putconn(conn)



