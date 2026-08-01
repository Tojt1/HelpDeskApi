from database import pool
import exceptions

def create_comment(ticket_id, comment, user):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO comment(content, ticket_id, author_id) VALUES (%s, %s, %s)",
                        (comment.content, ticket_id, user))

            conn.commit()

            return {"information": "Pomyślnie utworzono komentarz"}

        except Exception:
            conn.rollback()
            raise exceptions.DbAddError("Wystąpił błą∂ podczas dodawania komentarza")

        finally:
            pool.putconn(conn)

def get_all_comments(ticket_id):
    conn = pool.getconn()
    with conn.cursor() as cur:
        try:
            cur.execute("SELECT id, content, author_id, created FROM comment WHERE ticket_id = %s",
                        (ticket_id, ))

            return cur.fetchall()

        except Exception:
            raise exceptions.DbDownloadError("Błą∂ podczas pobierania komentarzy")

        finally:
            pool.putconn(conn)

def get_comm(comm_id):
    conn = pool.getconn()
    with conn.cursor() as cur:
        try:
            cur.execute("SELECT content, ticket_id, author_id, created FROM comment WHERE id = %s", (comm_id, ))
            return cur.fetchone()

        except Exception:
            raise exceptions.DbDownloadError("Błąd podczas pobierania komentarza")

        finally:
            pool.putconn(conn)

def delete_comm(comm_id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("DELETE FROM tickets WHERE id = %s", (comm_id, ))
            conn.commit()
            return {"information": "Pomyślnie usunięto komentarz"}

        except Exception:
            conn.rollback()
            raise exceptions.DbDeleteError("Wystąpił błąd podczas usuwania komentarza")

        finally:
            pool.putconn(conn)

def update_comm(new_content,comm_id):
    conn = pool.getconn()

    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE comment SET content = %s WHERE id = %s", (new_content, comm_id))
            conn.commit()

            return True

        except Exception:
            conn.rollback()
            raise exceptions.DbUpdateError("Wystąpił błą∂ podczas aktualizacji komentarza")

        finally:
            pool.putconn(conn)