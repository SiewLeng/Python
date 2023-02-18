from math import floor
import random

#(a)
def isBetween1And49(list: list):
    """
    validate each of item in the list is between 1 and 49.
    """
    result = True
    for i in range (0, len(list), 1):
        if (list[i] < 1 or list[i] > 49):
            result = False
            break
    return result

#(a)
def isUnique(list: list):
    """
    validate all the item in the list is unique.
    """
    result = True
    for i in range (0, len(list) - 1, 1):
        for n in range (i + 1, len(list), 1):
            if (list[i] == list[n]):
                result = False
                break
        if (not result):
            break
    return result

#(a)
def ticketValidator(list: list):
    """
    validate length of list is 6.\n
    validate each of item in the list is between 1 and 49.\n
    validate all the item in the list is unique.
    """
    result = True
    if (len(list) != 6):
        result = False
    elif (not isBetween1And49(list)):
        result = False
    elif(not isUnique(list)):
        result = False
    return result

#(b)
def isNumDiffFromList(list: list, number: int):
    """
    validate that the number is different from all the items in list.
    """
    result = True
    for i in range (0, len(list), 1):
        if (number == list[i]):
            result = False
            break
    return result

#(b) 
def quickPick():
    """
    Return a list of 6 unique numbers between 1 and 49.
    """
    list = []
    noOfNumber = 6
    max = 49
    min = 1
    for i in range (0, noOfNumber, 1):
        randomNum = floor(random.random() * (max - min + 1)) + min
        while (not isNumDiffFromList(list, randomNum)):
            randomNum = floor(random.random() * (max - min + 1)) + min
        list.append(randomNum)
    return list

def main():
    for i in range(3):
        list = quickPick()
        print('QuickPick: ', list)
        print('ticketValidator({0}) >>>> '.format(list), ticketValidator(list))
main()