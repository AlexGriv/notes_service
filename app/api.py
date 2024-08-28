from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session

from app.crud import create_note, get_all_notes
from app.schemas import NoteCreate

router = APIRouter()


@router.post(
    '/new_note/',
    response_model_exclude_none=True,
    response_model_exclude_defaults=True,
)
async def create_new_note(
        note: NoteCreate,
        session: AsyncSession = Depends(get_async_session),
):
    new_note = await create_note(note, session)
    return new_note


@router.get(
    '/all/',
    response_model=list[NoteCreate],
    response_model_exclude_none=True,
)
async def get_all(session: AsyncSession = Depends(get_async_session)):
    notes = await get_all_notes(session)

    if not notes:
        raise HTTPException(status_code=404, detail="Notes not found")

    return notes
