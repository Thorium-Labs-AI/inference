import logging

from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from .routers.requests import router as client_router
from ..service.auth.authentication import authenticated

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(client_router, prefix="/chat")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")
def read_root():
    return {"message": "This works! 🚀"}


@app.get("/protected")
def get_protected(token: str = Depends(authenticated)):
    return {
        "message": "You've hit a private route 🕵️"
    }
