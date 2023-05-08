f = open("C:/Ausbildung/Python/AdventOfCode/2021/Day_2/input.txt", "r")

directions = []

for line in f:
    line = line.strip().split(" ")
    direction = line[0]
    line = int(line[1])
    directions.append([direction, line])


def move(directions):
    horizontal = 0
    depth = 0

    for line in directions:
        if line[0] == 'forward':
            horizontal += line[1]
        elif line[0] == 'down':
            depth += line[1]
        elif line[0] == 'up':
            depth -= line[1]
    
    return horizontal * depth

def move_aim(directions):
    aim = 0
    horizontal = 0
    depth = 0

    for line in directions:
        if line[0] == 'forward':
            horizontal += line[1]
            depth += line[1] * aim
        elif line[0] == 'down':
            aim += line[1]
        elif line[0] == 'up':
            aim -= line[1]

    return horizontal * depth

print(move(directions))
print(move_aim(directions))