from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine
from app.api.auth import router as auth_router

app = FastAPI(title="Atlas API")
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Atlas API 🚀"}


@app.get("/health")
def health():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {
        "database": "Connected ✅",
        "api": "Running 🚀",
    }