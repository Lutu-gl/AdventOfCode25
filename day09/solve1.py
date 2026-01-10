from itertools import combinations

with open("input.txt", "r") as file:
    coords = [tuple(map(int, line.split(","))) for line in file.read().splitlines()]

max_rec = 0
for c1, c2 in combinations(coords, 2):
    max_rec = max((abs(c1[0] - c2[0])+1)* (abs(c1[1] - c2[1])+1), max_rec)

print(max_rec)