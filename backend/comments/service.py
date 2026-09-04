import exceptions
from backend.tickets.service import check_ticket_is_close, check_ticket_exist
import backend.comments.repository as repository
from backend.users.service import decode_token


def add_comment(user_id ,ticket_id, comment, token):
    try:
        if decode_token(token)["id"] != user_id:
            raise exceptions.UserError("Użytkownik jest niepoprawny")
        if not check_ticket_exist(ticket_id):
            raise exceptions.TicketDontExistsError("Nie ma takiego Ticketu")
        if not check_ticket_is_close(ticket_id):
            raise exceptions.TicketClosedError("Ticket jestjuż zamknięty")
    except Exception as e:
        print("Błąd", e)
        raise exceptions.CommentError("Wystąpił błąd z komentarzem")


    return repository.create_comment(ticket_id, comment, user_id)

def get_all_comments(ticket_id):
    if not check_ticket_exist(ticket_id):
        raise exceptions.TicketDontExistsError("Nie ma takiego Ticketu")
    if not check_ticket_is_close(ticket_id):
        raise exceptions.TicketClosedError("Ticket jestjuż zamknięty")

    rows = repository.get_all_comments(ticket_id)

    if not rows:
        return {"information": "Nie ma tutaj jeszcze komentazry"}

    return [{
        "id":row[0],
        "content":row[1],
        "ticket_id":ticket_id,
        "author_id":row[2],
        "created":row[3]
    }
        for row in rows
    ]

def get_comment(ticket_id, comment_id):
    if not check_ticket_exist(ticket_id):
        raise exceptions.TicketDontExistsError("Nie ma takiego Ticketu")
    if not check_ticket_is_close(ticket_id):
        raise exceptions.TicketClosedError("Ticket jestjuż zamknięty")

    items = repository.get_comm(comment_id)
    if items is None:
        raise exceptions.CommentDontExistaError("Komentarz nie istnieje")

    return {
        "id":comment_id,
        "content":items[0],
        "ticket_id":items[1],
        "author_id":items[2],
        "created":items[3]
    }

def delete_comment(ticket_id, comment_id):
    if not check_ticket_exist(ticket_id):
        raise exceptions.TicketDontExistsError("Nie ma takiego Ticketu")
    if not check_ticket_is_close(ticket_id):
        raise exceptions.TicketClosedError("Ticket jestjuż zamknięty")

    return repository.delete_comm(comment_id)

def update_commnent(ticket_id, comment_id, content):
    if not check_ticket_exist(ticket_id):
        raise exceptions.TicketDontExistsError("Nie ma takiego Ticketu")
    if not check_ticket_is_close(ticket_id):
        raise exceptions.TicketClosedError("Ticket jestjuż zamknięty")

    return update_commnent(content, comment_id)