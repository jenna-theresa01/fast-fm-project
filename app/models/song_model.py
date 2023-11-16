from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Column, ForeignKey, String, DateTime, Float, Table, Integer

from models.album_model import Album
from models.artist_model import Artist

class Base(DeclarativeBase):
    pass

# song_artists_association_table = Table("song_artists", Base.metadata, 
#     Column('artist_id', Integer, ForeignKey)
    
# )

class Song(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String, default="Title")
    length: Mapped[float] = Column(Float, default="Length")
    release_date: Mapped[str] = Column(DateTime.date, default="Release Date")

    albums: Mapped[List["Album"]] = relationship(back_populates="songs")
    artists: Mapped[List["Song"]] = relationship(back_populates="song")

class SongArtist(Base):
    __tablename__ = "song_artists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"))
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))

    # this is where I back populate to my tables that the foreign keys are connected to 
    artist: Mapped["Artist"] = relationship(back_populates="artists")
    song: Mapped["Song"] = relationship(back_populates="song")