input = """..#..##.
#.....##
##.#.#.#
..#...#.
.###....
######..
.###..#.
..#..##."""

input2 = """.#.
..#
###"""

# part 1

cycles = [[]]

for i, line in enumerate(input.splitlines()): # input
    z = 0
    for j, c in enumerate(line):
        if c == '#':
            x = j
            y = i
            z = 0
            cycles[0].append((x, y, z))

def print_cycle(cycle):
    for z in range(min([cube[2] for cube in cycle]), max([cube[2] for cube in cycle]) + 1): # z: different pages
        print(f'z={z}:')
        for y in range(min([cube[1] for cube in cycle]), max([cube[1] for cube in cycle]) + 1):
            for x in range(min([cube[0] for cube in cycle]), max([cube[0] for cube in cycle]) + 1):
                print('#' if (x, y, z) in cycle else '.', end='')
            print()
        print()

print_cycle(cycles[0])

def get_neighbor_coordinates(x, y, z):
    neighbors = []

    for xi in range(x - 1, x + 2):
        for yi in range(y - 1, y + 2):
            for zi in range(z - 1, z + 2):
                if not (xi == x and yi == y and zi == z):
                    neighbors.append((xi, yi, zi))

    return neighbors

for i in range(1, 6 + 1): # boot-up cycles
    newGrid = []
    lastGrid = cycles[i - 1]

    minX = min([t[0] for t in lastGrid]) - 1
    maxX = max([t[0] for t in lastGrid]) + 1
    minY = min([t[1] for t in lastGrid]) - 1
    maxY = max([t[1] for t in lastGrid]) + 1
    minZ = min([t[2] for t in lastGrid]) - 1
    maxZ = max([t[2] for t in lastGrid]) + 1

    for xi in range(minX, maxX + 1):
        for yi in range(minY, maxY + 1):
            for zi in range(minZ, maxZ + 1):
                neighborCoords = get_neighbor_coordinates(xi, yi, zi)
                neighborCount = 0
                
                for neighbor in neighborCoords:
                    if neighbor in lastGrid:
                        neighborCount += 1

                active = (xi, yi, zi) in lastGrid

                if active and neighborCount in [2, 3]:
                    newGrid.append((xi, yi, zi))
                elif active:
                    pass # deactivate the cube
                elif not active and neighborCount == 3:
                    newGrid.append((xi, yi, zi))
                
    cycles.append(newGrid)
    #print(f'after {i} cycles:\n')
    #print_cycle(newGrid)

for i, cycle in enumerate(cycles):
    #print(cycle)
    print(f'len(cycle[{i}])={len(cycle)}')



# part 2

cycles = [[]]

for i, line in enumerate(input.splitlines()): # input
    for j, c in enumerate(line):
        if c == '#':
            x = j
            y = i
            z = 0
            w = 0
            cycles[0].append((x, y, z, w))

def get_neighbor_coordinates_4d(x, y, z, w):
    neighbors = []

    for xi in range(x - 1, x + 2):
        for yi in range(y - 1, y + 2):
            for zi in range(z - 1, z + 2):
                for wi in range(w - 1, w + 2):
                    if not (xi == x and yi == y and zi == z and wi == w):
                        neighbors.append((xi, yi, zi, wi))

    return neighbors

for i in range(1, 6 + 1): # boot-up cycles
    newGrid = []
    lastGrid = cycles[i - 1]

    minX = min([t[0] for t in lastGrid]) - 1
    maxX = max([t[0] for t in lastGrid]) + 1
    minY = min([t[1] for t in lastGrid]) - 1
    maxY = max([t[1] for t in lastGrid]) + 1
    minZ = min([t[2] for t in lastGrid]) - 1
    maxZ = max([t[2] for t in lastGrid]) + 1
    minW = min([t[3] for t in lastGrid]) - 1
    maxW = max([t[3] for t in lastGrid]) + 1

    for xi in range(minX, maxX + 1):
        for yi in range(minY, maxY + 1):
            for zi in range(minZ, maxZ + 1):
                for wi in range(minW, maxW + 1):
                    neighborCoords = get_neighbor_coordinates_4d(xi, yi, zi, wi)
                    neighborCount = 0
                    
                    for neighbor in neighborCoords:
                        if neighbor in lastGrid:
                            neighborCount += 1

                    active = (xi, yi, zi, wi) in lastGrid

                    if active and neighborCount in [2, 3]:
                        newGrid.append((xi, yi, zi, wi))
                    elif active:
                        pass # deactivate the cube
                    elif not active and neighborCount == 3:
                        newGrid.append((xi, yi, zi, wi))
    
    print(f'finished cycle {i}')
    cycles.append(newGrid)

for i, cycle in enumerate(cycles):
    print(f'len(cycle[{i}])={len(cycle)}')