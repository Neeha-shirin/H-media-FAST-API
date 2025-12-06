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



#cinema 

# ----------------------- Cinema News -----------------------

from sqlalchemy.orm import Session
from . import models, schemas


# Create
def create_cinema_news(db: Session, news: schemas.CinemaNewsCreate):
    db_news = models.CinemaNews(
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

# Update
def update_cinema_news(db: Session, news_id: int, news: schemas.CinemaNewsCreate):
    db_news = db.query(models.CinemaNews).filter(models.CinemaNews.id == news_id).first()
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

# Get all
def get_all_cinema_news(db: Session):
    return db.query(models.CinemaNews).all()

# Get by id
def get_cinema_news_by_id(db: Session, news_id: int):
    return db.query(models.CinemaNews).filter(models.CinemaNews.id == news_id).first()

# Delete
def delete_cinema_news(db: Session, news_id: int):
    db_news = db.query(models.CinemaNews).filter(models.CinemaNews.id == news_id).first()
    if not db_news:
        return None
    db.delete(db_news)
    db.commit()
    return db_news




# ----------------------- Meet The Person -----------------------

def create_meet_person(db: Session, data: schemas.MeetThePersonCreate):
    db_item = models.MeetThePerson(
        title=data.title,
        slug=data.slug,
        content=data.content,
        author=data.author,
        image=data.image
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_meet_person(db: Session, item_id: int, data: schemas.MeetThePersonCreate):
    db_item = db.query(models.MeetThePerson).filter(models.MeetThePerson.id == item_id).first()
    if not db_item:
        return None

    db_item.title = data.title
    db_item.slug = data.slug
    db_item.content = data.content
    db_item.author = data.author
    db_item.image = data.image

    db.commit()
    db.refresh(db_item)
    return db_item


def get_all_meet_person(db: Session):
    return db.query(models.MeetThePerson).all()


def get_meet_person_by_id(db: Session, item_id: int):
    return db.query(models.MeetThePerson).filter(models.MeetThePerson.id == item_id).first()


def delete_meet_person(db: Session, item_id: int):
    db_item = db.query(models.MeetThePerson).filter(models.MeetThePerson.id == item_id).first()
    if not db_item:
        return None

    db.delete(db_item)
    db.commit()
    return True


# ----------------------- More News -----------------------

def create_more_news(db: Session, data: schemas.MoreNewsCreate):
    db_item = models.MoreNews(
        title=data.title,
        slug=data.slug,
        content=data.content,
        author=data.author,
        image=data.image
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_more_news(db: Session, item_id: int, data: schemas.MoreNewsCreate):
    db_item = db.query(models.MoreNews).filter(models.MoreNews.id == item_id).first()
    if not db_item:
        return None

    db_item.title = data.title
    db_item.slug = data.slug
    db_item.content = data.content
    db_item.author = data.author
    db_item.image = data.image

    db.commit()
    db.refresh(db_item)
    return db_item


def get_all_more_news(db: Session):
    return db.query(models.MoreNews).all()


def get_more_news_by_id(db: Session, item_id: int):
    return db.query(models.MoreNews).filter(models.MoreNews.id == item_id).first()


def delete_more_news(db: Session, item_id: int):
    db_item = db.query(models.MoreNews).filter(models.MoreNews.id == item_id).first()
    if not db_item:
        return None

    db.delete(db_item)
    db.commit()
    return True
