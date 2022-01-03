#!/usr/bin/python3
"""Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """rotate algorithm"""
    N = len(matrix)

    if (N < 2):
        exit

    for x in range(0, int(N / 2)):
        for y in range(0, N - x - 1):
            tmp = matrix[x][y]

            matrix[x][y] = matrix[N-1-y][x]
            matrix[N-1-y][x] = matrix[N-1-x][N-1-y]
            matrix[N-1-x][N-1-y] = matrix[y][N-1-x]
            matrix[y][N-1-x] = tmp
