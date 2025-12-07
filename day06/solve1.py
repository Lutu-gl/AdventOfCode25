from functools import reduce

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    *range_lines, last_line = lines
    operations = last_line.split()
    exercise_lines = [list(map(int, line.split())) for line in range_lines]

exercises = [list(nums) for nums in zip(*exercise_lines)]

res = 0
for i, operation in enumerate(operations):
    print(exercises[i])

    if operation == '+':
        res += sum(exercises[i])
    else:
        res += reduce(lambda acc, num: acc * num, exercises[i],1)

print(res)