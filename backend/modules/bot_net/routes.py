from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .logic import send_message

router = APIRouter(prefix="/modules/bot_net", tags=["modules:bot_net"])


class SendIn(BaseModel):
    phone: str
    peer: str
    text: str


@router.post("/run")
async def run(in_: SendIn):
    try:
        await send_message(in_.phone, in_.peer, in_.text)
        return {"ok": True}
    except Exception as e:
        raise HTTPException(400, detail=str(e))


def init_routes(app):
    app.include_router(router)
