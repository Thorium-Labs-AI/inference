import logging

import redis.asyncio as redis
from fastapi import FastAPI, Depends
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from starlette.middleware.cors import CORSMiddleware

from .routers.management import router as management_router
from .routers.user import router as client_router
from ..config.get_config import config
from ..service.security.cors import allowed_origins

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


app.include_router(client_router, prefix="/chat")
app.include_router(management_router, prefix="/management")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", dependencies=[Depends(RateLimiter(times=5, hours=1))])
def read_root():
    return {"message": "Thank you for using Flow! 🚀"}
