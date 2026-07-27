from users.service import decode_token, check_user_admin
from tickets import repository



def check_ticket_is_close(ticket_id):
    if repository.check_if_ticket_close(ticket_id) == "CLOSED":
        return False
    return True

def check_ticket_exist(ticket_id):
    if repository.db_exists_ticket(ticket_id) is None:
        return False
    return True

def assign_agent(ticket_id, jwt_token):
    user_id = decode_token(jwt_token)
    if not check_ticket_exist(ticket_id):
        return {"error":"Nie ma takiego ticketu"}
    if not check_user_admin(user_id):
        return {"error": "Nie masz uprawnień aby to zrobić"}
    if not check_ticket_is_close(ticket_id):
        return {"error": "Ten ticket jst zamkniety"}

    return repository.assign_agent(ticket_id, user_id)

def create_ticket(ticket, user_d):
    return repository.add_ticket(ticket, user_d)

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

def get_tickets_by_status(status, limit, page):
    return repository.get_tickets_by_status(status)

def get_all_tickets(limit, page):
    offset = (page-1) * limit
    rows = repository.get_all_tickets(limit, offset)
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
