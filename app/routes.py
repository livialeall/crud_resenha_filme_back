from fastapi import APIRouter, Form, HTTPException
from pydantic import BaseModel
from app.database import db
from app.models import Review
import logging
router = APIRouter()

@router.post("/create_review")
async def create_review(data: Review):
    db.append(data.model_dump())
    return data

@router.get("/")
def home():
    return {"detail":"HOME"}

@router.get("/read_review/")
def read_review():
    return db

@router.put("/update_review/{id}")
def update_review(id,data):
    for index,review in enumerate(db):
        if review.id == id:
            db[index] = data
            return data
        
@router.delete("/delete_review/{id}")
def delete_review(id):
    for index,review in enumerate(db):
        if review.id == id :
            db.remove(review)
            return {"detail": "Task deleted"}