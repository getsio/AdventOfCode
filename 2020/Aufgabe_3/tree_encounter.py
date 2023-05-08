f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_3/input_data.txt", "r")
lines = []
tree_cnt = 0

for line in f:
    lines.append(line.rstrip())

def get_slope_trees(lines, x_coord, y_coord):
    line_length = len(lines[0])
    tree_cnt_test = 0

    x = x_coord
    y = y_coord

    for i in range(y, len(lines), y):
        if lines[i][x] == '#':
            tree_cnt_test += 1
        x += x_coord
        if x > line_length-1:
            x -= line_length

    return tree_cnt_test

slope_1 = get_slope_trees(lines, 1, 1)
slope_2 = get_slope_trees(lines, 3, 1)
slope_3 = get_slope_trees(lines, 5, 1)
slope_4 = get_slope_trees(lines, 7, 1)
slope_5 = get_slope_trees(lines, 1, 2)

result = slope_1 * slope_2 * slope_3 * slope_4 * slope_5

print(slope_1, slope_2, slope_3, slope_4, slope_5, result)