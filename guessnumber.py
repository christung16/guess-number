import random

hi = 100
lo = 1
random_number = random.randint(lo, hi)
trial = 1

while (1):
    guess = int(input ("Guess a number: "))
    if (random_number > guess):
        lo = guess
    elif (random_number < guess):
        hi = guess
    else:
        print ("Bingo!!")
        print ("You've tried ", trial, " times")
        break
    print (lo, " to ", hi)
    trial=trial+1
