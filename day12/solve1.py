import re

with open("input.txt", "r") as file:
    lines = file.read().split("\n\n")[-1].splitlines()

result = 0
for line in lines:
    x, y, *count = list(map(int, re.findall(r"\d+", line)))
    if x // 3 * y // 3 >= sum(count):
        result += 1

print(result)