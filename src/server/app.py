import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routers.requests import router as client_router
from .routers.management import router as management_router
from ..service.security.cors import allowed_origins
from ..service.security.rate_limits import limiter

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(client_router, prefix="/chat")
app.include_router(management_router, prefix="/management")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
@limiter.limit("5/minute")
def read_root(request: Request):
    return {"message": "This works! 🚀"}
