from pydantic import BaseModel


class DocumentInsertBody(BaseModel):
    name: str
    content: str
    description: str


class DocumentInsertResponse(BaseModel):
    id: str
