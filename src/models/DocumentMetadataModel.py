from typing import Optional

from pydantic import BaseModel


class DocumentMetadataModel(BaseModel):
    language: Optional[str]
    tags: list
    format: str
