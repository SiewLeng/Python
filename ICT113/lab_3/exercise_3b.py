"""
(while, sentinel, for loop) Modify program in 3a to allow for multiple input. The program
ends when -1 is entered for the input. Example:
Enter number: 2
1 x 2 = 2
2 x 5 = 4
Enter number: 3
1 x 3 = 3
2 x 3 = 6
3 x 3 = 9
Enter number: -1
"""

inputNum = int(input("Enter an integer: "))
while (inputNum != -1):
    for i in range(1, inputNum + 1, 1):
        print ("{0} x {1} = {2}".format(i, inputNum, i * inputNum))
    inputNum = int(input("Enter an integer: "))