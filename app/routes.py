from fastapi import APIRouter, HTTPException
from app.database import db
router = APIRouter()

@router.get("/")
def home():
    return {"detail":"HOME"}

@router.post("/create_review/")
def create_review(data):
    db.append(data)
    return data

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
def delete_revire(id):
    for index,review in enumerate(db):
        if review.id == id :
            db[index].pop()
            return {"detail": "Task deleted"}