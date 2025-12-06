from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/admin/meet-person", tags=["Admin – Meet The Person"])
public_router = APIRouter(prefix="/meet-person", tags=["Public – Meet The Person"])

# Admin authentication function
def admin_auth(username: str, password: str):
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin123"
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")


# ------------------- CREATE -------------------
@router.post("/", response_model=schemas.MeetThePersonOut)
def create_item(
    title: str = Form(...),
    slug: str = Form(...),
    content: str = Form(...),
    author: str = Form(...),
    image: UploadFile = File(None),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    admin_auth(username, password)

    image_path = None
    if image:
        import os
        os.makedirs("static/meet_person_images", exist_ok=True)
        file_location = f"static/meet_person_images/{image.filename}"
        with open(file_location, "wb+") as f:
            f.write(image.file.read())
        image_path = file_location

    data = schemas.MeetThePersonCreate(
        title=title, slug=slug, content=content, author=author, image=image_path
    )
    return crud.create_meet_person(db, data)


# ------------------- UPDATE -------------------
@router.put("/{item_id}", response_model=schemas.MeetThePersonOut)
def update_item(
    item_id: int,
    title: str = Form(...),
    slug: str = Form(...),
    content: str = Form(...),
    author: str = Form(...),
    image: UploadFile = File(None),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    admin_auth(username, password)

    image_path = None
    if image:
        import os
        os.makedirs("static/meet_person_images", exist_ok=True)
        file_location = f"static/meet_person_images/{image.filename}"
        with open(file_location, "wb+") as f:
            f.write(image.file.read())
        image_path = file_location

    data = schemas.MeetThePersonCreate(
        title=title, slug=slug, content=content, author=author, image=image_path
    )
    updated = crud.update_meet_person(db, item_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


# ------------------- DELETE -------------------
@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    admin_auth(username, password)
    deleted = crud.delete_meet_person(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Deleted successfully"}


# ------------------- PUBLIC GET -------------------
@public_router.get("/", response_model=list[schemas.MeetThePersonOut])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all_meet_person(db)


@public_router.get("/{item_id}", response_model=schemas.MeetThePersonOut)
def get_one(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_meet_person_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
