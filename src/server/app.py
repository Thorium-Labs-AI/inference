from fastapi import FastAPI
from .routers.requests import router as client_router

app = FastAPI()
app.include_router(client_router, prefix="/chat")

@app.get("/")
def read_root():
    return {"message": "This works! 🚀"}
