from fastapi import APIRouter, Depends, HTTPException
from app.core.auth import get_current_active_user
from app.core.database import get_session
from app.crud.user import get_user_by_username
from app.models.user import User
from app.schemas.user import UserCreate, UserPublic
from app.core.config import password_hash
from sqlmodel import Session

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserPublic, status_code=201)
def create_user(body: UserCreate, session: Session = Depends(get_session)):
    if get_user_by_username(session, body.username):
        raise HTTPException(status_code=409, detail="Username already registered")
    user = User(
        username=body.username,
        full_name=body.full_name,
        email=body.email,
        hashed_password=password_hash.hash(body.password),
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/me", response_model=UserPublic)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user