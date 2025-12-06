data = 0

with open('input.txt', 'r') as f:
    old = f.read()
    data = old.splitlines()

new_data = []
for line in data:
    thing = line.strip()
    new_data.append([x for x in thing.split(' ') if x != ''])


def add(nums):
    total = 0
    for num in nums:
        total += int(num)
    return total

def multiply(nums):
    total = 1
    for num in nums:
        total *= int(num)
    return total




final = 0
stuff = zip(*new_data)
for i in stuff:
    if i[-1] == '+':
        final += add(i[:-1])
    else:
        final += multiply(i[:-1])

print(final)