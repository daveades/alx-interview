#!/usr/bin/python3

import sys


def validate_input():
    """
    Validate command line arguments for N-Queens problem

    Checks:
    - Exactly one argument is provided
    - Argument is an integer
    - integer is >=4

    Returns:
    int: validated board size
    """

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

    return n


def is_safe(board, row, col):
    """
    check if a queen can be placed on board at the given position.


    Args:
    board(list): current board configuration
    row(int): Row to place queen
    col(int): Column to place queen

    Returns:
    bool: True if placement is safe, False otherwise
    """
    for prev_col in range(col):
        # check row conflict
        if board[prev_col] == row:
            return False

        if abs(board[prev_col] - row) == abs(prev_col - col):
            return False

    return True


def backtrack(col, n, board, solutions):
    """
    Recursively solve the N-Queens problem by placing queens on the board.

    Systematically tries to place queens in each column while ensuring
    no queens attack each other. Uses backtracking to explore all
    possible configurations.

    Args:
    col (int): Current column being processed in the backtracking algorithm.
    """
    # Base case: all queens placed
    if col == n:
        # convert solution to list of [row, col] coordinates
        solution = [[r, c] for c, r in enumerate(board)]
        solutions.append(solution)
        return
    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            backtrack(col + 1, n, board, solutions)
            board[col] = -1


def solve_n_queens(n):
    """
    Solve the N-Queens problem and return all possible solutions:


    Args:
    n(int): Board size


    Returns:
    list: List of all possible solutions
    """

    solutions = []
    board = [-1] * n

    backtrack(0, n, board, solutions)
    return solutions


def print_solutions(solutions):
    """
    print all solutions in the tequired format


    Args:
    solutions(list): List of solutions where each solution
            is a list of [row, col] coordinates
    """

    for solution in solutions:
        print(solution)


def main():
    """
    Main function to orchestrate N-Queens solution process
    """

    n = validate_input()
    solutions = solve_n_queens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
