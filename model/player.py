from fastapi import WebSocket

from model.speed import Speed
from model.world import World


class Player:

    websocket: WebSocket
    speed = Speed()
    x: int = 0
    y: int = 0

    def __init__(self, websocket: WebSocket) -> None:
        super().__init__()
        self.websocket = websocket
        await websocket.accept()
        while True:
            self.speed.handle_event(await websocket.receive_text())

    def on_tik(self):
        self.x += self.speed.x()
        self.y += self.speed.y()

    def on_redraw(self, world: World):
        await self.websocket.send_text(world.string())

    def string(self):
        return f"${self.x} ${self.y}"
