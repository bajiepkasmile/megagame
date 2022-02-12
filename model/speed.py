class Speed:

    _up: bool = False
    _down: bool = False
    _left: bool = False
    _right: bool = False

    async def x(self):
        if self._up and self._down:
            return 0
        elif self._up:
            return -5
        elif self._down:
            return 5
        else:
            return 0

    async def y(self):
        if self._left and self._right:
            return 0
        elif self._left:
            return -5
        elif self._right:
            return 5
        else:
            return 0

    async def handle_event(self, value: str):
        parts = value.split("_") # example: start_left stop_left

        action_str = parts[0]
        pressed: bool
        if action_str == "start":
            pressed = True
        elif action_str == "stop":
            pressed = False
        else:
            return

        direction_str = parts[1]
        if direction_str == "left":
            self._left = pressed
        elif direction_str == "right":
            self._right = pressed
        elif direction_str == "up":
            self._up = pressed
        elif direction_str == "down":
            self._down = pressed
