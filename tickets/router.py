from fastapi import APIRouter, Depends
from tickets.schem import CreateTicket
from tickets import service
from typing import Optional
from users.service import decode_token

router_ticket = APIRouter()

@router_ticket.post("/tickets")
def create_ticket(ticket:CreateTicket, user_d = Depends(decode_token)):
    return service.create_ticket(ticket, user_d)

@router_ticket.get("/tickets")
def get_tickets(sort:str = "created", status: Optional[str] = None, limit:int = 10, page:int = 1):
    if status is None:
        return service.get_all_tickets(limit, page, sort)
    else:
        return service.get_all_tickets_by_status(status, sort,  limit, page)

@router_ticket.get("/tickets/{ticket_id}")
def get_ticket_by_id(ticket_id:int):
    return service.get_ticket_by_id(ticket_id)

@router_ticket.patch("/tickets/{ticket_id}/assign")
def assign_agent(ticket_id:int, jwt_code):
    return service.assign_agent(ticket_id, jwt_code)