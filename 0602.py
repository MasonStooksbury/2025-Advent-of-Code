num_size = 4

data = 0

with open('input.txt', 'r') as f:
    old = f.read()
    data = old.splitlines()


everything = []
for line in data:
    arr = []
    count = 0
    string = ''
    for i,char in enumerate(line):
        if count == num_size:
            arr.append(string)
            count = 0
            string = ''
            continue
        if i == len(line)-1:
            string += char
            arr.append(string)
            count = 0
            string = ''
        string += char
        count += 1
    everything.append(arr)

new_everything = []
for line in everything:
    new_everything.append([e for i,e in enumerate(line) if e != ' ' and e != '  '])

print(new_everything)

stuff = zip(*new_everything)
print(list(stuff))

print('start')


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

for eq in zip(*new_everything):
    first_num = ''
    second_num = ''
    third_num = ''
    fourth_num = ''

    for i,num in enumerate(eq):
        if i == len(eq)-1:
            continue
        fourth_num += num[0]
        third_num += num[1]
        second_num += num[2]
        first_num += num[3]
    
    nums = [first_num, second_num, third_num, fourth_num]
    
    if '+' in eq[-1]:
        final += add(nums)
    else:
        final += multiply(nums)
    
print(final)





# final = 0
# stuff = zip(*new_data)
# for i in stuff:
#     if i[-1] == '+':
#         final += add(i[:-1])
#     else:
#         final += multiply(i[:-1])

# print(final)