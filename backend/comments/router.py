from fastapi import APIRouter, Depends, HTTPException
from backend.comments.schemas import Comment
from authorisation import  oauth2
import backend.comments.service as service
import exceptions
comments_router = APIRouter()

# Creating a comment on a specific ticket
@comments_router.post("/tickets/{user_id}/{ticket_id}/comments")
def create_comment(user_id:int ,ticket_id:int, comment:Comment, token = Depends(oauth2)):
    try:
        return service.add_comment(user_id, ticket_id, comment, token)
    except exceptions.DbAddError as e:
        raise HTTPException(
            status_code=400,
            detail= str(e)
        )
    except exceptions.TicketDontExistsError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except exceptions.TicketClosedError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except exceptions.CommentError as e:
        raise HTTPException(
            status_code=400,
            detail= str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# Get all coments on a specific ticket
@comments_router.get("/tickets/{user_id}/{ticket_id}/comments")
def get_comments_to_ticket(user_id:int, ticket_id:int, token = Depends(oauth2)):
    try:
        return service.get_all_comments(ticket_id, user_id, token)
    except exceptions.DbDownloadError as e:
        return HTTPException(
            status_code=400,
            detail = str(e)
        )

# Delete comment
@comments_router.delete("/tickets/{user_id}/{ticket_id}/comments/{comment_id}")
def delete_comment_from_ticket(user_id:int, ticket_id:int, comment_id:int, token = Depends(oauth2)):
    try:
        return service.delete_comment(user_id,ticket_id, comment_id, token)
    except exceptions.DbDeleteError as e:
        return HTTPException(
            status_code=400,
            detail = str(e)
        )

#Change content of comment
@comments_router.patch("/tickets/{ticket_id}/comments/{comment_id}")
def update_comment(ticket_id, comment_id, content):
    try:
        return service.update_commnent(ticket_id, comment_id, content)
    except exceptions.DbUpdateError as e:
        return HTTPException(
            status_code=400,
            detail= str(e)
        )