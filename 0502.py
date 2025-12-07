data = []

with open('input.txt', 'r') as f:
    old = f.read()
    data = old.splitlines()

# range(max(x[0], y[0]), min(x[-1], y[-1])+1)


check = 0
cstart = 0
cend = 0
for i,r in enumerate(data):
    if i == 1:
        check = r
        cstart, cend = check.split('-')
        cstart = int(cstart)
        cend = int(cend)
    start, end = r.split('-')
    print(cstart, start, cend, end)
    print(range(max(cstart, int(start)), min(cend, int(end))))
    



# all_nums = []

# for r in data:
#     start, end = r.split('-')

#     for i in range(int(start), int(end)+1):
#         all_nums.append(i)


# print(len(list(set(all_nums))))