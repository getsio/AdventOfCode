f = open("C:/Ausbildung/Python/AdventOfCode/2021/Day_5/input.txt", "r")
f = open("C:/Ausbildung/Python/AdventOfCode/2021/Day_5/example.txt", "r")

bingoNumbers = f.readline().strip().split(',')

f.readline()

fields = []
bingoField = []

for line in f:
  line.strip()
  if line != '\n':
    bingoRow = line.strip().split()
    bingoField.append(bingoRow)
  else:
    fields.append(bingoField)

print(fields)