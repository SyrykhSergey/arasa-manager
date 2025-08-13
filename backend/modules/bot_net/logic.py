from core.sessions import ensure_connected, get_client

async def send_message(phone: str, peer: str, text: str):
    client = await ensure_connected(phone)
    await client.send_message(peer, text)
    return True
