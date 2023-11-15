from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime

class Base(DeclarativeBase):
    pass

class Playlist(Base):
    __tablename__ = "playlists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Mapped(String, default="Title")
    length: Mapped[float] = Mapped(Float, default="Length")
    created_by: Mapped[int] = mapped_column(ForeignKey("users_id"))
    date_added: Mapped[str] = Mapped(DateTime.date, default="Date Added")