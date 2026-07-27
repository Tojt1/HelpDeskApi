from database import create_connection
import datetime
import exceptions




def db_exists_ticket(ticket_id):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT title FROM tickets WHERE id =%s", (ticket_id, ))
        return cur.fetchone()

def check_if_ticket_close(ticket_id):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT status from tickets WHERE id = %s", (ticket_id, ))
        return cur.fetchone()

def assign_agent(ticket_id, user_id):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE tickets SET status ='IN_PROGRESS', agent_id = %s, updated = %s WHERE id = %s", (user_id, datetime.datetime.now(), ticket_id))
            conn.commit()
            return {"information": "Pomyślnie dodano agenta do ticketa"}
        except exceptions.DbAddError:
            return {"error": "wystąpił błą∂ podczas dodawania agenta"}

def add_ticket(ticket, user_id):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO tickets(title, description, priority, category, author_id) VALUES(%s, %s, %s, %s, %s)", (ticket.title, ticket.description, ticket.priority, ticket.category, user_id))
            conn.commit()
            return {"information": "Pomyślnie utworzono ticket"}
        except exceptions.DbAddError:
            return {"error":"podano nieprawidlowoa wartosc"}

def get_ticket(ticket_id):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute(
                "SELECT * FROM tickets WHERE id =%s", (ticket_id, ))
            return cur.fetchone()
        except exceptions.DbDownloadError:
            return {"error": "wystąpił błąd podczas pobierania danych"}

def get_tickets_by_status(status, limit, offset):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute("SELECT * FROM tickets WHERE status = %s LIMIT %s OFFSET %s", (status, limit, offset ))
            return cur.fetchall()
        except exceptions.DbDownloadError:
            return {"error": "wystąpił błąd podczas pobierania danych"}

def get_all_tickets(limit, offset):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute("SELECT * FROM tickets LIMIT %s OFFSET %s", (limit, offset))
            return cur.fetchall()
        except exceptions.DbDownloadError:
            return {"error": "wystąpił błąd podczas pobierania danych"}
