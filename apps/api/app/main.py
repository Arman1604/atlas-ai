from fastapi import FastAPI

app = FastAPI(
    title="Atlas API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Atlas API 🚀",
        "status": "online"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }