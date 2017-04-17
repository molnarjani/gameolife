class Cell:
    """
    Individual cell in a board,
    manages it's life conditions based on neighbours
    """

    def __init__(self, x, y, board, alive=False):
        self.x = x
        self.y = y
        self.board = board
        self.alive = alive

    def __repr__(self):
        return 'X' if self.alive else ' '

    @property
    def neighbours(self):
        """
        (x-1, y-1) | (x-1, y) | (x-1, y+1)
        ----------------------------------
        (x,   y-1) | (x,   y) | (x,   y+1)
        ----------------------------------
        (x+1, y-1) | (x+1, y) | (x+1, y+1)
        """
        neighbours = []
        neighbour_indeces = [
            (self.x - 1, self.y - 1),
            (self.x - 1, self.y),
            (self.x - 1, self.y + 1),
            (self.x, self.y - 1),
            (self.x, self.y + 1),
            (self.x + 1, self.y - 1),
            (self.x + 1, self.y),
            (self.x + 1, self.y + 1),
        ]

        # for each index we try to get cell from the board,
        # if it exist we append it to neighbors
        # -1 is a valid index, but we need to exclude them from our list
        for x, y in neighbour_indeces:
            if x > -1 and y > -1:
                try:
                    neighbours.append(self.board[x][y])
                except IndexError:
                    pass

        return sum(1 for cell in neighbours if cell.alive)

    def update(self):
        # cell dies if it has less than 2 or more than 3 neighbours
        if self.alive and self.neighbours not in (2, 3):
            self.alive = False

        # dead cells with 3 neigbours resurrect for some reason
        if not self.alive and self.neighbours == 3:
            self.alive = True
