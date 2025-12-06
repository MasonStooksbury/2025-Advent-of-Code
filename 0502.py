data = []

with open('input.txt', 'r') as f:
    old = f.read()
    data = old.splitlines()


all_nums = []

for r in data:
    start, end = r.split('-')

    for i in range(int(start), int(end)+1):
        all_nums.append(i)


print(len(list(set(all_nums))))