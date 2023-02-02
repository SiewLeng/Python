"""
(while, sentinel) Modify program for 2a so that it repeatedly prompts for another string
to process until the user keys in “exit” to end the program. E.g.,
Enter String: Python
Number of times to repeat: 3
Python
Python
Python
Enter String: program
Number of times to repeat: 2
program
program
Enter String: exit
end
"""

string = input("Enter a string: ")
while (string !="exit"):
    numOfTimesToRepeat = int(input("Number of times to repeat: "))
    for i in range(0, numOfTimesToRepeat, 1):
        print(string)
    string = input("Enter a string: ")
print("End")


