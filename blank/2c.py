# Python code in text format
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

#(c)
def printInstruction():
    """
    print instructions of Toto
    """
    instructions = [
        'Toto Menu',
        '1. Ticket Entry',
        '2. Quick Pick',
        '0. Exit'
    ]
    print('\n')
    for i in range (0, len(instructions), 1):
        print(instructions[i])

#(c)
def userSelectNumber():
    """
    Prompt the user to pick a number until a total of 6 numbers are picked.\n
    If the user does not enter a number, this entry is not valid and the user will be prompt to pick another number.\n
    Return a list of 6 numbers picked by user.
    """
    list = []
    noOfNumber = 6
    count = 1
    while (count <= 6):
        pick = input('Enter pick {0}: '.format(count))
        if (pick.isdigit()): 
            list.append(int(pick))
            count += 1
        else:
            print('Invalid pick entered!')

    return list

#(c)
def bettingApp():
    """
    Print the Toto Menu which prompts user to enter option until user enter 0 to exit.\n
    If option is 1, allow user to enter 6 picks for Toto and check these 6 picks form a valid ticket.\n
    If option is 2, generate 6 unique numbers between 1 and 49.
    """
    printInstruction()
    option = input('Enter option: ')
    while (option != '0'):
        if (option == '1'):
            list = userSelectNumber()
            if (ticketValidator(list)):
                print('Your TOTO ticket {0} is valid'.format(list))
            else:
                print('{0} is an Invalid TOTO ticket'.format(list))
        elif(option == '2'):
            list = list = quickPick()
            print('This is your lucky ticket: {0}'.format(list))
        printInstruction()
        option = input('Enter option: ')
    print('Good luck to you!!')

bettingApp()
