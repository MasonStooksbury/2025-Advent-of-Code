from itertools import combinations

data = []

with open('input.txt', 'r') as f:
    old = f.read()
    data = old.splitlines()

joltages = []
total = 0

for line in data:
    pairs = list(combinations(line, 2))
    max_num = 0
    for pair in pairs:
        number = int(pair[0] + pair[1])
        if number > max_num:
            max_num = number
    joltages.append(max_num)
    total += max_num

print(joltages)
print(total)