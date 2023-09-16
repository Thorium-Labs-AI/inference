from pydantic import BaseModel


class DocumentDeleteBody(BaseModel):
    document_id: str
