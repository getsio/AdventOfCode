f = open("C:/Ausbildung/Python/AdventOfCode/2021/Day_3/test_input.txt", "r")
statuscode = []
sortedcode = []

for line in f:
    line = line.strip()
    statuscode.append(line.strip())

for char in statuscode[0]:
    sortedcode.append([])

for status in statuscode:
    for i in range(len(status)):
        sortedcode[i].append(status[i])

print(sortedcode)

def count_numbers(list):
    ones = 0
    zeroes = 0
    for number in list:
        if number == '1':
            ones += 1
        else:
            zeroes += 1

    return '1' if ones > zeroes else '0'

teststring = ""

for arr in sortedcode:
    teststring += count_numbers(arr)

print(teststring, bin('0b' + teststring)^bin('0b' + teststring))