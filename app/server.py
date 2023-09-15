import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.v1.router import router as router_v1

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(router_v1, prefix="/v1")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Thank you for using Thorium ✨"}
