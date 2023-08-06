from fastapi import APIRouter

from src.models.InputPayloadModels import EmbeddingInsertionPayload, ConfigUpsertPayload
from src.service.context_service import insert_embedding
from src.service.database.config_store import update_config

router = APIRouter()


@router.post("/embeddings/", tags=["embedding"])
async def insert_document(request: EmbeddingInsertionPayload):
    insert_embedding(document_name=request.document_name, content=request.content, metadata=request.meta)
    return {"response": "Successfully created embeddings."}


@router.post("/config/", tags=["configuration"])
async def upsert_config(request: ConfigUpsertPayload):
    update_config(customer="DemoCustomerFromToken", payload=request)
    return {"response": "Successfully updated configuration."}
