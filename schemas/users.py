from pydantic import BaseModel

from schemas.store import StoreResponseSchema


class RegisterUserSchema(BaseModel):
    email: str
    username: str
    password: str


class UserResponse(BaseModel):
    email: str
    username: str
    store: StoreResponseSchema
