from pydantic import BaseModel

class Review(BaseModel):
    id:int = None
    nome: str
    resenha: str = None
    nota: int