from aocd import get_data

data = get_data(day=6, year=2024).strip().split("\n")
grid = [list(row) for row in data]
rows, cols = len(grid), len(grid[0])

def solve():
    guard_pos = None
    direction = None
    directions_map = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions_map:
                guard_pos = (r, c)
                direction = directions_map[grid[r][c]]
                break
        if guard_pos:
            break

    visited = set()
    direction_order = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction = direction_order.index(direction)

    cursor = guard_pos

    while True:
        visited.add(cursor)

        next_r, next_c = cursor[0] + direction_order[current_direction][0], cursor[1] + direction_order[current_direction][1]
        # valid move?
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break

        if grid[next_r][next_c] != "#":
            cursor = (next_r, next_c)
        else:
            # turn right
            current_direction = (current_direction + 1) % 4
            next_r, next_c = cursor[0] + direction_order[current_direction][0], cursor[1] + direction_order[current_direction][1]
            cursor = (next_r, next_c)

    print(len(visited))
solve()