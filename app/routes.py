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

@router.put("/update_review")
async def update_review(data: Review):
    id :int = data.id
    for r in db:
        if(r.id == id):
            r.nome = data.nome
            r.resenha = data.resenha
            r.nota = data.nota
            return {"detail": "Review updated"}
    return {"detail": "Review not updated"}
        
@router.delete("/delete_review/{id}")
def delete_review(id : int):
    for r in db:
        if(r.id == id):
            db.remove(r)
            return {"detail": "Review deleted"}
    return {"detail": "Review not deleted"}