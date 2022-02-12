import asyncio
from typing import List

from ConnectionManager import ConnectionManager
from model.player import Player
import time


class World:
    players: List[Player] = []
    _manager: ConnectionManager
    test = False

    def __init__(self, manager):
        self._manager = manager

    async def start_game(self):
        start_time = time.time()
        while True:
            current_time = time.time()
            delta_time = current_time - start_time
            # if delta_time < 1:
            #     continue

            start_time = current_time #TODO: future feature
            count = int(delta_time / 10)
            start_time -= delta_time % 100

            await asyncio.sleep(0.1) # stub
            await self.on_redraw()
            await self.send_state_to_clients()

    def string(self): #TODO: change to oneliner
        world_str = ""
        for player in self.players:
            world_str += f"{player.string()}\n"
        return world_str

    async def add_player(self, player: Player):
        await self._manager.connect(websocket=player.websocket)
        self.players.append(player)
        await player.work()

    async def send_state_to_clients(self):
        await self._manager.broadcast(self.string())

    async def on_redraw(self):
        for player in self.players:
            await player.on_tik()
