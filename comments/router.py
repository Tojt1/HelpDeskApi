from fastapi import APIRouter
from comments.schem import Comment
import comments.service as service

comments_router = APIRouter()

@comments_router.post("/tickets/{ticket_id}/comments")
def create_comment(ticket_id:int, comment:Comment, jwt):
    return service.add_comment(ticket_id, comment, jwt)


@comments_router.get("/tickets/{ticket_id}/comments")
def get_comments_to_ticket(ticket_id):
    return service.get_all_comments(ticket_id)

@comments_router.get("/tickets/{ticket_id}/comments/{comment_id}")
def get_coemment_ticket(ticket_id, comment_id):
    return service.get_comment(ticket_id, comment_id)