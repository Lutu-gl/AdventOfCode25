import re

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

adjacency_list = {}

for line in lines:
    match = re.match(r"^(\w+):\s+(.*)$", line.strip())
    source, destination = match.groups()
    destination = destination.split(" ")
    adjacency_list[source] = destination

def traverse(adjacency_list, source, goal):
    if source not in adjacency_list:
        return 0

    res = 0
    for dest in adjacency_list[source]:
        if dest == goal:
            res += 1
        else:
            res += traverse(adjacency_list, dest, goal)

    return res

result = traverse(adjacency_list, "you", "out")

print(result)