from curses.ascii import isdigit
from functools import reduce

with open("input.txt", "r") as file:
    matrix = [list(line) for line in file.read().splitlines()]

n = len(matrix)
column = reduce(lambda acc, line: max(acc, len(line)), matrix[:-1], 0) - 1  # get start index

# fill matrix up with empty spaces so we don't have to deal with index out of bound when iterating
for line in matrix:
    line += [' '] * (column-len(line)+1)

numbers = []
res = 0
while column >= 0:
    number_string = ""
    for line in matrix[:-1]:
        if isdigit(line[column]):
            number_string += line[column]
    if number_string:
        numbers.append(int(number_string))

    if matrix[n-1][column] == '+':
        res += sum(numbers)
        numbers = []
    elif matrix[n-1][column] == '*':
        res += reduce(lambda acc, num: acc * num, numbers, 1)
        numbers = []

    column -= 1

print(res)