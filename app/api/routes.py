from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import langid
from app.services.llm_service import get_llm_response
from app.services.vector_db_service import search_similar_documents

router = APIRouter()

class Query(BaseModel):
    user_name: str
    question: str

@router.post("/query")
async def query(query: Query):
    try:
        context = search_similar_documents(query.question)
        if not context:
            raise HTTPException(status_code=404, detail="No relevant context found")
        language, confidence = langid.classify(query.question)
        print(language)
        response = get_llm_response(query.question, context[0], language)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
