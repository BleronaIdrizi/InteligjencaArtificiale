def dfs(graph, start, visited):
    stack = [start]
    visited[start] = True

    while stack:
        current = stack.pop()
        print(current, end=" ")

        for neighbor in graph[current]:
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True

# Për të testuar DFS:
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}
visited_nodes = {node: False for node in graph}
start_node = 1
print("DFS:")
dfs(graph, start_node, visited_nodes)

# Backtracking implementation
def is_valid(candidate):
    return len(set(candidate)) == len(candidate)

def backtracking(problem_space, solution=[]):
    if len(solution) == len(problem_space):
        print(solution)
        return

    for candidate in problem_space:
        if is_valid(solution + [candidate]):
            backtracking(problem_space, solution + [candidate])

# Për të testuar Backtracking:
problem_space = [1, 2, 3, 4]
print("\nBacktracking:")
backtracking(problem_space)
