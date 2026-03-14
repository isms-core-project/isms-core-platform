"""AI assistant API — streaming chat endpoint.

POST /api/v1/ai/chat
Returns SSE stream: data: {"text": "..."} chunks, terminated by data: [DONE]
"""

from typing import Literal

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.users import User
from src.services.ai_service import stream_chat

router = APIRouter(prefix="/ai", tags=["ai"])


class ChatMessage(BaseModel):
    role: str   # "user" | "assistant"
    content: str


class AIChatRequest(BaseModel):
    messages: list[ChatMessage]
    context_type: Literal["control", "general"] = "control"
    context_id: str | None = None       # control group UUID
    mode: Literal["assistant", "audit_prep", "gap_narrator"] = "assistant"


@router.post("/chat")
async def chat(
    body: AIChatRequest,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Stream an AI response as Server-Sent Events."""
    messages = [{"role": m.role, "content": m.content} for m in body.messages]

    return StreamingResponse(
        stream_chat(db, messages, body.context_type, body.context_id, body.mode),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@router.get("/status")
def ai_status(
    _user: User = Depends(get_current_user),
) -> dict:
    """Check whether AI is configured."""
    from src.core.config import get_settings
    settings = get_settings()
    return {"configured": bool(settings.anthropic_api_key), "model": settings.ai_model}
