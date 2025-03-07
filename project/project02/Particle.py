class Particle:
    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.x = x
        self.y = y

    def __str__(self):
        return f"{type(self).__name__}({self.x},{self.y})"

    def move(self):
        physics = self.physics()
        if physics is None:
            return
        self.grid.set(self.x, self.y, None)
        self.x, self.y = physics
        self.grid.set(self.x, self.y, self)