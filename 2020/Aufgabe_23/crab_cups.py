import time

#Beispiel: [3,8,9,1,2,5,4,6,7]
#Beispiel 2: [5,4,3,2,1]
#Input: [4,6,3,5,2,8,1,7,9]

labeling = [3,8,9,1,2,5,4,6,7]

current_cup = 0
cup_before = None

label_length = 1000000
given_length = 9

start = time.time()
curr_perc = 5

def enlarge_label(label):
    num = len(label) + 1
    while len(label) < 1000000:
        label.append(num)
        num += 1

def correct_range(curr):
    while curr >= label_length:
        curr -= label_length
    return curr

def get_string(label, curr):
    lab_str = ""
    for num in label:
        if curr == num:
            lab_str += "(" + str(num) + ") "
        else:
            lab_str += str(num) + " "

    return lab_str

def get_result(label):
    res = ""
    ind = correct_range(label.index(1) + 1)
    while len(res) < len(label)-1:
        res += str(label[ind])
        ind = correct_range(ind + 1)

    return res

enlarge_label(labeling)
moves = len(labeling)
print(labeling[-1])

for move in range(6):
    new_perc = int(move / moves * 100)
    if new_perc % 1 == 0 and new_perc != curr_perc:
        curr_perc = new_perc
        print("Aktuell: " + str(curr_perc) + "% --- Zeit vergangen: " + str(time.time() - start))
    

    #print("-- move " + str(move + 1) + " --")
    #print("cups: " + get_string(labeling, labeling[current_cup]))

    cup_one = correct_range(current_cup + 1)
    cup_two = correct_range(current_cup + 2)
    cup_three = correct_range(current_cup + 3)

    print(labeling[:10],labeling[-6:], labeling[current_cup], labeling[cup_one], labeling[cup_two], labeling[cup_three])

    one_val = labeling[cup_one]
    two_val = labeling[cup_two]
    three_val = labeling[cup_three]

    #print("pick up: " + str(one_val) + ", " + str(two_val) + ", " + str(three_val))

    curr_val = labeling[current_cup]
    destination_val = curr_val

    while destination_val in [curr_val, one_val, two_val, three_val]:
        destination_val -= 1
        if destination_val < 1:
            destination_val = label_length
        print(destination_val)

    #print(destination_val)

    labeling.remove(one_val)
    labeling.remove(two_val)
    labeling.remove(three_val)

    destination = labeling.index(destination_val)
    #print("destination: " + str(destination_val))

    if destination + 1 > len(labeling) - 3:
        labeling.append(one_val)
        labeling.append(two_val)
        labeling.append(three_val)
    else:
        labeling.insert(destination + 1, one_val)
        labeling.insert(destination + 2, two_val)
        labeling.insert(destination + 3, three_val)

    current_cup = correct_range(current_cup + 4)
    #print()
    

#print("-- final --")
#print("cups: " + get_string(labeling, labeling[current_cup]))
#print(get_result(labeling))

index_one = labeling.index(1)
#print(labeling[correct_range(index_one + 1)], labeling[correct_range(index_one + 2)])