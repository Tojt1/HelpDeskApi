from fastapi import APIRouter

router_ticket = APIRouter()

@router_ticket.get("/ticket/<ticket_id>")
def get_ticket(ticket_id:int):
    