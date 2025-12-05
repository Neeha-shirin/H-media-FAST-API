from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# ---------------- News ----------------

class NewsBase(BaseModel):
    title: str
    slug: str
    content: str
    author: str
    image: Optional[str] = None


class NewsCreate(NewsBase):
    pass


class NewsOut(NewsBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ---------------- Banner ----------------

class BannerBase(BaseModel):
    title: str
    image: Optional[str] = None
    status: str   # "active" or "inactive"


class BannerCreate(BannerBase):
    pass


class BannerOut(BannerBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
