from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from auth import get_current_user
from schemas import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
