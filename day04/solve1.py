with open("input.txt", "r") as file:
    ranges = [list(line.strip()) for line in file]

dx = [-1,0,1,1,1,0,-1,-1]
dy = [1,1,1,0,-1,-1,-1,0]
directions = list(zip(dx, dy))

rolls_accessible = 0
for y in range(len(ranges)):
    for x in range (len(ranges[y])):
        if ranges[y][x] != '@':
            continue
        num_rolls = 0;

        for (dx, dy) in directions:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= len(ranges[y]) or ny >= len(ranges):
                continue
            if ranges[ny][nx] == '@':
                num_rolls += 1
        if num_rolls < 4:
            rolls_accessible += 1

print(rolls_accessible)