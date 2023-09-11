from typing import Dict
import pathlib
import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import aiofiles
from uuid import uuid4
from . import ws_routes

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = PROJECT_ROOT / "frontend" / "dist"

INDEX = DIST / "index.html"
app = FastAPI()

"""
Must be the path pointed to by `base` in vite.config.ts
"""
app.mount("/dist", StaticFiles(directory=str(DIST)))


@app.get("/", response_class=HTMLResponse)
async def get_root() -> HTMLResponse:
    async with aiofiles.open(INDEX, mode="r") as f:
        content = await f.read()

    return HTMLResponse(content)


@app.get("/test")
async def test() -> Dict:
    return {"foo": f"A python-generated uuid: {uuid4()}"}


app.websocket("/ws")(ws_routes.websocket_endpoint)


async def serve() -> None:
    server = uvicorn.Server(
        config=uvicorn.Config(app=app, port=8000, log_level="debug")
    )
    await server.serve()


if __name__ == "__main__":
    asyncio.run(serve())
