#!/usr/bin/python3
"""
Nqueens challenge module
"""

import sys


def print_board(board: list):
    """display full board"""
    for b in board:
        print(b)


def set_up_board(board: list, n: int, forbidden_boxes: list):
    """set all chessboard diagonals to 1"""
    for i in range(n):
        board[i][i] = 1
        board[i][n-i-1] = 1
        forbidden_boxes.append([i, i])
        forbidden_boxes.append([i, n-i-1])


def set_forbidden_boxes(board: list, h: int, v: int, n: int):
    # set forbidden boxes
    tmp_h = h
    tmp_v = v

    #### set forbidden frontal boxes ####

    # up
    while tmp_v + 1 < n:
        if board[tmp_h][tmp_v+1] == 0:
            print("frontal frobidden set front")
            board[tmp_h][tmp_v+1] = 1
        tmp_v += 1
    tmp_v = v

    # right
    while tmp_h + 1 < n:
        if board[tmp_h+1][tmp_v] == 0:
            print("frontal frobidden set right: ",
                  [tmp_h+1, tmp_v])
            board[tmp_h+1][tmp_v] = 1
        tmp_h += 1

    tmp_h = h

    # down
    while tmp_v - 1 >= 0:
        if board[tmp_h][tmp_v-1] == 0:
            print("frontal frobidden set down")
            board[tmp_h][tmp_v-1] = 1
        tmp_v -= 1
    tmp_v = v

    # left
    while tmp_h - 1 >= 0:
        if board[tmp_h-1][tmp_v] == 0:
            print("frontal frobidden set right: ",
                  [tmp_h-1, tmp_v])
            board[tmp_h-1][tmp_v] = 1
        tmp_h -= 1
    tmp_h = h

    #### set forbidden diagonals boxes ####

    # right diagonal down
    while tmp_h + 1 < n and tmp_v + 1 < n:
        print("diagonal right: ", board[tmp_h+1][tmp_v+1])
        if board[tmp_h+1][tmp_v+1] == 0:
            board[tmp_h+1][tmp_v+1] = 1
        tmp_h += 1
        tmp_v += 1
    tmp_h = h
    tmp_v = v

    # right diagonal up
    while tmp_h - 1 >= 0 and tmp_v + 1 < n:
        if board[tmp_h-1][tmp_v+1] == 0:
            board[tmp_h-1][tmp_v+1] = 1
        tmp_h -= 1
        tmp_v += 1
    tmp_h = h
    tmp_v = v

    # left diagonal down
    while tmp_h + 1 < n and tmp_v - 1 >= 0:
        print("diagonal left: ", board[tmp_h+1][tmp_v-1])
        if board[tmp_h+1][tmp_v-1] == 0:
            board[tmp_h+1][tmp_v-1] = 1
        tmp_h += 1
        tmp_v -= 1
    tmp_h = h
    tmp_v = v

    # left diagonal up
    while tmp_h - 1 >= 0 and tmp_v - 1 >= 0:
        if board[tmp_h-1][tmp_v-1] == 0:
            board[tmp_h-1][tmp_v-1] = 1
        tmp_h -= 1
        tmp_v -= 1
    tmp_h = h
    tmp_v = v


def main():
    """This function solve the challenge of placing
    N non-attacking queens on an N×N chessboard"""

    if (len(sys.argv) != 2):
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")

    elif (int(sys.argv[1]) < 4):
        print("N must be at least 4")
        exit(1)

    n = int(sys.argv[1])
    board = [[0 for i in range(n)] for j in range(n)]

    forbidden_boxes = []
    set_up_board(board, n, forbidden_boxes)

    print_board(board)
    print("--------------------------------")

    for h in range(n):
        v = 0
        for v in range(n):
            if board[h][v] == 0:
                # set geometrical queens
                print("add queen: ", [h, v])
                board[h][v] = 9
                if board[n-h-1][n-v-1] == 0:
                    print("add queen: ", [n-1-h, n-1-v])
                    board[n-h-1][n-v-1] = 9

                opp_h = n-h-1
                opp_v = n-v-1
                set_forbidden_boxes(board, h, v, n)
                set_forbidden_boxes(board, opp_h, opp_v, n)

                print_board(board)
                print("------------------------")


if __name__ == "__main__":
    main()
