from fastapi import APIRouter
from comments.schem import Comment
from comments.service import add_comment

comments_router = APIRouter()

@comments_router.post("/tickets/{ticket_id}/comments")
def create_comment(ticket_id:int, comment:Comment, jwt):
    return add_comment(ticket_id, comment, jwt)