def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_valid_move(grid, num, row, col):
    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check 3x3 subgrid
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True  # The Sudoku puzzle is solved

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(grid, num, row, col):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True  # Successfully solved

            grid[row][col] = 0  # Backtrack

    return False  # No solution found

def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None  # All cells are filled

if __name__ == "__main__":
    unsolved_sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(unsolved_sudoku):
        print("Solved Sudoku:")
        print_sudoku(unsolved_sudoku)
    else:
        print("No solution exists.")
