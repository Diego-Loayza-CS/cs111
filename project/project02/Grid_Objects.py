from Particle import Particle
import random


class Sand(Particle):

    def is_move_ok(self, x, y):
        if self.grid.in_bounds(x, y) and self.grid.in_bounds(x, y - 1):
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


class Rock(Particle):

    @staticmethod
    def physics():
        return None


class Bubble(Particle):

    def is_move_ok(self, x, y):
        if self.grid.in_bounds(x, y) and self.grid.in_bounds(x, y + 1):
            if self.grid.get(x, y) is None and self.grid.get(x, y + 1) == self:
                return True
            elif self.grid.get(x, y) is None and self.grid.get(x, y + 1) is None:
                return True
        return False

    def physics(self):

        # IMPORTANT: ONLY SELECT ONE TYPE OF PHYSICS

        ## CORRECT FOR PROJECT
        # if self.is_move_ok(self.x, self.y - 1):
        #     return self.x, self.y - 1
        # elif self.is_move_ok(self.x + 1, self.y - 1):
        #     return self.x + 1, self.y - 1
        # elif self.is_move_ok(self.x - 1, self.y - 1):
        #     return self.x - 1, self.y - 1
        # return None

        ## IMPLEMENTATION OF "GOING FURTHER"
        rand_num = random.randrange(0, 300)
        if rand_num < 30:  # 30% chance
            if self.is_move_ok(self.x + 1, self.y):
                return self.x + 1, self.y
        if rand_num < 45:  # 15% chance
            if self.is_move_ok(self.x + 1, self.y - 1):
                return self.x + 1, self.y - 1
        if rand_num < 55:  # 10% chance
            if self.is_move_ok(self.x, self.y - 1):
                return self.x, self.y - 1
        if rand_num < 70:   # 15% chance
            if self.is_move_ok(self.x - 1, self.y - 1):
                return self.x - 1, self.y - 1
        if 70 <= rand_num < 100:  # 30% chance
            if self.is_move_ok(self.x - 1, self.y):
                return self.x - 1, self.y
            elif self.is_move_ok(self.x - 1, self.y - 1):
                return self.x - 1, self.y - 1
            elif self.is_move_ok(self.x, self.y - 1):
                return self.x, self.y - 1
            elif self.is_move_ok(self.x + 1, self.y - 1):
                return self.x + 1, self.y - 1
            elif self.is_move_ok(self.x + 1, self.y):
                return self.x + 1, self.y
        return None


