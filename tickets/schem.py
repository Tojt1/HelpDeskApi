from pydantic import BaseModel

class Ticket(BaseModel):
    title: str
    description: str
    priority : int
    category: str