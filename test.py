string = '###$&&###'

# data[rindex] = data[rindex][:(cindex-1)] + '.' + data[rindex][cindex:]

for i,e in enumerate(string):
    if e == '$':
        string = string[:i] + '.' + string[i+1:]
        break

# string = string[:2] + '.' + string[3:]

print(string)