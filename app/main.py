from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import news, admin

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="News Website Backend")

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
