import os

from utils import getInputFileLines

previous = None
times_increased = 0

for line in getInputFileLines('1'):
    current = int(line.replace('\n', ''))
    if previous is not None and current > previous:
        times_increased += 1
    previous = current

print(times_increased)
