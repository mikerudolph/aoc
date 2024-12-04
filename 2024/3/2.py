from aocd import get_data
import re

def solve():
    remove = r"don't\(\).*?(do\(\)|$)"
    data = re.sub(remove, "", get_data(day=3, year=2024).replace(" ", ""), flags=re.DOTALL)

    pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    matches = re.findall(pattern, data, flags=re.DOTALL)

    total = 0

    for match in matches:
        num1, num2 = map(int, match)
        total += num1 * num2

    print(total)

solve()