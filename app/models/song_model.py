from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Column, ForeignKey, String, DateTime, Float, Table, Integer

from models.album_model import AlbumModel
from models.artist_model import ArtistModel

class Base(DeclarativeBase):
    pass

# song_artists_association_table = Table("song_artists", Base.metadata, 
#     Column('artist_id', Integer, ForeignKey)
    
# )

class SongModel(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String, default="Title")
    length: Mapped[float] = Column(Float, default="Length")
    release_date: Mapped[str] = Column(DateTime.date, default="Release Date")

    albums: Mapped[List["AlbumModel"]] = relationship(back_populates="songs")
    artists: Mapped[List["SongModel"]] = relationship(back_populates="song")

class SongArtistModel(Base):
    __tablename__ = "song_artists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"))
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))

    # this is where I back populate to my tables that the foreign keys are connected to 
    artist: Mapped["ArtistModel"] = relationship(back_populates="artists")
    song: Mapped["SongModel"] = relationship(back_populates="song")