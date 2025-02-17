class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """

    def __init__(self, width, height):
        """
        Create grid `array` width by height. Create a Grid object with
        a width, height, and array. Initially all locations hold None.
        >>> grid = Grid(2, 2)
        >>> grid.array
        [[None, None], [None, None]]
        """
        self.width = int(width)
        self.height = int(height)
        self.array = []

        i = 0
        while i < self.height:
            n = 0
            grid_list = []
            while n < self.width:
                grid_list.append(None)
                n += 1
            self.array.append(grid_list)
            i += 1


    def get(self, x, y):
        """
        Gets the value stored value at (x, y).
        (x, y) should be in bounds.
        >>> grid = Grid(2, 2)
        >>> grid.array = [[1, 2], [4, 5]]
        >>> grid.get(0, 1)
        4
        >>> grid.get(1, 0)
        2
        """
        return self.array[y][x]

    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        >>> grid = Grid(2, 2)
        >>> grid.set(1, 1, "Milk")
        >>> grid.set(1, 0, "Dud")
        >>> grid.array
        [[None, 'Dud'], [None, 'Milk']]
        """
        self.array[y][x] = val

    def __str__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"


    def __repr__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        return self.array == other.array
