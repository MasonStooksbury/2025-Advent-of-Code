data = []

with open('input.txt', 'r') as f:
    data = f.read()
    # data = old.splitlines()

# total = 0

# for i in data:
#     total += i.count('^')

print(data.count('^'))