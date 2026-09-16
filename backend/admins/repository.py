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

def assign_agent(agent_id, date_now, ticket_id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE tickets SET status='IN_PROGRESS', agent_id=%s,updated=%s WHERE id=%s", (agent_id, date_now, ticket_id))
            conn.commit()
        except Exception as e:
            print("Błąd", e)
            conn.rollback()
        finally:
            pool.putconn(conn)