from fastapi import APIRouter

from src.service.context_service import insert_embedding
from src.service.models.InputPayloadModels import EmbeddingInsertionPayload

router = APIRouter()


@router.post("/embeddings/", tags=["embedding"])
async def send_message_to_chatbot(request: EmbeddingInsertionPayload):
    insert_embedding(request.text, request.meta)
    return {"response": "Successfully created embeddings."}
