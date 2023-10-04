def is_safe(board, row, col):
    # Check if it's safe to place a queen at board[row][col]
    # Check the left side of this row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check lower diagonal on the left side
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solve_n_queens(board, col):
    # Base case: If all queens are placed, return True
    for row in board:
        print(' '.join(['Q' if x == 1 else '.' for x in row]))
    print()
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False

N = int(input()) # Change N to solve for a different N-Queens problem
board = [[0] * N for _ in range(N)]
if solve_n_queens(board, 0):
    print("Solution exists:")
    for row in board:
        print(' '.join(['Q' if x == 1 else '.' for x in row]))
else:
    print("No solution exists.")