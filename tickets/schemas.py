from pydantic import BaseModel

class CreateTicket(BaseModel):
    title: str
    description: str
    category: str