from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Column, ForeignKey, Integer, String

from models.album_model import Album

class Base(DeclarativeBase):
    pass

class Artist(Base):
    __tablename__ = "artists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")
    albums_released: Mapped[int] = Column(Integer, default="Albums Released")

    # connect the albums_released column to the id in album class/table


class AlbumArtist(Base):
    __tablename__ = "album_artists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"))
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"))

    # this is where I back populate to my tables that the foreign keys are connected to 
    artists: Mapped["Artist"] = relationship(back_populates="artists")
    albums: Mapped["Album"] = relationship(back_populates="albums")