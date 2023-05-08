f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_10/input_data.txt", "r")

joltage_list = []
difference_one = 0
difference_three = 0

def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        if i < len(lst)-1 and lst[i+1] - lst[i] <= 3:
            m = lst[i]

            remLst = lst[:i] + lst[i+1:]

            for p in permutation(remLst):
                l.append([m] + p)
    return l

for line in f:
    joltage_list.append(int(line.rstrip()))

joltage_list.sort()
joltage_list.append(joltage_list[len(joltage_list)-1]+3)

print(joltage_list)

for i in range(len(joltage_list)):
    if i < len(joltage_list)-1:
        if joltage_list[i] + 1 == joltage_list[i+1]:
            difference_one += 1
        elif joltage_list[i] + 3 == joltage_list[i+1]:
            difference_three += 1
        
#print(difference_one, difference_three, difference_one * difference_three)
#print(joltage_list)

solution = {0:1}

for line in joltage_list:
    solution[line] = 0

    if line-1 in solution:
        solution[line] += solution[line-1]
    
    if line-2 in solution:
        solution[line] += solution[line-2]

    if line-3 in solution:
        print(line, line-3)
        solution[line] += solution[line-3]


print(solution)