data = []

with open('input.txt', 'r') as f:
    old = f.read()
    data = old.splitlines()



def getAdjacentRolls(row, column):
    rolls = 0
    spaces_to_check = []

    if row == 0 or row == len(data)-1 or column == 0 or column == len(data[0])-1:
        if row == 0:
            if column == 0:
                spaces_to_check = [data[row][column+1], data[row+1][column], data[row+1][column+1]]
            elif column == len(data[0])-1:
                spaces_to_check = [data[row][column-1], data[row+1][column], data[row+1][column-1]]
            else:
                spaces_to_check = [data[row][column-1], data[row][column+1], data[row+1][column-1], data[row+1][column], data[row+1][column+1]]
        elif row == len(data)-1:
            if column == 0:
                spaces_to_check = [data[row][column+1], data[row-1][column], data[row-1][column+1]]
            elif column == len(data[0])-1:
                spaces_to_check = [data[row][column-1], data[row-1][column], data[row-1][column-1]]
            else:
                spaces_to_check = [data[row][column-1], data[row][column+1], data[row-1][column-1], data[row-1][column], data[row-1][column+1]]
            pass
        elif column == 0:
            spaces_to_check = [data[row][column+1], data[row-1][column], data[row-1][column+1], data[row+1][column], data[row+1][column+1]]
        elif column == len(data[0])-1:
            spaces_to_check = [data[row][column-1], data[row-1][column-1], data[row-1][column], data[row+1][column], data[row+1][column-1]]
    else:
        spaces_to_check = [data[row-1][column-1], data[row-1][column], data[row-1][column+1],
            data[row][column-1], data[row][column+1],
            data[row+1][column-1], data[row+1][column], data[row+1][column+1]
        ]
    
    for space in spaces_to_check:
        if space == '@':
            rolls += 1
    
    return rolls <= 3



total = 0
found_stuff = False
loop = True

while loop:
    found_stuff = False
    for rindex, row in enumerate(data):
        for cindex, column in enumerate(row):
            if data[rindex][cindex] == '@' and getAdjacentRolls(rindex, cindex):
                total += 1
                data[rindex] = data[rindex][:cindex] + '.' + data[rindex][cindex+1:]
                found_stuff = True
    if not found_stuff:
        loop = False

print(total)





















# data = []

# with open('input.txt', 'r') as f:
#     old = f.read()
#     data = old.splitlines()



# def getAdjacentRolls(row, column):
#     rolls = 0
#     spaces_to_check = []

#     if row == 0 or row == len(data)-1 or column == 0 or column == len(data[0])-1:
#         if row == 0:
#             if column == 0:
#                 spaces_to_check = [{'icon': data[row][column+1], 'coords': [row, column+1]}, {'icon': data[row+1][column], 'coords': [row+1, column]}, {'icon': data[row+1][column+1], 'coords': [row+1, column+1]}]
#             elif column == len(data[0])-1:
#                 spaces_to_check = [{'icon': data[row][column-1], 'coords': [row, column-1]}, {'icon': data[row+1][column], 'coords': [row+1, column]}, {'icon': data[row+1][column-1], 'coords': [row+1, column-1]}]
#             else:
#                 spaces_to_check = [{'icon': data[row][column-1], 'coords': [row, column-1]}, {'icon': data[row][column+1], 'coords': [row, column+1]}, {'icon': data[row+1][column-1], 'coords': [row+1, column-1]}, {'icon': data[row+1][column], 'coords': [row+1, column]}, {'icon': data[row+1][column+1], 'coords': [row+1, column+1]}]
#         elif row == len(data)-1:
#             if column == 0:
#                 spaces_to_check = [{'icon': data[row][column+1], 'coords': [row, column+1]}, {'icon': data[row-1][column], 'coords': [row-1, column]}, {'icon': data[row-1][column+1], 'coords': [row-1, column+1]}]
#             elif column == len(data[0])-1:
#                 spaces_to_check = [{'icon': data[row][column-1], 'coords': [row, column-1]}, {'icon': data[row-1][column], 'coords': [row-1, column]}, {'icon': data[row-1][column-1], 'coords': [row-1, column-1]}]
#             else:
#                 spaces_to_check = [{'icon': data[row][column-1], 'coords': [row, column-1]}, {'icon': data[row][column+1], 'coords': [row, column+1]}, {'icon': data[row-1][column-1], 'coords': [row-1, column-1]}, {'icon': data[row-1][column], 'coords': [row-1, column]}, {'icon': data[row-1][column+1], 'coords': [row-1, column+1]}]
#             pass
#         elif column == 0:
#             spaces_to_check = [{'icon': data[row][column+1], 'coords': [row, column+1]}, {'icon': data[row-1][column], 'coords': [row-1, column]}, {'icon': data[row-1][column+1], 'coords': [row-1, column+1]}, {'icon': data[row+1][column], 'coords': [row+1, column]}, {'icon': data[row+1][column+1], 'coords': [row+1, column+1]}]
#         elif column == len(data[0])-1:
#             spaces_to_check = [{'icon': data[row][column-1], 'coords': [row, column-1]}, {'icon': data[row-1][column-1], 'coords': [row-1, column-1]}, {'icon': data[row-1][column], 'coords': [row-1, column]}, {'icon': data[row+1][column], 'coords': [row+1, column]}, {'icon': data[row+1][column-1], 'coords': [row+1, column-1]}]
#     else:
#         spaces_to_check = [{'icon': data[row-1][column-1], 'coords': [row-1, column-1]}, {'icon': data[row-1][column], 'coords': [row-1, column]}, {'icon': data[row-1][column+1], 'coords': [row-1, column+1]},
#             {'icon': data[row][column-1], 'coords': [row, column-1]}, {'icon': data[row][column+1], 'coords': [row, column+1]},
#             {'icon': data[row+1][column-1], 'coords': [row+1, column-1]}, {'icon': data[row+1][column], 'coords': [row+1, column]}, {'icon': data[row+1][column+1], 'coords': [row+1, column+1]}
#         ]

#     result = {'status': false, 'rolls': []}
    
#     for space in spaces_to_check:
#         if space['icon'] == '@':
#             rolls += 1
#             result['rolls'].append(space['coords'])

    
#     return result



# total = 0

# for rindex, row in enumerate(data):
#     for cindex, column in enumerate(row):
#         if data[rindex][cindex] == '@':
#             result = getAdjacentRolls(rindex, cindex)

#             total += 1

# print(total)