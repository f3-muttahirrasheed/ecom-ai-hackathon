from fastapi import APIRouter
from pydantic import BaseModel
from .groq_integration import ask_groq

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = ask_groq(request.message)
    return {"response": response}
