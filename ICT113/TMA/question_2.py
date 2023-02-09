from math import floor
import random

#(a)
def isBetween1And49(list):
    result = True
    for i in range (0, len(list), 1):
        if (list[i] < 1 or list[i] > 49):
            result = False
            break
    return result

#(a)
def isUnique(list):
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
def ticketValidator(list):
    result = True
    if (len(list) != 6):
        result = False
    elif (not isBetween1And49(list)):
        result = False
    elif(not isUnique(list)):
        result = False
    return result

#(b)
def isNumDiffFromList(list, number):
    result = True
    for i in range (0, len(list), 1):
        if (number == list[i]):
            result = False
            break
    return result

#(b) 
def quickPick():
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
    instructions = [
        'Toto Menu',
        '1. Ticket Entry',
        '2. Quick Pick',
        '0. Exit'
    ]
    for i in range (0, len(instructions), 1):
        print(instructions[i])

#(c)
def userSelectNumber():
    list = []
    noOfNumber = 6
    for i in range (0, noOfNumber, 1):
        list.append(int(input('Enter pick {0}:'.format(i + 1))))
    return list

#(c)
def bettingApp():
    printInstruction()
    option = input('Enter option:')
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
        option = input('Enter option:')
    print('Good luck to you!!')

bettingApp()

