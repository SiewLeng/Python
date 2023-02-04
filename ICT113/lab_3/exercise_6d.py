"""
(nested while loop) Modify the program in part c). After the player guesses
correctly, prompt the player whether he wishes to play again with this prompt:
“do you want to play again? (y/n)”. If yes, repeat the whole process.
Head or Tail (H or T): H
Wrong!
Head or Tail (H or T): T
Wrong!
Head or Tail (H or T): H
Correct!
You got it in 3 tosses!
Play again? (y/n): y
Head or Tail (H or T): H
You got it in 2 tosses!
Play again? (y/n): n
Program end
"""

from math import floor
import random

isCorrectGuess = False
continueGame = True

while continueGame:
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

    toPlayGame = input("Play again? (y/n): ")
    if toPlayGame == "Y" or toPlayGame == "y":
        continueGame = True
        isCorrectGuess = False
    else:
        continueGame = False
        isCorrectGuess = False
