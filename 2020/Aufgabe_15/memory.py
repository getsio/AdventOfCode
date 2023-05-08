f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_15/input_data2.txt", "r")

end = 2020
starting_numbers = []
numbers_spoken = []
turn = 1

for line in f:
    numbers = line.split(",")
    for number in numbers:
        starting_numbers.append(int(number))

while True:
    if turn-1 < len(starting_numbers):
        numbers_spoken.append(starting_numbers[turn-1])
    else:
        if numbers_spoken.count(numbers_spoken[-1]) <= 1:
            #print(numbers_spoken.count(numbers_spoken[-1]), numbers_spoken, turn)
            numbers_spoken.append(0)
        else:      
            numbers_spoken.reverse()
            last_index = len(numbers_spoken)-1 - numbers_spoken[1:].index(numbers_spoken[0])
            numbers_spoken.reverse()
            numbers_spoken.append((turn-1) - (last_index))
    #print("Turn " + str(turn) + ": " + str(numbers_spoken[-1]))

    turn += 1
    if turn == 2021:
        break

print(numbers_spoken)