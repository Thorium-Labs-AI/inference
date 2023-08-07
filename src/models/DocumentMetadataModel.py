from typing import Optional

from pydantic import BaseModel


class DocumentMetadataModel(BaseModel):
    customer: str
    language: Optional[str]
    tags: dict
    format: str
