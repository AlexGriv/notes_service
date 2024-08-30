# app/models/user.py
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from app.core.db import Base
from sqlalchemy import Column, Integer


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
