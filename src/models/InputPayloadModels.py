from typing import Union, Optional, List

from pydantic import BaseModel

from src.models.DocumentMetadataModel import DocumentMetadataModel


class ChatHistoryItem(BaseModel):
    text: str
    isUser: bool


class ChatRequestPayload(BaseModel):
    message: str
    history: List[ChatHistoryItem]


class EmbeddingInsertionPayload(BaseModel):
    document_name: str
    content: str
    meta: DocumentMetadataModel


class ConfigUpsertPayload(BaseModel):
    # Frontend Config
    display_name: Optional[str]
    color_scheme: Optional[List[str]]  # primary, secondary, accent, error
    font_url: Optional[str]
    img_url: Optional[str]
    dimensions: Optional[List[int]]

    # Chatbot Config
    welcome_message: Optional[str]
    instructions_message: Optional[str]
    context_message: Optional[str]
    allowed_domains: Optional[Union[List[str], None]]
    sentence_chunk_size: Optional[int]
    word_overlap: Optional[int]
