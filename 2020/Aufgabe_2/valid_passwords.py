f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_2/input_data.txt", "r")
password_list = []
min_val = []
max_val = []
s_char = []
valid_pw_counter = 0

def count_char(input_string, input_char):
    counter = 0

    for char in input_string:
        if char == input_char:
            counter += 1
    
    return counter

def check_position(input_string, input_char, pos_1, pos_2):
    b_pos1 = False
    b_pos2 = False

    if input_string[pos_1] == input_char:
        b_pos1 = True

    if input_string[pos_2] == input_char:
        b_pos2 = True

    if b_pos1 != b_pos2:
        return True

    return False

for line in f:
    line_list = line.split(':')
    recommendation_list = line_list[0].split(' ')
    value_list = recommendation_list[0].split('-')

    min_val.append(int(value_list[0]))
    max_val.append(int(value_list[1]))
    s_char.append(recommendation_list[1])
    password_list.append(line_list[1][1:].rstrip())


for i in range(len(password_list)):
    #char_counter = count_char(password_list[i], s_char[i])
    if check_position(password_list[i], s_char[i], min_val[i]-1, max_val[i]-1):
        valid_pw_counter += 1
    '''if char_counter >= min_val[i] and char_counter <= max_val[i]:
        valid_pw_counter += 1
        print(char_counter, min_val[i], max_val[i], s_char[i], password_list[i])'''

print(valid_pw_counter)
    