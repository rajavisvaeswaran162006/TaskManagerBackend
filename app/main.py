
from fastapi import FastAPI

from app.database import engine, Base
from app import models
from app.routes import router

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Student Task & Note Manager API",
    description="A simple API for user authentication and personal task management",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Student Task & Note Manager API",
        "status": "Running"
    }
