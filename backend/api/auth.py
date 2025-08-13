from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.sessions import ensure_connected, get_client

router = APIRouter(prefix="/auth", tags=["auth"])

class PhoneIn(BaseModel):
    phone: str

class CodeIn(BaseModel):
    phone: str
    code: str

@router.post("/send_code")
async def send_code(data: PhoneIn):
    phone = data.phone
    client = await ensure_connected(phone)
    try:
        await client.send_code_request(phone)
        return {"ok": True, "phone": phone}
    except Exception as e:
        raise HTTPException(400, detail=str(e))

@router.post("/sign_in")
async def sign_in(data: CodeIn):
    phone, code = data.phone, data.code
    client = await ensure_connected(phone)
    try:
        await client.sign_in(phone=phone, code=code)
        me = await client.get_me()
        return {"ok": True, "user": {"id": me.id, "name": me.first_name}}
    except Exception as e:
        raise HTTPException(400, detail=str(e))
