from sqlmodel import Session
from app.core.config import engine

def get_session():
    with Session(engine) as session:
        yield session