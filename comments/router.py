from fastapi import APIRouter, Depends
from comments.schem import Comment
from users.service import decode_token
import comments.service as service

comments_router = APIRouter()

@comments_router.post("/tickets/{ticket_id}/comments")
def create_comment(ticket_id:int, comment:Comment, user_id = Depends(decode_token)):
    return service.add_comment(ticket_id, comment, user_id)


@comments_router.get("/tickets/{ticket_id}/comments")
def get_comments_to_ticket(ticket_id):
    return service.get_all_comments(ticket_id)

@comments_router.get("/tickets/{ticket_id}/comments/{comment_id}")
def get_coemment_ticket(ticket_id, comment_id):
    return service.get_comment(ticket_id, comment_id)

@comments_router.delete("/tickets/{ticket_id}/comments/{comment_id}")
def delete_comments_from_ticket(ticket_id, comment_id):
    return service.delete_comment(ticket_id, comment_id)

@comments_router.patch("/tickets/{ticket_id}/comments/{comment_id}")
def update_comment(ticket_id, comment_id, content):
    return service.update_commnent(ticket_id, comment_id, content)