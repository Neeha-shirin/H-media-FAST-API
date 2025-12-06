from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from .. import database, crud, schemas
import os

router = APIRouter(prefix="/admin/more-news", tags=["More News"])

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_auth(username: str, password: str):
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")

# Add More News
@router.post("/", response_model=schemas.MoreNewsOut)
def add_more_news(
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
        os.makedirs("static/more_news_images", exist_ok=True)
        file_location = f"static/more_news_images/{image.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
        image_path = file_location

    obj = schemas.MoreNewsCreate(
        title=title, slug=slug, content=content, author=author, image=image_path
    )
    return crud.create_more_news(db, obj)


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, crud, schemas

# Public routes
public_router = APIRouter(prefix="/more-news", tags=["Public – More News"])

@public_router.get("/", response_model=list[schemas.MoreNewsOut])
def get_all(db: Session = Depends(database.get_db)):
    return crud.get_all_more_news(db)

@public_router.get("/{item_id}", response_model=schemas.MoreNewsOut)
def get_one(item_id: int, db: Session = Depends(database.get_db)):
    item = crud.get_more_news_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# Update More News
@router.put("/{item_id}", response_model=schemas.MoreNewsOut)
def update_more_news(
    item_id: int,
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
        import os
        os.makedirs("static/more_news_images", exist_ok=True)
        file_location = f"static/more_news_images/{image.filename}"
        with open(file_location, "wb+") as f:
            f.write(image.file.read())
        image_path = file_location

    news_obj = schemas.MoreNewsCreate(
        title=title, slug=slug, content=content, author=author, image=image_path
    )
    updated = crud.update_more_news(db, item_id, news_obj)
    if not updated:
        raise HTTPException(status_code=404, detail="More News not found")
    return updated


# Delete More News
@router.delete("/{item_id}")
def delete_more_news(
    item_id: int,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)
    deleted = crud.delete_more_news(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="More News not found")
    return {"detail": "Deleted successfully"}
