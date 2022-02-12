from fastapi import WebSocket

from model.speed import Speed


class Player:
    x: int = 200
    y: int = 200

    def __init__(self, id: int, websocket: WebSocket) -> None:
        self.speed = Speed()
        self.id = id
        self.websocket = websocket

    async def work(self):
        while True:
            data = await self.websocket.receive_text()
            await self.speed.handle_event(data)

    async def on_tik(self):
        self.x += await self.speed.x()
        self.y += await self.speed.y()

    def string(self):
        return f"{self.x} {self.y}"
