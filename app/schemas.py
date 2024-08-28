from pydantic import BaseModel, Field, validator


class NoteCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    description: str = Field(..., min_length=1, max_length=150)


class NotesDB(NoteCreate):
    id: int

    class Config:
        orm_mode = True
