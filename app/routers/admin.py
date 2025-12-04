from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from .. import database, crud, schemas
import os

router = APIRouter(prefix="/admin", tags=["admin"])

# Read admin username/password from .env
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

# Simple login (form-based)
@router.post("/login")
def admin_login(username: str = Form(...), password: str = Form(...)):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Protected admin CRUD
def admin_auth(username: str = Form(...), password: str = Form(...)):
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")

@router.post("/news", response_model=schemas.NewsOut)
def add_news(news: schemas.NewsCreate, db: Session = Depends(database.get_db),
             username: str = Form(...), password: str = Form(...)):
    admin_auth(username, password)
    return crud.create_news(db, news)

@router.put("/news/{news_id}", response_model=schemas.NewsOut)
def edit_news(news_id: int, news: schemas.NewsCreate, db: Session = Depends(database.get_db),
              username: str = Form(...), password: str = Form(...)):
    admin_auth(username, password)
    updated = crud.update_news(db, news_id, news)
    if not updated:
        raise HTTPException(status_code=404, detail="News not found")
    return updated

@router.delete("/news/{news_id}")
def remove_news(news_id: int, db: Session = Depends(database.get_db),
                username: str = Form(...), password: str = Form(...)):
    admin_auth(username, password)
    deleted = crud.delete_news(db, news_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="News not found")
    return {"detail": "Deleted successfully"}
