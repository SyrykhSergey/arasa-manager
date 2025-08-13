from telethon import TelegramClient
from telethon.sessions import StringSession
from pathlib import Path
from typing import Dict, Optional
from .config import settings

SESSIONS_PATH = Path(settings.SESSIONS_DIR)
SESSIONS_PATH.mkdir(parents=True, exist_ok=True)

_clients: Dict[str, TelegramClient] = {}


def get_session_path(phone: str) -> Path:
    safe = phone.replace("+", "plus_")
    return SESSIONS_PATH / f"{safe}.session"


def get_client(phone: str) -> TelegramClient:
    if phone in _clients:
        return _clients[phone]
    session_file = str(get_session_path(phone))
    client = TelegramClient(session_file, settings.TELEGRAM_API_ID, settings.TELEGRAM_API_HASH)
    _clients[phone] = client
    return client


async def ensure_connected(phone: str) -> TelegramClient:
    client = get_client(phone)
    if not client.is_connected():
        await client.connect()
    return client


async def disconnect_all():
    for cl in _clients.values():
        if cl.is_connected():
            await cl.disconnect()
