rules = """
Tic Tac Toe is a 2-player game played on a 3x3 grid.

Use coordinates (row, column) to place your move. Rows and columns go from 1 to 3.

Board with coordinates:

  A,1 |  A,2  | A,3
------|-------|------
  B,1 |  B,2  | B,3
------|-------|------
 C,1  |  C,2  | C,3

Example: to place in the top-right corner, choose A,3.

Players take turns placing X and O. The goal is to get 3 in a row horizontally, vertically, or diagonally.

First to 3 in a row wins. If all spaces are filled and no one wins, it's a tie.

Grab a friend and play together!
"""
print(rules)

circle = '⭕'
cross = '❌'

board = [
    ["A,1", "A,2", "A,3"],
    ["B,1", "B,2", "B,3"],
    ["C,1", "C,2", "C,3"]
]

import copy

def board_full(board):
    for row in board:
        for cell in row:
            if cell != cross and cell != circle:
                return False
    return True


def check(board, x, y):
    return board[x][y] != cross and board[x][y] != circle


def winner(board):

    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2]:
            if board[r][0] in (cross, circle):
                return True
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c]:
            if board[0][c] in (cross, circle):
                return True

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] in (cross, circle):
            return True

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] in (cross, circle):
            return True

    return False


def bot():

    for r in range(3):
        for c in range(3):
            if check(board, r, c):

                board[r][c] = circle
                if winner(board):
                    return r, c
                board[r][c] = f"{'ABC'[r]},{c+1}"

    for r in range(3):
        for c in range(3):
            if check(board, r, c):

                board[r][c] = cross
                if winner(board):
                    board[r][c] = circle
                    return r, c
                board[r][c] = f"{'ABC'[r]},{c+1}"

    for r in range(3):
        for c in range(3):
            if check(board, r, c):
                return r, c


def make_board():
    print()
    print("   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("  -----|-----|-----")
    print("   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("  -----|-----|-----")
    print("   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print()


make_board()

for i in range(1, 10):

    while True:
        x = input("Player 1 (❌) enter row,col (e.g. C,3): ").upper()

        if len(x) >= 3 and x[0] in 'ABC' and x[2] in '123':

            if x[0] == 'A':
                r = 0
            elif x[0] == 'B':
                r = 1
            else:
                r = 2

            c = int(x[2]) - 1

            if check(board, r, c):
                board[r][c] = cross
                break
            else:
                print("ERROR. Spot already taken.")
        else:
            print("ERROR. Please enter again.")

    make_board()

    if winner(board):
        print("Congrats you won!")
        break

    if board_full(board):
        print("It's a tie!")
        break

    r, c = bot()
    board[r][c] = circle

    make_board()

    if winner(board):
        print("I won!")
        break