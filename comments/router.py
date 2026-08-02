from fastapi import APIRouter, Depends, HTTPException
from comments.schem import Comment
from users.service import decode_token
import comments.service as service
import exceptions
comments_router = APIRouter()

@comments_router.post("/tickets/{ticket_id}/comments")
def create_comment(ticket_id:int, comment:Comment, user_id = Depends(decode_token)):
    try:
        return service.add_comment(ticket_id, comment, user_id)
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