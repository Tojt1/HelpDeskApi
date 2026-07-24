from tickets.service import check_ticket_is_close, check_ticket_exist
from users.service import decode_token
from comments.repository import create_comment



def add_comment(ticket_id, comment, jwt):
    if not check_ticket_exist(ticket_id):
        return {"error": "Nie ma takiego tokenu"}
    if not check_ticket_is_close(ticket_id):
        return {"error": "Ten token jst zamkniety"}

    user = decode_token(jwt)

    return create_comment(ticket_id, comment, user)
