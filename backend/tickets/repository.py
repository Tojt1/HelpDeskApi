from database import pool
import datetime
import exceptions


def db_exists_ticket(ticket_id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT title FROM tickets WHERE id =%s", (ticket_id, ))
            return cur.fetchone()

        except Exception:
            raise exceptions.DBCehckExistsError("Wystąpił błąd podczas sprawdzania ticketu")

        finally:
            pool.putconn(conn)

def check_if_ticket_close(ticket_id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT status from tickets WHERE id = %s", (ticket_id, ))
            return cur.fetchone()

        except Exception:
            raise exceptions.DBCehckExistsError("wystąpił błąd podczas sprawdzania, czy ticket jest zamknięty")

        finally:
            pool.putconn(conn)

def assign_agent(ticket_id, user_id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE tickets SET status ='IN_PROGRESS', agent_id = %s, updated = %s WHERE id = %s", (user_id, datetime.datetime.now(), ticket_id))
            conn.commit()
            return True
        except Exception:
            conn.rollback()
            raise exceptions.DBAssignAgentError("Wystąpił błąd podczas przypisywania agenta do ticketa ")

        finally:
            pool.putconn(conn)

def add_ticket(ticket, user_id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO tickets(title, description, category, author_id) VALUES(%s, %s, %s, %s)",
                        (ticket.title, ticket.description, ticket.category, user_id))
            # conn.commit()
            return True

        except Exception:
            conn.rollback()
            raise exceptions.DbAddError("Wystąpił błąd podczas tworzenia ticketa")

        finally:
            pool.putconn(conn)

def get_ticket(ticket_id, user_id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT * FROM tickets WHERE id =%s and author_id =%s", (ticket_id, user_id))
            return cur.fetchone()

        except Exception:
            raise exceptions.DbDownloadError("Wystąpił błąd poczas pobierania ticketu")

        finally:
            pool.putconn(conn)

def get_tickets_by_status(status, sort,  limit, offset):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute(f"SELECT * FROM tickets WHERE status = %s ORDER BY {sort}  LIMIT %s OFFSET %s", (status, limit, offset ))
            return cur.fetchall()

        except Exception:
            raise exceptions.DbDownloadError("Wystąpił błąd podczas pobierania ticketów za pomoca statusu")

        finally:
            pool.putconn(conn)

def get_all_tickets(limit, offset, sort):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute(f"SELECT * FROM tickets ORDER BY {sort} DESC LIMIT %s OFFSET %s", (limit, offset))
            return cur.fetchall()

        except Exception:
            raise exceptions.DbDownloadError("Wystąpił błąd podczas pobierania ticketów")

        finally:
            pool.putconn(conn)

def get_tickets_by_user(user_id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT id, title, description, status, priority, category, created FROM tickets WHERE author_id = %s", (user_id, ))
            return cur.fetchall()

        except Exception as e:
            print("Error", e)

        finally:
            pool.putconn(conn)
