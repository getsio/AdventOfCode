f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_12/ip.txt", "w")
f.write("")
f.close()

f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_12/ip.txt", "a")

counter = 1
ip_str = "195.240.72."

for i in range(16):
    bin_str_1 = str(int(bin(i)[2:].zfill(4) + bin(0b0000)[2:].zfill(4), 2))
    bin_str_2 = str(int(bin(i)[2:].zfill(4) + bin(0b1111)[2:].zfill(4), 2))

    if counter < 10:
        counter_str = " " + str(counter)
    else:
        counter_str = str(counter)

    output_str = "Netz " + counter_str + ": " + ip_str + bin_str_1 + " - " + ip_str + bin_str_2
    f.write(output_str + "\n")

    counter += 1

f.close()