class Projectile:
    speed = 5
    direction_calculation = {'up': ('y', 5), 'down': ('y', -5), 'right': ('x', 5), 'left': ('x', -5)}

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.calc_tuple = self.direction_calculation[direction]

    def __str__(self):
        return f"Projectile {self.x} {self.y}"

    def on_tik(self):
        self.__dict__[self.calc_tuple[0]] += self.calc_tuple[1]



