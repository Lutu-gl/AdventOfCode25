with open("input.txt", "r") as file:
    grid = [list(line) for line in file.read().splitlines()]

for y, line in enumerate(grid):
    if "S" in line:
        x = line.index("S")
        break

timelines = [[0 for _ in row] for row in grid]
timelines[y][x] = 1

n = len(timelines)
m = len(timelines[0])

for i in range(y+1,n):
    for j in range(m):
        timeline = timelines[i-1][j]
        if timeline == 0:
            continue
        if grid[i][j] == '^':
            timelines[i][j-1] += timeline
            timelines[i][j+1] += timeline
            continue
        timelines[i][j] += timeline

res = sum(timelines[-1])
print(res)