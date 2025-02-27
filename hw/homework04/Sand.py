from Particle import Particle


class Sand(Particle):

    def is_move_ok(self, x, y):
        if self.grid.in_bounds(x, y) and self.grid.in_bounds(x, y - 1):
            print(f"primer if: {self.grid.get(x, y)} , {self.grid.get(x, y - 1)}")
            if self.grid.get(x, y) is None and self.grid.get(x, y - 1) == self:
                return True
            elif self.grid.get(x, y) is None and self.grid.get(x, y - 1) is None:
                return True
        return False

    def physics(self):
        if self.is_move_ok(self.x, self.y + 1):
            return self.x, self.y + 1
        elif self.is_move_ok(self.x - 1, self.y + 1):
            return self.x - 1, self.y + 1
        elif self.is_move_ok(self.x + 1, self.y + 1):
            return self.x + 1, self.y + 1
        return None
