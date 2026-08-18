from fastapi import FastAPI
from backend.users.router import router_user
from database import create_tables
from backend.tickets.router import router_ticket
from backend.comments.router import comments_router
from fastapi.middleware.cors import CORSMiddleware

create_tables()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()

app.include_router(router_user)
app.include_router(router_ticket)
app.include_router(comments_router)