from typing import List
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List
from .models import Note
from app.core.db import get_async_session
from app import models, schemas
from app.crud import create_note
from app.schemas import NoteCreate, NotesDB

router = APIRouter()


@router.post('/new_note/', response_model_exclude_none=True,
             response_model_exclude_defaults=True,)
async def create_new_note(
        note: NoteCreate,
        session: AsyncSession = Depends(get_async_session),
):
    new_note = await create_note(note, session)
    return new_note

@router.get('/all/', response_model_exclude_none=True)
async def get_all_notes(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Note))
    notes = result.scalars().all()

    if not notes:
        raise HTTPException(status_code=404, detail="Notes not found")

    return notes
