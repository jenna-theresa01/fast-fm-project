from typing import Optional

from pydantic import BaseModel, EmailStr

class AlbumSchema(BaseModel):
    id: int
    title: str
    length: float
    release_date: str

class AlbumSongSchema(BaseModel):
    id: int
    song_id: int
    album_id: int
    order: int