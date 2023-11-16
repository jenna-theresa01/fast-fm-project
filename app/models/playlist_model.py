from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime

class Base(DeclarativeBase):
    pass

class Playlist(Base):
    __tablename__ = "playlists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String, default="Title")
    length: Mapped[float] = Column(Float, default="Length")
    created_by: Mapped[int] = mapped_column(ForeignKey("users_id"))
    date_added: Mapped[str] = Column(DateTime.date, default="Date Added")

    # do I need to back populate created by foreign key to the users table?

class PlaylistSong(Base):
    __tablename__ = "playlist_songs"

    id: Mapped[int] = mapped_column(primary_key=True, default=True)
    song_id: Mapped[int] = mapped_column(ForeignKey(songs_id))
    playlist_id: Mapped[int] = mapped_column(ForeignKey(playlists.id))
    order: Mapped[int] = Column(Integer, default="Order")

    # this is where I back populate to my tables that the foreign keys are connected to 
    