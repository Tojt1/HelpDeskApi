from database import  pool
import exceptions


def create_user(user, hashed_password):
    conn = pool.getconn()

    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s)", (user.name, user.email, hashed_password))
            conn.commit()
            return True

    except Exception:
        conn.rollback()
        raise exceptions.DbAddError("Wystąpił błąd podczas dodawania użytkownika")

    finally:
        pool.putconn(conn)

def check_user_email(email):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT id FROM users WHERE email = %s", (email,))
            return cur.fetchone()

        except Exception:
            raise exceptions.DBCehckExistsError("Wystąpił błąd podczas sprawdzania email użytkownika")

        finally:
            pool.putconn(conn)

def check_user_password(email):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT password, id FROM users WHERE email = %s", (email,))
            return cur.fetchone()

        except Exception:
            raise exceptions.DBCehckExistsError("Wystąpił błąd podczas sprawdzania hasła użytkownika")
        finally:
            pool.putconn(conn)

def get_all_users():
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT id, name, role FROM users")
            return cur.fetchall()

        except Exception:
            raise exceptions.DbDownloadError("Wystąpił błąd podczas pobierania użytkowniowk")

        finally:
            pool.putconn(conn)

def get_id(email):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT id FROM users WHERE email = %s", (email, ))
            return cur.fetchone()

        except Exception:
            raise exceptions.GetUserIdError("Wystąpił błąd podczas pobierania ID użytkownika ")

        finally:
            pool.putconn(conn)

def download_user_info(id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT name, email, role, active, created FROM users WHERE id = %s", (id, ))
            return cur.fetchone()

        except Exception:
            raise exceptions.DbDownloadError("Wystąpił błąd podczas pobierania informacji użytkownika")

        finally:
            pool.putconn(conn)

def get_user_role(user_id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT role FROM users WHERE id = %s", (user_id, ))
            return cur.fetchone()

        except Exception:
            raise exceptions.DBCehckExistsError("Wystąpił błąd podczas pobierania roli użytkownika")

        finally:
            pool.putconn(conn)



