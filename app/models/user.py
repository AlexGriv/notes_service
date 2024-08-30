# app/models/user.py
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from app.core.db import Base
from sqlalchemy import Boolean, Column, Integer


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_active: bool = Column(Boolean, default=True)
    is_verified: bool = Column(Boolean, default=True)
