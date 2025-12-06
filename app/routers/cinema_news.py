from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from .. import database, crud, schemas
import os

router = APIRouter(prefix="/admin/cinema-news", tags=["Cinema News"])

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_auth(username: str, password: str):
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")

# Add Cinema News
@router.post("/", response_model=schemas.CinemaNewsOut)
def add_cinema_news(
    title: str = Form(...),
    slug: str = Form(...),
    content: str = Form(...),
    author: str = Form(...),
    image: UploadFile = File(None),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)

    image_path = None
    if image:
        os.makedirs("static/cinema_images", exist_ok=True)
        file_location = f"static/cinema_images/{image.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
        image_path = file_location

    news_obj = schemas.CinemaNewsCreate(
        title=title, slug=slug, content=content, author=author, image=image_path
    )
    return crud.create_cinema_news(db, news_obj)


# Edit Cinema News
@router.put("/{news_id}", response_model=schemas.CinemaNewsOut)
def edit_cinema_news(
    news_id: int,
    title: str = Form(...),
    slug: str = Form(...),
    content: str = Form(...),
    author: str = Form(...),
    image: UploadFile = File(None),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)

    image_path = None
    if image:
        os.makedirs("static/cinema_images", exist_ok=True)
        file_location = f"static/cinema_images/{image.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
        image_path = file_location

    news_obj = schemas.CinemaNewsCreate(
        title=title, slug=slug, content=content, author=author, image=image_path
    )
    updated = crud.update_cinema_news(db, news_id, news_obj)
    if not updated:
        raise HTTPException(status_code=404, detail="Cinema News not found")
    return updated


# Delete Cinema News
@router.delete("/{news_id}")
def remove_cinema_news(
    news_id: int,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)
    deleted = crud.delete_cinema_news(db, news_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Cinema News not found")
    return {"detail": "Deleted successfully"}


# Public endpoints
public_router = APIRouter(prefix="/cinema-news", tags=["Cinema News"])

@public_router.get("/", response_model=list[schemas.CinemaNewsOut])
def read_cinema_news(db: Session = Depends(database.get_db)):
    return crud.get_all_cinema_news(db)
