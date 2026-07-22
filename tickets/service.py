from users.service import decode_token
from tickets import repository

def create_ticket(ticket, user):
    user_id = decode_token(user)
    return repository.add_ticket(ticket, user_id)
