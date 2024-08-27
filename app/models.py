from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    description = Column(String(150), index=True)
