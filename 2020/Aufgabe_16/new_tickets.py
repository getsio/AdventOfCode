import time

f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_16/input3.txt", "r")
new_rules = {}
fitting_keys = {}
final_keys = {}
my_ticket = []
nearby_tickets = []
start = time.time()

valid_tickets = []
invalid_tickets = []
invalid_numbers = []

for line in f:
    if ":" in line and "your" not in line and "nearby" not in line:
        line_split = line.rstrip().split(":")
        line = line_split[1].split(" ")
        first = line[1].split("-")
        second = line [3].split("-")
        new_rule = [int(first[0]), int(first[1]), int(second[0]), int(second[1])]
        new_rules[line_split[0]] = new_rule
    elif "your" in line:
        my_ticket = f.readline().rstrip().split(",")
        for i in range(len(my_ticket)):
            my_ticket[i] = int(my_ticket[i])
    else:
        if not "nearby" in line and line != "\n":
            line = line.rstrip().split(",")
            line_list = []
            for number in line:
                line_list.append(int(number))
            nearby_tickets.append(line_list)

print("Rules:\n" + str(new_rules) + "\n")
print("My Ticket:\n" + str(my_ticket) + "\n")
print("Nearby Tickets:\n" + str(nearby_tickets))
# ----------------------------------------------------------------------------------------

for n_ticket in nearby_tickets:
    valid_counter = 0
    for number in n_ticket:
        invalid_number = True
        
        for key in new_rules:
            if new_rules[key][0] <= number <= new_rules[key][1] or new_rules[key][2] <= number <= new_rules[key][3]:
                invalid_number = False
                valid_counter += 1
                break
        
        if invalid_number:
            invalid_numbers.append(number)
    if valid_counter == len(n_ticket):
        valid_tickets.append(n_ticket)


for key in new_rules:
    fitting_keys[key] = []

    for i in range(len(valid_tickets[0])):
        col = 0
        fit_cnt = 0
        while col < len(valid_tickets):
            if new_rules[key][0] <= valid_tickets[col][i] <= new_rules[key][1] or new_rules[key][2] <= valid_tickets[col][i] <= new_rules[key][3]:
                fit_cnt += 1
            else:
                break
            col += 1

            if fit_cnt == len(valid_tickets):
                fitting_keys[key].append(i)


#print(fitting_keys)
while len(final_keys) != len(new_rules):
    for keys in fitting_keys:
        if len(fitting_keys[keys]) == 1:
            remove_col = fitting_keys[keys][0]
            del fitting_keys[keys]
            final_keys[keys] = remove_col
            break

    for keys in fitting_keys:
        if remove_col in fitting_keys[keys]:
            fitting_keys[keys].remove(remove_col)


print(final_keys)
#print(my_ticket[final_keys['class']], my_ticket[final_keys['row']], my_ticket[final_keys['seat']])
#print(my_ticket[final_keys['departure location']] * my_ticket[final_keys['departure station']] * my_ticket[final_keys['departure platform']] *
#my_ticket[final_keys['departure track']] * my_ticket[final_keys['departure date']] * my_ticket[final_keys['departure time']])
print("Time taken: " + str(time.time() - start))