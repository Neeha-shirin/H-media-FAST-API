from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import news, admin,banner,cinema_news
from .routers import cinema_news
from .routers import meet_the_person, more_news

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="News Website Backend")
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(news.router)   # public news
app.include_router(admin.router)  # admin CRUD
app.include_router(banner.router)         # admin CRUD
app.include_router(banner.public_router)  # public view


app.include_router(cinema_news.router)        # admin endpoints
app.include_router(cinema_news.public_router) # public endpoints
app.include_router(meet_the_person.router)
app.include_router(meet_the_person.public_router)

app.include_router(more_news.router)
app.include_router(more_news.public_router)
