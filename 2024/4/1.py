from aocd import get_data
import numpy as np

data = get_data(day=4, year=2024).split("\n")

directions = [
    (0, 1), # Right
    (0, -1), # Left
    (1, 0), # Down
    (-1, 0), #Up
    (1, 1), # D-right
    (-1, -1), # U-left
    (1, -1), # D-left
    (-1, 1), # U-right
]

def solve(data=data):
    rows, cols = len(data), len(data[0])
    count = 0

    data = np.array([list(row) for row in data])

    def is_in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search(x, y, dx, dy, word):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_in_bounds(nx, ny) or data[nx][ny] != word[i]:
                return False
        return True


    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search(x, y, dx, dy, "XMAS"):
                    count += 1

    print(count)

solve()