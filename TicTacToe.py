rules = """
Tic Tac Toe is a 2-player game played on a 3x3 grid.

Use coordinates (row, column) to place your move. Rows and columns go from 1 to 3.

Board with coordinates:

  1,1 |  1,2  | 1,3
------|-------|------
  2,1 |  2,2  | 2,3
------|-------|------
 3,1  |  3,2  | 3,3

Example: to place in the top-right corner, choose (1,3).

Players take turns placing X and O. The goal is to get 3 in a row horizontally, vertically, or diagonally.

First to 3 in a row wins. If all spaces are filled and no one wins, it's a tie.

Grab a friend and play together!
"""

circle = '⭕'
cross = '❌'

board = [
    ["1,1", "1,2", "1,3"],
    ["2,1", "2,2", "2,3"],
    ["3,1", "3,2", "3,3"]
]

def check(board, x, y):
    if board[x][y] == circle or board[x][y] == cross:
        return False
    return True

def winner():
    if len(set(board[0])) <= 1:
        return True
    elif len(set(board[1])) <= 1:
        return True 
    elif len(set(board[2])) <= 1:
        return True
    elif board[0][0] == board [1][0] == board[2][0]:
        return True
    elif board[0][1] == board [1][1] == board[2][1]:
        return True
    elif board[0][0] == board [1][0] == board[2][0]:
        return True
    elif board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        return True
    else:
        return False
def make_board():
    print()
    print("   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("  -----|-----|-----")
    print("   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("  -----|-----|-----")
    print("   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print()


for i in range(1, 10):

    while True:
        x = input("Player 1 (❌) enter row,col (e.g. 1,3): ")

        if len(x) >= 3 and x[0] in '123' and x[2] in '123':
            r = int(x[0]) - 1
            c = int(x[2]) - 1

            if check(board, r, c):
                board[r][c] = cross
                break
            else:
                print("ERROR. Spot already taken.")
        else:
            print("ERROR. Please enter again.")

    make_board()
    if winner() == True:
        print("Player 1 one!")
        break

    while True:
        o = input("Player 2 (⭕) enter row,col (e.g. 1,3): ")

        if len(o) >= 3 and o[0] in '123' and o[2] in '123':
            r = int(o[0]) - 1
            c = int(o[2]) - 1

            if check(board, r, c):
                board[r][c] = circle
                break
            else:
                print("ERROR. Spot already taken.")
        else:
            print("ERROR. Please enter again.")

    make_board()
    make_board()
    if winner() == True:
        print("Player 2 one!")
        break
