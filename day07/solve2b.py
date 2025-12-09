from functools import cache

@cache
def beam_down(position):
    x, y = position
    n = len(grid)
    num_splits = 0
    while y < n:
        if grid[y][x] == '^':
            num_splits += 1
            num_splits += beam_down((x-1, y))
            num_splits += beam_down((x+1, y))
            break
        grid[y][x] = '|'
        y+=1
    return num_splits


with open("input.txt", "r") as file:
    grid = [list(line) for line in file.read().splitlines()]

for y, line in enumerate(grid):
    if "S" in line:
        x = line.index("S")
        break


res = beam_down((x, y+1))
print(res+1)