from users.service import decode_token
from tickets import repository

def create_ticket(ticket, user):
    user_id = decode_token(user)
    return repository.add_ticket(ticket, user_id)

def get_all_tickets():
    rows = repository.get_all_tickets()
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

def get_ticket_by_id(ticket_id):
    row = repository.get_ticket(ticket_id)
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

