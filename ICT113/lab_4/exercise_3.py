"""
(List) Write a program to record the statistics of 100 throws of a dice.
Use an initial list as follows to record the occurrences of each value of the dice:
diceCount = [0, 0, 0, 0, 0, 0, 0]
The element at index 0 of the list will not be used. When the dice value is 1, add 1 to
index 1 of the list etc. After 100 throws of the dice, display a summary of the
occurrences of the dice values as follows:
Dice Occurrence
1 16
2 14
3 15
4 17
5 18
6 20
Total 100
"""

import random
from math import floor

diceCount = [0, 0, 0, 0, 0, 0, 0]
total = 0

for i in range(1, 101, 1):
    #generate random number between 1 to 6
    diceNumber = floor(random.random() * 6) + 1 
    diceCount[diceNumber] += 1
    total += 1

print("{0:<8} {1:<0}".format("Dice", "Occurrence"))

for i in range(1, 7, 1):
    print("{0:<8} {1:<0}".format(i, diceCount[i]))

print("{0:<8} {1:<0}".format("Total", total))