from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import news, admin,banner

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
