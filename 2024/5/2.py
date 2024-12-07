from aocd import get_data
from collections import defaultdict, deque

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

def sort(subgraph, nodes):
    in_degree = {node: 0 for node in nodes}
    for x in nodes:
        for y in subgraph[x]:
            if y in nodes:
                in_degree[y] += 1

    # Kahn
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in subgraph[node]:
            if neighbor in nodes:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    return sorted_order

def solve():
    graph = defaultdict(set)
    for rule in rules:
        x, y = map(int, rule.split("|"))
        
        graph[x].add(y)

    total = 0

    for update in updates:
        if not isValid(update, graph):
            subgraph = defaultdict(set)
            for x in update:
                subgraph[x] = {y for y in graph[x] if y in update}

            sorted = sort(subgraph, update)

            total += sorted[len(sorted) // 2]

    print(total)

solve()