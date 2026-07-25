from database import  create_connection
import exceptions

def create_comment(ticket_id, comment, user):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO comment(content, ticket_id, author_id) VALUES (%s, %s, %s)", (comment.content, ticket_id, user))
            conn.commit()
            return {"information": "Pomyślnie utworzono komentarz"}
        except exceptions.DbAddError:
            return {"error": "wystąpił błą∂ podczas dodawania komentazra"}

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
        try:
            cur.execute("DELETE FROM tickets WHERE id = %s", (comm_id, ))
            conn.commit()
            return {"information": "Pomyślnie usunięto komentarz"}
        except exceptions.DbDeleteError:
            return {"error": "Wystąpił błą∂ podczas usuwania komentarza"}

def update_comm(new_content,comm_id):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE comment SET content = %s WHERE id = %s", (new_content, comm_id))
            conn.commit()
            return {"information": "Pomyślnie zaktualizowano komentarz"}
        except exceptions.DbUpdateError:
            return {"error": "Wystąpił błą∂ podczas updatowanie komentarza"}