from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(title="Username", max_length=100, unique=True, index=True)
    full_name: str | None = Field(default=None, max_length=100)
    email: str | None = Field(default=None, max_length=100)
    hashed_password: str = Field(title="Hashed Password")
    disabled: bool = Field(default=False)