with open("input.txt", "r") as file:
    ranges, numbers = file.read().split("\n\n")

ranges = [list(map(int, range.split("-"))) for range in ranges.splitlines()]
numbers = [int(number) for number in numbers.splitlines()]

fresh_count = 0
for number in numbers:
    fresh = False
    for range in ranges:
        if range[0] <= number <= range[1]:
            fresh = True
            break
    if fresh:
        fresh_count += 1

print(fresh_count)