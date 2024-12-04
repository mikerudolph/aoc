from aocd import get_data
import re

def solve():
    data = get_data(day=3, year=2024)

    pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    matches = re.findall(pattern, data)

    total = 0

    for match in matches:
        num1, num2 = map(int, match)
        total += num1 * num2

    print(total)

solve()