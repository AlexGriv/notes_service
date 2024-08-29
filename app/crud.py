import requests
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.check_note import correct_text
from app.models import Note, User
from app.schemas import NoteCreate


async def create_note(new_note: NoteCreate,
                      session: AsyncSession,
                      user: Optional[User] = None) -> Note:
    new_note_data = new_note.dict()

    if user is not None:
        new_note_data['user_id'] = user.id

    try:
        for key, value in new_note_data.items():
            if isinstance(value, str):
                new_note_data[key] = correct_text(value)

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при обращении к Яндекс.Спеллеру: {e}")

    db_note = Note(**new_note_data)

    session.add(db_note)
    await session.commit()
    await session.refresh(db_note)
    return db_note


async def get_all_notes(session: AsyncSession, user: User) -> list[NoteCreate]:
    if user.is_superuser:
        result = await session.execute(select(Note))
        return result.scalars().all()
    else:
        reservations = await session.execute(
            select(Note).where(Note.user_id == user.id))
        return reservations.scalars().all()
