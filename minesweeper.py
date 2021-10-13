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
        pos = str(x) + ',' + str(y)
        if board.get(pos) == None:
            board[pos] = 'MINE'
            mine_count += 1
            #print("Board x: {x} and y: {y} = {mine}".format(x = x, y = y , mine = board[key]))
    return board

def get_mine_counts(board, board_width, board_height):
    board2 = board.copy()
    for pos, value in board.items():
        print("pos: {pos} and value: {value}".format(pos = pos, value = value))
        if value == "MINE":
            x, y = pos.split(',')
            print("x: {x}, y: {y}".format(x = x, y = y))
            for i in range(int(x) - 1, int(x) + 2):
                if i >= 0:
                    for j in range(int(y) - 1, int(y) + 2):
                        if j >= 0:
                            current = str(i) + ',' + str(j)
                            print("current: {0}".format(current))
                            if board.get(current) != None:
                                if board[current] == "MINE":
                                    board2[current] = "MINE"
                            if board2.get(current) == None:
                                board2[current] = 1
                            elif board2[current] == "MINE":
                                pass
                            else:
                                board2[current] += 1
    return board2
                     

board = {}
board = get_mine_positions(board, 5, 5, 5)
board = get_mine_counts(board, 5, 5)
print("------------------------------------")
for x in range(0, board_width):
    for y in range(0,board_height):
        pos = str(x) + ',' + str(y)
        if (board.get(pos) != None):
            if (board[pos] == "MINE"):
                print("Mine in: x:{x} y:{y}".format(x = x, y = y))
            else:
                print("Number of mines close to {pos}: {num}".format(pos = pos, num = board[pos])) 
