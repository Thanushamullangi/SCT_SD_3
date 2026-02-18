def print_board(board):
    for row in board:
        print(row)

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    row, col = pos

    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True

    row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


board = []

print("Enter the Sudoku row by row (use 0 for empty cells)")

for i in range(9):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    board.append(row)


if solve(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("No solution exists.")
