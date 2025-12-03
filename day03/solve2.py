with open("input.txt", "r") as file:
    battery = [list(map(int, line.strip())) for line in file]

res = 0
for bank in battery:
    n = len(bank)
    indexed_range = list(enumerate(bank))
    sorted_indexed_range = sorted(indexed_range, key= lambda x: -x[1])

    number_string = ""
    for i in range(12):
        filtered = list(filter(lambda x: x[0] <  n-12+1+i, sorted_indexed_range))
        number_string += str(filtered[0][1])
        sorted_indexed_range = list(filter(lambda  x: x[0] > filtered[0][0], sorted_indexed_range)) # remove added and previous elements

    res += int(f"{number_string}")

print(res)