#!/usr/bin/python

def binary_search(number, lo, hi):
    trial = 1
    while (lo<=hi):
        guess= int((hi+lo)/2)
        if guess==number:
            return (guess, trial)
        elif guess < number:
            lo=guess+1
        else:
            hi=guess-1
        trial=trial+1
    return (-1, trial) # -1 means no number found

if __name__ == "__main__":
    lo = 1
    hi = 100
    number = int(input("What is a number in mind? "))
    result,trial = binary_search(number, lo, hi)
    if result == -1:
        print ("Cannot find the correct number!!! :( ")
    else:
        print ("Bingo!!! Your number is ", result)
        print ("I tried ", trial, " time(s)")