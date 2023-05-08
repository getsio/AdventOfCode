f = open("C:/Ausbildung/Python/AdventOfCode/2021/Day_4/test_input.txt", "r")
numbers = f.readline().strip().split(",")
f.readline()
bingo_fields = []
bingo_field = []

for line in f:
  if line != '\n':

    if line[0] == ' ':
      line = line[1:]

    line = line.strip("\n").replace("  ", " ")
    line = line.split(" ")
    bingo_field.append(line)
  else:
    bingo_fields.append(bingo_field)
    bingo_field = []

bingo_fields.append(bingo_field)


print(numbers)
print()

for field in bingo_fields:
  for bingo in field:
    print(bingo)
  print()