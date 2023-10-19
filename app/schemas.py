import uuid
from typing import List

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


# TO support creation and update APIs
class CreateAndUpdatePost(BaseModel):
    title: str
    content: str


# TO support list and get APIs
class Post(CreateAndUpdatePost):
    id: int

    class Config:
        orm_mode = True


# To support list post-API
class PaginatedPostInfo(BaseModel):
    limit: int
    offset: int
    data: List[Post]
