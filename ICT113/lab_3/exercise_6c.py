"""
A Head or Tail guessing game is played by tossing a coin and allowing the user to
guess either H or T.
Write separate programs for each version of the game. The versions have increasing
levels of complexity:

(while) This version re-tosses the coin whenever the player makes a wrong
guess and allow the player to keep guessing until he make a correct guess.
Display the number of tosses the player takes to make a correct guess.
Head or Tail (H or T): H
Wrong!
Head or Tail (H or T): T
Wrong!
Head or Tail (H or T): H
Correct!
You got it in 3 tosses!
"""
from math import floor
import random

isCorrectGuess = False
numOfGuess = 0

while not isCorrectGuess:
    guess = input("Head or Tail (H or T): ")
    numOfGuess += 1
    # check for correct or incorrect guess
    randomInt = floor(random.randrange(0, 2))
    if randomInt == 1 and (guess == "T" or guess == "t"):
        isCorrectGuess = True
        print("Correct!")
    elif randomInt == 0 and (guess == "H" or guess == "h"):
        isCorrectGuess = True
        print("Correct!")
    else:
        isCorrectGuess = False
        print("Incorrect!")

print("You got it in {0} tosses".format(numOfGuess))