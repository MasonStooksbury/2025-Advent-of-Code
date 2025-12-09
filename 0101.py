data = []

with open('stuff.txt', 'r') as f:
    old_data = f.read()
    data = old_data.splitlines()

start_position = 50
current_position = start_position

count = 0


def newPosition(curr_pos, direction, distance):
    global count
    
    for _ in range(distance):
        if direction == 'L':
            curr_pos -= 1
            if curr_pos == 0:
                count += 1
            if curr_pos < 0:
                curr_pos = 99
        else:
            curr_pos += 1
            if curr_pos > 99:
                curr_pos = 0
            if curr_pos == 0:
                count += 1
    
    return curr_pos




for turn in data:
    current_position = newPosition(current_position, turn[0], int(turn[1:]))

print(count)






  # if curr_pos < 0:
    #     new_pos = (100 + curr_pos) * -1
    # elif curr_pos > 99:
    #     new_pos = curr_pos - distance
    # else:
    #     new_pos = curr_pos