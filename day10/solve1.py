import re
from collections import Counter

class XorSet(set):
    def update(self, *others):
        for other in others:
            self ^= other

    def add(self, __element):
        if __element in self:
            self.remove(__element)
        else:
            super().add(__element)

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

# parse input
req_list = []
sets_list = []
for i, line in enumerate(lines):
    match = re.search(r'\[(.*)\] (\(.*\))', line)
    req = match.group(1)
    set_req = set()
    for index, char in enumerate(req):
        if char == '#':
            set_req.add(index)
    req_list.append(set_req)

    sets = []
    string_sets = match.group(2)
    for set_string in string_sets.split(" "):
        set_element = set()
        for element in set_string[1:-1].split(","):
            set_element.add(int(element))
        sets.append(set_element)
    sets_list.append(sets)


# perform calculation
# we have the sets and we have the end_result
# calculate the power set out of the sets together with a number of how many sets it took to create it
# we need to store only the min number on operations it took

result = 0
for index, req in enumerate(req_list):
    sets = sets_list[index]

    # calculate power set, contains tuple of set and the number of sets used
    power_set = []
    min_sets_used = len(sets)
    for i in range(0, pow(2, len(sets))):
        combination_set = XorSet()
        c = i
        choose_set = 0
        sets_used = 0
        while c > 0:
            if c & 1 == 1:
                sets_used += 1
                combination_set.update(sets[choose_set])
            choose_set+=1
            c >>= 1
        if combination_set == req:
            min_sets_used = min(min_sets_used, sets_used)
        power_set.append((combination_set, sets_used))
    result += min_sets_used

print(result)