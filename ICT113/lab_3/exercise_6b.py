"""
A Head or Tail guessing game is played by tossing a coin and allowing the user to
guess either H or T.
Write separate programs for each version of the game. The versions have increasing
levels of complexity:

(for...range) The program starts by asking how many rounds the player wishes
to play the game. When all the rounds are over, display the number of times
the player made the correct guess.
How many rounds to play? : 5
Round 1: Head or Tail (H or T): H
Correct!
Round 2: Head or Tail (H or T): T
Wrong!
...
Round 5: Head or Tail (H or T): H
Correct!
You guess 3 correct out 5 rounds.
"""
from math import floor
import random

numOfTimes = int(input("How many rounds to play? : "))
numOfCorrectGuess = 0

for i in range(1, numOfTimes + 1, 1):
    quess = input("Round {0}: Head or Tail (H or T): ".format(i))

    # check for correct or incorrect guess
    isCorrectGuess = False
    randomInt = floor(random.randrange(0, 2))
    if randomInt == 1 and (quess == "T" or quess == "t"):
        isCorrectGuess = True
    elif randomInt == 1 and (quess == "H" or quess == "h"):
        isCorrectGuess = True
    
    # print the result
    if isCorrectGuess:
        print("Correct!")
        numOfCorrectGuess += 1
    else:
        print("Wrong!")
    
print("You have quessed {0} correct out of {1} rounds".format(numOfCorrectGuess, numOfTimes))
