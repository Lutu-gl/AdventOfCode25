import re, z3
from collections import Counter

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

# parse input
req_list = []
sets_lists = []
joltages_list = []
for i, line in enumerate(lines):
    r = re.match(r'\[(.*)\] (\(.*\)) {(.*)}', line)
    _, string_sets, joltages = r.groups()
    set_req = set()

    sets = []
    for set_string in string_sets.split(" "):
        set_element = set()
        for element in set_string[1:-1].split(","):
            set_element.add(int(element))
        sets.append(set_element)
    sets_lists.append(sets)


    joltages_list.append(list(map(int, joltages.split(","))))

result = 0
for index, joltages in enumerate(joltages_list):
    sets_list = sets_lists[index]
    button_presses = z3.Ints(f"p{i}" for i in range(len(sets_list)))
    o = z3.Optimize()

    for button_press in button_presses:
        o.add(button_press >= 0)

    for button, joltage in enumerate(joltages):
        rel_button_presses = [button_press for i, button_press in enumerate(button_presses) if button in sets_list[i]]
        o.add(joltage == sum(rel_button_presses))

    o.minimize(sum(button_presses))
    o.check()
    result += o.model().eval(sum(button_presses)).as_long()

print(result)
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# different requirement/equations to achieve solution
# buttons b0,b1...bn (in our example until b5)
# rm is requirement of light n r0,r1...rm (in out example until r3)
# p0,...pn determine how many presses each button has, are integer
# For all pj: pj >= 0   (button presses have to be positive)
# Light 0: 3 = 0*p0 + 0*p1 + 0*p2 + 0*p3 + 1*p4 + 1*p5
# Light 1: 5 = 0*p0 + 1*p1 + 0*p2 + 0*p3 + 0*p4 + 1*p5
# ...
# we want to minimize the number of button presses to reach solution {3,5,4,7}
# min(sum(p0,...pn)

# this is a integer linear problem