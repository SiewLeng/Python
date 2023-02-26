"""
Solve computational problems using structured programming and apply data structures
in problem solving.
(a) Given the following list:
qtyPrice = [2, 1.5, 4, 0.5, 1, 2.5, 3, 2.0]
Each pair of value in the list represents a quantity and unit price. For example,
the first pair 2, 1.5 is 2 units at 1.5 per unit. Write a code segment using control
structures to display the subtotal and total price as follows:
2 x 1.5 = 3.0
4 x 0.5 = 2.0
1 x 2.5 = 2.5
3 x 2.0 = 6.0
4 items.
Total price $13.50
(15 marks)

(b) Given the following declaration,
numlist = []
Write a code segment that repeatedly prompts for integer values and inserts the
value to numlist. Program ends when the length of numlist is 5. The value must
be added in ascending order. Do not use any sort functions. Display the contents
of the list after each input. A sample execution of the program is as follows:
Enter num: 5
[5]
Enter num: 9
[5,9]
Enter num: 5
[5,5,9]
Enter num: 2
[2,5,5,9]
Enter num: 7
[2,5,5,7,9]
(10 marks)
"""

def question_3a():
    qtyPrice = [2, 1.5, 4, 0.5, 1, 2.5, 3, 2.0]
    numOfItem = 0
    totalPrice = 0
    for i in range(0, len(qtyPrice), 2):
        numOfItem += 1
        costOfItem = qtyPrice[i] * qtyPrice[i + 1]
        totalPrice += costOfItem
        print('{0} x {1} = {2}'.format(qtyPrice[i], qtyPrice[i + 1], costOfItem))
    print('{0} items.'.format(numOfItem))
    print('Total price ${0:.2f}.'.format(totalPrice))

def question_3b():
    numlist = []
    while(len(numlist) <= 4):
        num = int(input('Enter num: '))
        if len(numlist) == 0:
            numlist.append(num)
        else:
            isInsert = False
            for i in range(0, len(numlist), 1):
                if (num < numlist[i]):
                    numlist.insert(i, num)
                    isInsert = True
                    break
            if not isInsert:
                numlist.append(num)
        print(numlist)

question_3a()
question_3b()