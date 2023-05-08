f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_1/input_data2.txt", "r")
year_list = []
for years in f:
    year_list.append(int(years[0:-1]))

i = 0

while i < len(year_list):
    for years in year_list:
        for year in year_list:
            if year_list[i] + years + year == 2020:
                print(year_list[i] * years * year)
    i += 1
