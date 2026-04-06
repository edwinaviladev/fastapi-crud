from sqlmodel import Field, SQLModel

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(title="Title", max_length=100)
    description: str = Field(title="Description", max_length=1000)