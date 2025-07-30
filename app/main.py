# app/main.py
from fastapi import FastAPI, Depends
from app.database import engine, get_db
from app import models
from app.routers import items

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Hello World"}