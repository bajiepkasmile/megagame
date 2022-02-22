from typing import Dict

from starlette.websockets import WebSocketDisconnect

from megagame.ConnectionManager import ConnectionManager
from megagame.model.player import Player


class World:
    players: Dict[int, Player] = {}
    _manager: ConnectionManager

    def __init__(self, manager):
        self._manager = manager

    def __str__(self):
        return '\n'.join([str(player) for player in self.players.values()])

    def add(self, client_id, player):
        self.players[client_id] = player

    async def remove(self, client_id: int):
        self.players.pop(client_id)

    async def redraw_and_send(self, count):
        for i in range(count):
            await self.on_redraw()
        await self.send_state_to_clients()

    async def send_state_to_clients(self):
        await self._manager.broadcast(str(self))

    async def on_redraw(self):
        for player in self.players.values():
            await player.on_tik()
