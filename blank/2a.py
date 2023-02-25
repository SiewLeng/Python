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

list1 = [5, 47, 6, 32, 49, 30]
list2 = [5, 6, 7, 6, 45, 31]
list3 = [6, 45, 31]
list4 = [51, 47, 6, 32, 49, 30]

def printResult(list: list):
    print('tickerValidator({0}) >>> '.format(list), ticketValidator(list))
printResult(list1)
printResult(list2)
printResult(list3)
printResult(list4)
