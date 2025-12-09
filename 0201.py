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
        wee = str(int(first) + i)
        math = len(wee)//2
        if len(wee) % 2 == 0:
            first_half = wee[:math]
            last_half = wee[math:]
            
            if first_half == last_half:
                total += int(wee)

print(total)