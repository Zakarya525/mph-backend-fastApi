from fastapi import APIRouter, Depends

from schemas.users import UserResponse
from utils import get_current_user

user_router = APIRouter(prefix="", tags=['Users'])


@user_router.get("/users/me", response_model=UserResponse)
async def read_users_me(current_user=Depends(get_current_user)):
    return current_user.to_json()
