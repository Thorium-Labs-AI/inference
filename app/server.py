from http.client import HTTPException

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.v1.router import router as router_v1

app = FastAPI(
    title="Thorium Labs - Client API",
    description="The REST interface for chat-based LLMs. \n Developed by Thorium Labs Inc.",
)

app.include_router(router_v1, prefix="/v1")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": str(exc.detail)}


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Thank you for using Thorium ✨"
    }
