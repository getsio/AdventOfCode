import itertools

f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_14/input_data.txt", "r")
mem = {}

def get_possible_ints(new_val):
    occ = new_val.count("X")
    combinations = list(itertools.product(["0","1"], repeat=occ))
    indexes = []

    for comb in combinations:
        val_copy = new_val
        for val in comb:
            val_copy = val_copy.replace("X", val, 1)
        indexes.append(int(val_copy, 2))

    return indexes

for line in f:
    line.rstrip()
    if "mask" in line:
        mask = line.split()[2]
    else:
        mem_list = line.split()
        mem_val = int(mem_list[2])
        mem_index = mem_list[0][4:-1]
        mem[mem_index] = mem_val

        mem_index_bin = bin(int(mem_index))[2:].zfill(36)
        new_val = ""

        for i in range(len(mem_index_bin)):
            if mask[i] == "X":
                new_val += "X"
            elif mask[i] == "1":
                new_val += mask[i]
            else:
                new_val += mem_index_bin[i]

        new_indexes = get_possible_ints(new_val)
        del mem[mem_index]
        for new_index in new_indexes:
            mem[new_index] = mem_val

#print(mem)
new_sum = 0

for key in mem:
    new_sum += mem[key]

print(new_sum)
