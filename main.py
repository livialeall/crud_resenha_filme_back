from fastapi import FastAPI
from app.routes import router

app = FastAPI(title = "CRUD Resenha de Filmes")

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)

