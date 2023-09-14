import logging

import redis.asyncio as redis
from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter
from starlette.middleware.cors import CORSMiddleware

from .routers.inference import router as inference_router
from .routers.management import router as management_router
from ..config.get_config import config

logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.on_event("startup")
async def startup():
    try:
        redis_instance = redis.Redis(host=config.redis_host, port=config.redis_port, username=config.redis_username,
                                     password=config.redis_password)
        await FastAPILimiter.init(redis_instance)
    except Exception as e:
        logging.error(f'Starting FastAPI limiter failed. Reason: {e}')


app.include_router(inference_router, prefix="/inference")
app.include_router(management_router, prefix="/management")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Thank you for using Flow! 🚀"}
