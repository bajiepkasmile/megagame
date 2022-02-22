from megagame.model.playerstate import PlayerState
from megagame.model.projectile import Projectile


class Player:
    x: int = 200
    y: int = 200

    def __init__(self, client_id: int):
        self.state = PlayerState()
        self.client_id = client_id
        self.projectiles = []

    def __str__(self):
        projs_str = [str(projectile) for projectile in self.projectiles]
        return '\n'.join([f"Player {self.client_id} {self.x} {self.y}", *projs_str])

    async def on_tik(self):
        self.x += await self.state.x()
        self.y += await self.state.y()
        for projectile in self.projectiles:
            projectile.on_tik()

    def set_state(self, attr, value):
        self.state.__setattr__(attr, value)

    def set_sight(self, value):
        self.state.sight = value

    def add_projectile(self):
        self.projectiles.append(Projectile(self.x, self.y, self.state.sight))
