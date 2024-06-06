from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import PostCreate, Post, User
from models import Post as DBPost
from dependencies import get_db, get_current_active_user
from cachetools import TTLCache
from typing import List

router = APIRouter()

cache = TTLCache(maxsize=100, ttl=300)

@router.post("/", response_model=Post)
def add_post(post: PostCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    new_post = DBPost(text=post.text, owner_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/", response_model=List[Post])
def get_posts(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    if 'posts' in cache:
        return cache['posts']
    posts = db.query(DBPost).filter(DBPost.owner_id == current_user.id).all()
    cache['posts'] = posts
    return posts

@router.delete("/{post_id}", response_model=dict)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    post = db.query(DBPost).filter(DBPost.id == post_id, DBPost.owner_id == current_user.id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    if 'posts' in cache:
        del cache['posts']
    return {"message": "Post deleted successfully"}