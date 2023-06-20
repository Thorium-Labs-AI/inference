from fastapi import FastAPI, Depends
from .routers.requests import router as client_router
from ..service.auth.authentication import authenticated

app = FastAPI()
app.include_router(client_router, prefix="/chat")


@app.get("/")
def read_root():
    return {"message": "This works! 🚀"}


@app.get("/protected")
def get_protected(token: str = Depends(authenticated)):
    return {
        "message": "You've hit a private route 🕵️"
    }
