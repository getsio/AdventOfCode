#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_6/example.txt", "r")
f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_6/input_data.txt", "r")

orbits = list()
endPoints = list()
orbFrom = list()
orbTo = list()

for line in f.readlines():
    orbs = tuple(line.rstrip().split(')'))
    orbits.append(orbs)
    orbFrom.append(orbs[0])
    orbTo.append(orbs[1])

def fromOrbTo(start, end, orbList):
    for i in range(len(orbList) - 1, -1, -1):
        if end == orbList[i][1]:
            #print(orbList[i])
            startPos = i
            break
    
    thisStart = orbList[startPos][0]
    counter = 1
    result = counter
    #print(orbList[i])

    for i in range(startPos, -1, -1):
        nextEnd = orbList[i - 1][1]

        if thisStart == nextEnd:
            #print(orbList[i - 1])
            thisStart = orbList[i - 1][0]
            counter += 1
            result += counter

        if orbList[i][0] == start:
            break

    print(counter)
    return counter
    #print(i)

for orb in orbTo:
    if not orb in orbFrom:
        endPoints.append(orb)

#print(len(endPoints))
start = orbits[0][0]
result = 0
#print(orbTo)
for point in orbTo:
    result += fromOrbTo(start, point, orbits)
#print(fromOrbTo(orbits[0][0], endPoints[0], orbits))

#print(result)