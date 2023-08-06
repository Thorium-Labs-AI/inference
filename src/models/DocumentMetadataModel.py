from typing import Optional

from pydantic import BaseModel


class DocumentMetadataModel(BaseModel):
    customer: str
    document_name: str
    language: Optional[str]
    tags: dict
    format: str
