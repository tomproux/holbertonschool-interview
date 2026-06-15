#!/usr/bin/python3
"""Solve the N queens puzzle."""

import sys


def solve_nqueens(n):
    """Return all solutions for an n x n board."""
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if col in cols or row + col in pos_diag or row - col in neg_diag:
                continue

            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            board[row] = col

            backtrack(row + 1)

            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    backtrack(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in solve_nqueens(n):
        print(solution)
