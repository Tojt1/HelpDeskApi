import backend.admins.repository as repository
import datetime

def load_all_users():
    rows = repository.get_all_users()
    return [{
        "id":row[0],
        "name":row[1],
        "role":row[2]
    }
        for row in rows
    ]

def assign_agent_to_ticket(user, ticket_id):
    try:
        repository.assign_agent(user["id"], datetime.datetime.now(), ticket_id)
    except Exception as e:
        print("Błąd", e)