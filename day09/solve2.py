from collections import deque
from itertools import combinations

with open("input.txt", "r") as file:
    coords = [tuple(map(int, line.split(","))) for line in file.read().splitlines()]

x_values = set()
y_values = set()

for (x, y) in coords:
    x_values.add(x)
    y_values.add(y)

x_values_sorted = sorted(x_values)
y_values_sorted = sorted(y_values)

values_x_compressed = []
values_y_compressed = []

for x1, x2 in zip(x_values_sorted, x_values_sorted[1:]):
    values_x_compressed.append(x2 - x1 - 1)

for y1, y2 in zip(y_values_sorted, y_values_sorted[1:]):
    values_y_compressed.append(y2 - y1 - 1)


# grid[][] with compressed coordinates with size x_values_sorted * y_values_sorted
grid = [[0 for _ in range(len(values_x_compressed)+1)] for _ in range(len(values_y_compressed)+1)]

for ((x1,y1),(x2,y2)) in zip(coords, coords[1:] + coords[:-1]):
    index_x1 = x_values_sorted.index(x1)
    index_x2 = x_values_sorted.index(x2)
    index_y1 = y_values_sorted.index(y1)
    index_y2 = y_values_sorted.index(y2)

    if index_x2 > index_x1:
        for i in range(index_x2 - index_x1+1):
            grid[index_y1][index_x1+i] = 1
    if index_x1 > index_x2:
        for i in range(index_x1 - index_x2 +1):
            grid[index_y1][index_x1-i] = 1

    if index_y2 > index_y1:
        for j in range(index_y2 - index_y1+1):
            grid[index_y1+j][index_x1] = 1
    if index_y1 > index_y2:
        for j in range(index_y1 - index_y2+1):
            grid[index_y1-j][index_x1] = 1


# flood fill
outside = {(-1, -1)}    # is outside for sure
queue = deque(outside)

while len(queue) > 0:
    ty, tx = queue.popleft()
    for ny, nx in [(ty-1, tx), (ty+1, tx), (ty, tx+1), (ty, tx-1)]:
        if nx < -1 or ny < -1 or nx > len(grid[0]) or ny > len(grid): continue
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == 1: continue
        if (ny, nx) in outside: continue
        outside.add((ny, nx))
        queue.append((ny, nx))


for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (y, x) not in outside:
            grid[y][x] = 1

# prefix sum array of grid
psa = [[0 for _ in range(len(values_x_compressed)+1)] for _ in range(len(values_y_compressed)+1)]
for y in range(len(psa)):
    for x in range(len(psa[0])):
        top = psa[y-1][x] if y > 0 else 0
        left = psa[y][x-1] if x > 0 else 0
        topleft = psa[y-1][x-1] if x > 0 and y > 0 else 0
        psa[y][x] = top + left - topleft + grid[y][x]

def validate(x1, y1, x2, y2):
    c_x2, c_x1 = sorted([x_values_sorted.index(x1), x_values_sorted.index(x2)])
    c_y2, c_y1 = sorted([y_values_sorted.index(y1), y_values_sorted.index(y2)])

    # get psa value
    top = psa[c_y2-1][c_x1] if c_y2-1 >= 0 else 0
    left = psa[c_y1][c_x2-1] if c_x2-1 >= 0 else 0
    topleft = psa[c_y2-1][c_x2-1] if c_y2-1 >= 0 and c_x2-1 >= 0 else 0

    psa_value = psa[c_y1][c_x1] - top - left + topleft

    return psa_value == (c_x1 - c_x2 + 1) * (c_y1 - c_y2 + 1)


max_rec = 0
valid = []
not_valid = []

for (x1, y1), (x2, y2) in combinations(coords, 2):
    max_rec = max(((abs(x2 - x1)+1) * (abs(y2 - y1)+1)) if validate(x1,y1,x2,y2) else 0, max_rec)
print(max_rec)