with open("input.txt", "r") as file:
    ranges = [list(map(int, line.strip())) for line in file]

res = 0
for range in ranges:
    indexed_range = list(enumerate(range))
    sorted_indexed_range = sorted(indexed_range, key= lambda x: -x[1])

    first_element = sorted_indexed_range[0]
    if (first_element[0] == len(range)-1):    # element is last element
        res += int(f"{sorted_indexed_range[1][1]}{first_element[1]}")
        continue

    filtered = list(filter(lambda x: x[0] >= first_element[0], sorted_indexed_range))
    res += int(f"{filtered[0][1]}{filtered[1][1]}")

print(res)
