from database import pool
import exceptions

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