from typing import Optional

from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    id: int
    name: str
    playlists_created: int