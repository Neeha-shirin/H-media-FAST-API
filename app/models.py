from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)      # new
    content = Column(String, nullable=False)
    author = Column(String, nullable=False)                 # new
    image = Column(String, nullable=True)                   # new, store image URL/path
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # already exists


class Banner(Base):
    __tablename__ = "banners"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    image = Column(String, nullable=True)  # store banner image path
    status = Column(String, default="inactive")  # "active" or "inactive"
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    
    

class CinemaNews(Base):
    __tablename__ = "cinema_news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    content = Column(String, nullable=False)
    author = Column(String, nullable=False)
    image = Column(String, nullable=True)  # image path
    created_at = Column(DateTime(timezone=True), server_default=func.now())
