from aocd import get_data

data = get_data(day=4, year=2024).split("\n")

def solve():
    rows, cols = len(data), len(data[0])
    count = 0

    for x in range(rows):
        for y in range(cols):
            if x + 2 < rows and y + 2 < cols and data[x][y] == "M" and data[x+1][y+1] == "A" and data[x+2][y+2] == 'S' and data[x+2][y] == 'M' and data[x][y+2] == 'S':
                count += 1
            if x + 2 < rows and y + 2 < cols and data[x][y] == "M" and data[x+1][y+1] == "A" and data[x+2][y+2] == 'S' and data[x+2][y] == 'S' and data[x][y+2] == 'M':
                count += 1
            if x + 2 < rows and y + 2 < cols and data[x][y] == "S" and data[x+1][y+1] == "A" and data[x+2][y+2] == 'M' and data[x+2][y] == 'M' and data[x][y+2] == 'S':
                count += 1
            if x + 2 < rows and y + 2 < cols and data[x][y] == "S" and data[x+1][y+1] == "A" and data[x+2][y+2] == 'M' and data[x+2][y] == 'S' and data[x][y+2] == 'M':
                count += 1

    print(count)

solve()