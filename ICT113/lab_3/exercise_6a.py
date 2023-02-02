"""
A Head or Tail guessing game is played by tossing a coin and allowing the user to
guess either H or T.
Write separate programs for each version of the game. The versions have increasing
levels of complexity:

(if...else) The program uses a random function to generate either H or T. User
makes a guess, and the outcome is displayed:
Head or Tail (H or T): H
Correct!
(User can key his guess in uppercase or lowercase(that is, H or h or T or t).
Any letter other than H or T is considered as an incorrect guess.
"""
from math import floor
import random

guess = input("Head or Tail (H or T): ")
randomInt = floor(random.randrange(0, 2))

if randomInt == 1 and (guess == 'T' or guess == 't'):
    print("Correct!")
elif randomInt == 0 and (guess == 'H' or guess == 'h'):
    print("Correct!")
else:
    print("Incorrect!")


