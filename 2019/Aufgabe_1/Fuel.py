file = open("werte.txt")
fuel = file.readlines()
for i in range (len(fuel)):
    fuel[i] = int(fuel[i])//3-2
    summe = fuel[i]
    while summe > 0:
        summe = summe//3-2
        if summe < 0:
            summe = 0
        fuel[i] += summe

erg = sum(fuel)
print (erg)
file.close()

