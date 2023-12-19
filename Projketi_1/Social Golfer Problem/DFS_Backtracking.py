from itertools import combinations

def generate_possible_groups(existing_groups, week):
    players = set(range(N))  # N është numri total i lojtarëve

    # Hiqni lojtarët që tashmë janë caktuar në grupe në javët e mëparshme
    for w in range(week):
        week_groups = existing_groups[w]
        if week_groups is not None:  # Sigurohuni që ka grupe për këtë javë
            for group in week_groups:
                players.difference_update(group)

    # Krijo të gjitha kombinimet e mundshme të grupeve prej 4 lojtarësh nga lojtarët e mbetur
    for group_combination in combinations(players, 4):
        yield group_combination


def valid_group(new_group, existing_groups, week):
    for w in range(week):
        for existing_group in existing_groups[w]:
            if len(set(new_group).intersection(existing_group)) > 1:
                return False
    return True

def dfs(groups, week=0):
    if week == W:  # W është numri i javëve
        return True
    for group in generate_possible_groups(groups, week):
        if valid_group(group, groups, week):
            groups[week] = [group]  # Sigurohuni që ky është një listë e grupeve
            if dfs(groups, week + 1):
                return True
            # Backtracking
            groups[week] = None
    return False

# Vendosni W dhe N sipas nevojave të projektit tuaj
W = 9
N = 32

initial_groups = [None] * W
result = dfs(initial_groups)

def print_solution(groups):
    for week, week_groups in enumerate(groups):
        print(f"Week {week + 1}:", end=" ")
        for group in week_groups:
            print(",".join(str(player) for player in group), end=" | ")
        print()  # Print a newline at the end of each week

# Pasi të keni gjetur zgjidhjen:
if result:
    print_solution(initial_groups)
else:
    print("Nuk u gjet zgjidhje.")