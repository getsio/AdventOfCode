#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_5/example.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_5/example2.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_5/example3.txt", "r")
f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_5/input_data.txt", "r")

#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_5/input_data2.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_5/gravExample.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_5/gravExample2.txt", "r")
#f = open("C:/Ausbildung/Python/AdventOfCode/2019/Aufgabe_5/gravExample3.txt", "r")

opcode = list(map(int, f.read().split(',')))
#print(opcode)
pos = 0

while pos < len(opcode):
    if opcode[pos] != 99:
        strCode = str(opcode[pos]).zfill(5)
        C = strCode[2]
        B = strCode[1]
        A = strCode[0]

        if C == '0':
            firstParameter = opcode[pos + 1]
        elif C == '1':
            firstParameter = pos + 1

        if strCode[3] == '0' and not (strCode[4] == '3' or strCode[4] == '4'):
            if B == '0':
                secondParameter = opcode[pos + 2]
            elif B == '1':
                secondParameter = pos + 2

        print(strCode, pos, opcode[firstParameter])
        if opcode[firstParameter] == 0:
            isZero = True
        else:
            isZero = False

    if strCode[3] == '0' and strCode[4] == '1':
        opcode[opcode[pos + 3]] = opcode[firstParameter] + opcode[secondParameter]
        pos += 4
    elif strCode[3] == '0' and strCode[4] == '2':
        opcode[opcode[pos + 3]] = opcode[firstParameter] * opcode[secondParameter]
        pos += 4
    elif strCode[3] == '0' and strCode[4] == '3':
        valInput = int(input("Input: "))
        #print(firstParameter)
        opcode[firstParameter] = valInput
        pos += 2
    elif strCode[3] == '0' and strCode[4] == '4':
        print("Instruction Output: " + str(opcode[firstParameter]) + " at position " + str(pos + 1))
        pos += 2
    elif strCode[3] == '0' and strCode[4] == '5':
        if not isZero:
            pos = opcode[secondParameter]
        else:
            pos += 3
    elif strCode[3] == '0' and strCode[4] == '6':
        if isZero:
            pos = opcode[secondParameter]
        else:
            pos += 3
    elif strCode[3] == '0' and strCode[4] == '7':
        if opcode[firstParameter] < opcode[secondParameter]:
            opcode[opcode[pos + 3]] = 1
        else:
            opcode[opcode[pos + 3]] = 0
        pos += 4
    elif strCode[3] == '0' and strCode[4] == '8':
        if opcode[firstParameter] == opcode[secondParameter]:
            opcode[opcode[pos + 3]] = 1
        else:
            opcode[opcode[pos + 3]] = 0
        pos += 4
    elif opcode[pos] == 99:
        break
    else:
        pos += 1
    #print(pos)

#print(opcode)