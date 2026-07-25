from database import  create_connection

def create_comment(ticket_id, comment, user):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("INSERT INTO comment(content, ticket_id, author_id) VALUES (%s, %s, %s)", (comment.content, ticket_id, user))
        conn.commit()
        return {"information": "Pomyślnie utworzono komentarz"}

def get_all_comments(ticket_id):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id, content, author_id, created FROM comment WHERE ticket_id = %s", (ticket_id, ))
        return cur.fetchall()

def get_comm(comm_id):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT content, ticket_id, author_id, created FROM comment WHERE id = %s", (comm_id, ))
        return cur.fetchone()

def delete_comm(comm_id):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM tickets WHERE id = %s", (comm_id, ))
        conn.commit()
        return {"information": "Pomyślnie usunięto komentarz"}