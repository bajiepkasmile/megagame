import asyncio

from starlette.websockets import WebSocketDisconnect

from megagame.ConnectionManager import manager
from megagame.EventHandler import EventHandler
from megagame.model.player import Player
from megagame.model.tiker import Tiker
from megagame.model.world import World


class GameService:
    _world = None

    async def init_game(self):
        self._world = World(manager=manager)
        asyncio.create_task(Tiker().start(self._world.redraw_and_send))

    async def add_player(self, client_id, websocket):
        await manager.connect(websocket=websocket)
        player = Player(client_id=client_id)
        self._world.add(client_id, player)

        ev = EventHandler(player)
        try:
            while True:
                data = await websocket.receive_text()
                await ev.handle_event(data)
        except WebSocketDisconnect:
            await self._world.remove(client_id)
            manager.disconnect(websocket)
            await manager.broadcast(f"Player #{client_id} left the chat")


game_service = GameService()
