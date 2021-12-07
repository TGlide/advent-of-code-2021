import os

from utils import getInputFileLines

# Each window has 3 numbers max
windows = []

for line in getInputFileLines('1'):
    num = int(line.replace('\n', ''))
    windows.append([])
    for window in windows:
        if len(window) < 3:
            window.append(num)

previous = None
times_increased = 0
for window in [sum(w) for w in windows if len(w) == 3]:
    if previous is not None and window > previous:
        times_increased += 1
    previous = window

print(times_increased)
