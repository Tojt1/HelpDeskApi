from fastapi import FastAPI
from users.router import router_user
from database import create_tables

create_tables()

app = FastAPI()

app.include_router(router_user)