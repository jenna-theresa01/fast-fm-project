from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime

from models.song_model import Song

class Base(DeclarativeBase):
    pass

class Album(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String, default="Title")
    length: Mapped[float] = Column(Float, default="Length")
    release_date: Mapped[str] = Column(DateTime.date, default="Release Date")

    songs: Mapped[List["Song"]] = relationship(back_populates="albums")

    # do I need to back populate created by foreign key to another table?

class AlbumSong(Base):
    __tablename__ = "album_songs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"))
    order: Mapped[int] = Column(Integer, default="Order")

    # this is where I back populate to my tables that the foreign keys are connected to 
    song: Mapped["Song"] = relationship(back_populates="albums")
    album: Mapped["Album"] = relationship(back_populates="songs")