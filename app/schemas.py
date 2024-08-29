from typing import Optional
from pydantic import BaseModel, Field
from fastapi_users import schemas


class NoteCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    description: str = Field(..., min_length=1, max_length=150)
    user_id: Optional[int]

    class Config:
        orm_mode = True


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
