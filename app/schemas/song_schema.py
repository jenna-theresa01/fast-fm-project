from typing import Optional

from pydantic import BaseModel, EmailStr

class SongSchema(BaseModel):
    id: int
    title: str
    length: float
    release_date: str

class SongArtistSchema(BaseModel): 
    id: int
    artist_id: int
    song_id: int