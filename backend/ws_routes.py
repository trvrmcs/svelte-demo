import asyncio
from fastapi import WebSocket


async def websocket_endpoint(ws: WebSocket) -> None:
    await ws.accept()
    i = 0
    while True:
        await ws.send_json({"some": "json", "i": i})
        i += 1
        await asyncio.sleep(1)
