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
            board[pos] = 'M'
            mine_count += 1
            #print("Board x: {x} and y: {y} = {mine}".
            #        format(x = x, y = y , mine = board[key]))
    return board

def get_mine_counts(board, board_width, board_height):
    board2 = board.copy()
    for pos, value in board.items():
        #print("pos: {pos} and value: {value}".
        #        format(pos = pos, value = value))
        if value == "M":
            x, y = pos.split(',')
            #print("x: {x}, y: {y}".format(x = x, y = y))
            for i in range(int(x) - 1, int(x) + 2):
                if i >= 0:
                    for j in range(int(y) - 1, int(y) + 2):
                        if j >= 0:
                            current = str(i) + ',' + str(j)
                            if board.get(current) != None:
                                if board[current] == "M":
                                    board2[current] = "M"
                            if board2.get(current) == None:
                                board2[current] = 1
                            elif board2[current] == "M":
                                pass
                            else:
                                board2[current] += 1
    return board2

def init_visible(board, visible, board_width, board_height):
    i = 0
    while (i < board_width):
        j = 0
        while (j < board_height):
            pos = str(i) + ',' + str(j)
            visible[pos] = 'N'
            j += 1
        i += 1
    count = 1
    while (count == 1):
        i = random.randint(0, board_width - 1)
        j = random.randint(0, board_height - 1)
        pos = str(i) + ',' + str(j)
        if (board.get(pos) != None) & (board[pos] != 'M'):
            visible[pos] = 1
            count = 0
    return visible

def print_board(board, visible, board_width, board_height):
    i = 0
    while (i < board_width):
        j = 0
        while (j < board_height):
            pos = str(i) + ',' + str(j)
            if visible[pos] == 'Y':
                if board.get(pos) != None:
                    print(board[pos], end = " ")
                else:
                    print("0", end = " ")
            elif visible[pos] == 'F':
                print("F", end = " ")
            else:
                print("X", end = " ")
            j += 1
        print("\n", end = "")
        i += 1

board = {}
visible = {}
board = get_mine_positions(board, 5, 5, 5)
board = get_mine_counts(board, 5, 5)
visible = init_visible(board, visible, 5, 5)
print("------------------------------------")
print_board(board, visible, 5, 5)
print("------------------------------------")
#for x in range(0, board_width):
#    for y in range(0,board_height):
#        pos = str(x) + ',' + str(y)
#        if (board.get(pos) != None):
#            if (board[pos] == "M"):
#                print("Mine in: x:{x} y:{y}".format(x = x, y = y))
#            else:
#                print("Number of mines close to {pos}: {num}".
#                        format(pos = pos, num = board[pos]))
