from collections import deque

def bfs(graph, start):
    visited = {node: False for node in graph}
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# Për të testuar BFS:
graph_bfs = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}
start_node_bfs = 1
print("\nBFS:")
bfs(graph_bfs, start_node_bfs)

def is_valid(candidate):
    # Kjo është një funksion i imagjinar që vlerëson validitetin e një zgjidhjeje të mundshme
    # Për shembull, nëse keni një problemin që kërkon një zgjidhje të ndaluar, këtu do të vendosni logjikën e validitetit.

    # Për shembull, një zgjidhje është e vlefshme nëse nuk përmban dy elemente të njëjtë.

    return len(set(candidate)) == len(candidate)

def backtracking(problem_space, solution=[]):
    if len(solution) == len(problem_space):
        # Nëse kemi gjetur një zgjidhje të mundshme, printo rezultatin
        print(solution)
        return

    for candidate in problem_space:
        if is_valid(solution + [candidate]):
            # Shto kandidatin në zgjidhje dhe vazhdo kërkimin me zgjidhjen e re
            backtracking(problem_space, solution + [candidate])

# Për të testuar Backtracking:
problem_space_backtracking = [1, 2, 3, 4]
print("\nBacktracking:")
backtracking(problem_space_backtracking)
