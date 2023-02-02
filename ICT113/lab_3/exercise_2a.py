"""
(for loop) Write a program that reads 2 input values: a string and an integer. The
program prints the string a number of times specified by the integer value. For
example,
Input string: hello
Number of times to repeat: 3
hello
hello
hello
"""

string = input("Enter a string: ")
numOfTimes = int(input("Enter an integer: "))

for i in range(0, numOfTimes, 1):
    print(string)