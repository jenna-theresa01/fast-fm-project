from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String

from models.playlist_model import PlaylistModel

class Base(DeclarativeBase):
    pass

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")
    playlists_created: Mapped[int] = Column(Integer, default="Playlists Created")

    # create the relationship to the playlist model from the user model
    user: Mapped[List["PlaylistModel"]] = relationship(back_populates="playlists")

