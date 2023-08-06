import logging

import redis.asyncio as redis
from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter
from starlette.middleware.cors import CORSMiddleware

from .routers.management import router as management_router
from .routers.user import router as client_router
from ..service.security.cors import allowed_origins
from ..utils.shared import from_env

logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.on_event("startup")
async def startup():
    try:
        redis_url = from_env("REDIS_URL", throw_err=True)
        redis_instance = redis.from_url(url=redis_url, encoding="utf8", decode_responses=True)
        await FastAPILimiter.init(redis_instance)
    except Exception as e:
        logging.error(f'Starting FastAPI limiter failed. Reason: {e}')


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
def read_root():
    return {"message": "Thank you for using Flow! 🚀"}
