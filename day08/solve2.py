import heapq
import math
from itertools import combinations

with open("input.txt", "r") as file:
    points = [tuple(map(int, line.split(","))) for line in file.read().splitlines()]


heap = []
for point1, point2 in combinations(points, 2):
    val = math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2) + math.pow(point1[2] - point2[2], 2))
    heapq.heappush(heap, (val, point1, point2))

sets = []
for point in points:
    s = set()
    s.add(point)
    sets.append(s)

while len(sets) != 1:
    smallest = heapq.heappop(heap)
    found = False

    for set1 in sets:
        if smallest[1] in set1:
            found = True
            set1.add(smallest[2])
            for set2 in sets:
                if set1 == set2:
                    continue
                if smallest[2] in set2:
                    set1.update(set2)
                    sets.remove(set2)
        if smallest[2] in set1:
            found = True
            set1.add(smallest[1])
            for set2 in sets:
                if set1 == set2:
                    continue
                if smallest[1] in set2:
                    set1.update(set2)
                    sets.remove(set2)

print(smallest[1][0] * smallest[2][0])
