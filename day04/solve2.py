with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

dx = [-1,0,1,1,1,0,-1,-1]
dy = [1,1,1,0,-1,-1,-1,0]
directions = list(zip(dx, dy))

rolls_accessible = 0
remove_positions = []

while True:
    for (x, y) in remove_positions:
        grid[y][x] = '.'

    remove_positions = []


    for y in range(len(grid)):
        for x in range (len(grid[y])):
            if grid[y][x] != '@':
                continue
            num_rolls = 0

            for (dx, dy) in directions:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= len(grid[y]) or ny >= len(grid):
                    continue
                if grid[ny][nx] == '@':
                    num_rolls += 1
            if num_rolls < 4:
                remove_positions.append((x, y))
                rolls_accessible += 1
    if not remove_positions:
        break

print(rolls_accessible)