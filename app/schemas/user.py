from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str | None = None
    email: str | None = None

class UserPublic(BaseModel):
    id: int | None
    username: str
    full_name: str | None
    email: str | None
    disabled: bool