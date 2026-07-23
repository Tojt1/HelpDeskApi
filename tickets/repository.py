from database import create_connection

def add_ticket(ticket, user_id):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO tickets(title, description, priority, category, author_id) VALUES(%s, %s, %s, %s, %s)", (ticket.title, ticket.description, ticket.priority, ticket.category, user_id))
            conn.commit()
            return {"information": "Pomyślnie utworzono ticket"}
        except ValueError:
            return {"error":"podano nieprawidlowoa wartosc"}

def get_all_tickets():
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute("SELECT id, title, description, status, priority, category, author_id, agent_id, created, updated, closed FROM tickets")
            return cur.fetchall()
        except ValueError:
            return {"error": "wystąpił błąd podczas pobierania danych"}

def get_ticket(ticket_id):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute(
                "SELECT id, title, description, status, priority, category, author_id, agent_id, created, updated, closed FROM tickets WHERE id =%s", (ticket_id, ))
            return cur.fetchone()
        except ValueError:
            return {"error": "wystąpił błąd podczas pobierania danych"}