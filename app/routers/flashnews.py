from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .. import database, crud, schemas

router = APIRouter(prefix="/admin/flash-news", tags=["Flash News"])
public_router = APIRouter(prefix="/flash-news", tags=["Public – Flash News"])

# Simple admin authentication (like Cinema News)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_auth(username: str, password: str):
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")


# ---------------- Admin Routes ----------------

# Create Flash News
@router.post("/", response_model=schemas.FlashNewsOut)
def create_flash_news(
    title: str = Form(...),
    status: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)
    flash_obj = schemas.FlashNewsCreate(title=title, status=status)
    return crud.create_flash_news(db, flash_obj)


# Update Flash News
@router.put("/{flash_id}", response_model=schemas.FlashNewsOut)
def update_flash_news(
    flash_id: int,
    title: str = Form(...),
    status: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)
    flash_obj = schemas.FlashNewsCreate(title=title, status=status)
    updated = crud.update_flash_news(db, flash_id, flash_obj)
    if not updated:
        raise HTTPException(status_code=404, detail="Flash News not found")
    return updated


# Delete Flash News
@router.delete("/{flash_id}")
def delete_flash_news(
    flash_id: int,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    admin_auth(username, password)
    deleted = crud.delete_flash_news(db, flash_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Flash News not found")
    return {"detail": "Deleted successfully"}


# ---------------- Public Routes ----------------

@public_router.get("/", response_model=list[schemas.FlashNewsOut])
def get_all_flash_news(db: Session = Depends(database.get_db)):
    return crud.get_all_flash_news(db)

@public_router.get("/{flash_id}", response_model=schemas.FlashNewsOut)
def get_one_flash_news(flash_id: int, db: Session = Depends(database.get_db)):
    item = crud.get_flash_news_by_id(db, flash_id)
    if not item:
        raise HTTPException(status_code=404, detail="Flash News not found")
    return item
