from fastapi import APIRouter
from database import create_connection

conn = create_connection()

router = APIRouter()

@router.get("/")
def get_users():
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, role FROM users")
        rows = cur.fetchall()
        return [{
            "id":row[0],
            "name":row[1],
            "role":row[2]
        }
            for row in rows
        ]
@router.post("/add-user")
def create_user():
    pass