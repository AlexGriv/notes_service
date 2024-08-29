from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import auth_backend, fastapi_users
from app.schemas import UserCreate, UserRead, UserUpdate, NoteCreate
from app.crud import create_note, get_all_notes
from app.core.user import current_user
from app.models import User

router = APIRouter()


@router.post(
    '/new_note/',
    response_model_exclude_none=True,
    response_model_exclude_defaults=True,
    tags=['note'],
)
async def create_new_note(
        note: NoteCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    new_note = await create_note(note, session, user)
    return new_note


@router.get(
    '/all/',
    response_model=list[NoteCreate],
    response_model_exclude_none=True,
    tags=['note'],
)
async def get_all(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    notes = await get_all_notes(session, user)

    if not notes:
        raise HTTPException(status_code=404, detail="Notes not found")

    return notes


from fastapi import APIRouter

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)
