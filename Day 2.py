with open('input.txt') as f:
    all_commands = [line.strip() for line in f]
    all_commands = [command.split() for command in all_commands]


def get_depth_and_pos(lst):
    horizontal_pos = 0
    depth = 0
    for i in range(len(lst)):
        if lst[i][0] == "forward":
            horizontal_pos += int(lst[i][1])
        elif lst[i][0] == "down":
            depth += int(lst[i][1])
        else:
            depth -= int(lst[i][1])
    return horizontal_pos * depth

def get_depth_aim_pos(lst):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for i in range(len(lst)):
        if lst[i][0] == "forward":
            horizontal_pos += int(lst[i][1])
            depth += aim * int(lst[i][1]) 
        elif lst[i][0] == "down":
            aim += int(lst[i][1])
        else:
            aim -= int(lst[i][1])
    return horizontal_pos * depth
            

print(get_depth_and_pos(all_commands))
print(get_depth_aim_pos(all_commands))