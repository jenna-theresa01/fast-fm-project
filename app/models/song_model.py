from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float

class Base(DeclarativeBase):
    pass

class Song(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String, default="Title")
    length: Mapped[float] = Column(Float, default="Length")
    release_date: Mapped[str] = Column(DateTime.date, default="Release Date")
