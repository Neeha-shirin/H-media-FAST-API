from sqlalchemy.orm import Session
from . import models, schemas

def create_news(db: Session, news: schemas.NewsCreate):
    db_news = models.News(
        title=news.title,
        slug=news.slug,
        content=news.content,
        author=news.author,
        image=news.image
    )
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

def update_news(db: Session, news_id: int, news: schemas.NewsCreate):
    db_news = db.query(models.News).filter(models.News.id == news_id).first()
    if not db_news:
        return None
    db_news.title = news.title
    db_news.slug = news.slug
    db_news.content = news.content
    db_news.author = news.author
    db_news.image = news.image
    db.commit()
    db.refresh(db_news)
    return db_news
# crud.py
def get_all_news(db: Session):
    return db.query(models.News).all()

def get_news_by_id(db: Session, news_id: int):
    return db.query(models.News).filter(models.News.id == news_id).first()
