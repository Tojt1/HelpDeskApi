from fastapi import APIRouter, Depends, HTTPException
from backend.tickets.schemas import CreateTicket
from backend.tickets import service
from typing import Optional
from authorisation import oauth2
import exceptions

router_ticket = APIRouter()

@router_ticket.post("/tickets")
def create_ticket(ticket:CreateTicket, user_id = Depends(oauth2)):
    try:
        print(ticket)
        print(user_id)
        return service.create_ticket(ticket, user_id)
    except exceptions.DbAddError as e:
        raise HTTPException(
            status_code=400,
            detail= str(e)
        )

@router_ticket.get("/tickets")
def get_tickets(sort:str = "created", status: Optional[str] = None, limit:int = 10, page:int = 1):
    try:
        if status is None:
            return service.get_all_tickets(limit, page, sort)
        else:
            return service.get_all_tickets_by_status(status, sort, limit, page)
    except exceptions.DbDownloadError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
@router_ticket.get("/tickets/{user_id}")
def get_ticket_by_user(user_id = Depends(oauth2)):
    return service.get_tickets_by_user(user_id)

@router_ticket.get("/tickets/{ticket_id}")
def get_ticket_by_id(ticket_id:int):
    try:
        return service.get_ticket_by_id(ticket_id)
    except exceptions.DbDownloadError as e:
        raise HTTPException(
            status_code=400,
            detail= str(e)
        )

@router_ticket.patch("/tickets/{ticket_id}/assign")
def assign_agent(ticket_id:int, jwt_code):
    try:
        return service.assign_agent(ticket_id, jwt_code)
    except exceptions.DBAssignAgentError as e:
        raise HTTPException(
            status_code=400,
            detail= str(e)
        )