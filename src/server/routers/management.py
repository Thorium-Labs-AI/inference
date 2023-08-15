from fastapi import APIRouter
from starlette import status

from src.models.ChatbotConfig import ChatbotConfig
from src.models.ContextModels import EmbeddingInsertPayload
from src.service.context_service import ContextService
from src.service.database.config_store import ConfigStore

router = APIRouter()


@router.post("/embeddings/", tags=["embedding"], status_code=status.HTTP_201_CREATED)
async def insert_document(request: EmbeddingInsertPayload):
    context_service = ContextService()
    context_service.insert_embedding(document_name=request.document_name, content=request.content,
                                     metadata=request.metadata, customer="HardcodedCustomer")
    return {"response": "Successfully created embeddings."}


@router.post("/chatbots/", tags=["configuration"], status_code=status.HTTP_201_CREATED)
async def upsert_config(request: ChatbotConfig):
    config_store = ConfigStore()
    config_store.update_config(chatbot_config=request)
    return {"response": "Successfully updated configuration."}
