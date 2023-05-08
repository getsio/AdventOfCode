f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_4/example.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_4/example2.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_4/example3.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_4/input_data.txt", "r")

exampleOne = "111111"
exampleTwo = "223450"
exampleThree = "123789"

startingPoint = "234208"
endPoint = "765869"

passwordCounter = 0

for value in range(int(startingPoint), int(endPoint) + 1):
    numberString = str(value)
    adjDigits = False
    pos = 0

    while pos < len(numberString) - 1:
        if not adjDigits and numberString.count(numberString[pos]) == 2:
            adjDigits = True

        if not(int(numberString[pos + 1]) >= int(numberString[pos])):
            break

        pos += 1

    if pos == 5 and adjDigits:
        passwordCounter += 1

print(passwordCounter)