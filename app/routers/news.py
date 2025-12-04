from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, crud, schemas

router = APIRouter(prefix="/news", tags=["news"])

@router.get("/", response_model=list[schemas.NewsOut])
def read_news(db: Session = Depends(database.get_db)):
    return crud.get_all_news(db)

@router.get("/{news_id}", response_model=schemas.NewsOut)
def read_news_detail(news_id: int, db: Session = Depends(database.get_db)):
    return crud.get_news(db, news_id)
