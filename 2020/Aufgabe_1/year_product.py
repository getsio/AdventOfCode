f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_1/input_data2.txt", "r")
nums = []
for number in f:
    nums.append(int(number[0:-1]))

nums.sort()

for i in range(len(nums)-1, -1, -1):
    if nums[i] + nums[0] > 2020:
        nums.remove(nums[i])
