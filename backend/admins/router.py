from fastapi import APIRouter, HTTPException, Depends
import backend.admins.service as service
import exceptions
import backend.users.service as userserice
from authorisation import require_admin

router_admin = APIRouter()

@router_admin.get("/")
def get_users():
    try:
        return userserice.load_all_users()
    except exceptions.DbDownloadError as e :
        return HTTPException(
            status_code=400,
            detail= str(e)
        )

@router_admin.get("/{ticket_id}/assign")
def assing_agent(ticket_id, user=Depends(require_admin)):
    try:
        service.assign_agent_to_ticket(user, ticket_id)
    except Exception as e:
        print("Błąd", e)