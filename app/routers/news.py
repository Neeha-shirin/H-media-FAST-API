from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, crud, schemas

router = APIRouter(prefix="/news", tags=["news"])

# news.py
@router.get("/", response_model=list[schemas.NewsOut])
def read_news(db: Session = Depends(database.get_db)):
    return crud.get_all_news(db)

@router.get("/{news_id}", response_model=schemas.NewsOut)
def read_news_detail(news_id: int, db: Session = Depends(database.get_db)):
    news_item = crud.get_news_by_id(db, news_id)
    if not news_item:
        raise HTTPException(status_code=404, detail="News not found")
    return news_item
