from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsBase(BaseModel):
    title: str
    slug: str
    content: str
    author: str
    image: Optional[str] = None  # stores path of uploaded file

class NewsCreate(NewsBase):
    pass

class NewsOut(NewsBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


from sqlalchemy.orm import Session
from . import models, schemas

# Create banner
def create_banner(db: Session, banner: schemas.BannerCreate):
    db_banner = models.Banner(
        title=banner.title,
        image=banner.image,
        status=banner.status
    )
    db.add(db_banner)
    db.commit()
    db.refresh(db_banner)
    return db_banner

# Update banner
def update_banner(db: Session, banner_id: int, banner: schemas.BannerCreate):
    db_banner = db.query(models.Banner).filter(models.Banner.id == banner_id).first()
    if not db_banner:
        return None
    db_banner.title = banner.title
    db_banner.image = banner.image
    db_banner.status = banner.status
    db.commit()
    db.refresh(db_banner)
    return db_banner

# Delete banner
def delete_banner(db: Session, banner_id: int):
    db_banner = db.query(models.Banner).filter(models.Banner.id == banner_id).first()
    if not db_banner:
        return False
    db.delete(db_banner)
    db.commit()
    return True

# Get all banners
def get_all_banners(db: Session):
    return db.query(models.Banner).all()

# Get banner by id
def get_banner_by_id(db: Session, banner_id: int):
    return db.query(models.Banner).filter(models.Banner.id == banner_id).first()
