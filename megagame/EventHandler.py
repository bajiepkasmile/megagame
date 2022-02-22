DELIMETER = ' '


class Action:
    def __init__(self, player):
        self._player = player

    def handle(self):
        raise NotImplemented


class MoveAction(Action):
    ACTIONS = {'start': True, 'stop': False}
    is_pressed = None
    direction_str = None

    def __init__(self, player, args):
        super().__init__(player=player)
        self.args = args

    def parse_arguments(self):
        self.direction_str = self.args[0]
        self.is_pressed = self.ACTIONS.get(self.args[1])

    def handle(self):
        self.parse_arguments()
        self._player.set_state(self.direction_str, self.is_pressed)
        if self.is_pressed:
            self._player.set_sight(self.direction_str)


class AttackAction(Action):
    def __init__(self, player, args):
        super().__init__(player=player)
        self.args = args

    def handle(self):
        self._player.add_projectile()



class EventHandler:
    action_types = {'Move': MoveAction, 'Attack': AttackAction}

    def __init__(self, player):
        self._player = player

    async def handle_event(self, data):
        parts = data.split(DELIMETER)

        if not (action := self.action_types.get(parts[0])):
            raise Exception  # TODO change exception type
        action(self._player, parts[1:]).handle()
