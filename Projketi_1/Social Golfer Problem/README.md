# Social Golfers Problem

## Përshkrimi

"Social Golfers Problem" është një sfidë që përfshin organizimin e lojtarëve të golfit në grupe. Problemi specifikon se 32 lojtarë golfi luajnë golf një herë në javë në grupe prej 4 lojtarësh. Qëllimi është të organizohen lojtarët në mënyrë që asnjë dy lojtarë të mos luajnë më shumë se një herë në të njëjtin grup gjatë një sezoni.

## Qëllimi i Projektit

Projekti synon të zhvillojë algoritme të ndryshme për zgjidhjen e këtij problemi, përfshirë përdorimin e Depth-First Search (DFS) me backtracking dhe Breadth-First Search (BFS) me backtracking.

## Zgjidhjet

Zgjidhja përfshin dy metoda të ndryshme:

1. **Zgjidhja me Depth-First Search (DFS) dhe Backtracking:**
   - Përdor një qasje të thellë të parë për të eksploruar mundësitë dhe backtracking për të korrigjuar zgjedhjet në rast se rruga aktuale nuk çon në zgjidhje.

2. **Zgjidhja me Breadth-First Search (BFS) dhe Backtracking:**
   - Eksploron mundësitë në një mënyrë më të gjerë dhe përdor një radhë për të menaxhuar gjendjet e ndryshme të tabelës. Kjo metodë mund të jetë më e ngadaltë por ofron një qasje më të gjerë.

## Përdorimi

Për të ekzekutuar zgjidhjet, duhet të keni Python të instaluar në sistemin tuaj. Ju mund të ekzekutoni skriptat e zgjidhjes duke përdorur komandat e mëposhtme në terminalin tuaj:

```bash
python3 -u DFS_Backtracking.py  # Për zgjidhjen me DFS
python3 -u BFS_Backtracking.py  # Për zgjidhjen me BFS
