import requests

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.check_note import check_spelling
from app.models import Note
from app.schemas import NoteCreate


async def create_note(
    new_note: NoteCreate,
    session: AsyncSession,
) -> Note:
    new_note_data = new_note.dict()
    #for word in new_note_data['description']:
    #   if check_spelling(word)
    #try:
    #    result = check_spelling(new_note_data['description'])
    #    for error in result:
    #        new_note_data['description'] = error['s'][0]
    #except requests.exceptions.RequestException as e:
    #    new_note_data['description'] = e

    db_note = Note(**new_note_data)

    session.add(db_note)
    await session.commit()
    await session.refresh(db_note)
    return db_note


async def get_all_notes(session: AsyncSession, ) -> list[NoteCreate]:
    result = await session.execute(select(Note))
    return result.scalars().all()
