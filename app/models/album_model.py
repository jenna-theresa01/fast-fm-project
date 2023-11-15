from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime

class Base(DeclarativeBase):
    pass

class Album(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String, default="Title")
    length: Mapped[float] = Column(Float, default="Length")
    release_date: Mapped[str] = Column(DateTime.date, default="Release Date")