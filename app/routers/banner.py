from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from .. import database, crud, schemas
import os

router = APIRouter(prefix="/admin/banner", tags=["banner"])

# Admin auth helper
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_auth(username: str, password: str):
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")


# -----------------------
# Add Banner
# -----------------------
@router.post("/", response_model=schemas.BannerOut)
def add_banner(
    title: str = Form(...),
    image: UploadFile = File(None),
    status: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)

    image_path = None
    if image:
        os.makedirs("static/banners", exist_ok=True)
        file_location = f"static/banners/{image.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
        image_path = file_location

    banner_obj = schemas.BannerCreate(title=title, image=image_path, status=status)
    return crud.create_banner(db, banner_obj)


# -----------------------
# Update Banner
# -----------------------
@router.put("/{banner_id}", response_model=schemas.BannerOut)
def edit_banner(
    banner_id: int,
    title: str = Form(...),
    image: UploadFile = File(None),
    status: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)

    image_path = None
    if image:
        os.makedirs("static/banners", exist_ok=True)
        file_location = f"static/banners/{image.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
        image_path = file_location

    banner_obj = schemas.BannerCreate(title=title, image=image_path, status=status)
    updated = crud.update_banner(db, banner_id, banner_obj)
    if not updated:
        raise HTTPException(status_code=404, detail="Banner not found")
    return updated


# -----------------------
# Delete Banner
# -----------------------
@router.delete("/{banner_id}")
def remove_banner(
    banner_id: int,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)
    deleted = crud.delete_banner(db, banner_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Banner not found")
    return {"detail": "Deleted successfully"}


# -----------------------
# Get Banners (Public)
# -----------------------
from fastapi import APIRouter

public_router = APIRouter(prefix="/banner", tags=["banner"])

@public_router.get("/", response_model=list[schemas.BannerOut])
def read_banners(db: Session = Depends(database.get_db)):
    return crud.get_all_banners(db)
