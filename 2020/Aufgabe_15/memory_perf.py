import time

starting_numbers = (14,1,17,0,3,20)
numbers_spoken = {}
max_turns = 30000000
last_spoken = starting_numbers[0]
start_time = time.time()

for turn in range(max_turns):
    if turn < len(starting_numbers):
        numbers_spoken[last_spoken] = turn
        last_spoken = starting_numbers[turn]
    elif not last_spoken in numbers_spoken:
        numbers_spoken[last_spoken] = turn
        last_spoken = 0
    else:
        before_turn = numbers_spoken[last_spoken]
        numbers_spoken[last_spoken] = turn
        last_spoken = turn - before_turn

numbers_spoken[last_spoken] = turn
print("Result: " + str(last_spoken) + " after " + str("%.3f" % (time.time() - start_time)) + "s")