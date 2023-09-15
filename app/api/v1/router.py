from fastapi import APIRouter

from endpoints.inference import router as inference_router
from endpoints.management import router as management_router
from endpoints.public import router as public_router

router = APIRouter()

router.include_router(public_router, prefix="/public")
router.include_router(inference_router, prefix="/inference")
router.include_router(management_router, prefix="/management")
