from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .. import database, crud, schemas
import os

router = APIRouter(prefix="/admin", tags=["admin"])

# Load admin credentials from .env
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


# -----------------------
# Admin Login
# -----------------------
@router.post("/login")
def admin_login(username: str = Form(...), password: str = Form(...)):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


# -----------------------
# Admin Authentication Helper
# -----------------------
def admin_auth(username: str, password: str):
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")


# -----------------------
# Add News
# -----------------------
from fastapi import UploadFile, File

@router.post("/news", response_model=schemas.NewsOut)
def add_news(
    title: str = Form(...),
    slug: str = Form(...),
    content: str = Form(...),
    author: str = Form(...),
    image: UploadFile = File(None),   # <-- File upload
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)

    image_path = None
    if image:
        # save uploaded file to local folder
        os.makedirs("static/images", exist_ok=True)

        file_location = f"static/images/{image.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
        image_path = file_location

    news_obj = schemas.NewsCreate(
        title=title, slug=slug, content=content, author=author, image=image_path
    )
    return crud.create_news(db, news_obj)


#edit news

@router.put("/news/{news_id}", response_model=schemas.NewsOut)
def edit_news(
    news_id: int,
    title: str = Form(...),
    slug: str = Form(...),
    content: str = Form(...),
    author: str = Form(...),
    image: UploadFile = File(None),  # optional
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)

    image_path = None
    if image:
        os.makedirs("static/images", exist_ok=True)

        file_location = f"static/images/{image.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
        image_path = file_location

    news_obj = schemas.NewsCreate(
        title=title, slug=slug, content=content, author=author, image=image_path
    )
    updated = crud.update_news(db, news_id, news_obj)
    if not updated:
        raise HTTPException(status_code=404, detail="News not found")
    return updated



# -----------------------
# Delete News
# -----------------------
@router.delete("/news/{news_id}")
def remove_news(
    news_id: int,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)
    deleted = crud.delete_news(db, news_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="News not found")
    return {"detail": "Deleted successfully"}
