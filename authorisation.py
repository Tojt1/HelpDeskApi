from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from backend.users.service import decode_token

oauth2 = OAuth2PasswordBearer(tokenUrl="/login")


def require_admin(token = Depends(oauth2)):
    user = decode_token(token)
    if user["role"] != "ADMIN":
        raise HTTPException(
            status_code=403,
            detail="status code required"
        )

    return user