class PlayerState:
    sight = 'right'

    up: bool = False
    down: bool = False
    left: bool = False
    right: bool = False

    async def x(self):
        if self.left and self.right:
            return 0
        elif self.left:
            return -5
        elif self.right:
            return 5
        else:
            return 0

    async def y(self):
        if self.up and self.down:
            return 0
        elif self.up:
            return 5
        elif self.down:
            return -5
        else:
            return 0

    # async def handle_event(self, value: str):
    #     parts = value.split("_")
    #
    #     action_str = parts[0]
    #     pressed: bool
    #     if action_str == "start":
    #         pressed = True
    #     elif action_str == "stop":
    #         pressed = False
    #     else:
    #         return
    #
    #     direction_str = parts[1]
    #     if direction_str == "left":
    #         self.left = pressed
    #     elif direction_str == "right":
    #         self.right = pressed
    #     elif direction_str == "up":
    #         self.up = pressed
    #     elif direction_str == "down":
    #         self.down = pressed
    #
    #     self.sight = direction_str
