from utils import getInputFileLines


pos = 0
depth = 0
aim = 0
for line in getInputFileLines('2'):
    command, value = line.split()
    if command == 'forward':
        pos += int(value)
        depth += aim * int(value)
    elif command == 'down':
        aim += int(value)
    elif command == 'up':
        aim -= int(value)

print(pos, depth, pos * depth)
