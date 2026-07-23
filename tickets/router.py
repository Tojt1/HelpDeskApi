from fastapi import APIRouter
from tickets.schem import CreateTicket
from tickets import service

router_ticket = APIRouter()

@router_ticket.post("/tickets")
def create_ticket(ticket:CreateTicket, user):
    return service.create_ticket(ticket, user)

@router_ticket.get("/tickets")
def get_tickets():
    return service.get_all_tickets()