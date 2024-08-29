from app.core.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    description = Column(String(150), index=True)
    user_id = Column(Integer,
                     ForeignKey('user.id', name='fk_notes_user_id_user'))
