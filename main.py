import random
from pprint import pprint
from time import sleep

from cell import Cell

COLS = 5
ROWS = 5


def update(board):
    """ Updates every cell in board """
    for col in board:
        for cell in col:
            cell.update()


if __name__ == '__main__':
    BOARD = [[None for y in range(COLS)] for x in range(ROWS)]
    for y in range(COLS):
        for x in range(ROWS):
            BOARD[x][y] = Cell(x, y, BOARD, random.randint(0, 1))

    while True:
        pprint(BOARD)
        print()
        update(BOARD)
        sleep(.2)
