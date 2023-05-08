f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_14/input_data2.txt", "r")
mem = {}

for line in f:
    line.rstrip()
    if "mask" in line:
        mask = line.split()[2]
    else:
        mem_list = line.split()
        mem_index = mem_list[0][4:-1]
        mem[mem_index] = bin(int(mem_list[2]))[2:].zfill(36)

        #print(mem[mem_index], int(mem[mem_index], 2))
        #print(mask)
        new_val = ""

        for i in range(len(mem[mem_index])):
            if mask[i] == "X":
                new_val += mem[mem_index][i]
            else:
                new_val += mask[i]

        #print(new_val, int(new_val, 2))
        mem[mem_index] = int(new_val, 2)
        #print()

#print(mask)
#print(mem)
new_sum = 0

for key in mem:
    new_sum += mem[key]

print(new_sum)