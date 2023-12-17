# Sudoku Solver

Ky projekt përmban zgjidhjet e ndryshme për një lojë Sudoku duke përdorur algoritme të ndryshme të kërkimit siq janë: Depth-First Search (DFS) & Backtracking dhe Breadth-First Search (BFS) & Backtracking.

## Përshkrimi

Sudoku është një lojë logjike që konsiston në një tabelë 9x9, e ndarë në katrore të vogla 3x3. Qëllimi është të mbushësh tabelën në mënyrë që çdo rresht, çdo kolonë dhe çdo katror 3x3 të përmbajë të gjitha numrat nga 1 deri në 9 pa përsëritje.

## Zgjidhjet

Projekti përmban dy zgjidhje të ndryshme për të zgjidhur Sudoku:

1. **Zgjidhja me Depth-First Search (DFS) dhe Backtracking:**
   - Përdor një qasje të thellë të parë për të eksploruar mundësitë dhe backtracking për të korrigjuar zgjedhjet në rast se rruga aktuale nuk çon në zgjidhje.

2. **Zgjidhja me Breadth-First Search (BFS) dhe Backtracking:**
   - Eksploron mundësitë në një mënyrë më të gjerë duke përdorur një radhë për të menaxhuar gjendjet e ndryshme të tabelës. Kjo metodë mund të jetë më e ngadaltë por ofron një qasje më të gjerë.

## Përdorimi

Për të ekzekutuar zgjidhjet, duhet të keni Python të instaluar në sistemin tuaj. Pasi ta keni klonuar projektin file-s mund t'i ekzekutoni si më poshtë:

```bash
python3 -u DFS_Backtracking.py  # Për zgjidhjen me DFS
python3 -u BFS_Backtracking.py  # Për zgjidhjen me BFS
