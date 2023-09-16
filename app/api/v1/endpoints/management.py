from fastapi import APIRouter
from starlette import status

from app.schemas.documents.delete import DocumentDeleteBody
from app.schemas.documents.insert import DocumentInsertResponse, DocumentInsertBody
from app.services.documents import storage

router = APIRouter()


@router.post("/documents/", status_code=status.HTTP_201_CREATED)
async def insert_document(body: DocumentInsertBody) -> DocumentInsertResponse:
    document_id: str = storage.insert_document(body)
    return DocumentInsertResponse(id=document_id)


@router.delete("/documents/", status_code=status.HTTP_200_OK)
async def delete_document(body: DocumentDeleteBody):
    storage.delete_document(body)
    return {
        "response": "ok",
        "message": "Successfully deleted document."
    }
