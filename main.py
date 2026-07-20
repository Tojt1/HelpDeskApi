from fastapi import FastAPI
from router import router
from database import create_tables

create_tables()

app = FastAPI()

app.include_router(router)