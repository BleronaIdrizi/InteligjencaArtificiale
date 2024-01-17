from constraint import Problem, AllDifferentConstraint

def sudoku_solver(grid):
    # Create a new constraint problem
    problem = Problem()

    # Variables: (row, column) pairs
    variables = [(row, col) for row in range(9) for col in range(9)]

    # Set domain for each variable
    for variable in variables:
        row, col = variable
        if grid[row][col] == 0:
            problem.addVariable(variable, range(1, 10))
        else:
            problem.addVariable(variable, [grid[row][col]])

    # Add row and column constraints
    for i in range(9):
        problem.addConstraint(AllDifferentConstraint(), [(i, col) for col in range(9)])
        problem.addConstraint(AllDifferentConstraint(), [(row, i) for row in range(9)])

    # Add 3x3 grid constraints
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            problem.addConstraint(AllDifferentConstraint(), [(row + i, col + j) for i in range(3) for j in range(3)])

    # Solve the problem
    solution = problem.getSolutions()

    # Return the first solution (if any)
    return solution[0] if solution else None

# Example Sudoku grid (0 represents empty cells)
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# Solve the puzzle
solution = sudoku_solver(grid)

# Print the solution
if solution:
    for row in range(9):
        print([solution[(row, col)] for col in range(9)])
else:
    print("No solution found")
