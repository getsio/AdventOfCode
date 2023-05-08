f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_12/input_data2.txt", "r")

instructions = []
direction = "E"

direction_key_1 = 1
direction_key_2 = 0
direction_key = 1

directions = ["N", "E", "S", "W"]
turn = ["L", "R"]

pos_x = 0
pos_y = 0

waypoint_one = 10
waypoint_two = 1

def correct_key(key):
    if key > 3:
        while key > 3:
            key -= 4
    elif key < 0:
        while key < 0:
            key += 4

    return key


for line in f:
    instructions.append(line.rstrip())

for line in instructions:
    new_direction = line[0]
    move_val = int(line[1:])

    if new_direction in directions:
        if new_direction == "N" and directions[direction_key_1] == "N":
            #pos_y += move_val
            waypoint_one += move_val
        elif new_direction == "E" and directions[direction_key_1] == "E":
            #pos_x += move_val
            waypoint_one += move_val
        elif new_direction == "S" and directions[direction_key_1] == "S":
            #pos_y -= move_val
            waypoint_one += move_val
        elif new_direction == "W" and directions[direction_key_1] == "W":
            #pos_x -= move_val
            waypoint_one += move_val

        if new_direction == "N" and directions[direction_key_2] == "N":
            #pos_y += move_val
            waypoint_two += move_val
        elif new_direction == "E" and directions[direction_key_2] == "E":
            #pos_x += move_val
            waypoint_two += move_val
        elif new_direction == "S" and directions[direction_key_2] == "S":
            #pos_y -= move_val
            waypoint_two += move_val
        elif new_direction == "W" and directions[direction_key_2] == "W":
            #pos_x -= move_val
            waypoint_two += move_val

    elif new_direction in turn:
        move_val /= 90

        if new_direction == "L":
            move_val *= -1

        #direction_key = correct_key(direction_key + int(move_val))
        direction_key_1 = correct_key(direction_key_1 + int(move_val))
        direction_key_2 = correct_key(direction_key_2 + int(move_val))

        #direction = directions[direction_key]

    elif new_direction == 'F':
        '''if direction == "N":
            pos_y += move_val
        elif direction == "E":
            pos_x += move_val
        elif direction == "S":
            pos_y -= move_val
        elif direction == "W":
            pos_x -= move_val'''

        if directions[direction_key_1] == "N":
            pos_x += move_val * waypoint_one
        elif directions[direction_key_1] == "E":
            pos_y += move_val * waypoint_one
        elif directions[direction_key_1] == "S":
            pos_x -= move_val * waypoint_one
        elif directions[direction_key_1] == "W":
            pos_y -= move_val * waypoint_one

        if directions[direction_key_2] == "N":
            pos_x += move_val * waypoint_two
        elif directions[direction_key_2] == "E":
            pos_y += move_val * waypoint_two
        elif directions[direction_key_2] == "S":
            pos_x -= move_val * waypoint_two
        elif directions[direction_key_2] == "W":
            pos_y -= move_val * waypoint_two
        


print(pos_x, pos_y, abs(pos_x) + abs(pos_y))