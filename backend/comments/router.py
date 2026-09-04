from fastapi import APIRouter, Depends, HTTPException
from backend.comments.schemas import Comment
from authorisation import  oauth2
import backend.comments.service as service
import exceptions
comments_router = APIRouter()

@comments_router.post("/tickets/{user_id}/{ticket_id}/comments")
def create_comment(user_id:int ,ticket_id:int, comment:Comment, token = Depends(oauth2)):
    try:
        return service.add_comment(user_id, ticket_id, comment, token)
    except exceptions.DbAddError as e:
        return HTTPException(
            status_code=400,
            detail= str(e)
        )


@comments_router.get("/tickets/{ticket_id}/comments")
def get_comments_to_ticket(ticket_id):
    try:
        return service.get_all_comments(ticket_id)
    except exceptions.DbDownloadError as e:
        return HTTPException(
            status_code=400,
            detail = str(e)
        )

@comments_router.get("/tickets/{ticket_id}/comments/{comment_id}")
def get_coemment_ticket(ticket_id, comment_id):
    try:
        return service.get_comment(ticket_id, comment_id)
    except exceptions.DbDownloadError as e:
        return HTTPException(
            status_code=400,
            detail= str(e)
        )

@comments_router.delete("/tickets/{ticket_id}/comments/{comment_id}")
def delete_comments_from_ticket(ticket_id, comment_id):
    try:
        return service.delete_comment(ticket_id, comment_id)
    except exceptions.DbDeleteError as e:
        return HTTPException(
            status_code=400,
            detail = str(e)
        )

@comments_router.patch("/tickets/{ticket_id}/comments/{comment_id}")
def update_comment(ticket_id, comment_id, content):
    try:
        return service.update_commnent(ticket_id, comment_id, content)
    except exceptions.DbUpdateError as e:
        return HTTPException(
            status_code=400,
            detail= str(e)
        )