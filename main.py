from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(title = "CRUD Resenha de Filmes")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Origem permitida
    allow_credentials=True,  # Permite envio de cookies/autenticação
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)

