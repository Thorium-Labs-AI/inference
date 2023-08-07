from fastapi import APIRouter
from starlette import status

from src.models.InputPayloadModels import EmbeddingInsertionPayload, ConfigUpsertPayload
from src.service.context_service import ContextService
from src.service.database.config_store import update_config

router = APIRouter()


@router.post("/embeddings/", tags=["embedding"], status_code=status.HTTP_201_CREATED)
async def insert_document(request: EmbeddingInsertionPayload):
    context_service = ContextService()
    context_service.insert_embedding(document_name=request.document_name, content=request.content,
                                     metadata=request.meta)
    return {"response": "Successfully created embeddings."}


@router.post("/config/", tags=["configuration"], status_code=status.HTTP_201_CREATED)
async def upsert_config(request: ConfigUpsertPayload):
    update_config(customer="DemoCustomerFromToken", payload=request)
    return {"response": "Successfully updated configuration."}
