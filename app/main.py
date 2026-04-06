from fastapi import FastAPI
from sqlmodel import SQLModel
from app.core.config import engine
from app.core.cache import init_cache
from app.api.v1 import auth, users, tasks

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    SQLModel.metadata.create_all(engine)
    await init_cache()

# Incluir routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)