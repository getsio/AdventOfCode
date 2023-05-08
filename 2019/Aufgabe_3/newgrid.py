def getMinMax(valOne, valTwo):
    if valOne <= valTwo:
        return valOne, valTwo
    else:
        return valTwo, valOne

def getManhattanDistance(inputList):
    manhattanDistance = 0
    for coords in inputList:
        newDistance = abs(coords[0]) + abs(coords[1])
        if manhattanDistance == 0 or newDistance < manhattanDistance:
            manhattanDistance = newDistance
    return manhattanDistance

f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_3/input_data.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_3/example.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_3/example2.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_3/example3.txt", "r")
lanes = list()

for line in f:
    line = line.rstrip().split(',')
    coordinates = [(0, 0)]

    for instruction in line:
        direction = instruction[0]
        moveVal = int(instruction[1:])

        valX = 0
        valY = 0

        lastPosition = coordinates[len(coordinates) - 1]

        if direction == 'R':
            valY = 1
        elif direction == 'L':
            valY = -1
        elif direction == 'U':
            valX = 1
        elif direction == 'D':
            valX = -1

        newPosition = (valX * moveVal + lastPosition[0], valY * moveVal + lastPosition[1])
        coordinates.append(newPosition)
    
    lanes.append(coordinates)

'''for lane in lanes:
    print(lane)'''

intersection = list()
steps = list()
stepsOne = 0

for i in range(1, len(lanes[0])):
    #print(lanes[0][i])
    actualLane = lanes[0][i]
    stepsTwo = 0

    xBefore = lanes[0][i-1][0]
    yBefore = lanes[0][i-1][1]

    xSmall, xBig = getMinMax(lanes[0][i-1][0], actualLane[0])
    ySmall, yBig = getMinMax(lanes[0][i-1][1], actualLane[1])
    
    #print(xSmall, xBig)
    #print(ySmall, yBig)

    for j in range(1, len(lanes[1])):
        actualLaneNew = lanes[1][j]

        xBeforeNew = lanes[1][j-1][0]
        yBeforeNew = lanes[1][j-1][1]

        xSmallNew, xBigNew = getMinMax(lanes[1][j-1][0], actualLaneNew[0])
        ySmallNew, yBigNew = getMinMax(lanes[1][j-1][1], actualLaneNew[1])

        stepsOneNew = stepsOne

        if xSmall < actualLaneNew[0] < xBig and ySmallNew < actualLane[1] < yBigNew:
            intersection.append((actualLaneNew[0], actualLane[1]))

            pathOne = abs(xBefore - actualLaneNew[0])
            pathTwo = abs(yBeforeNew - actualLane[1])

            stepsOneNew += pathOne
            stepsTwo += pathTwo
            steps.append((stepsOneNew, stepsTwo))

        elif ySmall < actualLaneNew[1] < yBig and xSmallNew < actualLane[0] < xBigNew:
            intersection.append((actualLane[0], actualLaneNew[1]))

            pathOne = abs(yBefore - actualLaneNew[1])
            pathTwo = abs(xBeforeNew - actualLane[0])

            stepsOneNew += pathOne
            stepsTwo += pathTwo
            steps.append((stepsOneNew, stepsTwo))

        stepsTwo += xBigNew - xSmallNew
        stepsTwo += yBigNew - ySmallNew
    stepsOne += xBig - xSmall
    stepsOne += yBig - ySmall

print(getManhattanDistance(intersection))
print(steps[0][0] + steps[0][1])