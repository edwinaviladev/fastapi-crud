from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.core.database import get_session
from app.core.auth import authenticate_user, create_access_token
from app.schemas.token import LoginRequest, Token
from sqlmodel import Session

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token", response_model=Token)
def login_for_access_token(body: LoginRequest, session: Session = Depends(get_session)):
    user = authenticate_user(session, body.username, body.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return Token(access_token=access_token, token_type="bearer")