import re
from functools import cache

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

adjacency_list = {}

for line in lines:
    match = re.match(r"^(\w+):\s+(.*)$", line.strip())
    source, destination = match.groups()
    destination = destination.split(" ")
    adjacency_list[source] = destination

@cache
def traverse(source, goal, visit_dac, visit_fft):
    if source not in adjacency_list:
        return 0

    res = 0
    for dest in adjacency_list[source]:
        if dest == goal and visit_dac and visit_fft:
            res += 1
        elif dest == "dac":
            res += traverse(dest, goal, True, visit_fft)
        elif dest == "fft":
            res += traverse(dest, goal, visit_dac, True)
        else:
            res += traverse(dest, goal, visit_dac, visit_fft)


    return res

result = traverse("svr", "out", False, False)

print(result)