from fastapi import APIRouter
from fastapi_utils.cbv import cbv
from starlette.websockets import WebSocket

from megagame.GameService import game_service

router = APIRouter()


@cbv(router)
class WebSocketEndpointHandler:

    @router.websocket("/ws/{client_id}")
    async def websocket_endpoint(self, websocket: WebSocket, client_id: int):
        await game_service.add_player(client_id=client_id, websocket=websocket)
