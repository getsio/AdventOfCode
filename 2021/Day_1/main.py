f = open("C:/Ausbildung/Python/AdventOfCode/2021/Day_1/input.txt", "r")
measurements = []

for line in f:
    measurements.append(int(line.strip()))

def getIncreased(measurements):
    increases = 0
    number_before = 0

    for i in range(len(measurements)):
        if i > 0 and measurements[i] > number_before:
            increases += 1
        number_before = measurements[i]

    return increases

def getThreeMeasurement(measurements):
    increases = 0
    number_before = 0

    for i in range(0, len(measurements) - 2):
        number = measurements[i] + measurements[i+1] + measurements[i+2]

        if i > 0 and number > number_before:
            increases += 1
        number_before = number
    
    return increases
            

print(getIncreased(measurements))
print(getThreeMeasurement(measurements))