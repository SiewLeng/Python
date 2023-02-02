"""
(while, sentinel loop) Write a program that displays the menu shown in the example
run repeatedly until the user chooses 0 to quit. You may assume that user enters only
valid numbers (0-3).
Menu
1. Option 1
2. Option 2
3. Option 3
0. Quit
Enter choice: 1
Option 1 selected
Menu
1. Option 1
2. Option 2
3. Option 3
0. Quit
Enter choice: 3
Option 3 selected
Menu
1. Option 1
2. Option 2
3. Option 3
0. Quit
Enter choice: 0
End of program
"""

def printMenu():
    print("Menu")
    for i in range(1, 4, 1):
        print("{0}. Option{0}".format(i))
    print("0. Quit")

printMenu()
choice = input("Enter choice: ")

while (choice != "0"):
    print("Option {0} selected".format(choice))
    printMenu()
    choice = input("Enter choice: ")
    
print("End of program")

