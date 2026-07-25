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

def get_comment(ticket_id, comment_id):
    if not check_ticket_exist(ticket_id):
        return {"error": "Nie ma takiego tokenu"}
    if not check_ticket_is_close(ticket_id):
        return {"error": "Ten token jst zamkniety"}

    items = repository.get_comm(comment_id)

    return {
        "id":comment_id,
        "content":items[0],
        "ticket_id":items[1],
        "author_id":items[2],
        "created":items[3]
    }

def delete_comment(ticket_id, comment_id):
    if not check_ticket_exist(ticket_id):
        return {"error": "Nie ma takiego tokenu"}
    if not check_ticket_is_close(ticket_id):
        return {"error": "Ten token jst zamkniety"}

    return repository.delete_comm(comment_id)

def update_commnent(ticket_id, comment_id, content):
    if not check_ticket_exist(ticket_id):
        return {"error": "Nie ma takiego tokenu"}
    if not check_ticket_is_close(ticket_id):
        return {"error": "Ten token jst zamkniety"}

    return update_commnent(content, comment_id)