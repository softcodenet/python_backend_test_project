from pydantic import BaseModel, EmailStr, constr
from typing import List, Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=6)

class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    text: constr(max_length=1048576)  # 1 MB max size

class Post(BaseModel):
    id: int
    text: str
    owner_id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
