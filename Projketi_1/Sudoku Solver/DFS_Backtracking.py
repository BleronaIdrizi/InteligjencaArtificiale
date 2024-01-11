def is_valid(board, row, col, num):
    # Kontrollon nëse numri është i ligjshëm në rreshtin, kolonën dhe katroren 3x3
    for x in range(9):
        # Kontrollon rreshtin, kolonën dhe katroren 3x3
        if board[row][x] == num or board[x][col] == num or board[3 * (row // 3) + x // 3][3 * (col // 3) + x % 3] == num:
            return False
    return True

def solve_sudoku_dfs(board):
    # Përpjeket të zgjidhë Sudoku-n përmes Depth First Search dhe Backtracking
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # Kontrollon nëse qelia është e zbrazët - backtracking
                for num in range(1, 10):  # Provon çdo numër nga 1 deri në 9
                    if is_valid(board, i, j, num):  # Kontrollon nëse numri është i ligjshëm
                        board[i][j] = num  # Vendos numrin në qeli
                        if solve_sudoku_dfs(board):  # Thirrje rekursive për të zgjidhur pjesën tjetër
                            return True  # Zgjidhja u gjet
                        board[i][j] = 0  # Backtracking nëse zgjidhja nuk u gjet
                return False  # Kthehet False nëse asnjë numër nuk është i ligjshëm
    return True  # Të gjitha qelitë janë të mbushura, zgjidhja u gjet

def print_sudoku_formatted(board):
    # Printon tabelën e Sudoku-s në një format të lexueshëm
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")  # Shtyp vija për të ndarë katrorët 3x3
        
        row_formatted = ""
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_formatted += " | "  # Shtyp një ndarës midis katrorëve 3x3
            row_formatted += str(num) if num != 0 else "."  # Shtyp numrin ose një pikë nëse qelia është e zbrazët
            row_formatted += " "
        print(row_formatted)  # Printon rreshtin e formatuar

# Tabela fillestare e Sudoku-s për tu zgjidhur
sudoku_board_dfs = [
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

# Printimi i mesazhit të detyrës
print(" \n************* Zgjidhja e Sudoku-s me Depth First Search (DFS) dhe Backtracking ************* \n")

# Printon tabelën e pazgjidhur të Sudoku-s
print(" ------------- Sudoku i pazgjidhur ------------- \n")
print_sudoku_formatted(sudoku_board_dfs)

# Zgjidh Sudoku-n dhe printo rezultatin
solved = solve_sudoku_dfs(sudoku_board_dfs)
if solved:
    # Printon tabelën e zgjidhur nëse zgjidhja u gjet
    print("\n ------------- Sudoku i zgjidhur -------------\n")
    print_sudoku_formatted(sudoku_board_dfs)
else:
    # Printon një mesazh nëse nuk ka zgjidhje
    print("Nuk ka zgjidhje.")