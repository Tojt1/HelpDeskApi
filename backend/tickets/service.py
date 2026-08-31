import exceptions
from backend.users.service import decode_token, check_user_admin
from backend.tickets import repository

allowed_sort = {
    "id":"id",
    "priority":"priority",
    "category":"category",
    "status":"status",
    "created":"created"
}

def check_ticket_is_close(ticket_id):
    if repository.check_if_ticket_close(ticket_id) == "CLOSED":
        return False
    return True

def check_ticket_exist(ticket_id):
    if repository.db_exists_ticket(ticket_id) is None:
        return False
    return True

def assign_agent(ticket_id, jwt_token):
    user_id = decode_token(jwt_token)["id"]
    if not check_ticket_exist(ticket_id):
        return {"error":"Nie ma takiego ticketu"}
    if not check_user_admin(user_id):
        return {"error": "Nie masz uprawnień aby to zrobić"}
    if not check_ticket_is_close(ticket_id):
        return {"error": "Ten ticket jst zamkniety"}

    return repository.assign_agent(ticket_id, user_id)

def create_ticket(ticket, token):
    print(ticket.title)
    if len(ticket.title) < 2:
        raise exceptions.EmptyFieldError("Wszystkie pole muszą być zapełnione")
    if len(ticket.description) < 2:
        raise exceptions.EmptyFieldError("Wszystkie pole muszą być zapełnione")
    if len(ticket.category) < 2:
        raise exceptions.EmptyFieldError("Wszystkie pole muszą być zapełnione")
    return repository.add_ticket(ticket, decode_token(token)["id"])

def get_ticket_by_id(ticket_id):
    row = repository.get_ticket(ticket_id)

    if row is None:
        return {"error": "Nie ma takiego ticketu"}
    return{
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "status": row[3],
        "priority": row[4],
        "category": row[5],
        "author_id": row[6],
        "agent_id": row[7],
        "updated": row[8],
        "closed": row[9]
    }

def get_all_tickets_by_status(status, sort,  limit, page):
    offset = (page-1) * limit
    sort = allowed_sort.get(sort, "id")
    return repository.get_tickets_by_status(status, sort, limit, offset)

def get_all_tickets(limit, page, sort):
    offset = (page-1) * limit
    sort = allowed_sort.get(sort, "id")
    rows = repository.get_all_tickets(limit, offset, sort)
    if not rows:
        return {"information": "Nie ma żadnych ticketów"}
    return[{
        "id":row[0],
        "title":row[1],
        "description":row[2],
        "status":row[3],
        "priority":row[4],
        "category":row[5],
        "author_id":row[6],
        "agent_id":row[7],
        "updated":row[8],
        "closed":row[9]
    }
        for row in rows
    ]

def get_tickets_by_user(token):
    user_id = decode_token(token)["id"]
    try:
        tickets = repository.get_tickets_by_user(user_id)
        return [
            {
            "id": ticket[0],
            "title": ticket[1],
            "descriiption": ticket[2],
            "status": ticket[3],
            "priority": ticket[4],
            "category": ticket[5],
            "created": ticket[6]
            }
            for ticket in tickets
        ]

    except Exception as e:
        print("Error", e)
        raise exceptions.DbDownloadError("Wystąpił  błąd pocxas pobierania ticketów")
