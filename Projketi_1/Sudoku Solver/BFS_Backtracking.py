from collections import deque

def is_valid(board, row, col, num):
    # Kontrollon nëse vendosja e numrit 'num' në qelinë e dhënë (row, col) është e ligjshme.
    # Kjo bëhet duke kontrolluar nëse numri tashmë ekziston në të njëjtin rresht, kolonë, ose në katrorin 3x3.
    for x in range(9):
        if board[row][x] == num or board[x][col] == num or board[3 * (row // 3) + x // 3][3 * (col // 3) + x % 3] == num:
            return False  # Numri është i përsëritur, prandaj vendosja nuk është e ligjshme.
    return True  # Vendosja e numrit është e ligjshme.

def get_next_unassigned(board):
    # Gjen qelinë e parë të zbrazët në tabelë.
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j  # Kthen pozicionin e qelisë së zbrazët.
    return None  # Nuk ka më qeli të zbrazëta.

def solve_sudoku_bfs(board):
    # Përdor Breadth-First Search për të zgjidhur Sudoku-n.
    queue = deque([board])  # Përdor një radhë për të ruajtur gjendjet e tabelës.
    while queue:
        curr_board = queue.popleft()  # Merr gjendjen e tanishme të tabelës nga radha.
        next_unassigned = get_next_unassigned(curr_board)  # Gjen qelinë e radhës për tu mbushur.
        if not next_unassigned:
            return curr_board  # Nëse të gjitha qelitë janë të mbushura, kthen tabelën si zgjidhje.
        i, j = next_unassigned
        for num in range(1, 10):  # Provon të vendosë çdo numër të mundshëm në qelinë.
            new_board = [row[:] for row in curr_board]  # Krijon një kopje të tabelës për çdo mundësi.
            if is_valid(new_board, i, j, num):
                new_board[i][j] = num  # Vendos numrin në qeli nëse është e ligjshme. - backtraching
                queue.append(new_board)  # Shton tabelën e re në radhë për tu kontrolluar më tej.
    return None  # Kthehet None nëse nuk gjendet ndonjë zgjidhje.

def print_sudoku_formatted(board):
    # Printon tabelën e Sudoku-s në një format të lexueshëm.
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")  # Shton një ndarës horizontale çdo tre rreshta.
        
        row_formatted = ""
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_formatted += " | "  # Shton një ndarës vertikale çdo tre kolona.
            row_formatted += str(num) if num != 0 else "."  # Printon numrin ose një pikë nëse qelia është e zbrazët.
            row_formatted += " "
        print(row_formatted)  # Printon rreshtin e formatuar të tabelës.

# Tabela fillestare e Sudoku-s për tu zgjidhur
sudoku_board_bfs = [
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
print(" \n************* Zgjidhja e Sudoku-s me Breadth First Search (BFS) dhe Backtracking ************* \n")

# Printon tabelën e pazgjidhur të Sudoku-s
print(" ------------- Sudoku i pazgjidhur ------------- \n")
print_sudoku_formatted(sudoku_board_bfs)

# Zgjidh Sudoku-n dhe printo rezultatin
solved = solve_sudoku_bfs(sudoku_board_bfs)
if solved:
    # Printon tabelën e zgjidhur nëse zgjidhja u gjet
    print("\n ------------- Sudoku i zgjidhur -------------\n")
    print_sudoku_formatted(solved)
else:
    # Printon një mesazh nëse nuk ka zgjidhje
    print("Nuk ka zgjidhje.")
