from tickets.service import check_ticket_is_close, check_ticket_exist
from users.service import decode_token
import comments.repository as repository



def add_comment(ticket_id, comment, jwt):
    if not check_ticket_exist(ticket_id):
        return {"error": "Nie ma takiego tokenu"}
    if not check_ticket_is_close(ticket_id):
        return {"error": "Ten token jst zamkniety"}

    user = decode_token(jwt)

    return repository.create_comment(ticket_id, comment, user)

def get_all_comments(ticket_id):
    if not check_ticket_exist(ticket_id):
        return {"error": "Nie ma takiego tokenu"}
    if not check_ticket_is_close(ticket_id):
        return {"error": "Ten token jst zamkniety"}

    rows = repository.get_all_comments(ticket_id)

    return [{
        "id":row[0],
        "content":row[1],
        "ticket_id":ticket_id,
        "author_id":row[2],
        "created":row[3]
    }
        for row in rows
    ]
