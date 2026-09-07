import exceptions
from backend.tickets.service import check_ticket_is_close, check_ticket_exist
import backend.comments.repository as repository
from backend.users.service import decode_token
from backend.users.repository import getname


# Logistic for adding new comment
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

# Logistic for getting all comments on a specific
def get_all_comments(ticket_id, user_id, token):
    try:
        if decode_token(token)["id"] != user_id:
            raise exceptions.UserError()
        if not check_ticket_exist(ticket_id):
            raise exceptions.TicketDontExistsError("Nie ma takiego Ticketu")
        if not check_ticket_is_close(ticket_id):
            raise exceptions.TicketClosedError("Ticket jestjuż zamknięty")

        rows = repository.get_all_comments(ticket_id)
        user_name = getname(user_id)

        if not rows:
            return {"information": "Nie ma tutaj jeszcze komentazry"}

        return [{
            "id":row[0],
            "content":row[1],
            "ticket_id":ticket_id,
            "author_id":row[2],
            "author_name":user_name[0],
            "created":row[3]
        }
            for row in rows
        ]
    except Exception as e:
        print("Błąd", e)

# Logistic for deleting comment
def delete_comment(ticket_id, comment_id):
    if not check_ticket_exist(ticket_id):
        raise exceptions.TicketDontExistsError("Nie ma takiego Ticketu")
    if not check_ticket_is_close(ticket_id):
        raise exceptions.TicketClosedError("Ticket jestjuż zamknięty")

    return repository.delete_comm(comment_id)

# Logistic for updating comment
def update_commnent(ticket_id, comment_id, content):
    if not check_ticket_exist(ticket_id):
        raise exceptions.TicketDontExistsError("Nie ma takiego Ticketu")
    if not check_ticket_is_close(ticket_id):
        raise exceptions.TicketClosedError("Ticket jestjuż zamknięty")

    return update_commnent(content, comment_id)