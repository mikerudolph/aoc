from aocd import get_data
from collections import defaultdict

rules, updates = get_data(day=5, year=2024).split("\n\n")
rules = rules.strip().split("\n")
updates = [list(map(int, line.split(','))) for line in updates.strip().split("\n")]

def isValid(update, graph):
    pos = {page: i for i, page in enumerate(update)}
    for x in update:
        for y in graph[x]:
            if y in pos and pos[x] > pos[y]:
                return False
    return True


def solve():
    graph = defaultdict(set)
    for rule in rules:
        x, y = map(int, rule.split("|"))
        
        graph[x].add(y)

    total = 0

    for update in updates:
        if isValid(update, graph):
            total += update[len(update) // 2]

    print(total)

solve()