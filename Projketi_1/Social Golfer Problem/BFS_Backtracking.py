from itertools import combinations
from collections import deque

def valid_group(new_group, existing_groups, week):
    for w in range(week):
        for existing_group in existing_groups[w]:
            if existing_group is not None and len(set(new_group).intersection(existing_group)) > 1:
                return False
    return True

def bfs():
    # Start with an empty list of groups for each week
    initial_state = [None] * W
    queue = deque([(initial_state, 0)])  # Start the queue with the initial state and week 0

    while queue:
        current_groups, week = queue.popleft()  # Get the current state and week

        if week == W:  # If we've filled all weeks, return the solution
            return current_groups

        # Generate all possible combinations of groups for this week
        for group_combination in combinations(range(N), 4):
            new_groups = list(current_groups)  # Copy the current state
            
            # Check if this combination is valid with all previous weeks
            if all(valid_group(group_combination, new_groups, w) for w in range(week)):
                new_groups[week] = [group_combination]  # Set this group for the current week
                queue.append((new_groups, week + 1))  # Add new state to the queue

    return None  # If the queue is empty and we haven't returned, there is no solution

# Vendosni W dhe N sipas nevojave të projektit tuaj
W = 5  # Numri i javëve që dëshironi të planifikoni
N = 32  # Numri total i lojtarëve

result = bfs()

def print_solution(groups):
    for week, week_groups in enumerate(groups):
        print(f"Week {week + 1}:", end=" ")
        for group in week_groups:
            print(",".join(str(player) for player in group), end=" | ")
        print()  # Print a newline at the end of each week

# Pasi të keni gjetur zgjidhjen:
if result:
    print_solution(result)
else:
    print("Nuk u gjet zgjidhje.")
