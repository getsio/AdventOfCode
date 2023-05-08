import copy

f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_11/input_data.txt", "r")
seat_list = []
change_counter = 1

for line in f:
    seat_list.append(list(line.rstrip()))

def change_seats(lst):
    n_lst = copy.deepcopy(lst)
    change_cnt = 0
    around_lst = []

    def check_around(col, row):
        for n_row in range(row-1, row+2):
            for n_col in range(col-1, col+2):
                if n_row != row and n_col != col:
                    if n_row >= 0 and n_col >= 0 and n_row < len(lst) and n_col < len(lst[n_row]):
                        #print(lst[n_col][n_row])
                        around_lst.append(lst[n_row][n_col])

    def check_directions(row, col):
        for n_row in range(row-1, -1, -1):
            if lst[n_row][col] == 'L' or lst[n_row][col] == '#':
                around_lst.append(lst[n_row][col])
                break

        n_col = col + 1
        for n_row in range(row-1, -1, -1):
            if n_col < len(lst[n_row]):
                if lst[n_row][n_col] == 'L' or lst[n_row][n_col] == '#':
                        around_lst.append(lst[n_row][n_col])
                        stop = True
                        break
                n_col += 1
            else:
                break

        for n_col in range(col+1, len(lst[row])):
            if lst[row][n_col] == 'L' or lst[row][n_col] == '#':
                around_lst.append(lst[row][n_col])
                break

        n_col = col + 1
        for n_row in range(row+1, len(lst)):
            if n_col < len(lst[n_row]):
                if lst[n_row][n_col] == 'L' or lst[n_row][n_col] == '#':
                    around_lst.append(lst[n_row][n_col])
                    break
                n_col += 1
            else:
                break

        for n_row in range(row+1, len(lst)):
            if lst[n_row][col] == 'L' or lst[n_row][col] == '#':
                around_lst.append(lst[n_row][col])
                break

        n_col = col - 1
        for n_row in range(row+1, len(lst)):
            if n_col >= 0:
                if lst[n_row][n_col] == 'L' or lst[n_row][n_col] == '#':
                    around_lst.append(lst[n_row][n_col])
                    break
                n_col -= 1
            else:
                break

        for n_col in range(col-1, -1, -1):
            if lst[row][n_col] == 'L' or lst[row][n_col] == '#':
                around_lst.append(lst[row][n_col])
                break

        n_col = col - 1
        for n_row in range(row-1, -1, -1):
            if n_col >= 0:
                if lst[n_row][n_col] == 'L' or lst[n_row][n_col] == '#':
                    around_lst.append(lst[n_row][n_col])
                    break
                n_col -= 1
            else:
                break

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            #check_around(i, j)
            check_directions(i, j)
            #print(around_lst)
            #print(around_lst)
            if lst[i][j] == 'L':
                if not '#' in around_lst:
                    change_cnt += 1
                    n_lst[i][j] = '#'
            elif lst[i][j] == '#':
                occ_cnt = 0
                for char in around_lst:
                    if char == '#':
                        occ_cnt += 1

                if occ_cnt >= 5:
                    change_cnt += 1
                    n_lst[i][j] = 'L'

            around_lst = []
    
    return change_cnt, n_lst

def count_occupied(lst):
    occ_cnt = 0

    for line in lst:
        for char in line:
            if char == '#':
                occ_cnt += 1

    return occ_cnt

def print_line(lst):
    for line in lst:
        for char in line:
            print(char, end="")
        print("")
    print()

while change_counter != 0:
    print_line(seat_list)
    new_list = []
    change_counter, new_list = change_seats(seat_list)
    seat_list = copy.deepcopy(new_list)
    print(change_counter)

print()
print(count_occupied(seat_list))
#print(len(seat_list[0]))