from typing import Optional

from pydantic import BaseModel, EmailStr

class PlaylistSchema(BaseModel):
    id: int
    title: str
    length: float
    created_by: int
    date_added: str

class PlaylistSongSchema(BaseModel):
    id: int
    song_id: int
    playlist_id: int
    order: int