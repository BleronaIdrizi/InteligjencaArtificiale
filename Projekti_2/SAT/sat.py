# -*- coding: utf-8 -*-

# Sigurohuni që të keni instaluar PySAT përmes pip nëse nuk e keni bërë tashmë:
# pip install python-sat

from pysat.formula import CNF
from pysat.solvers import Solver

# Numri i mysafirëve dhe tavolinave
num_mysafire = 100
num_tavolina = 10

# Lista e çifteve që nuk mund të ulen së bashku (shembull)
nuk_ulen_bashke = [(1, 5), (2, 8), (10, 20)]  # Mysafirët janë të numëruar nga 1 deri në 100

# Lista e çifteve që duhet të ulen së bashku (shembull)
duhet_ulen_bashke = [(3, 4), (15, 25), (30, 40)]

# Krijimi i formulës SAT
formula = CNF()

# Funksion për të kthyer variablat për çdo mysafir në çdo tavolinë
def var(mysafir, tavoline):
    return mysafir + num_mysafire * (tavoline - 1)

# Shtimi i kushteve që mysafirët që nuk mund të ulen së bashku të mos jenë në të njëjtën tavolinë
for (m1, m2) in nuk_ulen_bashke:
    for t in range(1, num_tavolina + 1):
        formula.append([-var(m1, t), -var(m2, t)])

# Shtimi i kushteve që mysafirët që duhet të ulen së bashku të jenë në të njëjtën tavolinë
for (m1, m2) in duhet_ulen_bashke:
    for t in range(1, num_tavolina + 1):
        formula.append([var(m1, t), -var(m2, t)])
        formula.append([-var(m1, t), var(m2, t)])

# Shtimi i kushtit që çdo mysafir duhet të jetë në një tavolinë
for m in range(1, num_mysafire + 1):
    formula.append([var(m, t) for t in range(1, num_tavolina + 1)])

# Zgjidhja e problemit
with Solver() as s:
    s.append_formula(formula)
    if s.solve():
        zgjidhja = s.get_model()
        mysafire_ne_tavolina = {t: [] for t in range(1, num_tavolina + 1)}
        for m in range(1, num_mysafire + 1):
            for t in range(1, num_tavolina + 1):
                if var(m, t) in zgjidhja:
                    mysafire_ne_tavolina[t].append(m)
                    break
        print("Zgjidhja e gjetur:")
        for t in mysafire_ne_tavolina:
            print("Tavolina {}: {}".format(t, mysafire_ne_tavolina[t]))
    else:
        print("Nuk ka zgjidhje.")
