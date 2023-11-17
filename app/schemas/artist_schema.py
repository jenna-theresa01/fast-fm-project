from typing import Optional

from pydantic import BaseModel, EmailStr

class ArtistSchema(BaseModel):
    id: int
    name: str
    albums_released: int

class AlbumArtistSchema(BaseModel):
    id: int
    artist_id: int
    album_id: int