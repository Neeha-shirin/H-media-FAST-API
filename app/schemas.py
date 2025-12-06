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
        from_attributes = True  # Pydantic v2


# ---------------- Banner ----------------

class BannerBase(BaseModel):
    title: str
    image: Optional[str] = None
    status: str  # "active" or "inactive"

class BannerCreate(BannerBase):
    pass

class BannerOut(BannerBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ---------------- Cinema News ----------------

class CinemaNewsBase(BaseModel):
    title: str
    slug: str
    content: str
    author: str
    image: Optional[str] = None

class CinemaNewsCreate(CinemaNewsBase):
    pass

class CinemaNewsOut(CinemaNewsBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # <-- FIXED


# ---------------- Meet The Person ----------------

class MeetThePersonBase(BaseModel):
    title: str
    slug: str
    content: str
    author: str
    image: Optional[str] = None

class MeetThePersonCreate(MeetThePersonBase):
    pass

class MeetThePersonOut(MeetThePersonBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ---------------- More News ----------------

class MoreNewsBase(BaseModel):
    title: str
    slug: str
    content: str
    author: str
    image: Optional[str] = None

class MoreNewsCreate(MoreNewsBase):
    pass

class MoreNewsOut(MoreNewsBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
