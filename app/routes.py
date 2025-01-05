from numbers import Number
from fastapi import APIRouter, Form, HTTPException
from pydantic import BaseModel
from app.database import db
from app.models import Review
router = APIRouter()

@router.post("/create_review")
async def create_review(data: Review):
    data.id = db.__len__() + 1
    db.append(data)
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
def delete_review(id : int):
    for r in db:
        if(r.id == id):
            db.remove(r)
            return {"detail": "Review deleted"}
    return {"detail": "Review not deleted"}