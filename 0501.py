data = []

with open('input.txt', 'r') as f:
    old = f.read()
    data = old.splitlines()


fresh_ranges = []
ids = []

ranges = True
for line in data:
    if ranges and line != '':
        fresh_ranges.append(line)
    elif line == '':
        ranges = False
    elif not ranges and line != '':
        ids.append(line)

fresh = 0

for i in ids:
    for r in fresh_ranges:
        start, end = r.split('-')

        if int(i) >= int(start) and int(i) <= int(end):
            fresh += 1
            break

print(fresh)
