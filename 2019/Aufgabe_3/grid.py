#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_3/input_data.txt", "r")
f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_3/example.txt", "r")

lanes = list()

for line in f:
    coordinates = [[0, 0]]
    line = line.rstrip().split(",")

    for instruction in line:
        direction = instruction[0]
        val = int(instruction[1:])

        valX = 0
        valY = 0

        if direction == 'R':
            valY = 1
        elif direction == 'L':
            valY = -1
        elif direction == 'U':
            valX = 1
        elif direction == 'D':
            valX = -1
        
        lastCoords = coordinates[len(coordinates) - 1]

        for x in range(1, val + 1):
            coordinates.append([valX * x + lastCoords[0], valY * x + lastCoords[1]])

    lanes.append(coordinates)

manhattanDistance = 0
chosen = lanes[0]
other = lanes[1]

for length in range(1, len(chosen)):
    if chosen[length] in other:
        newDistance = abs(chosen[length][0]) + abs(chosen[length][1])

        if manhattanDistance == 0 or newDistance < manhattanDistance:
            manhattanDistance = newDistance

print(manhattanDistance)
