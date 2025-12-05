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
# -----------------------
# Banner CRUD
# -----------------------

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


def delete_banner(db: Session, banner_id: int):
    db_banner = db.query(models.Banner).filter(models.Banner.id == banner_id).first()
    if not db_banner:
        return None

    db.delete(db_banner)
    db.commit()
    return True


def get_all_banners(db: Session):
    return db.query(models.Banner).all()


def get_banner_by_id(db: Session, banner_id: int):
    return db.query(models.Banner).filter(models.Banner.id == banner_id).first()
