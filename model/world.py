from model.player import Player
import time


class World:
    players: list

    def __init__(self) -> None:
        super().__init__()
        start_time = time.time()
        while True:
            current_time = time.time()
            delta_time = current_time - start_time
            if delta_time < 16:
                continue

            start_time = current_time
            count = int(delta_time / 16)

            for player in self.players:
                for i in range(0, count):
                    player.on_tik(self)
                player.on_redraw(self)

    def string(self):
        world_str = ""
        for player in self.players:
            world_str = f"${player.string()}\n"
        return world_str

    def add_player(self, player: Player):
        self.players.insert(0, player)
