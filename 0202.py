import re

data = ''

with open('input.txt', 'r') as f:
    data = f.readline()

ranges = data.split(',')

total = 0

for r in ranges:
    first, last = r.split('-')

    for i in range((int(last)-int(first))+1):
        # print(f'{int(first) + i}')
        x = re.search(r"\b(\d+)\1+\b", str(int(first)+i))
        if x is not None:
            # print(x.group())
            total += int(x.group())


    
    # input()
print(total)