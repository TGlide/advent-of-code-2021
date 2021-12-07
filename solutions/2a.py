from utils import getInputFileLines


pos = 0
depth = 0
for line in getInputFileLines('2'):
    command, value = line.split()
    if command == 'forward':
        pos += int(value)
    elif command == 'down':
        depth += int(value)
    elif command == 'up':
        depth -= int(value)

print(pos, depth, pos * depth)
