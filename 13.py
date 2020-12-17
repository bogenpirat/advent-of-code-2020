input = """1004345
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,379,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,557,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"""

earliestDeparture = int(input.splitlines()[0])
buses = [ int(x) for x in list(filter(lambda x: x != 'x', input.splitlines()[1].split(','))) ]
from copy import deepcopy
busLabels = deepcopy(buses)

# part 1

while min(buses) < earliestDeparture:
    for i, timestamp in enumerate(buses):
        if buses[i] < earliestDeparture:
            buses[i] += busLabels[i]

print('labels:', busLabels)
print('buses:', buses)
minTimestamp = min(buses)
minWaitIdx = buses.index(minTimestamp)
print(f'waiting time from {earliestDeparture}: bus {busLabels[minWaitIdx]} with {minTimestamp - earliestDeparture}mins')
print(f'solution: bus label * wait time = {busLabels[minWaitIdx] * (minTimestamp - earliestDeparture)}')
print()
# part 2

offsets = []
offset = 0
for c in input.splitlines()[1].split(','):
    if c == 'x':
        offset += 1
    else:
        offsets.append(offset)

print('labels:', busLabels)
print('offsets:', offsets)
