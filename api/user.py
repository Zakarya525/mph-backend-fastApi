from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from database import get_db_session
from models import User
from schemas.users import UserResponse
from utils import verify_token

user_router = APIRouter(prefix="", tags=['Users'])


@user_router.get("/users/me", response_model=UserResponse)
async def read_users_me(username=Depends(verify_token)):
    with get_db_session() as db_session:
        user = db_session.query(User).filter_by(user_name=username).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User '{username}' cannot be found.",
            )
        return user.to_json()
