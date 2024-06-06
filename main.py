from fastapi import FastAPI
from routers import auth, posts
from database import Base, engine

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
