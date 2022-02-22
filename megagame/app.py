import asyncio

from fastapi import APIRouter, FastAPI
from starlette.websockets import WebSocket

from megagame.ConnectionManager import manager
from megagame.GameService import game_service
from megagame.api import root_endpoint, websocket_endpoit
from megagame.model.player import Player
from megagame.model.world import World


def create_router() -> APIRouter:
    root_api_router = APIRouter()

    root_api_router.include_router(router=root_endpoint.router, prefix='', tags=[])
    root_api_router.include_router(router=websocket_endpoit.router, prefix='', tags=[])
    return root_api_router


def create_api(router: APIRouter) -> FastAPI:
    _app = FastAPI()

    if router:
        _app.include_router(router=router)

    return _app


def create_app() -> FastAPI:
    app = create_api(router=create_router())

    @app.on_event("startup")
    async def init_game():
        asyncio.create_task(game_service.init_game())

    return app
