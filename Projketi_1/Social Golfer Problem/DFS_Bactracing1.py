from itertools import combinations

def generate_possible_groups(existing_groups, week, N):
    players = set(range(N))  # N është numri total i lojtarëve

    # Hiqni lojtarët që tashmë janë caktuar në grupe në javët e mëparshme
    for w in range(week):
        week_groups = existing_groups[w]
        if week_groups is not None:  # Sigurohuni që ka grupe për këtë javë
            for group in week_groups:
                players.difference_update(group)

    # Krijo të gjitha kombinimet e mundshme të grupeve prej 4 lojtarësh nga lojtarët e mbetur
    return combinations(players, 4)

def valid_group(new_group, existing_groups, week):
    for w in range(week):
        for existing_group in existing_groups[w]:
            if len(set(new_group).intersection(existing_group)) > 1:
                return False
    return True

def dfs(groups, week, N):
    if week == len(groups):  # Kontrollo nëse të gjitha javët janë përpunuar
        return True
    for group in generate_possible_groups(groups, week, N):
        if valid_group(group, groups, week):
            groups[week] = [group]  # Sigurohuni që ky është një listë e grupeve
            if dfs(groups, week + 1, N):
                return True
            groups[week] = None  # Backtracking
    return False

def find_solution(N):
    # Provoni një numër të ndryshëm të javëve duke filluar nga 1 dhe duke rritur ngadalë
    for W in range(1, N // 4 + 1):  # N / 4 është numri maksimal teorik i javëve
        groups = [None] * W
        if dfs(groups, 0, N):
            return groups, W
    return None, 0

# Vendosni numrin e lojtarëve
N = 32

solution, max_weeks = find_solution(N)
def print_solution(groups):
    for week, week_groups in enumerate(groups):
        # Check if the week has any groups
        if week_groups is None or len(week_groups) == 0:
            print(f"Week {week + 1}: No groups assigned")
            continue

        print(f"Week {week + 1}:", end=" ")
        for group in week_groups:
            # Check if the group is valid
            if group:
                print(",".join(str(player) for player in group), end=" | ")
        print()  # Print a newline at the end of each week

# Print the solution
if solution:
    print_solution(solution)
    print(f"Numri maksimal i javëve: {max_weeks}")
else:
    print("Nuk u gjet zgjidhje.") 

