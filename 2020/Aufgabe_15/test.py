import time

puzzleInput = (0,3,6)
answers = {}
numCheck = puzzleInput[0]
start = time.time()

for turn in range(30000000):
    if turn < len(puzzleInput):                                                 
        answers[numCheck] = turn
        numCheck = puzzleInput[turn]
    elif numCheck not in answers:          
        #print(f"Not in numbers {numCheck}")
        answers[numCheck] = turn
        numCheck = 0
    elif numCheck in answers:
        #print(f"In numbers: {numCheck}")
        lastOccurance = answers[numCheck]
        
        #Add number from before to the list of numbers said (turn-1)
        answers[numCheck] = turn
        
        #Search for new number by saying how many turns apart the number is from when it previously has been spoken
        numCheck = turn - lastOccurance
        #print(f"New number: {numCheck}")

print("Result after " + str(time.time()-start) + "s :" + str(numCheck))