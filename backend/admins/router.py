from fastapi import APIRouter, HTTPException, Depends
import backend.admins.service as service
import exceptions

router_admin = APIRouter()

@router_admin.get("/")
def get_users():
    try:
        return service.load_all_users()
    except exceptions.DbDownloadError as e :
        return HTTPException(
            status_code=400,
            detail= str(e)
        )