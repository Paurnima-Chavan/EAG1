from fastapi import APIRouter
from pydantic import BaseModel
from sse_server.utils.gmail_client import send_email_sse


router = APIRouter(prefix="/tools/gmail_notify")


class GmailNotifyRequest(BaseModel):
    to: str
    subject: str
    body: str


@router.post("/")
async def notify(request: GmailNotifyRequest):
    return await send_email_sse(request.to, request.subject, request.body)
