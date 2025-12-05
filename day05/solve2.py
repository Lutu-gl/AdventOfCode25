with open("input.txt", "r") as file:
    ranges, _ = file.read().split("\n\n")

ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]
ranges.sort()

fresh_ingredients = 0

index = 1
start = ranges[0][0]
end = ranges[0][1]

while index < len(ranges):
    if ranges[index][0] <= end:
        end = max(end, ranges[index][1])
        index += 1
        continue
    fresh_ingredients += end - start + 1
    start = ranges[index][0]
    end = ranges[index][1]
    index += 1

fresh_ingredients += end - start + 1
print (fresh_ingredients)