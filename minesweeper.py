# minesweeper
import random

# Create board
board_width = 5
board_height = 5
num_mines = 5

def get_mine_positions(board, board_width, board_height, num_mines):
    mine_count = 0
    while (mine_count < num_mines):
        x = random.randint(0, board_width - 1)
        y = random.randint(0, board_height -1)
        key = str(x) + str(y)
        if board.get(key) == None:
            board[key] = 'MINE'
            mine_count += 1
            print("Board x: {x} and y: {y} = {mine}".format(x = x, y = y , mine = board[key]))
    return board

board = {}
board = get_mine_positions(board, 5, 5, 5)
for x in range(0, board_width):
    for y in range(0,board_height):
        if (board.get(str(x) + str(y)) != None):
            print("Mine in: x:{x} y:{y}".format(x = x, y = y))
